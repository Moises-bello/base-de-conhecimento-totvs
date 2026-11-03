---
article_id: 5701748974487
category: esocial - Smart eSocial
content_hash: 745cbe96d4d0266eba2f095e1906a5d071c73cde116e9dceeb10a18d3ea69d32
fetched_at: '2026-06-28T22:47:07.640187+00:00'
product: rm
section_id: 1500000834461
source: central-rm
title: RH - Linha Protheus - TAF - eSocial - O valor 'X' informado na tag  codLotacao
  não existe na base de dados
type: support-article
updated_at: '2024-08-16T18:54:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5701748974487-RH-Linha-Protheus-TAF-eSocial-O-valor-X-informado-na-tag-codLotacao-n%C3%A3o-existe-na-base-de-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23698902460951)**Tempo aproximado para leitura: **00:01:45 min****Dúvida**Ao enviar o evento S-1200 é apresentado a mensagem: **Erro 1 - O valor 'XXX' informado na tag codLotacao não existe na base de dados.****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - Todas as Versões.  
  
**Causa**O erro ocorre por não existir o Código de Lotação na tabela do S-1020 no TAF ou a vigência está posterior ao período de apuração.

Print eSocial  codLotação:![](https://totvssuporte.zendesk.com/attachments/token/6uQqBNR1LBe6WcN4yR6tMIngk/?name=inline403664037.png)

**Solução**Para corrigir o erro, realize os passos abaixo.

1 - Verifique se foi transmitido ao TAF o evento **S-1020**. Para tal validação, acesse no TAF o menu **Atualizações | Eventos eSocial | Tabelas | Lotações Tributárias** e localize pelo código da lotação correspondente.​  
2 - Caso ainda não tenha sido transmitido, envie o **S-1020** com inicio de vigência do **P****eríodo de Apuração** desejado.  
3 -  Em seguida, integre o evento novamente.  
  
**Saiba mais**Para mais informações acesse:

* [Identificação da origem da Lotação Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015506452-RH-RM-FOP-eSocial-Identifica%C3%A7%C3%A3o-da-origem-da-Lota%C3%A7%C3%A3o-Tribut%C3%A1ria?source=search)
* [Lotação tributária (S-1020) quando não utilizado tomadores de serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033722793-RH-RM-FOP-eSocial-Lota%C3%A7%C3%A3o-tribut%C3%A1ria-S-1020-quando-n%C3%A3o-utilizado-tomadores-de-servi%C3%A7os?source=search)
* [RH - RM - FOP - eSocial - S-1020 - Lotação tributária para empresas que utilizam tomadores de serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015470032-RH-RM-FOP-eSocial-S-1020-Lota%C3%A7%C3%A3o-tribut%C3%A1ria-para-empresas-que-utilizam-tomadores-de-servi%C3%A7os?source=search)
