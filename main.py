import logging

import coloredlogs

from Coach import Coach
from dama.DamaGame import Dama as Game
from dama.pytorch.NNet import NNetWrapper as nn
from dama.pytorch.NNet import args as nnet_args
from utils import *

import wandb

log = logging.getLogger(__name__)

coloredlogs.install(level='INFO')  # Change this to DEBUG to see more info.

args = dotdict({
    'numIters': 1000,
    'numEps': 100,              # Number of complete self-play games to simulate during a new iteration.
    'tempThreshold': 15,        #
    'updateThreshold': 0.6,     # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'maxlenOfQueue': 200000,    # Number of game examples to train the neural networks.
    'numMCTSSims': 200,          # Number of games moves for MCTS to simulate.
    'arenaCompare': 40,         # Number of games to play during arena play to determine if new net will be accepted.
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': True,
    'load_folder_file': ('./temp/', 'checkpoint_17.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

})


def main():
    excluded_keys = {'checkpoint', 'load_model', 'load_folder_file'}
    filtered_args = {k: v for k, v in args.items() if k not in excluded_keys}

    excluded_keys = {'cuda'}
    filtered_nnet_args = {k: v for k, v in nnet_args.items() if k not in excluded_keys}

    wandb.init(
        # set the wandb project where this run will be logged
        project="dama-project",

        # track hyperparameters and run metadata
        config={
            **filtered_args,
            **filtered_nnet_args
        },

        name = "wandb run name"
    )

    log.info('Loading %s...', Game.__name__)
    g = Game(8)

    log.info('Loading %s...', nn.__name__)
    nnet = nn(g)

    if args.load_model:
        log.info('Loading checkpoint "%s/%s"...', args.load_folder_file[0], args.load_folder_file[1])
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])
    else:
        log.warning('Not loading a checkpoint!')

    log.info('Loading the Coach...')
    c = Coach(g, nnet, args)

    if args.load_model:
        log.info("Loading 'trainExamples' from file...")
        c.loadTrainExamples()

    log.info('Starting the learning process 🎉')
    c.learn()

    wandb.finish()


if __name__ == "__main__":
    main()
