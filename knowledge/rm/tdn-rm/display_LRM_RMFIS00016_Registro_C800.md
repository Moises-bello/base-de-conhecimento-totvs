---
content_hash: 1c784336dc78bccca77759d398ec471c9353ad774c26a9f3117d281f0bb155a0
fetched_at: '2026-06-29T00:09:09.239436+00:00'
page_id: '393355375'
product: rm
source: tdn-rm
title: RMFIS00016_Registro_C800
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00016_Registro_C800
version: 4
---

# Geração do registro C800

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1 |
| **Ocorrência:** | Como gerar o registro C800 |
| **Ambiente:** | CorporeRM |
| **Passo a passo:** | De acordo com o manual do Sped Fiscal o Registro C800 refere-se a CUPOM FISCAL ELETRÔNICO – SAT (CF-E-SAT) (CÓDIGO 59) e deve ser gerado para cada CF-e-SAT (Código 59) emitido por equipamento SAT-CF-e, conforme Ajuste SINIEF no 11, de 24 de setembro de 2010    O sistema irá considerar os lançamentos de Saída que possuem o código modelo de documento 59.      O campo ''Número de Série do equipamento SAT", em Informações Adicionais - Outros do lançamento fiscal deve estar preenchido.      A CFOP utilizada no lançamento fiscal deve ser do tipo Fiscal.      Segue trecho do arquivo gerado:  |C800|59|00|555588|20082018|1110,00|0|0||123456789||0|1000,00|0|70,00|0|0|  |C850|000|5102|7,00|1110,00|1000,00|70,00||    OBS: De acordo com o manual da rotina, os registros C860 (Identificação do equipamento SAT-CF-e (Código 59) ) e C890 (Resumo diário de CF-eSAT (Código 59) por equipamento SAT-CF-e )serão gerados apenas para os perfis B ou C.  Tela de geração da rotina:      Trecho do arquivo gerado com Perfil B  |C860|59|123456789|20082018|555588|555588| |C890|000|5102|7,00|1110,00|1000,00|70,00|| |
| **Observações:** |  |
