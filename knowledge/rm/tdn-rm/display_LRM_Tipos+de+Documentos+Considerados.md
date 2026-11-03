---
content_hash: 5d67a569227204b610fd350501bd40afef39e2d6192c60d03d3174fdd45a9720
fetched_at: '2026-06-29T00:10:56.888037+00:00'
page_id: '593264241'
product: rm
source: tdn-rm
title: Tipos de Documentos Considerados
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipos+de+Documentos+Considerados
version: 19
---

## **01. Modelo de Documento**

Deverá ser criado um filtro de Operação para cada Modelo de Documento desejado.

0Identificação

Para Cada Modelo de Documento é possível definir algumas configurações para customizar o comportamento do Filtro

1leftTipo OperaçãoOperaçãoBase de CálculoData Opcional de Filtro

**Regras:**

* Neste campo serão listadas as Datas configuradas no Módulo Financeiro

  Imagem

  Acesse TOTVS Gestão Financeira |  Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a pagar | Lançamento | Datas opcionais

**Regras:**

* Não será permitida a inclusão de outro filtro que possua o mesmo "Tipo de documento" de um filtro já existente.
* Os campos Tipo de Operação e Natureza da BC de Crédito é exibido apenas quando é o registro F100
Filtro Tributo

Após salvar o Filtro, ficará disponível a aba "Filtro Tributo".

TribIdentificaçãoIdentificação

Na Aba "Identificação" deve ser informado o Tributo e o CST relacionado ao Modelo de Documento escolhido

Caso o parâmetro Base de Cálculo esteja preenchido com a opção "Utiliza Formula" na pasta identificação, será habilitado o campo para preenchimento da Fórmula

Registro 1900

Após realizar a parametrização do registro F500 deve ser definida a geração do registro 1900, que pode ser gerado a partir do "Valor Original":

Ou a partir da opção Utiliza Formula

**Regras:**

* A configuração do Registro 1900 ficará disponível somente para o cadastro relacionado ao Registro F500

## **02. Outras informações**
