---
content_hash: 8c7baa8cc25677bd51ec68b05e9e3c8ed413ec6fbd8e2b8eef248602decf539d
fetched_at: '2026-06-29T00:12:10.210271+00:00'
page_id: '953000345'
product: rm
source: tdn-rm
title: Grupo E – Identificação do Destinatário da Nota Fiscal eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953000345
version: 1
---

Informações

 Foi criado um novo Tipo de Natureza no cadastro da CFOP, este tipo é referente a Devolução por Recusa.

Ao enviar uma NF-e de um Movimento parametrizado através processo de Cópia por Referência em conjunto com o Tipo de Natureza igual a Devolução por Recusa, resultará em um XML da qual a tag destinatário (dest) será referente a empresa, e não ao cliente/fornecedor de origem/destino.

Mais sobre Natureza de Operação: <https://tdn.totvs.com/x/PoovGQ>

Veja como parametrizar Devolução por Recusa: <https://tdn.totvs.com/x/-lYrIw>

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo E – Identificação do Destinatário da Nota Fiscal eletrônica** | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 62 | E01 | Dest | Identificação do Destinatário da NF-e | Grupo obrigatório para a NF-e (modelo 55). |  |  | Se o Tipo de Destinatário do movimento for diferente de Empresa (TTMV.TIPODESTIN) Então  serão selecionados os dados do cliente fornecedor da nota (TMOV.CODCFO) Senão Se O Tipo emitente do movimento for igual a empresa (TTMV.TIPOEMITENTE) E  Edita Cliente Fornecedor Origem Destino habilitado (TITMTMV.EDITACFOORIGEMDESTINO) E A CFOP utilizado no movimento for de importação (DNATUREZA.CODNAT iniciada por 3) E Movimento de Entrada (TMOV.CODTMV iniciado por 1.2) Então Serão selecionados Os dados do cliente fornecedor origem Destino (TMOV.CODCFONATUREZA) Senão Se Filial Entrega Preenchido (TMOV.CODFILIALENTREGA) E Tipo de movimento de Transferência (TMOV.CODTMV iniciado por 3.1) Então Serão selecionados os dados da Filial de Entrega (TMOV.CODFILIALENTREGA) Senão Serão selecionados os dados da Filial de destino (TMOV.CODFILIALDESTINO)     A partir da versão 12.1.28 é possível transmitir NF-e de Devolução por Recusa sem os dados do cliente.  Outras regras:  A partir da versão 12.1.29 se nos parâmetros do movimento etapa **Mov - Transporte 2/3** | opção "**Utilizar Endereço de Coleta e Entrega como Destinatário**"  estiver preenchida como "**usa**"  Ao gerar o arquivo XML da NF será selecionado o "Endereço de Entrega do Movimento" ou "Endereço de entrega do Cli\for" |
| 63 | E02 | CNPJ | CNPJ do destinatário | Informar o CNPJ ou o CPF do destinatário, preenchendo os zeros não significativos. No caso de operação com o exterior, ou para comprador estrangeiro informar a tag "idEstrangeiro", com o número do passaporte ou outro documento legal para identificar pessoa estrangeira (campo aceita valor nulo). | FCFO.CGCCFO ou GFILIAL.CGC | CNPJ do Cliente/Fornecedor. | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 64 | E03 | CPF | CPF do destinatário | FCFO.CGCCFO ou GFILIAL.CGC | CPF do Cliente/Fornecedor. | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 64a | E03a | idEstrangeiro | Identificação do destinatário no caso de comprador estrangeiro | FCFO.DOCUMENTOESTRANGEIRO | Campo Documentos Estrangeiro | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação.  **Nota**: Habilitado apenas quando o país é do exterior. |
| 65 | E04 | xNome | Razão Social ou nome do destinatário | Tag obrigatória para a NF-e (modelo 55) e opcional para a NFC-e. | FCFO.NOME ou GFILIAL.NOME | Nome do Cliente/Fornecedor ou da Filial. | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação.  **Nota**: Quando a operação se tratar de emissão própria, será considerado o campo Nome do cadastro da Filial. |
| 66 | E05 | enderDest | Endereço do Destinatário da NF-e | Grupo obrigatório para a NF-e (modelo 55). |  | - | - |
| 67 | E06 | xLgr | Logradouro | - | DTIPORUA.DESCRICAO + (FCFO.RUA ou GFILIAL.RUA) | Tipo de Rua + Endereço | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 68 | E07 | nro | Número | - | FCFO.NUMERO ou GFILIAL.NUMERO | Número | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 69 | E08 | xCpl | Complemento | - | FCFO.COMPLEMENTO ou GFILIAL.COMPLEMENTO | Complemento | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 70 | E09 | xBairro | Bairro | - | DTIPOBAIRRO.DESCRICAO + FCFO.BAIRRO | Tipo de Bairro + Bairro | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 71 | E10 | cMun | Código do município | Utilizar a Tabela do IBGE (Anexo IX - Tabela de UF, Município e País). Informar ‘9999999 ‘para operações com o exterior. | FCFO.CODMUNICIPIO ou GFILIAL.CODMUNICIPIO | Cód. Município | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 72 | E11 | xMun | Nome do município | Informar ‘EXTERIOR ‘para operações com o exterior. | GMUNICIPIO.NOMEMUNICIPIO | Nome do município | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 73 | E12 | UF | Sigla da UF | Informar ‘EX’ para operações com o exterior. | FCFO.CODETD ou GFILIAL.ESTADO | Estado | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 74 | E13 | CEP | Código do CEP | Informar os zeros não significativos. | FCFO.CEP ou GFILIAL.CEP | CEP. Informar os zeros não significativos. (NT 2011/004). | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 75 | E14 | cPais | Código do País | Utilizar a Tabela do BACEN (Anexo IX - Tabela de UF, Município e País). | DPAIS.CODPAIS | 1058=Brasil | Codificação vinculada ao cadastro do país selecionado no movimento, pasta Dados Gerais | aba Identificação. |
| 76 | E15 | xPais | Nome do País | Brasil ou BRASIL | GPAIS.DESCRICAO | País | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 77 | E16 | fone | Telefone | Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone (v2.0). | FCFO.TELEFONE ou GFILIAL.DDD + GFILIAL.TELEFONE | DDD + Telefone | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 77a | E16a | indIEDest | Indicador da IE do Destinatário | 1=Contribuinte ICMS (informar a IE do destinatário); 2=Contribuinte isento de Inscrição no cadastro de Contribuintes do ICMS; 9=Não Contribuinte, que pode ou não possuir Inscrição Estadual no Cadastro de Contribuintes do ICMS.  **Nota 1:** No caso de NFC-e informar indIEDest=9 e não informar a tag IE do destinatário; **Nota 2:** No caso de operação com o Exterior informar indIEDest=9 e não informar a tag IE do destinatário; **Nota 3:** No caso de Contribuinte Isento de Inscrição (indIEDest=2), não informar a tag IE do destinatário. | FCFO.CONTRIBUIINTE ou DFILIAL.CONTRIBUINTE | Contribuinte ICMS | No cadastro do Cliente/Fornecedor, pasta Integrações | Tributos.  No caso do cadastro da Filial, Anexos | Dados Fiscais | pasta Dados Adicionais | aba Tributos. |
| 78 | E17 | IE | Inscrição Estadual do Destinatário | Campo opcional. Informar somente os algarismos, sem os caracteres de formatação (ponto, barra, hífen, etc.).Campo opcional. Informar somente os algarismos, sem os caracteres de formatação (ponto, barra, hífen, etc.). | FCFO.INSCRESTADUAL OU GFILIAL.INSCRICAOESTADUAL | Inscrição Estadual do Cliente/Fornecedor. Em se tratando de emissão própria, considera-se a Inscrição Estadual da Filial emitente. | Cadastro do Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. **Nota:** se a Inscrição Estadual estiver preenchida e o ramo de atividade for diferente de Produtor Rural, a IE será validada conforme a UF do Destinatário. **Nota2:** Em se tratando de emissão própria, se a Inscrição Estadual estiver preenchida como ISENTO ou estiver vazia, não impacta na emissão da NF-e.  Cadastro da IE da filia na pasta Dados Adicionais. |
| 79 | E18 | ISUF | Inscrição na SUFRAMA | Obrigatório, nas operações que se beneficiam de incentivos fiscais existentes nas áreas sob controle da SUFRAMA. A omissão desta informação impede o processamento da operação pelo Sistema de Mercadoria Nacional da SUFRAMA e a liberação da Declaração de Ingresso, prejudicando a comprovação do ingresso / internamento da mercadoria nestas áreas. (v2.0). | FCFO.SUFRAMA OU GFILIAL.SUFRAMA | Inscrição no SUFRAMA | No cadastro do Cliente/Fornecedor, pasta Integrações | Tributos.  No cadastro da Filial, pasta Dados Adicionais. |
| 79.1 | E18a | IM | Inscrição Municipal do Tomador do Serviço | Campo opcional, pode ser informado na NF-e conjugada, com itens de produtos sujeitos ao ICMS e itens de serviços sujeitos ao ISSQN. | GFILIAL.INSCMUN OU FCFO.INSCRMUNICIPAL | Inscrição Municipal | Emissão própria, cadastro da filial, pasta Dados Adicionais.  Tomador Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
| 79a | E19 | email | Email | Campo pode ser utilizado para informar o e-mail de recepção da NF-e indicada pelo destinatário (v2.0). | FCFO.EMAIL ou GFILIAL.EMAIL | E-Mail | Cliente/Fornecedor, pasta Dados Gerais | aba Identificação. |
