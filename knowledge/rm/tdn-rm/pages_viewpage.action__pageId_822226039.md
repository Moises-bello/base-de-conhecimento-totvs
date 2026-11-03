---
content_hash: 3d9a01ed35a7ad2c3ad87b52855205d486d630260fc286a3f2a85fed12ebb702
fetched_at: '2026-06-29T00:11:45.927145+00:00'
page_id: '822226039'
product: rm
source: tdn-rm
title: Parâmetros do Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822226039
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Cadastro de Parâmetros do Convênio**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Ao término de todos os cadastros anteriores, o próximo passo será efetuar a associação dos convênios criados com seus possíveis serviços, informar qual a porcentagem do valor que a empresa irá assumir e além de adicionar informações para cálculo das parcelas.

Nesse cadastro será registrado as modalidades de tipos de convênios que o funcionário pode realizar, junto a instituições conveniadas e tê-las descontadas parceladamente ou não em folha de pagamento. A empresa pode assumir um percentual no pagamento do que foi comprado. Este é um tipo de benefício que o funcionário possui, na compra de remédio e itens semelhantes.

## **02. EXEMPLO DE UTILIZAÇÃO**

Incluir / Editar / Excluir

De acordo com a imagem, os campos foram separados em dois grupos, sendo eles:

1)   Grupo 1 - Associação do convênio com seu serviço disponibilizado, além de informar o código da filial em que ficará disponível e o código de evento que será utilizado para efetuar o lançamento do desconto no envelope do funcionário.

2)   Grupo 2 - Será necessário optar pela Forma de parcelamento, onde:

* **Parcelamento fixo** – O campo “Nº limite de parcela” irá ficar disponível, permitindo assim que faça a inclusão de uma quantidade de parcelas limites.

* **Não limitar parcelas** – Não poderá limitar a quantidade de parcelas, sendo necessário assim informar esse valor ao cadastrar o movimento de convênio do funcionário.

* **Utilizar tabela de calcula** – O parcelamento irá ser calculado de acordo com a tabela de cálculo, para maiores explicações verifique o tópico **Movimentação de Convênio dos Funcionários**.

Após informar qual será a “Forma de pagamento”, deverá preencher qual o valor do percentual que a empresa irá cobrir para esse serviço de convênio, como também qual será a quantidade limite de parcelas e a vinculação da tabela de cálculo.

Dica

Lembrando que para os dois últimos itens citados (Limite de parcelas e tabela de cálculo), a disponibilidade de preenchimento se dará de acordo com a “Forma de pagamento”.

## **03.** **TELA Cadastro de Parâmetros do Convênio**

## ****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Identificador | Valor preenchido por default |
| Código da filial | Código da filial |
| Código do convênio | Código do convênio |
| Código do serviço do convênio | Código do serviço do convênio |
| Código do evento | Código de evento que será utilizado para efetuar o lançamento do desconto no envelope do funcionário |
| Forma de parcelamento | Selecionar a forma de pagamento |
| % Empresa | Caso a empresa decida arcar com alguma parte do convênio, exemplo 60% do valor do convênio será custeado pela empresa |
| Tabela de Cálculo para limite de desconto por parcela | Se a forma de parcelamento for 'Utilizar a tabela de cálculo' este campo será habilitado para o cadastro do código da tabela |
| Nº limite de parcelas | Se a forma de parcelamento for 'Parcelamento fixo' este campo será habilitado para o cadastro do número de parcelas |

## **04. TABELAS UTILIZADAS**

* PCONVENIOPARAM
