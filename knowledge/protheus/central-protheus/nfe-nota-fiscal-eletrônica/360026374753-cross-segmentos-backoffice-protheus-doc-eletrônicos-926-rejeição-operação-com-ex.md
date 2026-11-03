---
article_id: 360026374753
category: NFe - Nota Fiscal Eletrônica
content_hash: f20fc0f9b096c0ead5edbb64642578c12a09fe38cb1cea63027cd8888c1bad9f
fetched_at: '2026-06-28T22:40:03.346181+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  926 Rejeição :
  Operação com Exterior e país de destino igual a Brasil'
type: support-article
updated_at: '2025-08-12T00:35:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026374753-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-926-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-com-Exterior-e-pa%C3%ADs-de-destino-igual-a-Brasil
---

**Dúvida**Como solucionar a rejeição abaixo:

926 Rejeição : Operação com Exterior e país de destino igual a Brasil ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Tag **<UF>** é o Estado da emissão do destinatário

A Tag **<Cpais>** o código do pais do destinatário.

Se a UF for **EX** a TAG **Cpais** deve ser diferente de **1058** (Brasil).

1- Verificar se os cadastros abaixo estão corretos no ***Protheus no cadastro de Cliente* nos *campos* *Estado*** A1\_EST e ***Pais*** A1\_PAIS:

**![A1_EST__A1_PAIS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413550467607)**

**Ou**

2- Verificar se os cadastros abaixo estão corretos no *Protheus no cadastro de Fornecedor* ***nos campos Estado A2\_EST e Pais A2\_PAIS:***

![A2_PAIS_A2_EST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413544602775)

**Importante:**

Os campos ***A1\_PAIS** e **A2\_PAIS*** verificam a tabela ***SYA.***

* **Exemplo:**

***Estados Unidos***

**SYA ->** YA\_CODGI = 249 (deve conter os três primeiros códigos)  
**SYA ->** YA\_SISEXP= 2496 (deve conter os quatro dígitos do código)

* **Há uma tabela disponível no site da Sefaz:**

<http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Iy/5Qol1YbE=>

[Tabela de País - Relacionada a NT 2018.003. v1.00 (atualizada em 04/05/2018)](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hdos6Z3A8Xc=)

* ***Importante:***

Caso utilize o ***SIGAEIC** ou **SIGAECC*** a manutenção da tabela dos países pode ser realizada através da rotina.

Caso realize as notas pelo Compras ou Faturamento será necessário realizar a manutenção na tabela **SYA.**

Consulte a **tabela SYA e verificar se** para esse país deve estar conforme exemplo abaixo:

SYA ->**YA\_CODGI** = 023 **(com os três primeiros dígitos)**

SYA -> **YA\_SISEXP**= 0230**(com os quatro dígitos da SISCOMEX)**

**Caso não**esteja como o exemplo acima, este ajuste deve ser realizado **conforme a documentação abaixo:**

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Cadasto Sigla Paises tabela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040591674) [SYA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040591674)

* **Saiba mais:**

<http://www.bcb.gov.br/rex/Censo2000/port/manual/pais.asp?idpai=CENSOCE>

Caso o código do Pais do seu **destinatário tenha sido excluído**, verificar com a Sefaz como deverá proceder.

* ***Quando é uma Venda presencial para um cliente do Exterior:***

1- Essa nota  deve iniciar o seu CFOP por 5 ou seja **operação interna no TES no campo CFOP F4\_CF;**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34112289970071)**

2 -No cadastro de cliente deve ser **preenchido um documento do estrangeiro** no campo **A1\_PFISICA;**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045273334)

3- E no pedido de venda o tipo do cliente precisa ser consumidor final **C5\_TIPOCLI = F**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046125733)

* **Exemplo das TAGS no XML:**

<indFinal>1</indFinal>

<CFOP>5656</CFOP>

<idEstrangeiro>00000</idEstrangeiro>

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041678293)
