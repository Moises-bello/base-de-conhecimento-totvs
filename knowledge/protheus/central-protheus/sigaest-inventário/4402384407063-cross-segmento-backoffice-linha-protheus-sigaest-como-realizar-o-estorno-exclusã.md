---
article_id: 4402384407063
category: SIGAEST - INVENTÁRIO
content_hash: f7435c19454ee30d2c92f5fcdeb326f315f087640f583b9e892fe1b024011494
fetched_at: '2026-06-28T22:38:50.322823+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Como realizar o estorno
  (exclusão) de movimento de Inventário?
type: support-article
updated_at: '2026-03-27T18:38:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402384407063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-o-estorno-exclus%C3%A3o-de-movimento-de-Invent%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29522847566359) Tempo aproximado para leitura: **03:00:00 min**

**Dúvida**Como posso excluir/estornar um processo de Acerto de Inventário gerado erroneamente?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Caso esteja em um cenário onde foi processada à rotina MATA340 - Acerto de Inventário - e determinado produto gerou uma movimentação do tipo **INVENT** com quantidade incorreta, o único mecanismo de estornar seria pelas rotinas de Movimentos Internos Simples/Múltiplo (MATA240 ou MATA241). Vamos mostrar na prática um exemplo onde nosso produto de código **PA19**, onde tinha estoque de 60 porém fizemos a Digitação e Acerto de Inventário de quantidade 63 (por erro de digitação), então vamos estornar o movimento DE0 gerado de quantidade 3 (63-60):

![estorno_inv_pa19.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402391855511)

Com isso, o saldo do produto volta ao status anterior, que era e voltou a ser: 60.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402391899927)

**OBS:** Para realizar o estorno por item, é necessário alterar o parâmetro da rotina apertando a tecla F12 para selecionar a opção "Por item":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16808287465367)

***Importante*:** Após o estorno do Inventário, caso precisar refazer o inventário, ***é necessário que inclua novas digitações***. No padrão o campo **Status (B7\_STATUS) *não é alterado* com o estorno do inventário**, obrigando a inlusão de uma nova digitação do Inventário.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17465007282327)**

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)*

[*SIGAEST - MILE importação de arquivo da tabela SB7 (Digitação do inventário)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10573324218007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SB7-Digita%C3%A7%C3%A3o-do-invent%C3%A1rio-)

*[Clique aqui e veja mais artigos sobre Inventário no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)*
