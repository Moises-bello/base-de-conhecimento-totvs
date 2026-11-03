---
content_hash: e31481d72a84a88e8c55d7e8a5bd861479e6847c864d2a6a75b951493db7fe6e
fetched_at: '2026-06-29T00:06:16.258035+00:00'
page_id: '212894481'
product: rm
source: tdn-rm
title: TTHSBL_DT_Censo_Ensino_Superior_2015_Carga_Horaria_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHSBL_DT_Censo_Ensino_Superior_2015_Carga_Horaria_Aluno
version: 4
---

# CENSO DO ENSINO SUPERIOR 2015

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Atividades Acadêmicas* |
| **Função:** | *Censo do Ensino Superior* |
| **Situação/Requisito:** | *Circular nr° 100 divulgada pelo INEP informa que a partir do Censo de 2016 serão exigidas novas informações: Carga Horária prevista e já cumprida do curso do aluno; modificações na lista de tipos de remuneração para os professores visitantes..* |
| **Solução/Implementação:** | *O Assistente de preparação de dados sofreu as seguintes modificações: 1 -* *passou a verificar se os dados referentes à carga horária da Grade e da Disciplina dos alunos recenseados foi informada, relacionando os registros que omitem este dado e impedindo o avanço do processo. 2 - passou a registrar a carga horária já cumprida pelo aluno até a data de referência do Censo na tabela auxiliar *(SALUNOCURSOMEC)*  que é utilizada na geração do arquivo de exportação.*  *É importante salientar que as IE que utilizam o módulo de exportação de dados para o Censo do Ensino Superior, mesmo que controlem o cumprimento da grade acadêmica por outros critérios que não a Carga Horária, como Créditos ou Número de Disciplinas, devem registrar a Carga Horária das Grades e Disciplinas.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TTHSBL TTIN22* |
| **Requisito (ISSUE):** | **N/A*.* |
| **Versões/Release:** | *12.1.6* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
