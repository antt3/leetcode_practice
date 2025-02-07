class DLL:
    
    def __init__(self, page: str):
        self.page = page
        self.last =  None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DLL(homepage)
        self.visited = 0

    def visit(self, url: str) -> None:
        curr = self.history
        self.history.next = DLL(url)
        self.history = self.history.next
        self.history.last = curr
        self.visited += 1

    def back(self, steps: int) -> str:
        if self.visited:
            while self.history.last and steps:
                print(self.history.page)
                self.history = self.history.last
                self.visited -= 1
                steps -= 1
        return self.history.page

    def forward(self, steps: int) -> str:
        while steps and self.history.next:
            self.history = self.history.next
            self.visited += 1
            steps -= 1
        return self.history.page
