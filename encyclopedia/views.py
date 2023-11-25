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
                    request, "encyclopedia/index.html", {"entries": to_display}
                )
            else:
                return entry_by_title(request, title=search_entry)
    else:
        return render(request, "encyclopedia/index.html")
