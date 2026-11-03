---
article_id: 14526166593175
category: Encargos
content_hash: 9c1405297a0cea8a707244b615e2d46aa27f81b24aaef0958e636bdcfc3cc92d
fetched_at: '2026-06-28T22:46:52.328585+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração do encargo  TIPO 6 - Provisão de encargos de férias
type: support-article
updated_at: '2024-10-15T19:23:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14526166593175-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-6-Provis%C3%A3o-de-encargos-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27091172136471) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como fazer a geração do encargo TIPO 6 - Provisão de encargos de férias  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para geração do encargo TIPO 6 - Provisão de encargos de férias o sistema irá considerar o valor da seguinte forma : (Provisão \* % encargo / 100) + (Provisão \* % Aposentadoria Especial / 100) + (Provisão \* % (FAP \* SAT) / 100)

Caso o funcionário tenha percentual de aposentadoria especial o mesmo é informado no cadastro da seção centralizadora:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14524448562071)

No cadastro do funcionário aba FGTS/SEFIP:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14525131118103)

As informações de FAP devem ser cadastradas na seção centralizadora:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14525233679767)

E o Acidente de trabalho Percentual informado no cadastro da seção do funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27091172139159)

Cadastro do encargo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14525291751063)

Para geração é necessário verificar o código ativo do mesmo, pois no momento da geração irá selecionar o mesmo código ativo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14525636361879)

Caso utilizar o Rateio, o mesmo ficará salvo em Histórico de encargos | anexos | Rateio de encargo por centro de custo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14525716423191)

Log da geração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14525732624279)

**Saiba mais**  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)  
[RH - RM - FOP - Parametrização para cálculo de aposentadoria especial](RH%20-%20RM%20-%20FOP%20-%20C%C3%A1lculo%20do%20percentual%20de%20aposentadoria%20especial)
