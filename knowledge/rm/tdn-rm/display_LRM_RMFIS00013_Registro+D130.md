---
content_hash: 9db1b9d3d2c342012e7afe5d3294e93997e4f72c86943550f5aca93c8a6419e5
fetched_at: '2026-06-29T00:08:52.331494+00:00'
page_id: '338381380'
product: rm
source: tdn-rm
title: RMFIS00013_Registro D130
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00013_Registro+D130
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.X. |
| **Ocorrência:** | Parametrização do Registro D130. |
| **Ambiente:** |  |
| **Passo a passo:** | Este registro tem por objetivo informar o complemento do Conhecimento de Transporte Rodoviário de Cargas (Código 08) e Conhecimento de Transporte de Cargas Avulso (Código 8B).    **Abaixo contém as orientações para correta geração do registro D130 (SPED FISCAL):**    1. O sistema considera lançamentos de saídas, Conhecimento de Transporte Rodoviário de Cargas ou  Conhecimento de Transporte de Cargas Avulso  2. O tipo de documento informado deverá conter o "Código do Modelo de Documento" como "08" ou "8B";  3. Os campos **COD\_MUN\_ORIG** e **COD\_MUN\_DEST** são preenchidos com informações da aba Coleta e Entrega conforme figura 02   Figura 01  Figura 02     Segue trecho do arquivo gerado após parametrizações:    |D100|1|0|C00002|08|00|1||111111111||21022018|21022018|||15000,00|0|0|15000,00|15000,00|2700,00|0||||| |D130|C00002||9|3106200|3106200||15000,00|0|0|0|0|15000,00|| |
| **Observações:** |  |
