import re
import matplotlib.pyplot as plt

data = '''
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

EPOCH ::: 1
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

EPOCH ::: 1
Training Net: 100% 1349/1349 [00:40<00:00, 33.13it/s, Loss_pi=7.87e-01, Loss_v=1.73e-01]
EPOCH ::: 2
Training Net: 100% 1349/1349 [00:37<00:00, 35.65it/s, Loss_pi=6.10e-01, Loss_v=1.37e-01]
EPOCH ::: 3
Training Net: 100% 1349/1349 [00:37<00:00, 35.97it/s, Loss_pi=5.35e-01, Loss_v=1.19e-01]
EPOCH ::: 4
Training Net: 100% 1349/1349 [00:36<00:00, 36.74it/s, Loss_pi=4.83e-01, Loss_v=1.07e-01]
EPOCH ::: 5
Training Net: 100% 1349/1349 [00:35<00:00, 37.81it/s, Loss_pi=4.65e-01, Loss_v=9.80e-02]
EPOCH ::: 6
Training Net: 100% 1349/1349 [00:35<00:00, 38.27it/s, Loss_pi=4.48e-01, Loss_v=9.41e-02]
EPOCH ::: 7
Training Net: 100% 1349/1349 [00:35<00:00, 38.51it/s, Loss_pi=4.32e-01, Loss_v=8.83e-02]
EPOCH ::: 8
Training Net: 100% 1349/1349 [00:35<00:00, 38.08it/s, Loss_pi=4.22e-01, Loss_v=8.29e-02]
EPOCH ::: 9
Training Net: 100% 1349/1349 [00:35<00:00, 37.97it/s, Loss_pi=4.17e-01, Loss_v=8.21e-02]
EPOCH ::: 10
Training Net: 100% 1349/1349 [00:35<00:00, 38.49it/s, Loss_pi=4.18e-01, Loss_v=8.06e-02]
EPOCH ::: 11
Training Net: 100% 1349/1349 [00:35<00:00, 38.14it/s, Loss_pi=4.08e-01, Loss_v=7.60e-02]
EPOCH ::: 12
Training Net: 100% 1349/1349 [00:35<00:00, 37.96it/s, Loss_pi=4.02e-01, Loss_v=7.73e-02]
EPOCH ::: 13
Training Net: 100% 1349/1349 [00:36<00:00, 37.28it/s, Loss_pi=3.97e-01, Loss_v=7.35e-02]
EPOCH ::: 14
Training Net: 100% 1349/1349 [00:35<00:00, 38.15it/s, Loss_pi=3.96e-01, Loss_v=7.27e-02]
EPOCH ::: 15
Training Net: 100% 1349/1349 [00:35<00:00, 38.23it/s, Loss_pi=3.92e-01, Loss_v=7.15e-02]
EPOCH ::: 16
Training Net: 100% 1349/1349 [00:34<00:00, 38.63it/s, Loss_pi=3.89e-01, Loss_v=7.30e-02]
EPOCH ::: 17
Training Net: 100% 1349/1349 [00:34<00:00, 38.70it/s, Loss_pi=3.92e-01, Loss_v=7.14e-02]
EPOCH ::: 18
Training Net: 100% 1349/1349 [00:35<00:00, 38.20it/s, Loss_pi=3.88e-01, Loss_v=7.16e-02]
EPOCH ::: 19
Training Net: 100% 1349/1349 [00:35<00:00, 38.46it/s, Loss_pi=3.85e-01, Loss_v=6.92e-02]
EPOCH ::: 20
Training Net: 100% 1349/1349 [00:34<00:00, 38.60it/s, Loss_pi=3.85e-01, Loss_v=6.91e-02]
EPOCH ::: 21
Training Net: 100% 1349/1349 [00:36<00:00, 37.37it/s, Loss_pi=3.83e-01, Loss_v=6.94e-02]
EPOCH ::: 22
Training Net: 100% 1349/1349 [00:35<00:00, 38.37it/s, Loss_pi=3.81e-01, Loss_v=6.82e-02]
EPOCH ::: 23
Training Net: 100% 1349/1349 [00:35<00:00, 38.26it/s, Loss_pi=3.80e-01, Loss_v=6.84e-02]
EPOCH ::: 24
Training Net: 100% 1349/1349 [00:35<00:00, 38.21it/s, Loss_pi=3.76e-01, Loss_v=6.74e-02]
EPOCH ::: 25
Training Net: 100% 1349/1349 [00:35<00:00, 38.49it/s, Loss_pi=3.73e-01, Loss_v=6.54e-02]
EPOCH ::: 26
Training Net: 100% 1349/1349 [00:35<00:00, 38.37it/s, Loss_pi=3.66e-01, Loss_v=6.48e-02]
EPOCH ::: 27
Training Net: 100% 1349/1349 [00:34<00:00, 38.65it/s, Loss_pi=3.74e-01, Loss_v=6.58e-02]
EPOCH ::: 28
Training Net: 100% 1349/1349 [00:34<00:00, 38.86it/s, Loss_pi=3.68e-01, Loss_v=6.55e-02]
EPOCH ::: 29
Training Net: 100% 1349/1349 [00:35<00:00, 38.49it/s, Loss_pi=3.72e-01, Loss_v=6.41e-02]
EPOCH ::: 30
Training Net: 100% 1349/1349 [00:34<00:00, 38.57it/s, Loss_pi=3.71e-01, Loss_v=6.52e-02]
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