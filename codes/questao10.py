back_stack = []
forward_stack = []
current_page = None

def visit(site):
    global current_page
    if current_page:
        back_stack.append(current_page)
    forward_stack.clear()
    current_page = site
    print(f"Acessou: {current_page}")

def back():
    global current_page
    if not back_stack:
        print("Não há páginas para voltar.")
        return
    forward_stack.append(current_page)
    current_page = back_stack.pop()
    print(f"Voltou para: {current_page}")

def forward():
    global current_page
    if not forward_stack:
        print("Não há páginas para avançar.")
        return
    back_stack.append(current_page)
    current_page = forward_stack.pop()
    print(f"Avançou para: {current_page}")


visit("google.com")
visit("youtube.com")
visit("github.com")

back()
back()
forward()
visit("stackoverflow.com")

print("\nSTATUS FINAL")
print("Página atual:", current_page)
print("Voltar:", back_stack)
print("Avançar:", forward_stack)
