---
content_hash: 9983568b323006ac7f3f56225665e20842466bca98c0b339d10698757eab9726
fetched_at: '2026-06-29T00:08:10.048188+00:00'
page_id: '240300830'
product: rm
source: tdn-rm
title: NFE0020_Gerar_TAGS_cEAN_e_cEANTrib_Codigo_de_Barras
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0020_Gerar_TAGS_cEAN_e_cEANTrib_Codigo_de_Barras
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Gerar TAG cEAN e cEANTrib - Código de barras |
| **Passo a passo:** | **Introdução:**  Este Documento auxilia na parametrização para o envio de Notas Fiscais Eletrônicas preenchendo a tag <cEAN> e <cEANTrib>, que se refere ao código de barras do produto.  **Procedimentos:**  Inicialmente deve-se habilitar o parâmetro para utilizar o código de barras.  Para habilitá-lo Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento  | Parâmetros Gerais | Tabelas | [04.01.04.07] Produtos| etapa “**8 – Lote**“. Preencha o campo “**Usa códigos EAN**”.      **OBS: Não é obrigatório o preenchimento do código EAN para todos os itens. Verifique a necessidade dos produtos da empresa e selecione a opção adequada a sua necessidade.**  **Cadastro do produto:** acesse o cadastro do produto, onde estará disponível a aba “**código de Barras**”, Preencha campo "código" com o código de barras do produto.      Para o correto preenchimento da tag <cEAN> e <cEANTRIB>, devera ser cadastrado um código de barras para a unidade de controle utilizada para cada produto e uma unidade de venda para cada produto. Caso a unidade de venda e controle seja a mesma, devera ser informado apenas uma.      ( Neste exemplo, cadastramos uma unidade de controle “Unidade “ e uma unidade de venda “ Caixa”)  **OBS: Lembrando que para ser um código de barras válido para o XML, o mesmo deverá conter os seguintes tamanhos:**  **GTIN – 8**  **GTIN – 12**  **GTIN – 13**  **GTIN – 14**  **Caso não esteja nos tamanhos corretos, a tag será gerada vazia.**  **O numero “0” a esquerda, não são considerados como digito valido.**  Na aba “**Controle Estoque** “, deverá ser preenchido a **UNIDADE DE CONTROLE A SER TRIBUTADA**. Esta unidade será verificada no preenchimento da tag <cEANTrib>, onde o sistema verificará a unidade preenchida e levará o código de barras referente a ela.      **( Neste exemplo, foi utilizado a unidade de controle tributável como “unidade”, assim no XML, a tag <cEANTrib> receberá o código EAN que cadastramos para a unidade de controle “ UNIDADE “, no caso “7890000100020”)**  **Item de movimento:** Na inclusão do item no movimento, preencha a unidade de medida a ser utilizada, pois no XML, na tag <cEAN> será preenchido o código EAN cadastrado no produto referente a unidade selecionada.      **( Neste exemplo, vamos utilizar a unidade “ Caixa “. No XML será levado na tag <cEAN> o código cadastrado para a unidade “CAIXA”, no caso “78946513245678”).**  Ao realizar o envio da NF-E, podemos visualizar as informações do código de barras da nota na tag <cEAN> e <cEANTRIB>, conforme imagem:      Se na inclusão do movimento for utilizada uma unidade de movimentação “unidade” do produto, o XML ficará da seguinte forma: |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
