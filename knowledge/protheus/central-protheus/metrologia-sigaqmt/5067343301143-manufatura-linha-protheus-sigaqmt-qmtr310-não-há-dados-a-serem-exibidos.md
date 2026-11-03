---
article_id: 5067343301143
category: Metrologia (SIGAQMT)
content_hash: 5ac0c831d6b6940e4805c8819846892bbbc32edbcf5971d120278a10fa6a9a51
fetched_at: '2026-06-28T22:42:24.888226+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTR310 - Não há dados a serem exibidos
type: support-article
updated_at: '2022-03-28T13:44:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5067343301143-Manufatura-Linha-Protheus-SIGAQMT-QMTR310-N%C3%A3o-h%C3%A1-dados-a-serem-exibidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min****Ocorrência**No módulo **SIGAQMT - Metrologia**, ao tentar listar o relatório **QMTR310 - Instrumentos Disponíveis por Filial** é exibida a mensagem **Não há dados a serem exibidos**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Essa mensagem ocorre, pois a parametrização do Sistema está incorreta para a listagem do relatório.  
  
**Solução**Para que o relatório seja listado é necessário que o parâmetro **MV\_QMTPMOV - Define o tipo de movimentação a ser realizada no QMT** esteja com o conteúdo igual à **2 - Mov. entre outras Filiais** e existam registros nas tabelas **QN4 - Movimentos Instr. Filiais** e **QN5 - Instrumentos Disponíveis** para o instrumento selecionado para listagem.  
  
**Importante**  
Somente irá existir registros nas tabelas **QN4** e **QN5** se o instrumento for incluído quando o parâmetro **MV\_QMTPMOV** estiver com o conteúdo igual à **2**.  
Caso o instrumento já estiver cadastrado e o conteúdo do parâmetro for apenas alterado, não irá gerar registros nestas tabelas, e por consequência, o relatório não irá listar dados para o instrumento em questão.
