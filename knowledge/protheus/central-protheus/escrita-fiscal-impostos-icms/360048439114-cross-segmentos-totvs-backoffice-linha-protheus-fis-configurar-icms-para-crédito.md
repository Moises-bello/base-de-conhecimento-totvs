---
article_id: 360048439114
category: Escrita Fiscal - Impostos - ICMS
content_hash: 0b06a6834ea358722b049945a1788ee46d8a07510d4da731057dc3268f20ca39
fetched_at: '2026-06-28T22:39:25.630069+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configurar ICMS para
  Crédito Presumido
type: support-article
updated_at: '2025-01-28T21:07:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048439114-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configurar-ICMS-para-Cr%C3%A9dito-Presumido
---

**Duvida:**

Configurar ICMS para Credito Presumido.

**Ambiente:**

Protheus - A partir da versão 12

**Solução:**

O Tipo do Crédito Presumido do ICMS (**o campo Tp Cred Pres.(F4\_TPCPRES**), será utilizado para definir a forma de cálculo do crédito presumido do ICMS, sendo esse utilizado em conjunto com o campo “Crd.Pres (F4\_CRDPRES)”, onde deve ser informado o percentual de crédito.

**Opções disponíveis:**

C=Crédito Sobre total da operação;

B=Crédito Sobre Base de Cálculo do ICMS;

R=Crédito Sobre Base de Cálculo do ICMS, com redução no valor da operação.

F=Crédito Sobre valor total da operação com limite até o valor de frete da operação.

M = Crédito sobre o Valor da Mercadoria.

N = Crédito sobre o Valor do ICMS.

**Cadastro de TES - Tipos de Entrada e Saída (MATA080).**

1- Acesse o Cadastro de TES **(MATA080)** e atribua o percentual do crédito no campo

Crd. Pres. (F4\_CRDPRES)

2 - Após atribuir o percentual, informe através do campo **Tp Cred Pres (F4\_TPCPRES)** como será a forma

do cálculo do crédito presumido, por meio das seguintes opções disponíveis:

**C=Cred.Tot.oper**

Esta opção considera para base de cálculo do crédito presumido, o valor total da

operação, aplicando o percentual informado no campo **Crd.Pres.(F4\_CRDPRES)**.

***Exemplo de cálculo:***

Valor da operação = R$ 1.000,00

Percentual no campo Crd. Pres. = 9%

Cálculo do crédito presumido: 1.000,00 \* 9% = 90,00

**B=Cred. BC ICMS**

Esta opção considera para base de cálculo do crédito presumido, o valor da base de

cálculo do ICMS. Exemplo de cálculo:

Valor da operação = R$ 1.000,00

Base de cálculo do ICMS = 1.000,00

Percentual no campo Crd. Pres. = 20%

Cálculo do crédito presumido: 1.000,00 \* 20% = R$ 200,00

Valor do crédito presumido = R$ 200,00

**IMPORTANTE**

*Caso considere o IPI na base de cálculo do ICMS o cálculo do valor do crédito presumido seria*

*conforme exemplo abaixo:*

Valor da operação = R$ 1.000,00

Valor do IPI = R$100,00

Base de cálculo do ICMS = 1.100,00

Procedimentos para Utilização

Percentual no campo Crd. Pres. = 5%

Cálculo do crédito presumido: 1.100,00 \* 5% = R$ 55,00

Valor do crédito presumido = R$ 200,00**R=Cred.BC ICMS C/R**

Esta opção considera para base de cálculo do crédito presumido, o valor da base de cálculo do ICMS,

e também subtrai do valor total da operação o valor do crédito presumido calculado.

***Exemplo de cálculo:***

Valor da operação = R$ 1.000,00

Base de cálculo do ICMS = 1.000,00

Percentual no campo Crd. Pres. = 9%

Cálculo do crédito presumido: 1.000,00 \* 9% = R$ 90,00

Valor da operação após cálculo do crédito presumido = R$ 910,00

**F=Tot.Oper.Lim.Fret./Paut.**

Esta opção considera para base de cálculo do crédito presumido, o valor

total da operação, aplicando o percentual informado no campo Crd. Pres. (F4\_CRDPRES).

Para esta opção o valor do crédito presumido será limitado até o valor do frete da operação, ou

seja, se o valor do crédito presumido for maior que o valor do frete, então o valor será o mesmo

valor do frete e, se não houver frete, o crédito presumido não será calculado. Exemplo de cálculo:

Valor da operação = R$ 1.000,00

Valor de frete da operação =50

Base de cálculo do ICMS = 1.050,00

Percentual no campo Crd. Pres. = 12,20%

Cálculo do Crédito Presumido: 1.050,00 \* 12,20% = R$ 128,10

Valor do crédito presumido = R$ 128,10

Como o valor do crédito presumido foi maior que o valor do frete, por este motivo o valor do crédito presumido será de R$ 50,00 e não de R$ 128,10.

**IMPORTANTE.**

Para esta opção e para o estado de Santa Catarina **(MV\_ESTADO=SC)**, o valor do crédito presumido continuará sendo limitado até o valor do frete da operação, porém, caso a operação seja de pauta, também limitará o valor do crédito presumido pelo valor de pauta de ICMS.

**M=Cred.Val.Merc.**

Esta opção considera para base de cálculo do crédito presumido o valor da

mercadoria da operação, aplicando o percentual informado no campo Crd. Pres. (F4\_CRDPRES).

***Exemplo de cálculo:***

Valor da Mercadoria = R$ 1.000,00

Valor do ICMS-ST = R$ 1.185,00

Base de cálculo do ICMS = R$ 1.185,00

Percentual no campo Crd. Pres. = 7%

Cálculo do Crédito Presumido: 1.000,00 \* 7% = R$ 70,00

Valor do crédito presumido = R$ 70,00

**N=Val.ICMS**

Esta opção considera para a base de cálculo do crédito presumido o valor do ICMS da

operação, aplicando o percentual informado no campo Crd. Pres. (F4\_CRDPRES)

***Exemplo de cálculo:***

Valor da Mercadoria = R$ 1.000,00

Base de cálculo do ICMS = R$ 1.000,00

Valor do ICMS = R$ 180,00

Percentual no campo Crd. Pres. = 7%

Cálculo do Crédito Presumido: 180,00 \* 7% = R$12,60

Valor do crédito presumido = R$12,60

3 - Na aba outros do TES , verifique o campo F4\_AGREGCP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29275107254039)

= Sim, o valor do credito presumido é somado ao total da nota fiscal

= Não, o valor do credito presumido não é somado ao total da nota fiscal
