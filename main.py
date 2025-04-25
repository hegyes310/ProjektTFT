import requests
from langfuse.client import Langfuse
import json
import pandas as pd

def kalkulator(dataset_name: str,
    run_id: str,
    output_path: str):
    langfuse_client = Langfuse(
    )
    dataset_run = langfuse_client.get_dataset_run(
        dataset_name=dataset_name, dataset_run_name=run_id
    )

    run_items = []
    index = 0
    count = len(dataset_run.dataset_run_items)
    for run_item in dataset_run.dataset_run_items:
        run_item_dict = {
            "id": run_item.id,
            "dataset_item_id": run_item.dataset_item_id,
            "trace_id": run_item.trace_id,
            "created_at": run_item.created_at,
            "updated_at": run_item.updated_at,
        }
        proba = langfuse_client.get_dataset_item(run_item.dataset_item_id)
        trace = langfuse_client.fetch_trace(id=run_item.trace_id)
        run_item_dict["trace_name"] = trace.data.name
        # Example - Get fields from json input
        run_item_dict["input"] = trace.data.input
        run_item_dict["output"] = trace.data.output
        run_item_dict["expected_output"] = proba.expected_output
        run_item_dict["comment"] = trace.data.scores[0].comment
        run_item_dict["score"] = trace.data.scores[0].value

        # Example - Get fields from json output
        run_items.append(run_item_dict)
        print(f"index: {index}/{count}")
        index += 1

    df = pd.DataFrame(run_items)
    df.to_csv(output_path, index=False, encoding="utf-8", sep=";")


if __name__ == '__main__':
    dataset_name = "Talkabot"
    run_id = "Evaluation_Correctness_sas_v1"
    output_path = f"{run_id}.csv"
    kalkulator(dataset_name, run_id, output_path)
