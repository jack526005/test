const express = require('express');
const path = require('path');
const fs = require('fs');
const cors = require('cors');
const { time } = require('console');
const app = express();
const PORT = 3000;
const DB_FILE = path.join(__dirname, 'db.json');
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

//let nextId=4;
function loadTodos(){
    if(fs.existsSync(DB_FILE)){
      try{
       const raw=fs.readFileSync(DB_FILE,'utf-8'); 
        todos=JSON.parse(raw);
        nextId=todos.length>0?Math.max(...todos.map(t=>t.id))+1:1;
      }catch(err){
        console.error('加载待办事项失败:',err);
        todos=[];
      }
        
    }
  }
  loadTodos();
function saveTodos(){
  try{
    fs.writeFileSync(DB_FILE,JSON.stringify(todos,null,2));
  }catch(err){
    console.error('保存待办事项失败:',err);
  }
}
app.get('/api/todos',(req,res)=>{
    res.json(todos);
})
app.post('/api/todos',(req,res)=>{
    const {title}=req.body;
    if(!title||typeof title!=='string'){
      return res.status(400).json({error:'无效的标题'});
    }
    const newTodo={id:nextId++,title:title,completed:false};
    todos.push(newTodo);
    saveTodos();
    res.status(201).json(newTodo);
});
app.patch('/api/todos/:id',(req,res)=>{
    const id=parseInt(req.params.id,10);
    const todo=todos.find(t=>t.id===id); 
    if(!todo){
      return res.status(404).json({error:'待办事项未找到'});
    }
    const {title,completed}=req.body;
    if(typeof title==='string'){
      todo.title=title;
    }
    if(typeof completed==='boolean'){
      todo.completed=completed;
    }
    saveTodos();
    res.json(todo);

  })
app.delete('/api/todos/:id',(req,res)=>{
    const id=parseInt(req.params.id,10);
    const index=todos.findIndex(t=>t.id===id);
    if(index===-1){
      return res.status(404).json({error:'待办事项未找到'});
    }
    todos.splice(index,1);
    saveTodos();
    res.status(204).end("删除成功");
   
  });

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
})