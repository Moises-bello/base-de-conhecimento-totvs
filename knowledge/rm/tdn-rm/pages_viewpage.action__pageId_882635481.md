---
content_hash: 7f303a24a3fd5af1734c5a7b24f836444ec93bb97689005364adf636d7c1b2f8
fetched_at: '2026-06-29T00:12:00.169022+00:00'
page_id: '882635481'
product: rm
source: tdn-rm
title: DT - Smart UI - Histórico de Provisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=882635481
version: 5
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart UI - Histórico de Provisão |
| País: | Brasil |
| Épico | [DRHCALCRM-7264](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7264) |

## **02. SITUAÇÃO/REQUISITO**

Disponibilizar a nova tela do **Histórico de Provisão**, utilizando a tecnologia do **Smart UI**. Esta nova tela receberá uma evolução visual e em partes funcional, da tela que conhecemos como Histórico de provisão já disponibilizada na nossa atual MDI.

## **03. SOLUÇÃO**

Disponibilizamos a tela do **Histórico de Provisão**, utilizando o Smart UI para as versões 12.1.2502 e superiores. Essa implementação alterou visualmente o que já existia trazendo uma visão atualizada da pagina e também a maneira com que a utilizamos.   
  
A tela que já existia em versões inferiores a 12.1.2502 utilizava o padrão que já conhecemos na nossa MDI:  
  
   
  
Agora, com a utilização da nova tecnologia o seu visual ficou assim:  
  
  
  
Agora temos a opção de buscar registros que estão na tela sem necessariamente a criação de um filtro, como por exemplo, abaixo temos alguns registros sendo exibidos e caso queira retornar apenas o funcionário de chapa **00009**,  basta que preencha o campo **Buscar na tabela** :  
  
  
  
  
  
  Vale lembrar que essa funcionalidade realiza a busca em qualquer campo exibido na tela, **somente os registros exibidos**, por padrão a tabela exibe 10 registros por busca, mas esse valor pode ser alterado, exibindo 20 / 50 / 100 / 1000 registros .   
  
Outra função que recebeu alterações visuais e funcionais é o gerenciamento e aplicações de **Filtros,**anteriormente ao clicar em Filtro era aberto uma janela pop-up para que pudessemos criar ou utilizar filtros já criados.  
  
  
  
Agora ao clicarmos em **Filtro**, será aberta lateralmente uma janela para que possamos gerenciar nossos filtros, onde temos filtros padrões como **Ano** / **Mês** e **Funcionário** e também há a possibilidade de criarmos filtros personalizados, clicando em **Ir para filtros avançados** e Clicando em **+****Criar Filtro**:  
  
  
Para realizar a inclusão das clausulas do filtro, basta clicar em **+ Regra ,**selecionar o **Campo / Operador e Digitar seu filtro** como no exemplo abaixo:  
  
Para concluir a criação do Filtro, basta clicar então em **Salvar e Filtrar**  
  
Para realizar uma inclusão manual do Histórico de provisão, basta clicarmos em **+ Incluir** na pagina inicial, será então aberta uma pagina para a inclusão dos dados:  
  
  
 Após o preenchimento dos dados, basta clicar em Salvar para a inclusão efetiva do registro  
  
  
Caso queira Excluir o registro, é necessário selecionar a linha desejada e clicar em **Excluir**, após a confirmação o registro será excluído:

Atenção

Nesta versão, a exclusão de registros é **limitada a um por vez**.  
Ou seja, é necessário **selecionar apenas uma linha por vez**. A seleção múltipla (duas ou mais linhas) **não é permitida para exclusão**.

Se necessário editar também um registro é possível selecionando o registro, e clicando em **Editar:**  
  
Após editar o campo desejado, basta clicar em salvar para que a edição seja concluida  
  
Na tela inicial do historico de provisão é possível também ajustar as colunas do Grid, fixando-as ou então alterando sua posição de exibição ou então a sua não exibição. Também é permitido alterar a quantidade de registros que serão exibidos. Tudo isso pode ser feito através da função **Gerenciar Tabela**

###### **04. DEMAIS INFORMAÇÕES [Geração Histórico de Provisões (.Net)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719548)**
