---
content_hash: 0770c9da4f286ebfb4cc390c441002ca4cfd5cb4e670f61f22094bcd9d1c33f4
fetched_at: '2026-06-29T00:08:22.296255+00:00'
page_id: '269420846'
product: rm
source: tdn-rm
title: 185321_DT_Registro_Presenca_Alteracao_Horario_Etapa
type: documentation
url: https://tdn.totvs.com/display/LRM/185321_DT_Registro_Presenca_Alteracao_Horario_Etapa
version: 111
---

# REGISTRO DE PRESENÇA DO CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Registro de presença do candidato* |
| **Situação/Requisito:** | *Foi identificado que ao iniciar o processo de "registrar presença do candidato"  é exibido um erro não tratado informando falha no relacionamento de chave estrangeira que impede a execução do processo.* |
| **Solução/Implementação:** | *Foi identificado que o problema é causado quando o horário de uma etapa é alterado quando já existe registro de presença para candidatos no horário em questão. Sendo assim foi feito um ajuste que se a data ou horário de uma etapa for alterado o sistema irá verificar se já existem registros de presença para esta etapa, caso exista, não será permitido alterar a data e horário, alertando para o usuário.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | *N/A* |

divs
