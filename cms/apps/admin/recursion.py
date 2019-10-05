def create_file_list(data):
    tr_td = """
    <tr>
        <td>{id}</td>
        <td>{name}</td>
        <td>
            <a href="javascript:;" onClick="file_del(this,'{id}')">删除</a>
            <a href="/admin/file_down?id={id}">下载</a>
        </td>
    </tr>
    """
    html = ''
    for row in data:
        html += tr_td.format(id=row.fid,name=row.name)
    return html