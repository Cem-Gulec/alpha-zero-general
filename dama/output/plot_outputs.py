import re
import matplotlib.pyplot as plt

data = '''
args = dotdict({
    'numIters': 1000,
    'numEps': 100,              # Number of complete self-play games to simulate during a new iteration.
    'tempThreshold': 15,        #
    'updateThreshold': 0.6,     # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'maxlenOfQueue': 200000,    # Number of game examples to train the neural networks.
    'numMCTSSims': 400,          # Number of games moves for MCTS to simulate.
    'arenaCompare': 40,         # Number of games to play during arena play to determine if new net will be accepted.
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': True,
    'load_folder_file': ('./temp/', 'checkpoint_0.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

})

args = dotdict({
    'lr': 0.001,
    'dropout': 0.3,
    'epochs': 30,
    'batch_size': 64,
    'cuda': torch.cuda.is_available(),
    'num_channels': 512,
})



2024-05-08 08:26:54 DESKTOP-O0AAGL9 __main__[20828] INFO Loading Dama...
2024-05-08 08:26:54 DESKTOP-O0AAGL9 __main__[20828] INFO Loading NNetWrapper...
2024-05-08 08:26:56 DESKTOP-O0AAGL9 __main__[20828] INFO Loading checkpoint "./temp//checkpoint_0.pth.tar"...
2024-05-08 08:26:56 DESKTOP-O0AAGL9 __main__[20828] INFO Loading the Coach...
2024-05-08 08:26:57 DESKTOP-O0AAGL9 __main__[20828] INFO Loading 'trainExamples' from file...
2024-05-08 08:26:57 DESKTOP-O0AAGL9 Coach[20828] INFO File with trainExamples found. Loading it...
2024-05-08 08:26:57 DESKTOP-O0AAGL9 Coach[20828] INFO Loading done!
2024-05-08 08:26:57 DESKTOP-O0AAGL9 __main__[20828] INFO Starting the learning process 🎉
2024-05-08 08:26:57 DESKTOP-O0AAGL9 Coach[20828] INFO Starting Iter #1 ...
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100%|██████████| 85/85 [00:07<00:00, 11.78it/s, Loss_pi=4.76e+00, Loss_v=9.66e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 2
Training Net: 100%|██████████| 85/85 [00:02<00:00, 31.70it/s, Loss_pi=3.84e+00, Loss_v=6.14e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 3
Training Net: 100%|██████████| 85/85 [00:02<00:00, 30.83it/s, Loss_pi=3.38e+00, Loss_v=4.34e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 4
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.10it/s, Loss_pi=2.98e+00, Loss_v=3.47e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 5
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.36it/s, Loss_pi=2.62e+00, Loss_v=2.95e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 6
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.36it/s, Loss_pi=2.33e+00, Loss_v=2.73e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 7
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.41it/s, Loss_pi=2.12e+00, Loss_v=2.33e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 8
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.32it/s, Loss_pi=1.95e+00, Loss_v=1.95e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 9
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.23it/s, Loss_pi=1.78e+00, Loss_v=1.79e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 10
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.20it/s, Loss_pi=1.65e+00, Loss_v=1.74e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 11
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.00it/s, Loss_pi=1.53e+00, Loss_v=1.49e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 12
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.09it/s, Loss_pi=1.41e+00, Loss_v=1.31e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 13
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.09it/s, Loss_pi=1.36e+00, Loss_v=1.25e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 14
Training Net: 100%|██████████| 85/85 [00:02<00:00, 32.15it/s, Loss_pi=1.29e+00, Loss_v=1.10e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 15
Training Net: 100%|██████████| 85/85 [00:02<00:00, 30.98it/s, Loss_pi=1.23e+00, Loss_v=1.09e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 16
Training Net: 100%|██████████| 85/85 [00:02<00:00, 29.26it/s, Loss_pi=1.17e+00, Loss_v=1.21e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 17
Training Net: 100%|██████████| 85/85 [00:02<00:00, 31.94it/s, Loss_pi=1.13e+00, Loss_v=1.12e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 18
Training Net: 100%|██████████| 85/85 [00:02<00:00, 31.96it/s, Loss_pi=1.11e+00, Loss_v=1.03e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 19
Training Net: 100%|██████████| 85/85 [00:02<00:00, 31.67it/s, Loss_pi=1.10e+00, Loss_v=1.06e-01]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 20
Training Net: 100%|██████████| 85/85 [00:02<00:00, 29.70it/s, Loss_pi=9.92e-01, Loss_v=9.24e-02]
EPOCH ::: 21
Training Net: 100%|██████████| 85/85 [00:02<00:00, 30.23it/s, Loss_pi=9.98e-01, Loss_v=9.88e-02]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 22
Training Net: 100%|██████████| 85/85 [00:02<00:00, 30.56it/s, Loss_pi=9.97e-01, Loss_v=9.36e-02]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 23
Training Net: 100%|██████████| 85/85 [00:02<00:00, 31.04it/s, Loss_pi=9.61e-01, Loss_v=8.92e-02]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 24
Training Net: 100%|██████████| 85/85 [00:02<00:00, 30.42it/s, Loss_pi=9.43e-01, Loss_v=7.58e-02]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 25
Training Net: 100%|██████████| 85/85 [00:02<00:00, 28.85it/s, Loss_pi=9.22e-01, Loss_v=9.34e-02]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 26
Training Net: 100%|██████████| 85/85 [00:02<00:00, 28.58it/s, Loss_pi=9.33e-01, Loss_v=8.71e-02]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 27
Training Net: 100%|██████████| 85/85 [00:03<00:00, 28.03it/s, Loss_pi=9.41e-01, Loss_v=7.46e-02]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 28
Training Net: 100%|██████████| 85/85 [00:02<00:00, 30.30it/s, Loss_pi=8.84e-01, Loss_v=7.49e-02]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 29
Training Net: 100%|██████████| 85/85 [00:02<00:00, 30.64it/s, Loss_pi=8.91e-01, Loss_v=7.18e-02]
Training Net:   0%|          | 0/85 [00:00<?, ?it/s]EPOCH ::: 30
Training Net: 100%|██████████| 85/85 [00:02<00:00, 30.02it/s, Loss_pi=8.91e-01, Loss_v=8.84e-02]
2024-05-08 08:28:25 DESKTOP-O0AAGL9 Coach[20828] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100%|██████████| 20/20 [27:24<00:00, 82.23s/it]
Arena.playGames (2): 100%|██████████| 20/20 [28:04<00:00, 84.21s/it]
2024-05-08 09:23:54 DESKTOP-O0AAGL9 Coach[20828] INFO NEW/PREV WINS : 22 / 15 ; DRAWS : 3
2024-05-08 09:23:54 DESKTOP-O0AAGL9 Coach[20828] INFO REJECTING NEW MODEL
2024-05-08 09:23:54 DESKTOP-O0AAGL9 Coach[20828] INFO Starting Iter #2 ...
Self Play: 100%|██████████| 100/100 [2:13:35<00:00, 80.16s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100%|██████████| 170/170 [00:11<00:00, 15.28it/s, Loss_pi=4.36e+00, Loss_v=1.01e+00]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 2
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.37it/s, Loss_pi=3.38e+00, Loss_v=7.23e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 3
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.40it/s, Loss_pi=2.88e+00, Loss_v=5.58e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 4
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.39it/s, Loss_pi=2.56e+00, Loss_v=4.40e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 5
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.21it/s, Loss_pi=2.30e+00, Loss_v=3.46e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 6
Training Net: 100%|██████████| 170/170 [00:05<00:00, 31.58it/s, Loss_pi=2.09e+00, Loss_v=2.82e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 7
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.11it/s, Loss_pi=1.90e+00, Loss_v=2.47e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 8
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.36it/s, Loss_pi=1.76e+00, Loss_v=2.25e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 9
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.34it/s, Loss_pi=1.65e+00, Loss_v=2.13e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 10
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.51it/s, Loss_pi=1.55e+00, Loss_v=1.69e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 11
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.46it/s, Loss_pi=1.44e+00, Loss_v=1.57e-01]
EPOCH ::: 12
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.51it/s, Loss_pi=1.34e+00, Loss_v=1.41e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 13
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.51it/s, Loss_pi=1.30e+00, Loss_v=1.50e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 14
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.50it/s, Loss_pi=1.23e+00, Loss_v=1.39e-01]
EPOCH ::: 15
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.46it/s, Loss_pi=1.19e+00, Loss_v=1.31e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 16
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.34it/s, Loss_pi=1.16e+00, Loss_v=1.30e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 17
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.25it/s, Loss_pi=1.12e+00, Loss_v=1.14e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 18
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.17it/s, Loss_pi=1.11e+00, Loss_v=1.31e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 19
Training Net: 100%|██████████| 170/170 [00:05<00:00, 31.84it/s, Loss_pi=1.06e+00, Loss_v=1.10e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 20
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.07it/s, Loss_pi=1.01e+00, Loss_v=1.03e-01]
EPOCH ::: 21
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.08it/s, Loss_pi=1.03e+00, Loss_v=1.06e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 22
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.14it/s, Loss_pi=1.00e+00, Loss_v=1.03e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s, Loss_pi=7.83e-01, Loss_v=7.02e-02]EPOCH ::: 23
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.13it/s, Loss_pi=9.70e-01, Loss_v=9.69e-02]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 24
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.17it/s, Loss_pi=9.48e-01, Loss_v=1.06e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 25
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.07it/s, Loss_pi=9.56e-01, Loss_v=1.02e-01]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 26
Training Net: 100%|██████████| 170/170 [00:05<00:00, 32.10it/s, Loss_pi=9.79e-01, Loss_v=9.93e-02]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 27
Training Net: 100%|██████████| 170/170 [00:05<00:00, 31.97it/s, Loss_pi=9.30e-01, Loss_v=8.17e-02]
EPOCH ::: 28
Training Net: 100%|██████████| 170/170 [00:05<00:00, 31.66it/s, Loss_pi=9.54e-01, Loss_v=9.10e-02]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 29
Training Net: 100%|██████████| 170/170 [00:05<00:00, 31.91it/s, Loss_pi=9.62e-01, Loss_v=9.74e-02]
Training Net:   0%|          | 0/170 [00:00<?, ?it/s]EPOCH ::: 30
Training Net: 100%|██████████| 170/170 [00:05<00:00, 31.95it/s, Loss_pi=9.07e-01, Loss_v=8.64e-02]
2024-05-08 22:05:11 DESKTOP-O0AAGL9 Coach[1592] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100%|██████████| 20/20 [33:23<00:00, 100.17s/it]
Arena.playGames (2): 100%|██████████| 20/20 [40:49<00:00, 122.46s/it]
Checkpoint Directory exists! 
2024-05-08 23:19:24 DESKTOP-O0AAGL9 Coach[1592] INFO NEW/PREV WINS : 26 / 14 ; DRAWS : 0
2024-05-08 23:19:24 DESKTOP-O0AAGL9 Coach[1592] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
2024-05-08 23:19:24 DESKTOP-O0AAGL9 Coach[1592] INFO Starting Iter #2 ...
Self Play: 100%|██████████| 100/100 [5:24:56<00:00, 194.96s/it]
Checkpoint Directory exists! 
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 1
Training Net: 100%|██████████| 280/280 [00:12<00:00, 22.69it/s, Loss_pi=1.61e+00, Loss_v=3.73e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 2
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.14it/s, Loss_pi=1.28e+00, Loss_v=2.22e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 3
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.21it/s, Loss_pi=1.11e+00, Loss_v=1.75e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 4
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.23it/s, Loss_pi=1.01e+00, Loss_v=1.44e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 5
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.22it/s, Loss_pi=9.14e-01, Loss_v=1.33e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 6
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.21it/s, Loss_pi=8.67e-01, Loss_v=1.19e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 7
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.13it/s, Loss_pi=8.65e-01, Loss_v=1.23e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 8
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.21it/s, Loss_pi=8.40e-01, Loss_v=1.20e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 9
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.17it/s, Loss_pi=8.01e-01, Loss_v=1.12e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 10
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.26it/s, Loss_pi=7.68e-01, Loss_v=1.07e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 11
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.25it/s, Loss_pi=7.51e-01, Loss_v=1.04e-01]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 12
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.26it/s, Loss_pi=7.37e-01, Loss_v=9.58e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 13
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.19it/s, Loss_pi=7.38e-01, Loss_v=9.19e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 14
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.22it/s, Loss_pi=7.28e-01, Loss_v=9.42e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 15
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.21it/s, Loss_pi=7.33e-01, Loss_v=8.92e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 16
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.28it/s, Loss_pi=7.31e-01, Loss_v=9.78e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 17
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.20it/s, Loss_pi=7.31e-01, Loss_v=8.63e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 18
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.20it/s, Loss_pi=7.07e-01, Loss_v=8.70e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 19
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.18it/s, Loss_pi=6.97e-01, Loss_v=8.81e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 20
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.21it/s, Loss_pi=6.97e-01, Loss_v=8.02e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 21
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.17it/s, Loss_pi=6.89e-01, Loss_v=8.43e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 22
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.23it/s, Loss_pi=6.92e-01, Loss_v=9.08e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 23
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.23it/s, Loss_pi=6.89e-01, Loss_v=8.08e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 24
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.23it/s, Loss_pi=6.92e-01, Loss_v=8.28e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 25
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.24it/s, Loss_pi=6.72e-01, Loss_v=7.88e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 26
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.23it/s, Loss_pi=6.70e-01, Loss_v=7.70e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 27
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.14it/s, Loss_pi=6.71e-01, Loss_v=8.56e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 28
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.13it/s, Loss_pi=6.57e-01, Loss_v=7.69e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 29
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.21it/s, Loss_pi=6.58e-01, Loss_v=7.74e-02]
Training Net:   0%|          | 0/280 [00:00<?, ?it/s]EPOCH ::: 30
Training Net: 100%|██████████| 280/280 [00:12<00:00, 23.14it/s, Loss_pi=6.47e-01, Loss_v=7.51e-02]
2024-05-09 04:56:17 DESKTOP-O0AAGL9 Coach[1592] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100%|██████████| 20/20 [51:36<00:00, 154.84s/it]
Arena.playGames (2): 100%|██████████| 20/20 [1:07:29<00:00, 202.47s/it]
Checkpoint Directory exists! 
2024-05-09 06:55:24 DESKTOP-O0AAGL9 Coach[1592] INFO NEW/PREV WINS : 23 / 12 ; DRAWS : 5
2024-05-09 06:55:24 DESKTOP-O0AAGL9 Coach[1592] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
2024-05-09 06:55:24 DESKTOP-O0AAGL9 Coach[1592] INFO Starting Iter #3 ...
Self Play: 100%|██████████| 100/100 [10:10:43<00:00, 366.43s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.08it/s, Loss_pi=1.16e+00, Loss_v=2.54e-01]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 2
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.66it/s, Loss_pi=8.91e-01, Loss_v=1.64e-01]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 3
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.60it/s, Loss_pi=7.67e-01, Loss_v=1.30e-01]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 4
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.52it/s, Loss_pi=6.91e-01, Loss_v=1.09e-01]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 5
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.51it/s, Loss_pi=6.59e-01, Loss_v=1.01e-01]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 6
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.57it/s, Loss_pi=6.42e-01, Loss_v=9.30e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 7
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.51it/s, Loss_pi=6.27e-01, Loss_v=9.02e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 8
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.43it/s, Loss_pi=6.11e-01, Loss_v=8.97e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 9
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.33it/s, Loss_pi=6.06e-01, Loss_v=8.38e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 10
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.23it/s, Loss_pi=6.04e-01, Loss_v=8.43e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 11
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.42it/s, Loss_pi=6.03e-01, Loss_v=7.62e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 12
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.50it/s, Loss_pi=5.91e-01, Loss_v=7.69e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 13
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.38it/s, Loss_pi=5.64e-01, Loss_v=7.95e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 14
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.48it/s, Loss_pi=5.72e-01, Loss_v=7.76e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 15
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.22it/s, Loss_pi=5.73e-01, Loss_v=7.82e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 16
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.39it/s, Loss_pi=5.73e-01, Loss_v=7.66e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 17
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.41it/s, Loss_pi=5.56e-01, Loss_v=7.61e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 18
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.43it/s, Loss_pi=5.55e-01, Loss_v=7.58e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 19
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.36it/s, Loss_pi=5.66e-01, Loss_v=7.09e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 20
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.45it/s, Loss_pi=5.72e-01, Loss_v=7.52e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 21
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.31it/s, Loss_pi=5.52e-01, Loss_v=7.35e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 22
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.34it/s, Loss_pi=5.49e-01, Loss_v=6.92e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 23
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.00it/s, Loss_pi=5.47e-01, Loss_v=7.43e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 24
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.29it/s, Loss_pi=5.42e-01, Loss_v=7.05e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 25
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.21it/s, Loss_pi=5.45e-01, Loss_v=7.50e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 26
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.48it/s, Loss_pi=5.52e-01, Loss_v=6.95e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 27
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.27it/s, Loss_pi=5.33e-01, Loss_v=6.59e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 28
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.18it/s, Loss_pi=5.51e-01, Loss_v=6.86e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 29
Training Net: 100%|██████████| 395/395 [00:17<00:00, 21.95it/s, Loss_pi=5.52e-01, Loss_v=6.88e-02]
Training Net:   0%|          | 0/395 [00:00<?, ?it/s]EPOCH ::: 30
Training Net: 100%|██████████| 395/395 [00:17<00:00, 22.32it/s, Loss_pi=5.35e-01, Loss_v=6.83e-02]
2024-05-09 17:31:16 DESKTOP-O0AAGL9 Coach[1592] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100%|██████████| 20/20 [1:21:46<00:00, 245.31s/it]
Arena.playGames (2): 100%|██████████| 20/20 [1:43:14<00:00, 309.71s/it]
2024-05-09 20:36:16 DESKTOP-O0AAGL9 Coach[1592] INFO NEW/PREV WINS : 19 / 16 ; DRAWS : 5
2024-05-09 20:36:16 DESKTOP-O0AAGL9 Coach[1592] INFO REJECTING NEW MODEL
2024-05-09 20:36:16 DESKTOP-O0AAGL9 Coach[1592] INFO Starting Iter #4 ...
Self Play: 100%|██████████| 100/100 [10:40:25<00:00, 384.25s/it]



2024-05-12 14:46:17 0e1cec8e8708 __main__[48618] INFO Loading Dama...
2024-05-12 14:46:17 0e1cec8e8708 __main__[48618] INFO Loading NNetWrapper...
2024-05-12 14:46:17 0e1cec8e8708 __main__[48618] INFO Loading checkpoint "./temp//checkpoint_3.pth.tar"...
2024-05-12 14:46:18 0e1cec8e8708 __main__[48618] INFO Loading the Coach...
2024-05-12 14:46:18 0e1cec8e8708 __main__[48618] INFO Loading 'trainExamples' from file...
2024-05-12 14:46:18 0e1cec8e8708 Coach[48618] INFO File with trainExamples found. Loading it...
2024-05-12 14:46:24 0e1cec8e8708 Coach[48618] INFO Loading done!
2024-05-12 14:46:24 0e1cec8e8708 __main__[48618] INFO Starting the learning process 🎉
2024-05-12 14:46:24 0e1cec8e8708 Coach[48618] INFO Starting Iter #1 ...
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 512/512 [00:14<00:00, 36.17it/s, Loss_pi=4.82e-01, Loss_v=6.89e-02]
EPOCH ::: 2
Training Net: 100% 512/512 [00:12<00:00, 42.17it/s, Loss_pi=4.96e-01, Loss_v=6.88e-02]
EPOCH ::: 3
Training Net: 100% 512/512 [00:12<00:00, 42.16it/s, Loss_pi=4.92e-01, Loss_v=7.62e-02]
EPOCH ::: 4
Training Net: 100% 512/512 [00:11<00:00, 42.86it/s, Loss_pi=4.88e-01, Loss_v=7.09e-02]
EPOCH ::: 5
Training Net: 100% 512/512 [00:12<00:00, 42.48it/s, Loss_pi=4.79e-01, Loss_v=7.33e-02]
EPOCH ::: 6
Training Net: 100% 512/512 [00:11<00:00, 42.72it/s, Loss_pi=4.90e-01, Loss_v=7.28e-02]
EPOCH ::: 7
Training Net: 100% 512/512 [00:12<00:00, 42.40it/s, Loss_pi=4.88e-01, Loss_v=7.45e-02]
EPOCH ::: 8
Training Net: 100% 512/512 [00:12<00:00, 42.11it/s, Loss_pi=4.87e-01, Loss_v=7.44e-02]
EPOCH ::: 9
Training Net: 100% 512/512 [00:11<00:00, 42.98it/s, Loss_pi=4.76e-01, Loss_v=7.29e-02]
EPOCH ::: 10
Training Net: 100% 512/512 [00:11<00:00, 43.42it/s, Loss_pi=4.90e-01, Loss_v=6.84e-02]
EPOCH ::: 11
Training Net: 100% 512/512 [00:12<00:00, 42.59it/s, Loss_pi=4.70e-01, Loss_v=6.78e-02]
EPOCH ::: 12
Training Net: 100% 512/512 [00:11<00:00, 42.94it/s, Loss_pi=4.78e-01, Loss_v=6.70e-02]
EPOCH ::: 13
Training Net: 100% 512/512 [00:12<00:00, 42.34it/s, Loss_pi=4.79e-01, Loss_v=6.83e-02]
EPOCH ::: 14
Training Net: 100% 512/512 [00:12<00:00, 42.11it/s, Loss_pi=4.66e-01, Loss_v=6.86e-02]
EPOCH ::: 15
Training Net: 100% 512/512 [00:12<00:00, 42.36it/s, Loss_pi=4.73e-01, Loss_v=6.81e-02]
EPOCH ::: 16
Training Net: 100% 512/512 [00:11<00:00, 42.73it/s, Loss_pi=4.87e-01, Loss_v=7.26e-02]
EPOCH ::: 17
Training Net: 100% 512/512 [00:12<00:00, 42.46it/s, Loss_pi=4.65e-01, Loss_v=6.49e-02]
EPOCH ::: 18
Training Net: 100% 512/512 [00:12<00:00, 42.45it/s, Loss_pi=4.65e-01, Loss_v=6.38e-02]
EPOCH ::: 19
Training Net: 100% 512/512 [00:12<00:00, 42.63it/s, Loss_pi=4.62e-01, Loss_v=6.54e-02]
EPOCH ::: 20
Training Net: 100% 512/512 [00:12<00:00, 42.42it/s, Loss_pi=4.64e-01, Loss_v=7.31e-02]
EPOCH ::: 21
Training Net: 100% 512/512 [00:12<00:00, 42.43it/s, Loss_pi=4.65e-01, Loss_v=6.68e-02]
EPOCH ::: 22
Training Net: 100% 512/512 [00:12<00:00, 42.45it/s, Loss_pi=4.67e-01, Loss_v=6.56e-02]
EPOCH ::: 23
Training Net: 100% 512/512 [00:12<00:00, 42.28it/s, Loss_pi=4.63e-01, Loss_v=6.75e-02]
EPOCH ::: 24
Training Net: 100% 512/512 [00:11<00:00, 42.94it/s, Loss_pi=4.71e-01, Loss_v=6.60e-02]
EPOCH ::: 25
Training Net: 100% 512/512 [00:11<00:00, 42.78it/s, Loss_pi=4.46e-01, Loss_v=6.47e-02]
EPOCH ::: 26
Training Net: 100% 512/512 [00:12<00:00, 42.33it/s, Loss_pi=4.57e-01, Loss_v=6.26e-02]
EPOCH ::: 27
Training Net: 100% 512/512 [00:12<00:00, 42.14it/s, Loss_pi=4.65e-01, Loss_v=6.77e-02]
EPOCH ::: 28
Training Net: 100% 512/512 [00:12<00:00, 42.17it/s, Loss_pi=4.67e-01, Loss_v=6.61e-02]
EPOCH ::: 29
Training Net: 100% 512/512 [00:12<00:00, 42.41it/s, Loss_pi=4.63e-01, Loss_v=6.34e-02]
EPOCH ::: 30
Training Net: 100% 512/512 [00:12<00:00, 42.49it/s, Loss_pi=4.61e-01, Loss_v=6.60e-02]
2024-05-12 14:52:37 0e1cec8e8708 Coach[48618] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [30:13<00:00, 90.69s/it] 
Arena.playGames (2): 100% 20/20 [27:54<00:00, 83.74s/it]
2024-05-12 15:50:46 0e1cec8e8708 Coach[48618] INFO NEW/PREV WINS : 18 / 17 ; DRAWS : 5
2024-05-12 15:50:46 0e1cec8e8708 Coach[48618] INFO REJECTING NEW MODEL
2024-05-12 15:50:46 0e1cec8e8708 Coach[48618] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [3:15:49<00:00, 117.49s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 635/635 [00:18<00:00, 34.91it/s, Loss_pi=8.40e-01, Loss_v=1.72e-01]
EPOCH ::: 2
Training Net: 100% 635/635 [00:16<00:00, 38.42it/s, Loss_pi=6.61e-01, Loss_v=1.22e-01]
EPOCH ::: 3
Training Net: 100% 635/635 [00:16<00:00, 39.22it/s, Loss_pi=5.85e-01, Loss_v=1.07e-01]
EPOCH ::: 4
Training Net: 100% 635/635 [00:16<00:00, 38.47it/s, Loss_pi=5.46e-01, Loss_v=9.24e-02]
EPOCH ::: 5
Training Net: 100% 635/635 [00:16<00:00, 38.72it/s, Loss_pi=5.04e-01, Loss_v=8.66e-02]
EPOCH ::: 6
Training Net: 100% 635/635 [00:16<00:00, 38.76it/s, Loss_pi=5.11e-01, Loss_v=8.32e-02]
EPOCH ::: 7
Training Net: 100% 635/635 [00:16<00:00, 38.22it/s, Loss_pi=4.95e-01, Loss_v=8.13e-02]
EPOCH ::: 8
Training Net: 100% 635/635 [00:16<00:00, 38.51it/s, Loss_pi=4.92e-01, Loss_v=7.69e-02]
EPOCH ::: 9
Training Net: 100% 635/635 [00:16<00:00, 38.84it/s, Loss_pi=4.88e-01, Loss_v=7.66e-02]
EPOCH ::: 10
Training Net: 100% 635/635 [00:16<00:00, 38.79it/s, Loss_pi=4.91e-01, Loss_v=7.68e-02]
EPOCH ::: 11
Training Net: 100% 635/635 [00:15<00:00, 39.79it/s, Loss_pi=4.61e-01, Loss_v=7.17e-02]
EPOCH ::: 12
Training Net: 100% 635/635 [00:16<00:00, 39.30it/s, Loss_pi=4.77e-01, Loss_v=7.44e-02]
EPOCH ::: 13
Training Net: 100% 635/635 [00:16<00:00, 39.13it/s, Loss_pi=4.64e-01, Loss_v=7.06e-02]
EPOCH ::: 14
Training Net: 100% 635/635 [00:16<00:00, 38.67it/s, Loss_pi=4.69e-01, Loss_v=7.09e-02]
EPOCH ::: 15
Training Net: 100% 635/635 [00:16<00:00, 38.93it/s, Loss_pi=4.78e-01, Loss_v=7.01e-02]
EPOCH ::: 16
Training Net: 100% 635/635 [00:16<00:00, 38.63it/s, Loss_pi=4.66e-01, Loss_v=6.99e-02]
EPOCH ::: 17
Training Net: 100% 635/635 [00:16<00:00, 39.20it/s, Loss_pi=4.64e-01, Loss_v=7.03e-02]
EPOCH ::: 18
Training Net: 100% 635/635 [00:16<00:00, 39.10it/s, Loss_pi=4.56e-01, Loss_v=6.78e-02]
EPOCH ::: 19
Training Net: 100% 635/635 [00:16<00:00, 39.13it/s, Loss_pi=4.55e-01, Loss_v=6.86e-02]
EPOCH ::: 20
Training Net: 100% 635/635 [00:16<00:00, 39.45it/s, Loss_pi=4.62e-01, Loss_v=6.94e-02]
EPOCH ::: 21
Training Net: 100% 635/635 [00:16<00:00, 39.11it/s, Loss_pi=4.60e-01, Loss_v=7.02e-02]
EPOCH ::: 22
Training Net: 100% 635/635 [00:16<00:00, 39.08it/s, Loss_pi=4.47e-01, Loss_v=6.62e-02]
EPOCH ::: 23
Training Net: 100% 635/635 [00:16<00:00, 39.45it/s, Loss_pi=4.51e-01, Loss_v=6.67e-02]
EPOCH ::: 24
Training Net: 100% 635/635 [00:16<00:00, 39.28it/s, Loss_pi=4.45e-01, Loss_v=6.29e-02]
EPOCH ::: 25
Training Net: 100% 635/635 [00:16<00:00, 39.17it/s, Loss_pi=4.40e-01, Loss_v=6.51e-02]
EPOCH ::: 26
Training Net: 100% 635/635 [00:16<00:00, 39.64it/s, Loss_pi=4.45e-01, Loss_v=6.64e-02]
EPOCH ::: 27
Training Net: 100% 635/635 [00:16<00:00, 38.48it/s, Loss_pi=4.50e-01, Loss_v=6.71e-02]
EPOCH ::: 28
Training Net: 100% 635/635 [00:16<00:00, 39.08it/s, Loss_pi=4.42e-01, Loss_v=6.51e-02]
EPOCH ::: 29
Training Net: 100% 635/635 [00:16<00:00, 39.55it/s, Loss_pi=4.42e-01, Loss_v=6.31e-02]
EPOCH ::: 30
Training Net: 100% 635/635 [00:16<00:00, 39.16it/s, Loss_pi=4.37e-01, Loss_v=6.56e-02]
2024-05-12 19:14:53 0e1cec8e8708 Coach[48618] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [33:36<00:00, 100.81s/it]
Arena.playGames (2): 100% 20/20 [31:08<00:00, 93.43s/it]
2024-05-12 20:19:38 0e1cec8e8708 Coach[48618] INFO NEW/PREV WINS : 16 / 13 ; DRAWS : 11
2024-05-12 20:19:38 0e1cec8e8708 Coach[48618] INFO REJECTING NEW MODEL
2024-05-12 20:19:38 0e1cec8e8708 Coach[48618] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [3:16:19<00:00, 117.80s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 756/756 [00:22<00:00, 33.81it/s, Loss_pi=1.04e+00, Loss_v=2.38e-01]
EPOCH ::: 2
Training Net: 100% 756/756 [00:20<00:00, 36.89it/s, Loss_pi=7.79e-01, Loss_v=1.72e-01]
EPOCH ::: 3
Training Net: 100% 756/756 [00:20<00:00, 36.72it/s, Loss_pi=6.48e-01, Loss_v=1.36e-01]
EPOCH ::: 4
Training Net: 100% 756/756 [00:20<00:00, 36.01it/s, Loss_pi=5.97e-01, Loss_v=1.18e-01]
EPOCH ::: 5
Training Net: 100% 756/756 [00:21<00:00, 35.91it/s, Loss_pi=5.49e-01, Loss_v=1.04e-01]
EPOCH ::: 6
Training Net: 100% 756/756 [00:20<00:00, 36.12it/s, Loss_pi=5.27e-01, Loss_v=9.77e-02]
EPOCH ::: 7
Training Net: 100% 756/756 [00:20<00:00, 36.24it/s, Loss_pi=5.13e-01, Loss_v=9.28e-02]
EPOCH ::: 8
Training Net: 100% 756/756 [00:20<00:00, 36.64it/s, Loss_pi=5.06e-01, Loss_v=8.88e-02]
EPOCH ::: 9
Training Net: 100% 756/756 [00:20<00:00, 36.32it/s, Loss_pi=4.92e-01, Loss_v=8.57e-02]
EPOCH ::: 10
Training Net: 100% 756/756 [00:20<00:00, 36.08it/s, Loss_pi=4.78e-01, Loss_v=8.28e-02]
EPOCH ::: 11
Training Net: 100% 756/756 [00:20<00:00, 36.67it/s, Loss_pi=4.77e-01, Loss_v=7.87e-02]
EPOCH ::: 12
Training Net: 100% 756/756 [00:20<00:00, 36.31it/s, Loss_pi=4.69e-01, Loss_v=7.76e-02]
EPOCH ::: 13
Training Net: 100% 756/756 [00:20<00:00, 36.91it/s, Loss_pi=4.72e-01, Loss_v=7.56e-02]
EPOCH ::: 14
Training Net: 100% 756/756 [00:20<00:00, 37.05it/s, Loss_pi=4.60e-01, Loss_v=7.72e-02]
EPOCH ::: 15
Training Net: 100% 756/756 [00:20<00:00, 36.97it/s, Loss_pi=4.52e-01, Loss_v=7.80e-02]
EPOCH ::: 16
Training Net: 100% 756/756 [00:20<00:00, 37.11it/s, Loss_pi=4.61e-01, Loss_v=7.66e-02]
EPOCH ::: 17
Training Net: 100% 756/756 [00:20<00:00, 37.18it/s, Loss_pi=4.50e-01, Loss_v=7.44e-02]
EPOCH ::: 18
Training Net: 100% 756/756 [00:20<00:00, 36.63it/s, Loss_pi=4.49e-01, Loss_v=7.22e-02]
EPOCH ::: 19
Training Net: 100% 756/756 [00:20<00:00, 37.13it/s, Loss_pi=4.43e-01, Loss_v=7.16e-02]
EPOCH ::: 20
Training Net: 100% 756/756 [00:20<00:00, 36.70it/s, Loss_pi=4.38e-01, Loss_v=7.12e-02]
EPOCH ::: 21
Training Net: 100% 756/756 [00:20<00:00, 37.01it/s, Loss_pi=4.45e-01, Loss_v=7.29e-02]
EPOCH ::: 22
Training Net: 100% 756/756 [00:20<00:00, 37.24it/s, Loss_pi=4.46e-01, Loss_v=7.03e-02]
EPOCH ::: 23
Training Net: 100% 756/756 [00:20<00:00, 37.18it/s, Loss_pi=4.37e-01, Loss_v=6.80e-02]
EPOCH ::: 24
Training Net: 100% 756/756 [00:20<00:00, 36.99it/s, Loss_pi=4.28e-01, Loss_v=6.90e-02]
EPOCH ::: 25
Training Net: 100% 756/756 [00:20<00:00, 37.10it/s, Loss_pi=4.44e-01, Loss_v=7.33e-02]
EPOCH ::: 26
Training Net: 100% 756/756 [00:20<00:00, 36.82it/s, Loss_pi=4.24e-01, Loss_v=6.65e-02]
EPOCH ::: 27
Training Net: 100% 756/756 [00:20<00:00, 36.94it/s, Loss_pi=4.38e-01, Loss_v=6.68e-02]
EPOCH ::: 28
Training Net: 100% 756/756 [00:20<00:00, 37.15it/s, Loss_pi=4.20e-01, Loss_v=6.76e-02]
EPOCH ::: 29
Training Net: 100% 756/756 [00:20<00:00, 37.18it/s, Loss_pi=4.34e-01, Loss_v=6.78e-02]
EPOCH ::: 30
Training Net: 100% 756/756 [00:20<00:00, 37.03it/s, Loss_pi=4.31e-01, Loss_v=6.60e-02]
2024-05-12 23:46:24 0e1cec8e8708 Coach[48618] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [31:17<00:00, 93.88s/it]
Arena.playGames (2): 100% 20/20 [29:07<00:00, 87.36s/it]
2024-05-13 00:46:49 0e1cec8e8708 Coach[48618] INFO NEW/PREV WINS : 16 / 13 ; DRAWS : 11
2024-05-13 00:46:49 0e1cec8e8708 Coach[48618] INFO REJECTING NEW MODEL
2024-05-13 00:46:49 0e1cec8e8708 Coach[48618] INFO Starting Iter #4 ...
Self Play: 100% 100/100 [3:13:40<00:00, 116.21s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 874/874 [00:26<00:00, 33.61it/s, Loss_pi=1.18e+00, Loss_v=2.93e-01]
EPOCH ::: 2
Training Net: 100% 874/874 [00:24<00:00, 36.34it/s, Loss_pi=8.46e-01, Loss_v=2.01e-01]
EPOCH ::: 3
Training Net: 100% 874/874 [00:23<00:00, 36.68it/s, Loss_pi=7.11e-01, Loss_v=1.55e-01]
EPOCH ::: 4
Training Net: 100% 874/874 [00:23<00:00, 37.01it/s, Loss_pi=6.32e-01, Loss_v=1.33e-01]
EPOCH ::: 5
Training Net: 100% 874/874 [00:23<00:00, 36.75it/s, Loss_pi=5.82e-01, Loss_v=1.18e-01]
EPOCH ::: 6
Training Net: 100% 874/874 [00:23<00:00, 36.54it/s, Loss_pi=5.51e-01, Loss_v=1.08e-01]
EPOCH ::: 7
Training Net: 100% 874/874 [00:23<00:00, 36.46it/s, Loss_pi=5.24e-01, Loss_v=1.01e-01]
EPOCH ::: 8
Training Net: 100% 874/874 [00:23<00:00, 36.67it/s, Loss_pi=5.09e-01, Loss_v=9.75e-02]
EPOCH ::: 9
Training Net: 100% 874/874 [00:23<00:00, 36.81it/s, Loss_pi=4.98e-01, Loss_v=9.12e-02]
EPOCH ::: 10
Training Net: 100% 874/874 [00:23<00:00, 36.74it/s, Loss_pi=4.83e-01, Loss_v=8.85e-02]
EPOCH ::: 11
Training Net: 100% 874/874 [00:24<00:00, 36.15it/s, Loss_pi=4.71e-01, Loss_v=8.40e-02]
EPOCH ::: 12
Training Net: 100% 874/874 [00:23<00:00, 36.98it/s, Loss_pi=4.75e-01, Loss_v=8.57e-02]
EPOCH ::: 13
Training Net: 100% 874/874 [00:23<00:00, 36.92it/s, Loss_pi=4.59e-01, Loss_v=8.15e-02]
EPOCH ::: 14
Training Net: 100% 874/874 [00:23<00:00, 36.84it/s, Loss_pi=4.59e-01, Loss_v=8.12e-02]
EPOCH ::: 15
Training Net: 100% 874/874 [00:23<00:00, 36.92it/s, Loss_pi=4.60e-01, Loss_v=8.09e-02]
EPOCH ::: 16
Training Net: 100% 874/874 [00:23<00:00, 36.99it/s, Loss_pi=4.53e-01, Loss_v=8.27e-02]
EPOCH ::: 17
Training Net: 100% 874/874 [00:23<00:00, 36.83it/s, Loss_pi=4.42e-01, Loss_v=7.84e-02]
EPOCH ::: 18
Training Net: 100% 874/874 [00:23<00:00, 37.17it/s, Loss_pi=4.44e-01, Loss_v=7.60e-02]
EPOCH ::: 19
Training Net: 100% 874/874 [00:23<00:00, 37.00it/s, Loss_pi=4.31e-01, Loss_v=7.39e-02]
EPOCH ::: 20
Training Net: 100% 874/874 [00:23<00:00, 37.34it/s, Loss_pi=4.38e-01, Loss_v=7.49e-02]
EPOCH ::: 21
Training Net: 100% 874/874 [00:23<00:00, 37.24it/s, Loss_pi=4.40e-01, Loss_v=7.48e-02]
EPOCH ::: 22
Training Net: 100% 874/874 [00:23<00:00, 37.30it/s, Loss_pi=4.33e-01, Loss_v=7.22e-02]
EPOCH ::: 23
Training Net: 100% 874/874 [00:23<00:00, 37.02it/s, Loss_pi=4.25e-01, Loss_v=7.20e-02]
EPOCH ::: 24
Training Net: 100% 874/874 [00:23<00:00, 36.58it/s, Loss_pi=4.20e-01, Loss_v=7.19e-02]
EPOCH ::: 25
Training Net: 100% 874/874 [00:23<00:00, 37.46it/s, Loss_pi=4.25e-01, Loss_v=7.26e-02]
EPOCH ::: 26
Training Net: 100% 874/874 [00:23<00:00, 36.60it/s, Loss_pi=4.30e-01, Loss_v=7.32e-02]
EPOCH ::: 27
Training Net: 100% 874/874 [00:23<00:00, 37.45it/s, Loss_pi=4.18e-01, Loss_v=7.16e-02]
EPOCH ::: 28
Training Net: 100% 874/874 [00:23<00:00, 37.64it/s, Loss_pi=4.16e-01, Loss_v=7.22e-02]
EPOCH ::: 29
Training Net: 100% 874/874 [00:23<00:00, 37.02it/s, Loss_pi=4.17e-01, Loss_v=7.20e-02]
EPOCH ::: 30
Training Net: 100% 874/874 [00:23<00:00, 36.89it/s, Loss_pi=4.10e-01, Loss_v=6.92e-02]
2024-05-13 04:12:34 0e1cec8e8708 Coach[48618] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [32:20<00:00, 97.04s/it] 
Arena.playGames (2): 100% 20/20 [36:34<00:00, 109.73s/it]
2024-05-13 05:21:29 0e1cec8e8708 Coach[48618] INFO NEW/PREV WINS : 16 / 15 ; DRAWS : 9
2024-05-13 05:21:29 0e1cec8e8708 Coach[48618] INFO REJECTING NEW MODEL
2024-05-13 05:21:29 0e1cec8e8708 Coach[48618] INFO Starting Iter #5 ...
Self Play: 100% 100/100 [3:12:50<00:00, 115.70s/it]









2024-05-13 12:37:08 11a40a93e47a __main__[6444] INFO Loading Dama...
2024-05-13 12:37:08 11a40a93e47a __main__[6444] INFO Loading NNetWrapper...
2024-05-13 12:37:09 11a40a93e47a __main__[6444] INFO Loading checkpoint "./temp//checkpoint_4.pth.tar"...
2024-05-13 12:37:11 11a40a93e47a __main__[6444] INFO Loading the Coach...
2024-05-13 12:37:11 11a40a93e47a __main__[6444] INFO Loading 'trainExamples' from file...
2024-05-13 12:37:11 11a40a93e47a Coach[6444] INFO File with trainExamples found. Loading it...
2024-05-13 12:37:25 11a40a93e47a Coach[6444] INFO Loading done!
2024-05-13 12:37:25 11a40a93e47a __main__[6444] INFO Starting the learning process 🎉
2024-05-13 12:37:25 11a40a93e47a Coach[6444] INFO Starting Iter #1 ...
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 992/992 [00:27<00:00, 35.78it/s, Loss_pi=1.27e+00, Loss_v=3.24e-01]
EPOCH ::: 2
Training Net: 100% 992/992 [00:24<00:00, 41.10it/s, Loss_pi=9.11e-01, Loss_v=2.24e-01]
EPOCH ::: 3
Training Net: 100% 992/992 [00:24<00:00, 41.09it/s, Loss_pi=7.48e-01, Loss_v=1.78e-01]
EPOCH ::: 4
Training Net: 100% 992/992 [00:23<00:00, 41.36it/s, Loss_pi=6.74e-01, Loss_v=1.52e-01]
EPOCH ::: 5
Training Net: 100% 992/992 [00:23<00:00, 41.63it/s, Loss_pi=6.15e-01, Loss_v=1.36e-01]
EPOCH ::: 6
Training Net: 100% 992/992 [00:24<00:00, 41.11it/s, Loss_pi=5.70e-01, Loss_v=1.21e-01]
EPOCH ::: 7
Training Net: 100% 992/992 [00:23<00:00, 41.54it/s, Loss_pi=5.39e-01, Loss_v=1.12e-01]
EPOCH ::: 8
Training Net: 100% 992/992 [00:24<00:00, 41.00it/s, Loss_pi=5.14e-01, Loss_v=1.02e-01]
EPOCH ::: 9
Training Net: 100% 992/992 [00:23<00:00, 41.57it/s, Loss_pi=4.93e-01, Loss_v=9.87e-02]
EPOCH ::: 10
Training Net: 100% 992/992 [00:23<00:00, 41.57it/s, Loss_pi=4.85e-01, Loss_v=9.26e-02]
EPOCH ::: 11
Training Net: 100% 992/992 [00:23<00:00, 41.63it/s, Loss_pi=4.75e-01, Loss_v=9.16e-02]
EPOCH ::: 12
Training Net: 100% 992/992 [00:23<00:00, 42.01it/s, Loss_pi=4.65e-01, Loss_v=9.09e-02]
EPOCH ::: 13
Training Net: 100% 992/992 [00:24<00:00, 40.95it/s, Loss_pi=4.62e-01, Loss_v=8.64e-02]
EPOCH ::: 14
Training Net: 100% 992/992 [00:23<00:00, 41.92it/s, Loss_pi=4.61e-01, Loss_v=8.47e-02]
EPOCH ::: 15
Training Net: 100% 992/992 [00:23<00:00, 42.04it/s, Loss_pi=4.52e-01, Loss_v=8.49e-02]
EPOCH ::: 16
Training Net: 100% 992/992 [00:23<00:00, 41.99it/s, Loss_pi=4.44e-01, Loss_v=8.01e-02]
EPOCH ::: 17
Training Net: 100% 992/992 [00:23<00:00, 42.06it/s, Loss_pi=4.45e-01, Loss_v=8.38e-02]
EPOCH ::: 18
Training Net: 100% 992/992 [00:23<00:00, 41.86it/s, Loss_pi=4.38e-01, Loss_v=7.78e-02]
EPOCH ::: 19
Training Net: 100% 992/992 [00:23<00:00, 41.85it/s, Loss_pi=4.39e-01, Loss_v=8.13e-02]
EPOCH ::: 20
Training Net: 100% 992/992 [00:24<00:00, 41.16it/s, Loss_pi=4.26e-01, Loss_v=7.97e-02]
EPOCH ::: 21
Training Net: 100% 992/992 [00:23<00:00, 41.55it/s, Loss_pi=4.25e-01, Loss_v=7.73e-02]
EPOCH ::: 22
Training Net: 100% 992/992 [00:23<00:00, 41.94it/s, Loss_pi=4.15e-01, Loss_v=7.34e-02]
EPOCH ::: 23
Training Net: 100% 992/992 [00:23<00:00, 41.84it/s, Loss_pi=4.18e-01, Loss_v=7.61e-02]
EPOCH ::: 24
Training Net: 100% 992/992 [00:23<00:00, 41.64it/s, Loss_pi=4.27e-01, Loss_v=7.62e-02]
EPOCH ::: 25
Training Net: 100% 992/992 [00:23<00:00, 41.70it/s, Loss_pi=4.12e-01, Loss_v=7.24e-02]
EPOCH ::: 26
Training Net: 100% 992/992 [00:23<00:00, 41.75it/s, Loss_pi=4.15e-01, Loss_v=7.50e-02]
EPOCH ::: 27
Training Net: 100% 992/992 [00:23<00:00, 42.09it/s, Loss_pi=4.11e-01, Loss_v=7.22e-02]
EPOCH ::: 28
Training Net: 100% 992/992 [00:23<00:00, 42.16it/s, Loss_pi=4.11e-01, Loss_v=7.30e-02]
EPOCH ::: 29
Training Net: 100% 992/992 [00:23<00:00, 41.66it/s, Loss_pi=4.12e-01, Loss_v=7.47e-02]
EPOCH ::: 30
Training Net: 100% 992/992 [00:23<00:00, 41.52it/s, Loss_pi=4.06e-01, Loss_v=7.36e-02]
2024-05-13 12:49:37 11a40a93e47a Coach[6444] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [42:46<00:00, 128.33s/it]
Arena.playGames (2): 100% 20/20 [41:24<00:00, 124.24s/it]
2024-05-13 14:13:48 11a40a93e47a Coach[6444] INFO NEW/PREV WINS : 21 / 12 ; DRAWS : 7
2024-05-13 14:13:48 11a40a93e47a Coach[6444] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-13 14:13:54 11a40a93e47a Coach[6444] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [4:18:39<00:00, 155.19s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 1111/1111 [00:30<00:00, 36.00it/s, Loss_pi=5.74e-01, Loss_v=1.16e-01]
EPOCH ::: 2
Training Net: 100% 1111/1111 [00:28<00:00, 39.47it/s, Loss_pi=4.91e-01, Loss_v=9.73e-02]
EPOCH ::: 3
Training Net: 100% 1111/1111 [00:28<00:00, 38.62it/s, Loss_pi=4.55e-01, Loss_v=8.81e-02]
EPOCH ::: 4
Training Net: 100% 1111/1111 [00:28<00:00, 39.27it/s, Loss_pi=4.38e-01, Loss_v=8.36e-02]
EPOCH ::: 5
Training Net: 100% 1111/1111 [00:28<00:00, 39.20it/s, Loss_pi=4.22e-01, Loss_v=7.90e-02]
EPOCH ::: 6
Training Net: 100% 1111/1111 [00:28<00:00, 38.87it/s, Loss_pi=4.19e-01, Loss_v=7.70e-02]
EPOCH ::: 7
Training Net: 100% 1111/1111 [00:28<00:00, 38.99it/s, Loss_pi=4.16e-01, Loss_v=7.42e-02]
EPOCH ::: 8
Training Net: 100% 1111/1111 [00:28<00:00, 39.27it/s, Loss_pi=4.06e-01, Loss_v=7.35e-02]
EPOCH ::: 9
Training Net: 100% 1111/1111 [00:29<00:00, 38.22it/s, Loss_pi=3.99e-01, Loss_v=7.12e-02]
EPOCH ::: 10
Training Net: 100% 1111/1111 [00:28<00:00, 38.92it/s, Loss_pi=4.02e-01, Loss_v=7.14e-02]
EPOCH ::: 11
Training Net: 100% 1111/1111 [00:28<00:00, 38.63it/s, Loss_pi=4.00e-01, Loss_v=7.03e-02]
EPOCH ::: 12
Training Net: 100% 1111/1111 [00:28<00:00, 39.17it/s, Loss_pi=3.95e-01, Loss_v=7.13e-02]
EPOCH ::: 13
Training Net: 100% 1111/1111 [00:28<00:00, 39.11it/s, Loss_pi=3.95e-01, Loss_v=6.95e-02]
EPOCH ::: 14
Training Net: 100% 1111/1111 [00:28<00:00, 38.90it/s, Loss_pi=3.96e-01, Loss_v=6.94e-02]
EPOCH ::: 15
Training Net: 100% 1111/1111 [00:28<00:00, 39.38it/s, Loss_pi=3.92e-01, Loss_v=6.60e-02]
EPOCH ::: 16
Training Net: 100% 1111/1111 [00:28<00:00, 39.15it/s, Loss_pi=3.89e-01, Loss_v=6.86e-02]
EPOCH ::: 17
Training Net: 100% 1111/1111 [00:28<00:00, 38.75it/s, Loss_pi=3.88e-01, Loss_v=6.78e-02]
EPOCH ::: 18
Training Net: 100% 1111/1111 [00:28<00:00, 39.17it/s, Loss_pi=3.90e-01, Loss_v=6.78e-02]
EPOCH ::: 19
Training Net: 100% 1111/1111 [00:28<00:00, 38.83it/s, Loss_pi=3.80e-01, Loss_v=6.48e-02]
EPOCH ::: 20
Training Net: 100% 1111/1111 [00:28<00:00, 38.79it/s, Loss_pi=3.84e-01, Loss_v=6.59e-02]
EPOCH ::: 21
Training Net: 100% 1111/1111 [00:28<00:00, 38.72it/s, Loss_pi=3.81e-01, Loss_v=6.37e-02]
EPOCH ::: 22
Training Net: 100% 1111/1111 [00:28<00:00, 39.14it/s, Loss_pi=3.82e-01, Loss_v=6.52e-02]
EPOCH ::: 23
Training Net: 100% 1111/1111 [00:28<00:00, 39.21it/s, Loss_pi=3.73e-01, Loss_v=6.61e-02]
EPOCH ::: 24
Training Net: 100% 1111/1111 [00:28<00:00, 39.46it/s, Loss_pi=3.78e-01, Loss_v=6.61e-02]
EPOCH ::: 25
Training Net: 100% 1111/1111 [00:28<00:00, 39.37it/s, Loss_pi=3.85e-01, Loss_v=6.72e-02]
EPOCH ::: 26
Training Net: 100% 1111/1111 [00:28<00:00, 39.06it/s, Loss_pi=3.76e-01, Loss_v=6.48e-02]
EPOCH ::: 27
Training Net: 100% 1111/1111 [00:28<00:00, 39.62it/s, Loss_pi=3.73e-01, Loss_v=6.31e-02]
EPOCH ::: 28
Training Net: 100% 1111/1111 [00:28<00:00, 38.70it/s, Loss_pi=3.76e-01, Loss_v=6.08e-02]
EPOCH ::: 29
Training Net: 100% 1111/1111 [00:28<00:00, 39.07it/s, Loss_pi=3.74e-01, Loss_v=6.23e-02]
EPOCH ::: 30
Training Net: 100% 1111/1111 [00:28<00:00, 39.30it/s, Loss_pi=3.73e-01, Loss_v=6.49e-02]
2024-05-13 18:47:02 11a40a93e47a Coach[6444] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [42:02<00:00, 126.11s/it]
Arena.playGames (2): 100% 20/20 [43:52<00:00, 131.64s/it]
2024-05-13 20:12:57 11a40a93e47a Coach[6444] INFO NEW/PREV WINS : 14 / 13 ; DRAWS : 13
2024-05-13 20:12:57 11a40a93e47a Coach[6444] INFO REJECTING NEW MODEL
2024-05-13 20:12:57 11a40a93e47a Coach[6444] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [4:19:33<00:00, 155.74s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 1229/1229 [00:36<00:00, 33.63it/s, Loss_pi=6.94e-01, Loss_v=1.46e-01]
EPOCH ::: 2
Training Net: 100% 1229/1229 [00:33<00:00, 37.06it/s, Loss_pi=5.55e-01, Loss_v=1.18e-01]
EPOCH ::: 3
Training Net: 100% 1229/1229 [00:33<00:00, 37.10it/s, Loss_pi=4.92e-01, Loss_v=1.01e-01]
EPOCH ::: 4
Training Net: 100% 1229/1229 [00:32<00:00, 37.53it/s, Loss_pi=4.58e-01, Loss_v=9.68e-02]
EPOCH ::: 5
Training Net: 100% 1229/1229 [00:32<00:00, 37.69it/s, Loss_pi=4.42e-01, Loss_v=8.81e-02]
EPOCH ::: 6
Training Net: 100% 1229/1229 [00:32<00:00, 37.75it/s, Loss_pi=4.35e-01, Loss_v=8.53e-02]
EPOCH ::: 7
Training Net: 100% 1229/1229 [00:33<00:00, 37.12it/s, Loss_pi=4.22e-01, Loss_v=8.09e-02]
EPOCH ::: 8
Training Net: 100% 1229/1229 [00:32<00:00, 37.97it/s, Loss_pi=4.14e-01, Loss_v=7.77e-02]
EPOCH ::: 9
Training Net: 100% 1229/1229 [00:32<00:00, 37.71it/s, Loss_pi=4.08e-01, Loss_v=7.53e-02]
EPOCH ::: 10
Training Net: 100% 1229/1229 [00:32<00:00, 37.68it/s, Loss_pi=4.08e-01, Loss_v=7.59e-02]
EPOCH ::: 11
Training Net: 100% 1229/1229 [00:32<00:00, 38.19it/s, Loss_pi=4.05e-01, Loss_v=7.43e-02]
EPOCH ::: 12
Training Net: 100% 1229/1229 [00:32<00:00, 38.15it/s, Loss_pi=4.02e-01, Loss_v=7.26e-02]
EPOCH ::: 13
Training Net: 100% 1229/1229 [00:32<00:00, 37.44it/s, Loss_pi=3.99e-01, Loss_v=7.37e-02]
EPOCH ::: 14
Training Net: 100% 1229/1229 [00:32<00:00, 38.19it/s, Loss_pi=3.96e-01, Loss_v=7.15e-02]
EPOCH ::: 15
Training Net: 100% 1229/1229 [00:31<00:00, 38.60it/s, Loss_pi=3.93e-01, Loss_v=7.06e-02]
EPOCH ::: 16
Training Net: 100% 1229/1229 [00:32<00:00, 38.22it/s, Loss_pi=3.89e-01, Loss_v=6.86e-02]
EPOCH ::: 17
Training Net: 100% 1229/1229 [00:32<00:00, 38.30it/s, Loss_pi=3.89e-01, Loss_v=6.83e-02]
EPOCH ::: 18
Training Net: 100% 1229/1229 [00:32<00:00, 37.76it/s, Loss_pi=3.87e-01, Loss_v=6.83e-02]
EPOCH ::: 19
Training Net: 100% 1229/1229 [00:32<00:00, 37.56it/s, Loss_pi=3.84e-01, Loss_v=6.76e-02]
EPOCH ::: 20
Training Net: 100% 1229/1229 [00:31<00:00, 38.79it/s, Loss_pi=3.82e-01, Loss_v=6.71e-02]
EPOCH ::: 21
Training Net: 100% 1229/1229 [00:32<00:00, 38.28it/s, Loss_pi=3.84e-01, Loss_v=6.66e-02]
EPOCH ::: 22
Training Net: 100% 1229/1229 [00:32<00:00, 37.95it/s, Loss_pi=3.80e-01, Loss_v=6.89e-02]
EPOCH ::: 23
Training Net: 100% 1229/1229 [00:33<00:00, 36.87it/s, Loss_pi=3.81e-01, Loss_v=6.51e-02]
EPOCH ::: 24
Training Net: 100% 1229/1229 [00:33<00:00, 37.02it/s, Loss_pi=3.79e-01, Loss_v=6.39e-02]
EPOCH ::: 25
Training Net: 100% 1229/1229 [00:32<00:00, 37.35it/s, Loss_pi=3.73e-01, Loss_v=6.28e-02]
EPOCH ::: 26
Training Net: 100% 1229/1229 [00:32<00:00, 38.04it/s, Loss_pi=3.70e-01, Loss_v=6.50e-02]
EPOCH ::: 27
Training Net: 100% 1229/1229 [00:32<00:00, 37.85it/s, Loss_pi=3.74e-01, Loss_v=6.53e-02]
EPOCH ::: 28
Training Net: 100% 1229/1229 [00:32<00:00, 37.92it/s, Loss_pi=3.70e-01, Loss_v=6.32e-02]
EPOCH ::: 29
Training Net: 100% 1229/1229 [00:32<00:00, 37.47it/s, Loss_pi=3.75e-01, Loss_v=6.55e-02]
EPOCH ::: 30
Training Net: 100% 1229/1229 [00:32<00:00, 37.58it/s, Loss_pi=3.73e-01, Loss_v=6.54e-02]
2024-05-14 00:49:09 11a40a93e47a Coach[6444] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [41:33<00:00, 124.67s/it]
Arena.playGames (2): 100% 20/20 [36:00<00:00, 108.03s/it]
2024-05-14 02:06:43 11a40a93e47a Coach[6444] INFO NEW/PREV WINS : 13 / 16 ; DRAWS : 11
2024-05-14 02:06:43 11a40a93e47a Coach[6444] INFO REJECTING NEW MODEL
2024-05-14 02:06:43 11a40a93e47a Coach[6444] INFO Starting Iter #4 ...
Self Play: 100% 100/100 [4:21:49<00:00, 157.10s/it]











wandb: Currently logged in as: cemgulec (cem-gulec). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /content/drive/MyDrive/dama_project/wandb/run-20240514_142023-fc5z5fzb
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run wandb run name
wandb: ⭐️ View project at https://wandb.ai/cem-gulec/dama-project
wandb: 🚀 View run at https://wandb.ai/cem-gulec/dama-project/runs/fc5z5fzb
2024-05-14 14:20:24 c847504f8e82 __main__[28753] INFO Loading Dama...
2024-05-14 14:20:24 c847504f8e82 __main__[28753] INFO Loading NNetWrapper...
2024-05-14 14:20:24 c847504f8e82 __main__[28753] INFO Loading checkpoint "./temp//checkpoint_3.pth.tar"...
2024-05-14 14:20:24 c847504f8e82 __main__[28753] INFO Loading the Coach...
2024-05-14 14:20:24 c847504f8e82 __main__[28753] INFO Loading 'trainExamples' from file...
2024-05-14 14:20:24 c847504f8e82 Coach[28753] INFO File with trainExamples found. Loading it...
2024-05-14 14:20:39 c847504f8e82 Coach[28753] INFO Loading done!
2024-05-14 14:20:39 c847504f8e82 __main__[28753] INFO Starting the learning process 🎉
2024-05-14 14:20:39 c847504f8e82 Coach[28753] INFO Starting Iter #1 ...
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 1349/1349 [00:32<00:00, 41.79it/s, Loss_pi=7.88e-01, Loss_v=1.76e-01]
EPOCH ::: 2
Training Net: 100% 1349/1349 [00:30<00:00, 44.41it/s, Loss_pi=6.14e-01, Loss_v=1.36e-01]
EPOCH ::: 3
Training Net: 100% 1349/1349 [00:30<00:00, 44.43it/s, Loss_pi=5.27e-01, Loss_v=1.17e-01]
EPOCH ::: 4
Training Net: 100% 1349/1349 [00:29<00:00, 45.02it/s, Loss_pi=4.80e-01, Loss_v=1.04e-01]
EPOCH ::: 5
Training Net: 100% 1349/1349 [00:30<00:00, 44.46it/s, Loss_pi=4.62e-01, Loss_v=9.46e-02]
EPOCH ::: 6
Training Net: 100% 1349/1349 [00:30<00:00, 44.80it/s, Loss_pi=4.41e-01, Loss_v=8.98e-02]
EPOCH ::: 7
Training Net: 100% 1349/1349 [00:30<00:00, 44.72it/s, Loss_pi=4.36e-01, Loss_v=8.64e-02]
EPOCH ::: 8
Training Net: 100% 1349/1349 [00:30<00:00, 44.70it/s, Loss_pi=4.27e-01, Loss_v=8.33e-02]
EPOCH ::: 9
Training Net: 100% 1349/1349 [00:30<00:00, 44.61it/s, Loss_pi=4.22e-01, Loss_v=8.21e-02]
EPOCH ::: 10
Training Net: 100% 1349/1349 [00:30<00:00, 44.25it/s, Loss_pi=4.15e-01, Loss_v=7.85e-02]
EPOCH ::: 11
Training Net: 100% 1349/1349 [00:30<00:00, 44.64it/s, Loss_pi=4.04e-01, Loss_v=7.64e-02]
EPOCH ::: 12
Training Net: 100% 1349/1349 [00:30<00:00, 44.23it/s, Loss_pi=4.08e-01, Loss_v=7.79e-02]
EPOCH ::: 13
Training Net: 100% 1349/1349 [00:30<00:00, 43.76it/s, Loss_pi=4.00e-01, Loss_v=7.45e-02]
EPOCH ::: 14
Training Net: 100% 1349/1349 [00:31<00:00, 43.46it/s, Loss_pi=3.97e-01, Loss_v=7.30e-02]
EPOCH ::: 15
Training Net: 100% 1349/1349 [00:31<00:00, 43.40it/s, Loss_pi=3.93e-01, Loss_v=7.48e-02]
EPOCH ::: 16
Training Net: 100% 1349/1349 [00:31<00:00, 43.46it/s, Loss_pi=3.92e-01, Loss_v=7.30e-02]
EPOCH ::: 17
Training Net: 100% 1349/1349 [00:31<00:00, 43.41it/s, Loss_pi=3.85e-01, Loss_v=6.97e-02]
EPOCH ::: 18
Training Net: 100% 1349/1349 [00:31<00:00, 43.41it/s, Loss_pi=3.84e-01, Loss_v=7.00e-02]
EPOCH ::: 19
Training Net: 100% 1349/1349 [00:30<00:00, 43.69it/s, Loss_pi=3.85e-01, Loss_v=6.82e-02]
EPOCH ::: 20
Training Net: 100% 1349/1349 [00:31<00:00, 43.36it/s, Loss_pi=3.85e-01, Loss_v=6.93e-02]
EPOCH ::: 21
Training Net: 100% 1349/1349 [00:31<00:00, 43.37it/s, Loss_pi=3.83e-01, Loss_v=6.86e-02]
EPOCH ::: 22
Training Net: 100% 1349/1349 [00:30<00:00, 44.11it/s, Loss_pi=3.83e-01, Loss_v=6.84e-02]
EPOCH ::: 23
Training Net: 100% 1349/1349 [00:30<00:00, 44.19it/s, Loss_pi=3.81e-01, Loss_v=6.62e-02]
EPOCH ::: 24
Training Net: 100% 1349/1349 [00:30<00:00, 43.76it/s, Loss_pi=3.79e-01, Loss_v=6.60e-02]
EPOCH ::: 25
Training Net: 100% 1349/1349 [00:31<00:00, 43.46it/s, Loss_pi=3.78e-01, Loss_v=6.51e-02]
EPOCH ::: 26
Training Net: 100% 1349/1349 [00:30<00:00, 44.19it/s, Loss_pi=3.74e-01, Loss_v=6.60e-02]
EPOCH ::: 27
Training Net: 100% 1349/1349 [00:30<00:00, 43.56it/s, Loss_pi=3.70e-01, Loss_v=6.46e-02]
EPOCH ::: 28
Training Net: 100% 1349/1349 [00:30<00:00, 44.17it/s, Loss_pi=3.74e-01, Loss_v=6.60e-02]
EPOCH ::: 29
Training Net: 100% 1349/1349 [00:30<00:00, 43.92it/s, Loss_pi=3.65e-01, Loss_v=6.26e-02]
EPOCH ::: 30
Training Net: 100% 1349/1349 [00:31<00:00, 43.40it/s, Loss_pi=3.67e-01, Loss_v=6.46e-02]
2024-05-14 14:36:14 c847504f8e82 Coach[28753] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [32:12<00:00, 96.63s/it]
Arena.playGames (2): 100% 20/20 [33:20<00:00, 100.04s/it]
2024-05-14 15:41:48 c847504f8e82 Coach[28753] INFO NEW/PREV WINS : 15 / 15 ; DRAWS : 10
2024-05-14 15:41:48 c847504f8e82 Coach[28753] INFO REJECTING NEW MODEL
2024-05-14 15:41:48 c847504f8e82 Coach[28753] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [3:07:35<00:00, 112.55s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 1466/1466 [00:39<00:00, 37.28it/s, Loss_pi=8.67e-01, Loss_v=1.93e-01]
EPOCH ::: 2
Training Net: 100% 1466/1466 [00:36<00:00, 39.78it/s, Loss_pi=6.57e-01, Loss_v=1.50e-01]
EPOCH ::: 3
Training Net: 100% 1466/1466 [00:37<00:00, 38.73it/s, Loss_pi=5.66e-01, Loss_v=1.30e-01]
EPOCH ::: 4
Training Net: 100% 1466/1466 [00:38<00:00, 38.31it/s, Loss_pi=5.11e-01, Loss_v=1.14e-01]
EPOCH ::: 5
Training Net: 100% 1466/1466 [00:37<00:00, 39.40it/s, Loss_pi=4.78e-01, Loss_v=1.04e-01]
EPOCH ::: 6
Training Net: 100% 1466/1466 [00:36<00:00, 40.17it/s, Loss_pi=4.56e-01, Loss_v=9.58e-02]
EPOCH ::: 7
Training Net: 100% 1466/1466 [00:36<00:00, 40.11it/s, Loss_pi=4.43e-01, Loss_v=9.08e-02]
EPOCH ::: 8
Training Net: 100% 1466/1466 [00:36<00:00, 40.46it/s, Loss_pi=4.31e-01, Loss_v=8.93e-02]
EPOCH ::: 9
Training Net: 100% 1466/1466 [00:36<00:00, 40.22it/s, Loss_pi=4.20e-01, Loss_v=8.51e-02]
EPOCH ::: 10
Training Net: 100% 1466/1466 [00:36<00:00, 40.19it/s, Loss_pi=4.18e-01, Loss_v=8.32e-02]
EPOCH ::: 11
Training Net: 100% 1466/1466 [00:36<00:00, 39.99it/s, Loss_pi=4.15e-01, Loss_v=8.17e-02]
EPOCH ::: 12
Training Net: 100% 1466/1466 [00:36<00:00, 40.14it/s, Loss_pi=4.06e-01, Loss_v=8.02e-02]
EPOCH ::: 13
Training Net: 100% 1466/1466 [00:36<00:00, 40.03it/s, Loss_pi=3.99e-01, Loss_v=7.50e-02]
EPOCH ::: 14
Training Net: 100% 1466/1466 [00:36<00:00, 39.90it/s, Loss_pi=4.02e-01, Loss_v=7.48e-02]
EPOCH ::: 15
Training Net: 100% 1466/1466 [00:36<00:00, 40.34it/s, Loss_pi=3.96e-01, Loss_v=7.45e-02]
EPOCH ::: 16
Training Net: 100% 1466/1466 [00:36<00:00, 40.53it/s, Loss_pi=3.89e-01, Loss_v=7.26e-02]
EPOCH ::: 17
Training Net: 100% 1466/1466 [00:36<00:00, 40.59it/s, Loss_pi=3.90e-01, Loss_v=7.33e-02]
EPOCH ::: 18
Training Net: 100% 1466/1466 [00:36<00:00, 40.42it/s, Loss_pi=3.89e-01, Loss_v=7.15e-02]
EPOCH ::: 19
Training Net: 100% 1466/1466 [00:36<00:00, 39.83it/s, Loss_pi=3.83e-01, Loss_v=7.25e-02]
EPOCH ::: 20
Training Net: 100% 1466/1466 [00:35<00:00, 40.78it/s, Loss_pi=3.81e-01, Loss_v=7.07e-02]
EPOCH ::: 21
Training Net: 100% 1466/1466 [00:36<00:00, 40.44it/s, Loss_pi=3.78e-01, Loss_v=6.94e-02]
EPOCH ::: 22
Training Net: 100% 1466/1466 [00:36<00:00, 39.99it/s, Loss_pi=3.78e-01, Loss_v=7.00e-02]
EPOCH ::: 23
Training Net: 100% 1466/1466 [00:36<00:00, 40.41it/s, Loss_pi=3.74e-01, Loss_v=6.74e-02]
EPOCH ::: 24
Training Net: 100% 1466/1466 [00:36<00:00, 39.90it/s, Loss_pi=3.75e-01, Loss_v=6.86e-02]
EPOCH ::: 25
Training Net: 100% 1466/1466 [00:38<00:00, 38.28it/s, Loss_pi=3.73e-01, Loss_v=6.78e-02]
EPOCH ::: 26
Training Net: 100% 1466/1466 [00:36<00:00, 39.81it/s, Loss_pi=3.68e-01, Loss_v=6.83e-02]
EPOCH ::: 27
Training Net: 100% 1466/1466 [00:36<00:00, 40.45it/s, Loss_pi=3.75e-01, Loss_v=6.79e-02]
EPOCH ::: 28
Training Net: 100% 1466/1466 [00:36<00:00, 40.50it/s, Loss_pi=3.69e-01, Loss_v=6.56e-02]
EPOCH ::: 29
Training Net: 100% 1466/1466 [00:36<00:00, 40.45it/s, Loss_pi=3.71e-01, Loss_v=6.65e-02]
EPOCH ::: 30
Training Net: 100% 1466/1466 [00:36<00:00, 40.31it/s, Loss_pi=3.64e-01, Loss_v=6.40e-02]
2024-05-14 19:08:00 c847504f8e82 Coach[28753] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [32:48<00:00, 98.42s/it] 
Arena.playGames (2): 100% 20/20 [33:16<00:00, 99.81s/it]
2024-05-14 20:14:05 c847504f8e82 Coach[28753] INFO NEW/PREV WINS : 16 / 12 ; DRAWS : 12
2024-05-14 20:14:05 c847504f8e82 Coach[28753] INFO REJECTING NEW MODEL
2024-05-14 20:14:05 c847504f8e82 Coach[28753] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [3:09:22<00:00, 113.62s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 1585/1585 [00:42<00:00, 37.51it/s, Loss_pi=9.30e-01, Loss_v=2.08e-01]
EPOCH ::: 2
Training Net: 100% 1585/1585 [00:39<00:00, 39.82it/s, Loss_pi=6.99e-01, Loss_v=1.59e-01]
EPOCH ::: 3
Training Net: 100% 1585/1585 [00:39<00:00, 39.94it/s, Loss_pi=5.92e-01, Loss_v=1.37e-01]
EPOCH ::: 4
Training Net: 100% 1585/1585 [00:39<00:00, 40.45it/s, Loss_pi=5.32e-01, Loss_v=1.20e-01]
EPOCH ::: 5
Training Net: 100% 1585/1585 [00:39<00:00, 40.23it/s, Loss_pi=4.97e-01, Loss_v=1.08e-01]
EPOCH ::: 6
Training Net: 100% 1585/1585 [00:39<00:00, 39.98it/s, Loss_pi=4.71e-01, Loss_v=1.03e-01]
EPOCH ::: 7
Training Net: 100% 1585/1585 [00:39<00:00, 40.02it/s, Loss_pi=4.53e-01, Loss_v=9.45e-02]
EPOCH ::: 8
Training Net: 100% 1585/1585 [00:39<00:00, 40.10it/s, Loss_pi=4.37e-01, Loss_v=9.10e-02]
EPOCH ::: 9
Training Net: 100% 1585/1585 [00:39<00:00, 39.85it/s, Loss_pi=4.26e-01, Loss_v=8.76e-02]
EPOCH ::: 10
Training Net: 100% 1585/1585 [00:40<00:00, 39.48it/s, Loss_pi=4.23e-01, Loss_v=8.54e-02]
EPOCH ::: 11
Training Net: 100% 1585/1585 [00:39<00:00, 39.64it/s, Loss_pi=4.19e-01, Loss_v=8.44e-02]
EPOCH ::: 12
Training Net: 100% 1585/1585 [00:39<00:00, 40.25it/s, Loss_pi=4.04e-01, Loss_v=7.96e-02]
EPOCH ::: 13
Training Net: 100% 1585/1585 [00:39<00:00, 40.23it/s, Loss_pi=4.03e-01, Loss_v=7.99e-02]
EPOCH ::: 14
Training Net: 100% 1585/1585 [00:39<00:00, 40.47it/s, Loss_pi=4.04e-01, Loss_v=7.66e-02]
EPOCH ::: 15
Training Net: 100% 1585/1585 [00:39<00:00, 39.70it/s, Loss_pi=3.95e-01, Loss_v=7.55e-02]
EPOCH ::: 16
Training Net: 100% 1585/1585 [00:39<00:00, 40.59it/s, Loss_pi=3.99e-01, Loss_v=7.47e-02]
EPOCH ::: 17
Training Net: 100% 1585/1585 [00:39<00:00, 40.23it/s, Loss_pi=3.87e-01, Loss_v=7.38e-02]
EPOCH ::: 18
Training Net: 100% 1585/1585 [00:39<00:00, 40.04it/s, Loss_pi=3.86e-01, Loss_v=7.23e-02]
EPOCH ::: 19
Training Net: 100% 1585/1585 [00:39<00:00, 40.16it/s, Loss_pi=3.87e-01, Loss_v=7.03e-02]
EPOCH ::: 20
Training Net: 100% 1585/1585 [00:39<00:00, 40.20it/s, Loss_pi=3.78e-01, Loss_v=6.88e-02]
EPOCH ::: 21
Training Net: 100% 1585/1585 [00:39<00:00, 40.59it/s, Loss_pi=3.79e-01, Loss_v=6.95e-02]
EPOCH ::: 22
Training Net: 100% 1585/1585 [00:39<00:00, 40.39it/s, Loss_pi=3.83e-01, Loss_v=6.94e-02]
EPOCH ::: 23
Training Net: 100% 1585/1585 [00:39<00:00, 40.45it/s, Loss_pi=3.79e-01, Loss_v=6.94e-02]
EPOCH ::: 24
Training Net: 100% 1585/1585 [00:41<00:00, 38.46it/s, Loss_pi=3.73e-01, Loss_v=6.64e-02]
EPOCH ::: 25
Training Net: 100% 1585/1585 [00:39<00:00, 40.49it/s, Loss_pi=3.67e-01, Loss_v=6.79e-02]
EPOCH ::: 26
Training Net: 100% 1585/1585 [00:39<00:00, 40.57it/s, Loss_pi=3.72e-01, Loss_v=6.76e-02]
EPOCH ::: 27
Training Net: 100% 1585/1585 [00:39<00:00, 40.38it/s, Loss_pi=3.69e-01, Loss_v=6.52e-02]
EPOCH ::: 28
Training Net: 100% 1585/1585 [00:40<00:00, 39.25it/s, Loss_pi=3.67e-01, Loss_v=6.39e-02]
EPOCH ::: 29
Training Net: 100% 1585/1585 [00:41<00:00, 38.35it/s, Loss_pi=3.67e-01, Loss_v=6.60e-02]
EPOCH ::: 30
Training Net: 100% 1585/1585 [00:40<00:00, 39.47it/s, Loss_pi=3.71e-01, Loss_v=6.67e-02]
2024-05-14 23:43:38 c847504f8e82 Coach[28753] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [29:28<00:00, 88.45s/it]
Arena.playGames (2): 100% 20/20 [33:47<00:00, 101.40s/it]
2024-05-15 00:46:55 c847504f8e82 Coach[28753] INFO NEW/PREV WINS : 17 / 13 ; DRAWS : 10
2024-05-15 00:46:55 c847504f8e82 Coach[28753] INFO REJECTING NEW MODEL
2024-05-15 00:46:55 c847504f8e82 Coach[28753] INFO Starting Iter #4 ...
Self Play: 100% 100/100 [3:11:41<00:00, 115.02s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 1704/1704 [00:45<00:00, 37.06it/s, Loss_pi=9.83e-01, Loss_v=2.28e-01]
EPOCH ::: 2
Training Net: 100% 1704/1704 [00:41<00:00, 40.73it/s, Loss_pi=7.39e-01, Loss_v=1.77e-01]
EPOCH ::: 3
Training Net: 100% 1704/1704 [00:42<00:00, 39.81it/s, Loss_pi=6.23e-01, Loss_v=1.50e-01]
EPOCH ::: 4
Training Net: 100% 1704/1704 [00:42<00:00, 40.14it/s, Loss_pi=5.55e-01, Loss_v=1.31e-01]
EPOCH ::: 5
Training Net: 100% 1704/1704 [00:42<00:00, 39.82it/s, Loss_pi=5.07e-01, Loss_v=1.20e-01]
EPOCH ::: 6
Training Net: 100% 1704/1704 [00:42<00:00, 39.65it/s, Loss_pi=4.82e-01, Loss_v=1.09e-01]
EPOCH ::: 7
Training Net: 100% 1704/1704 [00:42<00:00, 40.01it/s, Loss_pi=4.54e-01, Loss_v=1.01e-01]
EPOCH ::: 8
Training Net: 100% 1704/1704 [00:43<00:00, 39.58it/s, Loss_pi=4.42e-01, Loss_v=9.63e-02]
EPOCH ::: 9
Training Net: 100% 1704/1704 [00:43<00:00, 39.52it/s, Loss_pi=4.31e-01, Loss_v=9.23e-02]
EPOCH ::: 10
Training Net: 100% 1704/1704 [00:43<00:00, 38.81it/s, Loss_pi=4.31e-01, Loss_v=8.82e-02]
EPOCH ::: 11
Training Net: 100% 1704/1704 [00:43<00:00, 39.24it/s, Loss_pi=4.20e-01, Loss_v=8.57e-02]
EPOCH ::: 12
Training Net: 100% 1704/1704 [00:44<00:00, 38.68it/s, Loss_pi=4.14e-01, Loss_v=8.38e-02]
EPOCH ::: 13
Training Net: 100% 1704/1704 [00:43<00:00, 39.32it/s, Loss_pi=4.09e-01, Loss_v=8.23e-02]
EPOCH ::: 14
Training Net: 100% 1704/1704 [00:41<00:00, 40.60it/s, Loss_pi=4.03e-01, Loss_v=7.85e-02]
EPOCH ::: 15
Training Net: 100% 1704/1704 [00:42<00:00, 40.19it/s, Loss_pi=3.95e-01, Loss_v=7.87e-02]
EPOCH ::: 16
Training Net: 100% 1704/1704 [00:43<00:00, 39.11it/s, Loss_pi=3.95e-01, Loss_v=7.66e-02]
EPOCH ::: 17
Training Net: 100% 1704/1704 [00:43<00:00, 38.80it/s, Loss_pi=3.91e-01, Loss_v=7.61e-02]
EPOCH ::: 18
Training Net: 100% 1704/1704 [00:43<00:00, 39.31it/s, Loss_pi=3.86e-01, Loss_v=7.36e-02]
EPOCH ::: 19
Training Net: 100% 1704/1704 [00:43<00:00, 38.76it/s, Loss_pi=3.85e-01, Loss_v=7.33e-02]
EPOCH ::: 20
Training Net: 100% 1704/1704 [00:43<00:00, 39.53it/s, Loss_pi=3.78e-01, Loss_v=7.19e-02]
EPOCH ::: 21
Training Net: 100% 1704/1704 [00:43<00:00, 39.42it/s, Loss_pi=3.83e-01, Loss_v=7.12e-02]
EPOCH ::: 22
Training Net: 100% 1704/1704 [00:44<00:00, 38.55it/s, Loss_pi=3.79e-01, Loss_v=6.98e-02]
EPOCH ::: 23
Training Net: 100% 1704/1704 [00:43<00:00, 38.80it/s, Loss_pi=3.77e-01, Loss_v=6.93e-02]
EPOCH ::: 24
Training Net: 100% 1704/1704 [00:43<00:00, 39.09it/s, Loss_pi=3.77e-01, Loss_v=6.93e-02]
EPOCH ::: 25
Training Net: 100% 1704/1704 [00:43<00:00, 39.32it/s, Loss_pi=3.70e-01, Loss_v=6.98e-02]
EPOCH ::: 26
Training Net: 100% 1704/1704 [00:43<00:00, 39.29it/s, Loss_pi=3.74e-01, Loss_v=6.90e-02]
EPOCH ::: 27
Training Net: 100% 1704/1704 [00:43<00:00, 39.22it/s, Loss_pi=3.63e-01, Loss_v=6.84e-02]
EPOCH ::: 28
Training Net: 100% 1704/1704 [00:43<00:00, 38.78it/s, Loss_pi=3.66e-01, Loss_v=6.56e-02]
EPOCH ::: 29
Training Net: 100% 1704/1704 [00:44<00:00, 38.45it/s, Loss_pi=3.61e-01, Loss_v=6.54e-02]
EPOCH ::: 30
Training Net: 100% 1704/1704 [00:44<00:00, 38.12it/s, Loss_pi=3.61e-01, Loss_v=6.59e-02]
2024-05-15 04:20:40 c847504f8e82 Coach[28753] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [34:14<00:00, 102.70s/it]
Arena.playGames (2): 100% 20/20 [30:41<00:00, 92.09s/it] 
2024-05-15 05:25:35 c847504f8e82 Coach[28753] INFO NEW/PREV WINS : 21 / 10 ; DRAWS : 9
2024-05-15 05:25:35 c847504f8e82 Coach[28753] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-15 05:25:40 c847504f8e82 Coach[28753] INFO Starting Iter #5 ...
Self Play: 100% 100/100 [3:23:48<00:00, 122.28s/it]








wandb: Currently logged in as: cemgulec (cem-gulec). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /content/drive/MyDrive/dama_project/wandb/run-20240515_125426-j6zdxp8y
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Run 5
wandb: ⭐️ View project at https://wandb.ai/cem-gulec/dama-project
wandb: 🚀 View run at https://wandb.ai/cem-gulec/dama-project/runs/j6zdxp8y
2024-05-15 12:54:27 ae73d31ad80f __main__[3154] INFO Loading Dama...
2024-05-15 12:54:27 ae73d31ad80f __main__[3154] INFO Loading NNetWrapper...
2024-05-15 12:54:27 ae73d31ad80f __main__[3154] INFO Loading checkpoint "./temp//checkpoint_4.pth.tar"...
2024-05-15 12:54:27 ae73d31ad80f __main__[3154] INFO Loading the Coach...
2024-05-15 12:54:28 ae73d31ad80f __main__[3154] INFO Loading 'trainExamples' from file...
2024-05-15 12:54:28 ae73d31ad80f Coach[3154] INFO File with trainExamples found. Loading it...
2024-05-15 12:54:50 ae73d31ad80f Coach[3154] INFO Loading done!
2024-05-15 12:54:50 ae73d31ad80f __main__[3154] INFO Starting the learning process 🎉
2024-05-15 12:54:50 ae73d31ad80f Coach[3154] INFO Starting Iter #1 ...
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 1826/1826 [00:45<00:00, 39.74it/s, Loss_pi=4.57e-01, Loss_v=8.46e-02]
EPOCH ::: 2
Training Net: 100% 1826/1826 [00:43<00:00, 42.35it/s, Loss_pi=4.13e-01, Loss_v=7.86e-02]
EPOCH ::: 3
Training Net: 100% 1826/1826 [00:43<00:00, 42.41it/s, Loss_pi=3.93e-01, Loss_v=7.38e-02]
EPOCH ::: 4
Training Net: 100% 1826/1826 [00:42<00:00, 42.55it/s, Loss_pi=3.80e-01, Loss_v=7.13e-02]
EPOCH ::: 5
Training Net: 100% 1826/1826 [00:43<00:00, 42.26it/s, Loss_pi=3.67e-01, Loss_v=6.90e-02]
EPOCH ::: 6
Training Net: 100% 1826/1826 [00:42<00:00, 42.56it/s, Loss_pi=3.66e-01, Loss_v=6.90e-02]
EPOCH ::: 7
Training Net: 100% 1826/1826 [00:43<00:00, 42.32it/s, Loss_pi=3.59e-01, Loss_v=6.65e-02]
EPOCH ::: 8
Training Net: 100% 1826/1826 [00:43<00:00, 42.04it/s, Loss_pi=3.61e-01, Loss_v=6.53e-02]
EPOCH ::: 9
Training Net: 100% 1826/1826 [00:42<00:00, 42.70it/s, Loss_pi=3.55e-01, Loss_v=6.47e-02]
EPOCH ::: 10
Training Net: 100% 1826/1826 [00:42<00:00, 42.62it/s, Loss_pi=3.54e-01, Loss_v=6.42e-02]
EPOCH ::: 11
Training Net: 100% 1826/1826 [00:43<00:00, 42.39it/s, Loss_pi=3.56e-01, Loss_v=6.36e-02]
EPOCH ::: 12
Training Net: 100% 1826/1826 [00:42<00:00, 43.25it/s, Loss_pi=3.57e-01, Loss_v=6.44e-02]
EPOCH ::: 13
Training Net: 100% 1826/1826 [00:42<00:00, 42.88it/s, Loss_pi=3.45e-01, Loss_v=6.29e-02]
EPOCH ::: 14
Training Net: 100% 1826/1826 [00:42<00:00, 42.87it/s, Loss_pi=3.49e-01, Loss_v=6.30e-02]
EPOCH ::: 15
Training Net: 100% 1826/1826 [00:43<00:00, 42.28it/s, Loss_pi=3.51e-01, Loss_v=6.23e-02]
EPOCH ::: 16
Training Net: 100% 1826/1826 [00:42<00:00, 42.51it/s, Loss_pi=3.49e-01, Loss_v=6.13e-02]
EPOCH ::: 17
Training Net: 100% 1826/1826 [00:43<00:00, 42.40it/s, Loss_pi=3.50e-01, Loss_v=6.21e-02]
EPOCH ::: 18
Training Net: 100% 1826/1826 [00:43<00:00, 42.05it/s, Loss_pi=3.46e-01, Loss_v=6.10e-02]
EPOCH ::: 19
Training Net: 100% 1826/1826 [00:43<00:00, 42.12it/s, Loss_pi=3.47e-01, Loss_v=6.11e-02]
EPOCH ::: 20
Training Net: 100% 1826/1826 [00:42<00:00, 42.59it/s, Loss_pi=3.43e-01, Loss_v=6.03e-02]
EPOCH ::: 21
Training Net: 100% 1826/1826 [00:43<00:00, 41.96it/s, Loss_pi=3.46e-01, Loss_v=5.96e-02]
EPOCH ::: 22
Training Net: 100% 1826/1826 [00:43<00:00, 41.83it/s, Loss_pi=3.43e-01, Loss_v=5.99e-02]
EPOCH ::: 23
Training Net: 100% 1826/1826 [00:43<00:00, 41.56it/s, Loss_pi=3.41e-01, Loss_v=6.08e-02]
EPOCH ::: 24
Training Net: 100% 1826/1826 [00:43<00:00, 42.11it/s, Loss_pi=3.41e-01, Loss_v=5.92e-02]
EPOCH ::: 25
Training Net: 100% 1826/1826 [00:43<00:00, 41.90it/s, Loss_pi=3.41e-01, Loss_v=5.84e-02]
EPOCH ::: 26
Training Net: 100% 1826/1826 [00:43<00:00, 41.99it/s, Loss_pi=3.42e-01, Loss_v=5.80e-02]
EPOCH ::: 27
Training Net: 100% 1826/1826 [00:43<00:00, 42.03it/s, Loss_pi=3.35e-01, Loss_v=5.77e-02]
EPOCH ::: 28
Training Net: 100% 1826/1826 [00:43<00:00, 42.24it/s, Loss_pi=3.38e-01, Loss_v=5.80e-02]
EPOCH ::: 29
Training Net: 100% 1826/1826 [00:43<00:00, 42.40it/s, Loss_pi=3.32e-01, Loss_v=5.77e-02]
EPOCH ::: 30
Training Net: 100% 1826/1826 [00:43<00:00, 42.22it/s, Loss_pi=3.37e-01, Loss_v=5.69e-02]
2024-05-15 13:16:47 ae73d31ad80f Coach[3154] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [32:06<00:00, 96.33s/it]
Arena.playGames (2): 100% 20/20 [35:20<00:00, 106.03s/it]
2024-05-15 14:24:14 ae73d31ad80f Coach[3154] INFO NEW/PREV WINS : 14 / 10 ; DRAWS : 16
2024-05-15 14:24:14 ae73d31ad80f Coach[3154] INFO REJECTING NEW MODEL
2024-05-15 14:24:15 ae73d31ad80f Coach[3154] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [3:10:01<00:00, 114.02s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 1943/1943 [00:50<00:00, 38.83it/s, Loss_pi=5.38e-01, Loss_v=9.77e-02]
EPOCH ::: 2
Training Net: 100% 1943/1943 [00:47<00:00, 41.06it/s, Loss_pi=4.55e-01, Loss_v=8.74e-02]
EPOCH ::: 3
Training Net: 100% 1943/1943 [00:46<00:00, 41.40it/s, Loss_pi=4.19e-01, Loss_v=8.07e-02]
EPOCH ::: 4
Training Net: 100% 1943/1943 [00:47<00:00, 41.28it/s, Loss_pi=4.00e-01, Loss_v=7.66e-02]
EPOCH ::: 5
Training Net: 100% 1943/1943 [00:47<00:00, 41.28it/s, Loss_pi=3.87e-01, Loss_v=7.50e-02]
EPOCH ::: 6
Training Net: 100% 1943/1943 [00:46<00:00, 41.38it/s, Loss_pi=3.76e-01, Loss_v=7.22e-02]
EPOCH ::: 7
Training Net: 100% 1943/1943 [00:46<00:00, 41.42it/s, Loss_pi=3.74e-01, Loss_v=6.98e-02]
EPOCH ::: 8
Training Net: 100% 1943/1943 [00:46<00:00, 41.54it/s, Loss_pi=3.69e-01, Loss_v=6.82e-02]
EPOCH ::: 9
Training Net: 100% 1943/1943 [00:46<00:00, 41.47it/s, Loss_pi=3.63e-01, Loss_v=6.79e-02]
EPOCH ::: 10
Training Net: 100% 1943/1943 [00:47<00:00, 41.30it/s, Loss_pi=3.67e-01, Loss_v=6.78e-02]
EPOCH ::: 11
Training Net: 100% 1943/1943 [00:47<00:00, 40.99it/s, Loss_pi=3.62e-01, Loss_v=6.46e-02]
EPOCH ::: 12
Training Net: 100% 1943/1943 [00:47<00:00, 41.18it/s, Loss_pi=3.60e-01, Loss_v=6.51e-02]
EPOCH ::: 13
Training Net: 100% 1943/1943 [00:47<00:00, 41.14it/s, Loss_pi=3.57e-01, Loss_v=6.37e-02]
EPOCH ::: 14
Training Net: 100% 1943/1943 [00:47<00:00, 41.06it/s, Loss_pi=3.59e-01, Loss_v=6.40e-02]
EPOCH ::: 15
Training Net: 100% 1943/1943 [00:47<00:00, 41.09it/s, Loss_pi=3.57e-01, Loss_v=6.15e-02]
EPOCH ::: 16
Training Net: 100% 1943/1943 [00:47<00:00, 41.28it/s, Loss_pi=3.54e-01, Loss_v=6.26e-02]
EPOCH ::: 17
Training Net: 100% 1943/1943 [00:46<00:00, 41.61it/s, Loss_pi=3.53e-01, Loss_v=6.02e-02]
EPOCH ::: 18
Training Net: 100% 1943/1943 [00:46<00:00, 41.82it/s, Loss_pi=3.52e-01, Loss_v=6.13e-02]
EPOCH ::: 19
Training Net: 100% 1943/1943 [00:46<00:00, 41.44it/s, Loss_pi=3.47e-01, Loss_v=5.98e-02]
EPOCH ::: 20
Training Net: 100% 1943/1943 [00:46<00:00, 41.68it/s, Loss_pi=3.50e-01, Loss_v=6.07e-02]
EPOCH ::: 21
Training Net: 100% 1943/1943 [00:49<00:00, 39.33it/s, Loss_pi=3.49e-01, Loss_v=5.96e-02]
EPOCH ::: 22
Training Net: 100% 1943/1943 [00:48<00:00, 40.47it/s, Loss_pi=3.42e-01, Loss_v=5.79e-02]
EPOCH ::: 23
Training Net: 100% 1943/1943 [00:49<00:00, 39.41it/s, Loss_pi=3.46e-01, Loss_v=5.94e-02]
EPOCH ::: 24
Training Net: 100% 1943/1943 [00:47<00:00, 41.06it/s, Loss_pi=3.46e-01, Loss_v=6.03e-02]
EPOCH ::: 25
Training Net: 100% 1943/1943 [00:47<00:00, 40.84it/s, Loss_pi=3.45e-01, Loss_v=5.93e-02]
EPOCH ::: 26
Training Net: 100% 1943/1943 [00:47<00:00, 41.14it/s, Loss_pi=3.45e-01, Loss_v=5.87e-02]
EPOCH ::: 27
Training Net: 100% 1943/1943 [00:47<00:00, 40.81it/s, Loss_pi=3.43e-01, Loss_v=5.79e-02]
EPOCH ::: 28
Training Net: 100% 1943/1943 [00:47<00:00, 41.10it/s, Loss_pi=3.45e-01, Loss_v=5.81e-02]
EPOCH ::: 29
Training Net: 100% 1943/1943 [00:47<00:00, 41.22it/s, Loss_pi=3.39e-01, Loss_v=5.73e-02]
EPOCH ::: 30
Training Net: 100% 1943/1943 [00:47<00:00, 41.20it/s, Loss_pi=3.38e-01, Loss_v=5.72e-02]
2024-05-15 17:58:14 ae73d31ad80f Coach[3154] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [33:40<00:00, 101.04s/it]
Arena.playGames (2): 100% 20/20 [31:13<00:00, 93.65s/it]
2024-05-15 19:03:08 ae73d31ad80f Coach[3154] INFO NEW/PREV WINS : 10 / 16 ; DRAWS : 14
2024-05-15 19:03:08 ae73d31ad80f Coach[3154] INFO REJECTING NEW MODEL
2024-05-15 19:03:08 ae73d31ad80f Coach[3154] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [3:12:15<00:00, 115.36s/it]









wandb: Currently logged in as: cemgulec (cem-gulec). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /content/drive/MyDrive/dama_project/wandb/run-20240515_233236-fzoz27l8
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Run 6
wandb: ⭐️ View project at https://wandb.ai/cem-gulec/dama-project
wandb: 🚀 View run at https://wandb.ai/cem-gulec/dama-project/runs/fzoz27l8
2024-05-15 23:32:37 2e7ca0b28b30 __main__[2469] INFO Loading Dama...
2024-05-15 23:32:37 2e7ca0b28b30 __main__[2469] INFO Loading NNetWrapper...
2024-05-15 23:32:37 2e7ca0b28b30 __main__[2469] INFO Loading checkpoint "./temp//checkpoint_2.pth.tar"...
2024-05-15 23:32:40 2e7ca0b28b30 __main__[2469] INFO Loading the Coach...
2024-05-15 23:32:40 2e7ca0b28b30 __main__[2469] INFO Loading 'trainExamples' from file...
2024-05-15 23:32:40 2e7ca0b28b30 Coach[2469] INFO File with trainExamples found. Loading it...
2024-05-15 23:33:07 2e7ca0b28b30 Coach[2469] INFO Loading done!
2024-05-15 23:33:07 2e7ca0b28b30 __main__[2469] INFO Starting the learning process 🎉
2024-05-15 23:33:07 2e7ca0b28b30 Coach[2469] INFO Starting Iter #1 ...
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2059/2059 [00:50<00:00, 40.96it/s, Loss_pi=5.91e-01, Loss_v=1.09e-01]
EPOCH ::: 2
Training Net: 100% 2059/2059 [00:46<00:00, 43.92it/s, Loss_pi=4.92e-01, Loss_v=9.58e-02]
EPOCH ::: 3
Training Net: 100% 2059/2059 [00:46<00:00, 43.95it/s, Loss_pi=4.43e-01, Loss_v=8.68e-02]
EPOCH ::: 4
Training Net: 100% 2059/2059 [00:46<00:00, 44.04it/s, Loss_pi=4.16e-01, Loss_v=8.33e-02]
EPOCH ::: 5
Training Net: 100% 2059/2059 [00:46<00:00, 43.96it/s, Loss_pi=4.04e-01, Loss_v=7.93e-02]
EPOCH ::: 6
Training Net: 100% 2059/2059 [00:46<00:00, 44.30it/s, Loss_pi=3.90e-01, Loss_v=7.53e-02]
EPOCH ::: 7
Training Net: 100% 2059/2059 [00:46<00:00, 44.48it/s, Loss_pi=3.84e-01, Loss_v=7.36e-02]
EPOCH ::: 8
Training Net: 100% 2059/2059 [00:46<00:00, 44.17it/s, Loss_pi=3.75e-01, Loss_v=7.13e-02]
EPOCH ::: 9
Training Net: 100% 2059/2059 [00:46<00:00, 43.86it/s, Loss_pi=3.69e-01, Loss_v=6.95e-02]
EPOCH ::: 10
Training Net: 100% 2059/2059 [00:47<00:00, 43.74it/s, Loss_pi=3.72e-01, Loss_v=6.73e-02]
EPOCH ::: 11
Training Net: 100% 2059/2059 [00:46<00:00, 44.34it/s, Loss_pi=3.67e-01, Loss_v=6.63e-02]
EPOCH ::: 12
Training Net: 100% 2059/2059 [00:46<00:00, 44.58it/s, Loss_pi=3.67e-01, Loss_v=6.63e-02]
EPOCH ::: 13
Training Net: 100% 2059/2059 [00:46<00:00, 44.29it/s, Loss_pi=3.63e-01, Loss_v=6.63e-02]
EPOCH ::: 14
Training Net: 100% 2059/2059 [00:47<00:00, 43.78it/s, Loss_pi=3.60e-01, Loss_v=6.48e-02]
EPOCH ::: 15
Training Net: 100% 2059/2059 [00:46<00:00, 44.38it/s, Loss_pi=3.60e-01, Loss_v=6.40e-02]
EPOCH ::: 16
Training Net: 100% 2059/2059 [00:46<00:00, 44.13it/s, Loss_pi=3.60e-01, Loss_v=6.32e-02]
EPOCH ::: 17
Training Net: 100% 2059/2059 [00:48<00:00, 42.19it/s, Loss_pi=3.56e-01, Loss_v=6.28e-02]
EPOCH ::: 18
Training Net: 100% 2059/2059 [00:47<00:00, 43.79it/s, Loss_pi=3.55e-01, Loss_v=6.18e-02]
EPOCH ::: 19
Training Net: 100% 2059/2059 [00:46<00:00, 43.88it/s, Loss_pi=3.52e-01, Loss_v=6.10e-02]
EPOCH ::: 20
Training Net: 100% 2059/2059 [00:46<00:00, 44.22it/s, Loss_pi=3.53e-01, Loss_v=5.98e-02]
EPOCH ::: 21
Training Net: 100% 2059/2059 [00:46<00:00, 43.83it/s, Loss_pi=3.50e-01, Loss_v=5.95e-02]
EPOCH ::: 22
Training Net: 100% 2059/2059 [00:46<00:00, 44.30it/s, Loss_pi=3.49e-01, Loss_v=5.94e-02]
EPOCH ::: 23
Training Net: 100% 2059/2059 [00:47<00:00, 43.56it/s, Loss_pi=3.45e-01, Loss_v=6.01e-02]
EPOCH ::: 24
Training Net: 100% 2059/2059 [00:46<00:00, 44.50it/s, Loss_pi=3.42e-01, Loss_v=5.86e-02]
EPOCH ::: 25
Training Net: 100% 2059/2059 [00:46<00:00, 44.22it/s, Loss_pi=3.46e-01, Loss_v=5.91e-02]
EPOCH ::: 26
Training Net: 100% 2059/2059 [00:46<00:00, 44.43it/s, Loss_pi=3.42e-01, Loss_v=5.82e-02]
EPOCH ::: 27
Training Net: 100% 2059/2059 [00:46<00:00, 44.15it/s, Loss_pi=3.43e-01, Loss_v=5.82e-02]
EPOCH ::: 28
Training Net: 100% 2059/2059 [00:46<00:00, 44.19it/s, Loss_pi=3.42e-01, Loss_v=5.82e-02]
EPOCH ::: 29
Training Net: 100% 2059/2059 [00:46<00:00, 44.52it/s, Loss_pi=3.41e-01, Loss_v=5.66e-02]
EPOCH ::: 30
Training Net: 100% 2059/2059 [00:46<00:00, 44.37it/s, Loss_pi=3.46e-01, Loss_v=5.71e-02]
2024-05-15 23:56:54 2e7ca0b28b30 Coach[2469] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [32:40<00:00, 98.04s/it] 
Arena.playGames (2): 100% 20/20 [32:12<00:00, 96.62s/it]
2024-05-16 01:01:47 2e7ca0b28b30 Coach[2469] INFO NEW/PREV WINS : 17 / 10 ; DRAWS : 13
2024-05-16 01:01:47 2e7ca0b28b30 Coach[2469] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-16 01:01:52 2e7ca0b28b30 Coach[2469] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [3:14:43<00:00, 116.84s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2178/2178 [00:53<00:00, 40.47it/s, Loss_pi=4.20e-01, Loss_v=7.37e-02]
EPOCH ::: 2
Training Net: 100% 2178/2178 [00:50<00:00, 42.88it/s, Loss_pi=3.78e-01, Loss_v=6.95e-02]
EPOCH ::: 3
Training Net: 100% 2178/2178 [00:51<00:00, 42.67it/s, Loss_pi=3.58e-01, Loss_v=6.76e-02]
EPOCH ::: 4
Training Net: 100% 2178/2178 [00:52<00:00, 41.51it/s, Loss_pi=3.55e-01, Loss_v=6.50e-02]
EPOCH ::: 5
Training Net: 100% 2178/2178 [00:50<00:00, 42.94it/s, Loss_pi=3.47e-01, Loss_v=6.39e-02]
EPOCH ::: 6
Training Net: 100% 2178/2178 [00:50<00:00, 43.26it/s, Loss_pi=3.43e-01, Loss_v=6.09e-02]
EPOCH ::: 7
Training Net: 100% 2178/2178 [00:52<00:00, 41.44it/s, Loss_pi=3.45e-01, Loss_v=6.07e-02]
EPOCH ::: 8
Training Net: 100% 2178/2178 [00:50<00:00, 42.92it/s, Loss_pi=3.40e-01, Loss_v=6.06e-02]
EPOCH ::: 9
Training Net: 100% 2178/2178 [00:50<00:00, 43.15it/s, Loss_pi=3.41e-01, Loss_v=5.92e-02]
EPOCH ::: 10
Training Net: 100% 2178/2178 [00:53<00:00, 40.82it/s, Loss_pi=3.39e-01, Loss_v=5.94e-02]
EPOCH ::: 11
Training Net: 100% 2178/2178 [00:51<00:00, 41.92it/s, Loss_pi=3.40e-01, Loss_v=5.67e-02]
EPOCH ::: 12
Training Net: 100% 2178/2178 [00:51<00:00, 42.68it/s, Loss_pi=3.36e-01, Loss_v=5.92e-02]
EPOCH ::: 13
Training Net: 100% 2178/2178 [00:52<00:00, 41.80it/s, Loss_pi=3.36e-01, Loss_v=5.63e-02]
EPOCH ::: 14
Training Net: 100% 2178/2178 [00:52<00:00, 41.58it/s, Loss_pi=3.38e-01, Loss_v=5.85e-02]
EPOCH ::: 15
Training Net: 100% 2178/2178 [00:50<00:00, 42.84it/s, Loss_pi=3.35e-01, Loss_v=5.66e-02]
EPOCH ::: 16
Training Net: 100% 2178/2178 [00:51<00:00, 42.41it/s, Loss_pi=3.35e-01, Loss_v=5.66e-02]
EPOCH ::: 17
Training Net: 100% 2178/2178 [00:52<00:00, 41.69it/s, Loss_pi=3.34e-01, Loss_v=5.66e-02]
EPOCH ::: 18
Training Net: 100% 2178/2178 [00:50<00:00, 42.81it/s, Loss_pi=3.37e-01, Loss_v=5.61e-02]
EPOCH ::: 19
Training Net: 100% 2178/2178 [00:51<00:00, 42.48it/s, Loss_pi=3.30e-01, Loss_v=5.50e-02]
EPOCH ::: 20
Training Net: 100% 2178/2178 [00:52<00:00, 41.21it/s, Loss_pi=3.31e-01, Loss_v=5.49e-02]
EPOCH ::: 21
Training Net: 100% 2178/2178 [00:50<00:00, 42.83it/s, Loss_pi=3.32e-01, Loss_v=5.38e-02]
EPOCH ::: 22
Training Net: 100% 2178/2178 [00:51<00:00, 42.27it/s, Loss_pi=3.28e-01, Loss_v=5.38e-02]
EPOCH ::: 23
Training Net: 100% 2178/2178 [00:52<00:00, 41.64it/s, Loss_pi=3.30e-01, Loss_v=5.41e-02]
EPOCH ::: 24
Training Net: 100% 2178/2178 [00:50<00:00, 42.87it/s, Loss_pi=3.30e-01, Loss_v=5.40e-02]
EPOCH ::: 25
Training Net: 100% 2178/2178 [00:51<00:00, 42.61it/s, Loss_pi=3.24e-01, Loss_v=5.28e-02]
EPOCH ::: 26
Training Net: 100% 2178/2178 [00:52<00:00, 41.45it/s, Loss_pi=3.27e-01, Loss_v=5.33e-02]
EPOCH ::: 27
Training Net: 100% 2178/2178 [00:50<00:00, 42.81it/s, Loss_pi=3.28e-01, Loss_v=5.33e-02]
EPOCH ::: 28
Training Net: 100% 2178/2178 [00:51<00:00, 42.39it/s, Loss_pi=3.28e-01, Loss_v=5.44e-02]
EPOCH ::: 29
Training Net: 100% 2178/2178 [00:52<00:00, 41.40it/s, Loss_pi=3.24e-01, Loss_v=5.30e-02]
EPOCH ::: 30
Training Net: 100% 2178/2178 [00:50<00:00, 42.76it/s, Loss_pi=3.25e-01, Loss_v=5.39e-02]
2024-05-16 04:42:53 2e7ca0b28b30 Coach[2469] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [33:25<00:00, 100.30s/it]
Arena.playGames (2): 100% 20/20 [31:56<00:00, 95.82s/it]
2024-05-16 05:48:16 2e7ca0b28b30 Coach[2469] INFO NEW/PREV WINS : 8 / 15 ; DRAWS : 17
2024-05-16 05:48:16 2e7ca0b28b30 Coach[2469] INFO REJECTING NEW MODEL
2024-05-16 05:48:16 2e7ca0b28b30 Coach[2469] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [3:15:14<00:00, 117.14s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2298/2298 [00:59<00:00, 38.89it/s, Loss_pi=4.84e-01, Loss_v=8.66e-02]
EPOCH ::: 2
Training Net: 100% 2298/2298 [00:57<00:00, 40.07it/s, Loss_pi=4.21e-01, Loss_v=7.96e-02]
EPOCH ::: 3
Training Net: 100% 2298/2298 [00:56<00:00, 40.96it/s, Loss_pi=3.86e-01, Loss_v=7.44e-02]
EPOCH ::: 4
Training Net: 100% 2298/2298 [00:55<00:00, 41.20it/s, Loss_pi=3.72e-01, Loss_v=7.02e-02]
EPOCH ::: 5
Training Net: 100% 2298/2298 [00:56<00:00, 40.96it/s, Loss_pi=3.63e-01, Loss_v=6.79e-02]
EPOCH ::: 6
Training Net: 100% 2298/2298 [00:55<00:00, 41.40it/s, Loss_pi=3.58e-01, Loss_v=6.53e-02]
EPOCH ::: 7
Training Net: 100% 2298/2298 [00:56<00:00, 40.79it/s, Loss_pi=3.49e-01, Loss_v=6.35e-02]
EPOCH ::: 8
Training Net: 100% 2298/2298 [00:56<00:00, 40.74it/s, Loss_pi=3.48e-01, Loss_v=6.33e-02]
EPOCH ::: 9
Training Net: 100% 2298/2298 [00:56<00:00, 41.00it/s, Loss_pi=3.44e-01, Loss_v=6.15e-02]
EPOCH ::: 10
Training Net: 100% 2298/2298 [00:56<00:00, 40.97it/s, Loss_pi=3.45e-01, Loss_v=6.06e-02]
EPOCH ::: 11
Training Net: 100% 2298/2298 [00:55<00:00, 41.15it/s, Loss_pi=3.41e-01, Loss_v=5.93e-02]
EPOCH ::: 12
Training Net: 100% 2298/2298 [00:55<00:00, 41.11it/s, Loss_pi=3.41e-01, Loss_v=5.86e-02]
EPOCH ::: 13
Training Net: 100% 2298/2298 [00:56<00:00, 40.95it/s, Loss_pi=3.42e-01, Loss_v=5.96e-02]
EPOCH ::: 14
Training Net: 100% 2298/2298 [00:55<00:00, 41.17it/s, Loss_pi=3.41e-01, Loss_v=5.87e-02]
EPOCH ::: 15
Training Net: 100% 2298/2298 [00:56<00:00, 40.80it/s, Loss_pi=3.37e-01, Loss_v=5.76e-02]
EPOCH ::: 16
Training Net: 100% 2298/2298 [00:56<00:00, 40.88it/s, Loss_pi=3.38e-01, Loss_v=5.73e-02]
EPOCH ::: 17
Training Net: 100% 2298/2298 [00:56<00:00, 40.97it/s, Loss_pi=3.34e-01, Loss_v=5.62e-02]
EPOCH ::: 18
Training Net: 100% 2298/2298 [00:55<00:00, 41.15it/s, Loss_pi=3.35e-01, Loss_v=5.61e-02]
EPOCH ::: 19
Training Net: 100% 2298/2298 [00:56<00:00, 41.02it/s, Loss_pi=3.39e-01, Loss_v=5.56e-02]
EPOCH ::: 20
Training Net: 100% 2298/2298 [00:55<00:00, 41.10it/s, Loss_pi=3.35e-01, Loss_v=5.57e-02]
EPOCH ::: 21
Training Net: 100% 2298/2298 [00:56<00:00, 41.03it/s, Loss_pi=3.36e-01, Loss_v=5.55e-02]
EPOCH ::: 22
Training Net: 100% 2298/2298 [00:56<00:00, 40.77it/s, Loss_pi=3.29e-01, Loss_v=5.49e-02]
EPOCH ::: 23
Training Net: 100% 2298/2298 [00:56<00:00, 40.85it/s, Loss_pi=3.30e-01, Loss_v=5.39e-02]
EPOCH ::: 24
Training Net: 100% 2298/2298 [00:55<00:00, 41.15it/s, Loss_pi=3.31e-01, Loss_v=5.44e-02]
EPOCH ::: 25
Training Net: 100% 2298/2298 [00:56<00:00, 40.93it/s, Loss_pi=3.30e-01, Loss_v=5.49e-02]
EPOCH ::: 26
Training Net: 100% 2298/2298 [00:56<00:00, 40.97it/s, Loss_pi=3.30e-01, Loss_v=5.42e-02]
EPOCH ::: 27
Training Net: 100% 2298/2298 [00:56<00:00, 40.85it/s, Loss_pi=3.32e-01, Loss_v=5.48e-02]
EPOCH ::: 28
Training Net: 100% 2298/2298 [00:56<00:00, 40.71it/s, Loss_pi=3.30e-01, Loss_v=5.34e-02]
EPOCH ::: 29
Training Net: 100% 2298/2298 [00:56<00:00, 41.00it/s, Loss_pi=3.30e-01, Loss_v=5.29e-02]
EPOCH ::: 30
Training Net: 100% 2298/2298 [00:55<00:00, 41.09it/s, Loss_pi=3.30e-01, Loss_v=5.32e-02]
2024-05-16 09:32:04 2e7ca0b28b30 Coach[2469] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [35:00<00:00, 105.03s/it]
Arena.playGames (2): 100% 20/20 [32:05<00:00, 96.28s/it]
2024-05-16 10:39:10 2e7ca0b28b30 Coach[2469] INFO NEW/PREV WINS : 8 / 16 ; DRAWS : 16
2024-05-16 10:39:10 2e7ca0b28b30 Coach[2469] INFO REJECTING NEW MODEL
2024-05-16 10:39:10 2e7ca0b28b30 Coach[2469] INFO Starting Iter #4 ...
Self Play: 100% 100/100 [3:21:13<00:00, 120.74s/it]
2024-05-16 14:00:24 2e7ca0b28b30 Coach[2469] WARNING Removing the oldest entry in trainExamples. len(trainExamplesHistory) = 21
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2332/2332 [01:02<00:00, 37.09it/s, Loss_pi=5.27e-01, Loss_v=1.01e-01]
EPOCH ::: 2
Training Net: 100% 2332/2332 [00:58<00:00, 39.76it/s, Loss_pi=4.34e-01, Loss_v=9.04e-02]
EPOCH ::: 3
Training Net: 100% 2332/2332 [00:58<00:00, 40.07it/s, Loss_pi=3.93e-01, Loss_v=8.36e-02]
EPOCH ::: 4
Training Net: 100% 2332/2332 [00:58<00:00, 40.09it/s, Loss_pi=3.72e-01, Loss_v=7.81e-02]
EPOCH ::: 5
Training Net: 100% 2332/2332 [00:57<00:00, 40.41it/s, Loss_pi=3.55e-01, Loss_v=7.54e-02]
EPOCH ::: 6
Training Net: 100% 2332/2332 [00:58<00:00, 40.11it/s, Loss_pi=3.45e-01, Loss_v=7.10e-02]
EPOCH ::: 7
Training Net: 100% 2332/2332 [00:57<00:00, 40.39it/s, Loss_pi=3.41e-01, Loss_v=6.96e-02]
EPOCH ::: 8
Training Net: 100% 2332/2332 [00:57<00:00, 40.45it/s, Loss_pi=3.37e-01, Loss_v=6.64e-02]
EPOCH ::: 9
Training Net: 100% 2332/2332 [00:57<00:00, 40.39it/s, Loss_pi=3.34e-01, Loss_v=6.52e-02]
EPOCH ::: 10
Training Net: 100% 2332/2332 [00:57<00:00, 40.59it/s, Loss_pi=3.30e-01, Loss_v=6.45e-02]
EPOCH ::: 11
Training Net: 100% 2332/2332 [00:57<00:00, 40.68it/s, Loss_pi=3.27e-01, Loss_v=6.24e-02]
EPOCH ::: 12
Training Net: 100% 2332/2332 [00:58<00:00, 39.85it/s, Loss_pi=3.29e-01, Loss_v=6.18e-02]
EPOCH ::: 13
Training Net: 100% 2332/2332 [00:57<00:00, 40.31it/s, Loss_pi=3.26e-01, Loss_v=6.07e-02]
EPOCH ::: 14
Training Net: 100% 2332/2332 [00:58<00:00, 40.04it/s, Loss_pi=3.24e-01, Loss_v=5.96e-02]
EPOCH ::: 15
Training Net: 100% 2332/2332 [00:57<00:00, 40.43it/s, Loss_pi=3.25e-01, Loss_v=5.89e-02]
EPOCH ::: 16
Training Net: 100% 2332/2332 [00:58<00:00, 40.01it/s, Loss_pi=3.22e-01, Loss_v=5.73e-02]
EPOCH ::: 17
Training Net: 100% 2332/2332 [00:58<00:00, 39.80it/s, Loss_pi=3.22e-01, Loss_v=5.71e-02]
EPOCH ::: 18
Training Net: 100% 2332/2332 [00:58<00:00, 40.13it/s, Loss_pi=3.19e-01, Loss_v=5.72e-02]
EPOCH ::: 19
Training Net: 100% 2332/2332 [00:58<00:00, 39.67it/s, Loss_pi=3.16e-01, Loss_v=5.68e-02]
EPOCH ::: 20
Training Net: 100% 2332/2332 [00:58<00:00, 40.20it/s, Loss_pi=3.16e-01, Loss_v=5.60e-02]
EPOCH ::: 21
Training Net: 100% 2332/2332 [00:59<00:00, 39.44it/s, Loss_pi=3.16e-01, Loss_v=5.63e-02]
EPOCH ::: 22
Training Net: 100% 2332/2332 [01:00<00:00, 38.74it/s, Loss_pi=3.17e-01, Loss_v=5.54e-02]
EPOCH ::: 23
Training Net: 100% 2332/2332 [00:58<00:00, 40.06it/s, Loss_pi=3.16e-01, Loss_v=5.58e-02]
EPOCH ::: 24
Training Net: 100% 2332/2332 [00:57<00:00, 40.67it/s, Loss_pi=3.12e-01, Loss_v=5.43e-02]
EPOCH ::: 25
Training Net: 100% 2332/2332 [00:59<00:00, 39.29it/s, Loss_pi=3.12e-01, Loss_v=5.41e-02]
EPOCH ::: 26
Training Net: 100% 2332/2332 [00:59<00:00, 39.29it/s, Loss_pi=3.12e-01, Loss_v=5.42e-02]
EPOCH ::: 27
Training Net: 100% 2332/2332 [00:58<00:00, 40.08it/s, Loss_pi=3.11e-01, Loss_v=5.31e-02]
EPOCH ::: 28
Training Net: 100% 2332/2332 [00:56<00:00, 41.12it/s, Loss_pi=3.11e-01, Loss_v=5.32e-02]
EPOCH ::: 29
Training Net: 100% 2332/2332 [00:56<00:00, 41.39it/s, Loss_pi=3.14e-01, Loss_v=5.42e-02]
EPOCH ::: 30
Training Net: 100% 2332/2332 [00:56<00:00, 41.27it/s, Loss_pi=3.10e-01, Loss_v=5.31e-02]
2024-05-16 14:30:03 2e7ca0b28b30 Coach[2469] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [34:39<00:00, 103.99s/it]
Arena.playGames (2): 100% 20/20 [37:36<00:00, 112.84s/it]
2024-05-16 15:42:19 2e7ca0b28b30 Coach[2469] INFO NEW/PREV WINS : 11 / 6 ; DRAWS : 23
2024-05-16 15:42:19 2e7ca0b28b30 Coach[2469] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-16 15:42:20 2e7ca0b28b30 Coach[2469] INFO Starting Iter #5 ...
Self Play: 100% 100/100 [3:15:40<00:00, 117.40s/it]




wandb: Currently logged in as: cemgulec (cem-gulec). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /content/drive/MyDrive/dama_project/wandb/run-20240517_235336-xwmi55i5
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Run 7
wandb: ⭐️ View project at https://wandb.ai/cem-gulec/dama-project
wandb: 🚀 View run at https://wandb.ai/cem-gulec/dama-project/runs/xwmi55i5
2024-05-17 23:53:37 fbc3c36d388a __main__[5357] INFO Loading Dama...
2024-05-17 23:53:37 fbc3c36d388a __main__[5357] INFO Loading NNetWrapper...
2024-05-17 23:53:37 fbc3c36d388a __main__[5357] INFO Loading checkpoint "./temp//checkpoint_4.pth.tar"...
2024-05-17 23:53:42 fbc3c36d388a __main__[5357] INFO Loading the Coach...
2024-05-17 23:53:42 fbc3c36d388a __main__[5357] INFO Loading 'trainExamples' from file...
2024-05-17 23:53:42 fbc3c36d388a Coach[5357] INFO File with trainExamples found. Loading it...
2024-05-17 23:54:22 fbc3c36d388a Coach[5357] INFO Loading done!
2024-05-17 23:54:22 fbc3c36d388a __main__[5357] INFO Starting the learning process 🎉
2024-05-17 23:54:22 fbc3c36d388a Coach[5357] INFO Starting Iter #1 ...
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2366/2366 [01:00<00:00, 39.18it/s, Loss_pi=3.61e-01, Loss_v=6.52e-02]
EPOCH ::: 2
Training Net: 100% 2366/2366 [00:57<00:00, 40.93it/s, Loss_pi=3.24e-01, Loss_v=6.26e-02]
EPOCH ::: 3
Training Net: 100% 2366/2366 [00:57<00:00, 41.05it/s, Loss_pi=3.12e-01, Loss_v=5.94e-02]
EPOCH ::: 4
Training Net: 100% 2366/2366 [00:57<00:00, 40.97it/s, Loss_pi=3.01e-01, Loss_v=5.83e-02]
EPOCH ::: 5
Training Net: 100% 2366/2366 [00:57<00:00, 41.06it/s, Loss_pi=2.99e-01, Loss_v=5.62e-02]
EPOCH ::: 6
Training Net: 100% 2366/2366 [00:57<00:00, 41.05it/s, Loss_pi=2.99e-01, Loss_v=5.64e-02]
EPOCH ::: 7
Training Net: 100% 2366/2366 [00:57<00:00, 40.95it/s, Loss_pi=2.98e-01, Loss_v=5.57e-02]
EPOCH ::: 8
Training Net: 100% 2366/2366 [00:57<00:00, 41.10it/s, Loss_pi=2.93e-01, Loss_v=5.31e-02]
EPOCH ::: 9
Training Net: 100% 2366/2366 [00:57<00:00, 41.09it/s, Loss_pi=2.92e-01, Loss_v=5.34e-02]
EPOCH ::: 10
Training Net: 100% 2366/2366 [00:57<00:00, 41.06it/s, Loss_pi=2.94e-01, Loss_v=5.38e-02]
EPOCH ::: 11
Training Net: 100% 2366/2366 [00:57<00:00, 40.98it/s, Loss_pi=2.90e-01, Loss_v=5.24e-02]
EPOCH ::: 12
Training Net: 100% 2366/2366 [00:57<00:00, 41.17it/s, Loss_pi=2.88e-01, Loss_v=5.10e-02]
EPOCH ::: 13
Training Net: 100% 2366/2366 [00:57<00:00, 41.06it/s, Loss_pi=2.88e-01, Loss_v=5.21e-02]
EPOCH ::: 14
Training Net: 100% 2366/2366 [00:57<00:00, 41.17it/s, Loss_pi=2.90e-01, Loss_v=5.12e-02]
EPOCH ::: 15
Training Net: 100% 2366/2366 [00:57<00:00, 41.15it/s, Loss_pi=2.87e-01, Loss_v=5.04e-02]
EPOCH ::: 16
Training Net: 100% 2366/2366 [00:57<00:00, 40.98it/s, Loss_pi=2.86e-01, Loss_v=5.00e-02]
EPOCH ::: 17
Training Net: 100% 2366/2366 [00:57<00:00, 40.80it/s, Loss_pi=2.83e-01, Loss_v=5.05e-02]
EPOCH ::: 18
Training Net: 100% 2366/2366 [00:58<00:00, 40.59it/s, Loss_pi=2.85e-01, Loss_v=5.12e-02]
EPOCH ::: 19
Training Net: 100% 2366/2366 [00:58<00:00, 40.75it/s, Loss_pi=2.86e-01, Loss_v=5.10e-02]
EPOCH ::: 20
Training Net: 100% 2366/2366 [00:57<00:00, 40.86it/s, Loss_pi=2.86e-01, Loss_v=4.92e-02]
EPOCH ::: 21
Training Net: 100% 2366/2366 [00:57<00:00, 40.86it/s, Loss_pi=2.83e-01, Loss_v=5.08e-02]
EPOCH ::: 22
Training Net: 100% 2366/2366 [00:57<00:00, 40.89it/s, Loss_pi=2.83e-01, Loss_v=5.02e-02]
EPOCH ::: 23
Training Net: 100% 2366/2366 [00:57<00:00, 40.90it/s, Loss_pi=2.87e-01, Loss_v=5.00e-02]
EPOCH ::: 24
Training Net: 100% 2366/2366 [00:57<00:00, 40.92it/s, Loss_pi=2.83e-01, Loss_v=4.90e-02]
EPOCH ::: 25
Training Net: 100% 2366/2366 [00:57<00:00, 41.06it/s, Loss_pi=2.85e-01, Loss_v=4.93e-02]
EPOCH ::: 26
Training Net: 100% 2366/2366 [00:57<00:00, 41.05it/s, Loss_pi=2.80e-01, Loss_v=4.91e-02]
EPOCH ::: 27
Training Net: 100% 2366/2366 [00:57<00:00, 40.95it/s, Loss_pi=2.81e-01, Loss_v=4.92e-02]
EPOCH ::: 28
Training Net: 100% 2366/2366 [00:57<00:00, 41.06it/s, Loss_pi=2.83e-01, Loss_v=4.82e-02]
EPOCH ::: 29
Training Net: 100% 2366/2366 [00:57<00:00, 41.04it/s, Loss_pi=2.84e-01, Loss_v=4.96e-02]
EPOCH ::: 30
Training Net: 100% 2366/2366 [00:57<00:00, 40.96it/s, Loss_pi=2.79e-01, Loss_v=4.83e-02]
2024-05-18 00:24:26 fbc3c36d388a Coach[5357] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [45:39<00:00, 136.97s/it]
Arena.playGames (2): 100% 20/20 [37:58<00:00, 113.93s/it]
2024-05-18 01:48:04 fbc3c36d388a Coach[5357] INFO NEW/PREV WINS : 10 / 8 ; DRAWS : 22
2024-05-18 01:48:04 fbc3c36d388a Coach[5357] INFO REJECTING NEW MODEL
2024-05-18 01:48:04 fbc3c36d388a Coach[5357] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [3:29:22<00:00, 125.63s/it]
2024-05-18 05:17:27 fbc3c36d388a Coach[5357] WARNING Removing the oldest entry in trainExamples. len(trainExamplesHistory) = 21
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2373/2373 [01:00<00:00, 39.37it/s, Loss_pi=4.17e-01, Loss_v=7.65e-02]
EPOCH ::: 2
Training Net: 100% 2373/2373 [00:58<00:00, 40.39it/s, Loss_pi=3.65e-01, Loss_v=7.02e-02]
EPOCH ::: 3
Training Net: 100% 2373/2373 [00:58<00:00, 40.59it/s, Loss_pi=3.36e-01, Loss_v=6.61e-02]
EPOCH ::: 4
Training Net: 100% 2373/2373 [00:59<00:00, 39.93it/s, Loss_pi=3.20e-01, Loss_v=6.28e-02]
EPOCH ::: 5
Training Net: 100% 2373/2373 [00:58<00:00, 40.39it/s, Loss_pi=3.11e-01, Loss_v=6.11e-02]
EPOCH ::: 6
Training Net: 100% 2373/2373 [00:58<00:00, 40.34it/s, Loss_pi=3.05e-01, Loss_v=5.93e-02]
EPOCH ::: 7
Training Net: 100% 2373/2373 [00:59<00:00, 40.07it/s, Loss_pi=3.06e-01, Loss_v=5.92e-02]
EPOCH ::: 8
Training Net: 100% 2373/2373 [00:59<00:00, 39.65it/s, Loss_pi=2.99e-01, Loss_v=5.70e-02]
EPOCH ::: 9
Training Net: 100% 2373/2373 [01:00<00:00, 39.14it/s, Loss_pi=2.99e-01, Loss_v=5.50e-02]
EPOCH ::: 10
Training Net: 100% 2373/2373 [00:59<00:00, 39.64it/s, Loss_pi=2.97e-01, Loss_v=5.54e-02]
EPOCH ::: 11
Training Net: 100% 2373/2373 [00:59<00:00, 39.97it/s, Loss_pi=2.94e-01, Loss_v=5.31e-02]
EPOCH ::: 12
Training Net: 100% 2373/2373 [00:59<00:00, 39.86it/s, Loss_pi=2.94e-01, Loss_v=5.22e-02]
EPOCH ::: 13
Training Net: 100% 2373/2373 [00:59<00:00, 39.90it/s, Loss_pi=2.93e-01, Loss_v=5.27e-02]
EPOCH ::: 14
Training Net: 100% 2373/2373 [00:59<00:00, 39.77it/s, Loss_pi=2.92e-01, Loss_v=5.19e-02]
EPOCH ::: 15
Training Net: 100% 2373/2373 [00:59<00:00, 39.97it/s, Loss_pi=2.96e-01, Loss_v=5.10e-02]
EPOCH ::: 16
Training Net: 100% 2373/2373 [00:59<00:00, 39.96it/s, Loss_pi=2.89e-01, Loss_v=5.07e-02]
EPOCH ::: 17
Training Net: 100% 2373/2373 [00:59<00:00, 39.98it/s, Loss_pi=2.91e-01, Loss_v=5.06e-02]
EPOCH ::: 18
Training Net: 100% 2373/2373 [00:59<00:00, 39.84it/s, Loss_pi=2.90e-01, Loss_v=5.00e-02]
EPOCH ::: 19
Training Net: 100% 2373/2373 [00:59<00:00, 39.90it/s, Loss_pi=2.89e-01, Loss_v=4.93e-02]
EPOCH ::: 20
Training Net: 100% 2373/2373 [00:59<00:00, 39.99it/s, Loss_pi=2.88e-01, Loss_v=4.91e-02]
EPOCH ::: 21
Training Net: 100% 2373/2373 [00:59<00:00, 39.91it/s, Loss_pi=2.86e-01, Loss_v=4.95e-02]
EPOCH ::: 22
Training Net: 100% 2373/2373 [00:59<00:00, 39.76it/s, Loss_pi=2.88e-01, Loss_v=4.99e-02]
EPOCH ::: 23
Training Net: 100% 2373/2373 [00:59<00:00, 39.73it/s, Loss_pi=2.85e-01, Loss_v=4.71e-02]
EPOCH ::: 24
Training Net: 100% 2373/2373 [00:59<00:00, 39.65it/s, Loss_pi=2.86e-01, Loss_v=4.80e-02]
EPOCH ::: 25
Training Net: 100% 2373/2373 [00:59<00:00, 39.73it/s, Loss_pi=2.86e-01, Loss_v=4.87e-02]
EPOCH ::: 26
Training Net: 100% 2373/2373 [00:59<00:00, 39.94it/s, Loss_pi=2.84e-01, Loss_v=4.92e-02]
EPOCH ::: 27
Training Net: 100% 2373/2373 [00:59<00:00, 39.86it/s, Loss_pi=2.84e-01, Loss_v=4.76e-02]
EPOCH ::: 28
Training Net: 100% 2373/2373 [00:59<00:00, 39.80it/s, Loss_pi=2.83e-01, Loss_v=4.79e-02]
EPOCH ::: 29
Training Net: 100% 2373/2373 [00:59<00:00, 39.76it/s, Loss_pi=2.85e-01, Loss_v=4.74e-02]
EPOCH ::: 30
Training Net: 100% 2373/2373 [00:59<00:00, 39.62it/s, Loss_pi=2.83e-01, Loss_v=4.75e-02]
2024-05-18 05:47:32 fbc3c36d388a Coach[5357] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [39:20<00:00, 118.04s/it]
Arena.playGames (2): 100% 20/20 [38:49<00:00, 116.49s/it]
2024-05-18 07:05:42 fbc3c36d388a Coach[5357] INFO NEW/PREV WINS : 13 / 11 ; DRAWS : 16
2024-05-18 07:05:42 fbc3c36d388a Coach[5357] INFO REJECTING NEW MODEL
2024-05-18 07:05:42 fbc3c36d388a Coach[5357] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [3:32:40<00:00, 127.61s/it]
2024-05-18 10:38:23 fbc3c36d388a Coach[5357] WARNING Removing the oldest entry in trainExamples. len(trainExamplesHistory) = 21
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2377/2377 [00:59<00:00, 39.75it/s, Loss_pi=4.83e-01, Loss_v=8.79e-02]
EPOCH ::: 2
Training Net: 100% 2377/2377 [00:58<00:00, 40.52it/s, Loss_pi=3.96e-01, Loss_v=7.98e-02]
EPOCH ::: 3
Training Net: 100% 2377/2377 [00:58<00:00, 40.48it/s, Loss_pi=3.61e-01, Loss_v=7.37e-02]
EPOCH ::: 4
Training Net: 100% 2377/2377 [00:58<00:00, 40.64it/s, Loss_pi=3.41e-01, Loss_v=6.95e-02]
EPOCH ::: 5
Training Net: 100% 2377/2377 [00:58<00:00, 40.47it/s, Loss_pi=3.27e-01, Loss_v=6.74e-02]
EPOCH ::: 6
Training Net: 100% 2377/2377 [00:58<00:00, 40.54it/s, Loss_pi=3.16e-01, Loss_v=6.45e-02]
EPOCH ::: 7
Training Net: 100% 2377/2377 [00:58<00:00, 40.62it/s, Loss_pi=3.13e-01, Loss_v=6.23e-02]
EPOCH ::: 8
Training Net: 100% 2377/2377 [00:58<00:00, 40.47it/s, Loss_pi=3.10e-01, Loss_v=5.99e-02]
EPOCH ::: 9
Training Net: 100% 2377/2377 [00:58<00:00, 40.48it/s, Loss_pi=3.07e-01, Loss_v=5.85e-02]
EPOCH ::: 10
Training Net: 100% 2377/2377 [00:58<00:00, 40.46it/s, Loss_pi=3.01e-01, Loss_v=5.68e-02]
EPOCH ::: 11
Training Net: 100% 2377/2377 [00:58<00:00, 40.55it/s, Loss_pi=3.03e-01, Loss_v=5.61e-02]
EPOCH ::: 12
Training Net: 100% 2377/2377 [00:58<00:00, 40.32it/s, Loss_pi=2.99e-01, Loss_v=5.39e-02]
EPOCH ::: 13
Training Net: 100% 2377/2377 [00:59<00:00, 40.26it/s, Loss_pi=2.99e-01, Loss_v=5.40e-02]
EPOCH ::: 14
Training Net: 100% 2377/2377 [00:58<00:00, 40.50it/s, Loss_pi=2.98e-01, Loss_v=5.25e-02]
EPOCH ::: 15
Training Net: 100% 2377/2377 [00:58<00:00, 40.41it/s, Loss_pi=2.95e-01, Loss_v=5.09e-02]
EPOCH ::: 16
Training Net: 100% 2377/2377 [00:58<00:00, 40.53it/s, Loss_pi=2.97e-01, Loss_v=5.25e-02]
EPOCH ::: 17
Training Net: 100% 2377/2377 [00:58<00:00, 40.74it/s, Loss_pi=2.97e-01, Loss_v=5.14e-02]
EPOCH ::: 18
Training Net: 100% 2377/2377 [00:58<00:00, 40.51it/s, Loss_pi=2.96e-01, Loss_v=5.13e-02]
EPOCH ::: 19
Training Net: 100% 2377/2377 [00:58<00:00, 40.78it/s, Loss_pi=2.91e-01, Loss_v=5.01e-02]
EPOCH ::: 20
Training Net: 100% 2377/2377 [00:58<00:00, 40.63it/s, Loss_pi=2.95e-01, Loss_v=4.98e-02]
EPOCH ::: 21
Training Net: 100% 2377/2377 [00:58<00:00, 40.64it/s, Loss_pi=2.94e-01, Loss_v=4.88e-02]
EPOCH ::: 22
Training Net: 100% 2377/2377 [00:58<00:00, 40.52it/s, Loss_pi=2.91e-01, Loss_v=4.85e-02]
EPOCH ::: 23
Training Net: 100% 2377/2377 [00:58<00:00, 40.50it/s, Loss_pi=2.91e-01, Loss_v=4.93e-02]
EPOCH ::: 24
Training Net: 100% 2377/2377 [00:58<00:00, 40.39it/s, Loss_pi=2.90e-01, Loss_v=4.88e-02]
EPOCH ::: 25
Training Net: 100% 2377/2377 [00:58<00:00, 40.49it/s, Loss_pi=2.91e-01, Loss_v=4.89e-02]
EPOCH ::: 26
Training Net: 100% 2377/2377 [00:58<00:00, 40.63it/s, Loss_pi=2.89e-01, Loss_v=4.77e-02]
EPOCH ::: 27
Training Net: 100% 2377/2377 [00:58<00:00, 40.56it/s, Loss_pi=2.89e-01, Loss_v=4.72e-02]
EPOCH ::: 28
Training Net: 100% 2377/2377 [00:58<00:00, 40.42it/s, Loss_pi=2.88e-01, Loss_v=4.67e-02]
EPOCH ::: 29
Training Net: 100% 2377/2377 [00:58<00:00, 40.39it/s, Loss_pi=2.87e-01, Loss_v=4.63e-02]
EPOCH ::: 30
Training Net: 100% 2377/2377 [00:58<00:00, 40.67it/s, Loss_pi=2.87e-01, Loss_v=4.60e-02]
2024-05-18 11:08:03 fbc3c36d388a Coach[5357] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [36:37<00:00, 109.89s/it]
Arena.playGames (2): 100% 20/20 [35:36<00:00, 106.84s/it]
2024-05-18 12:20:18 fbc3c36d388a Coach[5357] INFO NEW/PREV WINS : 14 / 11 ; DRAWS : 15
2024-05-18 12:20:18 fbc3c36d388a Coach[5357] INFO REJECTING NEW MODEL
2024-05-18 12:20:18 fbc3c36d388a Coach[5357] INFO Starting Iter #4 ...
Self Play: 100% 100/100 [3:21:40<00:00, 121.00s/it]
2024-05-18 15:41:58 fbc3c36d388a Coach[5357] WARNING Removing the oldest entry in trainExamples. len(trainExamplesHistory) = 21
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2375/2375 [01:01<00:00, 38.56it/s, Loss_pi=5.32e-01, Loss_v=9.85e-02]
EPOCH ::: 2
Training Net: 100% 2375/2375 [00:59<00:00, 39.69it/s, Loss_pi=4.38e-01, Loss_v=8.67e-02]
EPOCH ::: 3
Training Net: 100% 2375/2375 [01:00<00:00, 39.26it/s, Loss_pi=3.85e-01, Loss_v=8.06e-02]
EPOCH ::: 4
Training Net: 100% 2375/2375 [01:00<00:00, 39.34it/s, Loss_pi=3.57e-01, Loss_v=7.35e-02]
EPOCH ::: 5
Training Net: 100% 2375/2375 [00:59<00:00, 39.74it/s, Loss_pi=3.41e-01, Loss_v=6.99e-02]
EPOCH ::: 6
Training Net: 100% 2375/2375 [00:59<00:00, 39.80it/s, Loss_pi=3.31e-01, Loss_v=6.73e-02]
EPOCH ::: 7
Training Net: 100% 2375/2375 [00:59<00:00, 39.96it/s, Loss_pi=3.24e-01, Loss_v=6.40e-02]
EPOCH ::: 8
Training Net: 100% 2375/2375 [00:59<00:00, 40.01it/s, Loss_pi=3.16e-01, Loss_v=6.27e-02]
EPOCH ::: 9
Training Net: 100% 2375/2375 [00:59<00:00, 39.90it/s, Loss_pi=3.14e-01, Loss_v=5.96e-02]
EPOCH ::: 10
Training Net: 100% 2375/2375 [00:59<00:00, 39.88it/s, Loss_pi=3.10e-01, Loss_v=5.82e-02]
EPOCH ::: 11
Training Net: 100% 2375/2375 [00:59<00:00, 39.70it/s, Loss_pi=3.08e-01, Loss_v=5.78e-02]
EPOCH ::: 12
Training Net: 100% 2375/2375 [00:59<00:00, 39.78it/s, Loss_pi=3.05e-01, Loss_v=5.50e-02]
EPOCH ::: 13
Training Net: 100% 2375/2375 [00:59<00:00, 39.77it/s, Loss_pi=3.05e-01, Loss_v=5.31e-02]
EPOCH ::: 14
Training Net: 100% 2375/2375 [00:59<00:00, 39.71it/s, Loss_pi=3.04e-01, Loss_v=5.38e-02]
EPOCH ::: 15
Training Net: 100% 2375/2375 [00:59<00:00, 39.96it/s, Loss_pi=3.04e-01, Loss_v=5.29e-02]
EPOCH ::: 16
Training Net: 100% 2375/2375 [00:59<00:00, 40.20it/s, Loss_pi=3.02e-01, Loss_v=5.34e-02]
EPOCH ::: 17
Training Net: 100% 2375/2375 [00:59<00:00, 39.87it/s, Loss_pi=3.02e-01, Loss_v=5.15e-02]
EPOCH ::: 18
Training Net: 100% 2375/2375 [00:59<00:00, 39.71it/s, Loss_pi=2.97e-01, Loss_v=5.14e-02]
EPOCH ::: 19
Training Net: 100% 2375/2375 [00:59<00:00, 39.72it/s, Loss_pi=2.98e-01, Loss_v=5.10e-02]
EPOCH ::: 20
Training Net: 100% 2375/2375 [00:59<00:00, 39.92it/s, Loss_pi=2.98e-01, Loss_v=4.97e-02]
EPOCH ::: 21
Training Net: 100% 2375/2375 [00:59<00:00, 39.70it/s, Loss_pi=2.96e-01, Loss_v=4.93e-02]
EPOCH ::: 22
Training Net: 100% 2375/2375 [00:59<00:00, 39.88it/s, Loss_pi=2.97e-01, Loss_v=4.89e-02]
EPOCH ::: 23
Training Net: 100% 2375/2375 [00:59<00:00, 40.00it/s, Loss_pi=2.95e-01, Loss_v=4.79e-02]
EPOCH ::: 24
Training Net: 100% 2375/2375 [00:59<00:00, 39.97it/s, Loss_pi=2.93e-01, Loss_v=4.73e-02]
EPOCH ::: 25
Training Net: 100% 2375/2375 [01:00<00:00, 39.56it/s, Loss_pi=2.93e-01, Loss_v=4.79e-02]
EPOCH ::: 26
Training Net: 100% 2375/2375 [00:59<00:00, 39.90it/s, Loss_pi=2.90e-01, Loss_v=4.65e-02]
EPOCH ::: 27
Training Net: 100% 2375/2375 [00:59<00:00, 40.21it/s, Loss_pi=2.93e-01, Loss_v=4.72e-02]
EPOCH ::: 28
Training Net: 100% 2375/2375 [00:59<00:00, 39.63it/s, Loss_pi=2.90e-01, Loss_v=4.67e-02]
EPOCH ::: 29
Training Net: 100% 2375/2375 [01:00<00:00, 39.55it/s, Loss_pi=2.94e-01, Loss_v=4.71e-02]
EPOCH ::: 30
Training Net: 100% 2375/2375 [01:00<00:00, 39.08it/s, Loss_pi=2.89e-01, Loss_v=4.61e-02]
2024-05-18 16:12:11 fbc3c36d388a Coach[5357] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [35:39<00:00, 106.99s/it]
Arena.playGames (2): 100% 20/20 [44:45<00:00, 134.27s/it]
2024-05-18 17:32:37 fbc3c36d388a Coach[5357] INFO NEW/PREV WINS : 12 / 13 ; DRAWS : 15
2024-05-18 17:32:37 fbc3c36d388a Coach[5357] INFO REJECTING NEW MODEL
2024-05-18 17:32:37 fbc3c36d388a Coach[5357] INFO Starting Iter #5 ...
Self Play: 100% 100/100 [3:32:45<00:00, 127.66s/it]






wandb: Currently logged in as: cemgulec (cem-gulec). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /content/drive/MyDrive/dama_project/wandb/run-20240519_092431-qdsiwdxw
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Run 8
wandb: ⭐️ View project at https://wandb.ai/cem-gulec/dama-project
wandb: 🚀 View run at https://wandb.ai/cem-gulec/dama-project/runs/qdsiwdxw
2024-05-19 09:24:32 4c08552d4751 __main__[2314] INFO Loading Dama...
2024-05-19 09:24:32 4c08552d4751 __main__[2314] INFO Loading NNetWrapper...
2024-05-19 09:24:32 4c08552d4751 __main__[2314] INFO Loading checkpoint "./temp//checkpoint_4.pth.tar"...
2024-05-19 09:24:37 4c08552d4751 __main__[2314] INFO Loading the Coach...
2024-05-19 09:24:37 4c08552d4751 __main__[2314] INFO Loading 'trainExamples' from file...
2024-05-19 09:24:37 4c08552d4751 Coach[2314] INFO File with trainExamples found. Loading it...
2024-05-19 09:25:05 4c08552d4751 Coach[2314] INFO Loading done!
2024-05-19 09:25:05 4c08552d4751 __main__[2314] INFO Starting the learning process 🎉
2024-05-19 09:25:05 4c08552d4751 Coach[2314] INFO Starting Iter #1 ...
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2369/2369 [00:58<00:00, 40.71it/s, Loss_pi=5.98e-01, Loss_v=1.12e-01]
EPOCH ::: 2
Training Net: 100% 2369/2369 [00:55<00:00, 42.50it/s, Loss_pi=4.71e-01, Loss_v=9.82e-02]
EPOCH ::: 3
Training Net: 100% 2369/2369 [00:55<00:00, 42.51it/s, Loss_pi=4.12e-01, Loss_v=8.98e-02]
EPOCH ::: 4
Training Net: 100% 2369/2369 [00:55<00:00, 42.59it/s, Loss_pi=3.77e-01, Loss_v=8.25e-02]
EPOCH ::: 5
Training Net: 100% 2369/2369 [00:55<00:00, 42.69it/s, Loss_pi=3.56e-01, Loss_v=7.76e-02]
EPOCH ::: 6
Training Net: 100% 2369/2369 [00:55<00:00, 42.57it/s, Loss_pi=3.43e-01, Loss_v=7.35e-02]
EPOCH ::: 7
Training Net: 100% 2369/2369 [00:56<00:00, 42.30it/s, Loss_pi=3.31e-01, Loss_v=6.92e-02]
EPOCH ::: 8
Training Net: 100% 2369/2369 [00:56<00:00, 41.77it/s, Loss_pi=3.27e-01, Loss_v=6.75e-02]
EPOCH ::: 9
Training Net: 100% 2369/2369 [00:56<00:00, 41.98it/s, Loss_pi=3.23e-01, Loss_v=6.47e-02]
EPOCH ::: 10
Training Net: 100% 2369/2369 [00:56<00:00, 42.00it/s, Loss_pi=3.16e-01, Loss_v=6.16e-02]
EPOCH ::: 11
Training Net: 100% 2369/2369 [00:56<00:00, 41.86it/s, Loss_pi=3.13e-01, Loss_v=6.09e-02]
EPOCH ::: 12
Training Net: 100% 2369/2369 [00:55<00:00, 42.51it/s, Loss_pi=3.14e-01, Loss_v=5.80e-02]
EPOCH ::: 13
Training Net: 100% 2369/2369 [00:55<00:00, 42.49it/s, Loss_pi=3.14e-01, Loss_v=5.67e-02]
EPOCH ::: 14
Training Net: 100% 2369/2369 [00:56<00:00, 42.01it/s, Loss_pi=3.11e-01, Loss_v=5.65e-02]
EPOCH ::: 15
Training Net: 100% 2369/2369 [00:56<00:00, 42.09it/s, Loss_pi=3.08e-01, Loss_v=5.53e-02]
EPOCH ::: 16
Training Net: 100% 2369/2369 [00:56<00:00, 42.18it/s, Loss_pi=3.05e-01, Loss_v=5.44e-02]
EPOCH ::: 17
Training Net: 100% 2369/2369 [00:56<00:00, 42.09it/s, Loss_pi=3.05e-01, Loss_v=5.25e-02]
EPOCH ::: 18
Training Net: 100% 2369/2369 [00:56<00:00, 42.14it/s, Loss_pi=3.06e-01, Loss_v=5.18e-02]
EPOCH ::: 19
Training Net: 100% 2369/2369 [00:56<00:00, 42.23it/s, Loss_pi=3.04e-01, Loss_v=5.15e-02]
EPOCH ::: 20
Training Net: 100% 2369/2369 [00:55<00:00, 42.46it/s, Loss_pi=3.01e-01, Loss_v=5.14e-02]
EPOCH ::: 21
Training Net: 100% 2369/2369 [00:55<00:00, 42.58it/s, Loss_pi=3.01e-01, Loss_v=5.04e-02]
EPOCH ::: 22
Training Net: 100% 2369/2369 [00:55<00:00, 42.71it/s, Loss_pi=3.01e-01, Loss_v=5.04e-02]
EPOCH ::: 23
Training Net: 100% 2369/2369 [00:56<00:00, 42.19it/s, Loss_pi=2.99e-01, Loss_v=4.89e-02]
EPOCH ::: 24
Training Net: 100% 2369/2369 [00:57<00:00, 41.41it/s, Loss_pi=2.99e-01, Loss_v=4.79e-02]
EPOCH ::: 25
Training Net: 100% 2369/2369 [00:56<00:00, 42.03it/s, Loss_pi=3.00e-01, Loss_v=4.87e-02]
EPOCH ::: 26
Training Net: 100% 2369/2369 [00:55<00:00, 42.33it/s, Loss_pi=2.97e-01, Loss_v=4.78e-02]
EPOCH ::: 27
Training Net: 100% 2369/2369 [00:55<00:00, 42.65it/s, Loss_pi=2.94e-01, Loss_v=4.80e-02]
EPOCH ::: 28
Training Net: 100% 2369/2369 [00:55<00:00, 42.51it/s, Loss_pi=2.95e-01, Loss_v=4.69e-02]
EPOCH ::: 29
Training Net: 100% 2369/2369 [00:56<00:00, 41.97it/s, Loss_pi=2.94e-01, Loss_v=4.66e-02]
EPOCH ::: 30
Training Net: 100% 2369/2369 [00:56<00:00, 42.22it/s, Loss_pi=2.92e-01, Loss_v=4.52e-02]
2024-05-19 09:53:33 4c08552d4751 Coach[2314] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [35:24<00:00, 106.20s/it]
Arena.playGames (2): 100% 20/20 [40:40<00:00, 122.01s/it]
2024-05-19 11:09:37 4c08552d4751 Coach[2314] INFO NEW/PREV WINS : 14 / 11 ; DRAWS : 15
2024-05-19 11:09:37 4c08552d4751 Coach[2314] INFO REJECTING NEW MODEL
2024-05-19 11:09:37 4c08552d4751 Coach[2314] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [3:34:52<00:00, 128.92s/it]
2024-05-19 14:44:29 4c08552d4751 Coach[2314] WARNING Removing the oldest entry in trainExamples. len(trainExamplesHistory) = 21
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2368/2368 [01:02<00:00, 38.18it/s, Loss_pi=6.51e-01, Loss_v=1.20e-01]
EPOCH ::: 2
Training Net: 100% 2368/2368 [00:59<00:00, 39.71it/s, Loss_pi=5.18e-01, Loss_v=1.06e-01]
EPOCH ::: 3
Training Net: 100% 2368/2368 [00:59<00:00, 40.04it/s, Loss_pi=4.39e-01, Loss_v=9.63e-02]
EPOCH ::: 4
Training Net: 100% 2368/2368 [00:58<00:00, 40.15it/s, Loss_pi=3.96e-01, Loss_v=8.88e-02]
EPOCH ::: 5
Training Net: 100% 2368/2368 [00:59<00:00, 39.93it/s, Loss_pi=3.74e-01, Loss_v=8.34e-02]
EPOCH ::: 6
Training Net: 100% 2368/2368 [00:58<00:00, 40.21it/s, Loss_pi=3.55e-01, Loss_v=7.89e-02]
EPOCH ::: 7
Training Net: 100% 2368/2368 [00:58<00:00, 40.15it/s, Loss_pi=3.45e-01, Loss_v=7.40e-02]
EPOCH ::: 8
Training Net: 100% 2368/2368 [00:58<00:00, 40.22it/s, Loss_pi=3.35e-01, Loss_v=7.06e-02]
EPOCH ::: 9
Training Net: 100% 2368/2368 [00:58<00:00, 40.27it/s, Loss_pi=3.30e-01, Loss_v=6.61e-02]
EPOCH ::: 10
Training Net: 100% 2368/2368 [00:59<00:00, 40.04it/s, Loss_pi=3.27e-01, Loss_v=6.36e-02]
EPOCH ::: 11
Training Net: 100% 2368/2368 [00:59<00:00, 40.01it/s, Loss_pi=3.26e-01, Loss_v=6.24e-02]
EPOCH ::: 12
Training Net: 100% 2368/2368 [00:59<00:00, 39.97it/s, Loss_pi=3.21e-01, Loss_v=6.01e-02]
EPOCH ::: 13
Training Net: 100% 2368/2368 [00:58<00:00, 40.27it/s, Loss_pi=3.18e-01, Loss_v=5.86e-02]
EPOCH ::: 14
Training Net: 100% 2368/2368 [00:59<00:00, 40.08it/s, Loss_pi=3.15e-01, Loss_v=5.69e-02]
EPOCH ::: 15
Training Net: 100% 2368/2368 [00:58<00:00, 40.30it/s, Loss_pi=3.11e-01, Loss_v=5.60e-02]
EPOCH ::: 16
Training Net: 100% 2368/2368 [00:58<00:00, 40.35it/s, Loss_pi=3.10e-01, Loss_v=5.40e-02]
EPOCH ::: 17
Training Net: 100% 2368/2368 [00:58<00:00, 40.30it/s, Loss_pi=3.09e-01, Loss_v=5.36e-02]
EPOCH ::: 18
Training Net: 100% 2368/2368 [00:58<00:00, 40.22it/s, Loss_pi=3.13e-01, Loss_v=5.30e-02]
EPOCH ::: 19
Training Net: 100% 2368/2368 [00:59<00:00, 40.07it/s, Loss_pi=3.07e-01, Loss_v=5.14e-02]
EPOCH ::: 20
Training Net: 100% 2368/2368 [00:59<00:00, 40.12it/s, Loss_pi=3.04e-01, Loss_v=5.06e-02]
EPOCH ::: 21
Training Net: 100% 2368/2368 [00:59<00:00, 40.07it/s, Loss_pi=3.06e-01, Loss_v=5.10e-02]
EPOCH ::: 22
Training Net: 100% 2368/2368 [00:59<00:00, 40.03it/s, Loss_pi=3.02e-01, Loss_v=4.81e-02]
EPOCH ::: 23
Training Net: 100% 2368/2368 [00:59<00:00, 40.05it/s, Loss_pi=3.02e-01, Loss_v=4.86e-02]
EPOCH ::: 24
Training Net: 100% 2368/2368 [00:58<00:00, 40.24it/s, Loss_pi=3.02e-01, Loss_v=4.86e-02]
EPOCH ::: 25
Training Net: 100% 2368/2368 [01:00<00:00, 39.15it/s, Loss_pi=3.01e-01, Loss_v=4.76e-02]
EPOCH ::: 26
Training Net: 100% 2368/2368 [00:59<00:00, 39.60it/s, Loss_pi=3.00e-01, Loss_v=4.65e-02]
EPOCH ::: 27
Training Net: 100% 2368/2368 [01:00<00:00, 39.45it/s, Loss_pi=2.97e-01, Loss_v=4.55e-02]
EPOCH ::: 28
Training Net: 100% 2368/2368 [00:59<00:00, 39.57it/s, Loss_pi=2.99e-01, Loss_v=4.67e-02]
EPOCH ::: 29
Training Net: 100% 2368/2368 [00:58<00:00, 40.25it/s, Loss_pi=2.96e-01, Loss_v=4.57e-02]
EPOCH ::: 30
Training Net: 100% 2368/2368 [00:59<00:00, 39.91it/s, Loss_pi=2.96e-01, Loss_v=4.62e-02]
2024-05-19 15:14:29 4c08552d4751 Coach[2314] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [37:36<00:00, 112.83s/it]
Arena.playGames (2): 100% 20/20 [37:35<00:00, 112.77s/it]
2024-05-19 16:29:41 4c08552d4751 Coach[2314] INFO NEW/PREV WINS : 14 / 12 ; DRAWS : 14
2024-05-19 16:29:41 4c08552d4751 Coach[2314] INFO REJECTING NEW MODEL
2024-05-19 16:29:41 4c08552d4751 Coach[2314] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [3:37:10<00:00, 130.30s/it]
2024-05-19 20:06:52 4c08552d4751 Coach[2314] WARNING Removing the oldest entry in trainExamples. len(trainExamplesHistory) = 21
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2370/2370 [01:01<00:00, 38.59it/s, Loss_pi=7.14e-01, Loss_v=1.30e-01]
EPOCH ::: 2
Training Net: 100% 2370/2370 [00:59<00:00, 39.77it/s, Loss_pi=5.54e-01, Loss_v=1.11e-01]
EPOCH ::: 3
Training Net: 100% 2370/2370 [00:59<00:00, 39.67it/s, Loss_pi=4.65e-01, Loss_v=1.02e-01]
EPOCH ::: 4
Training Net: 100% 2370/2370 [01:00<00:00, 39.16it/s, Loss_pi=4.17e-01, Loss_v=9.46e-02]
EPOCH ::: 5
Training Net: 100% 2370/2370 [01:01<00:00, 38.26it/s, Loss_pi=3.84e-01, Loss_v=8.67e-02]
EPOCH ::: 6
Training Net: 100% 2370/2370 [00:59<00:00, 39.52it/s, Loss_pi=3.67e-01, Loss_v=8.16e-02]
EPOCH ::: 7
Training Net: 100% 2370/2370 [00:59<00:00, 39.74it/s, Loss_pi=3.55e-01, Loss_v=7.75e-02]
EPOCH ::: 8
Training Net: 100% 2370/2370 [01:00<00:00, 39.25it/s, Loss_pi=3.39e-01, Loss_v=7.37e-02]
EPOCH ::: 9
Training Net: 100% 2370/2370 [01:00<00:00, 39.19it/s, Loss_pi=3.41e-01, Loss_v=6.94e-02]
EPOCH ::: 10
Training Net: 100% 2370/2370 [00:59<00:00, 39.70it/s, Loss_pi=3.31e-01, Loss_v=6.78e-02]
EPOCH ::: 11
Training Net: 100% 2370/2370 [00:59<00:00, 39.76it/s, Loss_pi=3.29e-01, Loss_v=6.43e-02]
EPOCH ::: 12
Training Net: 100% 2370/2370 [00:59<00:00, 39.84it/s, Loss_pi=3.24e-01, Loss_v=6.24e-02]
EPOCH ::: 13
Training Net: 100% 2370/2370 [00:59<00:00, 39.78it/s, Loss_pi=3.24e-01, Loss_v=5.98e-02]
EPOCH ::: 14
Training Net: 100% 2370/2370 [00:59<00:00, 39.86it/s, Loss_pi=3.21e-01, Loss_v=5.84e-02]
EPOCH ::: 15
Training Net: 100% 2370/2370 [00:59<00:00, 39.62it/s, Loss_pi=3.17e-01, Loss_v=5.68e-02]
EPOCH ::: 16
Training Net: 100% 2370/2370 [01:00<00:00, 39.24it/s, Loss_pi=3.12e-01, Loss_v=5.38e-02]
EPOCH ::: 18
Training Net: 100% 2370/2370 [00:59<00:00, 39.81it/s, Loss_pi=3.16e-01, Loss_v=5.35e-02]
EPOCH ::: 19
Training Net: 100% 2370/2370 [01:02<00:00, 38.18it/s, Loss_pi=3.10e-01, Loss_v=5.12e-02]
EPOCH ::: 20
Training Net: 100% 2370/2370 [01:01<00:00, 38.44it/s, Loss_pi=3.13e-01, Loss_v=5.18e-02]
EPOCH ::: 21
Training Net: 100% 2370/2370 [01:01<00:00, 38.63it/s, Loss_pi=3.08e-01, Loss_v=4.93e-02]
EPOCH ::: 22
Training Net: 100% 2370/2370 [01:01<00:00, 38.63it/s, Loss_pi=3.06e-01, Loss_v=4.96e-02]
EPOCH ::: 23
Training Net: 100% 2370/2370 [01:01<00:00, 38.82it/s, Loss_pi=3.04e-01, Loss_v=4.90e-02]
EPOCH ::: 24
Training Net: 100% 2370/2370 [01:00<00:00, 38.99it/s, Loss_pi=3.04e-01, Loss_v=4.84e-02]
EPOCH ::: 25
Training Net: 100% 2370/2370 [01:00<00:00, 38.95it/s, Loss_pi=3.05e-01, Loss_v=4.78e-02]
EPOCH ::: 26
Training Net: 100% 2370/2370 [00:59<00:00, 39.68it/s, Loss_pi=3.05e-01, Loss_v=4.70e-02]
EPOCH ::: 27
Training Net: 100% 2370/2370 [00:59<00:00, 39.69it/s, Loss_pi=3.02e-01, Loss_v=4.60e-02]
EPOCH ::: 28
Training Net: 100% 2370/2370 [00:59<00:00, 39.66it/s, Loss_pi=2.98e-01, Loss_v=4.52e-02]
EPOCH ::: 29
Training Net: 100% 2370/2370 [01:03<00:00, 37.26it/s, Loss_pi=2.99e-01, Loss_v=4.49e-02]
EPOCH ::: 30
Training Net: 100% 2370/2370 [01:06<00:00, 35.79it/s, Loss_pi=3.00e-01, Loss_v=4.41e-02]
2024-05-19 20:37:30 4c08552d4751 Coach[2314] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [36:47<00:00, 110.38s/it]
Arena.playGames (2): 100% 20/20 [37:11<00:00, 111.55s/it]
2024-05-19 21:51:29 4c08552d4751 Coach[2314] INFO NEW/PREV WINS : 14 / 11 ; DRAWS : 15
2024-05-19 21:51:29 4c08552d4751 Coach[2314] INFO REJECTING NEW MODEL
2024-05-19 21:51:29 4c08552d4751 Coach[2314] INFO Starting Iter #4 ...
Self Play:  87% 87/100 [3:01:46<25:10, 116.20s/it]












wandb: Currently logged in as: cemgulec (cem-gulec). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /content/drive/MyDrive/dama_project/wandb/run-20240520_105450-7wfv8ygg
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Run 9
wandb: ⭐️ View project at https://wandb.ai/cem-gulec/dama-project
wandb: 🚀 View run at https://wandb.ai/cem-gulec/dama-project/runs/7wfv8ygg
2024-05-20 10:54:51 8b7f0ee5f4db __main__[2846] INFO Loading Dama...
2024-05-20 10:54:51 8b7f0ee5f4db __main__[2846] INFO Loading NNetWrapper...
2024-05-20 10:54:51 8b7f0ee5f4db __main__[2846] INFO Loading checkpoint "./temp//checkpoint_4.pth.tar"...
2024-05-20 10:54:55 8b7f0ee5f4db __main__[2846] INFO Loading the Coach...
2024-05-20 10:54:55 8b7f0ee5f4db __main__[2846] INFO Loading 'trainExamples' from file...
2024-05-20 10:54:55 8b7f0ee5f4db Coach[2846] INFO File with trainExamples found. Loading it...
2024-05-20 10:55:23 8b7f0ee5f4db Coach[2846] INFO Loading done!
2024-05-20 10:55:23 8b7f0ee5f4db __main__[2846] INFO Starting the learning process 🎉
2024-05-20 10:55:23 8b7f0ee5f4db Coach[2846] INFO Starting Iter #1 ...
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2371/2371 [00:59<00:00, 40.18it/s, Loss_pi=8.18e-01, Loss_v=1.51e-01]
EPOCH ::: 2
Training Net: 100% 2371/2371 [00:56<00:00, 42.17it/s, Loss_pi=6.30e-01, Loss_v=1.29e-01]
EPOCH ::: 3
Training Net: 100% 2371/2371 [00:55<00:00, 42.61it/s, Loss_pi=5.23e-01, Loss_v=1.17e-01]
EPOCH ::: 4
Training Net: 100% 2371/2371 [00:56<00:00, 42.21it/s, Loss_pi=4.62e-01, Loss_v=1.09e-01]
EPOCH ::: 5
Training Net: 100% 2371/2371 [00:55<00:00, 42.43it/s, Loss_pi=4.17e-01, Loss_v=9.88e-02]
EPOCH ::: 6
Training Net: 100% 2371/2371 [00:56<00:00, 42.24it/s, Loss_pi=3.89e-01, Loss_v=9.10e-02]
EPOCH ::: 7
Training Net: 100% 2371/2371 [00:55<00:00, 42.46it/s, Loss_pi=3.73e-01, Loss_v=8.61e-02]
EPOCH ::: 8
Training Net: 100% 2371/2371 [00:56<00:00, 42.33it/s, Loss_pi=3.59e-01, Loss_v=8.02e-02]
EPOCH ::: 9
Training Net: 100% 2371/2371 [00:56<00:00, 42.33it/s, Loss_pi=3.56e-01, Loss_v=7.76e-02]
EPOCH ::: 10
Training Net: 100% 2371/2371 [00:56<00:00, 42.09it/s, Loss_pi=3.45e-01, Loss_v=7.19e-02]
EPOCH ::: 11
Training Net: 100% 2371/2371 [00:56<00:00, 42.32it/s, Loss_pi=3.42e-01, Loss_v=6.89e-02]
EPOCH ::: 12
Training Net: 100% 2371/2371 [00:56<00:00, 41.84it/s, Loss_pi=3.37e-01, Loss_v=6.58e-02]
EPOCH ::: 13
Training Net: 100% 2371/2371 [00:56<00:00, 42.32it/s, Loss_pi=3.31e-01, Loss_v=6.31e-02]
EPOCH ::: 14
Training Net: 100% 2371/2371 [00:55<00:00, 42.42it/s, Loss_pi=3.32e-01, Loss_v=6.22e-02]
EPOCH ::: 15
Training Net: 100% 2371/2371 [00:55<00:00, 42.47it/s, Loss_pi=3.24e-01, Loss_v=5.94e-02]
EPOCH ::: 16
Training Net: 100% 2371/2371 [00:55<00:00, 42.54it/s, Loss_pi=3.24e-01, Loss_v=5.73e-02]
EPOCH ::: 17
Training Net: 100% 2371/2371 [00:55<00:00, 42.48it/s, Loss_pi=3.20e-01, Loss_v=5.49e-02]
EPOCH ::: 18
Training Net: 100% 2371/2371 [00:55<00:00, 42.37it/s, Loss_pi=3.17e-01, Loss_v=5.52e-02]
EPOCH ::: 19
Training Net: 100% 2371/2371 [00:55<00:00, 42.46it/s, Loss_pi=3.20e-01, Loss_v=5.27e-02]
EPOCH ::: 20
Training Net: 100% 2371/2371 [00:55<00:00, 42.56it/s, Loss_pi=3.16e-01, Loss_v=5.30e-02]
EPOCH ::: 21
Training Net: 100% 2371/2371 [00:55<00:00, 42.51it/s, Loss_pi=3.15e-01, Loss_v=5.10e-02]
EPOCH ::: 22
Training Net: 100% 2371/2371 [00:55<00:00, 42.46it/s, Loss_pi=3.10e-01, Loss_v=4.97e-02]
EPOCH ::: 23
Training Net: 100% 2371/2371 [00:55<00:00, 42.57it/s, Loss_pi=3.11e-01, Loss_v=4.94e-02]
EPOCH ::: 24
Training Net: 100% 2371/2371 [00:55<00:00, 42.65it/s, Loss_pi=3.10e-01, Loss_v=4.84e-02]
EPOCH ::: 25
Training Net: 100% 2371/2371 [00:56<00:00, 41.93it/s, Loss_pi=3.10e-01, Loss_v=4.71e-02]
EPOCH ::: 26
Training Net: 100% 2371/2371 [00:56<00:00, 41.85it/s, Loss_pi=3.11e-01, Loss_v=4.77e-02]
EPOCH ::: 27
Training Net: 100% 2371/2371 [00:56<00:00, 42.31it/s, Loss_pi=3.09e-01, Loss_v=4.64e-02]
EPOCH ::: 28
Training Net: 100% 2371/2371 [00:55<00:00, 42.38it/s, Loss_pi=3.05e-01, Loss_v=4.59e-02]
EPOCH ::: 29
Training Net: 100% 2371/2371 [00:55<00:00, 42.46it/s, Loss_pi=3.05e-01, Loss_v=4.47e-02]
EPOCH ::: 30
Training Net: 100% 2371/2371 [00:55<00:00, 42.57it/s, Loss_pi=3.04e-01, Loss_v=4.43e-02]
2024-05-20 11:23:50 8b7f0ee5f4db Coach[2846] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [57:18<00:00, 171.94s/it]
Arena.playGames (2): 100% 20/20 [1:11:15<00:00, 213.79s/it]
2024-05-20 13:32:25 8b7f0ee5f4db Coach[2846] INFO NEW/PREV WINS : 11 / 10 ; DRAWS : 19
2024-05-20 13:32:25 8b7f0ee5f4db Coach[2846] INFO REJECTING NEW MODEL
2024-05-20 13:32:25 8b7f0ee5f4db Coach[2846] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [5:39:17<00:00, 203.58s/it]
2024-05-20 19:11:42 8b7f0ee5f4db Coach[2846] WARNING Removing the oldest entry in trainExamples. len(trainExamplesHistory) = 21
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2372/2372 [01:03<00:00, 37.29it/s, Loss_pi=8.82e-01, Loss_v=1.59e-01]
EPOCH ::: 2
Training Net: 100% 2372/2372 [01:01<00:00, 38.61it/s, Loss_pi=6.70e-01, Loss_v=1.36e-01]
EPOCH ::: 3
Training Net: 100% 2372/2372 [01:02<00:00, 37.83it/s, Loss_pi=5.57e-01, Loss_v=1.24e-01]
EPOCH ::: 4
Training Net: 100% 2372/2372 [01:01<00:00, 38.31it/s, Loss_pi=4.81e-01, Loss_v=1.13e-01]
EPOCH ::: 5
Training Net: 100% 2372/2372 [01:00<00:00, 38.91it/s, Loss_pi=4.36e-01, Loss_v=1.05e-01]
EPOCH ::: 6
Training Net: 100% 2372/2372 [01:03<00:00, 37.55it/s, Loss_pi=4.03e-01, Loss_v=9.74e-02]
EPOCH ::: 7
Training Net: 100% 2372/2372 [01:01<00:00, 38.58it/s, Loss_pi=3.87e-01, Loss_v=9.18e-02]
EPOCH ::: 8
Training Net: 100% 2372/2372 [01:03<00:00, 37.09it/s, Loss_pi=3.70e-01, Loss_v=8.50e-02]
EPOCH ::: 9
Training Net: 100% 2372/2372 [01:02<00:00, 38.05it/s, Loss_pi=3.60e-01, Loss_v=7.99e-02]
EPOCH ::: 10
Training Net: 100% 2372/2372 [01:03<00:00, 37.57it/s, Loss_pi=3.53e-01, Loss_v=7.61e-02]
EPOCH ::: 11
Training Net: 100% 2372/2372 [01:03<00:00, 37.17it/s, Loss_pi=3.48e-01, Loss_v=7.26e-02]
EPOCH ::: 12
Training Net: 100% 2372/2372 [01:00<00:00, 39.03it/s, Loss_pi=3.44e-01, Loss_v=6.81e-02]
EPOCH ::: 13
Training Net: 100% 2372/2372 [01:01<00:00, 38.67it/s, Loss_pi=3.38e-01, Loss_v=6.60e-02]
EPOCH ::: 14
Training Net: 100% 2372/2372 [01:02<00:00, 38.25it/s, Loss_pi=3.38e-01, Loss_v=6.43e-02]
EPOCH ::: 15
Training Net: 100% 2372/2372 [01:00<00:00, 39.40it/s, Loss_pi=3.31e-01, Loss_v=6.07e-02]
EPOCH ::: 16
Training Net: 100% 2372/2372 [01:02<00:00, 38.01it/s, Loss_pi=3.28e-01, Loss_v=5.86e-02]
EPOCH ::: 17
Training Net: 100% 2372/2372 [01:00<00:00, 39.19it/s, Loss_pi=3.27e-01, Loss_v=5.72e-02]
EPOCH ::: 18
Training Net: 100% 2372/2372 [01:01<00:00, 38.46it/s, Loss_pi=3.26e-01, Loss_v=5.52e-02]
EPOCH ::: 19
Training Net: 100% 2372/2372 [01:01<00:00, 38.84it/s, Loss_pi=3.26e-01, Loss_v=5.52e-02]
EPOCH ::: 20
Training Net: 100% 2372/2372 [01:00<00:00, 39.15it/s, Loss_pi=3.18e-01, Loss_v=5.24e-02]
EPOCH ::: 21
Training Net: 100% 2372/2372 [01:01<00:00, 38.44it/s, Loss_pi=3.20e-01, Loss_v=5.15e-02]
EPOCH ::: 22
Training Net: 100% 2372/2372 [01:03<00:00, 37.33it/s, Loss_pi=3.20e-01, Loss_v=5.01e-02]
EPOCH ::: 23
Training Net: 100% 2372/2372 [01:00<00:00, 38.95it/s, Loss_pi=3.18e-01, Loss_v=4.91e-02]
EPOCH ::: 24
Training Net: 100% 2372/2372 [01:01<00:00, 38.45it/s, Loss_pi=3.15e-01, Loss_v=4.76e-02]
EPOCH ::: 25
Training Net: 100% 2372/2372 [01:01<00:00, 38.83it/s, Loss_pi=3.12e-01, Loss_v=4.77e-02]
EPOCH ::: 26
Training Net: 100% 2372/2372 [01:00<00:00, 39.25it/s, Loss_pi=3.12e-01, Loss_v=4.73e-02]
EPOCH ::: 27
Training Net: 100% 2372/2372 [01:00<00:00, 38.91it/s, Loss_pi=3.12e-01, Loss_v=4.60e-02]
EPOCH ::: 28
Training Net: 100% 2372/2372 [01:02<00:00, 38.09it/s, Loss_pi=3.08e-01, Loss_v=4.54e-02]
EPOCH ::: 29
Training Net: 100% 2372/2372 [01:00<00:00, 38.97it/s, Loss_pi=3.08e-01, Loss_v=4.56e-02]
EPOCH ::: 30
Training Net: 100% 2372/2372 [01:01<00:00, 38.73it/s, Loss_pi=3.10e-01, Loss_v=4.39e-02]
2024-05-20 19:43:10 8b7f0ee5f4db Coach[2846] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [57:53<00:00, 173.68s/it]
Arena.playGames (2): 100% 20/20 [1:00:02<00:00, 180.11s/it]
2024-05-20 21:41:05 8b7f0ee5f4db Coach[2846] INFO NEW/PREV WINS : 14 / 12 ; DRAWS : 14
2024-05-20 21:41:05 8b7f0ee5f4db Coach[2846] INFO REJECTING NEW MODEL
2024-05-20 21:41:05 8b7f0ee5f4db Coach[2846] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [5:44:43<00:00, 206.83s/it]
2024-05-21 03:25:49 8b7f0ee5f4db Coach[2846] WARNING Removing the oldest entry in trainExamples. len(trainExamplesHistory) = 21
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 2373/2373 [01:05<00:00, 36.49it/s, Loss_pi=9.36e-01, Loss_v=1.68e-01]
EPOCH ::: 2
Training Net: 100% 2373/2373 [01:01<00:00, 38.63it/s, Loss_pi=7.09e-01, Loss_v=1.45e-01]
EPOCH ::: 3
Training Net: 100% 2373/2373 [01:01<00:00, 38.52it/s, Loss_pi=5.80e-01, Loss_v=1.31e-01]
EPOCH ::: 4
Training Net: 100% 2373/2373 [01:01<00:00, 38.30it/s, Loss_pi=5.07e-01, Loss_v=1.20e-01]
EPOCH ::: 5
Training Net: 100% 2373/2373 [01:02<00:00, 37.68it/s, Loss_pi=4.51e-01, Loss_v=1.10e-01]
EPOCH ::: 6
Training Net: 100% 2373/2373 [01:01<00:00, 38.42it/s, Loss_pi=4.19e-01, Loss_v=1.02e-01]
EPOCH ::: 7
Training Net: 100% 2373/2373 [01:01<00:00, 38.58it/s, Loss_pi=3.96e-01, Loss_v=9.48e-02]
EPOCH ::: 8
Training Net: 100% 2373/2373 [01:04<00:00, 36.88it/s, Loss_pi=3.81e-01, Loss_v=8.83e-02]
EPOCH ::: 9
Training Net: 100% 2373/2373 [01:03<00:00, 37.64it/s, Loss_pi=3.70e-01, Loss_v=8.40e-02]
EPOCH ::: 10
Training Net: 100% 2373/2373 [01:02<00:00, 37.92it/s, Loss_pi=3.58e-01, Loss_v=7.89e-02]
EPOCH ::: 11
Training Net: 100% 2373/2373 [01:01<00:00, 38.60it/s, Loss_pi=3.54e-01, Loss_v=7.40e-02]
EPOCH ::: 12
Training Net: 100% 2373/2373 [01:01<00:00, 38.62it/s, Loss_pi=3.49e-01, Loss_v=7.03e-02]
EPOCH ::: 13
Training Net: 100% 2373/2373 [01:02<00:00, 38.16it/s, Loss_pi=3.43e-01, Loss_v=6.69e-02]
EPOCH ::: 14
Training Net: 100% 2373/2373 [01:01<00:00, 38.73it/s, Loss_pi=3.38e-01, Loss_v=6.54e-02]
EPOCH ::: 15
Training Net: 100% 2373/2373 [01:02<00:00, 38.13it/s, Loss_pi=3.36e-01, Loss_v=6.22e-02]
EPOCH ::: 16
Training Net: 100% 2373/2373 [01:01<00:00, 38.33it/s, Loss_pi=3.34e-01, Loss_v=6.04e-02]
EPOCH ::: 17
Training Net: 100% 2373/2373 [01:01<00:00, 38.73it/s, Loss_pi=3.30e-01, Loss_v=5.74e-02]
EPOCH ::: 18
Training Net: 100% 2373/2373 [01:02<00:00, 38.13it/s, Loss_pi=3.30e-01, Loss_v=5.64e-02]
EPOCH ::: 19
Training Net: 100% 2373/2373 [01:01<00:00, 38.71it/s, Loss_pi=3.25e-01, Loss_v=5.45e-02]
EPOCH ::: 20
Training Net: 100% 2373/2373 [01:01<00:00, 38.50it/s, Loss_pi=3.22e-01, Loss_v=5.22e-02]
EPOCH ::: 21
Training Net: 100% 2373/2373 [01:02<00:00, 38.20it/s, Loss_pi=3.21e-01, Loss_v=5.18e-02]
EPOCH ::: 22
Training Net: 100% 2373/2373 [01:02<00:00, 38.01it/s, Loss_pi=3.20e-01, Loss_v=5.06e-02]
EPOCH ::: 23
Training Net: 100% 2373/2373 [01:03<00:00, 37.65it/s, Loss_pi=3.18e-01, Loss_v=5.05e-02]
EPOCH ::: 24
Training Net: 100% 2373/2373 [01:01<00:00, 38.34it/s, Loss_pi=3.21e-01, Loss_v=4.85e-02]
EPOCH ::: 25
Training Net: 100% 2373/2373 [01:06<00:00, 35.69it/s, Loss_pi=3.16e-01, Loss_v=4.79e-02]
EPOCH ::: 26
Training Net: 100% 2373/2373 [01:03<00:00, 37.37it/s, Loss_pi=3.15e-01, Loss_v=4.67e-02]
EPOCH ::: 27
Training Net: 100% 2373/2373 [01:04<00:00, 37.07it/s, Loss_pi=3.16e-01, Loss_v=4.56e-02]
EPOCH ::: 28
Training Net: 100% 2373/2373 [01:02<00:00, 37.85it/s, Loss_pi=3.12e-01, Loss_v=4.53e-02]
EPOCH ::: 29
Training Net: 100% 2373/2373 [01:02<00:00, 37.95it/s, Loss_pi=3.09e-01, Loss_v=4.55e-02]
EPOCH ::: 30
Training Net: 100% 2373/2373 [01:02<00:00, 38.01it/s, Loss_pi=3.10e-01, Loss_v=4.32e-02]
2024-05-21 03:57:42 8b7f0ee5f4db Coach[2846] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [59:29<00:00, 178.49s/it]
Arena.playGames (2): 100% 20/20 [57:42<00:00, 173.12s/it]
2024-05-21 05:54:54 8b7f0ee5f4db Coach[2846] INFO NEW/PREV WINS : 16 / 7 ; DRAWS : 17
2024-05-21 05:54:54 8b7f0ee5f4db Coach[2846] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-21 05:55:00 8b7f0ee5f4db Coach[2846] INFO Starting Iter #4 ...
Self Play:  40% 40/100 [2:21:32<3:43:20, 223.35s/it]
'''

# Regex pattern to capture Loss_pi and Loss_v values
pattern = r'Loss_pi=([\d.e+-]+), Loss_v=([\d.e+-]+)'

# Finding all matches in the data
losses = re.findall(pattern, data)

# Splitting the results into separate lists for Loss_pi and Loss_v
loss_pi = [float(pi) for pi, _ in losses]
loss_v = [float(v) for _, v in losses]

# Plotting Loss_pi
plt.figure(figsize=(10, 5))
plt.plot(loss_pi, label='Loss_pi', marker=',')
plt.title('Loss_pi over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss_pi')
plt.grid(True)
plt.legend()
plt.show()

# Plotting Loss_v
plt.figure(figsize=(10, 5))
plt.plot(loss_v, label='Loss_v', marker=',', color='red')
plt.title('Loss_v over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss_v')
plt.grid(True)
plt.legend()
plt.show()

# Plotting Loss_pi and Loss_v on the same graph
plt.figure(figsize=(10, 5))
plt.plot(loss_pi, label='Loss_pi', marker=',')
plt.plot(loss_v, label='Loss_v', marker=',', color='red')
plt.title('Loss_pi and Loss_v over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()
plt.show()