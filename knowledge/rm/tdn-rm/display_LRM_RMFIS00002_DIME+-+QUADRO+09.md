---
content_hash: 15934a8f25051c8cd3bc1ce8a89602c1131e070625645f88676f71dab11d79eb
fetched_at: '2026-06-29T00:08:47.981690+00:00'
page_id: '321297579'
product: rm
source: tdn-rm
title: RMFIS00002_DIME - QUADRO 09
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00002_DIME+-+QUADRO+09
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.X |
| **Ocorrência:** | Registro 30- Somatório dos pagamentos de ICMS diferente do informado no imposto a recolher do quadro 9. |
| **Ambiente:** |  |
| **Passo a passo:** | O erro ocorre pois, no Registro 30 gerou valor de imposto à pagar e o Registro 33 não foi gerado.        **Solução**: Para gerar o registro 33 é necessário gerar a guia automática.          Segue trecho do arquivo gerado:    300901000000000001200000 300904000000000001200000 300905000000000000737851 300908000000000000737851 300912000000000000462149 300999900000000000462149 331210800201220170000000000046214900000000000000000000 |
| **Observações:** |  |
