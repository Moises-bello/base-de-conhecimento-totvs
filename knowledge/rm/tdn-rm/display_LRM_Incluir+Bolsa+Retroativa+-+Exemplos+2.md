---
content_hash: c6fbe2ead51bca52f218b3ae2a0e33e0238abcba8e78083be5d3aa77791fe021
fetched_at: '2026-06-29T00:09:36.845407+00:00'
page_id: '425459532'
product: rm
source: tdn-rm
title: Incluir Bolsa Retroativa - Exemplos 2
type: documentation
url: https://tdn.totvs.com/display/LRM/Incluir+Bolsa+Retroativa+-+Exemplos+2
version: 3
---

---

**1.2 – Dividir devolução pela quantidade de parcelas restantes**:

**Cenário 1:**− Contrato do aluno possui 6 parcelas no valor de 1000,00 cada.  
− Todos os lançamentos financeiros das 6 parcelas já foram gerados.  
− Somente o lançamento financeiro da parcela 1 já foi 'Baixado' e os outros ainda permanecem 'Em aberto'.  
− Foi incluída uma bolsa retroativa de 10% para as 6 parcelas deste contrato.  
**Resultado:**− Serão incluídos 6 lançamentos de devolução no valor de 100,00 cada referente às bolsas incluídas retroativamente.  
− Como a opção selecionada foi '*Dividir devolução pela quantidade de parcelas restantes'* serão automaticamente incluídos 'Vínculos' nos lançamentos das parcelas 'Em aberto' com os lançamentos de devolução criados com a inclusão da bolsa retroativa. O valor do 'Vínculo' incluído nos lançamentos corresponderá ao valor rateado do crédito de bolsa retroativa:  
Cálculos:  
• Valor total gerado de créditos de Bolsa Retroativa = 600,00 (6 x 100,00 referente a cada bolsa incluída)  
• Total de parcelas com lançamentos ainda 'Em aberto' = 5 (pois lançamento da parcela já foi 'Baixado')  
• Valor do 'Vínculo' incluído nos lançamentos das parcelas que estão 'Em aberto' = 120,00 (600 / 5 = 120,00)  
• Valor líquido dos lançamentos das parcelas que estão 'Em aberto' após o 'Vínculo' = 880,00 (1000,00 de valor original – 120,00 de crédito vinculado = 880,00)  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa Retroativa | Vínculo criado no Lcto da parcela | Valor líquido da parcela | Lcto de Devolução (L) |
| P1 = 1000,00 | Baixado | 10% = 100,00 (L1) | - | 1000,00 | L1 = 100,00 (100 / 5 = 20,00 vinculado em cada parcela) |
| P2 = 1000,00 | Em aberto | 10% = 100,00 (L2) | L1, L2, L3, L4, L5, L6 | 880,00 | L2 = 100,00 (100 / 5 = 20,00 vinculado em cada parcela) |
| P3 = 1000,00 | Em aberto | 10% = 100,00 (L3) | L1, L2, L3, L4, L5, L6 | 880,00 | L3 = 100,00 (100 / 5 = 20,00 vinculado em cada parcela) |
| P4 = 1000,00 | Em aberto | 10% = 100,00 (L4) | L1, L2, L3, L4, L5, L6 | 880,00 | L4 = 100,00 (100 / 5 = 20,00 vinculado em cada parcela) |
| P5 = 1000,00 | Em aberto | 10% = 100,00 (L5) | L1, L2, L3, L4, L5, L6 | 880,00 | L5 = 100,00 (100 / 5 = 20,00 vinculado em cada parcela) |
| P6 = 1000,00 | Em aberto | 10% = 100,00 (L6) | L1, L2, L3, L4, L5, L6 | 880,00 | L6 = 100,00 (100 / 5 = 20,00 vinculado em cada parcela) |
|  | | | | | Total = 600,00 sendo 120,00 vinculado em cada parcela            ( 6 (L) x 20,00 = 120,00 ) |

**Cenário 2 – \* Parte 1:**Contrato do aluno possui 6 parcelas no valor de 1000,00 cada.  
− Somente o lançamento financeiro da parcela 1 já foi gerado e está 'Baixado'  
− Os lançamentos financeiros das outras parcelas ainda não foram gerados.  
− Foi incluída uma bolsa retroativa de 10% para as 6 parcelas deste contrato.  
**Resultado:**− Será incluído somente 1 lançamento de devolução no valor de 100,00 referente à bolsa incluída para a única parcela (P1) que possui lançamento financeiro gerado e baixado.  
− Como não há parcelas com lançamentos financeiros gerados 'Em aberto', não foi criado 'Vínculo'.  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa Retroativa | Bolsa Comum | Vínculo criado no Lcto da parcela | Valor líquido da parcela | Lcto de Devolução (L) |
| P1 = 1000,00 | Baixado | 10% = 100,00 (L1) |  | - | 1000,00 | L1 = 100,00 (não foi criado vínculo) |
| P2 = 1000,00 | - |  | \*  10% = 100,00 |  |  |  |
| P3 = 1000,00 | - |  | \*  10% = 100,00 |  |  |  |
| P4 = 1000,00 | - |  | \*  10% = 100,00 |  |  |  |
| P5 = 1000,00 | - |  | \*  10% = 100,00 |  |  |  |
| P6 = 1000,00 | - |  | \*  10% = 100,00 |  |  |  |

                                                                                     \* No momento da geração do lançamento financeiro das parcelas, as bolsas serão aplicadas normalmente.

**Cenário 2 – \* Parte 2:**− O lançamento financeiro da parcela 2 foi gerado e está 'Em aberto'.  
**Resultado:**− Lançamento financeiro da parcela 2 foi gerado considerando-se o valor da bolsa de 10% aplicada anteriormente (parcela 1 à parcela 6), com isto o valor líquido da parcela 2 foi de 900,00 (1000,00 – 10% = 900,00), além disso, como a opção selecionada foi '*Dividir devolução pela quantidade de parcelas restantes',* no lançamento financeiro criado para a parcela 2 foi automaticamente incluído um 'Vínculo' de 20,00 com o lançamento de devolução criado anteriormente (valor do crédito correspondente à parcela = 100 / 5 = 20,00).  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa Retroativa | Bolsa Comum | Vínculo criado no Lcto da parcela | Valor líquido da parcela | Lcto de Devolução (L) |
| P1 = 1000,00 | Baixado | 10% = 100,00 (L1) |  | - | 1000,00 | L1 = 100,00 (100 / 5 = 20,00 vinculado em cada parcela) |
| P2 = 1000,00 | Em aberto |  | \*  10% = 100,00 | L1 | (900,00 - 20,00)    880,00 |  |
| P3 = 1000,00 | - |  | \*  10% = 100,00 |  |  |  |
| P4 = 1000,00 | - |  | \*  10% = 100,00 |  |  |  |
| P5 = 1000,00 | - |  | \*  10% = 100,00 |  |  |  |
| P6 = 1000,00 | - |  | \*  10% = 100,00 |  |  |  |
|  | | | | | | 20,00 = valor a ser vinculado em cada parcela a ser gerada |

**Importante**: À medida que os lançamentos financeiros das parcelas forem sendo gerados, os 'Vínculos' serão criados com os valores restantes do crédito (P2 com L1 = 20,00. P3 com L1 = 20,00. P4 com L1 = 20,00. P5 com L1 = 20,00. P6 com L1 = 20,00.)
