---
content_hash: 03b760efe07dd7c89d9109af704e8d8fa53a46a7b1c78bee58bc8fe77a75de38
fetched_at: '2026-06-29T00:06:05.491903+00:00'
page_id: '201723056'
product: rm
source: tdn-rm
title: TSWERJ_DT_Reprogramacao_Avisos_Automaticos
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWERJ_DT_Reprogramacao_Avisos_Automaticos
version: 1
---

# AVISOS AUTOMÁTICOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | C&P |
| **Módulo:** | Totvs Folha de Pagamento |
| **Função:** | Avisos Automáticos |
| **Situação/Requisito:** | Servidor que executa o Host para envio de avisos automáticos eleva o consumo de recursos até o seu travamento |
| **Solução/Implementação:** | Foi proposto o ajuste na rotina afim de evitar o gargalo causado pelo consumo de recursos do servidor.  Desta forma estamos reprogramando os avisos automáticos (Tabela PPRGAVISO; campos DTULTEXEC, DTPROXEXEC) independente do sucesso na execução.  Entendemos que a rotina deverá ser revista para uma melhor avaliação das regras e arquitetura utilizada. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSWERJ |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 12.1.7 |
