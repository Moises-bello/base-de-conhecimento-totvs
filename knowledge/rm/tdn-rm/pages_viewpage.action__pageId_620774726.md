---
content_hash: 93f85b634674c5aca2ffd0cbbb3024450cdca3b2b2fb573da2a6e7330bdf1aef
fetched_at: '2026-06-29T00:11:03.320618+00:00'
page_id: '620774726'
product: rm
source: tdn-rm
title: Evento S-1200 - Múltiplos Vínculos para Autônomo Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=620774726
version: 35
---

false

**A partir das Versões**

* 12.1.29.259
* 12.1.31.165
* 12.1.32.106
* e Superiores.

# Objetivo:

---

O objetivo deste documento é trazer informações de como enviar o evento S-1200 (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social)  para Autônomo Externo que possui Múltiplos Vínculos .

---

Passos para envio das informações para o eSocial:

### **Passo 1**

É necessário executar o Atualizador para criação da tabela PPAGTOAUTONOMOEXTMV e ajuste de campos na tabela PPAGTOAUTONOMOEXT.

### **Atenção:**

Caso antes da execução do atualizador exista autônomo com os campos: CNPJREMUNOUTREMPR, CODCATEG, VALORINSSOUTROEMPREGO da tabela PPAGTOAUTONOMOEXT preenchido, esses valores serão migrados para a nova tabela PPAGTOAUTONOMOEXT, isso foi necessário para atender situação onde existe mais de um vinculo para o autônomo. 

### **Passo 2**

Preencher a tabela PPAGTOAUTONOMOEXT  e  PPAGTOAUTONOMOEXTMV através de [importação](https://tdn.totvs.com/pages/viewpage.action?pageId=543064647), [webservice](https://tdn.totvs.com/pages/releaseview.action?pageId=425459227), conceito, etc. 

      Exemplo:

Dados na tabela PPAGTOAUTONOMOEXT

Informações dos autônomos registrados em outros sistemas.

* CATEGORIAESOCIAL: 701-Contribuinte individual - Autônomo em geral, exceto se enquadrado em uma das demais categorias de contribuinte individual
* VALORBRUTO: 2000,00
* VALORIRRF: 200,00
* VALORINSS: 220,00
* INDMV: 1

Acessar o menu Encargos | Autônomos Externos para visualizar as informações caso necessário: 

 

       

Dados na tabela PPAGTOAUTONOMOEXTMV

Informações dos dados de Múltiplos Vínculos dos autônomos externos.

Vinculo empregatícios 1:

* CNPJREMUNOUTREMPR: 77604422000109
* CODCATEG: 701
* VALORINSSOUTROEMPREGO: 3000,00

Vinculo empregatícios 2:

* CNPJREMUNOUTREMPR: 65660458000112
* CODCATEG: 701
* VALORINSSOUTROEMPREGO: 1000,00

### **Passo 3**

* No parametrizador deve existir eventos previamente cadastrados para serem informados no eSocial.

**Passo 4 -** Gerar os XML dos eventos periódicos S-1200 - Remuneração do Trabalhador da seguinte forma:

**Observação:**

Informações sobre a integração de dados e pagamento de autônomos acesse o link: [Integração de dados e Pagamento de Autônomos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=527858150)
