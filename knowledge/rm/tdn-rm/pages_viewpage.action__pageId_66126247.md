---
content_hash: c978f2507747c0f85f856c79e0dcd1c888e998409e5821e762c4a39a5c84804f
fetched_at: '2026-06-29T00:11:13.450436+00:00'
page_id: '66126247'
product: rm
source: tdn-rm
title: NF-e - Gerar TAG cEAN e cEANTrib – Código de barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66126247
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***apartir 11.40* |
| **Processo** | **:** | Gerar TAG cEAM e cEANTrib - Código de barras |
| **Subprocesso** | **:** | Gerar TAG cEAM e cEANTrib - Código de barras |
| **Data da publicação** | **:** | 09/07/2013 |

**Introdução:**

Este Documento auxilia na parametrização para o envio de Notas Fiscais Eletrônicas preenchendo a tag <cEAN> e <cEANTrib>, que se refere ao código de barras do produto.

**1º Passo:**

Inicialmente deve-se habilitar o parâmetro para utilizar o código de barras. Para habilitá-lo acesse o menu: Opções | Parâmetros | RM Nucleus | Parâmetros Gerais | Tabelas | [04.01.04.07] Produtos| etapa “**8 – Lote**“. Preencha o campo “**Usa códigos EAN**”.

**OBS: Não é obrigatório o preenchimento do código EAN para todos os itens. Verifique a necessidade dos produtos da empresa e selecione a opção adequada a sua necessidade.**

Apos parametrização acessem o cadastro do produto, onde estará disponível a aba “**código de Barras**”, onde devera ser preenchido o código de barras.

Para o correto preenchimento da tag <cEAN> e <cEANTRIB>, devera ser cadastrado um código de barras para a unidade de controle utilizada para cada produto e uma unidade de venda para cada produto. Caso a unidade de venda e controle seja a mesma, devera ser informado apenas uma.

( Neste exemplo, cadastramos uma unidade de controle “Unidade “ e uma unidade de venda “ Caixa”)

**OBS: Lembrando que para ser um código de barras válido para o XML, o mesmo deverá conter os seguintes tamanhos:**

**GTIN – 8**

**GTIN – 12**

**GTIN – 13**

**GTIN – 14**

**Caso não esteja nos tamanhos corretos, a tag será gerada vazia.**

**O numero “0” a esquerda, não são considerados como digito valido.**

Na aba “**Controle Estoque** “, deverá ser preenchido a **UNIDADE DE CONTROLE A SER TRIBUTADA**. Esta unidade será verificada no preenchimento da tag <cEANTrib>, onde o sistema verificará a unidade preenchida e levará o código de barras referente a ela.

**( Neste exemplo, foi utilizado a unidade de controle tributável como “unidade”, assim no XML, a tag <cEANTrib> receberá o código EAN que cadastramos para a unidade de controle “ UNIDADE “, no caso “7890000100020”)**

**2º Passo**

Na inclusão do item no movimento, preencha a unidade de medida a ser utilizada, pois no XML, na tag <cEAN> será preenchido o código EAN cadastrado no produto referente a unidade selecionada.

**( Neste exemplo, vamos utilizar a unidade “ Caixa “. No XML será levado na tag <cEAN> o código cadastrado para a unidade “CAIXA”, no caso “78946513245678”).**

Ao realizar o envio da NF-E, podemos visualizar as informações do código de barras da nota na tag <cEAN> e <cEANTRIB>, conforme imagem:

Se na inclusão do movimento for utilizada uma unidade de movimentação “unidade” do produto, o XML ficará da seguinte forma:

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
