---
content_hash: 59f5b4c414c2cd3ef04d5cb3df032031ddd5339a81f003aa8c450293146919f2
fetched_at: '2026-06-29T00:11:42.936093+00:00'
page_id: '799267135'
product: rm
source: tdn-rm
title: DES - Belo Horizonte - Registro E - Serviços Prestados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=799267135
version: 8
---

Serão selecionados todos os Lançamentos Fiscais de Saída da Filial selecionada na tela da rotina que atendem os seguintes critérios:

1. Lançamentos cuja data de saída ou de cancelamento (conforme o parâmetro especificado no item 1) esteja no período informado na tela da rotina;
2. Lançamentos com status "Normal" ou "Cancelado";
3. Lançamentos associados à AIDF cujo órgão responsável seja "Prefeitura" ou "Ambos".

|  |  |  |  |
| --- | --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** | **Observação** |
| 01 | Tipo de Registro | Identificação do registro. Caractere fixo "E". |  |
| 02 | Data de Emissão | Data de emissão informada no Lançamento Fiscal. |  |
| 03 | Código da tributação no município | Código do Serviço no Município informado no Lançamento Fiscal, ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. |  |
| 04 | Código subitem da lista de serviço | Campo "Código do Serviço Federal" informado no Anexo "Dados Fiscais do Produto" do Cadastro do Produtos/Serviços. |  |
| 05 | Modelo de documento | "Modelo ISS" associado ao Tipo de Documento (Espécie) nos parâmetros do TOTVS Gestão Fiscal (Processo 03.02.03 – Apur. ISS por Filial, Etapa 1 – Modelo ISS). Não existindo a relação, preencher com o valor do campo "Código Modelo Documento" do Tipo de Documento associado ao Lançamento Fiscal. |  |
| 06 | Série do documento | Série informada no Lançamento Fiscal. |  |
| 07 | Subsérie do documento | Subsérie informada no Lançamento Fiscal. |  |
| 08 | Tipo de Negócio | Regra A informação do Tipo de Negócio seguirá as seguintes considerações:  Se o status do Lançamento Fiscal for **"Cancelado"** Então o Tipo do Negócio é**"0 Cancelada";**  Se a AIDF associada ao Lançamento Fiscal for autorizada por "Prefeitura", fazer as seguintes considerações:  Se o campo **"Valor Bruto"** for igual ao campo **"Valor do Serviço"**                 Então o Tipo do Negócio é **"1 Exclusivamente Prestação de Serviços"**                 Senão **"2 Prestação de Serviços c/ Dedução";**  Se a AIDF associada ao Lançamento Fiscal for autorizada por "Ambos", fazer as seguintes considerações:  Se o Tipo de Cliente do Lançamento Fiscal for**"Empresa"**         Então o Tipo do Negócio é **"7 Devolução/Simples Remessa/Entrada";**  Se não existir item tributado pelo ISS informado no Lançamento Fiscal      Então o Tipo do Negócio é **"5 Vendas de Mercadorias/Transporte Intermunicipal";**  Se existir item tributado pelo ISS informado no Lançamento Fiscal = 1        Então o Tipo do Negócio é **"6 Prestação de Serviços c/ Venda de Mercadorias/Transporte Intermunicipal";**  Se Não existir o Tributo ISS no Lançamento ou no Item       Então Tipo de Negócio é **“08 Não Inicidência”** |  |
| 09 | Exigibilidade do ISSQN | Regra A informação da Exigibilidade do**ISSQN** seguirá as seguintes considerações:  Se o status do Lançamento Fiscal for **"Cancelado"**         Então o Tipo do Negócio é **"00 Cancelada";**  Se o lançamento for de exportação (CFOP para exterior) e o Município de Prestação do Serviço**não** for Belo Horizonte         Então Exigibilidade do ISSQN é**"02 Exportação";**  Se o Município de Prestação do Serviço for Belo Horizonte, fazer as seguintes considerações:  Se o Tipo de Recolhimento do ISS for **"Isento"**         Então Exigibilidade do ISSQN é**"04 Isenta do ISS em BH";**  Se o Tipo de Recolhimento do ISS for**"Depósito Judicial"**         Então Exigibilidade do ISSQN é **"05 Exigibilidade Suspensa por Decisão Judicial"**  Senão Exigibilidade do ISSQN é **"01 Exigível"**  Se a AIDF for autorizada por "Ambos" e não existir item tributado pelo ISS informado no Lançamento Fiscal         Então Exigibilidade do ISSQN é **"07 Vendas/Transporte Intermunicipal";**  Se Regime de ISS for IMUNE      Então Exigibilidade do ISSQN é **“03-Imunidade Tributaria”;**  Se Não existir Tributo ISS no Item ou Lançamento      Então Exigibilidade do ISSQN é **“06-Não Incidência”;** |  |
| 10 | Local da Incidência | Município da Prestação do Serviço informado no Lançamento Fiscal ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. |  |
| 11 | Regime especial da tributação | Regra A informação do Regime Especial de Tributação seguirá as seguintes considerações:  Se status do lançamento fiscal for**"Cancelado"**       Então o Regime de Tributação é **"0 Cancelada";**  Se a AIDF associada ao Lançamento Fiscal for autorizada por "Ambos" e não existir item tributado pelo ISS informado no Lançamento Fiscal        Então o Regime de Tributação é**"11 Vendas/Transporte Intermunicipal";**  Se o **"Regime ISS"** da Filial for:  **"Estimativa"**            Então o Regime de Tributação é**"2 Regime de Estimativa";** **"Sociedade Profissional"**            Então o Regime de Tributação é **"3 SPL - Sociedade de Profissionais Liberais";** **"Construção Civil"**            E não existir Tributo ISS no Item ou no Lançamento;   Então o Regime de Tributação é**“12-Não Incidência”**    Senão o Regime de Tributação é **"6 Construção Civil";**  **"Microempresa"**              Então o Regime de Tributação é **"9 ME ou EPP optante pelo Simples Nacional";**    Senão o Regime de Tributação é**"1 Regra Geral";**  Se Não existir Tributo ISS no Item ou Lançamento      Então Regime de Tributação é **“12-Não Incidência”;,**  Não aderência aos tipos: • 4 Cooperativa, • 5 Não disponível na DES 3.0, • 7 Propaganda e Publicidade/Intermediação, • 8 Agenciamento de Turismo/Administração de Fundos e • 10 MEI - Microeempreendedor Individual |  |
| 12 | Tipo de recolhimento do ISSQN | Se o Tipo de Recolhimento do ISS for "Retido na Fonte" ou "Retido na Fonte Deduzido" então preencher com "1". Caso contrário preencher com "2". |  |
| 13 | Número do documento | Número do Documento Inicial informado no Lançamento Fiscal. Se o documento for uma NFS-e o número do documento deve ser preenchido com o ano (4 dígitos) + o número da nota. |  |
| 14 | Número final | Número do Documento Final informado no Lançamento Fiscal. Se vazio, repetir o número inicial. Se o documento for uma NFS-e o número do documento deve ser preenchido com o ano (4 dígitos) + o número da nota. |  |
| 15 | Valor bruto | Este campo é preenchido com o somatório dos valores (quantidade x preço) de todos os itens do Lançamento Fiscal, considerando todas as suas parcelas. Para lançamentos com status "Cancelado", é preenchido com o valor zero. |  |
| 16 | Valor do serviço | Se a Filial estiver parametrizada para usar município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS dos Itens do Lançamento Fiscal, considerando somente os itens cujo município informado é igual ao município da Filial. Caso não haja nenhum serviço tributado no município, deve ser considerado o valor total dos serviços. Se a Filial estiver parametrizada para não usar o município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS do lançamento fiscal. Para lançamentos com status "Cancelado", é preenchido com o valor zero. |  |
| 17 | Alíquota | Alíquota informada para o tributo ISS no Item ou no lançamento, observando a se a Filial estiver parametrizada para utilizar município por item. |  |
| 18 | Situação do documento | Se o Status do Lançamento Fiscal for "Cancelado", então preencher com "**2 - Cancelado**", senão preencher com "**1 – Normal**". |  |
| 19 | Simples Nacional | Se o campo "Optante Regime Simplificado" estiver marcado no Anexo Dados Fiscais do Cadastro da Filial, receberá valor "**1 – Optante****ME/EPP**", senão recebe "**2 – Não optante**". |  |
| 20 | Inscrição Municipal do tomador | Preencher com os dados do Cliente/Fornecedor associado ao Lançamento Fiscal. O campo Cidade deve ser preenchido com o código do município conforme a tabela associada pelo usuário na tela de geração da rotina (IBGE). O campo País deve ser preenchido com o código do país associado ao Estado do Município conforme a tabela informada pelo usuário na tela de geração da rotina (BACEN). | O campo "Inscrição Municipal" só deve ser preenchido se o Cliente/Fornecedor for do mesmo município da Filial declarante. Nos demais casos, deixar em branco. |
| 21 | CNPJ do tomador | Preencher esses campos com os dados do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 22 | CPF do tomador | Preencher esses campos com os dados do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 23 | Nome do tomador | Nome ou razão social do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 24 | Logradouro do tomador | Logradouro do endereço do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 25 | Número do imóvel do tomador | Número do imóvel do endereço do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 26 | Complemento do tomador | Complemento do endereço do Cliente/Fornecedor associado ao Lançamento Fiscal. | Obrigatório no caso de ausência do número do imóvel. |
| 27 | Bairro do tomador | Nome do bairro do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 28 | Cidade do tomador | Código do IBGE da cidade do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 29 | País do tomador | Código do País do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 30 | CEP do tomador | CEP do endereço do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 31 | Telefone do tomador | Número do telefone do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 32 | E-mail do tomador | E-mail do prestador do Cliente/Fornecedor associado ao Lançamento Fiscal. |  |
| 33 | Inscrição Municipal do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 34 | CNPJ do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 35 | CPF do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 36 | Nome do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 37 | Logradouro do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 38 | Número do imóvel do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 39 | Complemento do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 40 | Bairro do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 41 | Cidade do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 42 | País do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 43 | CEP do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 44 | Telefone do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 45 | E-mail do terceiro vinculado/intermediário | Não aderência do Produto. Os campos serão gerados vazios. |  |
| 46 | Local de prestação | Município da Prestação do Serviço informado no Lançamento Fiscal ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. |  |
| 47 | País da prestação dos serviços | O campo País deve ser preenchido com o código do país associado ao Estado do Município da Prestação do Serviço conforme a tabela informada pelo usuário na tela de geração da rotina (BACEN). |  |
| 48 | Descrição do evento | Não aderência. |  |
| 49 | Data do evento | Não aderência. |  |
| 50 | Dada de competência | Data de Execução do Serviço, no formato MMAAAA. |  |
| 51 | Data de cancelamento | Se o Status do Lançamento Fiscal é "Cancelado", recebe a Data do Cancelamento. |  |
| 52 | Motivo de cancelamento | Este campo será preenchido com o primeiro caractere do "Motivo do Cancelamento" (aba Outros Dados). | Outros). Conforme Layout da rotina, os valores válidos são: 1 – Erro na emissão; 2 – Serviço não prestado; 4 – Duplicidade da nota; 9 – Outros Motivos. Caso o Motivo do Cancelamento se inicie com valores diferentes, este campo será preenchido com "9". |
| 53 | Outro Motivo de Cancelamento | Se o primeiro caractere do "Motivo do Cancelamento" for "9", receberá o restante da informação inserida no campo. |  |
| 54 | Número da nota substituidora | Este campo receberá o Número do Lançamento Fiscal substituto, informado na aba "Referências". | "Lançamentos Fiscais" do Lançamento Fiscal Cancelado. |
