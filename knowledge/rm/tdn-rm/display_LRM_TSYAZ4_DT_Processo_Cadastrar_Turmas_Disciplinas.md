---
content_hash: 07a50a5a3cfc2378508f5d88c8263ba73a36cabee1a6826eed10c27ed7cf48a5
fetched_at: '2026-06-29T00:06:02.944152+00:00'
page_id: '198950674'
product: rm
source: tdn-rm
title: TSYAZ4_DT_Processo_Cadastrar_Turmas_Disciplinas
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYAZ4_DT_Processo_Cadastrar_Turmas_Disciplinas
version: 1
---

# Processo de cadastro de turmas/disciplinas

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Cadastro de turmas/disciplinas* |
| **Situação/Requisito:** | *No processo de cadastro de turmas/disciplinas, caso seja informado uma data de início e uma data fim e, antes da execução do processo, esses valores forem apagados, é lançada uma exceção e o processo não é finalizado.* |
| **Solução/Implementação:** | *Ajustes no processo de cadastro de turmas/disciplinas para que, caso seja informado uma data de início ou uma data fim e, antes da execução do processo esses valores forem apagados, seja atribuído corretamente os valores ao parâmetros, permitindo a execução correta do processo.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSYAZ4* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.83.55* |
