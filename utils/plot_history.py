
import matplotlib.pyplot as plt

__all__ = ['plot_history']

def _plot(history_dict, what, ignore_first_n):
    plt.clf()
    epochs = range(1, len(history_dict[what])+1-ignore_first_n)
    plt.plot(epochs, history_dict[what][ignore_first_n:], 'bo', label=f'Training {what}')
    if f'val_{what}' in history_dict:
        plt.plot(epochs, history_dict[f'val_{what}'][ignore_first_n:], 'b', label=f'Validation {what}')
        plt.title(f'Training and validation {what}')
    else:
        plt.title(f'Training {what}')
    plt.xlabel('Epochs')
    plt.ylabel(what.title())
    plt.legend()
    plt.show()
    
def plot_history(history, ignore_first_n=0):
    """`history` can be a `keras.callbacks.History` or a `keras.callbacks.History.history` like dictionary"""
    history_dict = history if isinstance(history, dict) else history.history
    for k in history_dict:
        if k.startswith('val_'):
            continue
        _plot(history_dict, k, ignore_first_n)
