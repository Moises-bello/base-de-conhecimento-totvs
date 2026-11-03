---
article_id: 1500000473721
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 48eda92fb1c0eb6d2809dae5bd2075d9dc9c1ca7b692a4e8cc0897d4a258bfaf
fetched_at: '2026-06-28T22:42:47.068610+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Tela para selecionar o opcional default
  no MATA010 não é apresentada
type: support-article
updated_at: '2021-05-26T19:45:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000473721-Manufatura-Linha-Protheus-SIGAPCP-Tela-para-selecionar-o-opcional-default-no-MATA010-n%C3%A3o-%C3%A9-apresentada
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:55 min**  
**Dúvida**Por que os opcionais do **MP - Matéria Prima** de um **PI - Produto Intermediário** não estão sendo apresentados para seleção de **opcional** *default* no **PA - Produto Acabado** no **MATA010 - Cadastro de Produto**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Quando se possui uma estrutura conforme exemplo abaixo, onde temos um **PA**, **PI** e **MPs**, sendo que os **MPs** possuem **opcionais**. Para que no **MATA010** seja possível selecionar os **Opcionais** *default* no produto **PA** é necessário que o parâmetro **MV\_GERAOPI - Gera OP do produto Intermediário a Partir de OP do Produto Principal** esteja ativo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101626593/mceclip0.png)

**Saiba mais**Para saber como selecionar o **opcional** *default* no **MAT010** acesse o artigo: [Manufatura - Linha Protheus - SIGAPCP - Como informar o Opcional Default no cadastro de Produtos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028768452-MP-SIGAPCP-Como-informar-o-Opcional-Default-no-cadastro-de-Produtos)
