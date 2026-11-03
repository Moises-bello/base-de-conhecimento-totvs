---
content_hash: 2aba5b3fde6718953432d72719e6f286dbc09bd3df3b8ffddaf9a7379b009687
fetched_at: '2026-06-29T00:09:14.984350+00:00'
page_id: '421385326'
product: rm
source: tdn-rm
title: Copiar Folha Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Copiar+Folha+Tarefa
version: 6
---

**Copiar Folha Tarefa**

---

O processo "Copiar Folha Tarefa" será permitido para folhas tarefa que possuam status Cancelada ou Encerrada. Na cópia, os itens da Folha Tarefa serão copiados e a periodicidade da nova Folha Tarefa pode ser informada.  
As Folhas Tarefas geradas a partir da Cópia de Folha Tarefa terão o status "Em processamento".

* Para Folhas Tarefas de periodicidade Semanal, Quinzenal e Mensal, os campos "Periodicidade" e "Tipo de Apontamento" serão exibidos com os valores que foram definidos na folha origem da cópia; - Os campos "Data Início" e "Descrição" estarão disponíveis para preenchimento na criação da nova folha tarefa criada através da cópia; - A opção "Copiar Alocação da Equipe" estará visível somente quando a Folha Tarefa origem possuir o status Encerrada.+
* Para Folhas Tarefas de periodicidade Personalizada o campo "Tipo de Apontamento" será exibido com o valor que foi definido na folha origem da cópia; - Os campos "Data Início", "Data fim" e "Descrição" estarão disponíveis para preenchimento na criação da nova folha tarefa criada através da cópia; - A opção "Copiar Alocação da Equipe" estará visível somente quando a Folha Tarefa origem possuir o status Encerrada.+
* Caso a folha tarefa origem esteja com o status encerrada, serão copiados os itens associados a ela bem como as alocações de equipe da mesma, ambos respeitando as validações e regras de saldo na alocação de equipe.
* Caso a folha tarefa origem esteja com o status cancelada, serão copiados apenas os itens associados à Folha Tarefa origem, respeitando as validações de saldo na associação de itens à folha.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Folha Tarefa  
Itens da folha tarefa Alocação de mão de obra
