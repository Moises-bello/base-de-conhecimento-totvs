---
content_hash: d8f06c7b9e8909b8abd936fa80860ccc9636190aaeece645b15959011984a491
fetched_at: '2026-06-29T00:08:22.710840+00:00'
page_id: '269438273'
product: rm
source: tdn-rm
title: MEDU-903_DT_Copia_Processo_Seletivo_Alocacao_Automatica_Profissionais
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-903_DT_Copia_Processo_Seletivo_Alocacao_Automatica_Profissionais
version: 113
---

# COPIAR PROCESSO SELETIVO - ALOCAÇÃO AUTOMÁTICA DE PROFISSIONAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Copiar processo seletivo - alocação automática de profissionais* |
| **Situação/Requisito:** | *Foi identificado que ao executar o processo de cópia de processo seletivo utilizando a opção para copiar também os locais do processo seletivo e alocar automaticamente os profissionais, mesmo que um local utilize um tipo de profissional que não tenha nenhum profissional cadastrado o processo exibe o log informando que foram alocados profissionais para locais que não possuem candidatos.* |
| **Solução/Implementação:** | *Foi feito um ajuste na montagem do log que só exibirá a mensagem informando que foram alocados profissionais em locais que não possuem candidatos caso realmente sejam alocados profissionais para este local.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
