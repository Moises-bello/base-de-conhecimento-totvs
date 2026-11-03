---
content_hash: d189d77b56c3d44f53b694d39182b42960bed64010ad257b01277639a85586d6
fetched_at: '2026-06-29T00:08:49.542678+00:00'
page_id: '330843097'
product: rm
source: tdn-rm
title: Macros JS / CSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330843097
version: 401
---

]]>

# TOTVS Accordion

---

Para se utilizar o TOTVS Accordion, alguns passos devem ser utilizados:

1 - Adicione os Scripts

xml1scripttrue
]]>

2 - Adicione os CSSs

xml1csstrue]]>
Totvs = {
Accordion: function(optCollapsiblePanel){
var oCollapsiblePanel = function(optCollapsiblePanel){
this.Id = "CollapsiblePanel1";
this.ElementToAttach = window.body;
this.TitleMark = "titlemark";
this.Title = "";
this.TitleImageUrl = "";
this.Groups = [];
this.LoadComponents = function(optCollapsiblePanel){
if(optCollapsiblePanel != null && optCollapsiblePanel != undefined && !$.isEmptyObject(optCollapsiblePanel)){
if(optCollapsiblePanel.Id != null && optCollapsiblePanel.Id != undefined && optCollapsiblePanel.Id != "")
this.Id = optCollapsiblePanel.Id;
if(optCollapsiblePanel.ElementToAttach != null && optCollapsiblePanel.ElementToAttach != undefined)
this.ElementToAttach = optCollapsiblePanel.ElementToAttach;
if(optCollapsiblePanel.Title != null && optCollapsiblePanel.Title != undefined && optCollapsiblePanel.Title != "")
this.Title = optCollapsiblePanel.Title;
if(optCollapsiblePanel.TitleMark != null && optCollapsiblePanel.TitleMark != undefined && optCollapsiblePanel.TitleMark != "")
this.TitleMark = optCollapsiblePanel.TitleMark.replace("<").replace(">");
if(optCollapsiblePanel.TitleImageUrl != null && optCollapsiblePanel.TitleImageUrl != undefined && optCollapsiblePanel.TitleImageUrl != "")
this.TitleImageUrl = optCollapsiblePanel.TitleImageUrl;
if(optCollapsiblePanel.Groups != null && optCollapsiblePanel.Groups != undefined)
this.Groups = optCollapsiblePanel.Groups ;
}
var ElementCollapsiblePanel = document.createElement('div');
ElementCollapsiblePanel.id = this.Id + "\_OuterDiv";
ElementCollapsiblePanel.name = this.Id + "\_OuterDiv";
ElementCollapsiblePanel.className = "outerDiv";
var ElementCollapsiblePanelWrapper = document.createElement('div');
ElementCollapsiblePanelWrapper.id = this.Id + "\_OuterDivWrapper";
ElementCollapsiblePanelWrapper.name = this.Id + "\_OuterDivWrapper";
ElementCollapsiblePanelWrapper.className = "outerDivWrapper";
if(this.Title != null && this.Title != undefined && this.Title != ""){
if(this.TitleImageUrl != null && this.TitleImageUrl != undefined && this.TitleImageUrl != ""){
var ElementCollapsiblePanelWrapperTitleSpan = document.createElement('span');
ElementCollapsiblePanelWrapperTitleSpan.id = this.Id + "\_OuterDivWrapperTitleSpan";
ElementCollapsiblePanelWrapperTitleSpan.name = this.Id + "\_OuterDivWrapperTitleSpan";
ElementCollapsiblePanelWrapperTitleSpan.className = "outerDivWrapperTitleSpan";
var ElementCollapsiblePanelWrapperTitleSpanImg = document.createElement('img');
ElementCollapsiblePanelWrapperTitleSpanImg.id = this.Id + "\_OuterDivWrapperTitleSpanImg";
ElementCollapsiblePanelWrapperTitleSpanImg.name = this.Id + "\_OuterDivWrapperTitleSpanImg";
ElementCollapsiblePanelWrapperTitleSpanImg.className = "outerDivWrapperTitleSpanImg";
ElementCollapsiblePanelWrapperTitleSpanImg.src = this.TitleImageUrl;
ElementCollapsiblePanelWrapperTitleSpan.appendChild(ElementCollapsiblePanelWrapperTitleSpanImg);
var ElementCollapsiblePanelWrapperTitleSpanText = document.createElement('span');
ElementCollapsiblePanelWrapperTitleSpanText .id = this.Id + "\_OuterDivWrapperTitleSpanText";
ElementCollapsiblePanelWrapperTitleSpanText .name = this.Id + "\_OuterDivWrapperTitleSpanText";
ElementCollapsiblePanelWrapperTitleSpanText .className = "outerDivWrapperTitleSpanText";
ElementCollapsiblePanelWrapperTitleSpanText.innerHTML = this.Title;
ElementCollapsiblePanelWrapper.appendChild(ElementCollapsiblePanelWrapperTitleSpan);
ElementCollapsiblePanelWrapper.appendChild(ElementCollapsiblePanelWrapperTitleSpanText);
}
else
ElementCollapsiblePanelWrapper.innerHTML = this.Title;
}
else{
if($(window.document).find(this.TitleMark).length > 0)
ElementCollapsiblePanelWrapper.innerHTML = $(window.document).find(this.TitleMark)[0].innerHTML;
}
ElementCollapsiblePanel.appendChild(ElementCollapsiblePanelWrapper);
for(var i = 0; i < this.Groups.length; i++){
ElementCollapsiblePanel.appendChild(this.Groups[i]);
if(this.Groups.length > 1 && i < this.Groups.length - 1){
var \_paddingDiv = document.createElement("div");
\_paddingDiv.className = "paddingDiv";
ElementCollapsiblePanel.appendChild(\_paddingDiv);
}
}
if(typeof this.ElementToAttach === "string")
this.ElementToAttach = document.getElementById(this.ElementToAttach);
this.ElementToAttach.appendChild(ElementCollapsiblePanel);
return this;
}
return this.LoadComponents(optCollapsiblePanel);
}
return new oCollapsiblePanel(optCollapsiblePanel);
},
CollapsiblePanelGroup: function(optCollapsiblePanelGroup){
var oCollapsiblePanelGroup = function(optCollapsiblePanelGroup){
this.Id = "CollapsiblePanelGroup1";
this.Parent = null;
this.GroupTitleMark = "grouptitlemark{0}"
this.GroupTitle = "";
this.GrouptTitleImageUrl = "";
this.LoadComponents = function(optCollapsiblePanelGroup){
if(optCollapsiblePanelGroup!= null && optCollapsiblePanelGroup!= undefined && !$.isEmptyObject(optCollapsiblePanelGroup)){
if(optCollapsiblePanelGroup.GroupTitle != null && optCollapsiblePanelGroup.GroupTitle != undefined && optCollapsiblePanelGroup.GroupTitle != "")
this.GroupTitle = optCollapsiblePanelGroup.GroupTitle;
if(optCollapsiblePanelGroup.GroupTitleImageUrl!= null && optCollapsiblePanelGroup.GroupTitleImageUrl != undefined && optCollapsiblePanelGroup.GroupTitleImageUrl!= "")
this.GroupTitleImageUrl = optCollapsiblePanelGroup.GroupTitleImageUrl;
if(optCollapsiblePanelGroup.GroupTitleMark != null && optCollapsiblePanelGroup.GroupTitleMark != undefined && optCollapsiblePanelGroup.GroupTitleMark != "")
this.GroupTitleMark = optCollapsiblePanelGroup.GroupTitleMark.replace("<").replace(">");
}
var ElementCollapsiblePanelGroup = document.createElement('div');
ElementCollapsiblePanelGroup.id = this.Id + "\_GroupOuterDiv";
ElementCollapsiblePanelGroup.name = this.Id + "\_GroupOuterDiv";
ElementCollapsiblePanelGroup.className = "groupOuterDiv";
var ElementCollapsiblePanelGroupWrapper = document.createElement('div');
ElementCollapsiblePanelGroupWrapper.id = this.Id + "\_GroupOuterDivWrapper";
ElementCollapsiblePanelGroupWrapper.name = this.Id + "\_GroupOuterDivWrapper";
ElementCollapsiblePanelGroupWrapper.className = "groupOuterDivWrapper";
if(this.GroupTitle != null && this.GroupTitle != undefined && this.GroupTitle != ""){
if(this.GroupTitleImageUrl != null && this.GroupTitleImageUrl != undefined && this.GroupTitleImageUrl != ""){
var ElementCollapsiblePanelGroupWrapperTitleSpan = document.createElement('span');
ElementCollapsiblePanelGroupWrapperTitleSpan.id = this.Id + "\_GroupOuterDivWrapperTitleSpan";
ElementCollapsiblePanelGroupWrapperTitleSpan.name = this.Id + "\_GroupOuterDivWrapperTitleSpan";
ElementCollapsiblePanelGroupWrapperTitleSpan.className = "groupOuterDivWrapperTitleSpan";
var ElementCollapsiblePanelGroupWrapperTitleSpanImg = document.createElement('img');
ElementCollapsiblePanelGroupWrapperTitleSpanImg.id = this.Id + "\_GroupOuterDivWrapperTitleSpanImg";
ElementCollapsiblePanelGroupWrapperTitleSpanImg.name = this.Id + "\_GroupOuterDivWrapperTitleSpanImg";
ElementCollapsiblePanelGroupWrapperTitleSpanImg.className = "outerDivWrapperTitleSpanImg";
ElementCollapsiblePanelGroupWrapperTitleSpanImg.src = this.GroupTitleImageUrl;
ElementCollapsiblePanelGroupWrapperTitleSpan.appendChild(ElementCollapsiblePanelGroupWrapperTitleSpanImg);
var ElementCollapsiblePanelGroupWrapperTitleSpanText = document.createElement('span');
ElementCollapsiblePanelGroupWrapperTitleSpanText .id = this.Id + "\_GroupOuterDivWrapperTitleSpanText";
ElementCollapsiblePanelGroupWrapperTitleSpanText .name = this.Id + "\_GroupOuterDivWrapperTitleSpanText";
ElementCollapsiblePanelGroupWrapperTitleSpanText .className = "groupOuterDivWrapperTitleSpanText";
ElementCollapsiblePanelGroupWrapperTitleSpanText.innerHTML = this.GroupTitle;
ElementCollapsiblePanelGroupWrapper.appendChild(ElementCollapsiblePanelGroupWrapperTitleSpan);
ElementCollapsiblePanelGroupWrapper.appendChild(ElementCollapsiblePanelGroupWrapperTitleSpanText);
}
else
ElementCollapsiblePanelGroupWrapper.innerHTML = this.GroupTitle;
}
else{
if($(window.document).find(this.GroupTitleMark).length > 0)
ElementCollapsiblePanelGroupWrapper.innerHTML = $(window.document).find(this.GroupTitleMark)[0].innerHTML;
}
ElementCollapsiblePanelGroup.appendChild(ElementCollapsiblePanelGroupWrapper);
return ElementCollapsiblePanelGroup;
}
return this.LoadComponents(optCollapsiblePanelGroup);
}
return oCollapsiblePanelGroup(optCollapsiblePanelGroup);
},
CollapsiblePanelGroupItem: function(optCollapsiblePanelGroupItem){
var oCollapsiblePanelGroupItem = function(optCollapsiblePanelGroupItem) {
this.LoadComponents = function(optCollapsiblePanelGroupItem){
return null;
}
return this.LoadComponents(optCollapsiblePanelGroupItem);
}
return oCollapsiblePanelGroupItem(optCollapsiblePanelGroupItem);
}
}
]]>

3 - Adicione o Script das Chamadas ao TOTVS\_Accordion

js1Totvs.CollapsiblePanel Chamadatruetrue
var \_groups = [];
optCollapsiblePanelGroup1 = {
GroupTitle: "Grupo de Teste1",
GroupTitleImageUrl: "/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2"
}
var \_group1 = Totvs.CollapsiblePanelGroup(optCollapsiblePanelGroup1);
\_groups.push(\_group1);
optCollapsiblePanelGroup2 = {
GroupTitle: "Grupo de Teste2",
GroupTitleImageUrl: "/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2"
}
var \_group2 = Totvs.CollapsiblePanelGroup(optCollapsiblePanelGroup2);
\_groups.push(\_group2);
optCollapsiblePanel1 = {
ElementToAttach: "divContent",
Groups: \_groups,
TitleImageUrl: "/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2",
Title: "Título de Teste"
}
var \_collapsiblePanel1 = Totvs.Accordion(optCollapsiblePanel1);]]>
