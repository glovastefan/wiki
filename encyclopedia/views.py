from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry_by_title(request, title):
    return render(
        request,
        "encyclopedia/view_entry.html",
        {"entry": util.get_entry(title=title), "title": title},
    )


def search(request):
    if request.method == "POST":
        search_entry = request.POST.get("q", None)
        all_entries = util.list_entries()
        if search_entry in all_entries:
            return entry_by_title(request, title=search_entry)
        else:
            to_display = [
                entry for entry in all_entries if search_entry.lower() in entry.lower()
            ]
            if to_display:
                return render(
                    request, "encyclopedia/index.html", {"entries": to_display, "search": True}
                )
            else:
                return entry_by_title(request, title=search_entry)
    else:
        return render(request, "encyclopedia/index.html")
    
def new_entry(request):
    if request.method == "POST":
        new_title = request.POST.get("new_title")
        new_page = request.POST.get("new_entry_text")
        if not new_title:
            return render(request, "encyclopedia/error.html", {
                "error_message": "Title must be provided"
            })
        else:
            all_entries = [title.lower() for title in util.list_entries()]
            if new_title.lower() in all_entries:
                return render(request, "encyclopedia/error.html", {
                    "error_message": f"Title {new_title} already exist!"
                })
            else:
                with open(f"entries/{new_title}.md", "w") as new_file:
                    print(f"# {new_title}\n", file=new_file)
                    print(f"{new_page}", file=new_file)
                return render(request, "encyclopedia/new_page.html")

    else:
        return render(request, "encyclopedia/new_page.html")
