class TaskIndex(DocType):
    id = Integer()
    user = Text()
    description = Text()
    due = Date()

    class Meta:
        index = 'task'