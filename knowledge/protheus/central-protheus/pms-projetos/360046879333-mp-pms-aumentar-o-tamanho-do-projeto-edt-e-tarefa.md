---
article_id: 360046879333
category: PMS - Projetos
content_hash: 905af83fa72c5a7a03c0b3990edb7db6bdf51af2241009704c549f3408990962
fetched_at: '2026-06-28T22:37:14.990133+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: 'MP - PMS - AUMENTAR O TAMANHO DO  PROJETO, EDT E TAREFA. '
type: support-article
updated_at: '2021-04-29T21:12:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046879333-MP-PMS-AUMENTAR-O-TAMANHO-DO-PROJETO-EDT-E-TAREFA
---

**Dúvida**

Como alterar os campos da Tarefa, EDT e projeto?  
   
 **Ambiente**

Protheus – A partir da release 11.80.  
  
**Solução**

A alteração da **Tarefa e EDT**, devem ser realizadas através do grupo de campos (**EDT/TAREFA**).

Para acessar o grupo de campos entre no Configurador - Dicionário - Base de dados - dicionário, logo a abaixo terá a opção Grupo de campos.

Procure a opção edt/tarefa e altere para quantidade desejada, o máximo permitido é tamanho 50.

Para alteração do projeto utilize o grupo de campo Projeto, o tamanho máximo são de 30 caracteres.

Obs: Na integração com o Top da RM é importante  alterar o grupo de campos do Protheus, deixando o Projeto para 30 e as tarefas e EDT's com 50, ficando com a mesma quantidade do produto RM.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067033973/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067033373/mceclip0.png)
