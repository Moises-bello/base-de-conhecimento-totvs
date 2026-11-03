---
article_id: 360026440414
category: NFe - Nota Fiscal Eletrônica
content_hash: a32bd23131fb7a3e4e696bc9a327b3ab167ce5b9268d66d5fdde298de89739ba
fetched_at: '2026-06-28T22:40:03.379562+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  933 Rejeição :
  Informada modalidade de determinação da BC da ST diferente de MVA e informado o
  campo pMVAST'
type: support-article
updated_at: '2025-08-12T00:05:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026440414-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-933-Rejei%C3%A7%C3%A3o-Informada-modalidade-de-determina%C3%A7%C3%A3o-da-BC-da-ST-diferente-de-MVA-e-informado-o-campo-pMVAST
---

**Dúvida**Como solucionar a rejeição abaixo ?

933 Rejeição : Informada modalidade de determinação da BC da ST diferente de MVA e informado o campo pMVAST  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Sefaz espera que **não** seja gerada a TAG ***pMVAST*** para modalidade do ***BC ST diferente de 4:***

* **pMVAST** (Percentual da margem de valor Adicionado do ICMS ST)

 1-Para não gravar o campo **CD2\_MVA**  na **TES** na aba impostos o campo ***Marg. Solid.  F4\_MKPSOL=****1-Nunca***

***![933.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414406847639)***

2- Após isso, ***exclua a nota e gere novamente.***

* ***Saiba mais:***

Para a Sefaz ao calcular ***ICMS-ST*** e utilizar a situação tributária ***10, 30, 70, 90, 201, 202 ou 900*** é gerada a TAG:

* ***modBCST*** **(Modalidade de determinação da BC do ICMS ST)**

**Para a Sefaz**há seis modalidades de determinação de ***BC do ICMS ST**:*

0=**Preço tabelado ou máximo sugerido;**  
1=**Lista Negativa;**  
2=**Lista Positiva;**  
3=**Lista Neutra;**  
4=**Margem Valor Agregado;**  
5=**Pauta;**

6=**Valor da Operação.**

**Ao utilizar as opções:**

0=**Preço tabelado ou máximo sugerido;**  
1=**Lista Negativa;**  
2=**Lista Positiva;**  
3=**Lista Neutra;**  
5=**Pauta;**

6=**Valor da Operação.**

**Importante:**

O conteúdo da ***TAG modBCST*** é levado do campo CD2\_MODBC e o conteúdo da T***AG pMVAST***é levado do campo CD2\_MVA.

* Para gerar a modalidade de determinação da***BC da ST****6=***Valor da Operação

Se a nota for de **Diferencial de alíquotas com CST 10 ou 30** fazer a configuração abaixo:

[MP - FIS - COMO PREENCHER O CD2\_MODBC = 6 PARA DIFERENCIAL DE ST?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034832354)

* Para gerar a modalidade de determinação da**BC da ST****5**=Pauta (valor);

Fazer a configuração **conforme o link abaixo:**

[MP - FIS - COMO PREENCHER O CD2\_MODBC = 5 Calculo com pauta ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035336833)

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042092073)
