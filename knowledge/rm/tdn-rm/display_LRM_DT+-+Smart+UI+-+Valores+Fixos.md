---
content_hash: 00200a9f925bc268f5dd14a64cf495cfe52759faa393c0c5249fb0ed442c8e05
fetched_at: '2026-06-29T00:12:01.705975+00:00'
page_id: '898454059'
product: rm
source: tdn-rm
title: DT - Smart UI - Valores Fixos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Smart+UI+-+Valores+Fixos
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart UI - Valores Fixos |
| País: | Brasil |
| Épico | [DRHCALCRM-7174](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7174) |

[**02. SITUAÇÃO/REQUISITO**](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7282)

Disponibilizar a nova tela do **Valores Fixos** utilizando a tecnologia do **Smart UI**. Esta nova tela receberá uma evolução visual e em partes funcional, da tela que conhecemos como Valores Fixos já disponibilizada na nossa atual MDI.

## **03. SOLUÇÃO**

Disponibilizamos a tela de **Valores Fixos**, utilizando o Smart UI para as versões 12.1.2502 e superiores. Essa implementação alterou visualmente o que já existia trazendo uma visão atualizada da pagina e também a maneira com que a utilizamos.   
  
A tela que já existia em versões inferiores a 12.1.2502 utilizava o padrão que já conhecemos na nossa MDI:  
  
   
  
Agora, com a utilização da nova tecnologia o seu visual ficou assim:  
  
  
  
Agora temos a opção de buscar registros que estão na tela sem necessariamente a criação de um filtro, como por exemplo, abaixo temos alguns registros sendo exibidos e caso queira retornar apenas o codigo **SFAB**,  basta que preencha o campo **Buscar na tabela** :  
  
  
  
  
  
  Vale lembrar que essa funcionalidade realiza a busca em qualquer campo exibido na tela, **somente os registros exibidos**, por padrão a tabela exibe 10 registros por busca, mas esse valor pode ser alterado, exibindo 20 / 50 / 100 / 1000 registros .   
  
Outra função que recebeu alterações visuais e funcionais é o gerenciamento e aplicações de **Filtros,**anteriormente ao clicar em Filtro era aberto uma janela pop-up para que pudessemos criar ou utilizar filtros já criados.  
  
  
  
Agora ao clicarmos em **Filtro**, será aberta lateralmente uma janela para que possamos gerenciar nossos filtros, onde temos filtros padrões como **Código / Nome e **Finalidade**** e também há a possibilidade de criarmos filtros personalizados, clicando em **Ir para filtros avançados** e Clicando em **+****Criar Filtro**:  
  
  
  
Para realizar a inclusão das clausulas do filtro, basta clicar em **+ Regra ,**selecionar o **Campo / Operador e Digitar seu filtro** como no exemplo abaixo:  
  
  
  
Para concluir a criação do Filtro, basta clicar então em **Salvar e Filtrar**  
  
Para realizar uma inclusão manual dos Valores Fixos, basta clicarmos em **+ Incluir** na pagina inicial, será então aberta uma pagina para a inclusão dos dados:  
  
**Vale se atentar a regra de inclusão que já existia anteriormente, caso selecione uma Finalidade especifica, será necessário preencher o código correspondente a ela.**  
  
Após o preenchimento dos dados, basta clicar em Salvar para a inclusão efetiva do registro  
  
  
  
Caso queira Excluir o registro, é necessário selecionar a linha desejada e clicar em **Excluir**, após a confirmação o registro será excluído:

Atenção

Nesta versão, a exclusão de registros é **limitada a um por vez**.  
Ou seja, é necessário **selecionar apenas uma linha por vez**. A seleção múltipla (duas ou mais linhas) **não é permitida para exclusão**.

Se necessário editar também um registro é possível selecionando o registro, e clicando em **Editar:**  
  
Após editar o campo desejado, basta clicar em salvar para que a edição seja concluida  
  
É possível também realizarmos a copia de registros entre as coligadas, selecionando o registro e clicando em **Ações Relacionadas / Copiar valor fixo entre coligadas**  
  
  
  
  
Após isso, basta realizarmos a parametrização, selecionando qual coligada receberá o registro, e se ele deve substituir o registro existente em casos que hajam registros na coligada destino.  
  
  
  
E por fim, basta avançarmos para a execução do processo, podendo acompanhar o processo para a inclusão na base destino:  
  
Para acompanhar o processo, podemos clicar em **Ações Relacionadas e Acompanhar Processos:**

###### **04. DEMAIS INFORMAÇÕES [Valores Fixos](https://tdn.totvs.com/display/LRM/Valores+Fixos#ValoresFixos-1)**
