---
article_id: 4412912728599
category: MDFe - Manifesto de Carga
content_hash: 680ac049ca9eab4b99d02c3a141d2642e90f4cdd2ed4078dc48d75c386be6ef1
fetched_at: '2026-06-28T22:40:08.249289+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - 725 Rejeição:
  Grupo produto predominante deve ser informado para modal rodoviário'
type: support-article
updated_at: '2025-06-17T17:49:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412912728599-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-725-Rejei%C3%A7%C3%A3o-Grupo-produto-predominante-deve-ser-informado-para-modal-rodovi%C3%A1rio
---

**Dúvida**Como solucionar a rejeição abaixo:

725 Rejeição: Grupo produto predominante deve ser informado para modal rodoviário ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

Se modal rodoviário e Tipo Emitente for igual a ***Prestador de Serviço de Transporte (tpEmit=1)*** ou transportador que emitirá ***CT-e globalizado (tpEmit=3)*** ou Transportador Próprio que informou o Tipo de Transportador ***(tpEmi=2 com tag tpTransp informada)***, o grupo produto predominante deve estar informado ***(grupo: prodPred)***

1. Para gerar o **Produto predominante no MDF-e** realizar o procedimento abaixo:

A primeira maneira de preencher os dados do produto predominante é através do campo **Produto** presente na aba **Produto Predominante**. Ao informar o produto serão preenchidos automaticamente os campos **Descrição do produto**, **Código NCM**, **Cód. de Barras (GTIN)**. Os campos **Tipo de Carga**, **CEP Carregamento**, **CEP Descarregamento** não serão preenchidos automaticamente, sendo esses necessário preenchimento manual.

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_17-39-39.png?version=1&modificationDate=1624221580100&api=v2)

2. A segunda maneira de preenchimento dos dados do produto é através da rotina **Outras Ações / Produto Predominante**, que irá apresentar uma tela de seleção com os 10 produtos com maior quantidade (somatório das quantidades) de todos os produtos dos documentos selecionados na aba **Documentos.** 

**![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_17-36-21.png?version=1&modificationDate=1624221381410&api=v2)**

3. Para escolha dos produtos é realizada o agrupamento dos produtos de todos os documentos selecionados no MDF-e ,em seguida somados os seus valores totais (D1\_TOTAL/D2\_TOTAL) e são apresentados os 10 primeiros que resultam em maior valor para seleção. Caso não seja exibido o item desejado, o mesmo poderá ser informado manualmente como no procedimento anterior.

**![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-21_12-34-24.png?version=1&modificationDate=1624289664963&api=v2)**

**![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-21_12-36-38.png?version=1&modificationDate=1624289798417&api=v2)**

**Critério para exibição dos produtos predominantes com base legal:**

Visando esclarecer a correta identificação do produto predominante no MDF-e em operações de Transporte Rodoviário de Carga Lotação, assim entendida à que corresponda a uma única NF-e ou CT-e, com cargas distintas, o emitente deverá atender o disposto no §2° do art. 4° da [**RESOLUÇÃO ANTT Nº 5.867, DE 14 DE JANEIRO DE 2020**](https://www.in.gov.br/en/web/dou/-/resolucao-n-5.867-de-14-de-janeiro-de-2020-238315084), expedida pela Agência Nacional de Transportes Terrestres – ANTT, nos seguintes dizeres:

*“§2° Para o caso de operações de Transporte Rodoviário de Carga Lotação em que sejam transportadas cargas distintas, sujeitas à classificação em mais de um tipo de carga estabelecida no Anexo II desta Resolução, deverá ser considerada aquela que resulte em maior valor”.*

Abaixo serão detalhados os campos presentes na aba **Produto Predominante**:

* **Produto:** Campos apenas para auxiliar (facilitador) na busca do produto exibindo o cadastro de produto para seleção. **Este campo não é gravado e nem enviado a SEFAZ.**
* **Descrição do produto:** Informar a descrição do produto (caso seja utilizado um dos facilitadores, o campo de origem é a Descrição do Produto - B1\_DESC).
* **Tipo de Carga:** Informar o tipo da carga conforme Resolução ANTT nº. 5.849/2019. 01-Granel sólido; 02-Granel líquido; 03-Frigorificada; 04-Conteinerizada; 05-Carga Geral; 06-Neogranel; 07-Perigosa (granel sólido); 08-Perigosa (granel líquido); 09-Perigosa (carga frigorificada); 10-Perigosa (conteinerizada); 11-Perigosa (carga geral).
* **Código NCM:**Código NCM do produto (caso seja utilizado um dos facilitadores, o campo de origem é a NCM do Produto - B1\_POSIPI).
* **Cód. de barras (GTIN):** Informar o GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras (caso seja utilizado um dos facilitadores, o campo de origem é o código de barras do Produto - B1\_CODBAR).
* **CEP de Carregamento:**CEP onde foi carregado o MDF-e. Este campo refere-se a informação da **carga lotação** e deve ser informado somente quando MDF-e for de carga lotação.
* **CEP de Descarregamento:**CEP onde foi descarregado o MDF-e. Este campo refere-se a informação da **carga lotação** e deve ser informado somente quando MDF-e for de carga lotação.

Caso seja selecionado apenas um documento fiscal, obrigatoriamente devem ser informados os campos **CEP de Carregamento** e **CEP de Descarregamento**.

As informações de **produto predominante não são impressas no DAMDFE** padrão do sistema, podendo este ser customizado conforme necessidade do cliente através do RDMake padrão DAMDFE.PRW disponível no portal de downloads da TOTVS.

* **Validação da Sefaz:**

**![725_rejeicao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4412891757975)**
