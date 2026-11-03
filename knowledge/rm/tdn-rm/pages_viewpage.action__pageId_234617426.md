---
content_hash: 1fc4f0cb0fcefaca6ed8ae4b2ac3068a8307e2a68f8cd6638d7f0e2689bcf9dd
fetched_at: '2026-06-29T00:06:29.728392+00:00'
page_id: '234617426'
product: rm
source: tdn-rm
title: TTSDJI_DT_Gerar_Contabilização_Contrato_Sem_Parcela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234617426
version: 120
---

# GERAR CONTABILIZAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Educacional |
| **Função:** | Gerar Contabilização |
| **Situação/Requisito:** | Ao gerar a contabilização para um contrato que não possui parcelas, ocorria mensagem: Erro na seleção de registros de parcelas. Mensagem: Incorrect syntax near ')'. |
| **Solução/Implementação:** | Alterado processo de Gerar Contabilização, quando um contrato  não possui parcelas, ocorria mensagem: Erro na seleção de registros de parcelas. Mensagem: Incorrect syntax near ')'. Para um melhor entendimento, foi alterado a mensagem para:   Não existem parcelas cadastradas para o contrato 1070.   Não foi possível gerar a contabilização. Não existe nenhuma parcela cadastrada no(s) contrato(s) selecionados(s). |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | TUNKPN |
| **Requisito (ISSUE):** | *NA* |

divs
