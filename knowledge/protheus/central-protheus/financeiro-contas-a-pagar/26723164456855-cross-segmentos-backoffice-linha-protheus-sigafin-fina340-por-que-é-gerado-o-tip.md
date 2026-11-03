---
article_id: 26723164456855
category: Financeiro - Contas a Pagar
content_hash: 4db43d9a92c03c92394d4a3a5f7089e5157342eca283d8dd2cc7a85b0695a3a9
fetched_at: '2026-06-28T22:38:09.682883+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA340 - Por que é
  gerado o tipo DIC e exemplo no momento da compensação de contas a pagar
type: support-article
updated_at: '2026-01-02T17:19:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26723164456855-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA340-Por-que-%C3%A9-gerado-o-tipo-DIC-e-exemplo-no-momento-da-compensa%C3%A7%C3%A3o-de-contas-a-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26723164364567) Tempo aproximado para leitura: **00:15:00 min**  
  
**Dúvida**  
Por que é gerado o tipo DIC e exemplo no momento da compensação de contas a pagar?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro- Todas as versões  
  
**Solução**  
**Exemplo 1**

**1)** **FINA050 Inclusão de Título a pagar** - Crie um título A001 **tipo PA** de valor R$ 10 mil sem impostos (Movimento do **extrato bancário** no valor a pagar de R$ 10 mil)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154167191)](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154167191)

**FINA050 Inclusão de Título a pagar** - Crie um título A002 **tipo NF** de valor R$ 20 mil parametrizado com impostos de **PIS, COFINS e CSLL** para serem gerados no momento da baixa.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723164373015)](https://centraldeatendimento.totvs.com/hc/article_attachments/26723164373015)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154173207)](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154173207)

**2)** **FINA340** - Ao compensar a pagar do tipo **NF** com o **tipo PA**, será gerado:

**PIS** = R$ 65,00

**COFINS** = R$ 300,00

**CSLL** = R$ 100,00

**DIC = R$ 465,00**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154177047)](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154177047)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723164377751)](https://centraldeatendimento.totvs.com/hc/article_attachments/26723164377751)

**3)** **FINA080** **Baixas Manual a Pagar** do tipo: **NF,**  será gerado:

**PIS** = R$ 65,00

**COFINS** = R$ 300,00

**CSLL** = R$ 100,00

Gera uma movimentação bancária a pagar de **R$ 9.535,00**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154193687)](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154193687)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723164382359)](https://centraldeatendimento.totvs.com/hc/article_attachments/26723164382359)

**Qual foi o valor pago pela empresa?**

 - Foram **R$ 10 mil** referente ao inclusão do **tipo PA** (referente ao **passo 1)**  
 - Será feito os pagamentos dos impostos de **PIS, COFINS e CSLL** totalizando **R$ 465,00** (referente ao **passo 2)**

 - A **baixa parcial** do **tipo NF**, gerado uma movimentação bancária a pagar no valor de **R$ 9.535,00** (referente ao **passo 3)**

 - Será feito os pagamentos dos impostos de **PIS, COFINS e CSLL** totalizando **R$ 465,00** (referente ao **passo 3)**

 - Totaliza um valor pago de **R$ 20.465,00**, sendo que o valor da **nota fiscal (tipo NF)** é de **R$ 20.000,00**

 - Logo foi pago o valor **R$ 465,00 a mais**, e por esse motivo foi gerado o **tipo DIC** que será um crédito que a empresa possui junto ao fornecedor.

A empresa poderá utilizar o **tipo DIC** para compensar com uma outras notas ou solicitar o dinheiro de volta  através da rotina **FINA080 - Baixa Manual a Pagar** com o motivo de baixa **DEBITO CC**  onde o sistema irá fazer uma movimentação contrária (movimentação a receber referente a devolução)

**FINR470 - Extrato Bancário**

Onde foi realizado todas as baixas inclusive o **tipo: DIC** (gera uma entrada de valor)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727619556119)](https://centraldeatendimento.totvs.com/hc/article_attachments/26727619556119)

-----------------------------------------------------------------------------------------------------------------

Como podemos fazer a comparação do cenário acima utilizando a rotina **FINA080 baixa a pagar parcial,** ao invés de utilizar a inclusão do **tipo: PA**?

Como ficaria os pagamentos para um melhor entendimento da geração do tipo DIC?

**Exemplo 2**

**- FINA050 Inclusão de título**

Crie um título A001 **tipo NF** de valor **R$ 20 mil** parametrizado com impostos de **PIS, COFINS e CSLL**  para serem gerados no momento da baixa.

**- FINA080** **Baixas Manual a Pagar** para realizar o pagamento parcial.

Insira o valor de 10 mil no campo "**VALOR PAGO**", automaticamente será recalculado o valor para **R$ 9.535,00** (Movimento do **extrato bancário** no valor a pagar de R$ 9.535,00)

E será gerado os impostos a serem pago

**PIS** = R$ 65,00

**COFINS** = R$ 300,00

**CSLL** = R$ 100,00

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723164397335)](https://centraldeatendimento.totvs.com/hc/article_attachments/26723164397335)

**Importante:**   
Para que o sistema altere automaticamente o valor inserido no campo "**VALOR PAGO**" para o líquido, será necessário ter o conteúdo no parâmetro **MV\_BP10925 = 2 Valor líquido**

**MV\_BP10925  Define se deve considerar no valor de pagamento, o valor bruto da baixa parcial ou o valor liquido considerando os impostos.(1=Vl Bruto/2=Vl Liquido)**

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154213271)**](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154213271)

**3) FINA080** **Baixas Manual a pagar**:

Realize a segunda baixa.

No campo **"VALOR PAGO**" será gerado o valor de **R$ 9.535,00** (movimento do banco)

E será gerado os impostos a serem pagos

**PIS** = R$ 65,00

**COFINS** = R$ 300,00

**CSLL**= R$ 100,00

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154217495)](https://centraldeatendimento.totvs.com/hc/article_attachments/26723154217495)

**Qual foi o valor pago pela empresa?**

 - Foi **R$ 9.535,00** referente a baixa parcial   
 - Será feito os pagamentos dos impostos de **PIS, COFINS e CSLL** totalizando **R$ 465,00**

 - Realize a segunda baixa, será gerado uma **movimentação bancária** a pagar no valor de **R$ 9.535,00** referente ao baixa total da **NF.**

 - Será feito os pagamentos dos impostos de **PIS, COFINS e CSLL** totalizando **R$ 465,00**

 - Totalizando um valor pago de **R$ 20.000,00**

**FINR470 - Extrato Bancário**

Onde foi realizado todas as baixas

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727619568535)**](https://centraldeatendimento.totvs.com/hc/article_attachments/26727619568535)

**Segue mais exemplo de geração do tipo:DIC**

[FIN0053\_FINA340\_Compensação do tipo:PA com tipo:NF com impostos distintos e criação do tipo DIC](https://tdn.totvs.com/pages/releaseview.action?pageId=354465728)

Cenário como parametrizações

CENÁRIO LÍQUIDO  
MV\_PABRUTO = 2 (Líquido)  
MV\_COMPCP = .T.  
MV\_BP10925 = 2  
MV\_PAPRIME = 1

e

CENÁRIO BRUTO

MV\_PABRUTO = 1 (Bruto)  
MV\_BP10925 = 1  
MV\_PAPRIME = 2

**Sabia mais:**

- [FIN0053\_FINA340\_Compensação do tipo:PA com tipo:NF com impostos distintos e criação do tipo DIC](https://tdn.totvs.com/pages/releaseview.action?pageId=354465728)

[- Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA340 - Configuração dos parâmetros utilizados na Compensação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019492591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Configura%C3%A7%C3%A3o-dos-par%C3%A2metros-utilizados-na-Compensa%C3%A7%C3%A3o)

[- Compensação contas a pagar - FINA340 - Financeiro P12 - Mais exemplos do tipo DIC](https://tdn.totvs.com/pages/releaseview.action?pageId=504794483#Compensa%C3%A7%C3%A3ocontasapagarFINA340FinanceiroP12-04.PAR%C3%82METROSAPLICADOS)
