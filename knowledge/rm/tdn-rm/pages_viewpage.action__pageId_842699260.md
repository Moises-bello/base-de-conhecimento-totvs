---
content_hash: bb6f893f474664b7deb91b9c863694cff628aece80e8d9f45337269456995206
fetched_at: '2026-06-29T00:11:50.564875+00:00'
page_id: '842699260'
product: rm
source: tdn-rm
title: Parâmetros Rotina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=842699260
version: 24
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>trueAVISO

Esta funcionalidade está em desenvolvimento e será disponibilizada em breve.

## **01. Introdução**

Neste anexo será informado os Parâmetros que serão utilizados na Geração das Rotinas Fiscais.

## **02. Tela para inclusão dos valores Chave, Valor e Descrição**

## **03. Campos**

* O campo **Chave** se refere ao Nome do campo no Layout do gerador de saídas.
* O campo **Valor** se refere ao Valor do campo no Layout do gerador de saídas.
* O campo **Descrição** se refere a descrição do campo no Layout do gerador de saídas.
* O campo **Chave Contexto** será incluído apenas pelo "Processo Parâmetros da Rotina", de Importação dos Parâmetros do Layout. Este Campo será utilizado para Preencher a Classe dos Parâmetros na Central de Rotinas.

## **04. Regras**

### Regras Gerais

* A configuração dos parâmetros da rotina é realizada incluindo os campos "Chave" e "Valor" no cadastro. O campo chave é a referencia dos campos dos parâmetros da rotina, e o campo valor é o conteúdo do campo.
* O time de desenvolvimento irá disponibilizar o campo chave e valor para configuração conforme necessidade específica das rotinas fiscais.

### Regras Específicas

* Para apuração do PIS/COFINS é necessário cadastrar dois parâmetros chaves **APURACAO\_PIS** e **APURACAO\_COFINS.**
* Com as "Chaves" criadas, o campo "Valor" de cada um deverá ser preenchido com o código do tributo que deve ser igual ao Código do Tributo do Período de Apuração.

  Exemplo da Configuração dos Parâmetros de RotinaObservaçãoO campo "Valor" deve ser igual ao Código do Tributo do Período de Apuração que se deseja fazer os Cálculos da Consolidação PIS/COFINS.
