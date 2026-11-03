---
content_hash: c12cd35205f4ea728889d9117236189b3afc817ee497f200e1ad83e252ac191e
fetched_at: '2026-06-29T00:08:45.792246+00:00'
page_id: '315895937'
product: rm
source: tdn-rm
title: 1563660 DEDUINTEGRACOES-924 DT Liberação de webservice EduConsultaRapidaExtratoFinanceiroData
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315895937
version: 93
---

# Webservice EduConsultaRapidaExtratoFinanceiroData

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Consumo do webservice EduConsultaRapidaExtratoFinanceiroData |
| **Situação/Requisito:** | No Link em que é apresentado a documentação do webservice "EduConsultaRapidaExtratoFinanceiroData" esta apresentando a mensagem de não conformidade abaixo:  Erro ao carregar Schema. Ocorreu um erro ao efetuar a leitura das definições da tabela: Incorrect syntax near 'FLAN'.  Link: [http://api.totvs.com.br/devrm/](http://api.totvs.com.br/devrm/ "Follow link") |
| **Solução/Implementação:** | Ajustamos uma não conformidade na consulta de SQL utilizada para montar o schema.  É importante ressaltar que como regra ao consumir o recurso ReadRecord somente será listado o extrato financeiro conforme o usuário informado no contexto, ou seja, deverá ser informado no usuário do contexto o usuário cadastrado para o RA do aluno que deseja visualizar o extrato financeiro. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
