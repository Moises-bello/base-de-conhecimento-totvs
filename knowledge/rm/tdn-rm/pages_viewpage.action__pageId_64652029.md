---
content_hash: 55b88a23d981f0077073dd34fd8347b935d410bb57f6bce11a6d698f6eb58e39
fetched_at: '2026-06-29T00:11:11.286232+00:00'
page_id: '64652029'
product: rm
source: tdn-rm
title: RMFIS00005_DES BH - Arquivo Eletrônico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=64652029
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:** 11.52 |
| **Processo** | **:** | DES BH |
| **Subprocesso** | **:** | Mapeamento de campos |
| **Data da publicação** | **:** | 28/06/2013 |

# **Introdução**

O objetivo deste documento é oferecer uma visão geral a respeito da **Declaração Eletrônica de Serviços** – DES e os processos necessários no sistema de Gestão Fiscal para geração do arquivo para posterior importação no programa da Prefeitura.

Glossário de termos técnicos e siglas:

**DES** - Declaração Eletrônica de Serviços.

**ISSQN** - Imposto sobre Serviços de Qualquer Natureza.

**NFS-e** - Nota Fiscal de Serviço Eletrônica.

**CTISS** - Código de Tributação do ISSQN.

**AIDF** – Autorização para Impressão de Documento Fiscal.

**IBGE** - Instituto Brasileiro de Geografia e Estatística

**BACEN** – Banco Central do Brasil

**Regras Gerais**

A **DES** foi instituída pela Prefeitura de Belo Horizonte através do Decreto 11.467/2003. A declaração deve ser entregue ao Fisco Municipal em periodicidade mensal, até o dia 20 (vinte) de cada mês. São obrigadas à apresentação da **DES** todas as pessoas jurídicas estabelecidas em Belo Horizonte, contribuintes ou não do **ISSQN**, isentas ou imunes, optantes pelo Simples Nacional, inclusive os órgãos, empresas e entidades da Administração Pública direta e indireta (municipal, estadual ou federal), empresas individuais, condomínios, associações, sindicatos e cartórios notariais e de registro, partidos e comitês políticos, ainda que não haja **ISSQN**próprio devido ou retido na fonte a recolher.

Devem ser informadas na **DES** as seguintes operações:

**a)** Todos os serviços prestados, tomados ou vinculados a terceiros**¹**, acobertados ou não por documentos fiscais e sujeitos à incidência do **ISSQN**, devido ou não ao Município de Belo Horizonte;

**b)** Os documentos fiscais cancelados, extraviados ou com o prazo de validade expirado;

**c)** A identificação de todos os documentos fiscais emitidos, autorizados pelo Fisco Municipal, em decorrência ou não de uma prestação de serviços.

---

1 - Entende-se por vinculado a terceiro o serviço contratado e pago por pessoa diversa de seu tomador, a quem incumbirá providenciar o pagamento do repasse ou reembolso dos valores despendidos pelo terceiro. (§ 2º do Art. 2º do Decreto 14.837/2012).

---

Todos os documentos fiscais emitidos, autorizados conjuntamente pelos Fiscos Municipal e Estadual, devem ser declarados na **DES**, informando-se o valor total da nota fiscal emitida e, se houver, o valor do serviço prestado.

As operações devem ser registradas:

**a)** No mês da emissão do documento fiscal, quando se tratar de serviços prestados;

**b)** No mês do efetivo recebimento quando se tratar de serviços prestados a órgãos e entidades da Administração Pública direta e indireta do Município, Estado e União;

**c)** No mês do pagamento ou crédito (o que primeiro ocorrer), quando se tratar de serviços tomados.

As guias de recolhimento do **ISSQN** deverão ser geradas e obtidas pelos contribuintes e responsáveis tributários por meio do programa de computador da **DES**.

**Geração do arquivo**

A geração da **DES** deve ser executada a partir do menu **Rotinas Legais | Rotinas Municipais | Apuração de ISS**; na tela apresentada devem ser informados o Estado e a rotina. O arquivo é gravado no diretório de arquivos temporários do **TOTVS** **Gestão** **Fiscal** (Processo 03.04.03) e, posteriormente, importado no sistema da **DES** disponibilizado pela Prefeitura Municipal de Belo Horizonte. 

 Para a geração do arquivo, devem ser informados a Filial, período e a versão do layout da **DES**. Se a Filial selecionada for órgão público, marcar a opção “Órgão Público”. O preenchimento deste campo impacta na geração do campo 2 “Data de pagamento ou reconhecimento do crédito” do Registro Tipo "R" - Serviços Tomados, como veremos adiante.

Devem ser informadas, também, as Classificações que serão utilizadas para codificação do Município e para o País.

**1. Seleção de Lançamentos**

A seleção dos Lançamentos Fiscais de Entrada e Saída será feita de acordo com os parâmetros informados no **TOTVS Gestão Fiscal** (Processo 03.02.03 - Etapa “Apur. ISS por Filial” - Datas Apuração do **ISS**). As opções são:

• Data de Emissão;

• Data de Entrada/Saída;

• Data de Pagamento/Vencimento.

Utilizando a opção **“Data de Pagamento/Vencimento”**, o sistema se comportará da seguinte forma:

**a)** Se existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos  
Fiscais cujo Lançamento Financeiro associado esteja baixado no período informado na tela da  
rotina (Data de Baixa);

**b)** Se não existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos  
Fiscais cuja Data de Vencimento (aba **“Dados Financeiros”**) esteja dentro do período informado na tela da rotina.

Essa parametrização deve ser feita para cada tipo de operação:

**• Lançamentos de Entrada;**  
**• Lançamentos de Saída – Entidade Privada (Cliente/Fornecedor);**  
**• Lançamentos de Saída – Entidade Pública (Cliente/Fornecedor).**

**Importante!**

Se a Filial estiver parametrizada para utilizar município por item, as informações de Alíquota, Tipo de Recolhimento, Base de Cálculo e Valor do Imposto serão preenchidos de acordo com os dados informados na aba “Outros Tributos” dos Itens do Lançamento Fiscal. Se a Filial for parametrizada para não usar o município por item, esses campos serão preenchidos de acordo com os dados informados na aba “Outros Tributos” do Lançamento Fiscal.

**2. Registros**

A geração dos Registros da **DES** será realizada de acordo com as regras seguintes:

**2.1. Registro Tipo "H" - Identificação**

| Pos | Campo | Origem dos Dados |
| --- | --- | --- |
| **01** | Tipo do Registro | Identificação do registro. Caractere fixo "H". |
| **02** | Inscrição Municipal | Cadastro da Filial (*GFILIAL.INSCMUN*). |
| **03** | CNPJ/CPF | Cadastro da Filial (*GFILIAL.CGC*). |
| **04** | Versão do Sistema | Informado pelo usuário na tela de geração da rotina. |

**2.2. Registro Tipo "E" - Serviços Prestados**

Serão selecionados todos os Lançamentos Fiscais de Saída da Filial selecionada na tela da rotina que atendem os seguintes critérios:

**a)** Lançamentos cuja data de saída ou de cancelamento (de acordo com o parâmetro especificado   
no item 1) esteja dentro do período informado na tela da rotina;

**b)** Lançamentos com status **“Normal”** ou “**Cancelado”**;

**c)** Lançamentos associados à **AIDF** cujo órgão responsável seja “**Prefeitura**” ou “**Ambos**”.

| Pos | Campo |  | Origem dos Dados |
| --- | --- | --- | --- |
| 01 | Tipo do Registro |  | Identificação do registro. Caractere fixo "E". |
| 02 | Data de Emissão |  | Data de emissão informada no Lançamento Fiscal (DLAF.DATAEMISSAO) |
| 03 | Código de Tributação no Município |  | Código do Serviço no Município informado no Lançamento Fiscal, ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. (DLAF.CODIGOSERVICO) | (DITEM.CODIGOSERVICO) |
| 04 | Código Subitem da Lista de Serviço |  | Campo **“Código do Serviço Federal”** informado no Anexo “Dados Fiscais do Produto” do Cadastro do Produtos/Serviços. (TPRDFISCAL.CODIGOSERVICOFEDERAL) |
| 05 | Modelo do Documento |  | **“Modelo ISS”** associado ao Tipo de Documento (Espécie) nos parâmetros do **TOTVS Gestão Fiscal** (Processo 03.02.03 – Apur. ISS por Filial, Etapa 1 – Modelo ISS). Não existindo a relação, preencher com o valor do campo **“Código** **Modelo Documento”** do Tipo de Documento associado ao  Lançamento Fiscal. |
| 06 | Série do Documento |  | Série informada no Lançamento Fiscal. (DLAF.SERIEDOC) |
| 07 | Subsérie do Documento |  | Subsérie informada no Lançamento Fiscal. (DLAF.SUBSERIE) |
| 08 | Tipo de Negócio |  | Ver Item 2.2.1. |
| 09 | Exigibilidade do ISSQN |  | Ver Item 2.2.2. |
| 10 | Local da Incidência |  | Município da Prestação do Serviço informado no Lançamento Fiscal ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. (DLAF.CODMUNICIPIOSERV/UFMUNICIPIOSERV) (DITEM.CODMUNICIPIOSERV/UFMUNICIPIOSERV) |
| 11 | Regime Especial de Tributação |  | Ver Item 2.2.3. |
| 12 | Tipo de Recolhimento do ISSQN |  | Se o Tipo de Recolhimento do ISS for **“Retido na Fonte”** ou **“Retido na** **Fonte Deduzido”** então preencher com “1”. Caso contrário preencher com “2”. |
| 13 | Número do Documento |  | Número do Documento Inicial informado no Lançamento Fiscal. Se o documento for uma NFS-e o número do documento deve ser preenchido com o ano (4 dígitos) + o número da nota. (DLAF.DOCINI). |
| 14 | Número Final |  | Número do Documento Final informado no Lançamento Fiscal. Se vazio, repetir o número inicial. Se o documento for uma NFS-e o número do documento deve ser preenchido com o ano (4 dígitos) + o número da nota. (DLAF.DOCFIM) |
| 15 | Valor Bruto |  | Este campo é preenchido com o somatório dos valores (quantidade x preço) de todos os itens do Lançamento Fiscal, considerando todas as suas parcelas. Para lançamentos com status “Cancelado”, é preenchido com o valor zero. |
| 16 | Valor do Serviço |  | Se a Filial estiver parametrizada para usar município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS dos Itens do Lançamento Fiscal, considerando somente os itens cujo município informado é igual ao município da Filial. Caso não haja nenhum serviço tributado no município, deve ser considerado o valor total dos serviços. Se a Filial estiver parametrizada para não usar o município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS do lançamento fiscal. Para lançamentos com status “Cancelado”, é preenchido com o valor zero. |
| 17 | Alíquota |  | Alíquota informada para o tributo ISS no Item ou no lançamento, observando a se a Filial estiver parametrizada para utilizar município por item. (DTRBLAF.ALIQTRB) | (DTRBITEM.ALIQTRB) |
| 18 | Situação do Documento |  | Se o Status do Lançamento Fiscal for **“Cancelado”**, então preencher com **“2 - Cancelado”**, senão preencher com **“1 – Normal”.** |
| 19 | Simples Nacional |  | Se o campo **“Optante Regime Simplificado”** estiver marcado no Anexo Dados Fiscais do Cadastro da Filial, receberá valor **“1 – Optante** **ME/EPP”**, senão recebe **“2 – Não optante”.** |
| 20 | Inscrição Municipal do tomador |  | Preencher com os dados do Cliente/Fornecedor associado ao Lançamento Fiscal. O campo Cidade deve ser preenchido com o código do município de acordo com a tabela associada pelo usuário na tela de geração da rotina (IBGE). O campo País deve ser preenchido com o código do país associado ao Estado do Município de acordo com a tabela informada pelo usuário na tela de geração da rotina (**BACEN**). |
| 21 | CNPJ do tomador |  |
| 22 | CPF do tomador |  |
| 23 | Nome do tomador |  |
| 24 | Logradouro do tomador |  |
| 25 | Número do imóvel do tomador |  |
| 26 | Complemento do tomador |  |
| 27 | Bairro do tomador |  |
| 28 | Cidade do tomador |  |
| 29 | País do tomador |  |
| 30 | CEP do tomador |  |
| 31 | Telefone do tomador |  |
| 32 | E-mail do tomador |  |
| 33 | Inscrição Municipal do terceiro vinculado/intermediário |  | **Não aderência do Produto. Os campos serão gerados vazios.** |
| 34 | CNPJ do terceiro vinculado/intermediário |  |
| 35 | CPF do terceiro vinculado/intermediário |  |
| 36 | Nome do terceiro vinculado/intermediário |  |
| 37 | Logradouro do terceiro vinculado/intermediário |  |
| 38 | Número do imóvel do terceiro vinculado/intermediário |  |
| 39 | Complemento do terceiro vinculado/intermediário |  |
| 40 | Bairro do terceiro vinculado/intermediário |  |
| 41 | Cidade do terceiro vinculado/intermediário |  |
| 42 | País do terceiro vinculado/intermediário |  |
| 43 | CEP do terceiro vinculado/intermediário |  |
| 44 | Telefone do terceiro vinculado/intermediário |  |
| 45 | E-mail do terceiro vinculado/intermediário |  |
| 46 | Local de prestação |  | Município da Prestação do Serviço informado no Lançamento Fiscal ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. (DLAF.CODMUNICIPIOSERV/UFMUNICIPIOSERV) (DITEM.CODMUNICIPIOSERV/UFMUNICIPIOSERV) |
| 47 | País da prestação dos serviços |  | O campo País deve ser preenchido com o código do país associado ao Estado do Município da Prestação do Serviço de acordo com a tabela informada pelo usuário na tela de geração da rotina (BACEN). |
| 48 | Descrição do evento |  | Não aderência |
| 49 | Data do evento |  | Não aderência |
| 50 | Data de Competência |  | Data de Execução do Serviço, no formato MMAAA.(DLAF.DATAES) |
| 51 | Data de Cancelamento |  | Se o Status do Lançamento Fiscal é “Cancelado”, recebe a Data do Cancelamento. (DLAF.DATACANCELAMENTO) |
| 52 | Motivo de Cancelamento |  | Este campo será preenchido com o primeiro caractere do **“Motivo do Cancelamento”** (aba Outros Dados | Outros). Conforme Layout da rotina, os valores válidos são: 1 – Erro na emissão; 2 – Serviço não prestado; 4 – Duplicidade da nota; 9 – Outros Motivos. Caso o Motivo do Cancelamento se inicie com valores diferentes este campo será preenchido com **“9”.** (DLAF.MOTIVOCANCELAMENTO) |
| 53 | Outro Motivo de Cancelamento |  | Se o primeiro caractere do **“Motivo do Cancelamento”** for “9”, receberá o restante da informação inserida no campo. |
| 54 | Número da Nota Substituidora |  | Este campo receberá o Número do Lançamento Fiscal substituto, informado na aba **“Referências | Lançamentos Fiscais”** do Lançamento Fiscal Cancelado. |

**2.2.1. Tipo de Negócio**

A informação do Tipo de Negócio seguirá as seguintes considerações:

Se o status do Lançamento Fiscal for **"Cancelado"**  
Então o Tipo do Negócio é **"0 Cancelada";**

Se a AIDF associada ao Lançamento Fiscal for autorizada por **"Prefeitura"**, fazer as seguintes considerações:

Se o campo **"Valor Bruto"** for igual ao campo **"Valor do Serviço"**  
                Então o Tipo do Negócio é **"1 Exclusivamente Prestação de Serviços"**  
                Senão **"2 Prestação de Serviços c/ Dedução";**

Se a AIDF associada ao Lançamento Fiscal for autorizada por **"Ambos"**, fazer as seguintes considerações:

Se o Tipo de Cliente do Lançamento Fiscal for **"Empresa"**  
        Então o Tipo do Negócio é **"7 Devolução/Simples Remessa/Entrada";**

Se não existir item tributado pelo ISS informado no Lançamento Fiscal  
     Então o Tipo do Negócio é **"5 Vendas de Mercadorias/Transporte Intermunicipal";**

Se existir item tributado pelo ISS informado no Lançamento Fiscal = 1  
       Então o Tipo do Negócio é **"6 Prestação de Serviços c/ Venda de Mercadorias/Transporte Intermunicipal";**

Se Não existir o Tributo ISS no Lançamento ou no Item  
      Então Tipo de Negócio é **“08 Não Inicidência”**

**2.2.2. Exigibilidade do ISSQN**

A informação da Exigibilidade do **ISSQN** seguirá as seguintes considerações:

Se o status do Lançamento Fiscal for **"Cancelado"**  
        Então o Tipo do Negócio é **"00 Cancelada";**

Se o lançamento for de exportação (CFOP para exterior) e o Município de Prestação do Serviço **não** for Belo Horizonte  
        Então Exigibilidade do ISSQN é **"02 Exportação";**

Se o Município de Prestação do Serviço for Belo Horizonte, fazer as seguintes considerações:

Se o Tipo de Recolhimento do ISS for **"Isento"**  
        Então Exigibilidade do ISSQN é **"04 Isenta do ISS em BH";**

Se o Tipo de Recolhimento do ISS for **"Depósito Judicial"**  
        Então Exigibilidade do ISSQN é **"05 Exigibilidade Suspensa por Decisão Judicial"**

Senão Exigibilidade do ISSQN é **"01 Exigível"**

Se a AIDF for autorizada por **"Ambos"** e não existir item tributado pelo ISS informado no Lançamento Fiscal  
        Então Exigibilidade do ISSQN é **"07 Vendas/Transporte Intermunicipal";**

Se Regime de ISS for IMUNE  
     Então Exigibilidade do ISSQN é **“03-Imunidade Tributaria”;**

Se Não existir Tributo ISS no Item ou Lançamento  
     Então Exigibilidade do ISSQN é **“06-Não Incidência”;**

**2.2.3. Regime Especial de Tributação**

A informação do Regime Especial de Tributação seguirá as seguintes considerações:

Se status do lançamento fiscal for **"Cancelado"**  
      Então o Regime de Tributação é **"0 Cancelada";**

Se a AIDF associada ao Lançamento Fiscal for autorizada por **"Ambos"** e não existir item tributado pelo ISS informado no Lançamento Fiscal  
       Então o Regime de Tributação é **"11 Vendas/Transporte Intermunicipal";**

Se o **"Regime ISS"** da Filial for:

**"Estimativa"**  
           Então o Regime de Tributação é **"2 Regime de Estimativa";**  
**"Sociedade Profissional"**  
           Então o Regime de Tributação é **"3 SPL - Sociedade de Profissionais Liberais";**  
**"Construção Civil"**  
           E não existir Tributo ISS no Item ou no Lançamento;

 Então o Regime de Tributação é **“12-Não Incidência”**

Senão o Regime de Tributação é **"6 Construção Civil";**

**"Microempresa"**  
             Então o Regime de Tributação é **"9 ME ou EPP optante pelo Simples Nacional";**

Senão o Regime de Tributação é **"1 Regra Geral";**

Se Não existir Tributo ISS no Item ou Lançamento  
     Então Regime de Tributação é **“12-Não Incidência”;,**

Não aderência aos tipos:  
• 4 Cooperativa,  
• 5 Não disponível na DES 3.0,  
• 7 Propaganda e Publicidade/Intermediação,  
• 8 Agenciamento de Turismo/Administração de Fundos e  
• 10 MEI - Microeempreendedor Individual

**2.3. Registro Tipo "D" - Dedução De Materiais, Serviços Ou Repasses**

Para gerar esse Registro é preciso que a Filial esteja com o parâmetro **“Emite Livros de Construção Civil”**habilitado e que o campo **“Código Projeto”** esteja preenchido no Lançamento Fiscal. Será gerado um Registro do tipo “**D”** para cada Nota Fiscal de Dedução vinculada ao Lançamento Fiscal de saída.

| Pos | Campo | Origem dos Dados |
| --- | --- | --- |
| 01 | Tipo do Registro | Identificação do registro. Caractere fixo "D". |
| 02 | Número da NFS-e importada com dedução | Se o Lançamento Fiscal de saída vinculado à dedução dor uma NFS-e estes campos serão preenchidos com número e valor da NFS-e. |
| 03 | Valor da NFS-e importada com dedução |
| 04 | Tipo da Dedução | Se as Notas de Dedução forem de Materiais (Tipo de Dedução “1”), então recebe "1 - para Materiais”.  Se as Notas de Dedução forem de Subempreitada (Tipo de Dedução “2”), então recebe "2 – Serviços”.  Não aderência para os Tipos: • “3” para Alimentação e Bebidas/Frigobar, • “4” para Reembolso de despesas, • “5” para Outras Deduções e • “6” para Repasse consorciado. (DLAFREFERENCIA.TIPODEDUCAO) |
| 05 | Descrição do Tipo de Dedução | Este campo não será gerado, visto que o Tipo de Dedução “5” não será gerado. |
| 06 | Data de emissão do documento utilizado na Dedução | Esses campos serão preenchidos com as informações dos Lançamentos Fiscais associados como Notas Fiscais de Dedução |
| 07 | Número do documento utilizado na Dedução |
| 08 | Valor Bruto do documento utilizado na Dedução/Repasse |
| 09 | Valor do material, serviço ou repasse utilizado nesta na operação. | Valor da dedução informado para a Nota Fiscal de Dedução.  (DLAFREFERENCIA.VALORDEDUCAO) |
| 10 | Alíquota | Alíquota informada para o tributo ISS no Item ou no Lançamento Fiscal de entrada que foi utilizado como Dedução de Subempreitada. (DTRBLAF.ALIQTRB) | (DTRBITEM.ALIQTRB) |
| 11 | Tipo de recolhimento do ISSQN | Se o Tipo de Recolhimento informado para o tributo ISS no Item ou no Lançamento Fiscal de entrada que foi utilizado como Dedução de Subempreitada ISS for “Retido na Fonte” ou “Retido na Fonte Deduzido” então preencher com “1”. Caso contrário preencher com “2”. |
| 12 | Inscrição Municipal do emissor do documento de Dedução/Repasse | Estes campos serão preenchidos com os dados do Cliente/Fornecedor do lançamento de dedução associado ao Lançamento Fiscal de saída. |
| 13 | CNPJ do emissor do documento de Dedução/ Repasse |
| 14 | CPF do emissor do documento de Dedução/ Repasse |
| 15 | Razão Social do emissor do documento de Dedução/Repasse |
| 16 | Logradouro do emissor do documento de Dedução/Repasse |
| 17 | Número do endereço do emissor do documento de Dedução/Repasse |
| 18 | Complemento do endereço do emissor do documento de Dedução/Repasse |
| 19 | Nome do bairro do emissor do documento de Dedução/Repasse |
| 20 | Cidade do emissor do documento de Dedução/Repasse |
| 21 | País do emissor do documento de Dedução/Repasse |
| 22 | CEP do emissor do documento de Dedução/Repasse |
| 23 | Telefone do emissor do documento de Dedução/Repasse |
| 24 | E-mail do emissor do documento de Dedução/Repasse |

**2.4. Registro Tipo "R" - Serviços Tomados**

Serão selecionados todos os Lançamentos de Entrada da Filial selecionada na tela da rotina que atendam aos seguintes critérios:

a) Lançamentos cuja data de entrada (de acordo com o parâmetro especificado no item 1) estejam  
dentro do período informado na tela da rotina;

b) Lançamentos com status “Normal”;

c) Lançamentos que possuam em uma de suas parcelas pelo menos um item tributado pelo ISS  
(Anexo “Dados Fiscais” no Cadastro de Produto);

d) Lançamentos cuja forma de tributação da natureza de operação seja “Sem ICMS” e “Sem IPI” ou  
cujo CFOP associado seja “1.933” ou “2.933”.

| Pos | Campo | Origem dos Dados |
| --- | --- | --- |
| 01 | Tipo do Registro | Identificação do registro. Caractere fixo "R". |
| 02 | Data de pagamento ou reconhecimento do crédito | Se o campo “Órgão Público” for marcado no momento da geração da rotina, este campo será preenchido com a “Data Vencimento”. Caso contrário será preenchido com a “Data de Execução do Serviço”. |
| 03 | Data de emissão | Data de emissão informada no Lançamento Fiscal (DLAF.DATAEMISSAO) |
| 04 | Modelo do Documento | “Modelo ISS” associado ao Tipo de Documento (Espécie) nos parâmetros do TOTVS Gestão Fiscal (Processo 03.02.03 – Apur. ISS por Filial, Etapa 1 – Modelo ISS). Não existindo a relação, preencher com o valor do campo “Código Modelo Documento” do Tipo de Documento associado ao Lançamento Fiscal. |
| 05 | Série do Documento | Série informada no Lançamento Fiscal. (DLAF.SERIEDOC) |
| 06 | Subsérie do Documento | Subsérie informada no Lançamento Fiscal. (DLAF.SUBSERIE) |
| 07 | Situação Especial de Responsabilidade | Ver item 2.4.1. |
| 08 | Motivo de não Retenção | Ver item 2.4.2. |
| 09 | Local da incidência | Município da Prestação do Serviço informado no Lançamento Fiscal ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. (DLAF.CODMUNICIPIOSERV/UFMUNICIPIOSERV) (DITEM.CODMUNICIPIOSERV/UFMUNICIPIOSERV) |
| 10 | Tipo de recolhimento do ISSQN | Se o Tipo de Recolhimento do ISS for “Retido na Fonte” ou “Retido na Fonte Deduzido” então preencher com “1”. Caso contrário preencher com “2”. |
| 11 | Número do documento | Número do Documento Inicial informado no Lançamento Fiscal. Se o documento for uma NFS-e o número do documento deve ser preenchido com o ano (4 dígitos) + o número da nota. (DLAF.DOCINI) |
| 12 | Valor Bruto do documento | Este campo é preenchido com o somatório dos valores (quantidade x preço) de todos os itens do Lançamento Fiscal, considerando todas as suas parcelas. Para lançamentos com status “Cancelado”, é preenchido com o valor zero. |
| 13 | Valor do serviço | Se a Filial estiver parametrizada para usar município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS dos Itens do Lançamento Fiscal, considerando somente os itens cujo município informado é igual ao município da Filial. Caso não haja nenhum serviço tributado no município, deve ser considerado o valor total dos serviços. Se a Filial estiver parametrizada para não usar o município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS do lançamento fiscal. Para lançamentos com status “Cancelado”, é preenchido com o valor zero. |
| 14 | Alíquota | Alíquota informada para o tributo ISS no Item ou no lançamento, observando a se a Filial estiver parametrizada para utilizar município por item. (DTRBLAF.ALIQTRB) | (DTRBITEM.ALIQTRB) |
| 15 | Simples Nacional | Se o campo “Optante pelo Simples” estiver marcado na aba Dados Fiscais | Outros Dados do Cadastro de Cliente/Fornecedor, recebe valor “1 – Optante ME/EPP”; Senão, Se o campo “Porte da Empresa” estiver preenchido com a opção “MEI – Micro Empreendedor Individual” recebe “3 – Optante MEI”; Senão recebe “2 – Não optante”. |
| 16 | Inscrição Municipal | Preencher esses campos com os dados do Cliente/Fornecedor associado ao Lançamento Fiscal.,  O campo “Inscrição Municipal” só deve ser preenchido se o Cliente/Fornecedor for do mesmo município da Filial declarante. Nos demais casos, deixar em branco. |
| 17 | CNPJ |
| 18 | CPF |
| 19 | Nome do prestador |
| 20 | Logradouro do prestador |
| 21 | Número do imóvel do prestador |
| 22 | Complemento do prestador |
| 23 | Bairro do prestador |
| 24 | Cidade do prestador |
| 25 | País do prestador |
| 26 | CEP do prestador |
| 27 | Telefone do prestador |
| 28 | E-mail do prestador |
| 29 | Inscrição Municipal do tomador |
| 30 | CNPJ do tomador | Não aderência do Produto. Os campos serão gerados vazios. |
| 31 | CPF do tomador |
| 32 | Nome do tomador |
| 33 | Logradouro do tomador |
| 34 | Número do imóvel do tomador |
| 35 | Complemento do tomador |
| 36 | Bairro do tomador |
| 37 | Cidade do tomador |
| 38 | País do tomador |
| 39 | CEP do tomador |
| 40 | Telefone do tomador |
| 41 | E-mail do tomador |
| 42 | Local da prestação dos serviços | Município da Prestação do Serviço informado no Lançamento Fiscal ou no Item do Lançamento Fiscal se a Filial estiver parametrizada para utilizar município por item. (DLAF.CODMUNICIPIOSERV/UFMUNICIPIOSERV) (DITEM.CODMUNICIPIOSERV/UFMUNICIPIOSERV) |
| 43 | País da prestação dos serviços | O campo País deve ser preenchido com o código do país associado ao Estado do Município da Prestação do Serviço de acordo com a tabela informada pelo usuário na tela de geração da rotina (BACEN). |
| 44 | Descrição do Evento | Não aderência |
| 45 | Data do evento | Não aderência |

**2.4.1. Situação especial de responsabilidade**

A informação da Situação especial de responsabilidade seguirá as seguintes considerações:

Se o Regime do ISS do Cliente/Fornecedor for **“Construção Civil”**  
        Então a Situação de Responsabilidade é **“3 Construção Civil”;**

Senão Se o campo **"Valor Bruto"** for igual ao campo "Valor do Serviço" e Tem ISS no Lançamento ou no Item  
      Então a Situação de Responsabilidade é **“1 Exclusivamente Prestação de Serviços”;**  
         Senão **“2 Prestação de Serviços c/ Dedução”;**

Se Não existir Tributo ISS no Item ou Lançamento  
     Então Situação de Responsabilidade do ISSQN é **“07-Não Incidência”;**

Não aderência:

**• “4 Agenciamento de Turismo/Administração de Fundos”**  
**• “5 Propaganda e Publicidade/Intermediação”**  
**• “6 Propaganda e Publicidade/Intermediação – Isento”**

**2.4.2. Motivo de não retenção**

A informação do Motivo de não retenção seguirá as seguintes considerações:

Se o lançamento for de exportação (CFOP para exterior) e o Município de Prestação do Serviço não for Belo Horizonte  
        Então o Motivo da Não Retenção é **"17 Exportação";**

Se o Cliente/Fornecedor for Optante pelo Simples ou se o Porte da Empresa for **“MEI – Micro Empreendedor Individual”**  
        Então o Motivo da Não Retenção é **“14 MEI – Microempreendedor Individual”;**

Senão Se o Regime do ISS do Cliente/Fornecedor for:**“Imune”**  
          Então o Motivo da Não Retenção é **“2 Imunidade Tributária”**;

,

“Estimativa”  
         Então o Motivo da Não Retenção é **“3 Regime de Estimativa em BH”;**  
“Sociedade Profissional”  
         Então o Motivo da Não Retenção é **“6 SPL - Sociedade de Profissionais Liberais”;**  
“Incentivo à Cultura”  
         Então o Motivo da Não Retenção é **“7 Incentivador Cultural em BH”;**

Senão Se o Tipo de Recolhimento do ISS for:

**“Isento”**  
      Então o Motivo da Não Retenção é **“4 Isenta do ISSQN em BH”;**  
**“Depósito Judicial”**  
      Então o Motivo da Não Retenção é **“8 Exigibilidade do ISSQN Suspensa por Decisão****Judicial”;**  
**“Retido na Fonte”** ou **“Retido na Fonte Deduzido”**  
      Então o Motivo da Não Retenção é **“16 ISSQN Retido”;**

Se o Município de Prestação do Serviço não for Belo Horizonte  
      Então o Motivo da Não Retenção é **“5 Tributação fora de BH”;**

Senão **“1 Não retido” .**

Se Não existir Tributo ISS no item ou lançamento  
     Então Regime de Tributação é **“10-Não Incidência”;**

Não aderência:

**“9 Profissional Autônomo inscrito na PBH”**  
**“12 Cartórios”**  
**“13 PROEMP”**  
**“15 Desobrigado legalmente”**

**2.5. Registro Tipo "T" - Transmissão De Imóveis**

Não aderência do Produto.

**2.6. Registro Tipo "I" - Adquirente**

Não aderência do Produto.

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
