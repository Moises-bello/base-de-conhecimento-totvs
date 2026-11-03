---
article_id: 34555028714007
category: Financeiro - Movimentos Bancários
content_hash: f0980a369028b3ea9a8e83d5e4508d5b28efed516880864bb4bde54ff7f7ec41
fetched_at: '2026-06-28T22:37:31.844978+00:00'
product: protheus
section_id: 35057601824535
source: central-protheus
title: Cross Segmentos - TOTVS Linha Backoffice Protheus - FINA100 - Transferências
  entre contas em moedas diferentes
type: support-article
updated_at: '2026-03-04T17:17:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34555028714007-Cross-Segmentos-TOTVS-Linha-Backoffice-Protheus-FINA100-Transfer%C3%AAncias-entre-contas-em-moedas-diferentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34555006252183) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
É possível realizar a transferência entre contas de moedas diferentes?  
  
**Exemplo:**  
De: Banco Nacional (Saída)  
Para: Banco Internacional (Entrada)   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Não é possível realizar transferência de uma conta em banco nacional (origem) para uma conta em banco internacional (destino), uma vez que o processo somente é permitido quando ambas as instituições operam com a mesma moeda.  
   
A alternativa nesse cenário seria:

1. **Gerar uma movimentação a pagar** em moeda nacional (saída), considerando a taxa de câmbio do dia e o valor convertido em R$.
2. **Gerar uma movimentação a receber** em moeda estrangeira (ex.: Moeda 02 – Dólar), com o valor correspondente na cotação do mesmo dia.

Dessa forma, é possível registrar corretamente a operação entre as diferentes moedas.  
  
**Saiba mais**  
[Movimentos Bancários - FINA100 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=501480542)
