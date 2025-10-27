
      
        function getUrlParam(name) {
            const reg = new RegExp(`(^|&)${name}=([^&]*)(&|$)`);
            const r = window.location.search.substr(1).match(reg);
            return r ? decodeURIComponent(r[2]) : null;
        }

       
        const articleDatabase = {
            1: {
                title: "JavaScript 异步编程全解析",
                date: "2025-10-18",
                tag: "技术",
                tagColor: "primary",
                img: "../image/js.png",
                content: `
                    <p>JavaScript 作为一门单线程语言，异步编程是其核心特性之一。本文将从历史发展的角度，全面解析 JavaScript 异步编程的演进过程。</p>
                    
                    <h3>一、回调函数：异步编程的起点</h3>
                    <p>最早的异步实现方式是回调函数（Callback），通过将后续操作放入回调函数中，在异步任务完成后执行。例如：</p>
                    <pre><code>setTimeout(() => {
  console.log("异步任务完成");
}, 1000);</code></pre>
                    <p>但回调函数存在"回调地狱"问题，多层嵌套会导致代码可读性极差。</p>
                    
                    <h3>二、Promise：解决回调地狱</h3>
                    <p>ES6 引入的 Promise 采用链式调用方式，解决了回调嵌套问题：</p>
                    <pre><code>new Promise((resolve, reject) => {
  setTimeout(() => resolve("第一步完成"), 1000)
})
.then(res => {
  console.log(res);
  return "第二步完成";
})
.then(res => {
  console.log(res);
});</code></pre>
                    
                    <h3>三、async/await：异步编程的终极方案</h3>
                    <p>ES2017 引入的 async/await 语法糖，让异步代码看起来像同步代码：</p>
                    <pre><code>async function asyncTask() {
  const res1 = await new Promise(resolve => {
    setTimeout(() => resolve("第一步"), 1000);
  });
  const res2 = await new Promise(resolve => {
    setTimeout(() => resolve("第二步"), 1000);
  });
  console.log(res1, res2);
}</code></pre>
                    <p>这种方式兼具可读性和简洁性，已成为现代 JavaScript 异步编程的首选方案。</p>
                `
            },
            2: {
                title: "程序员的高效时间管理技巧",
                date: "2025-10-18",
                tag: "生活",
                tagColor: "success",
                img: "../image/shijianguanl.png",
                content: `
                    <p>程序员常常面临 deadlines 的压力，如何高效管理时间成为提升工作质量的关键。以下是经过实践验证的 5 个时间管理技巧。</p>
                    
                    <h3>1. 番茄工作法：碎片化时间管理</h3>
                    <p>将工作分解为 25 分钟的"番茄钟"，每个番茄钟后休息 5 分钟，4 个番茄钟后休息 15-30 分钟。这种方法能有效提升专注力，避免长时间工作导致的效率下降。</p>
                    
                    <h3>2. 任务优先级排序：四象限法则</h3>
                    <p>按照"重要且紧急"、"重要不紧急"、"紧急不重要"、"不紧急不重要"四个象限对任务排序，优先处理"重要且紧急"的任务，同时定期规划"重要不紧急"的任务（如技术学习），避免被紧急但不重要的事情占据时间。</p>
                    
                    <h3>3. 批量处理同类任务</h3>
                    <p>将邮件回复、代码评审、沟通等同类任务集中处理，减少任务切换带来的时间损耗。例如每天固定 10:00 和 16:00 处理邮件，避免随时查看邮件打断编码思路。</p>
                    
                    <h3>4. 学会说"不"：拒绝无效社交和低价值任务</h3>
                    <p>对于超出职责范围或低价值的任务，学会委婉拒绝。专注于能带来核心价值的工作，避免精力被分散。</p>
                    
                    <h3>5. 定期复盘：优化时间分配</h3>
                    <p>每天花 10 分钟回顾当天时间使用情况，每周进行一次总结，分析时间浪费的原因并调整计划，逐步优化时间管理方式。</p>
                `
            },
            3: {
                title: "从零开始学Python数据分析",
                date: "2025-10-19",
                tag: "学习",
                tagColor: "info",
                img: "../image/shujufenxi.jpg",
                content: `
                    <p>Python 凭借其丰富的数据分析库，已成为数据科学领域的首选语言。本文将带你从零开始，掌握 Python 数据分析的核心技能。</p>
                    
                    <h3>一、环境搭建：Anaconda 与 Jupyter Notebook</h3>
                    <p>推荐使用 Anaconda 发行版，内置了数据分析所需的大部分库（如 Pandas、NumPy、Matplotlib），并集成了 Jupyter Notebook 交互式开发环境，非常适合数据分析工作流。</p>
                    
                    <h3>二、核心库入门</h3>
                    <h4>1. NumPy：数值计算基础</h4>
                    <p>NumPy 提供了高性能的多维数组对象和数学函数，是数据分析的基础：</p>
                    <pre><code>import numpy as np
# 创建数组
arr = np.array([1, 2, 3, 4, 5])
# 计算平均值
print(arr.mean())  # 输出：3.0</code></pre>
                    
                    <h4>2. Pandas：数据处理核心</h4>
                    <p>Pandas 提供了 Series（一维数据）和 DataFrame（二维表格数据）两种数据结构，以及丰富的数据处理方法：</p>
                    <pre><code>import pandas as pd
# 读取CSV文件
df = pd.read_csv("data.csv")
# 查看前5行
print(df.head())
# 数据分组统计
print(df.groupby("category")["value"].mean())</code></pre>
                    
                    <h4>3. Matplotlib：数据可视化</h4>
                    <p>Matplotlib 是 Python 最基础的可视化库，可绘制折线图、柱状图、散点图等：</p>
                    <pre><code>import matplotlib.pyplot as plt
# 绘制折线图
plt.plot(df["date"], df["value"])
plt.title("数据趋势图")
plt.xlabel("日期")
plt.ylabel("数值")
plt.show()</code></pre>
                    
                    <h3>三、实战案例：电商销售数据分析</h3>
                    <p>通过分析电商销售数据，掌握数据清洗、特征工程、趋势分析、用户分群等实战技能，将理论知识转化为解决实际问题的能力。</p>
                `
            },
           
            4: {
                title: "React 组件设计模式实战",
                date: "2025-10-20",
                tag: "技术",
                tagColor: "primary",
                img: "../image/react.png",
                content: ` <p>React 组件设计模式的核心是解决复用、逻辑拆分、状态管理等问题，不同场景需匹配对应模式，以下是实战中高频使用的核心模式。</p>
    
    <h3>一、容器组件与展示组件</h3>
    <p>核心是分离数据逻辑与 UI 渲染，让两者各司其职。容器组件负责处理数据请求、状态管理等逻辑，不关注具体 UI 呈现；展示组件是纯 UI 组件，仅通过接收参数渲染界面，不包含任何业务逻辑。</p>
    <p>这种拆分能让展示组件在不同业务场景中灵活复用，容器组件则专注于数据层的逻辑维护，典型示例如下：</p>
    <pre><code>// 容器组件（处理逻辑）
import { useState, useEffect } from 'react';
import UserList from './UserList'; // 展示组件

function UserListContainer() {
  const [users, setUsers] = useState([]);
  
  useEffect(() => {
    // 数据请求逻辑
    fetch('/api/users')
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);
  
  return <UserList users={users} />;
}

// 展示组件（纯UI渲染）
function UserList({ users }) {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}</code></pre>

<h3>二、高阶组件（HOC）</h3>
<p>本质是“组件的装饰器”，通过一个函数接收原始组件，封装通用逻辑后返回一个增强版的新组件。核心作用是实现逻辑复用，比如给多个组件统一添加加载状态、权限校验等功能。</p>
<pre><code>// 高阶组件：添加加载状态逻辑
function withLoading(Component) {
  return function WithLoadingComponent({ isLoading, ...props }) {
    if (isLoading) {
      return <div>加载中...</div>;
    }
    return <Component {...props} />;
  };
}

// 使用高阶组件
const UserListWithLoading = withLoading(UserList);
// 调用：<UserListWithLoading isLoading={true} users={[]} /></code></pre>

<h3>三、自定义 Hook</h3>
<p>React 16.8 后推荐的逻辑复用方案，将组件间共享的状态逻辑抽取成独立函数。这些函数以“use”开头，可直接调用 React 内置 Hook，无需额外嵌套组件。</p>
<pre><code>// 自定义Hook：封装数据请求逻辑
function useFetchData(url) {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then(res => res.json())
      .then(data => setData(data))
      .finally(() => setLoading(false));
  }, [url]);
  
  return { data, loading };
}

// 组件中使用
function UserList() {
  const { data: users, loading } = useFetchData('/api/users');
  
  if (loading) return <div>加载中...</div>;
  return (
    <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>
  );
}</code></pre>

<h3>四、其他常用模式</h3>
<p><strong>复合组件</strong>：通过上下文共享状态，让关联组件（如标签页、下拉菜单）组合使用更自然，实现组件间联动。</p>
<p><strong>render props 模式</strong>：通过参数传递渲染函数，分离“逻辑提供”和“UI 渲染”，灵活定制 UI 样式和结构。</p>
<p><strong>组件懒加载</strong>：拆分非首屏组件为独立代码块，优化初始加载速度，配合 React.lazy 和 Suspense 使用。</p>`
            },
            5: {
                title: "程序员必备的健康管理指南",
                date: "2025-10-20",
                tag: "生活",
                tagColor: "primary",
                img: "../image/chengxuyanjiank.png",
                content: `<p>程序员健康管理的核心是“动静结合、节律作息”，长期久坐、作息不规律易引发肩颈劳损、视力下降等问题，以下是经过实践验证的全方位管理方案。</p>
    
    <h3>一、作息管理：守住生理节律</h3>
    <p>睡眠是身体修复的关键，长期熬夜会导致注意力不集中、免疫力下降，需建立稳定的作息习惯。</p>
    <ul>
      <li>固定作息区间：尽量 23 点前入睡，保证 7-8 小时睡眠，避免凌晨后熬夜编码。</li>
      <li>睡前仪式：睡前 1 小时远离电子屏幕，可用阅读、听白噪音替代刷手机，减少蓝光干扰。</li>
      <li>午间小憩：控制在 20-30 分钟，避免深度睡眠导致下午昏沉，提升下午工作效率。</li>
    </ul>
    
    <h3>二、体态与运动：对抗久坐伤害</h3>
    <p>久坐是程序员健康的头号敌人，需通过科学体态和规律运动缓解身体压力。</p>
    <h4>1. 正确工作体态</h4>
    <p>腰背挺直、双脚平放，屏幕与视线平齐，手臂自然下垂时肘部呈 90 度，避免含胸、低头看设备。</p>
    <h4>2. 碎片化运动方案</h4>
    <p>遵循“20-20-20”原则：每工作 20 分钟，看 6 米外物体 20 秒，缓解眼疲劳。</p>
    <p>每日累计 30 分钟运动，可拆分為 10 分钟/次：</p>
    <ul>
      <li>肩颈拉伸：抬头挺胸，左右转头各 10 次，肩膀环绕运动 15 次。</li>
      <li>手腕保护：握拳放松交替 20 次，避免长时间敲击键盘导致腱鞘炎。</li>
      <li>全身活动：站立踮脚、扩胸运动，促进血液循环。</li>
    </ul>
    
    <h3>三、饮食调理：精准补能</h3>
    <p>合理饮食能提供持续能量，避免因饥饿或高糖饮食导致的效率波动。</p>
    <ul>
      <li>早餐：高蛋白 + 复合碳水（鸡蛋、全麦面包、牛奶），拒绝空腹或仅吃零食。</li>
      <li>补水：每天饮水量不低于 1.5 升，用白开水替代奶茶、碳酸饮料，避免久坐缺水。</li>
      <li>加餐选择：坚果、水果（如蓝莓、香蕉），补充维生素和膳食纤维，缓解便秘。</li>
    </ul>
    
    <h3>四、心理调节：释放编码压力</h3>
    <p>长期面对需求压力和 bug 调试，易产生焦虑情绪，需及时调节心理状态。</p>
    <p>任务拆分：将大需求拆分为小目标，每完成一个小任务适当休息，减少焦虑感。</p>
    <p>兴趣转移：培养非工作兴趣（养花、打球、追剧），脱离代码环境，让大脑切换状态。</p>
    <p>沟通释放：遇到难题时及时与同事沟通，避免独自钻牛角尖，必要时暂停调整思路。</p>`
            },
            6: {
                title: "MySQL 性能优化实战教程",
                date: "2025-10-22",
                tag: "学习",
                tagColor: "primary",
                img: "../image/mysql.png",
                content: `<p>MySQL 性能优化需从索引设计、SQL 优化、配置调优、架构升级四个维度逐步深入，不合理的设计或查询会导致性能差距达 100 倍以上，以下是实战导向的优化方案。</p>
    
    <h3>一、索引优化：性能提升的基石</h3>
    <p>索引是加速查询的核心，需遵循“按需创建、避免冗余”原则，否则会增加写入成本。</p>
    <h4>1. 必建索引的场景</h4>
    <ul>
      <li>主键索引：InnoDB 表必须有主键（建议用自增 ID，避免 UUID 碎片化）。</li>
      <li>高频查询字段：WHERE、JOIN、ORDER BY、GROUP BY 涉及的字段（如 user_id、order_no）。</li>
    </ul>
    <h4>2. 联合索引的最左前缀原则</h4>
    <p>联合索引 (a,b,c) 仅能匹配 a、a+b、a+b+c 的查询场景，需按查询频率排序字段。</p>
    <pre><code>// 有效查询（命中联合索引）
SELECT * FROM order WHERE a=1;
SELECT * FROM order WHERE a=1 AND b=2;
// 无效查询（未命中联合索引）
SELECT * FROM order WHERE b=2;
SELECT * FROM order WHERE a=1 AND c=3;</code></pre>
    <h4>3. 索引失效的常见坑</h4>
    <p>WHERE 中用函数/计算：WHERE SUBSTR(name,1,3)='abc'（改用 name LIKE 'abc%'）。</p>
    <p>隐式类型转换：WHERE phone='13800138000'（phone 为 int 类型时索引失效）。</p>
    <p>LIKE 以 % 开头：WHERE name LIKE '%abc'（无法走索引，可考虑全文索引）。</p>
    
    <h3>二、SQL 语句优化：从“能跑”到“快跑”</h3>
    <h4>1. 避免全表扫描的技巧</h4>
    <p>用 EXPLAIN 分析执行计划，type 字段为 ALL 表示全表扫描，需优化：</p>
    <pre><code>// 分析查询计划
EXPLAIN SELECT * FROM order WHERE user_id=123;
// 优化点：user_id 需建索引</code></pre>
    <p>禁止 SELECT *：只查需要的字段，减少 IO 和内存消耗，触发覆盖索引。</p>
    <h4>2. 深分页优化</h4>
    <p>LIMIT 100000,10 会扫描前 100010 行，改用“基于主键定位”：</p>
    <pre><code>// 优化前（慢）
SELECT * FROM article LIMIT 100000, 10;
// 优化后（快，需主键自增）
SELECT * FROM article WHERE id > 100000 LIMIT 10;</code></pre>
    <h4>3. 子查询改 JOIN</h4>
    <pre><code>// 优化前（子查询创建临时表）
SELECT * FROM user WHERE id IN (SELECT user_id FROM order WHERE status=1);
// 优化后（JOIN 效率更高）
SELECT u.* FROM user u JOIN order o ON u.id=o.user_id WHERE o.status=1;</code></pre>
    
    <h3>三、配置调优与架构升级</h3>
    <p><strong>核心配置参数</strong>：innodb_buffer_pool_size 设为物理内存的 50%-70%，提升缓存命中率；innodb_log_file_size 增至 1-2G，减少日志切换频率。</p>
    <p><strong>读写分离</strong>：主库负责写操作，从库负责读操作，通过 binlog 同步数据，缓解主库压力。</p>
    <p><strong>分库分表</strong>：单表数据超 1000 万时，水平分表（按 user_id 哈希拆分）或垂直分表（拆分宽表字段），避免单表过大。</p>`
            },
            7: {
                title: "git 使用进阶指南",
                date: "2025-10-15",
                tag: "推荐",
                tagColor: "primary",
                img: "../image/git.jpg",
                content: ` <p>Git 是分布式版本控制系统的标杆，掌握进阶用法能大幅提升团队协作效率，避免代码冲突、版本回滚等问题，以下是实战高频技巧。</p>
    
    <h3>一、分支管理策略</h3>
    <p>合理的分支模型是团队协作的基础，主流采用 Git Flow 或简化版策略。</p>
    <h4>1. 核心分支类型</h4>
    <ul>
      <li>main/master：生产环境分支，保持稳定可部署状态。</li>
      <li>develop：开发分支，集成各功能分支的代码。</li>
      <li>feature/*：功能分支，从 develop 分出，完成后合并回 develop。</li>
      <li>hotfix/*：紧急修复分支，从 main 分出，修复后同步到 main 和 develop。</li>
    </ul>
    <h4>2. 分支操作示例</h4>
    <pre><code>// 创建并切换功能分支
git checkout -b feature/user-login develop
// 提交代码
git add .
git commit -m "完成用户登录功能"
// 合并到开发分支（本地）
git checkout develop
git merge feature/user-login
// 删除功能分支
git branch -d feature/user-login</code></pre>
    
    <h3>二、代码提交与撤销技巧</h3>
    <p>规范提交信息和灵活撤销操作，能保持提交记录清晰，避免误操作影响版本。</p>
    <h4>1. 规范提交信息</h4>
    <pre><code>// 格式：类型(范围): 描述（如 feat(登录): 新增短信验证码登录）
git commit -m "feat(login): add sms verification"
// 类型说明：feat(新功能)、fix(修复)、docs(文档)、style(格式)、refactor(重构)</code></pre>
    <h4>2. 撤销操作</h4>
    <pre><code>// 撤销工作区修改（未 git add）
git checkout -- 文件名
// 撤销暂存区修改（已 git add 未 commit）
git reset HEAD 文件名
// 回滚到上一个提交（保留修改，可重新提交）
git reset --soft HEAD~1
// 强制回滚到指定版本（谨慎使用，已推送的分支避免）
git reset --hard 提交ID</code></pre>
    
    <h3>三、冲突解决与协作技巧</h3>
    <p>多人协作时难免出现代码冲突，掌握高效解决方法和协作规范很重要。</p>
    <h4>1. 冲突解决步骤</h4>
    <pre><code>// 拉取远程最新代码
git pull origin develop
// 若出现冲突，编辑冲突文件（查找 <<<<<<< 标记）
// 解决后标记为已解决并提交
git add 冲突文件名
git commit -m "resolve conflict: 合并用户登录与权限控制代码"</code></pre>
    <h4>2. 协作高频命令</h4>
    <pre><code>// 关联远程分支
git remote add origin https://github.com/xxx/project.git
// 推送本地分支到远程
git push -u origin feature/user-login
// 拉取指定远程分支
git pull origin develop
// 查看远程分支
git remote -v
// 抓取远程分支（不合并）
git fetch origin</code></pre>
    
    <h3>四、进阶功能： stash 与 cherry-pick</h3>
    <p>应对临时切换分支、选择性合并代码等场景。</p>
    <pre><code>// 暂存工作区修改（切换分支时用）
git stash
// 恢复暂存的修改
git stash pop
// 选择性合并指定提交（如从 hotfix 合并到 develop）
git cherry-pick 提交ID</code></pre>`
            },
            8: {
                title: "linux 常用命令大全",
                date: "2025-10-23",
                tag: "推荐",
                tagColor: "primary",
                img: "../image/linux.jpg",
                content: `<p>Linux 是服务器端的主流操作系统，掌握常用命令能高效完成文件操作、进程管理、系统监控等工作，以下是开发和运维高频使用的命令集合。</p>
    
    <h3>一、文件与目录操作</h3>
    <p>核心命令覆盖目录切换、文件创建、复制、删除等基础操作，是日常使用的基础。</p>
    <pre><code>// 切换目录
cd /usr/local  // 绝对路径
cd ../test     // 相对路径（上一级目录下的 test）
cd ~           // 切换到用户主目录

// 查看目录内容
ls -l          // 详细列表（权限、大小、时间）
ls -a          // 显示隐藏文件（含 . 和 ..）

// 文件操作
touch test.txt // 创建文件
mkdir -p a/b/c // 递归创建多级目录
cp file1.txt dir1/ // 复制文件到目录
mv file1.txt file2.txt // 重命名文件
rm -rf dir1    // 强制删除目录及内容（谨慎使用）

// 查看文件内容
cat test.txt   // 查看全部内容
head -10 test.txt // 查看前10行
tail -f log.txt // 实时查看日志文件（常用）</code></pre>
    
    <h3>二、进程与服务管理</h3>
    <p>查看和控制进程、服务，解决程序卡死、端口占用等问题。</p>
    <pre><code>// 查看进程
ps -ef         // 查看所有进程
ps -ef | grep java // 过滤出 java 相关进程
top            // 实时监控进程资源占用（按 q 退出）

// 终止进程
kill -9 进程ID  // 强制终止进程（9 表示强制）

// 服务管理（systemd 系统）
systemctl start nginx  // 启动 nginx 服务
systemctl stop nginx   // 停止服务
systemctl restart nginx // 重启服务
systemctl status nginx // 查看服务状态
systemctl enable nginx // 设置开机自启</code></pre>
    
    <h3>三、文件权限与网络操作</h3>
    <p>权限配置保障文件安全，网络命令用于排查连接问题。</p>
    <pre><code>// 文件权限设置（r=4, w=2, x=1）
chmod 755 test.sh // 所有者 rwx，其他 rx（常用脚本权限）
chown user:group test.txt // 修改文件所有者和组

// 网络命令
ifconfig       // 查看网卡信息（部分系统用 ip addr）
ping www.baidu.com // 测试网络连通性
netstat -tuln  // 查看监听端口（t=TCP, u=UDP, l=监听, n=数字端口）
curl https://api.xxx.com // 发送 HTTP 请求（测试接口）
wget https://xxx.com/file.tar.gz // 下载文件</code></pre>
    
    <h3>四、压缩与查找命令</h3>
    <pre><code>// 压缩解压
tar -zcvf test.tar.gz dir1/ // 压缩目录为 tar.gz 格式
tar -zxvf test.tar.gz       // 解压 tar.gz 文件
unzip test.zip              // 解压 zip 文件

// 查找文件
find / -name "nginx.conf"  // 从根目录查找文件
grep "error" log.txt       // 在文件中查找字符串
grep -r "error" /var/log/  // 递归查找目录下含指定字符串的文件</code></pre>`
            },
            9: {
                title: "python 第三方库推荐",
                date: "2025-10-11",
                tag: "推荐",
                tagColor: "primary",
                img: "../image/python.jpg",
                content: ` <p>Python 生态的核心优势是丰富的第三方库，能快速实现各类功能，避免重复造轮子，以下是开发中高频使用的优质库推荐。</p>
    
    <h3>一、数据处理与分析库</h3>
    <p>此类库是数据分析、人工智能领域的基础，高效处理结构化和非结构化数据。</p>
    <h4>1. Pandas：数据处理神器</h4>
    <p>提供 DataFrame 数据结构，支持数据清洗、筛选、分组统计等操作，是数据分析的核心库。</p>
    <pre><code>import pandas as pd

// 读取 CSV 文件
df = pd.read_csv("data.csv")
// 查看数据基本信息
print(df.info())
// 数据筛选（年龄大于 30 的用户）
df_filtered = df[df["age"] > 30]
// 分组统计（按性别统计平均年龄）
df_grouped = df.groupby("gender")["age"].mean()
// 保存结果
df_filtered.to_csv("filtered_data.csv", index=False)</code></pre>
    <h4>2. NumPy：数值计算基础</h4>
    <p>提供高性能多维数组对象和数学函数，是 Pandas、Matplotlib 等库的依赖基础，适合数值运算。</p>
    <h4>3. Matplotlib/Seaborn：数据可视化</h4>
    <p>Matplotlib 是基础可视化库，支持折线图、柱状图等；Seaborn 基于 Matplotlib，样式更美观，操作更简洁。</p>
    
    <h3>二、Web 开发相关库</h3>
    <p>快速搭建 Web 应用、接口服务，适合后端开发场景。</p>
    <h4>1. Flask：轻量级 Web 框架</h4>
    <p>灵活简洁，适合小型应用和接口开发，学习成本低。</p>
    <pre><code>from flask import Flask, jsonify

app = Flask(__name__)

// 定义接口
@app.route("/api/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = {"id": user_id, "name": "张三", "age": 25}
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)</code></pre>
    <h4>2. Requests：HTTP 请求库</h4>
    <p>简洁易用，替代原生 urllib，支持 GET/POST 请求、文件上传、Cookie 管理等。</p>
    <h4>3. Django：全栈 Web 框架</h4>
    <p>内置 ORM、Admin 后台、认证系统，适合大型Web应用开发，开箱即用。</p>
    
    <h3>三、其他实用库</h3>
    <ul>
      <li><strong>BeautifulSoup4</strong>：网页爬虫必备，解析 HTML/XML 数据，提取关键信息。</li>
      <li><strong>PyPDF2</strong>：处理 PDF 文件，支持读取、合并、拆分 PDF。</li>
      <li><strong>logging</strong>：日志记录库，替代 print，支持分级、文件输出、格式化。</li>
      <li><strong>pytest</strong>：单元测试框架，简化测试用例编写和执行，支持断言、夹具等功能。</li>
      <li><strong>datetime</strong>：时间处理库，解决日期格式化、时间差计算等问题。</li>
    </ul>`
            }

        };


        function loadArticle() {
            const articleId = getUrlParam('id');
            const loading = document.getElementById('loading');
            const error = document.getElementById('error');
            const articleContent = document.getElementById('articleContent');

            if (!articleId || !articleDatabase[articleId]) {
                loading.style.display = 'none';
                error.style.display = 'block';
                return;
            }


            const article = articleDatabase[articleId];

            document.getElementById('articleTitle').textContent = article.title;
            document.getElementById('articleDate').textContent = article.date;
            document.getElementById('articleImg').src = article.img;
            document.getElementById('articleImg').alt = article.title;
            document.getElementById('articleBody').innerHTML = article.content;
            
          
            const tagHtml = `<span class="badge badge-${article.tagColor} article-tag">${article.tag}</span>`;
            document.getElementById('articleTags').innerHTML = tagHtml;

        
            loading.style.display = 'none';
            articleContent.style.display = 'block';
        }


        window.onload = loadArticle;
