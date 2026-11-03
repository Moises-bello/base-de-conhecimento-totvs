---
content_hash: 6ed4c22179ee3a4759ba58e5c6ad6dc90c2e74b77b670d4720bac608fde769c1
fetched_at: '2026-06-29T00:11:54.673759+00:00'
page_id: '856923135'
product: rm
source: tdn-rm
title: DMRISS - Brasília
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=856923135
version: 34
---

# Conteúdo

2Conteúdo

# 1. Introdução

O objetivo deste documento é oferecer uma visão geral a respeito da DMRISS e os processos necessários no sistema de Gestão Fiscal para geração do arquivo para posterior importação no programa da Prefeitura e apuração do ISSQN sendo considerados os lançamentos referente a serviços tomados.

Layout: **FISLAY0035 - DES-Brasilia-DF.TotvsGen**

Glossário de termos técnicos e siglas:

* **DMRISS** - Declaração Mensal de Serviços Tomados e Retenção dos Impostos Sobre Serviços.
* **ISSQN** - Imposto sobre Serviços de Qualquer Natureza.
* **NFS-e** - Nota Fiscal de Serviço Eletrônica.

# 2. Regras Gerais

O governo do Distrito Federal através do Decreto 43.982/2022 instituí no âmbito do Distrito Federal o Sistema de Gestão, Fiscalização e Arrecadação do Imposto Sobre Serviços de Qualquer Natureza - ISS. O acesso ao Sistema de Gestão do ISS dar-se-á por meio do Portal de Serviços da Receita do Distrito Federal, no endereço <https://www.receita.fazenda.df.gov.br/>. Através deste decreto fica estabelecido os modelos de documentos fiscais para acobertar as prestações de serviços, como também a emissão e armazenamento dos documentos fiscais e toda a gestão das obrigações acessórias. Em especifico temos a Declaração Mensal de Serviços Tomados e Retenção do ISS - DMRISS. Esta obrigação é constituída da relação de notas fiscais referente aos serviços tomados com retenção de imposto e deve ser elaborada no mês subsequente ao fato gerador.

# 3. Geração do arquivo

A geração da DMRISS deve ser executada a partir de Obrigações Acessórias | Gerador de Saídas. Sendo necessário obter o layout mais recente pelo TOTVS Compartilhamento.

O arquivo é gravado no diretório selecionado na tela de geração.

Para a geração do arquivo, devem ser informados:

* Filial;
* Período: Data inicial e final dos lançamentos a serem considerados. Lembrando que se trata de uma rotina mensal;
* Classificações que serão utilizadas para codificação do Município e para o País;
* Gerar Centralizada: Ao marcar este parâmetro, o sistema irá considerar lançamentos de entrada das filiais que possuem a mesma Inscrição Municipal e o mesmo município da filial selecionada. Desmarcado, será gerado apenas informações da filial informada.

# 4. Seleção de Lançamentos

A seleção dos Lançamentos Fiscais de Entrada serão feitos conforme os parâmetros informados no TOTVS Gestão Fiscal (Processo 03.02 - "Apuração de Tributos" → 03.02.03 - "ISS" → "Apur. por Filial" **→** Datas Apuração do ISS). As opções são:

* Data de Emissão;
* Data de Entrada/Saída;
* Data de Pagamento/Vencimento.

Utilizando a opção "Data de Pagamento/Vencimento", o sistema se comportará da seguinte forma:

* Se existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cujo Lançamento Financeiro associado esteja baixado no período informado na tela da rotina (Data de Baixa);
* Se não existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cuja Data de Vencimento (aba "Dados Financeiros") esteja no período informado na tela da rotina.

Essa parametrização deve ser feita para operação de Entrada.

***Importante!*** Se a Filial estiver parametrizada para utilizar município por item, as informações de Alíquota, Tipo de Recolhimento, Base de Cálculo e Valor do Imposto serão preenchidos conforme os dados informados na aba "Outros Tributos" dos Itens do Lançamento Fiscal. Se a Filial for parametrizada para não usar o município por item, esses campos serão preenchidos conforme os dados informados na aba "Outros Tributos" do Lançamento Fiscal.

# 5. Registros

A geração dos demais registros da DMRISS será realizada conforme as regras seguintes:

registroscabeçalhoCabeçalho2

### Cabeçalho - Identificação do Documento

|  |  |  |
| --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** |
| 01 | Inscrição municipal | Identificação da inscrição municipal, o sistema buscará pela coligada e filial. |
| 02 | Mês da competência | Mês referente ao pedido informado. Formato: **MM.** |
| 03 | Ano da competência | Ano referente ao período mensal de apuração. Formato: **AAAA.** |
| 04 | Hora  da geração | Considera para este campo a hora do sistema operacional na geração do arquivo. |
| 05 | Data da geração | Considera a data do sistema operacional na geração do arquivo. Formato: **DD/MM/AAAA.** |
| 06 | Razão social do tomador de serviços | Busca o nome da filial selecionada na tela de parâmetros. |
| 07 | Código Referente ao serviço contrato | Preencher com valor fixo = "**1**". |
| 08 | Texto fixo obrigatório da forma que está escrito | EXPORTAÇAO DECLARACAO ELETRONICA-ONLINE-NOTACONTROL |

textExemplo do Registro:registro-20Registro 2

### Registro  - Serviços Contratados

|  |  |  |
| --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** |
| 01 | Modelo | Documentos que tem ISS código = "**09**" |
| 02 | Número do documento | Número do documento |
| 03 | Valor Tributável | Valor Tributável. |
| 04 | Valor do Documento | Valor total do documento fiscal. |
| 05 | Alíquota | Alíquota. |
| 06 | Data de Emissão | Data de emissão do lançamento. |
| 07 | Data de Pagamento | Busca a data de vencimento do lançamento. |
| 08 | CPF/CNPJ | CPF/CNPJ do fornecedor. |
| 09 | Razão Social | Busca nome do Fornecedor do serviço tomado. |
| 10 | Inscrição Municipal | Inscrição Municipal do fornecedor do serviço. |
| 11 | Imposto Retido | Se retido gerar com **"1",** se não gerar com **"0"** |
| 12 | CEP | Busca CEP no cliente fornecedor. |
| 13 | Endereço | Busca endereço do fornecedor do serviço tomado. |
| 14 | Numero | Busca numero do fornecedor do serviço tomado. |
| 15 | Bairro | Busca o bairro do fornecedor. |
| 16 | Cidade | Busca a cidade do fornecedor. |
| 17 | Estado | Busca sigla do estado do fornecedor. |
| 18 | Código de área | Código de área. |
| 19 | Tributado no Município | Se o código do município do fornecedor for igual da filial gerar "**1**" se não  "**0**" |
| 20 | Item LC | Código de Serviço Federal. |
| 21 | Unidade Econômica | Caractere que indica a Unidade Econômica.  "**1**" = SIM |

textExemplo do Registro:estrutura\_registrosEstrutura do Arquivo2text
