# Ideal Solution
class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1

    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, len(self.len - 1))
        return self.history[self.i]


# Initial Solution Using An Array
# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.history = [homepage]
#         self.curr = 0

#     def visit(self, url: str) -> None:
#         self.history = self.history[:self.curr + 1]
#         self.history.append(url)
#         self.curr += 1

#     def back(self, steps: int) -> str:
#         self.curr = self.curr - steps if self.curr - steps >= 0 else 0
#         return self.history[self.curr]

#     def forward(self, steps: int) -> str:
#         self.curr = self.curr + steps if self.curr + steps < len(self.history) else len(self.history) - 1
#         return self.history[self.curr]


# Refactored Solution
# class DLL:
    
#     def __init__(self, page, last = None, next = None):
#         self.page = page
#         self.last =  last
#         self.next = next

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.history = DLL(homepage)

#     def visit(self, url: str) -> None:
#         self.history.next = DLL(url, self.history)
#         self.history = self.history.next

#     def back(self, steps: int) -> str:
#         while self.history.last and steps:
#             self.history = self.history.last
#             steps -= 1
#         return self.history.page

#     def forward(self, steps: int) -> str:
#         while steps and self.history.next:
#             self.history = self.history.next
#             steps -= 1
#         return self.history.page
        

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