---
article_id: 360026944631
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 089c8f5a4e42dd2008395f587542e1208952037c4b119382ca5ef591a81a5a69
fetched_at: '2026-06-28T22:42:42.264981+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Erro array out of bounds ( 0 of 19
  )  on A381LINOK (MATA381.PRX)
type: support-article
updated_at: '2024-10-08T15:22:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944631-Manufatura-Linha-Protheus-SIGAPCP-Erro-array-out-of-bounds-0-of-19-on-A381LINOK-MATA381-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:05 min****Ocorrência**Na rotina **MATA381 - Ajuste de Empenho**, ao alterar o empenho, ocorre a mensagem **Array out of bounds ( 0 of 19 ) on A381LINOK (MATA381.PRX)**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - A partir da versão 11.80  
  
**Causa**Esta situação ocorre quando algum campo da tabela **SD4 - Empenhos** não está marcado como **Usado** no **SIGACFG - Configurador**.  
  
**Solução**Acesse o **SIGACFG - Configurador** em **Base de Dados > Dicionário > Bases de Dados** e em **Dicionário de Dados** pesquise pela tabela **SD4**. Altere o cadastro desta tabela, e em **Campos**, localize os campos listados abaixo, e verifique se **todos** esses campos estão marcados como **Usado**, conforme exemplifico com o campo **D4\_OPORIG - Op Origem**:  
  
**D4\_COD - Produto**  
**D4\_TRT - Seq. Estrut.**  
**D4\_LOCAL - Armazém**  
**D4\_QUANT - Sal. Empenho**  
**D4\_QTDEORI - Qtd. Empenho**  
**D4\_QTSEGUM - Sld.Emp 2aUM**  
**D4\_LOTECTL - Lote**  
**D4\_NUMLOTE - Sub-Lote**  
**D4\_DTVALID - Data Validad**  
**D4\_POTENCI - Potencia Lot**  
**D4\_DATA - Dt Empenho**  
**D4\_OPORIG - Op Origem**

![usado.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360026274871/usado.jpg)

Caso algum campo não esteja, marque como **Usado** e efetue um novo teste.
