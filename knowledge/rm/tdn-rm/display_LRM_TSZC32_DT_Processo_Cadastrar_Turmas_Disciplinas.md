---
content_hash: 072b4e56745882127204c579528e1ab3828633106e6ebccbe992964c9ae67aba
fetched_at: '2026-06-29T00:06:03.229471+00:00'
page_id: '198951428'
product: rm
source: tdn-rm
title: TSZC32_DT_Processo_Cadastrar_Turmas_Disciplinas
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZC32_DT_Processo_Cadastrar_Turmas_Disciplinas
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
| **Chamados relacionados:** | *TSZC32* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
