---
article_id: 360026388274
category: NFe - Nota Fiscal Eletrônica
content_hash: 524ce9d475d647ff85ad48fd4100351b37cd005fbe20a75a13aedd0b708ad47e
fetched_at: '2026-06-28T22:40:03.371704+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  932 Rejeição :
  Informada modalidade de determinação da BC da ST como MVA e não informado o campo
  pMVAST'
type: support-article
updated_at: '2025-06-13T12:11:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026388274-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-932-Rejei%C3%A7%C3%A3o-Informada-modalidade-de-determina%C3%A7%C3%A3o-da-BC-da-ST-como-MVA-e-n%C3%A3o-informado-o-campo-pMVAST
---

**Dúvida**Como corrigir a rejeição abaixo:

932 Rejeição : Informada modalidade de determinação da BC da ST como MVA e não informado o campo pMVAST  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe -Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **Importante:**

O ambiente deve estar atualizado com **acumulado do fiscal do link abaixo:**

[Cross Segmentos - Backoffice Protheus - FIS - Atualização do Ambiente Fiscal, Módulo 09 (Livros Fiscais)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615333)

Para a Sefaz ao calcular **ICMS-ST** e utilizar a situação tributária **10, 30, 70, 90, 201, 202 ou 900** é gerada a TAG:

* modBCST **(Modalidade de determinação da BC do ICMS ST)**

**Para a Sefaz**há seis modalidades de determinação de **BC do ICMS ST**:

**0**=Preço tabelado ou máximo sugerido;  
**1**=Lista Negativa (valor);  
**2**=Lista Positiva (valor);  
**3**=Lista Neutra (valor);  
**4**=Margem Valor Agregado (%);  
**5**=Pauta (valor);

**6=**Valor da Operação.

 Quando é utilizada a opção 4 é obrigatório o envio do valor da Margem.

 **Verifique se sua modalidade é 4, 5 ou 6 e configure conforme a necessidade da empresa.**

Para gerar a modalidade de determinação da**BC da ST 4**=Margem Valor Agregado (%);

* Cadastrar uma margem para o calculo:

1. No cadastro de produto preencher para nota de saída a Margem do ICMS-ST da nota no campo:

Solid. Saida  **"B1\_PICMRET"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16836140521495)

ou

No cadastro de produto preencher para nota de entrada a Margem do ICMS-ST da nota no campo:

Solid. Entr. **"B1\_PICMENT"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046342213)

ou

2. Se caso utilizar o cadastro de exceção fiscal preencher o campo:

Margem Lucro **"F7\_MARGEM"**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16836084960663)

3- Para gravar o campo **CD2\_MVA**   na **TES** na aba impostos o campo **Marg. Solid. "F4\_MKPSOL"** deve ser **2 ou 3.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041135614)

* **Exemplo do XML:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041134594)

Ao utilizar opção da BC **da ST= 4**

**A Sefaz exige que seja gerada a TAG:**

* pMVAST **(Percentual da margem de valor Adicionado do ICMS ST)**

 Caso não seja gerada a TAG pMVAST gera a rejeição **932**.

 O conteúdo da TAG **modBCST** é levado do campo **CD2\_MODBC** e o conteúdo da TAG **pMVAST**é levado do campo **CD2\_MVA**

* Para gerar a modalidade de determinação da **BC da ST****5**=Pauta (valor);

Fazer a configuração **conforme o link abaixo:**

[MP - FIS - COMO PREENCHER O CD2\_MODBC = 5 Calculo com pauta ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035336833)

* Para gerar a modalidade de determinação da **BC da ST****6=**Valor da Operação

Se a nota for de **Diferencial de alíquotas com CST 10 ou 30** fazer a configuração abaixo:

[MP - FIS - COMO PREENCHER O CD2\_MODBC = 6 PARA DIFERENCIAL DE ST?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034832354)

* **Exemplo do XML:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045484694)**

* **Importante:**

Caso apresente **falha de Schema** com essa opção realizar atualização dos **Schemas do TSS** do link abaixo:

[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

* Para gerar nota de **complemento de ICMS-ST** **BC da ST****4**=Margem Valor Agregado (%);

Fazer a configuração do link abaixo:

[MP - FIS - Complemento de ICMS ST para Venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018997531)

Além disso:

* Cadastrar uma margem para o calculo:

1. No cadastro de produto preencher para nota de saída a Margem do ICMS-ST da nota no campo:

Solid. Saida  **"B1\_PICMRET"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16836140521495)

ou

No cadastro de produto preencher para nota de entrada a Margem do ICMS-ST da nota no campo:

Solid. Entr. **"B1\_PICMENT"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046342213)

ou

2. Se caso utilizar o cadastro de exceção fiscal preencher o campo:

Margem Lucro **"F7\_MARGEM"**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16836084960663)

3- Para gravar o campo **CD2\_MVA**   na **TES** na aba impostos o campo **Marg. Solid. "F4\_MKPSOL"** deve ser **2 ou 3.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041135614)

* **Exemplo do XML:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047181813)**

* Para gerar nota de **complemento de ICMS-ST** **BC da ST****4**=Margem Valor Agregado (%);

Fazer a configuração do link abaixo:

[MP - FIS - Como emitir nota fiscal Complementar FECP ICMS Próprio e FECP-ST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022285472)

Além disso:

* Cadastrar uma margem para o calculo:

1. No cadastro de produto preencher para nota de saída a Margem do ICMS-ST da nota no campo:

Solid. Saida  **"B1\_PICMRET"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16836140521495)

ou

No cadastro de produto preencher para nota de entrada a Margem do ICMS-ST da nota no campo:

Solid. Entr. **"B1\_PICMENT"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046342213)

ou

2. Se caso utilizar o cadastro de exceção fiscal preencher o campo:

Margem Lucro **"F7\_MARGEM"**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16836084960663)

3- Para gravar o campo **CD2\_MVA**   na **TES** na aba impostos o campo **Marg. Solid. "F4\_MKPSOL"** deve ser **2 ou 3.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041135614)

* **Exemplo do XML:**

![](https://totvssuporte.zendesk.com/attachments/token/MxfKjCuLxQXV9Uph1Nu0JBuEM/?name=inline339483485.png)

* **Validação da Sefaz:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044289594)
