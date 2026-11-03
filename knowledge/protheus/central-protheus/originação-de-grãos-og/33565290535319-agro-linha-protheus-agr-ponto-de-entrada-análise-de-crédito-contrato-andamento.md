---
article_id: 33565290535319
category: Originação de Grãos (OG)
content_hash: b76ee24780b0c97cd7f5697ba32c306ef704fcff733b7cd19b3189e74d2c1a7c
fetched_at: '2026-06-28T22:45:42.670540+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada Análise de Crédito - Contrato
  Andamento
type: support-article
updated_at: '2025-11-03T20:38:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33565290535319-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-An%C3%A1lise-de-Cr%C3%A9dito-Contrato-Andamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33565313672343) Tempo aproximado para leitura: **00:01:25 min**  
  
**Dúvida**  
Como funciona um **Ponto de Entrada Análise de Crédito - Contrato Andamento**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRX500O | Função Análise de Crédito | |
| **Ponto de Entrada:** | AGR500QC |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada para a manipulação da Consulta de análise de crédito de romaneio em andamento. |
| **Localização:** | Rotina de Romaneio Unificado/ Rotina Agendamento AGRO/ Rotina Contrato |
| **Eventos:** | O Ponto de Entrada é concluído para confirmar as alterações de inclusão ou alteração. |
| **Programa Fonte:** | AGRX500O |
| **Função:** | AX500FVlAn() |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **cQuery** | Caractere | Retorna a consulta que pode ser manipulada dentro do PE | Sim | |

**Exemplo:**

**#include '**[**protheus.ch**](http://protheus.ch/)**'**  
**#include '**[**parmtype.ch**](http://parmtype.ch/)**'**

**User Function AGR500QC()**

**Local cQuery := PARAMIXB[1]  //A variável contém a query passada no ponto de entrada**  
  
**Return cQuery**
