---
article_id: 4406285826967
category: RH - Rescisão
content_hash: 70832eccfb87c119db39c2db554ed9a22bd7a90840de1287cfe8295b6250876b
fetched_at: '2026-06-28T22:43:52.108013+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar as rubricas de periculosidade
  no TRCT
type: support-article
updated_at: '2025-09-02T20:57:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406285826967-RH-Linha-Protheus-GPE-Como-parametrizar-as-rubricas-de-periculosidade-no-TRCT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18694114379031) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Como parametrizar as rubricas de periculosidade no TRCT?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Para que as rubricas de periculosidade sejam impressas conforme *layout* do Ministério do Trabalho, realize as seguintes parametrizações abaixo:  
1. Para que as verbas de periculosidade sobre o saldo de salário (ID 0036 e 1281) sejam impressas na rubrica 54 do TRCT, o campo V.Homolognet deve estar preenchido com a rubrica 014 conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18694103708567)

2. As verbas de periculosidade sobre as verbas indenizatórias (ID 1681, 1682, 1683, 1684 e 1685 por exemplo) devem estar com o campo V. Homolognet em branco conforme abaixo, pois conforme *layout* do TRCT disponibilizado pelo Ministério do Trabalho, não há rubricas especificas para essas verbas, então no padrão do sistema serão impressas a partir da rubrica 95.1:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18694103709719)

**Exemplo:**

**Cálculo rescisão.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18694103716503)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18694114394391)

**TRCT**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18694103720087)

**Periculosidade ID 0036 rubrica 54**

**Periculosidade ID 1681 rubrica 95.1**

**Saiba mais:**  
[RH - Linha Protheus - GPE - Como parametrizar as rubricas de insalubridade no TRCT?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045294533-MP-GPE-Como-parametrizar-as-rubricas-de-insalubridade-no-TRCT-?source=search)

[RH - Linha Protheus - GPE - Como relacionar verba ao código homolognet para impressão no TRCT?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055876753-RH-Linha-Protheus-GPE-Como-relacionar-verba-ao-c%C3%B3digo-homolognet-para-impress%C3%A3o-no-TRCT-?source=search)
