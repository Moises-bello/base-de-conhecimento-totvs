---
article_id: 23001550763799
category: Administração de Pessoal
content_hash: 26c724e346e4a903727975782f64306772906f6aac79b4be452d746911d276f8
fetched_at: '2026-06-28T22:47:01.182215+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP -   Novos códigos de cálculos para apuração do FGTS na rescisão
type: support-article
updated_at: '2025-01-24T13:25:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23001550763799-RH-RM-FOP-Novos-c%C3%B3digos-de-c%C3%A1lculos-para-apura%C3%A7%C3%A3o-do-FGTS-na-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23001550741015) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como cadastrar os novos códigos de cálculos para atender o FGTS na rescisão?  
  
**Ambiente**

A partir dos patches/releases:

12.1.2306.252  
12.1.2310.194  
12.1.2402.132  
12.1.2406 e Superiores

**Solução**

*Código de Cálculo 467* - FGTS AVISO PRÉVIO do tipo Base para calcular o Valor do FGTS de Aviso Prévio considerando como Base de FGTS do aviso prévio os eventos com os CC’s 62, 219, 99 e 140, e todos os eventos de média do grupo de Aviso Prévio do Sindicato, e se os mesmos incidirem/estornarem no FGTS Folha.

Evento base de cálculo, do tipo valor e sem incidência. A prioridade será 81 fixo pelo sistema.

*Código de Cálculo 468* - FGTS 13º INDENIZADO do tipo Base para calcular o Valor do FGTS 13º sobre aviso prévio considerando como Base de FGTS 13º sobre aviso prévio os eventos com os CC’s  71, 220 e 98 e se os mesmos incidirem/estornarem no FGTS 13º.

Evento base de cálculo, do tipo valor e sem incidência. A prioridade será 81 fixo pelo sistema.

Na Rescisão Complementar os novos códigos de cálculo para as bases indenizadas 469 - BASE DE FGTS DIFERENÇA AVISO INDENIZADO e 470 - BASE DE FGTS DIFERENÇA 13º INDENIZADO

Importante:

Quando houver cálculo de rescisão complementar referente a rescisões processadas antes da liberação dessa implementação, os valores do FGTS não serão separados por não existirem Código de Cálculo 467 - FGTS AVISO PRÉVIO e Código de Cálculo 468 - FGTS 13º INDENIZADO na rescisão original.

Quando houver atualização da base de dados os campos novos serão preenchidos com NULL. Os campos criados nas tabelas somente serão preenchidos após cálculos depois da conversão da base de dados.

Saiba mais:

[Apuração do FGTS na Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=839304283)

[RH - RM - FOP - Códigos de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo)
