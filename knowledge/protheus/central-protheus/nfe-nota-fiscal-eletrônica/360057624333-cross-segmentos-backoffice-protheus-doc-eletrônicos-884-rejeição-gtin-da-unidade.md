---
article_id: 360057624333
category: NFe - Nota Fiscal Eletrônica
content_hash: 97e944372af0feeabb3d7f6f37ce271aa1f73630f810f4c0b3b0017e4868eb71
fetched_at: '2026-06-28T22:40:01.557931+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 884 Rejeição:
  GTIN da unidade tributável (cEANTrib) com prefixo inválido     '
type: support-article
updated_at: '2021-10-11T14:34:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057624333--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-884-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-cEANTrib-com-prefixo-inv%C3%A1lido
---

**Dúvida**Como solucionar a rejeição 884: GTIN da unidade tributável (cEANTrib) com prefixo inválido ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Importante:**

**Ao digitar o código de barras nos campos:**

* B1\_CODGTIN
* B1\_CODBAR
* B5\_2CODBAR

Os campos possuem um gatilho:

* Se tiver 12 deverão ser preenchidos 11 e o gatilho irá preencher o 12.
* Se tiver 13 deverão ser preenchidos 12 e o gatilho irá preencher o 13.
* Se tiver 14 deverão ser preenchidos 13 e o gatilho irá preencher o 14.

* Conforme a nota técnica **2017.001** o código **GTIN-8, GTIN-12, GTIN-13 ou GTIN-14** são os antigos códigos **EAN, UPC e DUN-14.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043870034/mceclip0.png)

No campo B1\_CODGTIN ou B1\_CODBAR ou B5\_2CODBAR **(caso esteja preenchido na SB5 a TAG ceantrib será levada desse campo)**deve ser preenchido o prefixo correto do código de barras que são os três primeiros algoritmos do GTIN

**OBS:** Antes de começar a usar chaves de identificação GS1 e códigos de barras, você precisa de um prefixo da empresa GS1. Este código globalmente exclusivo permite que você comece a usar padrões de identificação GS1.

Os Prefixos da Empresa GS1 são baseados nos Prefixos GS1. Note-se que, uma vez que as empresas membros da GS1 podem fabricar produtos em qualquer lugar do mundo, os Prefixos GS1 não identificam o país de origem de um determinado produto.

* **A lista de prefixos aceitos está disponível no link abaixo:**

[Tabela Prefixo GS1](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=mpYVEbsVRuE=)

 Ao clicar nesse **link acima será aberto um excel**

![GTIN.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006945652/GTIN.PNG)
