---
content_hash: 288919db1b8bd1e13099c1b14e1cf6c20bf1e8117d4c71e8985dae4f49fc50da
fetched_at: '2026-06-29T00:12:03.377503+00:00'
page_id: '907906497'
product: rm
source: tdn-rm
title: DT - Smart UI - Gerenciador do Log de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=907906497
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart UI - Gerenciador do Log de Cálculo |
| País: | Brasil |
| Épico | [DRHCALCRM-7688](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7688) |

## **02. SITUAÇÃO/REQUISITO**

Disponibilizar a nova tela do **Gerenciador do Log de Cálculo**, utilizando a tecnologia do **Smart UI**. Esta nova tela receberá uma evolução visual e em partes funcional, da tela que conhecemos como Gerenciador do Log de Cálculo já disponibilizada na nossa atual MDI.

## **03. SOLUÇÃO**

Disponibilizamos a tela do **Gerenciador do Log de Cálculo**, utilizando o Smart UI para as versões 12.1.2502 e superiores. Essa implementação alterou visualmente o que já existia trazendo uma visão atualizada da pagina e também a maneira com que a utilizamos.   
  
A tela que já existia em versões inferiores a 12.1.2502 utilizava o padrão que já conhecemos na nossa MDI:  
  
   
  
Agora, com a utilização da nova tecnologia o seu visual ficou assim:  
  
  
  
Agora temos a opção de buscar registros que estão na tela sem necessariamente a criação de um filtro, como por exemplo, abaixo temos alguns registros sendo exibidos e caso queira retornar apenas os log's de calculo realizados pela maquina **SPON010124550,** basta que preencha o campo **Buscar na tabela** :  
  
  
  
  
  Vale lembrar que essa funcionalidade realiza a busca em qualquer campo exibido na tela, **somente os registros exibidos**, por padrão a tabela exibe 10 registros por busca, mas esse valor pode ser alterado, exibindo 20 / 50 / 100 / 1000 registros .   
  
Outra função que recebeu alterações visuais e funcionais é o gerenciamento e aplicações de **Filtros,**anteriormente ao clicar em Filtro era aberto uma janela pop-up para que pudessemos criar ou utilizar filtros já criados.  
  
  
  
Agora ao clicarmos em **Filtro**, será aberta lateralmente uma janela para que possamos gerenciar nossos filtros, onde temos filtros padrões como **Tipo do Cálculo** / **Id do Job** e **Id Processo** e também há a possibilidade de criarmos filtros personalizados, clicando em **Ir para filtros avançados** e Clicando em **+****Criar Filtro**:  
  
  
  
Para realizar a inclusão das clausulas do filtro, basta clicar em **+ Regra ,**selecionar o **Campo / Operador e Digitar seu filtro** como no exemplo abaixo:  
  
  
Para concluir a criação do Filtro, basta clicar então em **Salvar e Filtrar**  
  
É possível também realizar o processo de movimentação dos logs de cálculo através do processo **Movimentar Logs** em **Ações Relacionadas**Para seguir com o processo, basta realizar a parametrização de quantidade de meses e data base para a movimentação, e se você deseja incluir a movimentação de funcionarios demitidos também  
  
  
  
É possível também gerar o log de calculo para que seja salvo em sua propria maquina através do processo **"Gerar Log de Calculo"** em Ações relacionadas, vale lembrar que agora os log's serão salvos no caminho designado através da tag **<fileserverpath>** do seu Rm.Host.exe.config. Para realizar a geração, basta selecionar o tipo de log que deseja e as demais parametrizações.

###### **04. DEMAIS INFORMAÇÕES**
