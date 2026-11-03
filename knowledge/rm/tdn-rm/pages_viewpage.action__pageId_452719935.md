---
content_hash: f13ed7b3a8b97bdff12b39c5c362bbd9d5f5a4ce5afbcc53741865685dbded88
fetched_at: '2026-06-29T00:10:11.086139+00:00'
page_id: '452719935'
product: rm
source: tdn-rm
title: Código de Cálculo 211 - IRRF RRA Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719935
version: 3
---

Este evento é do tipo desconto, valor e sem incidência.

Utilizado no cálculo do valor para RRA e será lançado no período parametrizado em Parametrizador / Folha Normal / Geral 2/2

Mais informações em: [Rendimentos Recebidos Acumuladamente (RRA)](https://tdn.totvs.com/pages/viewpage.action?pageId=715818269)

**Observação**  
É necessário que tenha cadastrado no sistema a tabela de cálculo com a finalidade 3 - RRA com os valores da faixas, percentual descontado e valores a deduzir de Imposto de Renda de RRA, para que o cálculo de imposto de renda de RRA seja calculado.  
   
Quando calculada a diferença utilizando o Cálculo de RRA, o valor do evento no campo Valor do IRRF é inserido no histórico de RRA vinculado ao funcionário. Esse valor é informado na DIRF, no campo correspondente, não sendo retornado nos rendimentos tributáveis.    
   
**Atenção**  
Caso o Funcionário tenha dois períodos de gozo de férias para serem recalculados as diferenças e um deles foi calculado no ano atual, mesmo com o parâmetro marcado, somente o valor referente aos eventos de RRA que serão considerados no IR RRA. As diferenças referentes ao ano atual serão considerados no evento CC 61.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
