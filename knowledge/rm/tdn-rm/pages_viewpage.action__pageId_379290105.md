---
content_hash: 2fa4246f10f3ee77fd511a0b493a75577bce9f4035e6eb4a28815b2d3b4eeb01
fetched_at: '2026-06-29T00:09:02.148710+00:00'
page_id: '379290105'
product: rm
source: tdn-rm
title: 3230527 DEDUINTEGRACOES-2692 DT Ajuste regra inclusão da bolsa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379290105
version: 1
---

# Cadastro de Bolsas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Inclusão/Alteração de Bolsas do Contrato do Aluno |
| **Situação/Requisito:** | O cliente sugere modificar a regra do sistema para que não considere na validação do percentual maior que 100% as bolsas que possuírem fórmula parametrizada, pois entendemos que o percentual será customizado pela fórmula cadastrada na bolsa, e neste caso a regra estará na fórmula. |
| **Solução/Implementação:** | A regra que valida se somatório das bolsas ultrapassou 100% somente é aplicada quando o sistema estiver parametrizado para que a classificação da bolsa seja por contrato e o tipo de classificação seja igual a somar bolsa e a bolsa seja do tipo percentual.   Evoluímos esta regra para que as bolsas que tenham fórmula parametrizada não sejam levadas em consideração, pois o percentual será customizado pela fórmula cadastrada na bolsa, e neste caso a regra estará na fórmula.   É importante ressaltar que a regra que valida se o somatório da bolsa ultrapassou 100% continua sendo aplicada na geração do lançamento, portanto a fórmula deve garantir que o percentual da bolsa seja ajustado de forma que o somatório dos percentuais das bolsas não ultrapassem 100%. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
| **Pacote:** | Informe o [linkdopacote] |
