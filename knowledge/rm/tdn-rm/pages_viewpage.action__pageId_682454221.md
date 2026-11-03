---
content_hash: 3314e660465cd9f9634dbc098b31ff7147a3a8879b1ca55cdcfb54f61f48a66f
fetched_at: '2026-06-29T00:11:18.096408+00:00'
page_id: '682454221'
product: rm
source: tdn-rm
title: DIME-SC (Declaração do ICMS e do Movimento Econômico - Santa Catarina)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=682454221
version: 123
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Com o objetivo de proporcionar uma melhor experiência e alinhamento às atualizações mais recentes dos nossos produtos, informamos que a funcionalidade **DIME-SC (Declaração do ICMS e do Movimento Econômico - Santa Catarina),** já disponível no Módulo Gestão Fiscal, não será mais suportada no produto **RM Liber.exe** a partir da **versão 12.1.2502**

Reforçamos que essa alteração faz parte do nosso processo de evolução tecnológica, com a descontinuidade gradual de funcionalidades no **RM** **Liber.exe**. Para garantir a continuidade do uso e acesso à funcionalidade DIME-SC, recomendamos que a geração seja feita diretamente no **Módulo Gestão Fiscal**.

# Conteúdo

Conteúdonone

# 01. O que é a DIME-SC?

A **DIME-SC** (Declaração do ICMS e do Movimento Econômico) é uma obrigação acessória exigida dos contribuintes inscritos no Cadastro de Contribuintes do ICMS (CCICMS) do estado de Santa Catarina. Através dessa declaração, os contribuintes informam mensalmente à Secretaria da Fazenda de Santa Catarina (SEF/SC) um resumo das suas operações e prestações que impactam a apuração do ICMS, bem como dados sobre o movimento econômico da empresa.

A DIME tem como principal objetivo consolidar as informações fiscais do contribuinte, facilitando a fiscalização e o controle tributário por parte do fisco estadual

# 02. Detalhamento dos Registros Gerados

Nesta seção, apresentamos os registros gerados pela DIME-SC. Cada registro é organizado conforme os quadros exigidos pela Secretaria da Fazenda de Santa Catarina. Abaixo, você encontrará a descrição de cada registro, suas fontes de dados e as condições para seu correta geração do arquivo.

01lefttrue01\_1Visão Geral dos Registros

**Tipos de Registros:**

Registro Tipo **20** - Dados do Contabilista / Responsável  
Registro Tipo **21** - Dados iniciais   
Registro Tipo **22** - Valores Fiscais Entradas  
Registro Tipo **23** - Valores Fiscais Saídas  
Registro Tipo **24** - Resumo dos Valores Fiscais  
Registro Tipo **25** - Resumo da Apuração dos Débitos  
Registro Tipo **26** - Resumo da Apuração dos Créditos  
Registro Tipo **30** - Cálculo do Imposto a Pagar ou Saldo Credor  
Registro Tipo **32** - Informações sobre Substituição Tributária  
Registro Tipo **33** - Discriminação dos Pagamentos do Imposto e dos Débitos Específicos  
Registro Tipo **34** - Informações sobre Diferença de Alíquota de Operação Interestadual à Consumidor  
Registro Tipo **35** - Demonstrativo da apuração do imposto devido pela apropriação de crédito presumido em ST aos créditos pelas entradas (DAICP)  
Registro Tipo **36** - Demonstrativo dos valores devidos aos fundos como contrapartida pela utilização de benefício fiscal  
Registro Tipo **37** - Demonstrativo da Apuração de Valores Devidos ou Saldo Credor de Fundos   
Registro Tipo **46** - Créditos por Regimes Especiais   
Registro Tipo **47** - Entradas de Extratores, Produtores Agropecuários e Pescadores  
Registro Tipo **48** - Informações para Rateio do Valor Adicionado   
Registro Tipo **49** - Entradas por Unidade da Federação  
Registro Tipo **50** - Saídas por Unidade da Federação  
Registro Tipo **51** - Exclusões de Valores para Apuração do Valor Adicionado  
Registro Tipo **80** - Resumo do Livro Registro de Inventário e Receita Bruta  
Registro Tipo **81** - Ativo  
Registro Tipo **82** - Passivo  
Registro Tipo **83** - Demonstração de Resultados  
Registro Tipo **84** - Detalhamento das Despesas  
Registro Tipo **85** - Discriminação das Contribuições (FIA) e (FEI)  
Registro Tipo **90** - Resumo do Livro Registro de Inventário e Receita Bruta (Encerramento de Atividades)  
Registro Tipo **91** - Ativo  
Registro Tipo **92** - Passivo  
Registro Tipo **93** - Demonstração de Resultados (Encerramento de Atividades)  
Registro Tipo **94**- Detalhamento das Despesas (Encerramento de Atividades)  
Registro Tipo **98** - Encerramento da Declaração  
Registro Tipo **99** - Encerramento do Arquivo

true1R2001\_1true01\_2Campos

Os dados deste Registro são montados com base nos campos CPF e Nome do Contabilista, informados no cadastro de Filiais, Pasta Dados Fiscais/ Contador.

Dados do Contabilista / Responsável

| ORDEM | CAMPOS | CONTEÚDO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Preenche com "20" |  |
| 02 | Quadro | Preenche com brancos |  |
| 03 | CPF | Número do CPF do Contador | Gerado com o CPF do Contador informado no Cadastro da Filial DFilial.CPFCONTADOR |
| 04 | Nome do Contabilista | Nome do Contabilista (Informativo) | Gerado como Nome do Contador informado no cadastro da Filial - Anexo Dados Fiscais - Subpasta Contador |
| 05 | Data e Hora | Preenche no formato  AAAAMMDDHHMISS |  |

true1R2101\_1true01\_2Campos

Os campos são montados com base nos dados informados na tela da Rotina.

Dados Iniciais

| ORDEM | CAMPOS | Conteúdo | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Preenche com "21" |  |
| 02 | Quadro | Preenche com 00 |  |
| 03 | Número de Inscrição | Número de Inscrição do Contribuinte | Gerado com o Campo Inscrição Estadual do Cadastro da Filial GFILIAL.INSCRICAOESTADUAL |
| 04 | Nome do Contribuinte | Nome do Contribuinte  (informativo) | Gerado com o Campo Nome do Cadastro da Filial GFILIAL.NOME |
| 05 | Período de referência da declaração | Período de referência da declaração no formato MMAAAA ( mês - ano) | Gerado com o Campo **Referencia** informado na tela de geração da Rotina |
| 06 | Tipo de declaração | 1 - Normal, 2 - Encerramento de Atividades 4 - Enquadramento no Simples Nacional ***(Redação dada pelo Art. 12 da Portaria SEF nº 004/16 - Efeitos fatos geradores a partir da referência janeiro/2016)*** | Gerado com o Campo Regime de Apuração informado na Tela de geração da Rotina |
| 07 | Regime de Apuração | 2 - Normal,  9 - Produtor Primário (se o declarante tiver inscrição de produtor primário). ***(Redação dada pelo Art. 12 da Portaria SEF nº 004/16 - Efeitos fatos geradores a partir da referência janeiro/2016)*** | Gerado com o Campo Regime de Apuração informado na Tela de geração da Rotina |
| 08 | Porte da empresa | 1 – Não se aplica | Atualmente é gerado com o campo **Porte** informado na tela da Rotina. Como só tem uma Opção é  Não se aplica pode ser gerado como fixo |
| 09 | Apuração consolidada? | 1 - Não é apuração consolidada, 2 - É estabelecimento consolidador, 3 - É estabelecimento consolidado. | Gerado com o campo **Apuração Consolidada** informado na tela de geração da Rotina |
| 10 | Apuração centralizada? | 1 - Não se aplica | Gerar fixo com a Opção “1 Não se aplica” |
| 11 | Transferência de créditos no período? | 1 - Não apurou ou reservou nem recebeu créditos, 2 - Apurou ou reservou créditos, 3 - Recebeu créditos, 4 - Apurou ou reservou e recebeu créditos, 5 - Apuração e reserva crédito sistema cooperativo agropecuário | Gerado com o campo **Transferência de Créditos no Período** informado na Tela de Geração da Rotina |
| 12 | Tem créditos presumidos? | 1 - Não se aplica | Gerar fixo com a Opção “1 Não se aplica” |
| 13 | Tem créditos por incentivos fiscais? | 1 - Não se aplica | Gerar fixo com a Opção “1 Não se aplica” |
| 14 | Movimento | 1 - Sem movimento e sem saldos, 2 - Sem movimento e com saldos, 3 - Com movimento. | Gerado com o Campo **Movimento** informado na tela de geração da Rotina |
| 15 | Substituto Tributário | 1 - Sim, 2 - Não. 3 - Substituído solidário | Gerado com o Campo **Substituto Tributário** Informado na tela de geração da Rotina |
| 16 | Tem escrita contábil | 1 - Sim é o estabelecimento principal, 2 - Não, 3 - Sim, dados informados no estabelecimento principal | Gerado com o Campo **Tem escrita contábil** informado na tela de geração da Rotina |
| 17 | Quantidade de trabalhadores na atividade |  | Gerado conforme o Campo **Número Empregados** informado na tela de geração da Rotina |

true1R2201\_1true01\_2CamposSerão selecionados os **Lançamentos Fiscais de Entrada** cuja Natureza Fiscal associada é Fiscal.

A data do Lançamento Fiscal deve estar dentro do Mês/ Ano de Referência selecionado na tela de geração da rotina.

São gerados registros totalizados por CFOP.

Valores Fiscais Entrada

| ORDEM | CAMPOS | CONTEÚDO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Preenche com "22" |  |
| 02 | Quadro | Preenche com "01" |  |
| 03 | CFOP | Código Fiscal de Operações e Prestações das Entradas | Gerado com o CFOP associado ao Lançamento Fiscal |
| 04 | Valor Contábil | Valor correspondente ao Valor Contábil | Somatório dos itens dos lançamentos.  VALORMERC =   Se DITEM.VALORMERC > 0   então     DITEM.VALORMERC –(DITEM.DESCONTOITEM +     DITEM.VALORDESPESA +   DITEM.SEGURO +  DITEM.IPI)  senão    DITEM.PRECOPRD \* DITEM.QTDEPRD –(DITEM.DESCONTOITEM +              DITEM.VALORDESPESA +  DITEM.SEGURO +  DITEM.IPI ) |
| 05 | Base de Cálculo | Valor correspondente à Base de Cálculo | DLAF.BASEREDICMS |
| 06 | Imposto Creditado | Valor correspondente ao Imposto Creditado | DLAF.VALORICMS |
| 07 | Isentas ou Não Tributadas | Valor Correspondente às operações Isentas ou não Tributadas | DLAF.ISENTOICMS |
| 08 | Outras | Valor correspondente a outras operações sem crédito de imposto | DLAF.OUTROSICMS |
| 09 | Base de Cálculo Imposto Retido | Valor correspondente à Base de Cálculo do Imposto Retido | DLAF.BASEUBST |
| 10 | Imposto Retido | Valor correspondente ao Imposto Retido | DLAF.VALORSUBST |
| 11 | Diferença de Alíquota | Valor correspondente ao Imposto Diferencial de Alíquota | DLAF.VALORDIFALIQ |

true1R2301\_1true01\_2CamposSerão selecionados os **Lançamentos Fiscais de Saída** cuja Natureza Fiscal associada é Fiscal.

A data do Lançamento Fiscal deve estar dentro do Mês/ Ano de Referência selecionado na tela de geração da rotina.

São gerados registros totalizados por CFOP.

Valores Fiscais Saídas

| ORDEM | CAMPOS | CONTEÚDO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Preenche com "23" |  |
| 02 | Quadro | Preenche com "02" |  |
| 03 | CFOP | Código Fiscal de Operações de Prestações das Saídas | Gerado com o CFOP associado ao Lançamento Fiscal |
| 04 | Valor Contábil | Valor correspondente ao Valor Contábil | SOMATÓRIO DOS ITENS DOS LANÇAMENTOS.  VALORMERC =   Se DITEM.VALORMERC > 0   então   DITEM.VALORMERC –(DITEM.DESCONTOITEM +   DITEM.VALORDESPESA + DITEM.SEGURO + DITEM.IPI)  senão  DITEM.PRECOPRD \* DITEM.QTDEPRD –(DITEM.DESCONTOITEM +     DITEM.VALORDESPESA +  DITEM.SEGURO +  DITEM.IPI +) |
| 05 | Base de Cálculo | Valor correspondente à Base de Cálculo | DLAF.BASEREDICMS |
| 06 | Imposto Creditado | Valor correspondente ao Imposto Creditado | DLAF.VALORICMS |
| 07 | Isentas ou Não Tributadas | Valor correspondente às operações Isentas ou não Tributadas | DALF.ISENTOICMS |
| 08 | Outras | Valor correspondente a outras operações sem crédito de imposto | DALF.OUTROSICMS |
| 09 | Base de Cálculo Imposto Retido | Valor correspondente à Base de Cálculo do Imposto Retido | DLAF.BASESUBST |
| 10 | Imposto Retido | Valor correspondente ao Imposto Retido | DALF.VALORSUBST |
| 11 | Diferença de Alíquota | Valores zerados |  |

true1R2401\_1true01\_2Campos

Os valores deste registro são gerados com a Totalização dos Valores Fiscais de Entrada e Saída, Valores impressos nos registros Tipo 22 e Tipo 23 respectivamente.

Resumo dos Valores Fiscais

|  | Item | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- | --- |
| 1 | 010 | Valor contábil |  | Soma do Valor Contábil do Lançamento Fiscal  DLAF.VALORCONT |
| 2 | 020 | Base de cálculo |  | Gerado com o Valor da Base de Cálculo Tributada do Lançamento Fiscal   DALF.BASEREDICMS |
| 3 | 030 | Imposto creditado |  | Gerado com o Valor do ICMS   DLAF.VALORICMS |
| 4 | 040 | Operações isentas ou não tributadas |  | Gerado como Valor de Isento do ICMS  DALF.ISENTOICMS |
| 5 | 050 | Outras operações sem crédito de imposto |  | Gerado com o valor de Outros do ICMS   DALF.OUTROSICMS |
| 6 | 053 | Base de Cálculo Imposto Retido | Calculado apenas se for SUBSTITUTO TRIBUTARIO = Sim ou Substituto solidário | DLAF.BASESUBST |
| 7 | 054 | Imposto Retido | Calculado apenas se for SUBSTITUTO TRIBUTARIO = Sim ou Substituto solidário | DLAF.VALORSUBST |
| 8 | 057 | Imposto Diferencial Alíquota |  | DLAF.VALORDIFALIQ |
|  | **Lançamentos de Saídas** | | | |
| 9 | 060 | Valor Contábil |  | Gerado com o Valor Contábil do Lançamento Fiscal  DLAF.VALORCONT |
| 10 | 070 | Base de Cálculo |  | Gerado com o Valor da Base de Cálculo Tributada do Lançamento Fiscal   DALF.BASEREDICMS |
| 11 | 080 | Imposto debitado |  | Gerado com o Valor do ICMS   DLAF.VALORICMS |
| 12 | 090 | Operações isentas ou não tributadas |  | Gerado como Valor de Isento do ICMS  DALF.ISENTOICMS |
| 13 | 100 | Outras operações sem débito de imposto |  | Gerado com o valor de Outros do ICMS   DALF.OUTROSICMS |
| 14 | 103 | Base de Cálculo Imposto Retido | Calculado apenas se for SUBSTITUTO TRIBUTARIO = Sim ou Substituto solidário | DLAF.BASESUBST |
| 15 | 104 | Imposto Retido | Calculado apenas se for SUBSTITUTO TRIBUTARIO = Sim ou Substituto solidário | DALF.VALORSUBST |

true1R2501\_1true01\_2CamposResumo da Apuração dos Débitos

|  | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 010 | Débito pelas saídas | Soma do Valor do ICMS dos Lançamentos Fiscais de Saída | DLAF.VALORICMS |
| 020 | Débito por diferencial de alíquota de ativo permanente | Soma do Valor do Diferencial de Alíquota dos Lançamentos Fiscais de Entrada, cuja Natureza de Operação é referente a Operações de Ativo Imobilizado, estiver habilitado. | DLAF.VALORDIFALIQ |
| 030 | Débito por diferencial de alíquota de material de uso ou consumo | Soma do Valor do Diferencial de Alíquota dos Lançamentos Fiscais de Entrada, cuja Natureza de Operação é referente a operações de Uso ou Consumo. CFOP do Código **1.556, 2.556, 3.556** | DLAF.VALORDIFALIQ |
| 040 | Débito de máquinas / equipamentos importados para ativo permanente | Soma Valor do ICMS dos Lançamentos Fiscais de Entrada, cuja Natureza de Operação é referente a operações de Ativo Imobilizado. | DLAF.VALORALIQ |
| 045 | Débito da Diferença de Alíquota de Operação ou Prestação a Consumidor Final de Outro Estado ***(Redação dada pelo Art. 2º da Portaria SEF nº 004/16 - Efeitos fatos geradores a partir da referência janeiro/2016)*** |  | Transportado do Registro 34 |
| **Estornos** | | | |
| 050 | Estorno de crédito | Soma Valor dos Lançamentos de Outros Débitos/ Créditos cujo Tipo é “Estorno de Crédito”. | DLDC.VALORLDC |
| 060 | Outros estornos de crédito |  | Item não gerado |
| 065 | Estorno de Crédito da Entrada em Decorrência da Utilização de Crédito Presumido ***(Redação dada pelo Art. 1º da Portaria SEF nº 070/17 - Efeitos fatos geradores a partir da referência abril/2017)*** |  |  |
| **Outros débitos** | | | |
| 070 | Outros débitos | Valor dos Lançamentos de Outros Débitos/ Créditos cujo Tipo é “Débito” e Sub Tipo é “Não de Aplica”, somado ao Valor do Diferencial de Alíquota dos Lançamentos Fiscais de Entrada, que não se enquadrarem nos casos dos itens 020 e 030. | DLAF.VALORDIFALIQ e   DLDC.VALORLDC |
| 990 | Subtotal de Débitos => (transportar para o item 010 do quadro 09 Cálculo do Imposto a Pagar ou Saldo Credor) |  | Soma dos itens anteriores |

true1R2601\_1true01\_2CamposResumo da Apuração dos Créditos

| ITEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 010 | Saldo credor do mês anterior | Saldo credor de ICMS resultante da apuração do mês anterior ao mês/ Ano de Referência. | Período Apuração | Saldo Anterior Tributo |
| Créditos Gerais | | | |
| 020 | Crédito pelas entradas | Soma do Valor do ICMS dos Lançamentos Fiscais de Entrada, com exceção dos associados a Naturezas de Operação de Ativo Imobilizado. | DLAF.VALORICMS |
| 030 | Crédito de ativo permanente | Soma do Valor do ICMS dos Lançamentos Fiscais de Entrada, cuja Natureza de Operação é referente a operações de Ativo Permanente, crédito de 1/48 do CIAP. | DLAF.VALORICMS + DLDC.VALORLDC |
| 040 | Crédito por diferencial de alíquota material de uso  / consumo | Não gerado |  |
| 045 | Crédito da Diferença de Alíquota de Operação ou Prestação a Consumidor Final de Outro Estado **(Redação dada pelo Art. 2º da Portaria SEF nº 087/16 - Efeitos fatos geradores a partir da referência janeiro/2016)** | Não gerado |  |
| 050 | Crédito de ICMS retido por substituição tributária | Valor do ICMS retido por substituição tributária quando a mercadoria for utilizada como insumo no processo produtivo, devendo esta hipótese de crédito ser prevista na legislação aplicável ou nas demais hipóteses previstas no RICMS-SC/01, Anexo 3, art. 22. Para a atender este item a SEFAZ, informou que deve ser a partir de lançamentos de Outros Débitos\Créditos com o Código de Ajuste "SC020010 Crédito do ICMS de mercadoria sujeita à substituição tributária".  <https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=422545651> | DLDC.VALORLDC |
| Totalização | | | |
| 990 | Subtotal de créditos |  | Calculado |

true1R30

Exemplo do Registro gerado no arquivo.

01\_1true01\_2CamposCálculo do Imposto a Pagar ou Saldo Credor

| ITEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| Totalização de Débitos | | | |
| 010 | Subtotal de Débitos | Gerado com o Valor do item 990 do registro tipo 25 ou registro 27 | Valor do item 990 do registro tipo 25 |
| 011 | Complemento de débito por mudança de regime de apuração |  |  |
| 020 | Saldos devedores recebidos de estabelecimentos consolidados |  | Valor dos Lançamentos de Outros Débitos/ Créditos cujo tipo é "Outros Débitos" e SubTipo é "Recebimento de Débito". |
| 030 | Débito por reserva de crédito acumulado | Não gerado |  |
| 036 | Segregação do Crédito Presumido Utilizado em Substituição aos Créditos pelas Entradas ***(Redação dada pelo Art. 3º da Portaria SEF nº 070/17 - Efeitos fatos geradores a partir da referência abril/2017)*** |  | Gerado com base nos lançamentos de Outros Débitos/Créditos do tipo DÉBITO com subtipo: SEGREGAÇÃO DO CRÉDITO PRESUMIDO. |
| 037 | Segregação do Crédito Decorrente do Pagamento Antecipado do ICMS Devido na Saída Subsequente à Importação, com Utilização de Crédito Presumido ***(Redação dada pelo Art. 3º da Portaria SEF nº 070/17 - Efeitos fatos geradores a partir da referência abril/2017)*** |  | Considera-se lançamentos de Outros Débitos/Créditos com o tipo DÉBITO e subtipo SEGREGAÇÃO DO CRÉDITO DECORRENTE DO PAGAMENTO ANTECIPADO. |
| 038 | Segregação de outros créditos permitidos para compensar com o débito pela utilização do crédito presumido ***(Redação dada pelo Art. 1º da Portaria SEF nº 186/17 - Efeitos fatos geradores a partir da referência abril/2017)*** |  | Considera-se lançamentos de Outros Débitos/Créditos com o tipo DÉBITO e subtipo SEGREGAÇÃO DE OUTROS CRÉDITOS PERMITIDOS PARA COMPENSAR COM O DÉBITO. |
| 040 | Total de débitos |  | Soma dos Itens 010, 020, 030 |
| Totalização de Créditos | | | |
| 050 | Subtotal de créditos |  | Valor do item 990 do registro tipo 26 |
| 051 | Não se aplica |  |  |
| 052 | Não se aplica |  |  |
| 060 | Saldos credores recebidos de estabelecimentos consolidados |  | Saldos credores recebidos de estabelecimentos consolidados: Valor dos Lançamentos de Outros Débitos/ Créditos cujo Tipo é "Outros Créditos" e Sub Tipo é "Recebimento de Crédito". |
| 070 | Créditos recebidos por transferência de outros contribuintes |  | Gerado de acordo com dados informados na tabela de Regime Especial, a partir dos valores das linhas em que a Origem for igual a 1. |
| 075 | Créditos declarados no DCIP |  | Este registro será gerado com as informações declaradas na aba Regime Especial da tela de geração da rotina, cujo campo Origem tenha valor 14. |
| 076 | Segregação dos Débitos Relativos às Saídas com Crédito Presumido em Substituição aos Créditos pelas Entradas ***(Redação dada pelo Art. 3º da Portaria SEF nº 070/17 - Efeitos fatos geradores a partir da referência abril/2017)*** |  | Será gerado com base nos lançamentos de Outros Débitos/Créditos do Tipo CRÉDITO e subtipo SEGREGAÇÃO DOS DÉBITOS COM CRÉDITO PRESUMIDO. |
| 080 | Total de créditos | Soma dos Itens 050, 060, 070, 080 |  |
| Ajuste da apuração decendial e antecipações | | | |
| 090 | Imposto do 1º decêndio | Não gerado |  |
| 100 | Imposto do 2º decêndio | Não gerado |  |
| 105 | Antecipações Combustíveis líquidos e gasosos |  |  |
| 110 | Total de ajustes da apuração decendial e antecipações | Não gerado |  |
| 120 | Saldo devedor (Total de Débitos – (Total de Créditos + Total de ajustes da apuração decendial e antecipações)) | Saldo Devedor | Obs.: Item não gerado quando as opções Movimento com valor “Sem movimento e com Saldo” e “Sem movimento e sem Saldo” estiverem marcadas. |
| 130 | Saldo devedor transferido ao estabelecimento consolidador |  | Saldo Devedor Transferido ao estabelecimento consolidador: Valor dos Lançamentos de Outros Débitos/ Créditos cujo Tipo é "Outros Créditos" e Sub Tipo é "Transferência de Débito". |
| 999 | Imposto a Recolher | Imposto a Recolher | Obs.: Item não gerado quando as opções Movimento com valor “Sem movimento e com Saldo” e “Sem movimento e sem Saldo” estiverem marcadas. |
| 140 | Saldo Credor |  | (Total de Créditos + Total de ajustes da apuração decendial e antecipações) – Total de Débitos |
| 150 | Saldo credor transferido ao estabelecimento consolidador |  | Valor dos Lançamentos de Outros Débitos/ Créditos cujo Tipo é "Outros Débitos" e Sub Tipo é "Transferência de Crédito". |
| 998 | Saldo Credor para o mês seguinte |  | Saldo Credor para o Período Seguinte |
| Discriminação do saldo credor para o mês seguinte | | | |
| 160 | Saldo credor transferível relativo à exportação. | Não gerado |  |
| 170 | Saldo credor transferível relativo a saídas isentas. | Não gerado |  |
| 180 | Saldo credor transferível relativo a saídas diferidas | Não gerado |  |
| 190 | Saldo credor relativo a outros créditos |  | Gerado com o mesmo valor do item 998 |

true1R32

Exemplo do Registro gerado no arquivo.

01\_1true01\_2Campos

Os itens deste registro só serão gerados se o campo Substituto Tributário, da Tela da rotina, está marcado como "Sim", "Substituto Solidário".

São consideradas apenas operações internas.

A geração é toda baseada nas regras de apuração do ICMS ST.

Lançamentos de Outros Débitos e Créditos e Saldo do Período anterior são considerados os vinculados ao Estado da Filial que se está gerando a rotina.

Informações sobre Substituição Tributária

| ITENS | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| **Informações sobre substituição tributária** | | | |
| 010 | Não se aplica |  | Item não é gerado |
| 020 | Não se aplica |  | Item não é gerado |
| 030 | Não se aplica |  | Item não é gerado |
| 040 | Não se aplica |  | Item não é gerado |
| 050 | Não se aplica |  | Item não é gerado |
| 060 | Base cálculo ICMS substituição tributária | Campo "Base Subst. Tributária" da Situação Tributária | BASESUBST |
| 065 | Imposto Retido apurado por mercadoria e recolhido por operação. |  | Item não é gerado |
| Débitos | | | |
| 070 | Imposto retido com apuração mensal | Campo "Valor ST" da Situação Tributária | VALORSUBST |
| 073 | Imposto Retido pelo AEHC com regime especial de apuração mensal. |  | Item não é gerado |
| 075 | Saldos devedores recebidos de estabelecimentos consolidados. |  | Item não é gerado |
| 080 | Total de débitos | Campo "Valor ST" da Situação Tributária | VALORSUBST |
| Créditos | | | |
| 090 | Saldo credor do período anterior sobre a substituição tributária | Campo "Saldo Tributo Anterior" da Apuração ICMS ST do Período de Apuração. | SaldoAnt do Período |
| 100 | Não se aplica |  | Item não é gerado |
| 105 | Créditos declarados no DCIP | De acordo com a tela de Regime de Apuração | Dados da tabela de Regime Especial cuja origem seja 16 |
| 110 | Não se aplica | Lançamento outros créditos, ICMSST, Subtipo Ressarcimento ST | Valor do lançamento de ajuste. |
| 115 | Ressarcimento do ICMS substituição tributária acobertado por NF-e (Redação acrescentada pelo Art. 2 da Portaria SEF nº 007/19 - Efeitos a partir de 01.01.19) |  | Item não é gerado |
| 116 | Devolução de mercadorias e desfazimento de venda (Redação acrescentada pelo Art. 4 da Portaria SEF N° 153 de 2012) |  | Quando o lançamento for de entrada, a regra de ICMS for de Substituição Tributária e a natureza for de Devolução, é considerado o campo DLAF.VALORSUBST |
| 120 | Não se aplica |  | Item não é gerado |
| 125 | Saldos credores recebidos de estabelecimentos consolidados |  | Item não é gerado |
| 130 | Total de créditos |  | Item 090 + Item 105 |
| 140 | Não se aplica |  | Item não é gerado |
| 150 | Não se aplica |  | Item não é gerado |
| 155 | Antecipações Combustíveis líquidos e gasosos |  | Item não é gerado |
| 160 | Total de ajustes das Antecipações Combustíveis |  | Item não é gerado |
| 170 | Saldo devedor |  | Item 080 - Item 130 |
| 180 | Saldo devedor transferido ao estabelecimento consolidador |  | Item não é gerado |
| 999 | Imposto a recolher sobre a substituição tributária |  | Item 170 |
| 190 | Saldo Credor (Total de Créditos + Total de ajustes das antecipações combustíveis) - (Total de Débitos)) |  | Item 130 - Item 080 |
| 200 | Saldo credor transferido ao estabelecimento consolidador. |  | Item não é gerado |
| 998 | Saldo Credor para o mês seguinte. |  | Item 190 |

true1R3301\_1true01\_2Campos

São selecionadas as Guias Normais e GNR vinculadas aos períodos de ICMS e ICMS ST respectivamente e que se encontram dentro do mês/ Ano de Referência.

**IMPORTANTE:** Para geração das Guias GNR serão consideradas apenas operações internas. (Campo ***UF*** da guia com o mesmo ***"Estado"*** da Filial).

Discriminação dos Pagamentos do Imposto e dos Débitos Específicos

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Preenche com "33" | Valor fixo |
| 02 | Quadro | Preenche com "12" | Valor fixo |
| 03 | Origem do Recolhimento | Prencher com   1 – Imposto,   2 – Substituição Tributária,   3 – Débitos Específicos | Se FlagGuiaPerNormal  Então: 1  Senão: 2  Observação: Opção 3 - Débitos Específicos não é gerada |
| 04 | Código de Receita | Código da Receita conforme tabela constante da Portaria SEF 164/04 | Gerado com o Campo Código da Receita da Guia DGUIAPERIODO.CODRECEITA |
| 05 | Data do vencimento do recolhimento DDMMAAAA |  | Gerado como Campo Data de Vencimento informado na Guia de Pagamento. DGUIAPERIODO.DATAVENC |
| 06 | Valor do recolhimento | Valor do recolhimento | Gerado com o Valor pago da Guia DGUIAPERIODO.VALORAPURADO |
| 07 | Classe do Vencimento | Código da Classe de Vencimento conforme Portaria do Secretário de Estado da Fazenda | Gerado com o valor do campo classe de vencimento da guia DGUIAPERIODO.CLASSEVENCIMENTO |
| 08 | Número do acordo | Número do registro do acordo de Tratamento Tributário Diferenciado - TTD ou Regime Especial | Não gerado |

true1R3401\_1true01\_2Campos

Demonstrativo dos valores do imposto relativo à parcela da diferença de alíquota devido a este Estado em decorrência da realização de operação que destinem bens ou serviços a consumidor final não contribuinte do imposto localizado em outra unidade da federação, em conformidade com o disposto na Emenda Constitucional 87/2015.

Este registro é gerado conforme as informações do Período de Apuração, subpasta Valores Diferencial de Alíquota onde o Campo “Remetente” seja igual a “SIM”.

Informações sobre Diferença de Alíquota de Operação Interestadual à Consumidor

|  |  |  |  |
| --- | --- | --- | --- |
| **ITENS** | **CAMPOS** | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| **Débitos** | | | |
| 010 | Débito da diferença de alíquota devido ao Estado |  | Debito Diferencial Alíquota |
| 020 | Outros débitos |  | Outros Débitos |
| 040 | Total de débitos |  | Soma dos itens 010 e 020 deste quadro |
| **Créditos** | | | |
| 050 | Saldo credor do período anterior sobre a diferença de alíquota |  | Saldo Credor/Devedor Anterior |
| 060 | Devolução de mercadorias e anulações de venda |  | Crédito Diferencial de Alíquota |
| 070 | Outros créditos |  | Outros Créditos |
| 090 | Total de créditos |  | Soma dos Itens 050, 060 e 070 deste quadro |
| **Pagamentos antecipados** | | | |
| 100 | Pagamentos Antecipados | Não será gerado |  |
| 110 | Total Pagamentos Antecipados | Não será gerado |  |
| **Saldo Devedor** | | | |
| 120 | Saldo devedor | Gerado somente se o saldo for devedor | Item 040 – Item 090 |
| 130 | Saldo devedor a compensar em conta gráfica | Gerado somente se o saldo for devedor (Item 040 – Item 090) | Item 120 |
| **Saldo Credor** | | | |
| 150 | Saldo Credor | Gerado somente se o saldo apurado for credor | Item 090 – Item 040 |
| 998 | Saldo Credor da diferença de alíquota para o mês seguinte | Gerado com o saldo credor transportado para o período seguinte | Item 150 |

true1R3501\_1true01\_2CamposDemonstrativo da apuração do imposto devido pela apropriação do crédito presumido em ST aos créditos pelas entradas (DAICP)

| ITENS | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 010 | Valor da Base de Cálculo das Saídas com Crédito Presumido |  | Gerado conforme informação gravada no campo  BC DA SAÍDA COM CRÉDITO PRESUMIDO da tela de geração da rotina. |
| 020 | Débitos Relativos às Saídas com Crédito Presumido em Substituição aos Créditos pelas Entradas |  | Gerado conforme os lançamentos de Outros Débitos/Créditos com o tipo CRÉDITO  e subtipo SEGREGAÇÃO DOS DÉBITOS COM CRÉDITO PRESUMIDO. Este campo é gerado também no Quadro 9 item 076. |
| 030 | Crédito Presumido Utilizado em Substituição aos Créditos pelas Entradas |  | Gerado conforme os lançamentos de Outros Débitos/Créditos com o tipo DÉBITO e subtipo SEGREGAÇÃO DO CRÉDITO PRESUMIDO. Este campo deve ser gerado também no Quadro 9 item 036. |
| 031 | Créditos Permitidos para Compensar com o Débito pela Utilização do Crédito Presumido ***(Redação dada pelo Art. 4º da Portaria SEF nº 186/17 - Efeitos fatos geradores a partir da referência abril/2017)*** |  | Gerado conforme os lançamentos de Outros Débitos/Créditos com o tipo DÉBITO e subtipo SEGREGAÇÃO DE OUTROS CRÉDITOS PERMITIDOS PARA COMPENSAR COM O DÉBITO. Este campo deve ser gerado também no Quadro 9 item 038. |
| 040 | Saldo Devedor Apurado pela Apropriação do Crédito Presumido no Mês |  | Calculado com o valor da diferença entre o item 030, 31 e o item 020, se o total de débitos for maior que o total dos créditos. Preenchido com zero quando o resultado for igual a zero. |
| 045 | (=) Débito pela utilização do crédito presumido recebido de estabelecimento consolidado ***(Redação dada pelo Art. 1º da Portaria SEF nº 230/17 - Efeitos a partir da referência agosto/2017)*** |  | Transportado do registro 34 |
| 050 | Débito Apurado pela Apropriação Extemporânea do Crédito Presumido |  | Não gerado |
| 110 | Saldo Credor das Antecipações para o Mês Seguinte Apurado no Mês Anterior |  | Gerado conforme valor informado no campo SALDO CREDOR DAS ANTECIPAÇÕES PARA O MÊS SEGUINTE APURADO NO MÊS ANTERIOR localizado na aba Outros Dados da tela de geração da rotina. |
| 120 | Crédito decorrente do Pagamento Antecipado do ICMS Devido na Saída Subsequente à Importação, com Utilização de Crédito Presumido |  | Gerado conforme os lançamentos de Outros Débitos/Créditos com o tipo DÉBITO e subtipo SEGREGAÇÃO DO CRÉDITO DECORRENTE DO PAGAMENTO ANTECIPADO. Este campo deve ser também gerado no Quadro 09 item 037. |
| 130 | Total das Antecipações |  | Somatório dos itens 110 e 120 deste quadro |
| 150 | Débito pela utilização do crédito presumido transferido ao estabelecimento consolidador consolidado ***(Redação dada pelo Art. 1º da Portaria SEF nº 230/17 - Efeitos a partir da referência agosto/2017)*** |  | Não gerado |
| 199 | Imposto a Recolher pela Utilização do Crédito Presumido |  | Preenchido com o valor da diferença entre o somatório dos itens 040 e 050 e o item 130, se o somatório dos itens 040 e 050 for maior que o item 130. Preencher com valor zero (0) quando o resultado for negativo, zerado ou quando o valor do item 130 for maior que o somatório dos itens 040 e 050. |
| 198 | Saldo Credor das Antecipações para o Mês Seguinte |  | Preenchido com a diferença entre o item 130 e o somatório dos itens 040 e 050, sempre que o valor resultar valor maior que zero (0). |

true1R3601\_1Gerado a partir do preenchimento do "Quadro 15" na tela de geração da rotina, caso o quadro não seja preenchido o registro não será gerado.  
  
Para informações de utilização da tela desse registro, confira a seção ""true01\_2CamposDemonstrativo dos valores devidos aos fundos como contrapartida pela utilização de benefício fiscal

Valores gerados conforme campos da aba "Quadro 15" da tela de geração da rotina.

| ITENS | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Tipo do registro | Valor fixo: '36' |
| 02 | Quadro | Numeração do quadro | Valor fixo: '15' |
| 03 | Sequencial |  | Gerado automaticamente |
| 04 | Código do Benefício TTD |  | Gerado conforme valor do campo "Código TTD" |
| 05 | Número da Concessão do TTD |  | Gerado conforme valor do campo "Num Concessão TTD" |
| 06 | Subtipo DCIP Crédito Presumido sem exigência de TTD |  | Gerado conforme valor do campo "Subtipo DCIP" |
| 07 | Valor da Base Cálculo ICMS das Operações ou Prestações para cada Número de Concessão |  | Gerado conforme valor do campo "Valor BC ICMS" |
| 08 | Valor do ICMS Exonerado para cada Número de Concessão |  | Gerado conforme valor do campo "Valor ICMS Exonerado" |
| 09 | Código Cálculo FUMDES |  | Gerado conforme valor do campo "Cód. FUMDES" |
| 10 | Valor FUMDES |  | Gerado conforme valor do campo "Valor FUMDES" |
| 11 | Código Cálculo FUNDO SOCIAL |  | Gerado conforme valor do campo "Cód. FUNDO SOCIAL" |
| 12 | Valor do FUNDO SOCIAL |  | Gerado conforme valor do campo "Valor FUNDO SOCIAL" |
| 13 | Valor Base de Cálculo do ICMS na NF de Devolução Relativo a cada Número de Concessão |  | Gerado conforme valor do campo "Valor BC ICMS na NF" |
| 14 | Valor ICMS Exonerado Correspondente a Devolução Relativo a cada Número de Concessão |  | Gerado conforme valor do campo "Devol. ICMS" |
| 15 | Valor do FUMDES Relativo à Devolução |  | Gerado conforme valor do campo "Devol. FUMDES" |
| 16 | Valor do FUNDO SOCIAL Relativo à Devolução |  | Gerado conforme valor do campo "Devol. FUNDO SOCIAL" |

true1R3701\_1

Gerado a partir do preenchimento do "Quadro 16" na tela de geração da rotina, caso o quadro não seja preenchido o registro não será gerado.

true01\_2CamposDemonstrativo da Apuração de Valores Devidos ou Saldo Credor de Fundos 

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo 37 |
| 02 | Quadro | Automático | Valor fixo 16 |
| 03 | Item |  | Célula "Código" da tabela do quadro 16 |
| 04 | Valor |  | Célula "Valor" da tabela do quadro 16 |

true1R4601\_1true01\_2Campos

Caso qualquer célula da coluna "Origem" seja preenchida com valor "1", "14" ou "16", todos os valores preenchidos na tabela "Regime Especial" serão gerados no registro 46.

Créditos por Regimes Especiais

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo '46' |
| 02 | Quadro | Automático | Valor fixo '46' |
| 03 | Sequência | Automático | Valor fixo '990' para o registro totalizador. Para os demais, preenchido com valor incremental |
| 04 | Identificação |  | Célula "Número" da tabela de Regime Especial |
| 05 | Valor |  | Célula "Valor" da tabela de Regime Especial |
| 06 | Origem |  | Célula "Origem" da tabela de Regime Especial |

true1R4701\_1true01\_2Campos

Serão selecionados Lançamentos Fiscais que não estejam Estornados ou Cancelados, associados a Naturezas de Operação cujo campo Tipo Natureza (Rotinas Legais) esteja definido como: "Compras a Extrat. Prod. Agrop. e Pescadores" ou "Receitas Prest. de Serv. e Energia Elétrica".

A data do Lançamento Fiscal deve está dentro do Período de Apuração selecionado na tela de geração da rotina.

A Unidade da Federação onde se iniciou ou realizou-se a operação ou prestação de serviços deve ser Santa Catarina. Esta informação é buscada no campo "UF" (Lançamento Fiscal / Situação Tributária/ Aba Prestação de Serviços).

São gerados registros totalizados por Município.

Entradas de Extratores, Produtores Agropecuários e Pescadores

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo '47' |
| 02 | Quadro | Automático | Valor fixo '47' |
| 03 | Código do Município |  | Codificação de Município informado como anexo ao município informado na Situação Tributária, Aba Prestação de Serviços |
| 04 | Valor da compra |  | Valor Total da Situação Tributária |

true1R4801\_1true01\_2Campos

Serão selecionados Lançamentos Fiscais de Saída que não estejam Estornados ou Cancelados, associados a Naturezas de Operação onde a natureza tenha o campo Tipo Natureza (Rotinas Legais) definido como: "Compras a Extrat. Prod. Agrop. e Pescadores" ou "Receitas Prest. de Serv. e Energia Elétrica" e o campo Classificação CFOP preenchido.

Serão selecionados somente Lançamentos Fiscais de Saída em que a Unidade da Federação onde se iniciou ou realizou-se a operação ou prestação de serviços tenha sido preenchida. Esta informação é buscada no campo "UF" (Lançamento Fiscal / Situação Tributária/ Aba Prestação de Serviços).

Serão selecionados Lançamentos Fiscais de Saída, Operações Internas e Interestaduais.

São gerados registros totalizados por Município, para os municípios do estado de Santa Catarina.

Para municípios de Outras Unidades da Federação, os registros serão totalizados sob o código 80047.

Informações para Rateio do Valor Adicionado

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor Fixo '48' |
| 02 | Quadro | Automático | Valor Fixo '48' |
| 03 | Código do Município |  | Código do Município informado no Lançamento Fiscal Sub Pasta Outros Dados / Aba Prestação de Serviços |
| 04 | Valor |  | Campo Valor Total da Situação Tributária |
| 05 | Código do Tipo de Atividade |  | Campo Classificação CFOP da Natureza |

true1R4901\_1true01\_2Campos

Serão selecionados os Lançamentos Fiscais de entrada cuja Natureza de Operação associada seja Fiscal.

A data do Lançamento Fiscal deve está dentro do Mês/Ano de Referência selecionado na tela de geração da rotina.

Os registros serão totalizados por UF.

Entradas por Unidade da Federação

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor Fixo '49' |
| 02 | Quadro | Automático | Valor Fixo '49' |
| 06 | Sigla do Estado |  | Gerado com a informação do campo Estado do Cliente/Fornecedor |
| 07 | Valor Contábil |  | Campo Valor Total Do Documento Fiscal (Lançamento Fiscal) |
| 08 | Base de Cálculo |  | Campo Base Tributada ICMS (Situação Tributária) |
| 09 | Outras |  | Campo Outros ICMS (Situação Tributária) |
| 10 | Petróleo – Energia elétrica | Valor do ICMS cobrado por Substituição Tributária em Petróleo/Energia | Campo Valor ST (Situação Tributária com CFOP específico - Blocos 1.250 e 2.250) |
| 11 | Outros produtos | Valor do ICMS cobrado por Substituição Tributária em Outros produtos | Campo Valor ST (Situação Tributária) |

true1R5001\_1true01\_2Campos

Para este registro, serão selecionados os Lançamentos Fiscais de Saída cuja Natureza Fiscal associada é Fiscal.

A data do Lançamento Fiscal deve está dentro do Mês/ Ano de Referência selecionado na tela de geração da rotina, e são gerados registros totalizados por UF.

Saídas por Unidade da Federação

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor Fixo '50' |
| 02 | Quadro | Automático | Valor Fixo '50' |
| 06 | Sigla do Estado |  | Gerado com o Campo Estado do Lançamento Fiscal |
| 07 | Valor Contábil Não Contribuinte |  | Campo Valor Total da Situação Tributária |
| 08 | Valor Contábil Contribuinte |  | Campo Valor Total da Situação Tributária |
| 09 | Base de Cálculo Não Contribuinte |  | Campo Base Tributada ICMS (Situação Tributária) |
| 10 | Base de Cálculo Contribuinte |  | Campo Base Tributada ICMS (Situação Tributária) |
| 11 | Outras |  | Soma dos campos Isento ICMS e Outros ICMS (Situação Tributária) |
| 12 | ICMS Cobrado por Substituição Tributária |  | Campo Valor ST (Situação Tributária) |

Observações:

* Alguns valores deste registro são totalizados por Contribuinte e Não contribuintes de ICMS:
* Lançamentos Fiscais associados a Filiais são totalizados como operações com Contribuintes.
* Lançamentos Fiscais associados com Cliente/Fornecedor são totalizados com base no campo Contribuinte de ICMS do Cadastro de Cliente Fornecedor.
* Lançamentos Fiscais associados com Estados são totalizados com base no campo Contribuinte do Cadastro de Lançamentos.
true1R5101\_1true01\_2Campos Registro Exclusões de Valores para Apuração do Valor Adicionado

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo 51 |
| 02 | Quadro | Automático | Valor fixo 51 |
| 03 | Item |  | Célula "Código" da tabela de Execuções |
| 04 | Valor |  | Célula "Valor" da tabela de Execuções |

true1R8001\_1true01\_2CamposResumo do Livro Registro de Inventário e Receita Bruta

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo 80 |
| 02 | Quadro | Automático | Valor fixo 80 |
| 03 | Item |  | Célula "Código" da tabela de Inventário |
| 04 | Valor |  | Célula "Valor" da tabela de Inventário |

true1R8101\_1true01\_2CamposAtivo

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo "81" |
| 02 | Quadro | Automático | Valor fixo "81" |
| 03 | Item |  | Célula "Código" da tabela de Ativos |
| 04 | Valor |  | Célula "Valor" da tabela de Ativos |

true1R8201\_1true01\_2CamposPassivo

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo 82 |
| 02 | Quadro | Automático | Valor fixo 82 |
| 03 | Item |  | Célula "Código" da tabela de Passivos |
| 04 | Valor |  | Célula "Valor" da tabela de Passivos |

true1R8301\_1true01\_2CamposDemonstração de Resultados

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo 83 |
| 02 | Quadro | Automático | Valor fixo 83 |
| 03 | Item |  | Célula "Código" da tabela de Resultados |
| 04 | Valor |  | Célula "Valor" da tabela de Resultados |

true1R8401\_1true01\_2CamposDetalhamento das Despesas

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo 84 |
| 02 | Quadro | Automático | Valor fixo 84 |
| 03 | Item |  | Célula "Código" da tabela de Despesas |
| 04 | Valor |  | Célula "Valor" da tabela de Despesas |

true1R8501\_1true01\_2CamposDetalhamento das Contribuições

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo 85 |
| 02 | Quadro | Automático | Valor fixo 85 |
| 03 | Item |  | Célula "Código" da tabela de Contribuições |
| 04 | Valor |  | Célula "Valor" da tabela de Contribuições |

true1R9001\_1true01\_2CamposResumo do Livro Registro de Inventário e Receita Bruta (Encerramento de Atividades)

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo "90" |
| 02 | Quadro | Automático | Valor fixo "90" |
| 03 | Item |  | Célula "Código" da tabela de Inventário |
| 04 | Valor |  | Célula "Valor" da tabela de inventário |

true1R9101\_1true01\_2CamposAtivo

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo "91" |
| 02 | Quadro | Automático | Valor fixo "91" |
| 03 | Item |  | Célula "Código" da tabela de Ativos |
| 04 | Valor |  | Célula "Valor" da tabela de Ativos |

true1R9201\_1true01\_2CamposPassivo

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo "92" |
| 02 | Quadro | Automático | Valor fixo "92" |
| 03 | Item |  | Célula "Código" da tabela de Passivos |
| 04 | Valor |  | Célula "Valor" da tabela de Passivos |

true1R9301\_1true01\_2CamposDemonstração de Resultados (Encerramento de Atividades)

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo 93 |
| 02 | Quadro | Automático | Valor fixo 93 |
| 03 | Item |  | Célula "Código" da tabela de Resultados |
| 04 | Valor |  | Célula "Valor" da tabela de Resultados |

true1R9401\_1true01\_2CamposDetalhamento das Despesas (Encerramento de Atividades)

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor fixo 94 |
| 02 | Quadro | Automático | Valor fixo 94 |
| 03 | Item |  | Célula "Código" da tabela de Despesas |
| 04 | Valor |  | Célula "Valor" da tabela de Despesas |

true1R9801\_1true01\_2CamposEncerramento da Declaração

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor Fixo "98" |
| 02 | Quadro | Automático | Preenchido com dois espaços em branco |
| 03 | Quantidade de Registros | Automático | Quantidade de registros presentes no arquivo **antes** do registro 98 |

true1R9901\_1true01\_2CamposEncerramento do Arquivo

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo de Registro | Automático | Valor Fixo "99" |
| 02 | Quadro | Automático | Preenchido com dois espaços em branco |
| 03 | Quantidade de Registros | Automático | Quantidades de registros presentes no arquivo, incluindo o próprio registro 99 |
| 04 | Quantidade de Declarações de ICMS | Automático | Preenchido com "1" |

# 03. Como gerar a DIME-SC?

A geração da DIME-SC no módulo fiscal encontra-se disponível em Obrigações Acessórias > Estaduais > DIME e, para utilizá-la, basta baixar seu layout mais recente disponível no TOTVS Compartilhamento.

A tela de geração da DIME-SC é composta por várias tabelas, sendo elas referentes aos valores de Ativos, Passivos, Resultados, Despesas, Inventário e Exclusões, além de outra tabela acerca de Regime Especial. Esta seção visa esclarecer eventuais dúvidas de utilização da tela de geração.

Utilização da telaleftAdicionar linhas

Para adicionar uma linha, basta clicar nas últimas células em branco e informar os valores desejados.

Excluir linhas

Para excluir uma linha, basta clicar na linha desejada à esquerda e pressionar a tecla "Delete".

Ordenar colunas

Caso desejado, é possível ordenar as colunas em ordem crescente e decrescente, ao clicar no cabeçalho da coluna. Essa funcionalidade pode ajudar em casos que, por exemplo, um código menor que os demais seja adicionado ao final da tabela, para exibi-lo ao topo dos demais após inclui-lo.  
Pode-se ordenar qualquer coluna, seja o "Código", a "Descrição" e o "Valor" das tabelas de "Ativo", "Passivo", "Resultados", "Despesas", "Inventário" e "Exclusões". Também é possível ordenar as colunas de "Valor", "Nome" e "Origem" da tabela "Regime Especial".  
Independentemente de as colunas estarem ordenadas ou não, o arquivo gerado pela rotina ordenará os valores da coluna "Código" em ordem crescente.  
Cada clique no cabeçalho da coluna alternará entre ordenação crescente ou decrescente.

Restaurar campos

Como as outras rotinas do TOTVS Gestão Fiscal, a DIME permite que seus parâmetros de geração sejam salvos. Logo, caso essa opção esteja selecionada na rotina, os campos e valores inseridos nas tabelas da DIME também serão salvos. Para retornar aos campos padrão da rotina, há um botão de "Redefinir campos ao padrão". Este botão zera os valores de todos os campos, exclui os campos inseridos manualmente e restaura todos os campos padrão que foram excluídos da tela. Esta ação é realizada em todas as tabelas, exceto a de Regime Especial, na qual não há campos padrão.

Quadro 15NavegaçãoInserir aba

Por padrão, a tela do Quadro 15 vem com uma aba para ser preenchida. Caso seja necessário adicionar mais abas, clique em "Novo Demonstrativo".

Excluir aba

Para excluir uma aba de demonstrativo, selecione a aba desejada e clique em "Excluir Demonstrativo".  
O número sequencial será recalculado automaticamente ao excluir uma aba.

Outras informações

Os botões de "Novo Demonstrativo" e "Excluir Demonstrativo" apenas serão habilitados quando a aba do "Quadro 15" estiver selecionada. O botão de "Restaurar Campos" será desabilitado durante o uso do "Quadro 15".  
  
As informações incluídas na aba do "Quadro 15" também são salvas nas preferências de usuário. Caso deseje inserir novos valores, edite os valores dos demonstrativos, ou exclua os demonstrativos existentes e inclua novos.  
  
Caso uma aba seja adicionada e nenhuma informação seja preenchida nela, ela não será salva nas preferências de usuário. O número sequencial será recalculado quando houver abas vazias.  
Entretanto, caso qualquer campo seja preenchido no demonstrativo, mesmo que com zeros, o demonstrativo será salvo e considerado na geração da rotina.

Parâmetros Quadros 80

Quanto aos quadros 80, 81, 82, 83, 84 e 85, existem alguns parâmetros em comum que devem ser passados caso sua geração seja necessário para a rotina. Sendo o checkbox "Gerar Declaração complementar" obrigatório para geração de todos estes.

Para geração dos quadros 90, 91, 92, 93 e 94, é necessário que o campo "Tipo Declaração" esteja selecionado com "Encerramento de Atividades".

Além desse parâmetro em comum, para os registros 80, 82 e 85, é necessário que o campo "Tem Escrita Contábil" esteja selecionado como "Sim, estab. principal" e/ou "Sim, dados do estabelecimento principal".

Para geração dos registros 81, 82 e 83, é necessário que o campo "Tem Escrita Contábil" esteja selecionado apenas como "Sim, dados do estabelecimento principal".

Validações das colunas

Para as tabelas de Ativo, Passivo, Resultados, Despesas, Inventário e Exclusões:

| Código | Descrição | Valor |
| --- | --- | --- |
| Apenas números, com limite de 3 números¹. **Campo obrigatório**. | Caracteres alfanuméricos e caracteres especiais, sem limite de tamanho | Apenas números e uma vírgula, suportando apenas duas casas decimais |

¹Caso um número com menos de 3 dígitos seja informado, ele será automaticamente completado com zeros à esquerda, até o seu limite.

Para a tabela de Regime Especial:

| Valor | Número | Origem |
| --- | --- | --- |
| Apenas números e uma vírgula, suportando apenas duas casas decimais | Caracteres alfanuméricos e caracteres especiais, com limite de 15 caracteres | Apenas números, sem limite de tamanho. Não aceita zeros à esquerda. |

Para a tabela do Quadro 15:

| Campo | Validação |
| --- | --- |
| Código TTD | Apenas números, limite de 4 dígitos |
| Num Concessão TTD | Apenas números, limite de 15 dígitos |
| Subtipo DCIP | Apenas números, limite de 4 dígitos |
| Cód. FUMDES | Caractere alfanumérico, limite de 1 caractere |
| Valor FUMDES | Apenas números e uma vírgula, suportando apenas duas casas decimais |
| Devol. FUMDES | Apenas números e uma vírgula, suportando apenas duas casas decimais |
| Cód. FUNDO SOCIAL | Caractere alfanumérico, limite de 1 caractere |
| Valor FUNDO SOCIAL | Apenas números e uma vírgula, suportando apenas duas casas decimais |
| Devol. FUNDO SOCIAL | Apenas números e uma vírgula, suportando apenas duas casas decimais |
| Valor BC ICMS | Apenas números e uma vírgula, suportando apenas duas casas decimais |
| Valor ICMS Exonerado | Apenas números e uma vírgula, suportando apenas duas casas decimais |
| Valor BC ICMS na NF | Apenas números e uma vírgula, suportando apenas duas casas decimais |
| Devol. ICMS | Apenas números e uma vírgula, suportando apenas duas casas decimais |

Campos padrão da telaCamposPadraoAtivo

| Código | Descrição |
| --- | --- |
| 110 | (=) Circulante |
| 111 | (+) Disponibilidades |
| 113 | (+) Contas a receber do circulante |
| 121 | (+) Estoque de mercadoria e matéria prima |
| 123 | (+) Outros estoques |
| 128 | (+) Outras contas do ativo circulante |
| 130 | (=) Realizável a longo prazo |
| 131 | (+) Contas a receber do realizável |
| 148 | (+) Outras contas do realizável |
| 150 | (=) Permanente |
| 151 | (+) Investimentos |
| 155 | (+) Imobilizado (líquido) |
| 157 | (+) Diferido (líquido) |
| 159 | (=) Total geral do ativo |

Passivo

| Código | Descrição |
| --- | --- |
| 210 | (=) Circulante |
| 211 | (+) Fornecedores |
| 213 | (+) Empréstimos e financiamentos |
| 215 | (+) Outras contas do passivo circulante |
| 230 | (=) Exigível a longo prazo |
| 240 | (=) Resultados de exercícios futuros |
| 269 | (=) Passivo a descoberto |
| 270 | (=) Patrimônio líquido |
| 271 | (+) Capital social |
| 278 | (+) Outras contas do patrimônio líquido |
| 279 | (+) Outras contas do patrimônio líquido (de valor negativo) |
| 299 | (=) Total geral do passivo |

Resultados

| Código | Descrição |
| --- | --- |
| 310 | (+) Receita bruta vendas/serviços |
| 311 | (-) Deduções da receita bruta |
| 320 | (=) Receita líquida vendas/serviços |
| 323 | (-) Custo da mercadoria ou produtos vendida(os) ou dos serviços prestados |
| 330 | (=) Lucro bruto |
| 331 | (=) Prejuízo bruto |
| 333 | (+) Outras receitas operacionais |
| 335 | (-) Despesas operacionais |
| 340 | (=) Lucro operacional |
| 341 | (=) Prejuízo operacional |
| 343 | (+) Receitas não operacionais |
| 345 | (-) Despesas não operacionais |
| 350 | (=) Resultado antes do I.R. e da contribuição social |
| 351 | (=) Resultado negativo antes do I.R. e da contribuição social |
| 353 | (-) Provisão para o IR e para a contribuição social |
| 360 | (=) Resultado após o I.R. e a contribuição social |
| 361 | (=) Resultado negativo após o I.R. e a contribuição social |
| 363 | (-) Participações e contribuições |
| 398 | (=) Prejuízo do exercício |
| 399 | (=) Lucro do exercício |

Despesas

| Código | Descrição |
| --- | --- |
| 411 | (+) Pró-labore |
| 412 | (+) Comissões, salários, ordenados |
| 421 | (+) Encargos sociais |
| 422 | (+) Tributos federais |
| 423 | (+) Tributos estaduais |
| 424 | (+) Tributos municipais |
| 431 | (+) Combustíveis e lubrificantes |
| 432 | (+) Água e telefone |
| 433 | (+) Energia elétrica |
| 441 | (+) Aluguéis |
| 442 | (+) Seguros |
| 443 | (+) Fretes e carretos |
| 451 | (+) Serviços profissionais |
| 461 | (+) Despesas financeiras |
| 498 | (+) Outras despesas |
| 499 | (=) Total |

Inventário

| Código | Descrição |
| --- | --- |
| 010 | Estoque no início do exercício |
| 020 | Estoque no fim do exercício |
| 030 | Receita bruta de vendas e serviços |

Exclusões

| Código | Descrição |
| --- | --- |
| 010 | (+) Prestação de serviços sujeita ao ISS |
| 020 | (+) 25% das transferências recebidas a preço de venda a varejo |
| 030 | (+) IPI relativo à aquisição de matérias-primas e mercadorias |
| 040 | (+) Parcela do ICMS retido por (Substituição Tributária) |
| 050 | (+) Subsídios concedidos por órgãos dos governos federal, estadual ou municipal |
| 060 | (+) Prestação de serviços sujeita ao ISS |
| 070 | (+) 25% das transferências efetuadas a preço de venda a varejo |
| 080 | (+) IPI incidente na saída de mercadorias |
| 090 | (+) Parcela do ICMS retido por Substituição Tributária |
| 980 | (=) Total dos valores excluídos das entradas |
| 990 | (=) Total dos valores excluídos das saídas |

# 04. Atualização de Layout

A Secretaria da Fazenda de Santa Catarina (SEF/SC) realiza atualizações periódicas no layout da DIME-SC, com o objetivo de adequar a declaração às novas exigências legais e aprimorar a coleta de informações fiscais e econômicas. Essas mudanças impactam a forma como os registros são gerados e exigem que os contribuintes ajustem suas configurações no sistema para garantir a conformidade com a legislação vigente.

Abaixo listamos as ultimas atualizações seguindo a publicação da [Portaria SEF N° 059/2023](https://legislacao.sef.sc.gov.br/html/portarias/2023/port_23_059.htm).

Os itens abaixo não serão gerados a partir de Março/2023.

**Quadro 04 - Resumo da Apuração dos Débitos:**

* Item 045 - Débito da Diferença de Alíquota de Operação ou Prestação a Consumidor Final de Outro Estado.

**Quadro 05 - Resumo da Apuração dos Créditos:**

* Item 030 - Crédito de ativo permanente;
* Item 040 - Crédito por diferencial de alíquota material de uso/consumo;
* Item 045 - Crédito da Diferença de Alíquota de Operação ou Prestação a Consumidor Final de Outro Estado;
* Item 050 - Crédito de ICMS retido por substituição tributária.

**Quadro 09 - Cálculo do Imposto a Pagar ou Saldo Credor:**

* Item 090 - Imposto do Primeiro Decêndio;
* Item 100 - Imposto do Segundo Decêndio;
* Item 105 - Antecipações Combustíveis Líquidos e Gasosos.

**Quadro 13 - Informações sobre Diferença de Alíquota de Operação Interestadual à Consumidor:** Esse registro não será mais gerado a partir de Março/2023.

Ainda de acordo com a referida Portaria, foi adicionado um item em um quadro que será gerado a partir de Março/2023, sendo ele:

**Quadro 11 - Informações sobre Substituição Tributária:** 

* Item 116 - Devolução de Mercadorias e Desfazimento de Venda
