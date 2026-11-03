---
article_id: 27583295878935
category: Financeiro - Movimentação Bancária
content_hash: cae295a7bed6ea8018b7d0b103c99fa1fb6a37ce5a62f897df9652a00552b9e6
fetched_at: '2026-06-28T22:38:19.434627+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Como efetuar
  de forma correta para cenários parciais, os matches não realizados e nem todos os
  dados foram identificados
type: support-article
updated_at: '2024-11-06T10:11:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27583295878935-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Como-efetuar-de-forma-correta-para-cen%C3%A1rios-parciais-os-matches-n%C3%A3o-realizados-e-nem-todos-os-dados-foram-identificados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27583295866775) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**No caso dos cenários parciais, os matches não realizados, visto que nem todos os dados foram identificados, como efetuar de forma correta?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -Financeiro - A partir da versão 12.1.22.10  
  
  
**Solução**

Os matches são realizados de duas formas, **manual ou automática**.

**Automática:** São **matches** realizados de forma automática pelo sistema. Funcionam da seguinte forma:  
Caso os registros encontrados na busca de acordo com os filtros utilizados, enquadrem-se em uma regra de match cadastrada na tabela **QLB (QLB\_REGMAT**). A rotina já realizara o **match**, e caso o usuário aplicar a conciliação, o registro será conciliado.

**Manual:** São os **matches** que são realizados pelo usuário selecionando um registro de origem e destino manualmente. Só é necessário realizar **matches manuais** em registros que não se enquadraram em nenhuma regra de match da configuração de conciliação utilizada.
