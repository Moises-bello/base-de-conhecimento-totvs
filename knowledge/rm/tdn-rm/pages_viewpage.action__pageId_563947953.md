---
content_hash: b59630ffef206b785888c84fd113aaba8da20ead7dfbc1493c7032fdff968c49
fetched_at: '2026-06-29T00:10:51.228550+00:00'
page_id: '563947953'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563947953
version: 10
---

Possibilitar utilização de Relatórios criados a partir do RM, utilizando Reports, ou desenvolvidos no próprio Portal de Imóveis. Além disto existem outros recursos que possibilitarão a visualização e impressão destes relatórios por grupos de acessos. Abaixo segue maiores detalhes destas funcionalidades.

#FF9000Relatórios

Ao acessar o menu Backend -> relatórios, será possível selecionar quais grupos de usuários poderão visualizar os relatórios.

Ao selecionar Permissões é possível marcar quais grupos terão acesso ao relatório.

Observações:

* Na visão Front de relatório será exibido somente relatórios cujo o grupo tenha permissão.
* Caso o relatório criado não tenha nenhum grupo selecionado, por padrão todos podem visualiza-lo.

Possibilitar utilização de Relatórios criados a partir do RM, utilizando Reports.

#FF9000Criar Reports via RM

É possível desenvolver relatórios no RM utilizando o recurso do Reports. Porém para isto existem algumas particularidades a serem realizadas afim de que o Layout possa utilizar consulta nas tabelas do Banco de dados do Portal de Imóveis que está integrado com o Banco de dados do TOTVS RM.

* Ao acessar o Reports (via RM), inclua um novo relatório onde neste relatório deverá ter a SQL respectiva ao informação que será gerada quando este mesmo relatório for filtrado no Portal de Imóveis. Observe na Imagem abaixo que existe uma parametrização que irá integrar esta consulta SQL com o Banco de dados Externo (neste caso o Banco do Portal de Imóveis).
* Ao criar a conexão de Banco de dados Externo, algumas parametrizações são necessárias, veja esta documentação: [Conexão de Banco de dados Externo](https://tdn.totvs.com/pages/viewpage.action?pageId=59900202)Parâmetros

  Os parâmetros disponíveis do Portal de Imóveis para utilização nas consultas do Reports são:

  + Identificador da proposta               (Campo ID da tabela Proposta)                               => PARAM\_PROPOSTA
  + Identificador do empreendimento (Campo Empreendimento\_id da tabela Proposta)   => PARAM\_EMPREENDIMENTO\_ID
  + Código do empreendimento          (Código do Empreendimento no RM)                     => PARAM\_COD\_PESS\_EMPR

* Em seguida, após salvar a consulta SQL, inclua a mesma no Reports, informando o parâmetro descrito na Sintaxe SQL (Obs.: Estes devem ter os mesmos nomes dos parâmetros disponíveis pelo Portal de Imóveis) e salve este layout. Veja na imagem a Consulta SQL e o Parâmetro inserido no Reports:

* Após realizar esta parametrização, ao acessar o Portal de Imóveis > Backend > Relatórios, será possível filtrar este relatório parametrizado. Clique em Adicionar e selecione o relatório criado a partir do Reports (clique em selecionar);

**[Mais dicas disponíveis sobre Recursos Gerenciais, clique aqui!](https://tdn.totvs.com/display/public/LRM/Menu+Gerencial)**
