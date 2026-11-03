---
content_hash: ac5af25df52389e13761132b0177ede6ebf93c4696129fd5cf4fdd879b81a60a
fetched_at: '2026-06-29T00:12:02.464776+00:00'
page_id: '901953974'
product: rm
source: tdn-rm
title: DT - Smart UI - Tarifas de Vale Transporte
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Smart+UI+-+Tarifas+de+Vale+Transporte
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart UI - Tarifas de Transporte |
| País: | Brasil |
| Épico | [DRHCALCRM-7275](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7275) |

## **02. SITUAÇÃO/REQUISITO**

Disponibilizar a nova tela de **Tarifas de Transporte**, utilizando a tecnologia do **Smart UI**. Esta nova tela receberá uma evolução visual e em partes funcional, da tela que conhecemos como Tarifas de Transporte já disponibilizada na nossa atual MDI.

## **03. SOLUÇÃO**

Disponibilizamos a tela de **Tarifas de Transporte**, utilizando o Smart UI para as versões 12.1.2502 e superiores. Essa implementação alterou visualmente o que já existia trazendo uma visão atualizada da pagina e também a maneira com que a utilizamos. 

## **04. DEMAIS INFORMAÇÕES**

A tela que já existia em versões inferiores a 12.1.2502 utilizava o padrão que já conhecemos na nossa MDI:  
  
  
  
Agora, com a utilização da nova tecnologia o seu visual ficou assim:  
  
  
  
Agora temos a opção de buscar registros que estão na tela sem necessariamente a criação de um filtro, como por exemplo, abaixo temos alguns registros sendo exibidos e caso queira retornar apenas o codigo **52545**,  basta que preencha o campo **Buscar na tabela** :  
  
  
  
  Vale lembrar que essa funcionalidade realiza a busca em qualquer campo exibido na tela, **somente os registros exibidos**, por padrão a tabela exibe 10 registros por busca, mas esse valor pode ser alterado, exibindo 20 / 50 / 100 / 1000 registros .   
  
Outra função que recebeu alterações visuais e funcionais é o gerenciamento e aplicações de **Filtros,**anteriormente ao clicar em Filtro era aberto uma janela pop-up para que pudessemos criar ou utilizar filtros já criados.  
  
  
  
Agora ao clicarmos em **Filtro**, será aberta lateralmente uma janela para que possamos gerenciar nossos filtros, onde temos filtros padrões como **Código** e também há a possibilidade de criarmos filtros personalizados, clicando em **Ir para filtros avançados**e Clicando em **+****Criar Filtro**:  
  
  
  
  
Para realizar a inclusão das clausulas do filtro, basta clicar em **+ Regra ,**selecionar o **Campo / Operador e Digitar seu filtro** como no exemplo abaixo:  
  
  
  
Para concluir a criação do Filtro, basta clicar então em **Salvar e Filtrar**  
  
Para realizar uma inclusão manual da Tarifas de Transporte, basta clicarmos em **+ Incluir** na pagina inicial, será então aberta uma pagina para a inclusão dos dados:  
  
Após o preenchimento dos dados, basta clicar em Salvar para a inclusão efetiva do registro  
  
  
  
Caso queira Excluir o registro, é necessário selecionar a linha desejada e clicar em **Excluir**, após a confirmação o registro será excluído:

Atenção

Nesta versão, a exclusão de registros é **limitada a um por vez**.  
Ou seja, é necessário **selecionar apenas uma linha por vez**. A seleção múltipla (duas ou mais linhas) **não é permitida para exclusão**.

Para editarmos um registro, basta selecionarmos a checkbox do mesmo e clicarmos em editar. Após realizar a edição do campo, basta clicarmos em Salvar.  
  
  
  
  
Neste módulo também é possível copiarmos registros entre coligadas, selecionando um ou mais registros e clicando em **Ações Relacionadas**, após isso clicar em **Copiar tarifas entre coligadas,**e realizar a parametrização necessaria para a copia.  
  
  
  
Feita a parametrização basta clicarmos em Concluir e o processo será executado

## **05. ASSUNTOS RELACIONADOS**
