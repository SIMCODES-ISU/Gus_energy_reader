from pathlib import Path

file_path = Path(__file__).parent.parent / "outputs" / "SCF_energy.txt"


def test_energy_file_exists():
    with open(file_path, 'r') as f:
        first_line = f.readline().split()
        #remove whitespace and split the fist line
        energy = float(first_line[5])
        float(energy)
        assert energy == -699.782153441754


test_energy_file_exists()
