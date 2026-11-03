---
article_id: 23221007727639
category: Financeiro - Contas a Receber
content_hash: b9ca169d90e45b6249ba6af6935721a2845d795fd54f73758f07306716fe92fd
fetched_at: '2026-06-28T22:38:12.771122+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Rateio de
  IR progressivo está calculando errado quando existem dois títulos com fornecedores
  diferentes porem com o mesmo CNPJ, e cada fornecedor tem rateio de 100% para CPFs
  diferente.
type: support-article
updated_at: '2024-05-03T19:40:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23221007727639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Rateio-de-IR-progressivo-est%C3%A1-calculando-errado-quando-existem-dois-t%C3%ADtulos-com-fornecedores-diferentes-porem-com-o-mesmo-CNPJ-e-cada-fornecedor-tem-rateio-de-100-para-CPFs-diferente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23221018359703) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**

Na inclusão do segundo título, o sistema está acumulando o IR onde o cadastro dos dois fornecedores possuem o mesmo CNPJ, porem com CPFs de rateio de Ir progressivo diferente.

**Cadastro do Fornecedor 01**

**CNPJ:** 00.000.001/0001-01

**CPF:** 111.111.111.11

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300185239)](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300185239)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243295612311)](https://centraldeatendimento.totvs.com/hc/article_attachments/23243295612311)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300215703)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300221847)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300239383)

**Cadastro do Fornecedor 02**

**CNPJ:** 00.000.001/0001-01

**CPF:** 222.222.222.22

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300246679)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243401141271)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243295675159)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA050 - Todas as versões

**Exemplo:**

**Título A no valor de R$ 3.500 - IR 154,60 - Calculo correto**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300280855)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300299799)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300303767)**

**Titulo B  no valor R$ 2.800,00 - IR 692,94 - Como podemos reparar o cálculo está errado.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243300315927)**

**Solução**

Para que esse cenário funcione perfeitamente é necessário que o parâmetro **MV\_AGLIMPJ** esteja configurado com conteúdo = **'3'** e os fornecedores possuam a mesma raiz de **CNPJ** ou o mesmo **CNPJ**

Ao incluir o primeiro do título, é necessário informar o campo "Gera Dirf"  = Sim (E2\_DIRF) e o código de retenção (E2\_CODRET) pertencente no parâmetro **MV\_RETIRRT.**

**Cálculo Correto do IR:**

#### **Titulo A para o fornecedor 01** no valor de R$ 3.500,00

#### 15,0% alíquota tabela progressiva x R$ 3.500,00= R$ 525,00

#### R$ 525,00 - R$ 370,40 valor da tabela progressiva = **R$ 154,60 IRPF**

#### **Titulo B para o fornecedor 02** no valor de R$ 2.800,00

#### 7,5% alíquota tabela progressiva x R$ 2.800,00 = R$ 210,00

#### R$ 210,00 - R$ 158,40 valor da tabela progressiva = **R$ 51,60 IRPF**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243295756951)

Podemos observar que o IR para o segundo título está correto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243295765655)

**SAIBA MAIS**

**[Cadastro de CPF's rateio de IRRF progressivo enviado a DIRF](https://tdn.totvs.com/display/PROT/Cadastro+de+CPF%27s+rateio+de+IRRF+progressivo+enviado+a+DIRF)**
