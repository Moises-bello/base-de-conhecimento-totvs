---
content_hash: 9ea20256fa87a1fd1b3821959110e5e8969a9fb4d1a5e0ac3d48a9c0fe323c3b
fetched_at: '2026-06-29T00:06:12.581525+00:00'
page_id: '205917870'
product: rm
source: tdn-rm
title: TTKKS0_DataServer_RhuEmprestimoEPIData
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKKS0_DataServer_RhuEmprestimoEPIData
version: 1
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
| **Chamados relacionados:** |  |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 12.1.8 |

divs
