---
content_hash: 7a96c54f9847d478f4d4072b341e3e57e6c9dc9d07f1ae0a4bf1f4d81d77e4e4
fetched_at: '2026-06-29T00:12:02.347267+00:00'
page_id: '900732545'
product: rm
source: tdn-rm
title: DMS - Ponta-Grossa
type: documentation
url: https://tdn.totvs.com/display/LRM/DMS+-+Ponta-Grossa
version: 16
---

# Conteúdo

**Conteúdonone**

# 1. Visão Geral

A Declaração de Serviços Tomados é uma rotina municipal cujo objetivo é informar à prefeitura o registro dos serviços prestado e contratados pelas pessoas jurídicas para que possam gerenciar, de forma eficaz, o recolhimento do Imposto sobre Serviços de Qualquer Natureza – ISSQN. Neste documento iremos demonstrar o processo para a extração das informações no Gestão Fiscal para a geração do arquivo

# 2. Geração do Arquivo XML

A geração da rotina municipal de Ponta Grossa é executada a partir do menu *Obrigações Acessórias | Rotinas Fiscais | Municipais*. Na tela de geração da rotina, informe os seguintes dados:

* Código da Filial
* Data de Emissão Inicial e Data de Emissão Final;
* Classificação de País

***Observação***: O arquivo será gerado em formato XML para depois ser importado no site da Prefeitura.

DMSPontaGrossaDeclaraçãodeServicos-gruposxmlLoteNotasFiscaisLoteNotasFiscais

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Tamanho** | **Observações** |
| NumeroLote | Número do lote de RPS | 15 | Identificador único do lote |
| CpfCnpj | Número CNPJ | 14 | CPF ou CNPJ da Filial. |
| InscricaoMunicipal | Número da Inscrição Municipal | 15 | Inscrição Municipal da Filial. |
| QuantidadeNotas | Determina a quantidade de Notas Fiscais no Lote | 5 | Quantidade de notas as serem importadas neste lote. |
| OptanteSimplesNacional | Verificar se a Filial é Optante Simples ou não | 1 | Verificar no cadastro da filial -1 para sim 2 para Não |
| RegimeEspecialTributacao | Código de Identificação do regime especial de tributação | 2 | Será gerado com a opção parametrizada em Filial > Anexos > Dados Fiscais > Tipo de Estabelecimento > Regime Especial de Tributação - NFS-e/TSS. A DMS Ponta Grossa aceita os seguintes valores ao validar o arquivo:   * 1 - Microempresa Municipal (ME); * 2 - Estimativa * 3 - Sociedade de Profissionais * 4 - Cooperativa * 5 - Microempresário Individual (MEI) * 6 - Microempresário e Empresa de Pequeno Porte (ME EPP) |

Informações da Nota Fiscal Informações da Nota Fiscal 

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Tamanho** | **Observação** |
| <InfNotaFiscal> |  |  | Tag pai que tem a função de agrupar as informações da nota fiscal |
| <NotaFiscal id=\*> |  |  | Indíce referente ao lançamento da Nota fiscal |
| <IdentificacaoNotaFiscal> |  |  | Tag pai que tem a função de identificar a nota fiscal |
| <Numero> | Numero da Nota Fiscal | 11 | Numero da nota fiscal do lançamento |
| <Serie> | Serie | 3 | Serie do lançamento fiscal |
| <TipoDocumento> | Modelo do documento | 3 | Buscar nos parâmetros de apuração do  ISS em modelo de iss ou no tipo de documento o codigo de modelo do documento do lançamento fisca. |
| <DataEmissao> | Data de Emissão do documento Fiscal. | 17 | Data de emissão do lançamento fiscal |
| <Status> | Status do lançamento Fiscal. | 1 | Status do lançamento fiscal 1- Normal 2- Cancelado |
| <TipoDeclaracao> |  | 1 | Fixar 2 - serviço Tomado |
| <ValorTotal> | Valor do documento fiscal. | 15,2 | Valor  contábil do lançamento fiscal |

Lista ServiçosLista Serviços

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Tamanho** | **Observação** |
| <Servico> |  |  | Tag referente ao serviço |
| <ValorBaseCalculo> | Base de calculo do tributo | 15,2 | Buscar base de cálculo do tributo  referente ao serviço no lançamento fiscal |
| <ValorServicos> | Valor do Serviço | 15,2 | Buscar valor do item do lançamento fiscal |
| <Valordeducoes> | Valor dedução do serviço | 15,2 | Este campo será gerado sobe Demanda |
| <ValorIss> | Valor do Tributo ISS referente ao serviço |  | Valor referente ao tributo ISS no item do  lançamento Fiscal |
| <Alíquota> | Valor percentual da alíquota do tributo | 4,2 | Percentual de alíquota referente ao tributo do item do lançamento. |
| <IssRetido> | Valor referente ao ISS Retido | 1 | Tipo de tributação do item 1=Sim 2=Não. |
| <ItemListaServico> | Código do Serviço | 5 | Código do serviço no item do lançamento fiscal ou na situação tributária |
| <Dicriminacao> | Descrição do Serviço Ou Informações Adicionai do Serviço. | 2000 | Esta informação será buscada no histórico do item  do lançamento |
| <CodigoMunicipio> | Código Município | 7 | Código do município de acordo com a tabela selecionada da prestação do serviço do lançamento fiscal. |
| <CodigoPais> | Código País | 4 | O campo País deve ser preenchido com o código do país associado ao Estado do Município da Prestação do Serviço de acordo com a tabela informada pelo usuário na tela de geração da rotina (BACEN). |
| <ExigibilidadeISS> | Código de Natureza de operação | 2 | Verifica o tipo de recolhimento do lançamento e o tipo de tributação do item. |
| <MunicipioIncidencia> | Município de Incidência do tributo | 7 | Código do município de acordo com a tabela selecionada da prestação do serviço do lançamento fiscal. |

TomadorTomador

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Tamanho** | **Observação** |
| <IdentificacaoTomador> |  |  | Tag Pai referente a informações do Tomador |
| <Cnpj>\*</Cnpj> | Numero do CNPJ do Tomador | 14 | Buscar na  Filial selecionada no contexto  CGC |
| <InscricaoMunicipal> | Inscr. Municipal do Tomador | 15 | Buscar na  Filial selecionada no contexto a Inscrição Estadual |
| <RazaoSocial> | Razão Social do Tomador | 150 | Buscar na  Filial selecionada no contexto a Razão Social do Tomador |
| <NomeFantasia> | Nome Fantasia do Tomador | 60 | Buscar na  Filial selecionada no contexto o Nome Fantasia do Tomador |
| <Endereco> | Tipo e nome do endereço do Tomador | 125 | Buscar na  Filial selecionada no contexto o endereço do Tomador |
| <Numero> | Numero do imóvel do tomador | 10 | Buscar na  Filial selecionada no contexto o numero do endereço do tomador |
| <Bairro> | Bairro do Tomador | 60 | Buscar na  Filial selecionada no contexto o Bairro do Tomador |
| <CodigoMunicipio> | Código de Identificação Município do Tomador conforme tabela do IBGE | 7 | Buscar na  Filial selecionada no contexto o código do Município do Tomador |
| <Uf> | Unidade Federativa do tomador | 2 | Buscar na  Filial selecionada no contexto a UF do Tomador |
| <CodigoPais> | Código da unidade do Pais do Tomador conforme tabela do BACEN | 4 | Buscar na  Filial selecionada no contexto o código do Pais do Tomador |
| <Cep> | Cep do Tomador | 8 | Buscar na  Filial selecionada no contexto o cep do Tomador |
| <Telefone> | Telefone do contato do tomador | 20 | Buscar na  Filial selecionada no contexto o telefone de contato do Tomador. |

PrestadorPrestador

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Tamanho** | **Observação** |
| <IdentificacaoPrestador> |  |  | Tag Pai de identificação do prestador |
| <Cnpj> | Numero do CNPJ do Prestador | 14 | Buscar   o CNPJ do prestador no clifor referente ao lançamento fiscal |
| <RazaoSocial> | Razão Social do Prestador | 150 | Buscar  o Razão Social  do prestador no clifor referente ao lançamento fiscal |
| <Endereco> | Tipo e nome do logradouro do Prestador | 125 | Buscar  o Endereço  do prestador no clifor referente ao lançamento fiscal |
| <Numero> | Numero do imóvel do Prestador | 10 | Buscar  o número do endereço  do prestador no clifor referente ao lançamento fiscal |
| <Bairro> | Bairro | 60 | Buscar  o bairro  do prestador no clifor referente ao lançamento fiscal |
| <CodigoMunicipio> | Código de Identificação do Município conforme tabela IBGE | 7 | Buscar  o código do município  do prestador no clifor referente ao lançamento fiscal |
| <Uf> | Sigla da Unidade Federativa | 2 | Buscar  a UF  do prestador no clifor referente ao lançamento fiscal |
| <CodigoPais> | Código da Unidade do Pais conforme tabela Bacen | 4 | Buscar  o código do país  do prestador no clifor referente ao lançamento fiscal |
| <Cep> | Número do Cep | 8 | Buscar  o cep  do prestador no clifor referente ao lançamento fiscal |
| <Telefone> | Telefone | 20 | Buscar  o telefone do contato  do prestador no clifor referente ao lançamento fiscal |

ExemploXMLExemplo XMLxmlExemplo de Arquivo  
0001

XXXXXXXXX
XXXXXX
1
1
1




000001
001
1
2024-12-31T00:00:00
1
1
1000.00



0
1000
0
50.00
1
1
14.01
Serviços Prestados
4119905
1058
1
4119905

         
           
             XXXXXX
           
         
         XXXXXX
         
           RUA TESTE
           10
           RONDA
           4119905
           PR
           84000000
         
         
            3323-4423
         
       
         
           
             XXXXXX
           
           XXXXXX
         
         XXXXXXX
         
           SILVA JARDIM
           2
           ESQ 14 DE JULHO
           CENTRO
           4119905
           PR
           84040020
         
         
            3323-4423
         
       
       
         \_
         \_
       
]]>
