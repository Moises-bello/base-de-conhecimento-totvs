---
article_id: 360025937174
category: CRM - Vendas
content_hash: 3eaa67d30a1e94a7ee599bc42e96295d773b5dddde5ff26b00cfa6e302953eaf
fetched_at: '2026-06-28T22:40:25.850574+00:00'
product: protheus
section_id: 1500001549102
source: central-protheus
title: Cross Seguimentos - TOTVS BackOffice (Linha Protheus) - CRM -  Help FT300VLDSTATUS
type: support-article
updated_at: '2025-02-12T15:07:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025937174-Cross-Seguimentos-TOTVS-BackOffice-Linha-Protheus-CRM-Help-FT300VLDSTATUS
---

**Ocorrência**O sistema esta apresentando o help **FT300VLDSTATUS** na exclusão/alteração da oportunidade.![help.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019552721/help.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Customer Relationship Management SIGACRM - Todas as versões  
  
**Causa**O help indica que a oportunidade gerada não pode sofrer alteração/exclusão pois o conteúdo do campo de status **AD1\_STATUS** esta como **Ganha** ou **Perdido**.

**Solução**

Ao encerrar uma oportunidade de vendas (FATA300/ CRMA110) com status "Ganha/Perdido" , seja no CRM, no Faturamento ou Gestão de Serviços, o sistema não reabre a oportunidade de vendas para alteração, se efetuar o click no botão alterar, o sistema exibirá o help.

A oportunidade com status ganha e perdido não pode ser excluída nem alterada.

Trata-se de  regras de negociação, ou seja, uma vez que a oportunidade de vendas foi finalizada como Ganha/Perdido, entende-se que foi negociado um produto/serviço, com um determinado valor para uma determinada condição de pagamento,  desta forma, se o cliente desistiu da negociação firmada,  entende-se que aquela negociação não vale mais e por isso, deve ser efetuado uma nova negociação e incluir uma nova oportunidade de vendas.

Este conceito precede desde versões anteriores a versão 11 , não é permitido sua exclusão/alteração e não há parametrização para sua reabertura.

Os status do campo **AD1\_STATUS** são:

* 1=Aberto
* 2=Perdido
* 3=Suspenso
* 9=Ganha

O help **FT300VLDSTATUS** ocorre em 4 situações:

1. Esta oportunidade não pode ser **alterada**pois está perdida
2. Esta oportunidade não pode ser **excluída**pois está perdida.
3. Esta oportunidade não pode ser **alterada**pois está encerrada.
4. Esta oportunidade não pode ser **excluída**pois está encerrada.
