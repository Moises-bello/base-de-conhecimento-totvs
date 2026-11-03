---
content_hash: d08677503e3ae9147634a739f9b6e5c042ccd926b9eb6ddc296c1027e852cd9b
fetched_at: '2026-06-29T00:12:16.344621+00:00'
page_id: '985664091'
product: rm
source: tdn-rm
title: Valorização Material e Medicamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=985664091
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
   1. **Valorização Especifica**
   2. **Valorização Padrão SIMPRO/BRAINDICE**
2. **Configurações**

## **01. VISÃO GERAL**

Esta página é destinada a explicar de forma completa o fluxo para realizar a valorização de Material e Medicamento.

### **01.1** **Valorização Especifica**

O cálculo do valor e dos dados do produto segue as seguintes regras:

1. 1. 1. Utiliza as informações do cadastro de produto como nome fantasia, descrição, unidade de controle, tipo do item, etc.
      2. Caso tenha a tabela **básica** de Matmed definida nos parâmetros gerais, o sistema obtêm as seguintes informações:
         1. Código específico, descrição, unidade de medida de faturamento, fator de conversão, preço, custo médio fixo, vínculo com Brasíndice, vínculo com Simpro, se é preço fixo
         2. Se existir informações o produto nessa tabela de Matmed, então o sistema verifica as seguintes condições:
            1. Está vinculado ou **Simpro ou Brasíndice** e não possui preço fixo. Se sim, acessa o histórico de preço na data do lançamento
            2. Se possuir valor, utiliza o **valor do histórico** das revistas
            3. Se não possuir valor e o produto possui o campo código especifico definido e não é preço fixo, então ele acessa o histórico de atualização desse item
               1. Se possuir valor, ele utiliza este preço
            4. Se não encontrou preço nos históricos, o preço a ser considerado é o definido na tabela.
      3. Após a tabela básica, o sistema pega o tipo do item, se material ou medicamento, e utiliza a tabela correspondente nas condições contratuais e **repete os passos do item 2**
      4. No caso de item particular, as tabelas a serem consideradas são os parâmetros: "*Tabelas de referência de preço para transferência de itens MATMED para Gastos Particulares*"

### **01.2** **Valorização Padrão SIMPRO/BRAINDICE**

Utiliza diretamente o preço padrão importado com os arquivos da revista em questão, não é necessário executar a rotina de atualização de preço para cada tabela.

## **02. CONFIGURAÇÕES VALORIZAÇÃO PADRÃO SIMPRO/BRASINDICE**

Para utilizar o preço padrão das revistas sem a necessidade de realizar atualização de preço tabela por tabela, é necessário configurar o campo Fonte de Preço para a revista correspondente. Desta forma, toda vez que for realizar o lançamento de um item na conta será realizado o calculo do preço com a aplicações de regras especificas.

Nota: Selecionando a origem do preço: Própria do Convênio, SIMPRO ou Brasíndice. Ao trocar a fonte, os campos da fonte anterior serão limpos e o grupo correspondente será desativado.

O usuário poderá configurar regras para cada tipo e classificação de produto diretamente no contrato.

Classificação do Item:

Configuração de regras para valorização do Material e Medicamento:

Então para o exemplo em questão temos 3 regras especificas para utilização neste contrato. A regra com vigência em 12/09/25 por exemplo diz o seguinte.    
No contrato da AMIL, para itens que sejam Material, da Categoria 12 e a Classe do produto 28, eu quero que prioriza o preço PMC (Preço Médio Consumidor)  da revista 1 e aplique os fatores configurados.

Desta forma como eu fixei uma revista, ao realizar um lançamento em MatMed esta regra deverá ser levada em consideração usando os preços trabalhados na revista ***1 - 20250006.***Caso não tenha sido fixada nenhuma revista o sistema deverá pegar sempre o preço da revista com vigência mais próxima (Não é a ultima revista importada e sim a vigência).

Caso o no lançamento do MatMed nenhuma regra seja encontrada, deverá ser levado em consideração o fatores configurados na tabela de preço do contrato ou caso a tabela de preço Mat ou Med não tenha sido informado no contrato, a tabela base deverá ser considerada.

Tabela Material não informada no contrato:

Tabelas básicas Material e Medicamento.

Importante

Sempre que existirem informações para o produto na tabela pesquisada ela será utilizada. Dessa forma, caso o produto tenha a descrição somente na tabela básica e o código específico na tabela do convênio, o sistema utilizará a descrição do item da tabela básica e o código específico, da tabela do convênio.
