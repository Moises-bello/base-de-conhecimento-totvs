---
content_hash: 1271606eb9c8f08e4633c2022cc913b35795f5a22efa4a4d086bf96198f70d9b
fetched_at: '2026-06-29T00:11:25.545002+00:00'
page_id: '712476903'
product: rm
source: tdn-rm
title: Operação - Auto-incremento (RM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=712476903
version: 13
---

CONTEÚDO

## 01. VISÃO GERAL

Instruções de como utilizar a Operação "Auto-incremento (RM)" na criação de um Conceito.  
Esta operação é utilizada para obter um contador sequencial e contínuo.  
A Tabela GAUTOINC é responsável por controlar os códigos de auto incremento do sistema.

## 02. EXEMPLO DE UTILIZAÇÃO

falseExemplo de Utilização1º Passo:

Em um conceito defina as configurações de Origem e Destino, conforme sua necessidade:

2º Passo:

Acesse a aba "Operações" e adicione a operação "**Auto-incremento (RM)**"

Na tela da operação, informe as seguintes configurações:

* Conexão: Que é o nome da conexão de destino
* Cód. AutoInc: Informe da tabela da conexão de destino que contém a coluna para auto incremento.

3º Passo:

Agora vamos realizar a ligação entre a coluna Auto incremental da tabela de Destino com a operação Auto-incremento (RM)

* Acesse a aba Ligações
* Em operações, selecione o tipo Auto-incremento (RM)
* Arraste e solte em cima da coluna de destino que representa o código sequencial auto incremental.
* Duas novas propriedades de ligação serão apresentadas para configurar: Coligada e Sistema

4º Passo:

Agora vamos configurar as propriedades da ligação, Coligada e Sistema:

* Coligada e Sistema, devem ser informados os valores da chave para obter o valor sequencial a tabela GAUTOINC.  
  O conteúdo do valor pode ser informado por uma ligação da tabela de origem, por um contexto ou por um valor fixo.  
    
  Na imagem abaixo segue um exemplo das formas de informar os valores:

## 03. OBSERVAÇÕES IMPORTANTES

ATENÇÃO!

Quando a conexão de destino for do tipo DataServer e de produto, a coluna do tipo auto-incremental poderá ter sua sequencia alterada pela regra de negócio do produto.

Dessa forma poderá existir um acréscimo a cada execução, pulando um número, porém mantendo a sequencia para cada registro.

Exemplo: 

* Execução 1: 2,3,4,5 (esperado 1,2,3,4)
* Execução 2: 7,8,9,10 (esperado 6,7,8,9)
* Execução 3: 12,13,14,15 (esperado 11,12,13,14)

No exemplo abaixo o tipo de conexão de destino com um DataServer do produto:
