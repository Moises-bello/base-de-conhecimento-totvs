---
content_hash: 316d9e238af9b38d7e9efc71609592a6873c4b38f691d6e74df244f54d372b72
fetched_at: '2026-06-29T00:11:49.381404+00:00'
page_id: '831838054'
product: rm
source: tdn-rm
title: Manutenção de Tabelas de Preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=831838054
version: 9
---

## **CONTEÚDO**

**CONTEÚDO**

## **01. VISÃO GERAL**

As tabelas de preço são utilizadas pela entidade hospitalar, onde cada tabela pode ser utilizada por um ou mais convênios, dependendo das particularidades de cada um.

Este processo tem como objetivo dar manutenção em tabelas de preço de Procedimentos e Serviços ou de Materiais e Medicamentos, permitindo efetuar cópias, reajuste de valores e deletar tabelas de preço.

Para saber mais sobre Tabelas de Preço Usadas (utilizadas nos Procedimentos e Serviços), acesse a página .

Para saber mais sobre Tabelas de MatMed Usadas (utilizadas nos Materiais e Medicamentos), acesse a página .

## **02. MANUTENÇÃO DE TABELAS DE PREÇO**

Para utilizar o processo de Manutenção de Tabelas de Preço, acessar: **Faturamento > Outros > Atualização de Preços > Manutenção de Tabelas de Preço**.

Dentro deste menu temos duas outras opções, que são **Procedimentos e Serviços** e **Materiais e Medicamentos**.

## **03. TELAS**

Nas telas destes processos, teremos inicialmente uma visão com as tabelas de preços para serem selecionadas.

Esta visão atende ao novo padrão visual do sistema, que assim como o padrão antigo, permite determinar as colunas que são visualizadas, clicando na "**engrenagem**", e deixando marcadas as colunas que deseja visualizar, ou alterando a ordem de exibição.

E também é possível efetuar um filtro na consulta que será efetuada na base de dados, clicando em "**Filtros**", e informando algum valor nos campos que desejar filtrar (campos não informados são ignorados).

Para utilizar os processos é necessário selecionar um dos registros listados, clicar em "**Processos**", e depois clicar em uma das opções, que são "**Copiar**", "**Deletar**" e "**Reajustar**".

Ao selecionar um dos processos, será exibida uma página com algumas etapas...

1. A 1º etapa é uma tela de boas vindas, que tem uma breve explicação sobre o processos.
2. A 2ª etapa são os dados do agendamento do processo.
3. A 3ª etapa é onde são informados os dados para o processamento.
4. A 4ª etapa é uma tela de pré-visualização dos dados informados, e se conclui o processamento.

Os campos a serem informados para cada processo são?

* **Copiar** (Para **Procedimentos e Serviços** ou **Materiais e Medicamentos**)
  + Tabela de Destino - A tabela de preço que receberá os dados da tabela de preço informada na tela principal
  + Preservar Valores Monetários - Este campo possui duas opções, que são:
    - Sim - Ao copiar os itens da tabela origem para a tabela destino, copiará todos campos.
    - Não - Ao copiar os itens da tabela origem para a tabela destino, copiará todos campos exceto os campos de valores monetários, como custo operacional, honorário, custo unitário, etc.
  + Sobrescrever Registros - Este campo possui duas opções, que são:
    - Sim - Caso a tabela de destino já exista e possua itens, apagará estes itens e copiará estes itens da tabela origem
    - Não - Caso a tabela de destino já exista e possua itens, não fazer nada, mantendo os valores atuais.
  + Filtro - Explicação do mesmo mais abaixo.
* **Deletar** (Para **Procedimentos e Serviços** ou **Materiais e Medicamentos**)
  + Filtro - Explicação do mesmo mais abaixo.
* **Reajustar** (Apenas para **Procedimentos e Serviços**)
  + Fator de conversão  - O percentual a ser aplicado no reajuste dos preços
  + Filtro - Explicação do mesmo mais abaixo.

A opção **Preservar Valores Monetários** é o antigo campo **Opções** do RMSaude

O filtro possui alguns campos, que são:

* Tipo de Filtro - Este campo define como será efetuado o filtro ao consultar os processar os registros na base de dados, e possui 4 opções, que são:
  + Total - Processará todos os itens
  + Especialidade - Habilitará o campo especialidade
  + Grupo - Habilitará o campo Grupo
  + Faixa - Habilitará os campos Faixa inicial e Faixa final
* Especialidade - Deve-se informar a especialidade
* Grupo - Deve-se informar o grupo de itens
* Faixa inicial - Deve-se informar o código de tabela de preço inicial
* Faixa final - Deve-se informar o código de tabela de preço final

## **04. DIFERENÇA ENTRE OS PROCESSOS**

Os dois processos (**Procedimentos e Serviços** ou **Materiais e Medicamentos**) no geral fazem as mesmas coisas, porém:

1. Processos:  
   Para Procedimentos e Serviços temos os 3 processos (Copiar, Deletar e Reajustar), enquanto para Materiais e Medicamentos temos apenas o Copiar e Deletar.
2. Filtro:  
   Para Procedimentos e Serviços o filtro possui as 4 opções (Total, Especialidade, Grupo e Faixa), e para Materiais e Medicamentos temos apenas Total ou Faixa.
3. Histórico:  
   Apenas o processo de Reajuste gera histórico, sendo assim, como apenas Procedimentos e Serviços possui o processo de Reajuste, apenas o mesmo possui histórico.

## **05. HISTÓRICO**

Como mencionado anteriormente, para Procedimentos e Serviços temos o processo de Reajustar, onde este gera um histórico.

Este histórico pode ser visualizado clicando no ícone de histórico na lista de dados da visão principal.

Após abrir o histórico, pode-se voltar a visão principal ao clicar no link "Manutenção Tabela Preço" no topo da página, ou no botão "Voltar" no rodapé.

## **06. PROCESSO REAJUSTAR**

Ao selecionar este processo, exibirá uma tela para informar o fator de conversão (fator de ajuste) e o filtro dos itens desta tabela de preço a serem ajustados.

* Fator de conversão:  
  Este campo determina o valor a ser ajustado, exemplo, se um item custa 100,00 e informar o fator 0,5, aumentará o valor em 50% do valor atual, ou seja:  
  50% de 100,00 = 50,00  
  100,00 (valor atual) + 50,00 (valor a somar com base no fator 0,5) = 150,00.
* Tipo de Filtro:  
  Este campo determina como filtrar os itens da tabela de preço, com as opções...
  + Total:  
    Todos os campos abaixo serão desabilitados.  
    Atualizará todos os itens da tabela de preço selecionada sem filtro.
  + Especialidade:  
    Habilitará apenas o campo "Especialidade".  
    Atualizará todos os itens da tabela de preço selecionada que pertencerem a especialidade informada.
  + Grupo:  
    Habilitará os campos "Especialidade" e "Grupo".  
    Atualizará todos os itens da tabela de preço selecionada que pertencerem a especialidade e grupo informados.
  + Faixa:  
    Habilitará os campos "Faixa inicial" e "Faixa final".  
    Atualizará todos os itens da tabela de preço selecionada que estiverem dentro da faixa informada.  
    Permite informar o mesmo valor nos dois campos, assim efetuando o ajuste em apenas um item.

Os itens ajustados podem ser visualizados em
