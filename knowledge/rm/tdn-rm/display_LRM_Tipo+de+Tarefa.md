---
content_hash: 21d13d3134fce40e63315220b47368c6a3b284c513221e24477da23e83fc4726
fetched_at: '2026-06-29T00:10:46.844775+00:00'
page_id: '556379441'
product: rm
source: tdn-rm
title: Tipo de Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipo+de+Tarefa
version: 14
---

---

Tipo de Tarefa será utilizado no momento na execução da  [Simulação 3D - Linha do Tempo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=556388762) para identificar os Objetos 3D em atraso (vermelho) e adiantados (amarelo) e em execução (verde).

Três tipos de Tarefas são criadas por padrão do sistema em cada Projeto, são elas:

* **001 - Construção:**
  + Aparência inicial Verde (Em execução);
  + Aparência final Opaco (Tarefa Finalizada);
  + Aparência adiantada Amarelo (Tarefa iniciada antes do Planejado);
  + Aparência atrasada Vermelho (Tarefa iniciada após o Planejado);
* **002 - Demolição:**
  + Aparência simulação inicial Opaco (Tarefa não iniciada);
  + Aparência inicial Vermelho (Em execução);
  + Aparência final Invisível (Tarefa Finalizada);
* **003 - Temporária:**  
  + Aparência inicial Amarelo (Em execução);
  + Aparência final Invisível (Tarefa Finalizada);

Os Tipos de Tarefas padrão do sistema são editáveis, a passíveis a exclusão caso não tenha nenhum vínculo com nenhuma Tarefa;

Ao incluir um novo Tipo de Tarefa, deve-se informar:

* **Código do Tipo da Tarefa:** Código que o novo Tipo de Tarefa irá assumir**;**
* **Descrição do Tipo de Tarefa:** Descrição do novo Tipo de Tarefa;
* **Aparência do Objeto 3D** - Cores e Transparência cadastrada em [Aparência do Objeto 3D](https://tdn.totvs.com.br/pages/viewpage.action?pageId=556379447);

[Voltar](https://tdn.totvs.com.br/display/LRM/BIM+-+TOP)
