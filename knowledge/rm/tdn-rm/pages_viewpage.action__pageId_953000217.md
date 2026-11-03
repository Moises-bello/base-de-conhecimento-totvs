---
content_hash: 0d90e80c03de124f6244a1b8d28bea4c56ef04f1af673228493a9687f0a5d042
fetched_at: '2026-06-29T00:12:10.183543+00:00'
page_id: '953000217'
product: rm
source: tdn-rm
title: Grupo C – Identificação do Emitente da Nota Fiscal Eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953000217
version: 3
---

**Observação importante**  
Quando a filial estiver com a opção de **Filial SCP** marcada, as informações apresentadas neste grupo serão geradas a partir do cadastro do **Sócio Ostensivo** informado, substituindo os dados do cadastro padrão da filial emissora.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo C – Identificação do Emitente da Nota Fiscal Eletrônica** | | | | | | | |
| **#** | **ID** | **Campo** | **Descrição** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 30 | C01 | emit | Identificação do emitente da NF-e |  |  |  |  |
| 31 | C02 | CNPJ | CNPJ do emitente | Informar o CNPJ do emitente. Na emissão de NF-e avulsa pelo Fisco, as informações do remetente serão informadas neste grupo. O CNPJ ou CPF deverão ser informados com os zeros não significativos. | GFILIAL.CGC | CNPJ da Filial. | Cadastro da Filial | pasta Identificação. |
| 31a | C02a | CPF | CPF do remetente | GFILIAL.CGC | CPF da Filial. | Cadastro da Filial | pasta Identificação. |
| 32 | C03 | xNome | Razão Social ou Nome do emitente | - | GFILIAL.NOME | Campo Nome informado na aba Identificação do cadastro da Filial. | Cadastro da Filial | pasta Identificação. |
| 33 | C04 | xFant | Nome fantasia | - | GFILIAL.NOMEFANTASIA | Campo Nome Fantasia informado na aba Identificação do cadastro da Filial. | Cadastro da Filial | pasta Identificação. |
| 34 | C05 | enderEmit | Endereço do emitente | - |  | Endereço da Filial. | Cadastro da Filial | pasta Endereço. |
| 35 | C06 | xLgr | Logradouro | - | DTIPORUA.DESCRICAO + GFILIAL.RUA | Tipo de Rua + o campo Endereço informado na aba Endereço do cadastro da Filial. | Cadastro da Filial | pasta Endereço. |
| 36 | C07 | nro | Número | - | GFILIAL.NUMERO | Campo Número informado na aba Endereço do cadastro da Filial. | Acesse Cadastros | Filial | aba Endereço. |
| 37 | C08 | xCpl | Complemento | - | GFILIAL.COMPLEMENTO | Campo Complemento informado na aba Endereço do cadastro da Filial. | Cadastro da Filial | pasta Endereço. |
| 38 | C09 | xBairro | Bairro | - | DTIPOBAIRRO.DESCRICAO + GFILIAL.BAIRRO | Tipo de Bairro + o campo Bairro do cadastro da Filial. | Cadastro da Filial | pasta Endereço. |
| 39 | C10 | cMun | Código do município | Utilizar a Tabela do IBGE (Anexo IX- Tabela de UF, Município e País). | GFILIAL.CODMUNICIPIO | Código IBGE vinculado ao cadastro do município. | Cadastro da Filial | pasta Endereço. |
| 40 | C11 | xMun | Nome do município | - | GMUNICIPIO.NOMEMUNICIPIO | Nome do município informado no cadastro. | Cadastro da Filial | pasta Endereço. |
| 41 | C12 | UF | Sigla da UF | - | GFILIAL.ESTADO | Estado selecionado na aba endereço do cadastro da Filial. | Cadastro da Filial | pasta Endereço. |
| 42 | C13 | CEP | Código do CEP | Informar os zeros não significativos. (NT 2011/004). | GFILIAL.CEP | Informado na aba endereço do cadastro da Filial. | Cadastro da Filial | pasta Endereço. |
| 43 | C14 | cPais | Código do país | 1058=Brasil | DPAIS.CODPAIS | País selecionado no endereço do cadastro da Filial. | Cadastro da Filial | pasta Endereço. |
| 44 | C15 | xPais | Nome do País | Brasil ou BRASIL | GPAIS.DESCRICAO | Descrição do cadastro do país. | Cadastro da Filial | pasta Endereço. |
| 45 | C16 | fone | Telefone | Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone (v2.0). | GFILIAL.DDD + GFILIAL.TELEFONE | DDD + Telefone | Cadastro da Filial | pasta Endereço.  **Nota**: Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone (v2.0). |
| 46 | C17 | IE | Inscrição Estadual do Emitente | Informar somente os algarismos, sem os caracteres de formatação (ponto, barra, hífen, etc.). **Nota**: Na emissão de NF-e Avulsa pode ser informado o literal “ISENTO” para os contribuintes do ICMS isentos de inscrição no Cadastro de Contribuintes de ICMS. | GFILIAL.INSCRICAOESTADUAL | Campo Inscrição Estadual da aba Dados Adicionais do cadastro da Filial. | Cadastro da Filial | pasta Dados Adicionais**.**  **Nota**:Será verificado se a IE é valida, porem, a IE não será validada se o ramo de atividade da Filial for produtor Rural. |
| 47 | C18 | IEST | IE do Substituto Tributário | IE do Substituto Tributário da UF de destino da mercadoria, quando houver a retenção do ICMS ST para a UF de destino. | DINSCEST.INSCEST | É gerado se a regra de ICMS da CFOP estiver configurada como "Substituto Tributário" no quadro "Situação da Retenção ICMS S.T." da aba Dados ICMS e no cadastro da filial estiver vinculada uma IEST referente ao estado de destino da operação. | Cadastro da Filial | Anexos. |
| 47.1 | C18.1 | -x- | Sequência XML | Grupo opcional. |  | - | - |
| 48 | C19 | IM | Inscrição Municipal do Prestador de Serviço | Informado na emissão de NF-e conjugada, com itens de produtos sujeitos ao ICMS e itens de serviços sujeitos ao ISSQN. | GFILIAL.INSCMUN | Inscrição Municipal informada na aba Dados Adicionais do cadastro da Filial. | Cadastro da Filial | pasta Dados Adicionais. |
| 49 | C20 | CNAE | CNAE fiscal | Campo Opcional. Pode ser informado quando a Inscrição Municipal (id:C19) for informada. | GFILIAL.CODATIVFED | Campo C.N.A.E informado na aba Dados Adicionais do cadastro da Filial. | Cadastro da Filial | pasta Dados Adicionais.  **Nota**: Somente será preenchido se a Inscrição municipal estiver preenchida. |
| 49a | C21 | CRT | Código de Regime Tributário | 1=Simples Nacional; 2=Simples Nacional, excesso sublimite de receita bruta; 3=Regime Normal. (v2.0). | DFILIAL.OPTANTESIMPLES  DFILIAL.SUBLIMITEEXCEDIDO | Para o caso de excesso de sublimite deve ser marcado o parâmetro SUBLIMITE EXCEDIDO que só estará disponível para filiais optantes pelo simples. | Cadastro da Filial | Anexos | pasta Dados Fiscais. |
