---
content_hash: 241732175fbd626f31828362ddda6d4f096fa18d47fb6e6f7838bbd38d21dd6a
fetched_at: '2026-06-29T00:10:35.523603+00:00'
page_id: '531010338'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitarios - Assistente de Cobranca -
  Gestão - Andamento da Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531010338
version: 7
---

Esta funcionalidade permite que a incorporadora, exiba as etapas de construção do seu empreendimento, exibindo percentual de completude para cada etapa, e que demostrem o andamento e evolução. Esta funcionalidade permite ao usuário cadastrar várias etapas significativas para o comprador de seu empreendimento. Para dar flexibilidade para o cadastro dessas etapas o sistema permite que o usuário informe uma descrição que será exibida para o comprador.

## **Avanço da Obra:**

**Código do Andamento:**  
Valor Auto incremental que é o identificador do andamento da obra.   
**Descrição:**  
Informe a descrição do andamento da obra.   
**Empreendimento:**  
Informe qual empreendimento terá a medição do andamento da obra associada.  
**Ordenação**:  
Informe a ordenação de exibição do Avanço no portal/app.  
**Peso**:  
Informe o Peso que cada etapa do Andamento tem sobre a Obra. 

## **Calculo do Andamento da Obra:**

O calculo do andamento da obra será feito via média ponderada, considerando o peso informado em cada cadastro do andamento de obra.

Exemplo: Foram inseridos 3 andamentos de obras com pesos e com percentual de avanços diferentes.

1º → Peso 1, Avanço 100%

2º → Peso 5, Avanço 100%

3º → Peso 3, Avanço 40%

Considerando esses valores o empreendimento está com 80% construído.

|  |  |  |
| --- | --- | --- |
| **Peso** | **Percentual** | **PesoXPercentual** |
| 1 | 100 | 100 |
| 5 | 100 | 500 |
| 3 | 40 | 120 |
| 9 | 240 | 720 |

|  |
| --- |
| **MEDIA\_PONDERADA** |
| 80,0000 |
