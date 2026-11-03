---
article_id: 14598083119511
category: RH - Rescisão
content_hash: 35efbcbee479b41ed151095dce72f7e6ff0776a96a67ed7f52ee1b54648f29a4
fetched_at: '2026-06-28T22:43:48.504442+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo de Indenização na Rescisão para Professor
  Id 0110
type: support-article
updated_at: '2023-05-15T13:34:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14598083119511-RH-Linha-Protheus-GPE-Calculo-de-Indeniza%C3%A7%C3%A3o-na-Rescis%C3%A3o-para-Professor-Id-0110
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como calcular Indenização na Rescisão para Professor Id 0110?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**

Para o cálculo da indenização de professores na rescisão contratual, devem ser adotados os seguintes procedimentos:

1 - Entrar em **Atualizações/ Cadastros/ Verbas** e crie uma verba de indenização na rescisão com as seguintes características:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14597885213591)

Ex.:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14597886901911)

2) Configurar os mnemônicos descritos;

3) Preencher campos necessários no Cadastro do Sindicato.

**Dica:**

**O identificador (Id 110) não é obrigatório, no entanto, caso não exista, o cálculo da indenização não será gerado.**

2 - Para configurar os mnemônicos, entrar em **Atualizações> Definições de cálculo> Mnemônicos**.

**P\_CODPGIND** - Códigos de rescisão para pagamento da indenização  
Informe os códigos de rescisão que serão utilizados no cálculo da indenização.

Este código é informado pelo usuário no início do cálculo da rescisão, de acordo com a Tabela 32 - Tipos de Rescisão.  
Exemplo: **01/02** (sempre entre aspas e separados por barra /).  
Neste exemplo, somente será calculada a indenização para as rescisões tipo 01 e 02.

**P\_PIDEM1SM** - Dia e mês de início do período para demissão sem pagamento da indenização no 1º semestre.

**P\_PIDEM2SM** - Dia e mês de início do período para demissão sem pagamento da indenização no 2º semestre.

Informe o dia e o mês que será utilizado como período ideal para efetuar a demissão do funcionário, pois, do início do período letivo até o dia e mês informado neste mnemônico, não serão calculados os dias de indenização.

Exemplo: Início do período letivo do 1º semestre: 01/02. Dia e mês cadastrados no mnemônico: 16/02. Desta forma, se o funcionário for demitido neste período, a empresa não incorrerá no pagamento da indenização.

**P\_CCAVITRA****-** Conta o aviso como dias trabalhados na apuração dos dias de indenização. Se preenchido com **S**, os dias de aviso serão somados à data de demissão para, a partir desta nova data, apurar os dias de indenização. Se **N**, os dias de indenização serão apurados a partir da data de demissão.

**P\_PAGRECES**- Pagar indenização referente ao período de recesso. Se S, serão apurados os dias de indenização contados do período de recesso até o início do próximo período letivo. Se N, não serão apurados os dias de indenização referentes ao período de recesso.

**P\_PAGINDFD** **-**Pagar os dias de indenização sobre férias e 13º salário. Se S, sobre os dias de indenização serão apurados os avos de férias e 13º salário. Se N, somente serão pagos os dias de indenização.

**P\_NDRECALS** **–**Quantidade de dias de recesso até o início do primeiro período do próximo ano letivo. Dias de recesso, que serão contados a partir do término do segundo semestre.

**Mnemônicos internos**

**nDiasIndP**- Dias de indenização do professor.

**nDFerIndP**- Dias de férias referentes à indenização.

**nA13oIndP**- Avos de 13º referentes à indenização.

Os 3 últimos mnemônicos descritos acima são utilizados pela rotina para os procedimentos de cálculo, portanto não necessitam de manutenção por parte do usuário.

**Observação:**

**Caso haja a necessidade de configurá-los por sindicato, aconselhamos que sejam criados campos compatíveis com os mnemônicos no Cadastro de Sindicatos (RCE) além de criar uma fórmula passando o conteúdo destes campos para os mnemônicos.**

3 - Cadastro de Sindicato:

Informar o código do sindicato no cadastro de funcionários e no cadastro de sindicato (aba Professor), preencher campos:

**D/M Ini 1.Sm.** (RCE\_INI1SM) - Dia e mês do inicio do 1º semestre.

**D/M Fim 1.Sm.** (RCE\_FIM1SM) - Dia e mês do fim do 1º semestre.

**D/M Ini 2.Sm.** (RCE\_INI2SM) - Dia e mês do inicio do 2º semestre.

**D/M Fim 2.Sm.** (RCE\_FIM2SM) - Dia e mês do fim do 2º semestre.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14597985586327)

4 - Exemplos:

**Exemplo 1:**

Com a verba configurada e os mnemônicos com as configurações abaixo, gera a verba 159 (Id 0110), referente a Indenização :

P\_CODPGIND   = “01/02” (Tipos de rescisão igual a 01 ou 02)

P\_PIDEM1SM   = “”  ( Pagará indenização em qualquer período de demissão)

P\_PIDEM2SM   = “” ( Pagará indenização em qualquer período de demissão)

Dias de indenização = Campo do sindicato (D/M Fim 2[.sm](http://1.sm/)) – Data Demissão

Dias de indenização = 15/12/2018 – 01/11/2018 = **44**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14597988304279)**

**Exemplo 2:** Se forem preenchidos os mnemônicos abaixo:

P\_CODPGIND   = “01/02”  (Tipos de rescisão igual a 01 ou 02)

P\_PIDEM1SM   = “01/03”  (Não paga indenização para o funcionário demitido no 1o. semestre até 01/03)

P\_PIDEM2SM   = “01/09”  (Não paga indenização para o funcionário demitido no 2o. semestre  até 01/09)

(Sindicato: 1º semestre = 01/02 à 30/06 // 2º semestre = 01/08 à 15/12 )

Não será gerada a indenização, pois como a demissão foi 05/02/2019 e o mnemônico P\_PIDEM1SM  está com mês/ano = 01/03, então o funcionário que teve demissão na janela de 01/02 e 01/03 não recebe indenização, ou seja, **não**gerou a verba 159 (Id0110):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14597964518935)

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo  
<https://tdn.totvs.com/pages/releaseview.action?pageId=759933852#ids-id4>
