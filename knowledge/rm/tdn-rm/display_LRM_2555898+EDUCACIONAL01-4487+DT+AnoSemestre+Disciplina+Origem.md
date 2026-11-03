---
content_hash: d745247511286812c32197f86b68abc96cb0747596448e8d6d97eae9115ff7e0
fetched_at: '2026-06-29T00:08:55.376664+00:00'
page_id: '348299670'
product: rm
source: tdn-rm
title: 2555898 EDUCACIONAL01-4487 DT AnoSemestre Disciplina Origem
type: documentation
url: https://tdn.totvs.com/display/LRM/2555898+EDUCACIONAL01-4487+DT+AnoSemestre+Disciplina+Origem
version: 88
---

# DISCIPLINA DE ORIGEM

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Disciplina de origem* |
| **Situação/Requisito:** | ``` Foi identificado uma inconsistência ao abrir a tela de análise curricular, era informado um mensagem relacionada ao tamanho do campo da base de dados. ``` |
| ``` Solução/Implementação: ``` | ``` Foi identificado que o problema estava relacionado com o campo "Ano/Semestre" na tela de disciplina de origem (Curso/Habilitação -> Aproveitamento de Estudos -> Anexos -> Disciplinas de Origem), este campo suportava mais de 10 caracteres, ```  ``` sendo que ao executar a análise curricular, este campo é utilizado e excedia o limite da análise curricular, foi feito o ajuste e o campo. ``` |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
