---
article_id: 360001020188
category: Originação de Grãos (OG)
content_hash: b7692c531b0443253458fc2eee9a998259197d007f65e7d290a73cf3304410df
fetched_at: '2026-06-28T22:45:40.995174+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Mensagem ao atualizar romaneio do tipo 3
type: support-article
updated_at: '2025-04-10T13:54:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001020188-Agro-Linha-Protheus-AGR-Mensagem-ao-atualizar-romaneio-do-tipo-3
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20415594294935)** Tempo aproximado para leitura: **00:00:35 min  
  
Ocorrência**Na rotina de **OGA250 -****Romaneio com Pesagem** ao tentar atualizar o registro de romaneio do **tipo 3 - Entrada para Depósito** é apresentada a mensagem **Em caso de formulário próprio, favor preencher os campos referentes à Nota Fiscal do Produtor**.  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12.1.17  
  
**Causa**Esse incidente ocorre, primeiramente, porque o parâmetro **MV\_AGRO205** está com o conteúdo **.F.**, validando, portanto, o preenchimento dos campos **Ser. NFP** e **Num. NFP**, que definem as informações referentes à **Nota Fiscal do Produtor.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Preencha o conteúdo referente a **Série da Nota Fiscal do Produtor**;

**2.** Preencha o conteúdo referente ao **Número da Nota Fiscal do Produtor**.
