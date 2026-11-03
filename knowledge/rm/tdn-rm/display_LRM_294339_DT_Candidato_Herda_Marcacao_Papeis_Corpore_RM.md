---
content_hash: 3242112c94e88d8a4dde4042b07be084a8c39859d97caed636aea3103737e998
fetched_at: '2026-06-29T00:08:23.867024+00:00'
page_id: '270096564'
product: rm
source: tdn-rm
title: 294339_DT_Candidato_Herda_Marcacao_Papeis_Corpore_RM
type: documentation
url: https://tdn.totvs.com/display/LRM/294339_DT_Candidato_Herda_Marcacao_Papeis_Corpore_RM
version: 112
---

# CADASTRO DE CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo - Portal* |
| **Função:** | *Inscrição* |
| **Situação/Requisito:** | *Quando é feito o cadastro de um candidato após o cadastro do responsável e este responsável já existe, sendo que este responsável possui algum papel no sistema (Aluno, candidato RH, funcionário, ex-funcionário ou professor), estes papeis são copiados para o cadastro do novo candidato (nova pessoa), o candidato não é criado como aluno nem nas demais funções, é somente copiada a marcação das colunas do banco de dados do cadastro de pessoa que fazem referência as funções do sistema.* |
| **Solução/Implementação:** | *Foi identificado que o cadastro herda os datasets do responsável anterior, sendo assim, os campos das funções estão preenchidos com as funções do responsável, para solução foi inserido uma validação que identifica se o cadastro do candidato é para uma nova pessoa, se for identificado que é uma nova pessoa, os campos que identificam as funções do cadastro de pessoa são alterados para o valor inicial que identifica que identifica que não há função.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
