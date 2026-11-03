---
article_id: 360045294533
category: RH - Rescisão
content_hash: e1fffcb1ec176cead2f54203316a0ca5313b8a626bce44ce393a3c07e110e361
fetched_at: '2026-06-28T22:43:49.561521+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar as rubricas de insalubridade
  no TRCT
type: support-article
updated_at: '2025-07-21T14:36:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045294533-RH-Linha-Protheus-GPE-Como-parametrizar-as-rubricas-de-insalubridade-no-TRCT
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26438794687383)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao imprimir o TRCT, como parametrizar as rubricas de insalubridade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE - Gestão de Pessoal - A partir da Versão 12.1.17.  
  
**Solução**Para que as rubricas de insalubridade sejam impressas conforme *layout* do Ministério do Trabalho, deve ser realizada as seguintes parametrizações abaixo:  
1. Para que as verbas de insalubridade sobre o saldo de salário (ID 0037, 0038, 0039 e 1282) sejam impressas na rubrica 53 do TRCT, o campo V.Homolognet deve estar preenchido com a rubrica 013 conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061517514)  
  
2. As verbas de insalubridade sobre as verbas indenizatórias (ID 1692, 1693, 1694, 1695, 1697, 1698 1699, 1700, 1701, 1702 e 1703) devem estar com o campo V. Homolognet em branco conforme abaixo, pois conforme *layout* do TRCT disponibilizado pelo Ministério do Trabalho, não há rubricas especificas para essas verbas, então no padrão do sistema serão impressas a partir da rubrica 95.1:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062427013)  
  
**OBS.:** Caso queira que o percentual da verba de insalubridade sobre o saldo de salário seja impresso no TRCT na rubrica 53, preencha nos IDs 0037, 0038, 0039 o percentual referente a cada uma das verbas.

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
