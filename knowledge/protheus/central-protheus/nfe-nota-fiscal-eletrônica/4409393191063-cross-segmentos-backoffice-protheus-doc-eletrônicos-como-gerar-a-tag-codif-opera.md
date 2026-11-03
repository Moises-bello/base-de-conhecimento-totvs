---
article_id: 4409393191063
category: NFe - Nota Fiscal Eletrônica
content_hash: 4f5b7e5ebb7403dc1c46a9ed74b0dbdf56963946fcbe85e89ce656dbd07c4adb
fetched_at: '2026-06-28T22:40:01.700828+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG
  CODIF - Operações com AEAC'
type: support-article
updated_at: '2021-10-01T20:14:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409393191063--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-CODIF-Opera%C3%A7%C3%B5es-com-AEAC
---

**Dúvida**Como gerar a TAG CODIF - Operações com AEAC ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para habilitar a opção de complemento de **combustível nos Livros Fiscais,** você deverá:  
  
1- Incluir um grupo de produto (**Combustíveis**)  
2- Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO**  
3- Informar o grupo no parâmetro **MV\_COMBUS**  
4- Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS**

**. CDD\_IFCOMP**

**O campo que levará CODIF:**

* **CD6->CD6\_SEFAZ**

* **Saiba mais:**

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada [MATUCOMP](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

Existe a possibilidade do campo CDD\_IFCOMP ser preenchido automaticamente. Para isso é necessário ativar o parâmetro MV\_ATUCOMP e usar o ponto de entrada [MATUCOMP](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

Ocorre a rejeição 660, pois é **obrigatória** a informação do grupo de combustível para os CFOPs constantes no **Anexo XI.02** - CFOP de Combustível e Lubrificantes (**NT 2012/003**)

Para preencher os Complementos de Combustíveis, entrar em **Livros Fiscais -> Movimentos-> NF Manual de saída->Ações Relacionadas->Complemento->Complementos de Combustível** e depois preencher os seguintes campos:

Complemento de combustível, para o **XML** a SEFAZ obriga somente 3 tags, **<cProdANP>** (**Código de produto da ANP**), **<UFCons>** (**Sigla da UF de consumo**) e <descANP> (Descrição do produto conforme ANP).

Após isso, retransmita a nota.

* Segue o link do **parecer da consultoria:**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=641834866)
