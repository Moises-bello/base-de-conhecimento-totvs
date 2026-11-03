---
content_hash: a534e2fa7484771f49d68de823318a7fc3d3b3005e9b0f3a3e14f6c36906a0ba
fetched_at: '2026-06-29T00:06:00.539547+00:00'
page_id: '196810572'
product: rm
source: tdn-rm
title: TSVVLU_DT_Reprogramacao_Avisos_Automaticos
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVVLU_DT_Reprogramacao_Avisos_Automaticos
version: 3
---

# AVISOS AUTOMÁTICOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | C&P |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Avisos Automáticos |
| **Situação/Requisito:** | Servidor que executa o Host para envio de avisos automáticos eleva o consumo de recursos até o seu travamento |
| **Solução/Implementação:** | Foi proposto o ajuste na rotina afim de evitar o gargalo causado pelo consumo de recursos do servidor.  Desta forma estamos reprogramando os avisos automáticos (Tabela PPRGAVISO; campos DTULTEXEC, DTPROXEXEC) independente do sucesso na execução.  Entendemos que a rotina deverá ser revista para uma melhor avaliação das regras e arquitetura utilizada. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** |  |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 11.82.40 |
