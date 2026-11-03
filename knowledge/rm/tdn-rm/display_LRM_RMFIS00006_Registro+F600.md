---
content_hash: f5b0a3a7bf2ea2c7491c54ec1d70b841508fdb3f7d0cd544ef3a2f167c107f61
fetched_at: '2026-06-29T00:08:41.337800+00:00'
page_id: '286721164'
product: rm
source: tdn-rm
title: RMFIS00006_Registro F600
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00006_Registro+F600
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.7 |
| **Ocorrência:** | Parametrização do Registro F600 - EFD Contribuições. |
| **Ambiente:** |  |
| **Passo a passo:** | Segue abaixo consistências para correta geração do registro F600 no arquivo EFD Contribuições     * Lançamento financeiro a **receber**;       -Tributos COFINS RF (TIPOTRIBFISC” igual a 20), PIS RF (TIPOTRIBFISC” igual a 19), CSRF (TIPOTRIBFISC” igual a 21) destacados no lançamento financeiro na aba de **Valores →** sub aba **Tributos** e deve conter código de retenção informado;      -Para correto preenchimento do campo 07 Indicador da Natureza da Receita, na aba de integração fiscal o campo indicador da natureza da receita deve ser preenchido;        -O lançamento deve estar baixado e a data da baixa deve compreender o período de geração da rotina;        **Não é necessário realizar o processo do Cálculo dos Documentos não Escriturados.**    Segue abaixo resultado do exemplo:    |F001|0|  |F010|21867387000158|  |F600||31082017|8000,00|292,00|5979|0|26020453000173|52,00|0,00|0|  |F600||31082017|8000,00|292,00|5960|0|26020453000173|0,00|240,00|0|  |F990|5| |
| **Observações:** |  |
