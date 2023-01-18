import threading


class CellMonitor:
    def __init__(self, cells):
        self.cells = cells

    def print_cells_stats(self):
        threading.Timer(2.0, self.print_cells_stats).start()
        for cell in  self.cells:
            print(f'[{cell.number}] cell <strength>={cell.strength}, <energy>={cell.energy}')
        print('-------------------------------')

