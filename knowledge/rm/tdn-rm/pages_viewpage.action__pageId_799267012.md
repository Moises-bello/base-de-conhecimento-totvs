---
content_hash: ba7caf226811b5ea433f591d9f8b9deb0025bc31fe682c7405aacb7065727dee
fetched_at: '2026-06-29T00:11:42.846718+00:00'
page_id: '799267012'
product: rm
source: tdn-rm
title: DES - Belo Horizonte - Registro R - Serviços Tomados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=799267012
version: 10
---

Serão selecionados todos os Lançamentos de Entrada da Filial selecionada na tela da rotina que atendam aos seguintes critérios:[

1. Lançamentos cuja data de entrada (conforme o parâmetro especificado no item 1) estejam no período informado na tela da rotina;
2. Lançamentos com status "Normal";
3. Lançamentos que possuam em uma de suas parcelas pelo menos um item tributado pelo ISS (Anexo "Dados Fiscais" no Cadastro de Produto);
4. Lançamentos cuja forma de tributação da natureza de operação seja "Sem ICMS" e "Sem IPI" ou cujo CFOP associado seja "1.933" ou "2.933".

|  |  |  |  |
| --- | --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** | **Observação** |
| 01 | Tipo do Registro | Identificação do registro. Caractere fixo "R". |  |
| 02 | Data de pagamento ou recolhimento do crédito. | Se o campo "Órgão Público" for marcado no momento da geração da rotina e  o sistema esteja parametrizado para buscar os Lançamentos de Entrada pela Data de Baixa, este campo será preenchido com a "Data da Baixa". Caso contrário será preenchido com a "Data do Vencimento". Se o campo "Órgão Público" estiver desmarcado será preenchido com a "Data de Execução do Serviço". |  |
| 03 | Data de emissão | Data de emissão informada no Lançamento Fiscal. |  |
| 04 | Modelo de Documento | "Modelo ISS" associado ao Tipo de Documento (Espécie) nos parâmetros do TOTVS Gestão Fiscal (Processo 03.02.03 – Apur. ISS por Filial, Etapa 1 – Modelo ISS). Não existindo a relação, preencher com o valor do campo "Código Modelo Documento" do Tipo de Documento associado ao Lançamento Fiscal. |  |
| 05 | Série do documento | Série informada no Lançamento Fiscal. |  |
| 06 | Subsérie do documento | Subsérie informada no Lançamento Fiscal. |  |
| 07 | Situação especial de responsabilidade | Regra A informação da Situação especial de responsabilidade seguirá as seguintes considerações: Se o Regime do ISS do Cliente/Fornecedor for "Construção Civil"  Então a Situação de Responsabilidade é "3 Construção Civil";  Senão Se o campo "Valor Bruto" for igual ao campo "Valor do Serviço" e Tem ISS no Lançamento ou no Item  Então a Situação de Responsabilidade é "1 Exclusivamente Prestação de Serviços";  Senão "2 Prestação de Serviços c/ Dedução";  Se Não existir Tributo ISS no Item ou Lançamento      Então Situação de Responsabilidade do ISSQN é "07-Não Incidência"; |  |
| 08 | Motivo de não retenção | Regra A informação do Motivo de não retenção seguirá as seguintes considerações:  Se o lançamento for com uma CFOP Origem/Destino = Exterior e o Município de Prestação do Serviço não for Belo Horizonte  Então o Motivo da Não Retenção é "17 Exportação";    Se o Porte da Empresa for do Cliente/Fornecedor for "MEI – Micro Empreendedor Individual"  Então o Motivo da Não Retenção é "14 MEI – Microempreendedor Individual";    Senão Se o Regime do ISS do Cliente/Fornecedor for:  "Imune"  Então o Motivo da Não Retenção é "2 Imunidade Tributária";  “Estimativa"  Então o Motivo da Não Retenção é "3 Regime de Estimativa em BH";  "Sociedade Profissional"  Então o Motivo da Não Retenção é "6 SPL - Sociedade de Profissionais Liberais";  "Incentivo à Cultura"  Então o Motivo da Não Retenção é "7 Incentivador Cultural em BH";  “Profissional Autônomo”  Então o Motivo da Não Retenção é“09-Profissional Autônomo com registro na PBH";    Senão Se o Tipo de Recolhimento do ISS for: "Isento"  Então o Motivo da Não Retenção é "4 Isenta do ISSQN em BH";  "Depósito Judicial"  Então o Motivo da Não Retenção é "8 Exigibilidade do ISSQN Suspensa por Decisão Judicial";  "Retido na Fonte" ou "Retido na Fonte Deduzido"  Então o Motivo da Não Retenção é "16 ISSQN Retido";    Se o Município de Prestação do Serviço não for Belo Horizonte  Se ISS Isento  Então o Motivo da Não Retenção é “1 Não Retido”;  Se Não Tem ISS  Então o Motivo da Não Retenção é “2 Imunidade Tributária”  Senão  Então o Motivo da Não Retenção é “5 Tributação fora de BH”;    Se Não existir Tributo ISS no item ou lançamento  Então Regime de Tributação é "10-Não Incidência";  Senão "1 Não retido".    **Não aderência:** "12 Cartórios" "13 PROEMP" "15 Desobrigado legalmente" |  |
| 09 | Local da incidência | Município da Prestação do Serviço informado no Lançamento Fiscal ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. |  |
| 10 | Tipo de recolhimento do ISSQN | Se o Tipo de Recolhimento do ISS for "Retido na Fonte" ou "Retido na Fonte Deduzido" então preencher com "1". Caso contrário preencher com "2". |  |
| 11 | Número do documento | Número do Documento Inicial informado no Lançamento Fiscal. Se o documento for uma NFS-e o número do documento deve ser preenchido com o ano (4 dígitos) + o número da nota. |  |
| 12 | Valor bruto do documento | Este campo é preenchido com o somatório dos valores (quantidade x preço) de todos os itens do Lançamento Fiscal, considerando todas as suas parcelas. Para lançamentos com status "Cancelado", é preenchido com o valor zero. |  |
| 13 | Valor do serviço | Se a Filial estiver parametrizada para usar município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS dos Itens do Lançamento Fiscal, considerando somente os itens cujo município informado é igual ao município da Filial. Caso não haja nenhum serviço tributado no município, deve ser considerado o valor total dos serviços. Se a Filial estiver parametrizada para não usar o município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS do lançamento fiscal. Para lançamentos com status "Cancelado", é preenchido com o valor zero. |  |
| 14 | Alíquota | Alíquota informada para o tributo ISS no Item ou no lançamento, observando a se a Filial estiver parametrizada para utilizar município por item. |  |
| 15 | Simples Nacional | Se o campo "Optante pelo Simples" estiver marcado na aba Dados Fiscais. | Outros Dados do Cadastro de Cliente/Fornecedor, recebe valor "1 – Optante ME/EPP"; Senão, Se o campo "Porte da Empresa" estiver preenchido com a opção "MEI – Micro Empreendedor Individual" recebe "3 – Optante MEI"; Senão recebe "2 – Não optante". |
| 16 | Inscrição Municipal | Preencher esses campos com os dados do Cliente/Fornecedor associado ao Lançamento Fiscal. | O campo "Inscrição Municipal" só deve ser preenchido se o Cliente/Fornecedor for do mesmo município da Filial declarante. Nos demais casos, deixar em branco. |
| 17 | CNPJ | Preencher esses campos com os dados do Cliente/Fornecedor associado ao Lançamento Fiscal. | Se não houver deixar em branco. |
| 18 | CPF | Preencher esses campos com os dados do Cliente/Fornecedor associado ao Lançamento Fiscal. | Se não houver deixar em branco. |
| 19 | Nome do prestador | Nome ou razão social do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 20 | Logradouro do prestador | Logradouro do endereço do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 21 | Número do imóvel do prestador | Número do imóvel do endereço do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 22 | Complemento do prestador | Complemento do endereço do Cliente/Fornecedor associado ao Lançamento Fiscal. | Obrigatório no caso de ausência do número do imóvel. |
| 23 | Bairro do prestador | Nome do bairro do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 24 | Cidade do prestador | Código do IBGE da cidade do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 25 | País do prestador | Código do País do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 26 | CEP do prestador | CEP do endereço do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 27 | Telefone do prestador | Número do telefone do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 28 | E-mail do prestador | E-mail do prestador do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 29 | Inscrição Municipal do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 30 | CNPJ do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 31 | CPF do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 32 | Nome do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 33 | Logradouro do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 34 | Número do imóvel do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 35 | Complemento do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 36 | Bairro do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 37 | Cidade do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 38 | País do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 39 | CEP do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 40 | Telefone do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 41 | E-mail do tomador | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 42 | Local da prestação dos serviços | Município da Prestação do Serviço informado no Lançamento Fiscal ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. |  |
| 43 | País da prestação dos serviços | O campo País deve ser preenchido com o código do país associado ao Estado do Município da Prestação do Serviço de acordo com a tabela informada pelo usuário na tela de geração da rotina (BACEN). |  |
| 44 | Descrição do evento | Não aderência |  |
| 45 | Data do evento | Não aderência |  |
