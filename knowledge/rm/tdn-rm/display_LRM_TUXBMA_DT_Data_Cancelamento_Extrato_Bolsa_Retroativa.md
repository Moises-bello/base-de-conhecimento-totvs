---
content_hash: 6619ee4cecee6012cd9541e591f2621d8c23f942652b0b3f70d47deb41b5a971
fetched_at: '2026-06-29T00:08:07.886482+00:00'
page_id: '237396404'
product: rm
source: tdn-rm
title: TUXBMA_DT_Data_Cancelamento_Extrato_Bolsa_Retroativa
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXBMA_DT_Data_Cancelamento_Extrato_Bolsa_Retroativa
version: 115
---

# INCLUSÃO/EXCLUSÃO DE BOLSA RETROATIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Inclusão/Exclusão de bolsa retroativa* |
| **Situação/Requisito:** | *Ao executar inclusão de bolsa retroativa, o sistema está fixando data de cancelamento de extrato de caixa igual à data do sistema.* |
| **Solução/Implementação:** | Criado novo parâmetro Educacional Integração | Financeiro - "Data de cancelamento de extrato igual à data de baixa, ao reconciliar extrato no processo de inclusão/exclusão de bolsa retroativa.  Caso esteja marcado, a data de cancelamento de extrato ficará igual à data da baixa. O default é estar desmarcado e neste caso irá gravar a data atual do sistema como data de cancelamento de extrato.     Este parâmetro somente ficará habilitado se estiver marcado o campo "Refaz automaticamente conciliação de extrato no processo de inclusão/exclusão de bolsa retroativa". |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | *N/A* |

divs
