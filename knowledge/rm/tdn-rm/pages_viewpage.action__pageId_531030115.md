---
content_hash: d09433457a8e021b15e0f60563035c2448d34e0793d4290e71a35a08e515c258
fetched_at: '2026-06-29T00:10:36.159576+00:00'
page_id: '531030115'
product: rm
source: tdn-rm
title: Regra para Lançamento Dentro ou Fora da Conta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531030115
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Parâmetro Geral**

## **01. VISÃO GERAL**

Nesta função definimos se o lançamento do item para determinado Prestador / Convênio será dentro ou fora da conta.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao incluir algum item de Honorário ou Diagnose e Terapia na Elaboração da Conta no nome do prestador, o sistema irá marcar o item como dentro ou fora da conta através das seguintes formas:

1) Configurando uma regra através da tela **Cadastros > Faturamento > Outros Cadastros >** **Regras de Lançamento Dentro ou Fora da Conta**, preenchendo os campos conforme necessidade.

2) Configurando o credenciamento do prestador através tela **Cadastro > Uso Geral > Prestador > Credenciamento**, informando no campo **Credenciamento** uma das opções abaixo:

* **Direto:**  Quando o Prestador em questão possuir credenciamento direto ao Convênio, o sistema irá marcar o lançamento do item como fora da conta se o parâmetro abaixo estiver marcado.   
  **Vale lembrar que essa regra não vale para o prestador principal da unidade de atendimento. Todo lançamento em nome do prestador principal é dentro da conta.**
* **Indireto:** Quando o Prestador em questão não possuir o credenciamento no Convênio, o sistema irá marcar o lançamento do item como dentro da conta.

3) Caso nenhum dos cadastros acima esteja feito, ainda assim é possível deixar o item como dentro ou fora da conta, para deixar como fora da conta, deverá ser pressionado o botão F**ora da conta** no momento da sua inclusão.

Mesmo com essas regras, caso o usuário escolha alterar o campo "Fora da Conta", o sistema salva conforme escolhido.
