---
article_id: 360050724593
category: RH - Férias
content_hash: 2162b3bd5c9d0b9c39bb1711effe30126a452b24f26579402a833155dfb43e35
fetched_at: '2026-06-28T22:43:58.285350+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionamento do mnemônico P_LIMTET - Cálculos
  do INSS das férias e/ou folha
type: support-article
updated_at: '2025-05-12T11:08:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050724593-RH-Linha-Protheus-GPE-Funcionamento-do-mnem%C3%B4nico-P-LIMTET-C%C3%A1lculos-do-INSS-das-f%C3%A9rias-e-ou-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21788193522711) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Funcionamento do mnemônico P\_LIMTET - Cálculos do INSS das férias e/ou folha  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Hoje no cálculo das férias particionadas o sistema possui três tipos de tratamento para o cálculo e apuração do INSS das férias. Em alguns casos o sistema ultrapassava o valor do desconto do INSS e da Dedução do INSS da base de cálculo do IRRF, isso gerava entendimentos diversos sobre o assunto. Por isso foi criado o mnemônico P\_LIMTET, que limita ao TETO tanto o desconto quanto a dedução do INSS da base do IRRF. 

**O mnemônico P\_LIMTET pode ser utilizado com as seguintes combinações:**

**MV\_DINSSFM = S e P\_LIMTET = .T. =** O sistema rateia o INSS já no cálculo das férias, trazendo os valores de INSS de férias mês seguinte proporcionalmente aos dias de gozo, porém não ultrapassa o teto.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708341897751)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708229963287)

**MV\_DINSSFM = S e P\_LIMTET = .F. =** O sistema rateia o INSS já no cálculo das férias, trazendo os valores de INSS de férias mês seguinte proporcionalmente aos dias de gozo, porém pode ultrapassar o teto (uso geralmente quando a folha é por regime de COMPETÊNCIA).

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708325515543)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708242699671)

**MV\_DINSSFM = N e P\_LIMTET = .T. =** O sistema NÃO rateia o INSS no cálculo das férias para fazer o recalculo diretamente na folha, ele leva os valores calculados nas férias para folha e realize a proporção das bases de INSS de férias e folha. E não ultrapassa o teto.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708288869015)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708246665111)

**MV\_DINSSFM = N e P\_LIMTET = .F. =** O sistema rateia o INSS já no cálculo das férias, trazendo os valores de INSS de férias mês seguinte proporcionalmente aos dias de gozo, porém ultrapassa o teto.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708272278039)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708226691479)

**MV\_DINSSFM = R e P\_LIMTET = .T. =** O sistema rateia o INSS já no cálculo das férias de acordo com os dias de gozo em cada mês, recalculando na folha apenas o INSS restante sem mudar o recibo das férias e realiza a limitação do teto.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708268643863)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708230652055)

**MV\_DINSSFM = R e P\_LIMTET = .F. =** O sistema rateia o INSS já no cálculo das férias de acordo com os dias de gozo em cada mês, recalculando na folha apenas o INSS restante sem mudar o recibo das férias e NÃO realiza a limitação do teto.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708268273559)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11708227080343)  
  
[Verifique Exemplos de cálculo aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=506394225)  
  
 **Saiba Mais**[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_DINSSFM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016451652-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-DINSSFM?source=search)[RH - Linha Protheus - GPE - Como conferir o INSS férias, quando o parâmetro MV\_DINSSFM esta com R e o funcionário teve férias partidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019891371-RH-Linha-Protheus-GPE-Como-conferir-o-INSS-f%C3%A9rias-quando-o-par%C3%A2metro-MV-DINSSFM-esta-com-R-e-o-funcion%C3%A1rio-teve-f%C3%A9rias-partidas-?source=search)  
[RH - Linha Protheus - GPE - Como conferir INSS salário e INSS férias em cálculo de folha de pagamento com o parâmetro MV\_DINSSFM = N](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008686801-RH-Linha-Protheus-GPE-Como-conferir-INSS-sal%C3%A1rio-e-INSS-f%C3%A9rias-em-c%C3%A1lculo-de-folha-de-pagamento-com-o-par%C3%A2metro-MV-DINSSFM-N?source=search)  
[RH - Linha Protheus - GPE - Conceito do cálculo de folha com Férias partidas utilizando o parâmetro MV\_DINSSFM= S](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017956652-RH-Linha-Protheus-GPE-Conceito-do-c%C3%A1lculo-de-folha-com-F%C3%A9rias-partidas-utilizando-o-par%C3%A2metro-MV-DINSSFM-S?source=search)
