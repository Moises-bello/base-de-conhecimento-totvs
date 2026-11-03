---
content_hash: c929ca7f644ae97873f2e10e25f87a89d87700f0e50bbc086f3ca190e750808e
fetched_at: '2026-06-29T00:08:32.032290+00:00'
page_id: '273982116'
product: rm
source: tdn-rm
title: 732350 EDUCACIONAL01-151 DT Inscrição na vaga de emprego de alunos de egresso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273982116
version: 111
---

# Candidatos à Vaga de Estágio

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Inscrição de alunos a vaga de emprego ou estágio |
| **Situação/Requisito:** | Ao tentar realizar inscrição de um egresso a uma vaga de emprego o sistema não retornou o egresso.   Este cenário ocorre nos casos em que o Aluno tem habilitação com a situação de matricula que indica a conclusão do curso (opção marcada no cadastro da situação de matricula) e não tem nenhuma matricula no curso.  Isto acontece nos casos de clientes que importaram informações de outro sistema e controlam o egresso somente colocando a habilitação e o status de matricula como formado. |
| **Solução/Implementação:** | Realizado uma melhoria para que seja possível cadastrar um aluno de egresso em uma vaga de emprego mesmo que ele não tenha histórico de matricula naquele curso.  Regras para permitir:  - A vaga tem que ser de emprego  - No cadastro do aluno tem que ter a habilitação conforme o perfil da vaga, e a situação de matricula que consta no cadastro tem que estar marcada com a opção que indica a conclusão do curso. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 732350 |
| **Requisito:** |  |

divs
