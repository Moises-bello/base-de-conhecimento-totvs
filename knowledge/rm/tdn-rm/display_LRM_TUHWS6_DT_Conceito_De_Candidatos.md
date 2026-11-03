---
content_hash: 9b81e965b60d64a44295811d2d2ecd909b7ffe5b644ea4f77aca98ec9a4f3dac
fetched_at: '2026-06-29T00:08:04.098094+00:00'
page_id: '235335780'
product: rm
source: tdn-rm
title: TUHWS6_DT_Conceito_De_Candidatos
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHWS6_DT_Conceito_De_Candidatos
version: 116
---

# CONCEITO DE CANDIDATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Pessoas* |
| **Função:** | *Conceito de Candidatos* |
| **Situação/Requisito:** | *Ao tentar importar candidatos através de um conceito, ocorre o erro:*  *Ocorreu algum erro ao executar o Processo, segue mensagem abaixo:*  *Candidatos[0] Erro na importação. Mensagem original: Erro em um ou mais registros do lote a seguir CODPESSOA=-1* *CODPESSOA=-2* *CODPESSOA=-3* *CODPESSOA=-4* *CODPESSOA=-5* *CODPESSOA=-6* *CODPESSOA=-7* *CODPESSOA=-8* *CODPESSOA=-9* *CODPESSOA=-10* *. Mensagem de erro: Violação de chave estrangeira*  *Possíveis causas:*  *- exclusão de registro que possui outros registros associados*  *- inclusão de registro detalhe sem um registro mestre associado | The INSERT statement conflicted with the FOREIGN KEY constraint "FKVCANDIDATOS\_PPESSOA". The conflict occurred in database "EXE1218TESTE", table "dbo.PPESSOA", column 'CODIGO'.* *The statement has been terminated.*    *>> Registros executados com Erro [Total: 10]:*    *Erro: Violação de chave estrangeira*    *Possíveis causas:*  *- exclusão de registro que possui outros registros associados*  *- inclusão de registro detalhe sem um registro mestre associado* |
| **Solução/Implementação:** | *Ajuste na importação de candidatos através de conceito.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TUHWS6* |
| **Requisito (ISSUE):** |  |

divs
