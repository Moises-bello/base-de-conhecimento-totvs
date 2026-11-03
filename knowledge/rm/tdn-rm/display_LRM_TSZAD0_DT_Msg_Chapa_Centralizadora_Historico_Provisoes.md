---
content_hash: 12082af8e290f0066e1631e7bf17c5078521e61d191fdae5ddfb7bc5f82a3c79
fetched_at: '2026-06-29T00:06:02.920072+00:00'
page_id: '198950129'
product: rm
source: tdn-rm
title: TSZAD0_DT_Msg_Chapa_Centralizadora_Historico_Provisoes
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZAD0_DT_Msg_Chapa_Centralizadora_Historico_Provisoes
version: 1
---

# HISTÓRICO DE PROVISÕES EXIBINDO MSG CHAPA CENTRALIZADORA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração do Histórico de Provisões* |
| **Situação/Requisito:** | *Mensagem de erro relacionada à obrigatoriedade de recalcular a chapa centralizadora de múltiplos vínculos está sendo exibida na geração do histórico de provisões.*  *Neste módulo não deve aparecer esta mensagem porque não ocorre cálculo dos encargos INSS e IRRF.* |
| **Solução/Implementação:** | *Ajustar a consistência de recálculo da chapa centralizadora de múltiplos vínculos, para não retornar erro no processo de geração do histórico de provisões.*  *Neste módulo nunca deve ser exibida a mensagem: "A chapa 00004, que é centralizadora de IRRF do funcionário 09856 não foi selecionada para o processo. O funcionário 00004 deverá ser recalculado para que o IRRF fique correto."* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSZAD0* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
