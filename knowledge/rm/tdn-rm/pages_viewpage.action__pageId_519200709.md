---
content_hash: 5e84b6e7e109051f361dee1a5d7fe7ac7c544a7349bc51d2a6a1109ddb23d3c1
fetched_at: '2026-06-29T00:10:30.131624+00:00'
page_id: '519200709'
product: rm
source: tdn-rm
title: Impressão de Etiquetas de código de barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519200709
version: 23
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Lista de processos permitidos**
   1. **Outras Ações / Ações relacionadas**
4. **Tela principal**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**
6. **Configurar campo no relatório para exibir código de barras**

PainelVisão Geral

## **01. VISÃO GERAL**

No Totvs Gestão Hospitalar, acessando o menu “**Farmácia> Etiquetas de código de barras**”, será possível imprimir as etiquetas dos produtos ou lotes selecionados.

Atenção

A nova funcionalidade utiliza o RM Report e a versão anterior utilizava o antigo Gerador. Para utilizar a nova versão é necessário converter o antigo relatório para o RM Reports e ajustá-lo caso seja necessário.

Está disponibilizado um relatório padrão na pasta: C:\TOTVS\CorporeRM\ObjetosGerenciais\Relatórios

O relatório padrão disponibilizado é o SAUREL0019 - Etiqueta de código de barras

## **05. TABELAS UTILIZADAS**

* SZTABW
Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

**Passos para a impressão das etiquetas:**

11Pesquisar o produto desejado

Acessando o menu “**Farmácia> Etiquetas de código de barras**”

Ao clicar no campo Produto, o sistema irá apresentar uma tela de pesquisa aos produtos, onde deverá ser selecionado o item desejado.

Caso o produto selecionado não seja controlado por Lote:

Caso o produto selecionado seja controlado por Lote:

**Observação:** Para não exibir itens sem saldo disponível, é necessário configurar os parâmetros gerais do sistema. Acesse: Menu > Ambiente > Parâmetros > Gestão Hospitalar. Em seguida, selecione a aba *11.03 - Estoque > Estoque - Identificação 1/5*. Veja a imagem abaixo para referência:

2Produtos selecionados para execução

A impressão de etiqueta somente será realizada nos itens selecionados na grid “Produtos Selecionados”.

O item selecionado na grid “Saldo disponível” deverá ser inserido na grid “Produtos Selecionados”, utilizando o botão 

Importante: serão exibidos no campo "Código de Barras" apenas os códigos de barras de itens que possuírem lote vinculados a ele.

3Impressão das etiquetas

Na grid “Produtos Selecionados”, marque os itens que deseja imprimir etiquetas e em seguida pressione o botão  Imprimir

Os itens serão inseridos na tabela temporárias SZTABW e em seguida gerado o relatório solicitado na tela.

4Inserir código de barras

O campo "**Inserir código e barra**" Somente será habilitado se estiver marcado o Parâmetro "**Utiliza código de barra padrão EAN128**" ou “**Utiliza código de barras padrão DataMatriz**” localizado no menu **Ambientes> Parâmetros> Gestão hospitalar> Estoque> Estoque-Identificação 4/5.**

Na grid “Produtos selecionados”, marque o item que deseja inserir código de barras e em seguida pressione o botão “Inserir código de barras”.

Digite o código de barras e salve.

O código de barras digitado será gravado no cadastro de Produto.  
Localizado no menu **Cadastro>Estoque>Produto>Código de barras**

Lista de Processos permitidos

## **03. Lista de Processos permitidos**

| Ação | Descrição |
| --- | --- |
|  | O item selecionado na grid “Saldo disponível” será inserido na grid “Produtos Selecionados”. Tecla de atalho: Ctrl + Insert. |
|  | Excluir itens da grid “Produtos Selecionados”. Tecla de atalho: Ctrl + Delete. |
| Imprimir | Na grid “Produtos Selecionados”, marque os itens que deseja imprimir etiquetas e em seguida pressione o botão “Imprimir”. Tecla de atalho: Ctrl + Print Screen.  Os itens serão inseridos na tabela temporárias SZTABW e em seguida gerado o relatório solicitado na tela. |
| Inserir código de barra | Somente será habilitado se estiver marcado o “Parâmetro Geral | Estoques II”, campos “Utiliza código de barras padrãoEAN128” ou “Utiliza código de barras padrão DataMatriz”.  Na grid “Produtos selecionados”, marque o item que deseja inserir código de barras e em seguida pressione o botão “Inserir código de barras”. Digite o código de barras e salve. O código de barras será gravado no cadastro de Produto |

Tela Principal

## **04. Tela Principal**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| **Quantidade de etiquetas a serem impressas** | A quantidade de etiquetas somente poderá ser alterado se o produto não utilizar número de série. Para os produtos que utilizam série, a quantidade será sempre 1. |
| **Relatório de impressão de etiquetas de código de barra** | Serão listados os relatórios do “RM Report” e o mesmo deverá conter os parâmetros com nome “NOMECOMP” e “COLIGADA”.  Este campo já virá preenchido com o default marcado no menu **Ambientes> Parâmetros> Gestão hospitalar> Estoque>Identificação 2/5**, campo “**Relatório de Impressão de Etiquetas de Código de Barras**”.  O parâmetro foi alterado para listar somente relatórios do gerador “RM Reports” (antes listava do “Gerador de relatórios”). |
| **Código do Produto** | Ao clicar no botão ao lado deste campo, será permitido pesquisar o produto desejado. Tecla de atalho: Ctrl + F |
| **Local de estoque** | No menu **Ambientes> Parâmetros> Gestão hospitalar>Estoque>Identificação 1/5**, temos o campo “**Impressão de etiquetas – Exibe apenas locais de estoque associados à filiais das unidades de faturamento**”. Caso este parâmetro esteja marcado, será listado na tela somente os locais de estoque das unidades de faturamento. |

O relatório deverá utilizar campos da tabela temporária SZTABW. IMPORTANTE!

Configurar campo no relatório para exibir código de barras

## **06. CONFIGURAR CAMPO NO RELATÓRIO PARA EXIBIR CÓDIGO DE BARRAS**

Acessar o menu RM > Gestão > Rm Reports e selecionar ou criar o relatório devido com o leiaute de código de barras, o RM Saúde disponibiliza por padrão o relatório SAUREL0019 - Etiqueta de código de barras.

Criar o leiaute e inserir um controle do tipo código de barras, em suas propriedades escolher qual o modelo de código de barras que será utilizado e associar o controle ao campo da consulta quando necessário.

]]>
