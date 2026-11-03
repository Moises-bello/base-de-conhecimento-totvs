---
article_id: 1500001934281
category: Integração RM
content_hash: ae4585363842f24c0befc8ab6c6b560e82eb854461ebc1d5d6b0962af9649c4b
fetched_at: '2026-06-28T22:42:36.925364+00:00'
product: protheus
section_id: 360012117913
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Recebimento de Custo Mão de Obra enviados
  pelo RM
type: support-article
updated_at: '2023-11-14T12:13:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001934281-Manufatura-Linha-Protheus-MNT-Recebimento-de-Custo-M%C3%A3o-de-Obra-enviados-pelo-RM
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:05** **min**  
**Dúvida**Como é realizado o recebimento do custo da mão de obra enviado pelo **Backoffice RM** ao **Manutenção de Ativos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integração RM - Todas as versões  
  
**Solução**Para o recebimento do custo de mão de obra enviados pelo **Backoffice RM**, é necessário a configuração manual para relacionar cada **Centro de Custo - T1\_CCUSTO** distinto ao produto do **RM**.Exemplo:

| Matrícula | Nome | Centro de Custo |
| --- | --- | --- |
| 000001 | João da Silva | 04.001.001 |
| 000002 | Pedro de Souza | 04.001.001 |
| 000003 | Maria das Dores Dias | 05.001.010 |
| 000004 | José Alcantara | 06.001.001 |

Conforme o exemplo acima, deve ser informado no cadastro de **De/Para** desta forma: 

| Campos | Conteúdo |
| --- | --- |
| **Referência** | **PROTHEUS** |
| **Tabela** | **ST1+EMPRESA+0** |
| **Alias** | **ST1** |
| **Campo** | **T1\_CCUSTO** |

**Importante**O produto que será relacionado no campo **Valor Externo** deve ter a unidade em **H - Hora - B1\_UM**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102918033/mceclip0.png)

O **Manutenção de Ativos** recebe os custos de **Mão de Obra/Produto** que são enviados pelo **Backoffice RM**.  
A valorização de custos de **Mão de Obra/Produto** é de responsabilidade do **Backoffice RM**.  
Através da rotina **Atualização de Custos - MNTA386** é possível atualizar os custos das ordens de serviço no **Manutenção de Ativos**, conforme o valor dos itens de estoque no **Backoffice RM**.
