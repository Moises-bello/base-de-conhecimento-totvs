---
content_hash: 4416b1bcd160bbe24817c2219acd5fee812380d2ff2b3952a9859e170d056d71
fetched_at: '2026-06-29T00:06:04.147033+00:00'
page_id: '200905930'
product: rm
source: tdn-rm
title: TT8306_DT_Geracao_de_Horario
type: documentation
url: https://tdn.totvs.com/display/LRM/TT8306_DT_Geracao_de_Horario
version: 1
---

# Geração de horários

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão**Educacional* |
| **Função:** | *Geração de horário* |
| **Situação/Requisito:** | *Ao executar o processo de geração de horário para turma é realizada uma validação de choque de horário do professor selecionado no processo. Existiam horários antigos cadastrados com a hora final igual a 24:00. Esse horário não existe e isso ocasionava erros ao realizar as conversões necessárias no processo.**.* |
| **Solução/Implementação:** | *Criado script para ajustes nas inconsistências encontradas. Os horários que possuem a hora final igual a 24:00 foram ajustados para 23:59, o último horário válido do dia.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TT8306* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.39* |
