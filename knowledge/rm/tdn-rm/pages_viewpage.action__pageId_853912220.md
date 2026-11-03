---
content_hash: 63f006bc24cbd91d9097b5bb9587bba46ab8c0623018c25c7c75eeb282cd08f7
fetched_at: '2026-06-29T00:11:54.530826+00:00'
page_id: '853912220'
product: rm
source: tdn-rm
title: Nota Técnica 2023.004
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853912220
version: 13
---

Nessa NT, foram criados novos campos no grupo YA. Informações de Pagamento e nos Grupos Tributação do ICMS que possuem ICMS desonerado. Também foram alterados campos dos grupos I01. Produtos e Serviços / Declaração de Importação e Z. Informações Adicionais da NF-e.

# **Conteúdo**

2Conteúdonone

## **01.** **Cronograma**

Esta Nota Técnica entra em vigor a partir de:

* Homologação a partir de **25/03/2024**.

* Produção a partir de **01/07/2024**.

## **02.** **Legislação**

Este documento foi elaborado com base na [Nota Técnica 2023.004 - v.1.11](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=) disponível no portal da NF-e.

## **03. Versões**

As alterações estão disponíveis a partir das versões abaixo.

* 12.1.2406.107
* 12.1.2402.175
* 12.1.2310.230
* 12.1.2306.278

## **04.** **Alterações**

Foi incluído a tag "**indDeduzDeson**" para a Tributação do ICMS nos CST(s) 20, 30, 40, 41, 50 e 70

icms201ICMS 20

### **ICMS 20**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação |
| 192.4 | N28b | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E | N27.1 | N | 0-1 | 1 | O campo só pode ser preenchido com:  0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e.  1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e.  **Este campo será gerado conforme as regras definidas no mapeamento de campos do grupo**  **Grupo Tributação do ICMS= 20** |

#### **Exemplo de XML**

Tag "**indDeduzDeson**" = 1. Esta situação ocorre quando a Opção "**ICMS Desonerado Não Afeta Valor Contábil**" na Regra de ICMS estiver **desmarcada**.

Exemplo
    
        0
        20
      {...}
        30.00
        9
        1
    
]]>

Tag "**indDeduzDeson**" = 0. Esta situação ocorre quando a Opção "**ICMS Desonerado Não Afeta Valor Contábil**" na Regra de ICMS estiver **marcada**.

Exemplo
    
        0
        20
      {...}
        30.00
        9
      0
    
]]>2ICMS 30

### ICMS 30

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação |
| 201.4 | N28b | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E | N27.1 | N | 0-1 | 1 | O campo só pode ser preenchido com:  0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e.  1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e.  **Este campo será gerado conforme as regras definidas no mapeamento de campos do grupo** |

#### **Exemplo de XML**

Tag "**indDeduzDeson**" = 1. Esta situação ocorre quando a Opção "**ICMS Desonerado Não Afeta Valor Contábil**" na Regra de ICMS estiver **desmarcada**.

Exemplo
    
        0
        30
      {...}
        30.00
        9
        1
    
]]>

Tag "**indDeduzDeson**" = 0. Esta situação ocorre quando a Opção "**ICMS Desonerado Não Afeta Valor Contábil**" na Regra de ICMS estiver **marcada**.

Exemplo
    
        0
        30
      {...}
        30.00
        9
      0
    
]]>3ICMS 40, 41, 50

### ICMS 40,41,50

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação |
| 204.03 | N28b | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E | N27.1 | N | 0-1 | 1 | O campo só pode ser preenchido com:  0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e.  1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e.  **Este campo será gerado conforme as regras definidas no mapeamento de campos do grupo** |

#### **Exemplo de XML**

Tag "**indDeduzDeson**" = 1. Esta situação ocorre quando a Opção "**ICMS Desonerado Não Afeta Valor Contábil**" na Regra de ICMS estiver **desmarcada**.

Exemplo
    
        0
        40
      {...}
        30.00
        9
        1
    
]]>

Tag "**indDeduzDeson**" = 0. Esta situação ocorre quando a Opção "**ICMS Desonerado Não Afeta Valor Contábil**" na Regra de ICMS estiver **marcada**.

Exemplo
    
        0
        40
      {...}
        30.00
        9
      0
    
]]>4ICMS 70

### ICMS 70

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação |
| 231.4 | N28b | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E | N27.1 | N | 0-1 | 1 | O campo só pode ser preenchido com:  0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e.  1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e.  **Este campo será gerado conforme as regras definidas no mapeamento de campos do grupo** |

#### **Exemplo de XML**

Tag "**indDeduzDeson**" = 1. Esta situação ocorre quando a Opção "**ICMS Desonerado Não Afeta Valor Contábil**" na Regra de ICMS estiver **desmarcada**.

Exemplo
    
        0
        70
      {...}
        30.00
        9
        1
    
]]>

Tag "**indDeduzDeson**" = 0. Esta situação ocorre quando a Opção "**ICMS Desonerado Não Afeta Valor Contábil**" na Regra de ICMS estiver **marcada**.

Exemplo
    
        0
        70
      {...}
        30.00
        9
      0
    
]]>
