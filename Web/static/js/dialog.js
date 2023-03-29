/**
 * 弹出消息提示框
 * @param {Object} title 标题
 * @param {Object} message 消息
 */
function alert(title, message) {
	//创建DOM元素对象
	var dialog = document.createElement("section");
	//设置属性
	dialog.setAttribute("id", "dialog");
	//添加给body DOM对象
	document.body.appendChild(dialog);
	//dialog插入HTML元素
	dialog.innerHTML = '<section>'
			+	'<i>X</i>'
			+	'<p class="title">' + (title ? title : '提示') + '</p>'
			+	'<p class="message">' + message + '</p>'
			+	'<p class="btn-groups">'
			+	'	<input type="button" value="确定" class="btn btn-primary" />'
			+	'</p>'
			+'</section>';
	//绑定事件
	dialog.querySelector("section > i").addEventListener("click", function() {
		closeDialog(dialog);
	});
	dialog.querySelector("section > p > .btn-primary").addEventListener("click", function() {
		closeDialog(dialog);
	});
}

/**
 * 弹出确认框
 * @param {Object} title 标题
 * @param {Object} message 消息
 * @param {Object} callback 回调函数
 */
function confirm(title, message, callback) {
	//创建DOM元素对象
	var dialog = document.createElement("section");
	//设置属性
	dialog.setAttribute("id", "dialog");
	//添加给body DOM对象
	document.body.appendChild(dialog);
	//dialog插入HTML元素
	dialog.innerHTML = '<section>'
			+	'<i>X</i>'
			+	'<p class="title">' + (title ? title : '提示') + '</p>'
			+	'<p class="message">' + message + '</p>'
			+	'<p class="btn-groups">'
			+	'	<input type="button" value="确定" class="btn btn-primary" />'
			+	'	<input type="button" value="取消" class="btn btn-default" />'
			+	'</p>'
			+'</section>';
	//绑定事件
	dialog.querySelector("section > i").addEventListener("click", function() {
		closeDialog(dialog);
	});
	dialog.querySelector("section > p > .btn-default").addEventListener("click", function() {
		closeDialog(dialog);
	});
	dialog.querySelector("section > p > .btn-primary").addEventListener("click", function() {
		callback.call();
		closeDialog(dialog);
	});
}

/**
 * 关闭对话框
 * @param {Object} dialog 对话框对象
 */
function closeDialog(dialog) {
	document.body.removeChild(dialog);
}