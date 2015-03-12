// js学起来也好多坑
// 函数里传参后赋值和python就大不一样(赋值传入函数的参数新对象)
// 一个button 的function内的所有运算会阻塞所有的响应 大约要用setTimeout来解决吧 有其他方法么
// document.getElementById 写起来好长啊......
// ()?():() 和 for(a in b) 似乎我的用法有问题 python的 a = b if c else d 真是suan爽
// 话说js有PEP8似的规范么
var state = "init";
var targetImageData;
var targetData;
var parent;
var child;
var yo = document.getElementById("result");
var ctx = yo.getContext("2d");
var config = {};
var total = {};

function start(){
    if(state == "init"){
        state = "looping";
        parent = new Drawing(config.triangleNum, ctx);
        child = new Drawing(config.triangleNum, ctx, parent);
        setTimeout(function(){looping(parent, child, targetData, ctx)}, 1);
    }
    else if(state == "pause"){
        state = "looping";
        setTimeout(function(){looping(total.parent, total.child, targetData, ctx)}, 1);
    }
}

function stop(){
    state = "init";
}

function pause(){
    state = "pause";
}

window.onload = function(){

    var picSelection = document.getElementById("targetToSelect");
    var targetCanvas = document.getElementById("target");
    var targetCtx = targetCanvas.getContext("2d");
    targetCtx.clearRect(0, 0, 256, 256);
    var image = new Image();
    image.onload = function(){
        targetCtx.drawImage(image, 0, 0);
        targetImageData = targetCtx.getImageData(0, 0, 256, 256);
        targetData = targetImageData.data;
    // Update existing image src on your page
    }
    image.src = "/static/image/" + picSelection.value + ".png";
    config.triangleNum = 80;
    config.point_max_mutate_rate = 0.0008;
    config.point_max_rate_mutate_range_down = 0;
    config.point_max_rate_mutate_range_up = 255;
    config.point_mid_mutate_rate = 0.003;
    config.point_mid_rate_mutate_range = 10;
    config.point_min_mutate_rate = 0.009;
    config.point_min_rate_mutate_range = 5;
    config.color_max_mutate_rate = 0.0008;
    config.color_max_rate_mutate_range_down = 0;
    config.color_max_rate_mutate_range_up = 255;
    config.color_mid_mutate_rate = 0.003;
    config.color_mid_rate_mutate_range = 10;
    config.color_min_mutate_rate = 0.009;
    config.color_min_rate_mutate_range = 5;
    config.color_alpha = 0.35;
}

function setIt(){
    if(state == "looping" || state == "pause"){
        if(config.triangleNum != document.getElementById("triangleNum").value){
            alert("oh no! Do not change triangleNum when looping or pause!\r\ngoogle 翻译:哦，不！不要改变triangleNum当循环或暂停");
            return;
        }
        if(document.getElementById("point_max_rate_mutate_range_down").value >= document.getElementById("point_max_rate_mutate_range_up").value ||
           document.getElementById("color_max_rate_mutate_range_down").value >= document.getElementById("color_max_rate_mutate_range_up").value ||
           document.getElementById("point_max_rate_mutate_range_down").value < 0 ||
           document.getElementById("point_max_rate_mutate_range_up").value > 255 ||
           document.getElementById("color_max_rate_mutate_range_down").value < 0 ||
           document.getElementById("color_max_rate_mutate_range_up").value > 255){
            alert("Do not trick me. XD\r\ngoogle翻译:不要欺骗我.XD");
            return;
        }
        config.point_max_mutate_rate            = document.getElementById("point_max_mutate_rate").value;
        config.point_max_rate_mutate_range_down = document.getElementById("point_max_rate_mutate_range_down").value;
        config.point_max_rate_mutate_range_up   = document.getElementById("point_max_rate_mutate_range_up").value;
        config.point_mid_mutate_rate            = document.getElementById("point_mid_mutate_rate").value;
        config.point_mid_rate_mutate_range      = document.getElementById("point_mid_rate_mutate_range").value;
        config.point_min_mutate_rate            = document.getElementById("point_min_mutate_rate").value;
        config.point_min_rate_mutate_range      = document.getElementById("point_min_rate_mutate_range").value;
        config.color_max_mutate_rate            = document.getElementById("color_max_mutate_rate").value;
        config.color_max_rate_mutate_range_down = document.getElementById("color_max_rate_mutate_range_down").value;
        config.color_max_rate_mutate_range_up   = document.getElementById("color_max_rate_mutate_range_up").value;
        config.color_mid_mutate_rate            = document.getElementById("color_mid_mutate_rate").value;
        config.color_mid_rate_mutate_range      = document.getElementById("color_mid_rate_mutate_range").value;
        config.color_min_mutate_rate            = document.getElementById("color_min_mutate_rate").value;
        config.color_min_rate_mutate_range      = document.getElementById("color_min_rate_mutate_range").value;
        config.color_alpha                      = document.getElementById("color_alpha").value;
    }
    else if(state == "init"){
        config.triangleNum                      = document.getElementById("triangleNum").value;
        config.point_max_mutate_rate            = document.getElementById("point_max_mutate_rate").value;
        config.point_max_rate_mutate_range_down = document.getElementById("point_max_rate_mutate_range_down").value;
        config.point_max_rate_mutate_range_up   = document.getElementById("point_max_rate_mutate_range_up").value;
        config.point_mid_mutate_rate            = document.getElementById("point_mid_mutate_rate").value;
        config.point_mid_rate_mutate_range      = document.getElementById("point_mid_rate_mutate_range").value;
        config.point_min_mutate_rate            = document.getElementById("point_min_mutate_rate").value;
        config.point_min_rate_mutate_range      = document.getElementById("point_min_rate_mutate_range").value;
        config.color_max_mutate_rate            = document.getElementById("color_max_mutate_rate").value;
        config.color_max_rate_mutate_range_down = document.getElementById("color_max_rate_mutate_range_down").value;
        config.color_max_rate_mutate_range_up   = document.getElementById("color_max_rate_mutate_range_up").value;
        config.color_mid_mutate_rate            = document.getElementById("color_mid_mutate_rate").value;
        config.color_mid_rate_mutate_range      = document.getElementById("color_mid_rate_mutate_range").value;
        config.color_min_mutate_rate            = document.getElementById("color_min_mutate_rate").value;
        config.color_min_rate_mutate_range      = document.getElementById("color_min_rate_mutate_range").value;
        config.color_alpha                      = document.getElementById("color_alpha").value;
    }

}
function changeSelect(val){
    state = "init";
    var picSelection = document.getElementById("targetToSelect");
    var targetCanvas = document.getElementById("target");
    var targetCtx = targetCanvas.getContext("2d");
    targetCtx.clearRect(0, 0, 256, 256);
    var image = new Image();
    image.onload = function(){
        targetCtx.drawImage(image, 0, 0);
        targetImageData = targetCtx.getImageData(0, 0, 256, 256);
        targetData = targetImageData.data;
    }
    image.src = "/static/image/" + picSelection.value + ".png";
    console.log(targetData);
}

// [s, e)
function randRange(s, e){
    var range = e - s;
    return s + Math.floor(Math.random() * range);
}
// [0,num)
function randWithNum(num){
    return randRange(0, num);
}
// random < num >> True
function rand(num){
    return Math.random() < num;
}

function Color(r, g, b, a){
    // || means or in python OMG
    this.r = r || randWithNum(255);
    this.g = g || randWithNum(255);
    this.b = b || randWithNum(255);
    this.a = 0.4;
}

Color.max_mutate_rate = 0.0008;
Color.mid_mutate_rate = 0.003;
Color.min_mutate_rate = 0.009;

Color.prototype.mutate = function(){
    var totalMutated = 0;
    if(rand(config.color_max_mutate_rate))
    {
        this.r = randRange(config.color_max_rate_mutate_range_down, config.color_max_rate_mutate_range_up);
        totalMutated += 1;
    }
    else if(rand(config.color_mid_mutate_rate))
    {
        this.r = Math.min(Math.max(0, this.r + randRange(-config.color_mid_rate_mutate_range, config.color_mid_rate_mutate_range)), 255);
        totalMutated += 1;
    }
    else if(rand(config.color_min_mutate_rate))
    {
        this.r = Math.min(Math.max(0, this.r + randRange(-config.color_min_rate_mutate_range, config.color_min_rate_mutate_range)), 255);
        totalMutated += 1;
    }

    if(rand(config.color_max_mutate_rate))
    {
        this.g = randWithNum(255);
        totalMutated += 1;
    }
    else if(rand(config.color_mid_mutate_rate))
    {
        this.g = Math.min(Math.max(0, this.g + randRange(-config.color_mid_rate_mutate_range, config.color_mid_rate_mutate_range)), 255);
        totalMutated += 1;
    }
    else if(rand(config.color_min_mutate_rate))
    {
        this.g = Math.min(Math.max(0, this.g + randRange(-config.color_min_rate_mutate_range, config.color_min_rate_mutate_range)), 255);
        totalMutated += 1;
    }

    if(rand(config.color_max_mutate_rate))
    {
        this.b = randWithNum(255);
        totalMutated += 1;
    }
    else if(rand(config.color_mid_mutate_rate))
    {
        this.b = Math.min(Math.max(0, this.b + randRange(-config.color_mid_rate_mutate_range, config.color_mid_rate_mutate_range)), 255);
        totalMutated += 1;
    }
    else if(rand(config.color_min_mutate_rate))
    {
        this.b = Math.min(Math.max(0, this.b + randRange(-config.color_min_rate_mutate_range, config.color_min_rate_mutate_range)), 255);
        totalMutated += 1;
    }
    return totalMutated;

}

function Point(x, y){
    this.x = x || randWithNum(255);
    this.y = y || randWithNum(255);
}

Point.max_mutate_rate = 0.0008;
Point.mid_mutate_rate = 0.003;
Point.min_mutate_rate = 0.009;

Point.prototype.mutate = function(){
    var totalMutated = 0;
    if(rand(config.point_max_mutate_rate)){
        this.x = randRange(config.point_max_rate_mutate_range_down, config.point_max_rate_mutate_range_up);
        this.y = randRange(config.point_max_rate_mutate_range_down, config.point_max_rate_mutate_range_up);
        totalMutated += 1;
    }
    else if(rand(config.point_mid_mutate_rate)){
        this.x = Math.min(Math.max(0, this.x + randRange(-config.point_mid_rate_mutate_range, config.point_mid_rate_mutate_range)), 255);
        this.y = Math.min(Math.max(0, this.y + randRange(-config.point_mid_rate_mutate_range, config.point_mid_rate_mutate_range)), 255);
        totalMutated += 1;
    }
    else if(rand(config.point_min_mutate_rate)){
        this.x = Math.min(Math.max(0, this.x + randRange(-config.point_min_rate_mutate_range, config.point_min_rate_mutate_range)), 255);
        this.y = Math.min(Math.max(0, this.y + randRange(-config.point_min_rate_mutate_range, config.point_min_rate_mutate_range)), 255);
        totalMutated += 1;
    }
    return totalMutated;
}

function Triangle(ps, color){
    this.points = new Array(3);
    for(var i = 0; i < 3; i++){
        if(ps){
            this.points[i] = new Point(ps[i].x, ps[i].y);
        }
        else{
            this.points[i] = new Point();
        }
        // (ps)? (this.points[i] = new Point(ps[i].x, ps[i].y)) : (this.points[i] = new Point());
    }
    (color)? (this.color = new Color(color.r, color.g, color.b, color.a)) : (this.color = new Color());
}

Triangle.prototype.mutate = function(){
    var totalMutated = 0;
    // for(p in this.points){
    for(var i = 0; i < 3; i++){
        totalMutated += this.points[i].mutate();
    }
    totalMutated += this.color.mutate();
    return totalMutated;
}

Triangle.prototype.draw = function(ctx){
    ctx.beginPath();
    ctx.fillStyle = 'rgb('+ this.color.r + ',' + this.color.g + ',' + this.color.b + ')';
    ctx.moveTo(this.points[0].x, this.points[0].y);
    ctx.lineTo(this.points[1].x, this.points[1].y);
    ctx.lineTo(this.points[2].x, this.points[2].y);
    ctx.closePath();
    ctx.fill();
}

function Drawing(triangleNum, ctx, parent){
    this.triangles = new Array(triangleNum);
    this.triangleNum = triangleNum;
    this.matchRate = 0;
    this.ctx = ctx;
    if(!parent){
        this.initAsParent();
    }
    else{
        this.cloneAndMutateFromParent(parent);
    }
}

Drawing.prototype.initAsParent = function(){
    for(var i = 0; i < this.triangleNum; i ++){
        this.triangles[i] = new Triangle();
    }
}

Drawing.prototype.cloneAndMutateFromParent = function(parent){
    var totalMutated = 0;
    for(var i = 0; i < this.triangleNum; i++){
        this.triangles[i] = new Triangle(parent.triangles[i].points, parent.triangles[i].color);
        totalMutated += this.triangles[i].mutate();
    }
    if(totalMutated < 1){
        // it's dirty but hmmmm...
        // I just wanna child mutate everytime
        // 默认参数下的数学期望是>1的
        this.dirty();
    }
}

Drawing.prototype.dirty = function(){
    var dirtyOne = randWithNum(this.triangleNum);
    var dirtyP = randWithNum(4);
    if(dirtyP < 3){
        this.triangles[dirtyOne].points[dirtyP].x = Math.min(Math.max(0, this.triangles[dirtyOne].points[dirtyP].x + randRange(-5, 5)), 255);
        this.triangles[dirtyOne].points[dirtyP].y = Math.min(Math.max(0, this.triangles[dirtyOne].points[dirtyP].y + randRange(-5, 5)), 255);
    }
    else{
        this.triangles[dirtyOne].color.r = Math.min(Math.max(0, this.triangles[dirtyOne].color.r + randRange(-8, 8)), 255);
        this.triangles[dirtyOne].color.g = Math.min(Math.max(0, this.triangles[dirtyOne].color.g + randRange(-8, 8)), 255);
        this.triangles[dirtyOne].color.b = Math.min(Math.max(0, this.triangles[dirtyOne].color.b + randRange(-8, 8)), 255);
    }
}

Drawing.prototype.draw = function(){
    this.ctx.clearRect(0, 0, 256, 256);
    this.ctx.globalAlpha = config.color_alpha;
    for(var i = 0; i < this.triangles.length; i++){
        this.triangles[i].draw(this.ctx);
    }
}

Drawing.prototype.calcRate = function(targetData){
    if(this.matchRate > 0){
        console.log(this.matchRate);
        return this.matchRate;
    }
    this.draw();
    this.matchRate = 0;
    var resultMatchRate = this.ctx.getImageData(0, 0, 256, 256);
    // for(i in resultMatchRate.data)
    for(var i = 0; i < resultMatchRate.data.length; i++){
        // alpha is out of our concern
        // matchRate += Delta r * Delta r + Delta g * Delta g + Delta b * Delta b
        if(i%3==0){
            continue;
        }
        this.matchRate += (targetData[i] - resultMatchRate.data[i]) * (targetData[i] - resultMatchRate.data[i]);
    }
    console.log(this.matchRate);
    return this.matchRate;
}

Drawing.prototype.drawIt = function(ctx){
    ctx.clearRect(0, 0, 256, 256);
    ctx.globalAlpha = 0.35;
    for(var i = 0; i < this.triangles.length; i++){
        this.triangles[i].draw(ctx);
    }
}

function looping(parent, child, targetData, ctx){
    if(state == "looping"){
        var date = new Date();
        if(parent.calcRate(targetData) > child.calcRate(targetData)){
            parent = child;
        }
        child = new Drawing(config.triangleNum, ctx, parent);
        var delay = 1;
        if(delay > 0){
            setTimeout(looping, delay, parent, child, targetData, ctx);
        }
        else{
            setTimeout(looping, 0, parent, child, targetData, ctx);
        }
    }
    else if(state == "pause"){
        total.parent = parent;
        total.child = child;
    }
}
