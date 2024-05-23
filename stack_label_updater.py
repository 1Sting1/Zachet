from observer import observer
class stack_label_updater(observer):
    def __init__(self, label, stack_operations):
        self.label = label
        stack_operations.add_observer(self)

    def update(self, observable, *args, **kwargs):
        if len(observable.stack) == 0:
            self.label.set('')
        else:
            self.label.set(', '.join([str(x) for x in observable.stack]))