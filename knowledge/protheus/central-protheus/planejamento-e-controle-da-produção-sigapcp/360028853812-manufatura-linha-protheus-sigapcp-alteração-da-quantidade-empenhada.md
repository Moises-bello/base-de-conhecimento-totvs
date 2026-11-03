---
article_id: 360028853812
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 2c086155783297eae3bd2b00541408f068ded7c6bf229c59aa9a0d9993dee515
fetched_at: '2026-06-28T22:42:40.768275+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Alteração da quantidade empenhada
type: support-article
updated_at: '2021-08-13T11:18:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028853812-Manufatura-Linha-Protheus-SIGAPCP-Altera%C3%A7%C3%A3o-da-quantidade-empenhada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min****Dúvida**Como alterar a quantidade empenhada para uma **OP - Ordem de Produção**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**A alteração da quantidade empenhada deve ser realizada através do **MATA380 - Ajuste de Empenhos Modelo I** ou **MATA381 - Ajuste de Empenhos Modelo II**, para isso siga os passos abaixo:

1. Altere o conteúdo do campo **D4\_QTDEORI - Qtd. Empenho** para a quantidade total que deve ser consumida nessa produção;
2. Altere o conteúdo do campo **D4\_QUANT - Sal. Empenho** para a quantidade informada no passo 1 subtraindo desse valor o que já foi requisitado para a **OP**.
