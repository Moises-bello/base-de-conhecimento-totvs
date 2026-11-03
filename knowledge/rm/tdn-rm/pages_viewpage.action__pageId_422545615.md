---
content_hash: dbcb06c5dd6b6aa4733f304b8b24de4de74b4b70df6953314c51d935da3da12a
fetched_at: '2026-06-29T00:09:19.582190+00:00'
page_id: '422545615'
product: rm
source: tdn-rm
title: Implementações para a NF-e 4.00
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545615
version: 8
---

Para adequar o processo da NF-e no RM ao layout 4.00 da NF-e foi necessária a criação de novos campos na base dados. Eles estão descritos abaixo.

**Operação Presencial** - Indicador de presença do comprador no estabelecimento no momento da operação.  
Excluída a Tag indPag (Indicador da Forma de Pagamento do Grupo B.  
Na Tag Indicador de presença "indPres" foi incluída a opção ("Operação Presencial, fora do estabelecimento, utilizado no caso de venda ambulante".  
**Localização do campo**: Aba integração Fiscal no Movimento.  
**Tag no XML**: indPres  
**Campo na base de dados**: TMOVFISCAL.OPERACAOPRESENCIAL e DLAF.OPERACAOPRESENCIAL  
**Valores permitidos**:  0 - Não se aplica,  
                                  1 - Operação presencial;  
                                  2 - Operação não presencial pela internet;  
                                  3 - Operação não presencial tele atendimento;  
                                  4 - NFC em operação com entrega em domicílio;  
                                  5 - Operação presencial, fora do estabelecimento;  
                                  9 - Operação não presencial outros.

**Documento Fiscal Referenciado** - Inclusão da opção 2 = Nota Fiscal modelo 02, que possibilitará referenciar este modelo de documento no Grupo Documentos Fiscais Referenciados.  
**Tag no XML**: indPres  
**Campo na base de dados**: FTDO.CODMODDOC

**Rastreabilidade de produto** - Criação do grupo para permitir a rastreabilidade de qualquer produto sujeito a regulações sanitárias, casos de recolhimento/recall, além de defensivos agrícolas, produtos veterinários, odontológicos, medicamentos, bebidas, águas envasadas, embalagens.   
**Tag no XML**: rastro, nLote, qLote, dFab, dVal e cAgre.  
**Campo na base de dados**: TLOTEPRD.NUMLOTE, TITMLOTEPRD.QUANTIDADE2, TLOTEPRD.DATAFABRICAÇÃO, TLOTEPRD.DATAVALIDADE e TLOTEPRD.CODAGREGACAO.

**Imposto sobre Produtos Industrializados** - Excluído o campo Classe de enquadramento do IPI;  
O Campo Código de Enquadramento atualmente é preenchido fixo com "999" deve passar a ser gerado com o código informado no Cadastro do Produto.  
**Localização do campo**: Aba Dados Fiscais – Tributação – Campo "Código Enquadramento do IPI".   
**Tag no XML**: cEnq  
**Campo na base de dados**: TPRDFISCAL.CODENQIPI.

**Produtos e Serviços da NF-e** - Criado novos campos para informar se o produto foi fabricado em escala relevante ou não, conforme Cláusula 23 do Convênio ICMS 52/2017 e, em caso de produção em escala NÃO relevante, o campo CNPJ do Fabricante deve ser informado.   
**Localização do campo**: Cadastro do Produto.  
**Tag no XML**: indEscala, CNPJFab e cBenef.  
**Valores permitidos**: S -  Produzido em Escala Relevante;  
                                 N – Produzido em Escala NÃO Relevante.

**Detalhamento Específico de Medicamento e de matérias-primas farmacêuticas** - Foi criada a tag cProdANVISA - Código de Produto da ANVISA.   
O Grupo de Medicamento apenas será gerado para Produtos Controlados por Lote e que estejam com Registro da Anvisa Preenchido no Cadastro Produto, (Anexo do Saúde ou Dados do Produto Aba Integração)  
Obs: Não será mais verificado se o Produto utiliza NCM's pertencentes aos grupos de NCM 3003 e 3004.  
O grupo de rastro é Obrigatório para Produto tipo Medicamento. Para gerar este grupo deve estar marcado o parâmetro "produto sujeito a regulações Sanitárias" localizado nos Dados Fiscais do Produto.   
**Tag no XML**: med, cProdANVISA e vPMC.  
**Campo na base de dados**: SZPRD.REGISTROANVISA.  
**Localização do campo**: Cadastro do Produto - Anexo Subpasta Informações RM Saúde ou Cadastro do Produto - Pasta Integração - Campo "Registro na Anvisa".

**Grupo de ICMS Normal e ST** - Incluídas tags para identificar o valor devido em decorrência do percentual de ICMS relativo ao Fundo de Combate à Pobreza.  
**Grupo Tributação do ICMS** = 00  
**Tag no XML**: pFCP e vFCP.  
**Campo na base de dados**: TPRDCODFISCAL.PERFECP e TTRBMOV.BASEDECALCULO.

**Grupo de ICMS Normal e ST** - Incluídas tags para identificar o valor devido em decorrência do percentual de ICMS relativo ao Fundo de Combate à Pobreza.  
**Grupo Tributação do ICMS** = 10, 20, 51, 70 e 90  
**Tag no XML**: vBCFCP, pFCP e vFCP.  
**Campo na base de dados**: TTRBMOV.BASEDECALCULO e TPRDCODFISCAL.PERFECP.  
   
**Grupo de ICMS Normal e ST** - Incluídas tags para identificar o valor devido em decorrência do percentual de ICMS relativo ao Fundo de Combate à Pobreza.  
**Grupo Tributação do ICMS** = 10, 30, 70 e 90  
**Tag no XML**: vBCFCPST, pFCPST e vFCPST.  
**Campo na base de dados**: TTRBMOV.BASEDECALCULO (ICMSST) e TPRDCODFISCAL.PERFECP.  
   
**Grupo de ICMS Normal e ST** - Incluídas tags para identificar o valor devido em decorrência do percentual de ICMS relativo ao Fundo de Combate à Pobreza.  
**Grupo Tributação do ICMS** = 60  
**Tag no XML**: vBCFCPST, pFCPSTRet, vFCPSTRet e pST.  
**Campo na base de dados**: TTRBMOV.BASEDECALCULO (ICMSST), TPRDCODFISCAL.PERFECP e (TTRBMOV.ALIQUOTA (ICMSST) (TTRBMOV.ALIQUOTA (ICMSST).

**Grupo de Repasse do ICMS ST** - Incluída nova opção para "Tributação de ICMS" 60 = cobrado anteriormente por substituição tributária.  
Tag no XML: CST.  
Valores permitidos: 41=Não Tributado (v2.0);  
                             60= cobrado anteriormente por substituição tributária.

**Grupo CRT** = 1 e CSOSN 201, 202, 203 e 900  
**Tag no XML**: vBCFCPST, pFCPST, vFCPST.  
**Campo na base de dados**: TTRBMOV.BASEDECALCULO (ICMSST) e TPRDCODFISCAL.PERFECP.

**Grupo de ICMS para a UF de Destino** – Incluídas a tags para identificar o valor devido em decorrência do percentual de ICMS relativo ao Fundo de Combate à Pobreza na UF de Destino.  
**Tag no XML**: vBCFCPUFDest.  
   
**Grupo Totalizador da NF-e** – Incluídas a tags para identificar o valor devido correspondente ao total da soma dos campos.  
**Tag no XML**: vFCP, vFCPST, vFCPSTRet e vIPIDevol.   
***Observação*.:** O Valor Total do IPI devolvido deve ser informado quando preenchido o Grupo Tributos Devolvidos na emissão de nota finNFe=4 (devolução) nas operações com não contribuintes do IPI.

**Grupo de Informações do Transporte da NF-e**– Alteração da tag modFrete.  
Tag no XML: modFrete.  
Valores permitidos:  0 - Contratação do Frete por conta do Remetente (CIF);  
                              1 - Contratação do Frete por conta do Destinatário (FOB);  
                              2 - Contratação do Frete por conta de Terceiros;  
                              3 - Transporte Próprio por conta do Remetente;  
                              4 -  Transporte Próprio por conta do Destinatário;  
                              9 - Sem Ocorrência de Transporte.

**Grupo de Informações Suplementares da Nota Fiscal** - Criação de novo campo com o objetivo de padronizar a URL de consulta por chave de acesso que aparece no DANFE NFC-e.  
**Tag no XML**: urlChave.

**Grupo de Informação de Pagamento** - Incluído no campo YA02 "Forma de Pagamento" a opção 14=Duplicata Mercantil,  
15=Boleto Bancário e 90=Sem Pagamento.  
**Tag no XML**: pag, tPag, vPag e vTroco.  
**Tag no XML**: tPag  
**Valores permitidos**:  01=Dinheiro  
                                  02=Cheque  
                                  03=Cartão de Crédito  
                                  04=Cartão de Débito  
                                  05=Crédito Loja  
                                  10=Vale Alimentação  
                                  11=Vale Refeição  
                                  12=Vale Presente  
                                  13=Vale Combustível  
                                  14=Duplicata Mercantil  
                                  15=Boleto Bancário  
                                  17=Pagamento Instantâneo (PIX)  
                                  18=Transferência bancária, Carteira Digital  
                                  19=Programa de fidelidade, Cashback, Crédito Virtual  
                                  20=Pagamento Instantâneo (PIX) – Estático  
                                  21=Crédito em Loja  
                                  22=Pagamento Eletrônico não Informado  
                                  90=Sem Pagamento  
                                  99=Outros  
**Tag no XML**: tBand;  
**Valores permitidos**:  01=Visa  
                                  02=Mastercard  
                                  03=American Express  
                                  04=Sorocred  
                                  05=Diners Club  
                                  06=Elo  
                                  07=Hipercard  
                                  08=Aura  
                                  09=Cabral  
                                  99=Outros

**Grupo de Produtos e Serviços da NF-e** – Alteração no preenchimento dos campos cEANTrib da NF-e e NFC-e quando o produto comercializado possuir código de barras com GTIN.  
**Tag no XML**: cEAN;  
**Valores permitidos**: Preencher com o código GTIN-8, GTIN-12, GTIN-13 ou GTIN-14 (antigos códigos EAN, UPC e DUN-14).  
**Tag no XML**: cEANTrib;  
**Valores permitidos**: Preencher com o código GTIN-8, GTIN-12, GTIN-13 ou GTIN-14 (antigos códigos EAN, UPC e DUN-14) da unidade tributável do produto.  
***Observação*.:** O GTIN Tributário deve corresponder ao GTIN da menor unidade comercializada no varejo identificável por código GTIN.  
**Para produtos que não possuem código de barras com GTIN, deve ser informado o literal "SEM GTIN"** De acordo com a NT 2017.001 v\_1.30 a obrigatoriedade de gerar as TAGs **cEan** e **cEanTrib** com a literal "**SEM** **GTIN**" no ambiente de **produção** é apenas após **01/12/2018**. Contudo, alguns estados já estão obrigando a geração desta informação no ambiente de produção antes do prazo e por este motivo estamos flexibilizando a geração destas TAGs conforme abaixo.  
Para os estados que já estão obrigando a geração da literal "SEM GTIN" deverá ser preenchido no cadastro da Filial o "**Campo** **Livre** **2**" com a literal "**SEM** **GTIN**".  
Cadastro da Filial >> Anexos >> Dados Fiscais >> Dados Adicionais >> Campo Livre 2  
Com esta configuração, ao enviar uma NF-e com itens que não possuem código GTIN cadastrado, o XML será gerado com a literal "SEM GTIN" nas TAGs cEan e cEanTrib.  
Após 01/12/2018 o processo enviará **automaticamente a literal "SEM GTIN"** independente do cadastro da Filial.  
Ressaltamos que **não** **é necessário cadastrar um código de barras "SEM GTIN" no produto**.

**Grupo Detalhamento Específico de Medicamento e de Matérias-primas Farmacêuticas -** Alteração no preenchimento da tag cProdANVISA quando possuir integração com o TOTVS Saúde. Caso possua integração com o TOTVS Saúde, o sistema irá verificar o preenchimento do código da Anvisa no cadastro do produto em Anexos | Informações RM Saúde. Se o campo não possuir valor, automaticamente será verificado o campo Registro Anvisa existente na aba Integração do cadastro do produto.  
**Tag no XML**: cProdANVISA

**Grupo LA Item de Combustível** - De acordo com a exigência da NT2016.002, foram implementadas tags relacionadas a combustível.  
**Tag no XML**: pGLP, pGNn, pGNi e vPart  
**Consistência**: As novas tags serão geradas no xml somente se código ANP do produto for igual a "210203001".

**Parâmetro para enviar valores opcionais da parcela no envio da NF-e 4.0**

Criação de parâmetro no tipo de movimento para identificar quais valores opcionais utilizados no tipo de movimento deverão ser considerados para cálculo do valor das parcelas da NF-e, essa implementação irá permitir ao usuário determinar entre quais valores opcionais ele quer enviar para os valores opcionais nos lançamentos financeiros e quais devem ser adicionados às parcelas no envio da Nota Fiscal Eletrônica (nas parcelas incluídas na tag "pag" do XML da NF-e).

**Parametrização Necessária**

* Acessar o **TOTVS Gestão de Estoque, Compras e Faturamento - Ambiente - Gestão de Estoque Compras e Faturamento** e acessar os Parâmetros do Tipo de Movimento utilizando para envio da NF-e.
* Acessar a etapa **Fin-Faturamento 4/6** e marcar o campo "**Usa Valor Opcional**" e "**Enviar Op NF-**e" de acordo com a parcela que dessa enviar os valores e preencher o campo de "**Fórmula Rateio Valor Opcional**" com a fórmula utilizada.

Para definir como será feito a distribuição para cada Valor Opcional, acessar a etapa **Fin - Faturamento 5/**6 e Definir se a Distribuição será feita por "**Rateio**", "**Primeira Parcela**" ou "**Última Parcela**" e qual parcela será feita a Distribuição.

* Outra parametrização Importante é nos Parâmetros do **TOTVS Gestão Financeira**:
* Acessar o **TOTVS Gestão Financeira →. Ambiente → TOTVS Gestão Financeira,** acessar a etapa 02.01.01.01 - Lançamento - Valores Opcionais;
* No campo de "**Op. Nome**" o usuário deve definir se o valor opcional correspondente irá "**Acrescentar**", "**Descontar**" ou "**Nada**" no valor opcional.

***Observação*:** Se o usuário selecionar "Acrescentar" o valor opcional será adicionado às parcelas selecionadas, caso ele selecione "Descontar" o valor opcional será subtraído às parcelas selecionadas e seja selecionado "Nada", nenhum valor daquele valor opcional será adicionado a nenhuma parcela. Cada campo apresentado nesta tela equivale a uma parcela do lançamento financeiro.

***IMPORTANTE!* Para o correto funcionamento da implementação da NF-e 4.0, será necessário aplicar o script via "Atualizador" para criação dos novos campos, segue documentação a ser seguida:**[Atualizador RM - Scripts Opcionais / Intermediários](http://tdn.totvs.com/pages/viewpage.action?pageId=322143046)

Legislação

* [Manuais da Início do conteúdo excluídoNF-e Fim do conteúdo excluído Início do conteúdo adicionadoNF-e/NFC-e Fim do conteúdo adicionado](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=33ol5hhSYZk=)
* [Notas Técnicas da Início do conteúdo excluídoNF-e Fim do conteúdo excluído Início do conteúdo adicionadoNF-e/NFC-e Fim do conteúdo adicionado](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=)
