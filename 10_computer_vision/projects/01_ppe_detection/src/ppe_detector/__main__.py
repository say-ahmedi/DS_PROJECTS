"""Run project commands with ``python -m ppe_detector``."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .dataset import audit_dataset
from .inspection import make_contact_sheet
from .split import create_split


def main() -> int:
    parser = argparse.ArgumentParser(description="Construction-PPE portfolio workflow")
    sub = parser.add_subparsers(dest="command", required=True)

    audit = sub.add_parser("audit", help="validate images and YOLO labels")
    audit.add_argument("dataset", type=Path)
    audit.add_argument("--output", type=Path, default=Path("artifacts/audit.json"))

    samples = sub.add_parser("samples", help="save ten annotated training images for manual review")
    samples.add_argument("dataset", type=Path)
    samples.add_argument("--output", type=Path, default=Path("artifacts/annotated_samples.jpg"))
    samples.add_argument("--count", type=int, default=10)

    split = sub.add_parser("split", help="reserve supplied validation as final test")
    split.add_argument("dataset", type=Path)
    split.add_argument("--output", type=Path, default=Path("artifacts/split"))
    split.add_argument("--seed", type=int, default=20261104)

    train = sub.add_parser("train", help="fine-tune a small pretrained detector")
    train.add_argument("--config", type=Path, default=Path("artifacts/split/data.yaml"))
    train.add_argument("--runs", type=Path, default=Path("runs"))
    train.add_argument("--weights", default="yolo26n.pt")
    train.add_argument("--epochs", type=int, default=20)
    train.add_argument("--image-size", type=int, default=416)
    train.add_argument("--batch", type=int, default=2)
    train.add_argument("--run-prefix", default="baseline")
    train.add_argument("--allow-cpu", action="store_true")

    evaluate = sub.add_parser("evaluate", help="write detector metrics")
    evaluate.add_argument("weights", type=Path)
    evaluate.add_argument("--config", type=Path, default=Path("artifacts/split/data.yaml"))
    evaluate.add_argument("--split", choices=("val", "test"), default="val")
    evaluate.add_argument("--output", type=Path, default=Path("artifacts/evaluation.json"))
    evaluate.add_argument("--image-size", type=int, default=416)
    evaluate.add_argument("--final-test", action="store_true", help="acknowledge the held-out test evaluation")

    predict = sub.add_parser("predict", help="write detections for one image")
    predict.add_argument("weights", type=Path)
    predict.add_argument("image", type=Path)
    predict.add_argument("--output", type=Path, default=Path("artifacts/prediction.json"))
    predict.add_argument("--image-size", type=int, default=416)

    args = parser.parse_args()
    if args.command == "audit":
        report = audit_dataset(args.dataset)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({key: report[key] for key in ("images", "boxes", "warnings", "errors")}, indent=2))
        return 1 if report["errors"] else 0
    if args.command == "split":
        manifest = create_split(args.dataset, args.output, seed=args.seed)
        print(json.dumps(manifest["counts"], indent=2))
        return 0
    if args.command == "samples":
        paths = make_contact_sheet(args.dataset, args.output, count=args.count)
        print(json.dumps({"contact_sheet": str(args.output), "images": paths}, indent=2))
        return 0
    from .model import evaluate as evaluate_model, predict as predict_model, train as train_model

    if args.command == "train":
        print(train_model(args.config, args.runs, weights=args.weights, epochs=args.epochs,
                          image_size=args.image_size, batch=args.batch, allow_cpu=args.allow_cpu,
                          run_prefix=args.run_prefix))
    elif args.command == "evaluate":
        if args.split == "test" and not args.final_test:
            parser.error("pass --final-test only after model selection is complete")
        print(json.dumps(evaluate_model(args.weights, args.config, args.output,
                                        split=args.split, image_size=args.image_size), indent=2))
    elif args.command == "predict":
        print(json.dumps(predict_model(args.weights, args.image, args.output,
                                       image_size=args.image_size), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

