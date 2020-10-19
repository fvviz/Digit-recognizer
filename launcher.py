from app.GUI import GUI

app = GUI(dim=200, model="nn_model.model")
app.init()
app.mainloop()  # maybe move this call inside init function?
