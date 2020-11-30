# miniCmd
 打造一款平台通用的Cmd命令行窗口，无需安装第三方依赖，初始Python3环境即可使用。
<h3>目前已实现的命令行功能：</h3>
<ol>
    <li>
        ls：列举当前目录下的文件和文件夹，参数有：
        <ol>
            <li>-f：列举当前目录下的所有文件；</li>
            <li>-F：列举当前目录下的所有文件夹；</li>
            <li>后缀名限制查找，支持过滤的后缀名有：'.docx', '.py', '.txt', '.zip', '.rar' , '.xlsx', '.xls', '.rtf', '.ppt', '.pptx' , '.doc', '.exe', '.dll', '.png', '.jpg' , '.sql', '.bmp', '.css', '.less', '.js' , '.vue', '.c', '.java', '.cpp', '.cs', '.sln', '.xml', '.json'。</li>
        </ol>
    </li>
    <li>pwd：获取当前路径。</li>
    <li>
        cd：切换路径，参数有：
        <ol>
            <li>..：返回上级目录；</li>
            <li>../..：返回上上级目录；</li>
            <li>path：合法有效的路径。</li>
        </ol>
    </li>
    <li>unzip：解压，支持解压的格式有：'.tar.bz2', '.tbz2', '.tar.gz', '.tgz', '.tar', '.tar.xz', '.txz', '.zip'。</li>
    <li>
        rm：删除文件或文件夹，参数有：
        <ol>
            <li>-f：永久删除文件，可同时删除多个文件；</li>
            <li>-rf：永久删除目录，可同时删除多个文件夹，文件夹不为空也会删除。</li>
        </ol>
    </li>
    <li>mkdir：新建文件夹，可一次性建立多个文件夹。</li>
    <li>mkfile：新建文件，可一次性建立多个文件。</li>
    <li>cls：清空命令行。</li>
    <li>ping：测试网络连接量。</li>
    <li>quit或q：退出命令行。</li>
    <li>date：获取当前时间。</li>
    <li>django: 快速生成Django应用程序目录结构（个人完善版）。</li>
    <li>print：python3语法输出。因为本命令行的实现基于python，所以python的任何语法都能够在本黑窗口实现。</li>
</ol>
