from django.shortcuts import render, get_object_or_404, redirect
from .models import L1_Name, Issue_History
from .forms import PostForm

def l1_list(request):
    l1names = L1_Name.objects.all()
    return render(request, 'mc_report/l1_list.html', {'l1names': l1names})

def issue_list(request, pk):
    l1_name = get_object_or_404(L1_Name, pk=pk)
    issues = Issue_History.objects.filter(l1_name=l1_name)
    return render(request, 'mc_report/issue_list.html', {'issues': issues})


def post_issue(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # 新しく作成された投稿の詳細ページにリダイレクト
            return redirect('issue_list', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mc_report/post_edit.html', {'form': form})