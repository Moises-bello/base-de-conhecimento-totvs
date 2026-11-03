---
article_id: 28107154143255
category: Rental by ItUp Business
content_hash: d75a1416c6787cb7c3e155b539d18b2b04177c6b242b118970f7f0526a7f800c
fetched_at: '2026-06-28T22:36:20.622528+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Erro na descrição do produto
  'C6_DESCRI' na rotina de Faturamento Automático (LOCA021), durante a geração do
  processo de aglutinação.
type: support-article
updated_at: '2026-04-09T12:48:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28107154143255-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Erro-na-descri%C3%A7%C3%A3o-do-produto-C6-DESCRI-na-rotina-de-Faturamento-Autom%C3%A1tico-LOCA021-durante-a-gera%C3%A7%C3%A3o-do-processo-de-aglutina%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28107145056023) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Erro na descrição do produto 'C6\_DESCRI' na rotina de Faturamento Automático (LOCA021), durante a geração do processo de aglutinação.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - P12.1.2310  
  
**Causa**  
Quando tentamos executar o processo na rotina de **Faturamento Automático** (**LOCA021**) para **PROJETOS** em que o campo **FP0\_AGLUNF** (**Aglutina NF**) está configurado como "**1-SIM"**, o sistema apresenta uma tela de erro, informando que o campo da descrição do produto (**C6\_DESCRI**) está "**INVALIDO"**.

```
AJUDA:TEXTO 
Descriçao deve ser informada.

Tabela SC5 27/11/2024 11:16:36
Tipo Pedido -  C5_TIPO    := N
Cliente -      C5_CLIENTE := 000001
Loja -         C5_LOJACLI := 01
Cond. Pagto -  C5_CONDPAG := 001
Vendedor 1 -   C5_VEND1   := 000001
Peso Liquido - C5_PESOL   := 0
Peso Bruto -   C5_PBRUTO  := 0
Seguro -       C5_SEGURO  := 0
Natureza -     C5_NATUREZ := RENTAL 2
Moeda -        C5_MOEDA   := 1
--------------------------------------------------------------------------------
Tabela SC6 27/11/2024 11:16:36
Erro no Item 1
--------------------------------------------------------------------------------
Filial - C6_FILIAL := 01
Item -         C6_ITEM    := 01
Produto -      C6_PRODUTO := 
Descricao -    C6_DESCRI  := < -- Invalido
Quantidade -   C6_QTDVEN  := 1
Prc Unitario - C6_PRCVEN  := 31155.95
Prc Lista -    C6_PRUNIT  := 31155.95
Vlr.Total -    C6_VALOR   := 31155.95
Qtd.Liberada - C6_QTDLIB  := 1
Tipo Saida -   C6_TES     := 502
C.Custo -      C6_CC      := 
--------------------------------------------------------------------------------
```

**Solução**

**Para solucionar esta ocorrência, temos duas sugestões:**

1. **Utilizar o parâmetro MV\_LOCX063 (Produto utilizado no PV de medição):** Defina um produto que será sempre utilizado e automaticamente levado para o pedido de venda.
2. **Na inclusão do Projeto, configurar o campo FP0\_AGLUNF (Aglutina NF) como "1 - SIM":** Ao fazer isso, o campo **FP0\_PRODL** (**Prod. Locação**) será aberto para edição, permitindo que você informe o produto a ser aglutinado no pedido de venda.

**Observação:** Caso já exista um projeto criado, basta realizar a alteração, informando o produto no campo **FP0\_PRODL** (**Prod. Locação**), e em seguida refazer o processo de Faturamento Automático.
