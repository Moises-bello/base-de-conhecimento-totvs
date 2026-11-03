---
content_hash: 3df676ca73277f78d9106f3cfa2d0cee77aa22f0d60fc0ad2fe4c46ced30bffe
fetched_at: '2026-06-29T00:11:54.765488+00:00'
page_id: '857579299'
product: rm
source: tdn-rm
title: DES - Cachoeirinha
type: documentation
url: https://tdn.totvs.com/display/LRM/DES+-+Cachoeirinha
version: 8
---

# Conteúdo

2Conteúdo

# 1. Introdução

O objetivo deste documento é oferecer uma visão geral a respeito da Declaração Eletrônica de Serviços – DES e os processos necessários no sistema de Gestão Fiscal para geração do arquivo para posterior importação no programa da Prefeitura e apuração do ISSQN sendo considerados os lançamentos referente a serviços tomados.

Glossário de termos técnicos e siglas:

* **DES** - Declaração Eletrônica de Serviços.
* **ISSQN** - Imposto sobre Serviços de Qualquer Natureza.
* **NFS-e** - Nota Fiscal de Serviço Eletrônica.

# 2. Regras Gerais

A Prefeitura de Cachoeirinha através do Decreto Nº 5.222, de 18 de dezembro de 2013, regulamenta a  Declaração Eletrônica  de Serviços Mensal, prevista no art. 121, da Lei Complementar nº [28](https://leismunicipais.com.br/a/rs/c/cachoeirinha/lei-complementar/2010/2/28/lei-complementar-n-28-2010-consolida-a-legislacao-tributaria-municipal-e-institui-o-codigo-tributario-do-municipio-de-cachoeirinha), de 23 de dezembro de 2010 - Código Tributário Municipal, e dá outras providências.

§ 1º A Declaração Eletrônica Mensal do ISSQN deverá ser efetuada por meio do programa de computador (software) chamado ISSQN ELETRÔNICO, o qual será disponibilizado no site da Prefeitura Municipal de Cachoeirinha na Internet [www.cachoeirinha.rs.gov.br](http://www.cachoeirinha.rs.gov.br).

A entrega da Declaração Eletrônica Mensal do ISSQN à Secretaria Municipal da Fazenda dar-se-á por transmissão via internet, por meio magnético ou por outros dispositivos de armazenamento eletrônico de dados, desde que haja viabilidade técnica para esse caso.

A Declaração Eletrônica Mensal do ISSQN deverá ser entregue mesmo quando o declarante não apresentar movimento no período, ou quando a empresa estiver inativa.

Devem ser informadas na DES as seguintes operações:

a) Todos os serviços tomados e acobertados por documentos fiscais e sujeitos à incidência do ISSQN, devido ou não ao Município de Cachoeirinha;  
b) Os documentos fiscais Autorizados e Cancelados.

# 3. Geração do arquivo

A geração da DES deve ser executada a partir de Obrigações Acessórias | Gerador de Saídas. Sendo necessário obter o layout mais recente pelo TOTVS Compartilhamento.

O arquivo é gravado no diretório selecionado na tela de geração.

Para a geração do arquivo, devem ser informados:

* Filial;
* Período: Data inicial e final dos lançamentos a serem considerados. Lembrando que se trata de uma rotina mensal;
* Classificações que serão utilizadas para codificação do Município e para o País;
* Gerar Centralizada: Ao marcar este parâmetro, o sistema irá considerar lançamentos de entrada das filiais que possuem a mesma Inscrição Municipal e o mesmo município da filial selecionada. Desmarcado, será gerado apenas informações da filial informada.

As guias de recolhimento do ISSQN deverão ser geradas e obtidas pelos contribuintes e responsáveis tributários por meio do software da DES.

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

**Observação:** A geração do arquivo da DES pelo Módulo Fiscal da linha RM não inclui o registro 40 (Exclusivo para Instituição Financeira)

A geração dos demais Registros da DES será realizada conforme as regras seguintes:

registrosregistro-10Registro 102

### Registro 10 - Identificação do Documento

|  |  |  |
| --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** |
| 01 | Tipo Registro | Identificação do registro. Caractere fixo "10". |
| 02 | Tipo Serviço | Preencher com valor fixo = "**2 - Serviço Tomado**" |
| 03 | Tipo Documento | Este campo será gerado com valor fixo = "**07**" |
| 04 | Número Documento | Número do Documento Inicial informado no Lançamento Fiscal. Se o documento for uma NFS-e o número do documento deve ser preenchido com o número da nota. |
| 05 | Competência | Data de Execução do Serviço, no formato **MM/AAAA**. |
| 06 | Tipo Pessoa | Se a Categoria do Cliente/Fornecedor for Pessoa Física, preencher com "**F**", se for Pessoa Jurídica, preencher com "**J**" |
| 07 | CPF/CNPJ  Prestador | Documento do prestador do serviço. |
| 08 | Tipo Pessoa | Será gerado apenas para Filial com CNPJ - Preenchido com "**J**" |
| 09 | CPF/CNPJ Tomador | Documento do tomador do serviço |
| 10 | Data Emissão | Data de emissão informada no Lançamento Fiscal, no formato **DD/MM/AAAA**. |
| 11 | Valor Contábil | Busca do valor contábil do lançamento. |
| 12 | Situação Documento | Valor Fixo - Preenchido com "**E – Emitido**". |
| 13 | Observações | Descrição do Documento - Gerado a partir do campo **Observação** da Situação tributária - Situação Tributária | Informações Adicionais | Outros Dados | Observação |
| 14 | Optante pelo Simples | Se o campo "Optante pelo Simples" estiver marcado, no menu Tributos do Cadastro do Cliente/Fornecedor, receberá valor "**S - Sim**", senão recebe "**N - Não**". |

textExemplo do Registro:registro-20Registro 202

### Registro 20 - Serviços Tomados

|  |  |  |
| --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** |
| 01 | Tipo Registro | Identificação do registro. Caractere fixo "20". |
| 02 | Tipo Serviço | Preencher com valor fixo = "**2 - Serviço Tomado**" |
| 03 | Tipo Documento | Este campo será gerado com valor fixo = "**07**" |
| 04 | Numero Documento | Número do Documento Inicial informado no Lançamento Fiscal. Se o documento for uma NFS-e o número do documento deve ser preenchido com o número da nota. |
| 05 | Competência | Data de Execução do Serviço, no formato **MM/AAAA**. |
| 06 | Tipo Pessoa | Se a Categoria do Cliente/Fornecedor for Pessoa Física, preencher com "**F**", se for Pessoa Jurídica, preencher com "**J**" |
| 07 | CPF/CNPJ Prestador | Documento do prestador do serviço. |
| 08 | Tipo Pessoa | Será gerado apenas para Filial com CNPJ - Preenchido com "**J**" |
| 09 | CPF/CNPJ Tomador | Documento do tomador do serviço |
| 10 | Código Item Lista Serviço | Código do Item da Lista de Serviços da Lei Complementar 116 |
| 11 | Alíquota Serviço | Alíquota Referente ao Item da Lista de Serviços |
| 12 | Valor Tributável | Valor Tributável |
| 13 | Dedução | Dedução |
| 14 | Valor Retido | Valor Retido |
| 15 | Local Prestação Serviço | Local da Prestação do Serviço |
| 16 | Cod Situação Tributaria | Código da Situação Tributária da Declaração do Serviço |
| 17 | Tributa ISS Município Prestador | Este campo será gerado com valor fixo = "**N**" |
| 18 | Redução ISS Obra | Não será gerado |

textExemplo do Registro:registro-30Registro 302

### Registro 30 - Identificação do Tomador

|  |  |  |
| --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** |
| 01 | Tipo Registro | Identificação do registro. Caractere fixo "30". |
| 02 | Tipo Pessoa | Será gerado apenas para Filial com CNPJ - Preenchido com "**J**" |
| 03 | CPF/CNPJ | CPF / CNPJ da pessoa |
| 04 | Razão Social | Nome / Razão Social |
| 05 | Logradouro | Descrição do logradouro |
| 06 | Numero Logradouro | Número Residência / Estabelecimento |
| 07 | Complemento Logradouro | Complemento do endereço |
| 08 | Bairro | Descrição do Bairro |
| 09 | Cidade | Nome da Cidade |
| 10 | Estado | Estado (Unidade da Federação) |
| 11 | CEP | Código de Endereçamento Postal |
| 12 | Fone | Fone comercial (99 9999-9999) |
| 13 | Fax | Fax (99 9999-9999) |

textExemplo do Registro:estrutura\_registrosEstrutura do Arquivo2textExemplo de Arquivo:
