---
content_hash: 468195ee3d5f5d662cb465d254b68027fd090cdb82cb35a70bbc689d4a21577c
fetched_at: '2026-06-29T00:12:08.351932+00:00'
page_id: '930794623'
product: rm
source: tdn-rm
title: DT -  Exportação de Funcionário - Erro "A consulta SQL utilizada pelo filtro
  não foi encontrada"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=930794623
version: 14
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS -  Folha de Pagamento |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Exportação de Funcionários - Erro "A consulta SQL utilizada pelo filtro não foi encontrada" |
| País: | Brasil |
| Issue: | [DRHROTRM-13351](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13351) |

## **02. SITUAÇÃO/REQUISITO**

Ao exportar um funcionário através do menu Gerador de Saída utilizando um filtro, o sistema está apresentando a seguinte mensagem de erro: **"A consulta SQL utilizada pelo filtro não foi encontrada!"**

## **03. SOLUÇÃO**

Durante a importação do layout , constatou-se que as consultas SQLs estavam sendo importadas com o código errado. Para resolver esta situação, foi necessário editar do layout, renomeando o nome padrão das sub-queries cadastradas. Com isso, as queries passaram a ser registradas na tabela **CONSSQL** com o **CODSENTENCA** correto no momento da importação.

Quando o layout é baixado via **TOTVS Compartilhamento**, as queries são automaticamente cadastradas durante o processo de importação. É possível consultá-las através do menu **Consultas SQL**. Ao final da importação, será exibido um log informando quais queries foram cadastradas ou atualizadas, juntamente com seus respectivos códigos (**CODSENTENCA**).

Conforme a documentação [Importação de Consulta SQL](https://tdn.totvs.com.br/pages/viewpage.action?pageId=334347509), caso a consulta já esteja cadastrada na base de dados, o processo de importação irá adicionar um sufixo sequencial no CODSENTENCA para a sub-query nova, evitando que o query do layout anterior seja sobreposta.

Caso haja atualização nas queries do layout, a recomendação é excluir as queries já salvas na base, pela tela "Consultas SQL", e realizar a importação novamente, garantindo que a query seja cadastrada novamente na base.

Outra alternativa é marcar a opção "Fixo", na tela de importação de layout, para que o CODSENTENCA salvo na base seja sobrescrito pela nova versão importada.
