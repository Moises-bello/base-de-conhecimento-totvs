---
content_hash: 1b3ab554ece806906b63a8decd14fdb581cb9d0146026a432a53b630edd54094
fetched_at: '2026-06-29T00:12:10.666343+00:00'
page_id: '953003403'
product: rm
source: tdn-rm
title: Grupo S - COFINS
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+S+-+COFINS
version: 1
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo S - COFINS** | | | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | Campo de Origem | Campo na Aplicação | Mais Informações |
| 293 | S01 | COFINS | Grupo COFINS | G | M01 |  | 0-1 |  | Informar apenas um dos grupos S02, S03, S04 ou S04 com base valor atribuído ao campo de CST da COFINS |  |  |  |
| 294 | S02 | COFINSAliq | Grupo COFINS tributado pela alíquota | CG | S01 |  | 1-1 |  |  |  |  |  |
| 295 | S06 | CST | Código de Situação Tributária da COFINS | E | S02 | N | 1-1 | 2 | 01=Operação Tributável (base de cálculo = valor da operação alíquota normal (cumulativo/não cumulativo)); 02=Operação Tributável (base de cálculo = valor da operação (alíquota diferenciada)); | TTRBMOV.SITTRIBUTARIA |  |  |
| 296 | S07 | vBC | Valor da Base de Cálculo da COFINS | E | S02 | N | 1-1 | 13v2 |  | TTRBMOV.BASEDECALCULO |  |  |
| 297 | S08 | pCOFINS | Alíquota da COFINS (em percentual) | E | S02 | N | 1-1 | 3v2-4 |  | TTRBMOV.ALIQUOTA |  |  |
| 298 | S11 | vCOFINS | Valor da COFINS | E | S02 | N | 1-1 | 13v2 |  | TTRBMOV.VALOR |  |  |
| 299 | S03 | COFINSQtde | Grupo de COFINS tributado por Qtde | CG | S01 |  | 1-1 |  |  |  |  |  |
| 300 | S06 | CST | Código de Situação Tributária da COFINS | E | S03 | N | 1-1 | 2 | 03=Operação Tributável (base de cálculo = quantidade vendida x alíquota por unidade de produto); | TTRBMOV.SITTRIBUTARIA |  |  |
| 301 | S09 | qBCProd | Quantidade Vendida | E | S03 | N | 1-1 | 12v0-4 |  | TITMMOV.QUANTIDADE |  |  |
| 302 | S10 | vAliqProd | Alíquota da COFINS (em reais) | E | S03 | N | 1-1 | 11v0-4 |  | TTRBMOV.ALIQUOTAPORVALOR |  |  |
| 303 | S11 | vCOFINS | Valor da COFINS | E | S03 | N | 1-1 | 13v2 |  | TTRBMOV.VALOR |  |  |
| 304 | S04 | COFINSNT | Grupo COFINS não tributado | CG | S01 |  | 1-1 |  |  | Diferente do processo executado com o TSS, quando o tributo não existir no item de movimento não será declarado como 08, simplesmente não enviaremos a tag do tributo no XML da nota |  |  |
| 305 | S06 | CST | Código de Situação Tributária da COFINS | E | S04 | N | 1-1 | 2 | 04=Operação Tributável (tributação monofásica, alíquota zero); 05=Operação Tributável (Substituição Tributária); 06=Operação Tributável (alíquota zero); 07=Operação Isenta da Contribuição; 08=Operação Sem Incidência da Contribuição; 09=Operação com Suspensão da Contribuição; | TTRBMOV.SITTRIBUTARIA |  |  |
| 306 | S05 | COFINSOutr | Grupo COFINS Outras Operações | E | S01 | N | 1-1 |  |  |  |  |  |
| 307 | S06 | CST | Código de Situação Tributária da COFINS | E | S05 | N | 1-1 | 2 | 49=Outras Operações de Saída; 50=Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno; 51=Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Não Tributada no Mercado Interno; 52=Operação com Direito a Crédito – Vinculada Exclusivamente a Receita de Exportação; 53=Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno; 54=Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação; 55=Operação com Direito a Crédito - Vinculada a Receitas Não Tributadas no Mercado Interno e de Exportação; 56=Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação; 60=Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno; 61=Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno; 62=Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação; 63=Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno; 64=Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação; 65=Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação; 66=Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação; 67=Crédito Presumido - Outras Operações; 70=Operação de Aquisição sem Direito a Crédito; 71=Operação de Aquisição com Isenção; 72=Operação de Aquisição com Suspensão; 73=Operação de Aquisição a Alíquota Zero; 74=Operação de Aquisição; sem Incidência da Contribuição; 75=Operação de Aquisição por Substituição Tributária; 98=Outras Operações de Entrada; 99=Outras Operações; | TTRBMOV.SITTRIBUTARIA |  |  |
| 307.1 | S06.1 | -x- | Sequência XML | CG | S05 |  | 1-1 |  | Informar os campos S07 e S08 para cálculo da COFINS em percentual. |  |  |  |
| 308 | S07 | vBC | Valor da Base de Cálculo da COFINS | E | S06.1 | N | 1-1 | 13v2 | TTRBMOV.BASEDECALCULO |  |  |
| 309 | S08 | pCOFINS | Alíquota da COFINS (em percentual) | E | S06.1 | N | 1-1 | 3v2-4 | TTRBMOV.ALIQUOTA |  |  |
| 309.1 | S08.1 | -x- | Sequência XML | CG | S05 |  | 1-1 |  | Informar os campos S09 e S10 para cálculo da COFINS em valor. |  |  |  |
| 310 | S09 | qBCProd | Quantidade Vendida | E | S08.1 | N | 1-1 | 12v0-4 | TITMMOV.QUANTIDADE |  |  |
| 311 | S10 | vAliqProd | Alíquota da COFINS (em reais) | E | S08.1 | N | 1-1 | 11v0-4 | TTRBMOV.ALIQUOTAPORVALOR |  |  |
| 312 | S11 | vCOFINS | Valor da COFINS | E | S05 | N | 1-1 | 13v2 |  | TTRBMOV.VALOR |  |  |
