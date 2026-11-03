---
article_id: 360025886691
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: c1290bda36388aaabfb78d20129d350c2dfcf6076282a609d4709929d3d3ef79
fetched_at: '2026-06-28T22:39:41.211411+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Relacionamento
  das Tabelas dos Títulos Provisórios do Tipo "PR" e "PRE" com o Financeiro
type: support-article
updated_at: '2022-06-02T13:12:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025886691-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Relacionamento-das-Tabelas-dos-T%C3%ADtulos-Provis%C3%B3rios-do-Tipo-PR-e-PRE-com-o-Financeiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min**

**Dúvida**

Como é feito o relacionamento das tabelas do SIGAEIC com as tabelas do SIGAFIN referente os títulos provisórios "PR" e "PRE"?

**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões  
  
**Solução**

Todos os títulos gerados pelo SIGAEIC terão prefixo "EIC" e para cada fase do seu processo, será gerado um TIPO de Título, como segue:

**1 -Previsão do Pedido**

**1.1** Ao fazer a inclusão da *Purchase Order* com uma tabela Pré-Cálculo informada no campo W2\_TAB\_PC, o número do título será gravado com base da numeração preenchida no campo W2\_PO\_SIGA.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024772692/mceclip1.png)

**1.2** No SIGAFIN a informação será gravada com o No. Titulo no campo E2\_NUM, o Prefixo no campo E2\_PREFIXO "EIC", o Tipo do título no campo E2\_TIPO "PR" e no Histórico no campo E2\_HIST contendo a expressão do número do pedido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024772872/mceclip2.png)

**2 - Previsão Embarque/Desembaraço**

**2.1** Ao fazer a inclusão do Embarque/Desembaraço com uma tabela Pré-Cálculo informada no campo W6\_TAB\_PC, o número do título será gravado com base da numeração preenchida no campo W6\_NUMDUP.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024774872/mceclip3.png)

**2. 2** No SIGAFIN a informação será gravada com o No. Titulo no campo E2\_NUM, o Prefixo no campo E2\_PREFIXO "EIC", o Tipo do título no campo E2\_TIPO "PRE" e no Histórico no campo E2\_HIST contendo a expressão do número do Embarque/Desembaraço. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024787151/mceclip4.png)
