---
article_id: 29316145578263
category: Originação de Grãos (OG)
content_hash: d6d1545018ed0b63549920f5818c768eb711924818bd0e97a79c251163de4e23
fetched_at: '2026-06-28T22:45:44.841217+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Romaneio não altera o status ao excluir Documento
  de Entrada na Gestão Agroindústria - Manutenção
type: support-article
updated_at: '2025-06-24T20:32:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29316145578263-Agro-Linha-Protheus-AGR-Romaneio-n%C3%A3o-altera-o-status-ao-excluir-Documento-de-Entrada-na-Gest%C3%A3o-Agroind%C3%BAstria-Manuten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29316129544215) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**  
Como funciona uma estrutura em que o **Romaneio não altera o status ao excluir Documento de Entrada na Gestão Agroindústria - Manutenção**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Veja na tabela os **Dados Gerais**;

| Linha de Produto: | Protheus |
| --- | --- |

| Segmento: | Backoffice |
| Módulo: | Gestão de Agronegócio |
| Função: | OGA251 - Romaneio sem pesagem |
| Requisito/Story/Issue (informe o requisito relacionado) : | DAGROCCO-3218 |

  

**2.** **Situação/Requisito**;  
Ao estornar um documento de entrada de um **Romaneio** com dois contratos, o Sistema altera o status para Atualizado, mas não permite reabrir;

**3.** **Solução**.  
O Sistema verifica se todos os documentos de entradas do romaneio foram estornados para permitir o processo de **Reabrir o romaneio**. A partir desta versão o Sistema só permitirá reabrir um romaneio já confirmado se todos os documentos de entrada foram estornados.
