import re

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
'''

# Regex pattern to capture Loss_pi and Loss_v values
pattern = r'Loss_pi=([\d.e+-]+), Loss_v=([\d.e+-]+)'

# Finding all matches in the data
losses = re.findall(pattern, data)

# Splitting the results into separate lists for Loss_pi and Loss_v
loss_pi = [float(pi) for pi, _ in losses]
loss_v = [float(v) for _, v in losses]

print("Loss_pi:", loss_pi)
print("Loss_v:", loss_v)
