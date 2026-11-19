from js import document, window
from pyodide.ffi import create_proxy


# This is the finder itself
non_metals = {
    "H": ("Hydrogen", "1", "1.008"),
    "C": ("Carbon", "6", "12.011"),
    "N": ("Nitrogen", "7", "14.007"),
    "O": ("Oxygen", "8", "15.999"),
    "F": ("Fluorine", "9", "18.998"),
    "P": ("Phosphorus", "15", "30.974"),
    "S": ("Sulfur", "16", "32.06"),
    "Cl": ("Chlorine", "17", "35.45")
}

def search_element(event):
    Element1 = document.getElementById("nm-element-symbol").value.strip()

    # Its a dash if it is nothing
    result = non_metals.get(Element1, ("Element not found in non-metals list", "-", "-"))

    element_name = result[0]
    atomic_number = result[1]
    atomic_mass = result[2]

    document.getElementById("nm-res-symbol").innerText = Element1 if element_name != "Element not found in non-metals list" else "-"
    document.getElementById("nm-res-name").innerText = element_name
    document.getElementById("nm-res-number").innerText = atomic_number
    document.getElementById("nm-res-mass").innerText = atomic_mass

def setup_non_metal(event=None):
    button = document.getElementById("nm-btn-submit")
    button.addEventListener("click", create_proxy(search_element))

setup_non_metal()

add_club_members = [
    "John Wick",
    "Saint Nicolas",
    "Logan Paul",
    "Bomb Squad 14",
    "Coco Martin"
]

def add_member(event):
    first_name = document.getElementById("add-fname").value.strip()
    last_name = document.getElementById("add-lname").value.strip()
    full_name = f"{first_name} {last_name}".strip()
    add_club_members.append(full_name)
    document.getElementById("add-result").innerText = f"Congratulations {full_name}! You are now part of the ICT club."
    document.getElementById("add-members-list").innerText = ", ".join(add_club_members)
    document.getElementById("add-member-count").innerText = f"Official Club Members: {len(add_club_members)} STUDENTS"
    document.getElementById("add-fname").value = ""
    document.getElementById("add-lname").value = ""

def setup_add_member(event=None):
    document.getElementById("add-members-list").innerText = ", ".join(add_club_members)
    document.getElementById("add-member-count").innerText = f"Official Club Members: {len(add_club_members)} STUDENTS"
    button = document.getElementById("add-btn-submit")
    button.addEventListener("click", create_proxy(add_member))

setup_add_member()

chk1_club_members = [
    "John Wick",
    "Saint Nicolas",
    "Logan Paul",
    "Bomb Squad 14",
    "Coco Martin"
]

def check_membership_1(event):
    first_name = document.getElementById("chk1-fname").value.strip()
    last_name = document.getElementById("chk1-lname").value.strip()
    full_name = f"{first_name} {last_name}".strip()
    full_name_lower = full_name.lower()
    members_lower = list(map(str.lower, chk1_club_members))
    is_member = full_name_lower in members_lower
    messages = [
        f"Sorry not sorry {full_name}, your name is not on the list, get out.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]
    # This is to display
    document.getElementById("chk1-result").innerText = messages[is_member]

def setup_checker_1(event=None):
    document.getElementById("chk1-members-list").innerText = ", ".join(chk1_club_members)
    button = document.getElementById("chk1-btn-submit")
    button.addEventListener("click", create_proxy(check_membership_1))

window.onload = create_proxy(setup_checker_1)

chk2_club_members = [
    "John Wick",
    "Saint Nicolas",
    "Logan Paul",
    "Bomb Squad 14",
    "Coco Martin"
]

def check_membership_2(event):
    first_name = document.getElementById("chk2-fname").value.strip()
    last_name = document.getElementById("chk2-lname").value.strip()
    full_name = f"{first_name} {last_name}".strip()
    full_name_lower = full_name.lower()
    members_lower = list(map(str.lower, chk2_club_members))
    is_member = full_name_lower in members_lower
    messages = [
        f"Sorry not sorry {full_name}, your name is not on the list, get out.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]
    document.getElementById("chk2-result").innerText = messages[is_member]

def setup_checker_2(event=None):
    document.getElementById("chk2-members-list").innerText = ", ".join(chk2_club_members)
    button = document.getElementById("chk2-btn-submit")
    button.addEventListener("click", create_proxy(check_membership_2))

setup_checker_2()