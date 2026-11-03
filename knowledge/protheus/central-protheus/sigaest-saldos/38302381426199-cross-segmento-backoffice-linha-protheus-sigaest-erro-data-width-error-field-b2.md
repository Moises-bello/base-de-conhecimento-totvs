---
article_id: 38302381426199
category: SIGAEST - SALDOS
content_hash: 58e4ce2bf38dac75ad8c41af8ba3498d18fb0270fe368e517322a2d1b12870be
fetched_at: '2026-06-28T22:39:14.962611+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: 'Cross Segmento – Backoffice (Linha Protheus) – SIGAEST – Erro Data width error
  Field: B2_QTSEGUM'
type: support-article
updated_at: '2026-02-10T18:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38302381426199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-Data-width-error-Field-B2-QTSEGUM
---

O erro "Data width error Field: B2\_QTSEGUM Value: 2891650.000000" no TOTVS Protheus ocorre devido a valor incorreto na Segunda Unidade de Medida, geralmente por erro de digitação, lançamento manual ou customização. Recomenda-se identificar o produto, localizar e estornar ou ajustar a movimentação para corrigir o saldo e evitar recorrência.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38302420751767) Tempo aproximado para leitura: 00**:**02:00 **min**  
  
**Dúvida**  
Ao realizar o **apontamento de produção ou qualquer outra rotina**, em alguns itens é apresentada a seguinte mensagem no *error.log*:

**"Data width error Field: B2\_QTSEGUM Value: 2891650.000000"**

O erro impede a continuidade do processamento da rotina.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**

O problema ocorre devido ao produto informado na variavel B2\_COD do errorlog possuir **valor incorreto na Segunda Unidade de Medida (B2\_QTSEGUM)** em alguma movimentação.

Esse comportamento geralmente é ocasionado por:

* erro de digitação na movimentação;
* lançamento manual incorreto;
* ou possível customização que gravou valor indevido.

No próprio *error.log* é possível visualizar o trecho que destaca o produto com inconsistência, bem como os valores gravados na tabela **SB2**.

**Solução**

Para correção, deve-se:

1. Identificar no *error.log* o produto apresentado na variável **B2\_COD**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38302420756247)

  2. Localizar qual movimentação originou o valor incorreto;

  3. Caso possível, **estornar a movimentação**;

 4. Se o estorno não for viável, **realizar ajuste de quantidade** para adequar o saldo do campo e evitar a recorrência do erro.

Recomenda-se realizar filtro nas tabelas:

* **SD1**
* **SD2**
* **SD3**

Verificando principalmente os campos:

* **D1\_QTSEGUM**
* **D2\_QTSEGUM**
* **D3\_QTSEGUM**

Buscar por movimentações que apresentem **quantidades muito elevadas ou fora do padrão**, pois normalmente indicam erro de digitação do usuário ou alguma customização.

**Veja também no link abaixo instruções sobre esse error.log:**  
[***MP - SIGAEST - Data Width error - Field: B2\_VATU1 / B2\_VATU2 / B2\_VATU3 / B2\_VATU4 / B2\_VATU5. Como resolver?***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003491921-MP-SIGAEST-Data-Width-error-Field-B2-VATU1-B2-VATU2-B2-VATU3-B2-VATU4-B2-VATU5-Como-resolver-?source=search)

**Saiba Mais:**  
[*Clique aqui e veja mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)
