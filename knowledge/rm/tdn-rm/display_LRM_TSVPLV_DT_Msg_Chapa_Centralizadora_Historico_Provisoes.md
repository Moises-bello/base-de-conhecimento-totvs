---
content_hash: e5bb81ce8695f87e121f32b220a3512e5940f244b0edcf135ed92707aa6d743a
fetched_at: '2026-06-29T00:06:02.915871+00:00'
page_id: '198950070'
product: rm
source: tdn-rm
title: TSVPLV_DT_Msg_Chapa_Centralizadora_Historico_Provisoes
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVPLV_DT_Msg_Chapa_Centralizadora_Historico_Provisoes
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
| **Chamados relacionados:** | *TSVPLV* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
