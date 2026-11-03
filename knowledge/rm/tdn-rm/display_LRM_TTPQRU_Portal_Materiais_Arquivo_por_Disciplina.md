---
content_hash: 680d1f5e61c5e5862cc392f7fe4720bf91ea41eb71bdd3a838f937a9981c292a
fetched_at: '2026-06-29T00:06:16.842100+00:00'
page_id: '212900498'
product: rm
source: tdn-rm
title: TTPQRU_Portal_Materiais_Arquivo_por_Disciplina
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPQRU_Portal_Materiais_Arquivo_por_Disciplina
version: 2
---

# Portal - Materiais. Arquivo por disciplina

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Materiais. Arquivo por disciplina, portal.* |
| **Situação/Requisito:** | *Ao fazer upload de um material no menu administração do portal do professor e associar esse material a determinada turma, o material acaba sendo visualizado também por todas as turmas e não só a turma onde foi associado, no contexto de ensino básico.* |
| **Solução/Implementação:** | *Ajustes na visualização dos materiais, no contexto de ensino básico. O arquivo será visualizado apenas para os alunos da turma desde que o parâmetro "Visualizar apenas materiais de disciplinas com o status 'É uma disciplina em curso, para o contexto de ensino superior, ou 'Conta como aluno matriculado na turma', para o contexto de ensino básico, marcado'" esteja habilitado ([Configurações -> Parâmetros -> RM Portal -> RM Portal - Gerais -> Portal - Geral 4/5]). Além disso, para o contexto de ensino básico, todos os alunos que possuam uma matrícula na disciplina cujo status aponte para 'Conta como aluno matriculado na turma', visualizarão o arquivo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TTPQRU* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
|  |  |

divs
