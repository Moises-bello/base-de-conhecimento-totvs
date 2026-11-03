---
article_id: 360024952953
category: Inspeção de Entradas (SIGAQIE)
content_hash: 447b6e03de04b16a3df0426c79ed7c7dddd07c9dff442981618f6f635f92e46a
fetched_at: '2026-06-28T22:42:26.974615+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Fórmula de cálculo do IPO - Índice
  de Pontualidade
type: support-article
updated_at: '2024-07-02T13:25:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024952953-Manufatura-Linha-Protheus-SIGAQIE-F%C3%B3rmula-de-c%C3%A1lculo-do-IPO-%C3%8Dndice-de-Pontualidade
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24591134525079) Tempo aproximado para leitura:**00:01:30 min**  
**Dúvida**Qual a fórmula de cálculo do **IPO - Índice de Pontualidade?**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**O **IES** - **Índice de Entrega e Serviços** reflete o **IPO - Índice de Pontualidade do Fornecedor**, calculado automaticamente pelo Sistema a partir das movimentações registradas.  
  
A fórmula de cálculo do **IPO** é:

![IPO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038218054)

Onde:**Ni** = Quantidade entregue em atraso  
**Di** = Número de dias em atraso  
**Nt** = Quantidade total entregue  
**MV\_QDIAIPO** – **Número máximo de dias em atraso para o cálculo do** **IPO**. **Exemplo**Ni = 1000  
Di = 4  
Nt= 2000  
**MV\_QDIAIPO** = 180  
  
**IPO** = (1-(1000\*4) / (180\*2000))\*100  
**IPO** =  98,89   
  
Se o **Número de dias em atraso de cada entrega** - **Di** for maior que o especificado no parâmetro **MV\_QDIAIPO**, este é assumido.  
  
**Observação**

O campo **QEK\_DIASAT - Dias em Atraso** é resultado da **subtração de D1\_DTDIGIT - C7\_DATPR**. O **cálculo da quantidade de dias em atraso é feito pelo módulo de Compras** e gravado no campo QEK\_DIASAT no momento da integração. Com a utilização do parâmetro **MV\_DATAHOM - Na homologação do aviso de recebimento para produtos com TES e que serão classificados utiliza a database (1) ou data final de entrega (2)** com conteúdo igual a 2, o campo **D1\_DTDIGIT será gravado com o valor do campo F1\_RECBMTO**.   
Para dias em atraso:   
- **Se o número de dias em atraso for menor** que o definido no parâmetro MV\_QDIAIPO, o valor acumulado será o valor absoluto do produto dos campos Tam. Lote - QEK\_TAMLOT pelo Dias Atraso - QEK\_DIASAT: **QEK\_TAMLOT \* QEK\_DIASAT**;   
- **Se o número de dias em atraso for maior** que o definido no parâmetro MV\_QDIAIPO o produto do campo Tam. Lote - QEK\_TAMLOT pelo conteúdo do parâmetro MV\_QDIAIPO: **QEK\_TAMLOT \* MV\_QDIAIPO**.
