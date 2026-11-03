---
content_hash: 4b16005eff9a6b95cece02f47b866f24af42ae9d942d8de26b48e623518657c9
fetched_at: '2026-06-29T00:06:25.950853+00:00'
page_id: '224453501'
product: rm
source: tdn-rm
title: TTZTGQ_DT_Geracao_Historico_Ensino_Basico
type: documentation
url: https://tdn.totvs.com/display/LRM/TTZTGQ_DT_Geracao_Historico_Ensino_Basico
version: 118
---

# GERAÇÃO DE HISTÓRICO PARA ENSINO BÁSICO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Geração de Histórico para Ensino Básico* |
| **Situação/Requisito:** | *Ao importar o histórico dos alunos marcando a opção para usar carga horária da disciplina, o sistema mostra o somatório da carga horária inferior ao valor que deveria ser. Foi verificado que o sistema não leva em consideração as disciplinas que possuem faltas nulas no momento da importação do histórico.* |
| **Solução/Implementação:** | *Ajuste no processo de geração de histórico, alterando-se a consulta, para que seja considerado as faltas que ainda não foram lançadas, ou seja, faltas que não possuem registro no banco de dados.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.9.104* |
| **Versão Expedida:** | *12.1.9.104* |

divs
