---
content_hash: 24ee13f497f716d7899e56c7dd9142a74affbcd8e7ee6e78d3a7c41b38e60d33
fetched_at: '2026-06-29T00:12:00.183106+00:00'
page_id: '883049970'
product: rm
source: tdn-rm
title: DT - Smart UI - Consulta Movimento da Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883049970
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart UI - Consulta Movimento da Integração |
| País: | Brasil |
| Épico | [DRHCALCRM-7266](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7266) |

## **02. SITUAÇÃO/REQUISITO**

Disponibilizar a nova tela de **Consulta Movimento de Integração,** utilizando a tecnologia do **Smart UI**. Esta nova tela receberá uma evolução visual e em partes funcional, da tela que conhecemos como Consulta Movimento de Integração já disponibilizada na nossa atual MDI.

## **03. SOLUÇÃO**

Disponibilizamos a tela do **Consulta Movimento de Integração**, utilizando o Smart UI para as versões 12.1.2502 e superiores. Essa implementação alterou visualmente o que já existia trazendo uma visão atualizada da pagina e também a maneira com que a utilizamos.

### ✔️ Visual Atualizado

A interface anterior, presente nas versões abaixo de 12.1.2502, utilizava a tecnologia MDI tradicional.

Com a nova Smart UI, o visual é mais limpo, responsivo e intuitivo:  
  
   
  
Agora, com a utilização da nova tecnologia o seu visual ficou assim:  
  
  
  
Agora temos a opção de buscar registros que estão na tela sem necessariamente a criação de um filtro, como por exemplo, abaixo temos alguns registros sendo exibidos e caso queira retornar apenas o funcionário de chapa **00004**,  basta que preencha o campo **Buscar na tabela** :  
  
  
  
  
  
  Vale lembrar que essa funcionalidade realiza a busca em qualquer campo exibido na tela, **somente os registros exibidos**, por padrão a tabela exibe 10 registros por busca, mas esse valor pode ser alterado, exibindo 20 / 50 / 100 / 1000 registros .   
  
Outra função que recebeu alterações visuais e funcionais é o gerenciamento e aplicações de **Filtros,**anteriormente ao clicar em Filtro era aberto uma janela pop-up para que pudessemos criar ou utilizar filtros já criados.  
  
  
  
Agora ao clicarmos em **Filtro**, será aberta lateralmente uma janela para que possamos gerenciar nossos filtros, onde temos filtros padrões como **Ano** / **Mês** e **Funcionário** e também há a possibilidade de criarmos filtros personalizados, clicando em **Ir para filtros avançados** e Clicando em **+****Criar Filtro**:  
  
  
Para realizar a inclusão das clausulas do filtro, basta clicar em **+ Regra ,**selecionar o **Campo / Operador e Digitar seu filtro** como no exemplo abaixo:  
  
  
Para concluir a criação do Filtro, basta clicar então em **Salvar e Filtrar**  
  
  
  
Caso queira Excluir o registro, é necessário selecionar a linha desejada e clicar em **Excluir**, após a confirmação o registro será excluído:

Atenção

Nesta versão, a exclusão de registros é **limitada a um por vez**.  
Ou seja, é necessário **selecionar apenas uma linha por vez**. A seleção múltipla (duas ou mais linhas) **não é permitida para exclusão**.

Na tela inicial do historico de provisão é possível também ajustar as colunas do Grid, fixando-as ou então alterando sua posição de exibição ou então a sua não exibição. Também é permitido alterar a quantidade de registros que serão exibidos. Tudo isso pode ser feito através da função **Gerenciar Tabela**

## **04. DEMAIS INFORMAÇÕES**
