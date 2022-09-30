#### 代码：

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
//上面是引用空间,需要在这引入相应工具箱才能在接下来代码使用

public class PlayeeMove : MonoBehaviour
{
    public float speed; //声明变量,不去赋值会有相应的默认值不会出bug
    
    public Vector3 playerInput; //引用变量，它是存储三维空间中物体位置的组件 Vector3 == (x,y,z)
    
    //游戏场景出现后运行
    void Start(){
        
    }
    
    //游戏每一帧都运行
    void Update(){
        //时实检测玩家的方向键输入，然后将其转换成（0，0）的坐标值存储起来
      playerInput = new Vector3(Input.GetAxisRaw("Horizontal"),
      Input.GetAxisRaw("Vertical"));  
   
        //自带的工具箱，代表的是脚本绑定的Game Object的当前的位置
        transform.position = playerInput*speed*Time.deltaTime
        +transform.position;
        //Time.deltaTime代表时间的变量, 加上后可以让角色速度不受帧影响
    }
}

```



```c#
public int health //其他代码文件也可以使用这些信息 会显示在unity界面中（方便频繁调试）
      
//开放性  类型  名字
      
private int health //局限于当前的脚本中
```

