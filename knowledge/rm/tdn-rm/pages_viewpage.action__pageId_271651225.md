---
content_hash: 6079868483766d3f291a492133faaae1a114cec28111ddd6a91d54e78a09ac54
fetched_at: '2026-06-29T00:08:27.948712+00:00'
page_id: '271651225'
product: rm
source: tdn-rm
title: RMFIS00003_Integração TAF x RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271651225
version: 8
---

**1. Artefatos Necessários**

Layout's disponibilizados na central de downloads para que seja importado pela ferramenta Gerador de Saídas.

* Layout: **TAF.TotvsGen**
* Layout: **TAF-ECF.TotvsGen**
* Layout: **TAF-Contabil.TotvsGen**

O script disponibilizado para criação da tabela **TAFST1** no Banco de Dados RM**,** esta tabela é utilizada para fazer a integração banco a banco com o TAF (Totvs Automação Fiscal).

* Script: **LI.2015.07\_02**

**2.Definição dos Layouts**

* **Layout TAF**

Integra as informações referentes a documentos fiscais e período de apurado do ICMS e do IPI, que serão utilizadas para atender as rotinas do SPED Fiscal (ICMS/IPI) e da EFD Contribuições (PIS/COFINS).

* **Layout TAF-ECF**

Integração dos registros no TAF com informações pertinentes rotina ECF (Escrituração Contábil Fiscal) em periodicidade definida no Cadastro de Parâmetros da ECF.

* **Layout TAF-Contábil**

Integração dos registros no TAF com informações pertinentes ao modulo Gestão Contábil RM, em periodicidade definida na parametrização

As parametrizações utilizadas nos layout´s TAF são as mesmas que são apresentadas na geração das rotinas Sped Fiscal (ICMS/IPI), EFD Contribuições e ECF.

**3. Registros Gerados pelos Layout's Disponibilizados**

Na tabela abaixo os campos marcados com "Sim" são gerados e "vazio" não são gerados.

|  |  |  |  |
| --- | --- | --- | --- |
| **Registro do Layout TAF (Totvs Automação Fiscal)** | **TAF** | **TAF-Contábil** | **TAF-ECF** |
| **T001 Complemento do Cadastro de Estabelecimentos** | Sim | Sim | Sim |
| **T001AA Cadastro de Inscrição do estabelecimento substituto** | Sim |  |  |
| **T001AB Processos referenciados** | Sim |  | Sim |
| **T001AC Cadastro de Veículos** | Sim |  |  |
| **T001AD Cadastro do Equipamento ECF/SAT-CF** | Sim |  |  |
| **T001AE Cadastro de Documento de Arrecadação** | Sim |  |  |
| **T001AF Campos extras - GNRE On-Line** |  |  |  |
| **T001AG Saldo em estoque por produto** |  |  |  |
| **T001AH Tabela de receita bruta mensal para fins de rateio de créditos comuns** | Sim |  |  |
| **T001AI Identificação de Períodos Dispensados da Escrituração Fiscal Digital das Contribuições - EFD Contribuições** |  |  |  |
| **T001AJ Código dos Totalizadores da Redução Z** | Sim |  |  |
| **T001AK Cadastro de Informações Complementares** | Sim |  |  |
| **T001AL Cadastro de Observações do Lançamento Fiscal** | Sim |  |  |
| **T001AM Identificação das empresas que possuem SCP (sócias Ostensivas)** | Sim | Sim | Sim |
| **T002 Informações do contabilista** | Sim |  | Sim |
| **T003 Cadastro de Participantes** | Sim |  |  |
| **T003AA Alteração do Cadastro de Participantes** | Sim |  |  |
| **T004 Regime de Apuração da Contribuição Previdenciária Sobre Receita Bruta** | Sim |  |  |
| **T005 Identificação das Unidades de Medida** | Sim |  |  |
| **T006 Cadastro de Unidade de Medida para o Fator de Conversão** | Sim |  |  |
| **T006AA Fatores de Conversão de Unidade de Medida** | Sim |  |  |
| **T007 Identificação do Item (Produtos/Serviços)** | Sim |  |  |
| **T007AA Alteração da Identificação do Item (Produtos/Serviços)** |  |  |  |
| **T007AB Consumo Especifico Padronizado** |  |  |  |
| **T008 Cadastro de Bens ou Componentes do Ativo Imobilizado** | Sim |  |  |
| **T009 Cadastro de Natureza de Operação** | Sim |  |  |
| **T010 Cadastro de Plano de Contas Contábeis** | Sim | Sim | Sim |
| **T010AA Plano de Contas Referencial** |  |  | Sim |
| **T010AB Subcontas Correlatas** |  |  | Sim |
| **T011 Cadastro de Centro de Custos** | Sim | Sim | Sim |
| **T012 Cadastro de AIDF** | Sim |  |  |
| **T012AA Documentos fiscais autorizados** | Sim |  |  |
| **T013 Cadastro de Documentos Fiscais (Nota Fiscal de Serviço/Mercadorias)** | Sim |  |  |
| **T013AA Cadastro de Informações Complementares de Documentos Fiscais** **(Modelos 01, 1B e 55)** | Sim |  |  |
| **T013AB Cadastro de Processos Referenciados por Informação Complementar** | Sim |  |  |
| **T013AC Cadastro de Operações de Importação** | Sim |  |  |
| **T013AD Modais de transporte (Modelo 26)** | Sim |  |  |
| **T013AE Cadastro de Documento de Arrecadação referenciado** | Sim |  |  |
| **T013AF Cadastro de Documento Fiscal Referenciado** | Sim |  |  |
| **T013AGCadastro de Cupom Fiscal Referenciado** | Sim |  |  |
| **T013AHCadastro de Coleta e/ou Entrega (Modelos 01, 1B e 04)** |  |  |  |
| **T013AICadastro de Faturas** **(Modelo 01)** | Sim |  |  |
| **T013AJ Cadastro de Vencimento de Faturas** | Sim |  |  |
| **T013AK Cadastro Complementar de Volumes Transportados e Operações com Combustíveis** **(Modelos 01 e 04)** | Sim |  |  |
| **T013AL Observações do Lançamento Fiscal (Modelos 01, 1B, 04 e 55)** | Sim |  |  |
| **T013AM Outras obrigações tributarias, ajustes e informações de valores provenientes dos documentos fiscais.** | Sim |  |  |
| **T013AN Complemento do Documento Fiscal** **(Modelos 06, 28 e 29)** | Sim |  |  |
| **T013AO Complemento do Documento Fiscal - Modelos 08, 8B e 26** | Sim |  |  |
| **T013AP Cadastro dos Tributos por Documentos Fiscais (Nota Fiscal de Serviço/Mercadorias)** | Sim |  |  |
| **T013AQ Local de coleta/Entrega - Modelos 08, 8B, 09, 10, 11, 26 e 27** |  |  |  |
| **T013AR Complemento do Documento Fiscal - Modelos 21 e 22** | Sim |  |  |
| **T013AS Complemento do Documento Fiscal - Operações com ICMS-ST recolhido para UF diversa do destinatário do documento fiscal (Modelos 55)** |  |  |  |
| **T013AT Complemento do Documento Fiscal - Documentos Cancelados (Modelos 02, 13, 14, 15 E 16)** | Sim |  |  |
| **T013AU Complemento do Documento Fiscal - Modelo 09** | Sim |  |  |
| **T013AV Complemento do Documento Fiscal - Modelo 10** | Sim |  |  |
| **T013AX Cadastro de Processos Referenciados por Documento Fiscal** | Sim |  |  |
| **T013AW Complemento do Documento Fiscal – Modelos 08, 8B, 09, 10, 11, 26 e 27** |  |  |  |
| **T013AY Complemento do Documento Fiscal - Documentos Informados (Modelos 13, 14, 15 E 16)** | Sim |  |  |
| **T013AZ Aquisição de Cana de Açúcar (Modelo 55)** |  |  |  |
| **T013BA Fornecimento Diário de Cana (Modelo 55)** |  |  |  |
| **T013BB Deduções - Cana (Modelo 55)** |  |  |  |
| **T013BC Autorização de Créditos Acumulados de ICMS** |  |  |  |
| **T015 Cadastro dos Itens dos Documentos Fiscais** | Sim |  |  |
| **T015AA Cadastro de Operações com Medicamentos - Complemento do Item Modelos 01 e 55** | Sim |  |  |
| **T015AB Complemento do Item do Documento Fiscal - Modelos 06, 28 e 29** | Sim |  |  |
| **T015AC Cadastro de Operações com Arma de Fogo - Complemento do Item modelo 01** |  |  |  |
| **T015AD Cadastro de Operações com Veículos Novos - Complemento do Item modelos 01 e 55** |  |  |  |
| **T015AE Cadastro de Tributos por Item de Documento** | Sim |  |  |
| **T015AF Cadastro de Armazenamento de Combustíveis - Complemento do Item modelos 01 e 55** | Sim |  |  |
| **T015AG Ressarcimento de ICMS em operações com ST - Complemento do Item modelos 01 e 55** |  |  |  |
| **T015AH Complemento do item do Documento Fiscal - Modelo 21 e 22** | Sim |  |  |
| **T015AI Complemento do item do Documento Fiscal - Modelo 07** |  |  |  |
| **T020 Apuração e/ou Sub-Apuração do ICMS** | Sim |  |  |
| **T020AA Ajustes da Apuração do Tributo** | Sim |  |  |
| **T020AB Informações adicionais dos ajustes da Apuração - Processos referenciados ou Documentos de arrecadação** |  |  |  |
| **T020AC Informações adicionais dos ajustes da Apuração - Identificação dos documentos fiscais** | Sim |  |  |
| **T020AD Informações adicionais dos ajustes da Apuração - Valores declaratórios** | Sim |  |  |
| **T020AE Obrigações a recolher** | Sim |  |  |
| **T020AF Resumo por CFOP** | Sim |  |  |
| **T020AG Autorização de Créditos Acumulados de ICMS** |  |  |  |
| **T021 Apuração de ST** | Sim |  |  |
| **T021****AA Ajustes da Apuração do Tributo** | Sim |  |  |
| **T021AB Informações adicionais dos ajustes da Apuração - Processos referenciados ou Documentos de arrecadação** |  |  |  |
| **T021AC Informações adicionais dos ajustes da Apuração - Identificação dos documentos fiscais** | Sim |  |  |
| **T021AD Obrigações a recolher** | Sim |  |  |
| **T021AE Resumo por Estado + CFOP** |  |  |  |
| **T022 Apuração de IPI** | Sim |  |  |
| **T022AA Ajustes da Apuração do Tributo** | Sim |  |  |
| **T022AB Detalhamento do IPI por CFOP** |  |  |  |
| **T023 Crédito de Pis/Pasep/COFINS relativo ao período** |  |  |  |
| **T023AA Detalhamento da base de cálculo do crédito apurado no período** |  |  |  |
| **T023AB Ajustes da Apuração do credito do PIS/COFINS** |  |  |  |
| **T023AC Detalhamento dos ajustes de crédito de PIS/COFINS apurado** |  |  |  |
| **T024 Consolidação da Contribuição do período** | Sim |  |  |
| **T024AA Detalhamento por código de receita** |  |  |  |
| **T024AB Detalhamento da contribuição do período** | Sim |  |  |
| **T024AC Composição da Base de Cálculo** |  |  |  |
| **T024AD Ajustes da Contribuição Apurada** |  |  |  |
| **T024AE Detalhamento dos ajustes da Contribuição Apurada** |  |  |  |
| **T024AF Informações adicionais de diferimento** | Sim |  |  |
| **T030 Demais documentos e operações geradoras de contribuições e créditos não vinculados ao documento fiscal** | Sim |  |  |
| **T030AA Processos referenciados** |  |  |  |
| **T031 Bens incorporados ao Ativo Imobilizado - Operações geradoras de créditos com base nos encargos de depreciação e amortização** | Sim |  |  |
| **T031AA Processos referenciados** |  |  |  |
| **T032 Bens incorporados ao Ativo Imobilizado - Operações geradoras de créditos com base no valor de aquisição/contribuição** | Sim |  |  |
| **T032AA Processos referenciados** |  |  |  |
| **T033 Operações da atividade imobiliária - Unidade imobiliária vendida** | Sim |  |  |
| **T033AA Processos referenciados** |  |  |  |
| **T033AB Operações da atividade imobiliária - custo incorrido da unidade imobiliária** | Sim |  |  |
| **T033AC Operações da atividade imobiliária - custo orçado da unidade imobiliária vendida** | Sim |  |  |
| **T034 Contribuição retida na fonte** | Sim |  |  |
| **T035 Deduções diversas** | Sim |  |  |
| **T036 Créditos decorrentes de eventos de incorporação, fusão e cisão** |  |  |  |
| **T037 Credito presumido sobre estoque de abertura** |  |  |  |
| **T045 Período de Apuração ICMS/IPI** | Sim |  |  |
| **T045AA Estoque Escriturado** | Sim |  |  |
| **T045AB Outras Movimentações Internas Entre Mercadorias** | Sim |  |  |
| **T045AC Itens Produzidos** | Sim |  |  |
| **T045AD Insumos Consumidos** | Sim |  |  |
| **T045AE Industrialização Efetuada por Terceiros** | Sim |  |  |
| **T045AF** **Industrialização Em Terceiros - Insumos Consumidos** | Sim |  |  |
| **T046** **Produto x Insumos** | Sim |  |  |
| **T046 AAInsumos** | Sim |  |  |
| **T050 Credito de ICMS sobre Ativo Permanente** | Sim |  |  |
| **T050AA Movimentação do bem ou componente do ativo imobilizado** | Sim |  |  |
| **T050AB Outros créditos CIAP** |  |  |  |
| **T050AC Identificação dos documentos fiscais que acobertaram a entrada/saída do bem ou componente CIAP** | Sim |  |  |
| **T050AD Identificação dos itens dos documentos fiscais que acobertaram a entrada/saída do bem ou componente CIAP** | Sim |  |  |
| **T051** **Apuração do Difal/Fecp** | Sim |  |  |
| **T051AA** **Ajuste de Apuração Difal/Fecp** | Sim |  |  |
| **T051AB** **Info. Adicionais Ajuste Apuração** | Sim |  |  |
| **T051AC** **Info. Adicionais Ajuste Documento** | Sim |  |  |
| **T051AD Obrigações de DIFAL/FECP a Recolher** |  |  |  |
| **T060 Contribuição do PIS/PASEP ou da COFINS diferida em períodos anteriores - Valores a pagar no período** | Sim |  |  |
| **T061 PIS/PASEP – Folha de salários** | Sim |  |  |
| **T062 Detalhamento das receitas isentas, não alcançadas pela incidência da contribuição, sujeitas a alíquota zero ou vendas com suspensão - PIS/PASEP ou COFINS** |  |  |  |
| **T065 Controle dos créditos fiscais - PIS/PASEP e/ou COFINS** | Sim |  |  |
| **T065AA Apuração de credito extemporâneo - Documentos e operações de período anteriores - PIS/PASEP e/ou COFINS** | Sim |  |  |
| **T065AB Apuração de credito extemporâneo - Itens do Documento e operações de período anteriores - PIS/PASEP e/ou COFINS** | Sim |  |  |
| **T066 Informações de Exportação - Complemento do documento** | Sim |  |  |
| **T066AA Informações de Exportação - Itens dos documentos de exportação** | Sim |  |  |
| **T066AB Informações de Exportação - Exportações indiretas - Mercadorias de terceiros** | Sim |  |  |
| **T069 Movimentação diária de combustíveis - Informações complementares do item do documento fiscal** | Sim |  |  |
| **T069AA Movimentação diária de combustíveis por tanque** | Sim |  |  |
| **T069AB Volume de vendas** | Sim |  |  |
| **T070 Bombas** | Sim |  |  |
| **T070AA Lacres das bombas** | Sim |  |  |
| **T070AB Bicos das bombas** | Sim |  |  |
| **T071 Controle de valores retidos na fonte - PIS/PASEP e/ou COFINS** | Sim |  |  |
| **T072 Informações sobre valores agregados** | Sim |  |  |
| **T073 Totais de operações com cartão de credito/debito** | Sim |  |  |
| **T075 Incorporação imobiliária** | Sim |  |  |
| **T075AA Processos referenciados** |  |  |  |
| **T076 Demonstrativo de credito sobre o transporte aéreo – DCTA** |  |  |  |
| **T078 Movimento ECF** | Sim |  |  |
| **T078AA Cadastro da Redução Z (Códigos 02, 2D, 2E, 13, 14, 15 e 16)** | Sim |  |  |
| **T078AB** **Totalizadores parciais da redução Z (Códigos 02 e 2D)** | Sim |  |  |
| **T078AC Cadastro dos Itens do Movimento Diário** | Sim |  |  |
| **T078AD Cadastro do Documento Fiscal Emitido por ECF** | Sim |  |  |
| **T078AE Cadastro dos Itens dos Documentos Fiscais Emitidos por ECF** | Sim |  |  |
| **T078AF Cadastro dos Tributos dos Itens dos Documentos Fiscais Emitidos por ECF** | Sim |  |  |
| **T078AG Processos referenciados** |  |  |  |
| **T078AH Resumo diário do ECF por PIS/PASEP** | Sim |  |  |
| **T078AI Resumo diário do ECF por COFINS** | Sim |  |  |
| **T078AJ Resumo diário do ECF por ICMS** | Sim |  |  |
| **T078AK Complemento dos Documentos Informados (Códigos 13, 14, 15 e 16 e 2E)** | Sim |  |  |
| **T078AL Registro Analítico do Movimento Diário (Códigos 13, 14, 15 e 16 e 2E)** |  |  |  |
| **T079 Inventario** | Sim |  |  |
| **T079AA Itens do Inventario** | Sim |  |  |
| **T079AB Informação complementar do Inventário** |  |  |  |
| **T081 Controle de Produção diária da Usina** | Sim |  |  |
| **T082 Contribuição Previdenciária sobre a receita bruta** | Sim |  |  |
| **T082AA Complemento da contribuição - Detalhamento da Apuração da Contribuição** |  |  |  |
| **T082AB Processos referenciados** |  |  |  |
| **T083 Consolidação da Contribuição Previdenciária sobre a receita bruta** | Sim |  |  |
| **T083AA Ajustes da Contribuição Previdenciária sobre a receita bruta** | Sim |  |  |
| **T084 Consolidação das operações da Pessoa Jurídica submetida ao regime de tributação com base no Lucro Presumido** | Sim |  |  |
| **T084AA Consolidação das operações da Pessoa Jurídica submetida ao regime de tributação com base no Lucro Presumido** | Sim |  |  |
| **T084AB Processos Referenciados** |  |  |  |
| **T085 Composição da receita escriturada no período - Detalhamento da receita recebida pelo Regime de caixa** | Sim |  |  |
| **T086 Identificação da Pessoa Jurídica/Estabelecimento** | Sim |  |  |
| **T086AA Consolidação das Operações do período** | Sim |  |  |
| **T086AB Processos referenciados** | Sim |  |  |
| **T086AC Composição das Receitas, Deduções e/ou exclusões do período** | Sim |  |  |
| **T086AD Processos referenciados** | Sim |  |  |
| **T086AE Complemento das operações - Detalhamento das Receitas, Deduções e/ou Exclusões do Período** | Sim |  |  |
| **T086AF Processos referenciados** |  |  |  |
| **T087 Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário** |  |  | Sim |
| **T087AA Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)** |  |  | Sim |
| **T087AB Mapeamento Referencial do Saldo Final** |  |  | Sim |
| **T087AC Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento** |  |  | Sim |
| **T087AD Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento** |  |  | Sim |
| **T088 Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário** |  |  | Sim |
| **T088AA Balanço Patrimonial** |  |  |  |
| **T088AB Método de Avaliação de Estoques** |  |  | Sim |
| **T088AC Informativo da Composição de Custos** |  |  | Sim |
| **T088AD Demonstração do Resultado do Exercício** |  |  |  |
| **T089 Identificação da Conta na Parte B do e-Lalur e do e-Lacs** |  |  | Sim |
| **T090 Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real** |  |  | Sim |
| **T090AA Lançamentos da Parte A do e-Lalur** |  |  | Sim |
| **T090AB Conta da Parte B do e-Lalur** |  |  | Sim |
| **T090AC Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lalur** |  |  | Sim |
| **T090AD Números dos Lançamentos Relacionados à Conta Contábil** |  |  | Sim |
| **T090AE Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento** |  |  | Sim |
| **T090AF Lançamento na Conta da Parte B do e-Lalur e do e-Lacs sem Reflexo na Parte A** |  |  | Sim |
| **T090AG Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento** |  |  | Sim |
| **T090AH Controle de Saldos das Contas da Parte B do e-Lalur e do e-Lacs** |  |  |  |
| **T090AI Lançamentos da Parte A do e-Lacs** |  |  | Sim |
| **T090AJ Conta da Parte B do e-Lacs** |  |  | Sim |
| **T090AK Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lacs** |  |  | Sim |
| **T090AL Números dos Lançamentos Relacionados à Conta Contábil** |  |  | Sim |
| **T090AM Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento** |  |  | Sim |
| **T091 Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real** |  |  | Sim |
| **T091AA Registros Genéricos - Bloco N** |  |  | Sim |
| **T091AB Informações da Base de Cálculo dos Incentivos Fiscais** |  |  |  |
| **T092 Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido** |  |  | Sim |
| **T092AA Balanço Patrimonial** |  |  |  |
| **T092AB Registros Genéricos - Bloco P** |  |  | Sim |
| **T092AC Demonstrativo do Resultado do Exercício** |  |  |  |
| **T093 Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Arbitrado** |  |  | Sim |
| **T093AA Registros Genéricos - Bloco T** |  |  | Sim |
| **T094 Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas** |  |  | Sim |
| **T094AA Balanço Patrimonial** |  |  |  |
| **T094AB Registros Genéricos - Bloco U** |  |  | Sim |
| **T094AC Demonstração do Resultado** |  |  |  |
| **T095 Atividades Incentivadas – PJ em Geral** |  |  |  |
| **T096 Registros Genéricos - Bloco X** |  |  | Sim |
| **T102 Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior** |  |  | Sim |
| **T103 Pagamentos/Remessas Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior** |  |  | Sim |
| **T104 Pagamentos/Recebimentos do Exterior ou de Não Residentes** |  |  |  |
| **T105 Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica** |  |  | Sim |
| **T106 Vendas a Comercial Exportadora com Fim Específico de Exportação** |  |  | Sim |
| **T107 Detalhamento das Exportações da Comercial Exportadora** |  |  | Sim |
| **T108 Demonstrativo do Imposto de Renda, CSLL e Contribuição Previdenciária Retidos na Fonte** |  |  | Sim |
| **T109 Doações a Campanhas Eleitorais** |  |  |  |
| **T110 Ativos no Exterior** |  |  |  |
| **T111 Identificação de Sócios ou Titular** |  |  | Sim |
| **T112 Rendimentos de Dirigentes, Conselheiros, Sócios ou Titular** |  |  |  |
| **T113 Rendimentos de Dirigentes e Conselheiros – Imunes ou Isentas** |  |  | Sim |
| **T114 Participação Permanente em Coligadas ou Controladas** |  |  | Sim |
| **T115 Fundos/Clubes de Investimento** |  |  |  |
| **T116 Participações em Consórcios de Empresas** |  |  |  |
| **T116AA Participantes do Consórcio** |  |  |  |
| **T117 Dados de Sucessoras** |  |  |  |
| **T118 Outras Informações** |  |  | Sim |
| **T119 Outras Informações (Lucro Presumido)** |  |  | Sim |
| **T120 Mês das Informações de Optantes pelo Refis (Lucros Real, Presumido e Arbitrado)** |  |  |  |
| **T120AA Informações de Optantes pelo Refis (Lucros Real, Presumido e Arbitrado)** |  |  |  |
| **T121 Informações de Optantes pelo Refis – Imunes ou Isentas** |  |  |  |
| **T122 Informações de Optantes pelo PAES** |  |  | Sim |
| **T123 Outras Informações** |  |  |  |
| **T124 Lançamento Contábil** |  | Sim | Sim |
| **T124AA Partidas do Lançamento** |  | Sim | Sim |
| **T125 Tabela de Histórico Padronizado** |  | Sim | Sim |
| **T126 Demonstrativo das Diferenças na Adoção Inicial** |  |  | Sim |
| **T127 Abertura do Arquivo Digital ECF e Parâmetros Complementares** |  |  | Sim |

***Links úteis***

* [Projeto TAF (Totvs Automação Fiscal) Totvs](http://tdn.totvs.com/x/tYvuDQ)
* [Gerador de Saídas](http://tdn.totvs.com.br/pages/releaseview.action?pageId=161351571)
* [Como gerar documentação do layout TAF](http://tdn.totvs.com/pages/viewpage.action?pageId=271650461)
