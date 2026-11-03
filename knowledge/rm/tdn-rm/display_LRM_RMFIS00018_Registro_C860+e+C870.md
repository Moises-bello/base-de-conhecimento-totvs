---
content_hash: 67097a267f155f34b2f4544bd557014b1883cb09bfa3d3d0c716c3525530f6a8
fetched_at: '2026-06-29T00:09:09.235988+00:00'
page_id: '393354996'
product: rm
source: tdn-rm
title: RMFIS00018_Registro_C860 e C870
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00018_Registro_C860+e+C870
version: 3
---

# Geração do registro C860 e C870

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1 |
| **Ocorrência:** | Como gerar o registro C860 e 870 |
| **Ambiente:** | CorporeRM |
| **Passo a passo:** | De acordo com o manual do EFD Contribuições o registro C860 - Identificação do Equipamento SAT-CF- utilizado para escrituração pela pessoa jurídica, da receita da venda de bens e serviços mediante a emissão de cupom fiscal eletrônico – CF-e-SAT (código 59), conforme Ajuste SINIEF no 11, de 24 de setembro de 2010.  E registro C870 referente ao Resumo Diário de Documentos Emitidos por Equipamento SAT-Cf-e (Código 59) – PIS/Pasep e Cofins Registro para demonstração da receita consolidada e apuração das contribuições sociais, por equipamento SAT-CFe, referente aos documentos fiscais emitidos no período    O sistema selecionará lançamentos fiscais de saída com código modelo de documento 59 (SAT).      Será necessário preencher o campo "Número de Série do equipamento SAT" na aba Informações Adicionais - Outros do lançamento fiscal.      Os tributos PIS e Cofins devem estar destacados no Item do lançamento Fiscal.        Segue trecho do arquivo gerado:  |C860|59|123456789|20082018|555588|555588| |C870|00.000|5102|1000,00|0,00|01|1000,00|0,6500|6,50|01|1000,00|3,0000|30,00|2| |
| **Observações:** |  |
