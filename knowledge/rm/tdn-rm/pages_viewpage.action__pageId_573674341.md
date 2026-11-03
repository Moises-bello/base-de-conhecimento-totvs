---
content_hash: 53fae1f14c24fcc1c496ba2611a630aac1e05bf873329d3f034c28048d240b2b
fetched_at: '2026-06-29T00:10:52.981115+00:00'
page_id: '573674341'
product: rm
source: tdn-rm
title: Validações TISS - Honorários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=573674341
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Para cada item de Honorário em um atendimento, as seguintes validações são feitas:

* O prestador executante é validado da mesma forma que os prestadores responsável e solicitante.
* Procura a tabela ANS usada. Se não for encontrada, um erro é retornado com a mensagem 'Item XXXX não está com a definição da tabela na ANS. Acesse o cadastro de Tabelas de Preços Usadas e faça a correlação com ANS.'.
* Caso o atendimento tenha uma guia com o Tipo de Nota Uni Bh = Guia de Honorário individual, o sistema verifica se existe mais de um prestador entre os lançamentos, retornando 'Guia de Honorário Individual não pode conter lançamentos para mais de um prestador.'.
* Caso não contenha o CBO para a versão TISS, um erro é retornado com a mensagem 'Não foi identificado o CBO para versão do padrão TISS. Código: XXXX Versão: XXXX. Altere o CBO no lançamento'.
* Caso conter Técnica Utilizada informada e não for compatível com a versão TISS, é retornado 'A técnica XXXX do procedimento XXXX esta incompatível com a versão XXXX do padrão TISS - ANS.'

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

## **03. TABELAS UTILIZADAS**

* SZATENDHONORARIO
* SZATENDAUTORIZ
* SZCONDCONTRAT
* SZANSCBO
* SZANSTECNICA
]]>
