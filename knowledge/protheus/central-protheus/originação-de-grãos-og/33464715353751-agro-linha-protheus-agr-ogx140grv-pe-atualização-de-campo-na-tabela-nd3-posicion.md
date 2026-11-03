---
article_id: 33464715353751
category: Originação de Grãos (OG)
content_hash: c39bdb790f7695dc5303387dda981cddc29dfd0e75de52c71992824bd303a815
fetched_at: '2026-06-28T22:45:41.115103+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - OGX140GRV PE atualização de campo na tabela ND3
  posicionada - SISDEV
type: support-article
updated_at: '2025-07-15T12:59:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33464715353751-Agro-Linha-Protheus-AGR-OGX140GRV-PE-atualiza%C3%A7%C3%A3o-de-campo-na-tabela-ND3-posicionada-SISDEV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33464752763799) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como funciona um **Ponto de Entrada para** **Manipular dados na geração de produção à Pagar - Registro de Negócios**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Visão Geral:**  
O ponto de entrada **OGX140GRV()** esta disponível na rotina de **OGX140** a qual é executada após a gravação do documento de entrada **MATA103** onde o parâmetro **MV\_SISDEV** deve estar ativo e o produto deve ser do tipo  semente.

Este ponto de entrada **OGX140GRV** permite a atualização de campo na tabela **ND3** posicionada, esta tabela **ND3** é referente aos campos de integração com o Sistema **SISDEV**. A execução deste ponto de entrada não interfere na execução da rotina de documento de entrada.

|  |  |
| --- | --- |
| **Localização:** | OGX140GRV() |
| **Programa Fonte:** | OGX140 |
| **Função:** | Ponto de Entrada para a atualização de campo na tabela ND3 posicionada. |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | |  |  |  |  | |

**Exemplo de Utilização:**

Neste exemplo é gravado dados em um campo customizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33464752764439)
