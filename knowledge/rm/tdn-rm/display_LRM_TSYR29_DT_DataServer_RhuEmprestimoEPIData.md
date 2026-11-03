---
content_hash: ba2f6b26fd1dd8eb581e859b2ebd70eaa321071ea36713c3fdb18c2e21432d52
fetched_at: '2026-06-29T00:06:12.543449+00:00'
page_id: '205917569'
product: rm
source: tdn-rm
title: TSYR29_DT_DataServer_RhuEmprestimoEPIData
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYR29_DT_DataServer_RhuEmprestimoEPIData
version: 122
---

# DATASERVER RHUEMPRESTIMOEPIDATA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | DataServer RhuEmprestimoEPIData |
| **Situação/Requisito:** | Ao criar conceito e tentar associar ao cadastro de EPI está gerando mensagem conforme descrito abaixo.  Ocorreu um erro ao efetuar a leitura das definições da Tabela:  ORA-00904: VEMPRESTIMOEPI.IDMOTDEVOLUCAO: identificador inválido |
| **Solução/Implementação:** | Verificado que as propriedades da tabela não estavam definidas de forma correta. Porém, seguindo a regra da aplicação, não é possível realizar inclusão, alteração ou exclusão de dados na tabela VEMPRESTIMOEPI. Todos os dados presentes nesta tabela são gerenciados através do processo de Fornecimento de EPI, portanto, ao tentar realizar a inclusão utilizando esse dataserver, o sistema irá apresentar a seguinte mensagem:  "Não é possível realizar inserção, edição ou inclusão de empréstimo de EPI. Esses procedimentos devem ser realizados através do processo de Fornecimento de EPI." |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSYR29 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 11.82.42 |

divs
