---
content_hash: 8e674bbb523f3cd50a442afb02d690aa78f54c0c38bdd20b5e42f87f2d591546
fetched_at: '2026-06-29T00:12:10.076133+00:00'
page_id: '949425241'
product: rm
source: tdn-rm
title: Geração das tags cEAN, cEANTrib e uTrib- Código de Barras e Unidade e Medida
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=949425241
version: 15
---

**Introdução:**

Este Documento auxilia na parametrização para o envio de Notas Fiscais Eletrônicas preenchendo a tag <cEAN>, <uTrib> e <cEANTrib>, que se referem ao código de barras  e a Unidade de Medidas do produto.

LayoutOperações para o Estado e Outros Estados

**1º Passo:**

Inicialmente deve-se habilitar o parâmetro para utilizar o código de barras. Para habilitá-lo acesse o menu: Opções | Parâmetros | RM Núcleos | Parâmetros Gerais | Tabelas | [04.01.04.07] Produtos| etapa “**8 – Lote**“. Preencha o campo “**Usa códigos EAN**”.

  

**OBS: Não é obrigatório o preenchimento do código EAN para todos os itens. Verifique a necessidade dos produtos da empresa e selecione a opção adequada a sua necessidade.**

Após parametrização acessem o cadastro do produto, onde estará disponível a aba “**código de Barras**”, onde devera ser preenchido o código de barras.

( Neste exemplo, cadastramos uma unidade de controle “Unidade “ e uma unidade de venda “ Caixa”)

Para o correto preenchimento da tag <cEAN> e <cEANTRIB>, devera ser cadastrado um código de barras para a unidade de controle utilizada para cada produto e uma unidade de venda para cada produto. Caso a unidade de venda e controle seja a mesma, devera ser informado apenas uma.

Caso a unidade de medida comercial seja diferente da unidade de medida tributável (que será informada no XML da nota), será necessário informa seu valor no campo da Unidade de Medida Tributável, conforme imagem abaixo:

( Neste exemplo, cadastramos uma a unidade "KG" como unidade tributável de “Caixa”)

Na aba “**Controle Estoque** “, deverá ser preenchido a **UNIDADE DE CONTROLE A SER TRIBUTADA**. Esta unidade será verificada no preenchimento da tag <cEANTrib>, onde o sistema verificará a unidade preenchida e levará o código de barras referente a ela.

( Neste exemplo, foi utilizado a unidade de controle tributável como “unidade”, assim no XML, a tag <cEANTrib> receberá o código EAN que cadastramos para a unidade de controle “ UNIDADE “, no caso “78900000245678”)

**2º Passo**

Na inclusão do item no movimento, preencha a unidade de medida a ser utilizada, pois no XML, na tag <cEAN> será preenchido o código EAN cadastrado no produto referente a unidade selecionada.

( Neste exemplo, vamos utilizar a unidade “ Caixa “. No XML será levado na tag <cEAN> o código cadastrado para a unidade “CAIXA”, no caso “78946513245678”).

Ao realizar o envio da NF-E, podemos visualizar as informações do código de barras da nota na tag <cEAN> e <cEANTRIB>, conforme imagem:

Se na inclusão do movimento for utilizada uma unidade de movimentação “unidade” do produto, o XML ficará da seguinte forma:

**Observações:**

* **Lembrando que para ser um código de barras válido para o XML, o mesmo deverá conter os seguintes tamanhos:**

**GTIN – 8**

**GTIN – 12**

**GTIN – 13**

**GTIN – 14**

* **Caso não esteja nos tamanhos corretos, a tag será gerada vazia.**
* **O numero “0” a esquerda, não são considerados como digito valido.**
Operações para Comércio Exterior

Para atender exigências da Sefaz (como tabela NCM), é necessário informar uma unidade de medida específica e o Código de Barras na nota fiscal. Podem ocorrer casos em que a unidade de medida de controle do estoque nacional não seja compatível com a unidade de medida exigida pela tabela NCM para comércio exterior.

EXEMPLO:

Supondo que seu produto pertença ao NCM: 02021000 e que suas unidades cadastradas sejam as seguintes:

Para o NCM 02021000, em operações de comércio exterior, a Sefaz exige que sua unidade de medida tributável seja 'KG'. Mas no caso acima, não podemos simplesmente cadastrar a Unidade 'KG' com um novo Código de Barras, pois isso causaria problemas no controle de estoque.

Para tornar esse cenário possível de envio sem ocasionar rejeições, será necessário informar os campos Unidade de Medida e Código de Barras referente ao grupo Exterior no cadastro do produto:

Não é obrigatório o preenchimento dos campos para todos os produtos. Verifique a necessidade dos produtos da empresa e preencha a opção adequada a sua necessidade.

Os valores informados nos campos Código de Barras e Unidade Tributável dentro do grupo Exterior, serão levados para o XML e exibidos nas TAG <EANTrib> e  <uTrib> no grupo I - Produtos e Serviços da NF-e.

Lembrando que estes campos seguirão as regras de tamanho e quantidade definidos no manual do contribuinte.
