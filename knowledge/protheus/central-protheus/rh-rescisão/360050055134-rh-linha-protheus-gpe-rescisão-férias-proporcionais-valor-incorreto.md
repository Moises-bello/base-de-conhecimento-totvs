---
article_id: 360050055134
category: RH - Rescisão
content_hash: 07816e7eabf5f1dc2b01d9c6db1b1ab247af23b15611bc2a8bd481bddbab24ca
fetched_at: '2026-06-28T22:43:54.444179+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Rescisão férias proporcionais valor incorreto.
type: support-article
updated_at: '2025-05-07T21:21:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050055134-RH-Linha-Protheus-GPE-Rescis%C3%A3o-f%C3%A9rias-proporcionais-valor-incorreto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19275923593623) Tempo aproximado para leitura: **00:01:30 min**

**Ocorrência**  
No calculo da rescisão o valor das férias proporcionais ficam incorreto.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**   
Esse incidente ocorre, pois o sistema esta subtraindo o valor das férias sobre aviso da verba de férias proporcionais indevidamente quando não há verbas com os IDs de médias de rescisão cadastradas.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Crie novas verbas e relacione aos IDs abaixo:

0248 Média Férias Vencidas Rescisão  
0249 Média Férias Proporcionais Rescisão  
0250 Média Aviso Prévio Rescisão  
0251 Média 13º Salário Rescisão  
0252 Média Férias Aviso Prévio Indenizado Rescisão  
0253 Média  13º Salário Aviso Prévio Indenizado Rescisão

Para configuração das mesmas utilize as mesmas incidências correspondente a verba original.  
Exemplo: 0248 Médias Férias Vencidas =  Verba Férias Vencidas

Observação: Lembrando que as verbas de férias de médias devem estar com NÃO pra média.

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo

[RH - Linha Protheus - GPE - Férias Proporcionais dividindo por 31 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003366622-RH-Linha-Protheus-GPE-F%C3%A9rias-Proporcionais-dividindo-por-31-dias-?source=search)

[RH - Linha Protheus - GPE - Dias de Faltas injustificadas não estão abatendo nas Férias da Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016647531-RH-Linha-Protheus-GPE-Dias-de-Faltas-injustificadas-n%C3%A3o-est%C3%A3o-abatendo-nas-F%C3%A9rias-da-Rescis%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Referência de Férias Proporcionais na Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12626645046807-RH-Linha-Protheus-GPE-Refer%C3%AAncia-de-F%C3%A9rias-Proporcionais-na-Rescis%C3%A3o-?source=search)

[RH - Linha Protheus - GPE - Como calcular a rescisão para um funcionário de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010059471-RH-Linha-Protheus-GPE-Como-calcular-a-rescis%C3%A3o-para-um-funcion%C3%A1rio-de-f%C3%A9rias?source=search)

[RH - Linha Protheus - GPE - Cálculo de rescisão após retorno de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047533313-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-ap%C3%B3s-retorno-de-f%C3%A9rias?source=search)

[RH - Linha Protheus - GPE - Abatimento faltas nos avos férias proporcionais rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13312210019991-RH-Linha-Protheus-GPE-Abatimento-faltas-nos-avos-f%C3%A9rias-proporcionais-rescis%C3%A3o?source=search)
