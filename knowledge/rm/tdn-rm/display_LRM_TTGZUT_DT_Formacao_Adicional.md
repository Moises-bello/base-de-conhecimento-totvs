---
content_hash: f73a592fad4bd5d6002c80fc50476df98c266435f0707a1f7d233916ee9e6a17
fetched_at: '2026-06-29T00:06:13.783469+00:00'
page_id: '208346436'
product: rm
source: tdn-rm
title: TTGZUT_DT_Formacao_Adicional
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGZUT_DT_Formacao_Adicional
version: 1
---

# FORMAÇÃO ADICIONAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Formação Adicional* |
| **Situação/Requisito:** | *O formato da carga horária na turma de treinamento (formato hora), após o encerramento da turma, é carregada para a formação adicional em formato inteiro, de modo que uma turma inferior a 1 hora tenha lançado na formação adicional o valor '0'.* |
| **Solução/Implementação:** | *Ajuste no campo Carga Horária no cadastro de Formação Adicional. Esse campo passa a ser do tipo TimeTextBox, permitindo o cadastro de horas e minutos. Também foi necessário a criação de um script para converter os registros já presentes no banco de dados, convertendo a Carga Horária da Formação Adicional de horas para minutos.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTGZUT* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |

divs
