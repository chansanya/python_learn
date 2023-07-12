import requests
from plotly import offline

# 执行API调用并存储响应。
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

print(f"状态码: {r.status_code}")
# 将API响应赋给一个变量。
response_dict = r.json()

# 处理结果。
print(response_dict.keys())

# 将API响应赋给一个变量。
response_dict = r.json()
print(f"总仓库: {response_dict['total_count']}")

# 探索有关仓库的信息。
repo_dicts = response_dict['items']
print(f"获取到仓库数：: {len(repo_dicts)}")

repo_names, stars, labels,repo_links = [], [],[],[]

for repo_dict in repo_dicts:
    print(f"仓库数据属性数: {len(repo_dict)}")
    print(f"名字: {repo_dict['name']}")
    print(f"作者: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"仓库地址: {repo_dict['html_url']}")
    print(f"创建: {repo_dict['created_at']}")
    print(f"修改: {repo_dict['updated_at']}")
    print("============================================")
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)


# 可视化。
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'GitHub上最受欢迎的Python项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='./html/python_repos.html')
