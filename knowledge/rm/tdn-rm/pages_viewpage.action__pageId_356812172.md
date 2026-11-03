---
content_hash: ea2855934da8c4f624bfdb6d17af7e2bdcfe975cbb4b0ac04800e12e0c2286e4
fetched_at: '2026-06-29T00:08:57.813037+00:00'
page_id: '356812172'
product: rm
source: tdn-rm
title: FISCAL01-4363 DT Integração TAF x RM Reg. T154 (Faturas)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=356812172
version: 4
---

# Integração RM x TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Registros para Integração TAF |
| **Situação/Requisito:** | Gerar os registros T154, T154AA e T154AF |
| **Solução/Implementação:** | Foi implementado o registro T154, T154AA e T154AF no Layout TAF.  **Dicas para geração do registro:**  Serão selecionados os movimentos cuja a parametrização "**Movimentos de Repasse EFD Reinf**" estiver marcada.    O registro **T154** será gerado com os dados do movimento  O registro **T154AA** será gerado com os dados do item do movimento  O registro **T154AF** será gerado com os dados do processo vinculado ao movimento  O registro **T003** campo IND\_ASSOC\_DESPORT será gerado com valor fixo "1 - Sim" para os participantes cuja origem for o T154  O registro **T001** campo IND\_ASSOC\_DESPORT será gerado com valor "1 - Sim" se a filial estiver parametrizada como Associação desportiva    O registro **T001** campo IND\_PROD\_RURAL será gerado com valor "1 - Sim" se a filial estiver parametrizada como Produtor Rural. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Requisito:** | FIS000408 |
| **Documento de Referência:** |  |
