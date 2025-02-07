class DLL:
    
    def __init__(self, page, last = None, next = None):
        self.page = page
        self.last =  last
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DLL(homepage)

    def visit(self, url: str) -> None:
        self.history.next = DLL(url, self.history)
        self.history = self.history.next

    def back(self, steps: int) -> str:
        while self.history.last and steps:
            self.history = self.history.last
            steps -= 1
        return self.history.page

    def forward(self, steps: int) -> str:
        while steps and self.history.next:
            self.history = self.history.next
            steps -= 1
        return self.history.page
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# Initial Solution
# class DLL:
    
#     def __init__(self, page: str):
#         self.page = page
#         self.last =  None
#         self.next = None

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.history = DLL(homepage)
#         self.visited = 0

#     def visit(self, url: str) -> None:
#         curr = self.history
#         self.history.next = DLL(url)
#         self.history = self.history.next
#         self.history.last = curr
#         self.visited += 1

#     def back(self, steps: int) -> str:
#         if self.visited:
#             while self.history.last and steps:
#                 print(self.history.page)
#                 self.history = self.history.last
#                 self.visited -= 1
#                 steps -= 1
#         return self.history.page

#     def forward(self, steps: int) -> str:
#         while steps and self.history.next:
#             self.history = self.history.next
#             self.visited += 1
#             steps -= 1
#         return self.history.page