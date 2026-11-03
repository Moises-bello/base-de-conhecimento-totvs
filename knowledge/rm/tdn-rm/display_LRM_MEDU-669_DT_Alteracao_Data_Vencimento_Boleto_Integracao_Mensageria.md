---
content_hash: 8e07c3c2b148c9485ced89633bbf51dcbce69ecd66fb5fef05807fd104742028
fetched_at: '2026-06-29T00:08:21.514069+00:00'
page_id: '268828598'
product: rm
source: tdn-rm
title: MEDU-669_DT_Alteracao_Data_Vencimento_Boleto_Integracao_Mensageria
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-669_DT_Alteracao_Data_Vencimento_Boleto_Integracao_Mensageria
version: 116
---

# ALTERAÇÃO DE DATA DE VENCIMENTO DE BOLETO NA INTEGRAÇÃO POR MENSAGERIA ÚNICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Alteração de data de vencimento de boleto* |
| **Situação/Requisito:** | *Alterações de datas de vencimento de boletos, na integração por mensageria única, não são abortadas quando é disparado um erro.*  *Essa alteração pode ser realizada no TOTVS Gestão Educacional para um boleto de uma parcela de um contrato ou no TOTVS Processo Seletivo para um boleto de uma inscrição de candidato.* |
| **Solução/Implementação:** | *Alteração no sistema para que o gatilho que envia a mensagem esteja dentro do sistema financeiro. Dessa forma, ao ocorrer um erro na integração, o mesmo é identificado e a operação é abortada.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | MEDU-813 |
| **Requisito (ISSUE):** | *N/A* |

divs
