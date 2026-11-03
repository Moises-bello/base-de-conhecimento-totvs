---
content_hash: d99b6721f138f04764c93d34abd009a8939ae2bc656d19bae032412d398fb35f
fetched_at: '2026-06-29T00:09:36.755218+00:00'
page_id: '425459516'
product: rm
source: tdn-rm
title: Incluir Bolsa Retroativa - Exemplo 1
type: documentation
url: https://tdn.totvs.com/display/LRM/Incluir+Bolsa+Retroativa+-+Exemplo+1
version: 10
---

---

**1.1 –** **Aplicar devolução no lançamento da primeira parcela em aberto**:

**Cenário 1:**  
Contrato do aluno possui 6 parcelas no valor de 1000,00 cada.  
− Todos os lançamentos financeiros das 6 parcelas já foram gerados.  
− Somente o lançamento financeiro da parcela 1 já foi 'Baixado' e os outros ainda permanecem 'Em aberto'.  
− Foi incluída uma bolsa retroativa de 10% para as 6 parcelas deste contrato.  
**Resultado:**− Serão incluídos 6 lançamentos de devolução no valor de 100,00 cada referente às bolsas incluídas retroativamente.  
− Neste contrato o lançamento financeiro da parcela 2 é o primeiro lançamento que se encontra 'Em aberto' e como a opção selecionada foi '*Aplicar devolução no lançamento da primeira parcela em aberto*' será então incluído um 'Vínculo' neste lançamento com os lançamentos de devolução criados com a inclusão da bolsa retroativa. Assim, este lançamento passará a ter um valor líquido de 400,00 (Valor original = 1000,00. Valor das devoluções = 100,00 cada = 600,00 no total. Valor líquido = 1000,00 – 600,00 = 400,00).  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

**Importante**:   
− No momento da baixa do lançamento financeiro da parcela 2 será feita a baixa dos lançamentos de devolução.  
− Em lançamentos financeiros com status = 'Baixado' não haverá a inclusão de 'Vínculos' como foi o caso do lançamento financeiro da parcela 1.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa Retroativa | Vínculo criado no Lcto da parcela | Valor líquido da parcela | Lcto de Devolução (L) |
| P1 = 1000,00 | Baixado | 10% = 100,00 | - | 1000,00 | L1 = 100,00 |
| P2 = 1000,00 | Em aberto | 10% = 100,00 | L1, L2, L3, L4, L5, L6 | (1000,00 – 600,00)=400,00 | L2 = 100,00 |
| P3 = 1000,00 | Em aberto | 10% = 100,00 |  | 1000,00 | L3 = 100,00 |
| P4 = 1000,00 | Em aberto | 10% = 100,00 |  | 1000,00 | L4 = 100,00 |
| P5 = 1000,00 | Em aberto | 10% = 100,00 |  | 1000,00 | L5 = 100,00 |
| P6 = 1000,00 | Em aberto | 10% = 100,00 |  | 1000,00 | L6 = 100,00 |

**Cenário 2:**Contrato do aluno possui 6 parcelas sendo:  
− Parcela 1 no valor de 1000,00. Lançamento financeiro já foi gerado e já foi 'Baixado'.  
− Parcelas 2 a 6 no valor de 100,00 cada. Lançamentos financeiros já foram gerados e ainda estão 'Em aberto'.   
− Foi incluída uma bolsa retroativa de 10% para as 6 parcelas deste contrato.  
**Resultado:**− Serão incluídos 6 lançamentos de devolução, sendo o primeiro no valor de 100,00 e mais 5 no valor de 10,00 cada referente às bolsas incluídas retroativamente.  
− A parcela 2 deste contrato é a primeira parcela cujo lançamento financeiro está 'Em aberto' e, como a opção selecionada foi '*Aplicar devolução no lançamento da primeira parcela em aberto*', será então incluído um 'Vínculo' neste lançamento com os lançamentos de devolução criados com a inclusão da bolsa retroativa. O valor do 'Vínculo' será neste lançamento o valor máximo possível (100,00):  
Cálculos:  
• Valor total gerado de créditos de Bolsa Retroativa = 150,00 (100,00 + 5 x 10,00 cada referente às bolsas incluídas)  
• Valor do 'Vínculo' criado no lançamento da parcela 2 que está em aberto = 100,00 (valor máximo permitido conforme o valor líquido da parcela que é = 100,00)  
• Valor líquido do lançamento da parcela 2 após o 'Vínculo' = 0,00 (100,00 de valor original – 100,00 de crédito vinculado)  
− A parcela 3 deste contrato é a próxima parcela cujo lançamento financeiro está 'Em aberto'. Como na parcela 2 já foram aproveitados 100,00 como valor máximo possível, na parcela 3 será vinculado o valor máximo possível do crédito restante:  
Cálculos:  
• Valor restante de créditos de Bolsa Retroativa = 50,00 (150,00 – 100,00 que já foram utilizados no lançamento da parcela 2)  
• Valor do 'Vínculo' criado no lançamento da parcela 3 que está em aberto = 50,00  
• Valor líquido do lançamento da parcela 3 após o 'Vínculo' = 50,00 (100,00 de valor original – 50,00 de crédito vinculado)  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

**Importante**: Ao baixar os lançamentos referentes às parcelas 2 e 3, os lançamentos de devolução que estão vinculados à estes, serão baixados automaticamente.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa Retroativa | Vínculo criado no Lcto da parcela | Valor líquido Lcto da parcela | Lcto de Devolução (L) |
| P1 = 1000,00 | Baixado | 10% = 100,00 (L1) | - | 1000,00 | L1 = 100,00 |
| P2 =   100,00 | Em aberto | 10% =   10,00 (L2) | L1 | 0,00 | L2 =   10,00 |
| P3 =   100,00 | Em aberto | 10% =   10,00 (L3) | L2, L3, L4, L5, L6 | 50,00 | L3 =   10,00 |
| P4 =   100,00 | Em aberto | 10% =   10,00 (L4) |  | 100,00 | L4 =   10,00 |
| P5 =   100,00 | Em aberto | 10% =   10,00 (L5) |  | 100,00 | L5 =   10,00 |
| P6 =   100,00 | Em aberto | 10% =   10,00 (L6) |  | 100,00 | L6 =   10,00 |

**Cenário 3 - \* Parte 1**'Contrato 1' do aluno possui 6 parcelas no valor de 1000,00 cada.  
− Todos os lançamentos financeiros das 6 parcelas já foram gerados.  
− Somente o lançamento financeiro da parcela **6** ainda está 'Em aberto', os outros foram todos 'Baixados'.  
− Foi incluída uma bolsa retroativa de 50% para as 6 parcelas deste contrato.  
**Resultado:**− Serão incluídos 6 lançamentos de devolução no valor de 500,00 cada referente às bolsas incluídas retroativamente.  
− Neste 'Contrato 1' somente o lançamento financeiro da parcela 6 se encontra 'Em aberto' e como a opção selecionada foi '*Aplicar devolução nas próximas parcelas*' será então incluído um *'Vínculo'* neste lançamento com os lançamentos de devolução criados com a inclusão da bolsa retroativa no valor máximo permitido. Assim, este lançamento passará a ter um valor líquido de 0,00 (Valor original = 1000,00 - Valor das devoluções vinculadas 1000,00 (L1: 500,00 + L2: 500,00).  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

**Importante**: No momento da baixa do lançamento financeiro da parcela 6 será feita a baixa automática dos lançamentos de devolução L1 e L2, pois estarão sendo abatidos neste momento.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Parcelas   **Contrato 1** | Status do Lcto da parcela | Bolsa Retroativa | Vínculo criado no Lcto da parcela | Valor líquido Lcto da parcela | Lcto de Devolução (L) |  |
| P1 = 1000,00 | Baixado | 50% = 500,00 (L1) | - | 1000,00 | L1 = 500,00 |  |
| P2 = 1000,00 | Baixado | 50% = 500,00 (L2) | - | 1000,00 | L2 = 500,00 | Reparem: |
| P3 = 1000,00 | Baixado | 50% = 500,00 (L3) | - | 1000,00 | L3 = 500,00 \* | \*Este valor será 'Vinculado' na (P1) do próximo contrato |
| P4 = 1000,00 | Baixado | 50% = 500,00 (L4) | - | 1000,00 | L4 = 500,00 \* | \*Este valor será 'Vinculado' na (P1) do próximo contrato |
| P5 = 1000,00 | Baixado | 50% = 500,00  (L5) | - | 1000,00 | L5 = 500,00 \* | \*Este valor será 'Vinculado' na (P2) do próximo contrato |
| P6 = 1000,00 | Em aberto | 50% = 500,00 (L6) | L1  e  L2 | (1000-L1-L2)      0,00 Status = 'Baixado' | L6 = 500,00 \* | \*Este valor será 'Vinculado' na (P2) do próximo contrato |
|  | | | | | Saldo Devolução pendente = 2000,00 (3000,00 - L1 - L2) que serão utilizados no **Contrato 2** |  |

**Cenário 3 - \* Parte 2:**− Baixa realizada na parcela 6 do 'Contrato **1**' que agora está *finalizado* (todos os lançamentos financeiros das parcelas do 'Contrato **1**' estão agora 'Baixados').  
− Incluído o 'Contrato **2**' para o aluno.  
− Todos os lançamentos financeiros das 6 parcelas do 'Contrato **2**' foram gerados.  
**Resultado:**− Como a opção '*Usar devoluções pendentes após término de contrato nos próximos contratos'*, previamente parametrizada em *Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Bolsa Retroativa 1/3* está *marcada*, foram criados 'Vínculos' automaticamente nos lançamentos financeiros da parcela 1 e da parcela 2 com o valor máximo permitido em cada parcela ('Vínculo' na parcela 1 com o L3 = 500,00 e L4 = 500,00 e 'Vínculo' na parcela 2 com o L5 = 500,00 e L6 = 500,00), assim o valor do crédito de Bolsa Retroativa do 'Contrato **1**' foi finalizado.  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do 'Contrato 1' e 'Contrato 2' do aluno e também da bolsa no 'Contrato 1' serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |
| --- | --- | --- | --- |
| Parcelas   **Contrato 2** | Status do Lcto da parcela | Vínculo criado no Lcto da parcela | Valor líquido Lcto da parcela |
| P1 = 1000,00 | Em aberto | L3 \*  e   L4 \* | (1000 - L1 - L2)        0,00 |
| P2 = 1000,00 | Em aberto | L5 **e   L6** | (1000 - L1 - L2)        0,00 |
| P3 = 1000,00 | Em aberto | - | 1000,00 |
| P4 = 1000,00 | Em aberto | - | 1000,00 |
| P5 = 1000,00 | Em aberto | - | 1000,00 |
| P6 = 1000,00 | Em aberto | - | 1000,00 |

                                                                            \* Lctos de Devolução criados anteriormente

**Cenário 4:**

***A partir da versão 12.1.33,**foi adicionada uma validação para que, nos casos onde existam lançamentos baixados, o sistema calcule o valor à ser devolvido para o aluno utilizando o valor baixado.*

Contrato do aluno possui 6 parcelas sendo:  
− Parcelas 1 a 5 no valor de 1000,00 cada. Lançamentos financeiros já foram gerados e já 'Baixados'.  
− Parcela 6 no valor de 1000,00. Lançamentos financeiros já foram gerados e ainda estão 'Em aberto'.   
− Foi incluída uma bolsa retroativa de 100% para as 6 parcelas deste contrato.  
**Resultado:**− Serão incluídos 6 lançamentos de devolução, sendo que um deles será no valor de 1000,00 que está em aberto. Os lançamentos já baixados terão o crédito calculado conforme o valor baixado.  
Cálculos:  
• Valor total gerado de créditos de Bolsa Retroativa = 6000,00 (6 x 1000,00 referente às bolsas incluídas)  
• Parcela 1 - Valor baixado é de 1000,00 por este motivo o crédito de devolução deve ser de 1000,000.  
• Parcelas 2, 4 e 5 - Por algum motivo foram pagas com desconto de 3%, o valor do crédito da bolsa é de 1000,00 por lançamento, porém como o valor baixado é menor que o valor do crédito, o valor à ser usado como crédito de devolução destes lançamentos é de 970,00.  
• Parcela 6 - Como a parcela está em aberto, o valor do crédito é calculado sobre o valor original do lançamento ou seja 1000,00.  
• Parcela 3 - O valor baixado é de 1050,00 ou seja é maior que o valor original do lançamento, neste caso existe um fator limitador que impede que o valor do crédito de devolução seja maior que o valor original do lançamento, por este motivo o crédito de devolução é de 1000,00.**\***  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa Retroativa | Vínculo criado no Lcto da parcela | Valor líquido Lcto da parcela | Lcto de Devolução (L) |
| P1 = 1000,00 | Baixado | 100% = 1000,00 (L1) | - | 1000,00 | L1 = 1000,00 |
| P2 = 1000,00 | Baixado | 100% =   1000,00 (L2) |  | 970,00 | L2 =  970,00 |
| P3 = 1000,00 | Baixado | 100% =   1000,00 (L3) |  | 1050,00 | L3 =  1000,00**\*** |
| P4 = 1000,00 | Baixado | 100% =   1000,00 (L4) |  | 970,00 | L4 =  970,00 |
| P5 = 1000,00 | Baixado | 100% =   1000,00 (L5) |  | 970,00 | L5 =  970,00 |
| P6 = 1000,00 | Em aberto | 10% =   1000,00 (L6) |  | 1000,00 | L6 =  1000,00 |

**\***Foi adicionado um novo parâmetro no sistema que permite que o crédito de devolução seja o valor baixado mesmo que tal valor ultrapasse o valor original do lançamento. Tal parâmetro pode ser alterado em (*Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Bolsa Retroativa 1/3 | **Considerar valores de acréscimos no cálculo de crédito retroativo (apenas parcelas já baixadas)***)
