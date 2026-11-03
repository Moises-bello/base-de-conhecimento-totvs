---
article_id: 24960787161367
category: SIGAACD - Automação e Coleta de Dados
content_hash: 60d76c4c6d6dd1c23ab7fa248446435620b038065b5ac25d4c4d0c84eb0bf6f9
fetched_at: '2026-06-28T22:39:12.640362+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como realizar o estorno
  da etiqueta de endereçamento (advindo de NF de Entrada) via CB0?
type: support-article
updated_at: '2024-07-17T13:27:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24960787161367-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-realizar-o-estorno-da-etiqueta-de-endere%C3%A7amento-advindo-de-NF-de-Entrada-via-CB0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24960818424599) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como realizar o estorno da etiqueta de endereçamento advindo de Nota Fiscal via tabela CB0?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**Neste artigo abordaremos como realizar corretamente o processo de estorno de etiqueta de endereçamento.

**O que é necessário para que seja feito o estorno?**

1. Estar com os parâmetros **MV\_ACDCB0 ='01'** e **MV\_CBPE016 = .T.** além do parâmetro **MV\_LOCALIZ = S**.
2. O ambiente precisa estar com os [RDMAKEs](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016774791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-RDMakes-do-SIGAACD) da impressora devidamente compilados.
3. Para estornar um endereço nesta modalidade, o mesmo deve ter sido criado através de uma Nota de Entrada ao (que vai gerar etiqueta na tabela CB0).
4. O endereçamento deve ser feito via ACDV060 - Via Coletor de Dados ou Emulador Telnet com linguagem VT100

**Como realizar o Estorno da etiqueta do Endereçamento?**

1 - Para realizar o estorno é necessário acessar a rotina (**MATA265**), clicar no botão "Outras Ações"-> "Estornar", marca um 'S' no item que deseja estornar e "Confirma".  Após isso, será apresentada a tela abaixo para informar a etiqueta que deseja estornar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24960818427543)

2 - Selecionando a etiqueta que deseja estornar é realizado o estorno corretamente na tabela SDB.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24960787138967)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24960787139735)

**Saiba Mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - Como efetuar o Controle e Endereçar Produtos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014866531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA265-Como-efetuar-o-Controle-e-Endere%C3%A7ar-Produtos-no-Protheus)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - Como efetuar o Controle e Endereçar Produtos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)*  
*[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
