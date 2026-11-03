---
article_id: 360021478452
category: Inspeção de Entradas (SIGAQIE)
content_hash: 7601daa9d5290281dd90260cd7a158efccbbb945a8901a6be80f36f025db38d3
fetched_at: '2026-06-28T22:42:26.846143+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - A situação do Fornecedor x Produto
  não foi informada
type: support-article
updated_at: '2021-06-17T20:41:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021478452-Manufatura-Linha-Protheus-SIGAQIE-A-situa%C3%A7%C3%A3o-do-Fornecedor-x-Produto-n%C3%A3o-foi-informada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min  
  
Ocorrência**Ao realizar a importação de entrada de material na inspeção por meio da rotina de **QIEA183 -  Importação** ou ao incluir um documento de entrada na rotina **MATA103 - Documento de Entrada**, é apresentada a mensagem de inconsistência **A situação do Fornecedor x Produto não foi informada**.   
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**  
Esta mensagem ocorre quando o campo **Situação - A5\_SITU** na rotina de **MATA061 - Produto x Fornecedor** não foi preenchido para o fornecedor e produto em questão.  
  
**Solução**Para que a mensagem não seja mais exibida é necessário:

1. Acessar a rotina **MATA061** pelo módulo **21 - Inspeção de Entradas**, para que o campo **Situação** esteja visível;
2. Preencher este campo com o conteúdo desejado;
3. Realizar o processamento novamente seja por meio da rotina **MATA103** ou **QIEA183**.
