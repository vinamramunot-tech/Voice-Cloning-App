import os
import torch


def get_latest_checkpoint(checkpoint_folder):
    checkpoints = os.listdir(checkpoint_folder)
    if not checkpoints:
        return None

    latest_checkpoint = checkpoints[0]
    if len(checkpoints) > 1:
        for checkpoint in checkpoints:
            if int(checkpoint.split("_")[1].split(".")[0]) > int(latest_checkpoint.split("_")[1].split(".")[0]):
                latest_checkpoint = checkpoint

    return os.path.join(checkpoint_folder, latest_checkpoint)


def load_checkpoint(checkpoint_path, model, optimizer):
    checkpoint_dict = torch.load(checkpoint_path, map_location="cpu")
    model.load_state_dict(checkpoint_dict["state_dict"])
    optimizer.load_state_dict(checkpoint_dict["optimizer"])
    iteration = checkpoint_dict["iteration"]
    return model, optimizer, iteration


def save_checkpoint(model, optimizer, learning_rate, iteration, filepath):
    torch.save(
        {
            "iteration": iteration,
            "state_dict": model.state_dict(),
            "optimizer": optimizer.state_dict(),
            "learning_rate": learning_rate,
        },
        filepath,
    )
