---
content_hash: 6bbec67b72d801b31ab3ccc3560556c21766831f151f339ac2da346b4c8d920a
fetched_at: '2026-06-29T00:11:55.039639+00:00'
page_id: '860229966'
product: rm
source: tdn-rm
title: DMS - Ribeirão Preto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=860229966
version: 8
---

# Conteúdo

## 2Conteúdo

# 1. Introdução

O objetivo deste documento é oferecer uma visão geral a respeito da Declaração de Serviços Contratos e os processos necessários no sistema de Gestão Fiscal para geração do arquivo para posterior importação no programa da Prefeitura e apuração do ISSQN sendo considerados os lançamentos referente a serviços tomados.

Layout: **FISLAY0036 - DES-Ribeirão-Preto-SP.TotvsGen**

Glossário de termos técnicos e siglas:

* **Declaração de Serviços Contratos**.
* **ISSQN** - Imposto sobre Serviços de Qualquer Natureza.
* **NFS-e** - Nota Fiscal de Serviço Eletrônica.

# 2. Regras Gerais

Para cumprir com as obrigações acessórias perante a prefeitura municipal de Ribeirão Preto através do Decreto Nº 176, de 31/07/2020 regulamenta os dispositivos da Lei Municipal Nº 2.415 de 21 de dezembro de 1970 (Código Tributário Municipal), dispondo sobre o sistema de Gerenciamento do ISSQN, Nota Fiscal de Serviço Eletrônica - NFS-E, Nota Fiscal de Serviços Avulsa Eletrônica, Recibo Provisório de Serviço, Declaração Eletrônica de Serviços, Declaração Eletrônica do Responsável Tributário, Declaração Eletrônica de Serviços de Instituições Financeira e dá outras providências.

<https://www.notacontrol.com.br/static-issnetonline/Ajuda/Html/index.html?ajuda_importacao_iss_net.html>

# 3. Geração do arquivo

A geração da Declaração de Serviços Contratos deve ser executada a partir de Obrigações Acessórias | Gerador de Saídas. Sendo necessário obter o layout mais recente pelo TOTVS Compartilhamento.

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

A geração dos demais registros da Declaração de Serviços Contratos será realizada conforme as regras seguintes:

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

textExemplo do Registro:estrutura\_registrosExemplo do Arquivo2text
