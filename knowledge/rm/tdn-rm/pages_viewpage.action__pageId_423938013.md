---
content_hash: 8c607762f92f432a96f359b35683b2ad767895647985049b94df9b8357200c93
fetched_at: '2026-06-29T00:09:24.774988+00:00'
page_id: '423938013'
product: rm
source: tdn-rm
title: Importação Layout ANFAVEA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938013
version: 4
---

O processo de Importação Layout ANFAVEA importará movimentos no layout cedido pela Associação Nacional de Fabricantes de Veículos Automotores (ANFAVEA).   
 O layout ANFAVEA (montadoras) foi elaborado, juntamente com o Sindipeças (fornecedores), com o objetivo de padronizar a transação que complementa o Pedido de Compras entre Cliente e Fornecedor, explicitando prazos/quantidades para entrega/embarque da peça/material.   
 Para utilizar o processo de Importação Layout Anfavea é necessário incluir um novo conceito através do TOTVS Business Conector |  Conceito tecla CRTL + botão Incluir ou através do processo "Importar Conceito". Após a inclusão, edite o conceito e selecione o arquivo texto a ser importado através da opção "Importação Anfavea", botão Editar. Após salvar as configurações, selecione o conceito e execute Processar Novo Conceito, preencha o Código Anfavea e o Tipo de Movimento, e clique em "Executar".

|  |  |
| --- | --- |
| **Modelo Descritivo** | |
| ITP | Informações de início de transmissão. Não traz nenhuma informação essencial para o sistema. |
| PE1 | É o registro que indica a linha de dados do item. Essa linha traz, dentre outras informações, o código do produto no fabricante, que é a informação responsável pela identificação do item na base de dados. |
| PE2 | Esta linha de registro traz informações de entrega/embarque dos pedidos. |
| PE3 | Depois da linha do item é a linha mais importante. Ela traz a DATA, a HORA e a QUANTIDADE da entrega/embarque do item. |
| PE4 | Este registro traz os dados da embalagem. |
| TE1 | Esta linha é utilizada para informar um texto livre. |
| FTP | Informações de fim de transmissão. Não traz nenhuma informação essencial para o sistema. |

**LAYOUT DE IMPORTAÇÃO**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Linha ITP - INÍCIO DA TRANSMISSÃO** | | | | | |
| **DESCRIÇÃO DO CAMPO** | **TIPO** | **TAMANHO** | **DECIMAL** | **POSIÇÃO** | **UTILIZAÇÃO NO RM** |
| Identificação do Tipo de Registro | A | 3 | 0 | 001-003 | N/A |
| Identificação do Processo | N | 3 | 0 | 004-006 | N/A |
| Numero da Versão da Transação | N | 2 | 0 | 007-008 | N/A |
| Numero de Controle Transmissão | N | 5 | 0 | 009-013 | N/A |
| Identificação Geração do Movimento | N | 12 | 0 | 014-025 | Data de Emissão do Movimento (TMOV.DATAEMISSAO) e Data de Emissão do Item de Movimento (TITMMOV.DATAEMISSAO) |
| Identificação Transmissor na Comunicação | N | 14 | 0 | 026-039 | CNPJ do Cli/For: a partir desta informação será recuperado a Coligada e Código do Cliente Fornecedor para utilização no Movimento. (TMOV.CODCOLCFO e TMOV.CODCFO) |
| Identificação Receptor na Comunicação | A | 14 | 0 | 040-053 | CNPJ da Coligada. (GCOLIGADA.CGC) |
| Código Interno do Transmissor | A | 8 | 0 | 054-061 | N/A |
| Código Interno do Receptor | A | 8 | 0 | 062-069 | N/A |
| Nome do Transmissor | A | 25 | 0 | 070-094 | N/A |
| Nome do Receptor | A | 25 | 0 | 095-119 | N/A |
| Espaço | A | 9 | 0 | 120-128 | N/A |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Linha PE1 - DADOS DO ITEM** | | | | | |
| **DESCRIÇÃO DO CAMPO** | **TIPO** | **TAMANHO** | **DECIMAL** | **POSIÇÃO** | **UTILIZAÇÃO NO RM** |
| Identificação do Tipo de Registro | A | 3 | 0 | 001-003 | N/A |
| Código Fabrica de Destino | A | 3 | 0 | 004-006 | N/A |
| Identificação Programa Atual | A | 9 | 0 | 007-015 | N/A |
| Data do Programa Atual | N | 6 | 0 | 016-021 | N/A |
| Identificação. Programa Anterior | A | 9 | 0 | 022-030 | N/A |
| Data do Programa Anterior | N | 6 | 0 | 031-036 | N/A |
| Código item do Cliente | A | 30 | 0 | 037-066 | Campo para ser utilizado na consulta que retorna os dados do Produto. Pode ser o Número do Fabricante (TPRODUTODEF.NUMNOFABRIC) ou o Código do Produto (TPRODUTO.CODIGOPRD). |
| Código item do Fornecedor | A | 30 | 0 | 067-096 | N/A |
| Num. Do pedido de Compra | A | 12 | 0 | 097-108 | N/A |
| Código Local de Destino | A | 5 | 0 | 109-113 | N/A |
| Identificação para Contato | A | 11 | 0 | 114-124 | N/A |
| Código Unidade de Medida | A | 2 | 0 | 125-126 | N/A |
| Quantidade Casa Decimais | N | 1 | 0 | 127-127 | N/A |
| Código Tipo de Fornecimento | A | 1 | 0 | 128-128 | N/A |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Linha PE2 - INFORMAÇÕES DE ENTREGA / EMBARQUE** | | | | | |
| **DESCRIÇÃO DO CAMPO** | **TIPO** | **TAMANHO** | **DECIMAL** | **POSIÇÃO** | **UTILIZAÇÃO NO RM** |
| Identificação do Tipo de Registro | A | 3 | 0 | 001-003 | N/A |
| Data Ultima Entrega/Embarque | N | 6 | 0 | 004-009 | N/A |
| Numero Ultima Nota Fiscal | N | 6 | 0 | 010-015 | N/A |
| Série Ultima Nota Fiscal | A | 4 | 0 | 016-019 | N/A |
| Data Ultima Nota Fiscal | N | 6 | 0 | 020-025 | N/A |
| QTD Ultima Entrega/Embarque | N | 12 | 3 | 026-037 | N/A |
| QTD Entrega/Embarque Acumulada | N | 14 | 3 | 038-051 | Campo para ser utilizado na consulta que retorna os dados do Produto. Pode ser o Número do Fabricante (TPRODUTODEF.NUMNOFABRIC) ou o Código do Produto (TPRODUTO.CODIGOPRD). |
| QTD Necessária Acumulada | N | 14 | 3 | 052-065 | N/A |
| QTD Lote Mínimo | N | 12 | 3 | 066-077 | N/A |
| Código Frequência Fornecimento | A | 3 | 0 | 078-080 | N/A |
| Data Liberação p/ Produção | N | 4 | 0 | 081-084 | N/A |
| Data Liberação Matéria Prima | N | 4 | 0 | 085-088 | N/A |
| Código Local de Descarga | A | 7 | 0 | 089-095 | N/A |
| Período de Entrega/Embarque | A | 4 | 0 | 096-099 | N/A |
| Código Situação do Item | A | 2 | 0 | 100-101 | N/A |
| Identificação do Tipo de Programação | A | 1 | 0 | 102-102 | N/A |
| Pedido da Revenda | A | 13 | 0 | 103-115 | N/A |
| Qualificação da Programação | A | 1 | 0 | 116-116 | N/A |
| Espaço | A | 12 | 0 | 117-128 | N/A |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Linha PE3 - CRONOGRAMA DE ENTREGA** | | | | | |
| **DESCRIÇÃO DO CAMPO** | **TIPO** | **TAMANHO** | **DECIMAL** | **POSIÇÃO** | **UTILIZAÇÃO NO RM** |
| Identificação do Tipo de Registro | A | 3 | 0 | 001-003 | N/A |
| Data Entrega/Embarque do Item | N | 6 | 0 | 004-009 | Atualiza a informação de Data de Entrega do Movimento(TMOV.DATAENTREGA) e Data de Entrega do Item de Movimento(TITMMOV.DATAENTREGA). |
| Hora p/ Entrega/Embarque do Item | N | 2 | 0 | 010-011 | N/A |
| QTD de Entrega/Embarque do Item | N | 9 | 0 | 012-020 | Atualiza a informação de quantidade do item de movimento (TITMMOV.QUANTIDADE). |
| Data Entrega/Embarque do Item | N | 6 | 0 | 021-026 | Atualiza a informação de Data de Entrega do Movimento(TMOV.DATAENTREGA) e Data de Entrega do Item de Movimento(TITMMOV.DATAENTREGA). |
| Hora p/ Entrega/Embarque do Item | N | 2 | 0 | 027-028 | N/A |
| QTD de Entrega/Embarque do Item | N | 9 | 0 | 029-037 | Atualiza a informação de quantidade do item de movimento (TITMMOV.QUANTIDADE). |
| Data Entrega/Embarque do Item | N | 6 | 0 | 038-043 | Atualiza a informação de Data de Entrega do Movimento(TMOV.DATAENTREGA) e Data de Entrega do Item de Movimento(TITMMOV.DATAENTREGA). |
| Hora p/ Entrega/Embarque do Item | N | 2 | 0 | 044-045 | N/A |
| QTD de Entrega/Embarque do Item | N | 9 | 0 | 046-054 | Atualiza a informação de quantidade do item de movimento (TITMMOV.QUANTIDADE). |
| Data Entrega/Embarque do Item | N | 6 | 0 | 055-060 | Atualiza a informação de Data de Entrega do Movimento(TMOV.DATAENTREGA) e Data de Entrega do Item de Movimento(TITMMOV.DATAENTREGA). |
| Hora p/ Entrega/Embarque do Item | N | 2 | 0 | 061-062 | N/A |
| QTD de Entrega/Embarque do Item | N | 9 | 0 | 063-071 | Atualiza a informação de quantidade do item de movimento (TITMMOV.QUANTIDADE). |
| Data Entrega/Embarque do Item | N | 6 | 0 | 072-077 | Atualiza a informação de Data de Entrega do Movimento(TMOV.DATAENTREGA) e Data de Entrega do Item de Movimento(TITMMOV.DATAENTREGA). |
| Hora p/ Entrega/Embarque do Item | N | 2 | 0 | 078-079 | N/A |
| QTD de Entrega/Embarque do Item | N | 9 | 0 | 080-088 | Atualiza a informação de quantidade do item de movimento (TITMMOV.QUANTIDADE). |
| Data Entrega/Embarque do Item | A | 6 | 0 | 089-094 | Atualiza a informação de Data de Entrega do Movimento(TMOV.DATAENTREGA) e Data de Entrega do Item de Movimento(TITMMOV.DATAENTREGA). |
| Hora p/ Entrega/Embarque do Item | A | 2 | 0 | 095-096 | N/A |
| QTD de Entrega/Embarque do Item | A | 9 | 0 | 097-105 | Atualiza a informação de quantidade do item de movimento (TITMMOV.QUANTIDADE). |
| Data Entrega/Embarque do Item | A | 6 | 0 | 106-111 | Atualiza a informação de Data de Entrega do Movimento(TMOV.DATAENTREGA) e Data de Entrega do Item de Movimento(TITMMOV.DATAENTREGA). |
| Hora p/ Entrega/Embarque do Item | A | 2 | 0 | 112-113 | N/A |
| QTD de Entrega/Embarque do Item | A | 9 | 0 | 114-122 | Atualiza a informação de quantidade do item de movimento (TITMMOV.QUANTIDADE). |
| Espaço | A | 6 | 0 | 123-128 | N/A |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Linha PE4 - DADOS DA EMBALAGEM** | | | | | |
| **DESCRIÇÃO DO CAMPO** | **TIPO** | **TAMANHO** | **DECIMAL** | **POSIÇÃO** | **UTILIZAÇÃO NO RM** |
| Identificação do Tipo de Registro | A | 3 | 0 | 001-003 | N/A |
| Identificação Embalagem Secundaria Cliente | A | 30 | 0 | 004-033 | N/A |
| Identificação Embalagem Secundaria Fornecedor | A | 30 | 0 | 034-036 | N/A |
| Capacidade Embalagem Secundaria | N | 12 | 3 | 064-075 | N/A |
| Identificação Embalagem Primária Cliente | A | 30 | 0 | 076-105 | N/A |
| Identificação Embalagem Primária Fornecedor | N | 12 | 3 | 106-117 | N/A |
| Código Responsável P/ Embalagem | A | 1 | 0 | 118-118 | N/A |
| Espaço | A | 10 | 0 | 119-128 | N/A |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Linha TE1 – TEXTO LIVRE** | | | | | |
| **DESCRIÇÃO DO CAMPO** | **TIPO** | **TAMANHO** | **DECIMAL** | **POSIÇÃO** | **UTILIZAÇÃO NO RM** |
| Identificação do Tipo de Registro | A | 3 | 0 | 001-003 | N/A |
| Texto Livre Informativo | A | 40 | 0 | 004-043 | Atualiza a informação do histórico do movimento. (TMOVHISTORICO.HISTORICOCURTO ou TMOVHISTORICO.HISTORICOLONGO) |
| Texto Livre Informativo | A | 40 | 0 | 044-083 | Atualiza a informação do histórico do movimento. (TMOVHISTORICO.HISTORICOCURTO ou TMOVHISTORICO.HISTORICOLONGO) |
| Texto Livre Informativo | A | 17 | 2 | 084-123 | Atualiza a informação do histórico do movimento. (TMOVHISTORICO.HISTORICOCURTO ou TMOVHISTORICO.HISTORICOLONGO) |
| Espaço | A | 93 | 0 | 124-128 | N/A |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Linha FTP - TERMINO TRANSMISSÃO DE DADOS** | | | | | |
| **DESCRIÇÃO DO CAMPO** | **TIPO** | **TAMANHO** | **DECIMAL** | **POSIÇÃO** | **UTILIZAÇÃO NO RM** |
| Identificação do Tipo de Registro | A | 3 | 0 | 001-003 | N/A |
| Número de Controle Transmissão | N | 5 | 0 | 004-008 | N/A |
| Quantidade Registros na Transação | N | 9 | 0 | 009-017 | N/A |
| Numero Total de Valores | N | 17 | 2 | 018-034 | N/A |
| Categoria da Operação | A | 1 | 0 | 035-035 | N/A |
| Espaço | A | 93 | 0 | 036-128 | N/A |

***Observações***

* Há 2 possíveis Identificadores do Produto: Código do Produto, Número do Produto no Fabricante
* Apenas tipos de movimentos do grupo de pedidos de vendas (2.1) com numeração sequencial e local de emissão fixo estão disponíveis para importação.
* As linhas de registro PE1 e PE3 tem um nível de importância muito grande com relação as demais linhas do layout. Grande parte das informações necessárias para a importação se encontra nessas linhas.
* Quando existir o mesmo produto com mesma data de entrega(Linha PE3) será considerado a quantidade do último item. *Exemplo: 3 itens na linha PE3 onde as datas de entrega e quantidade são:**Item 1: data de entrega 12/01/2014 e quantidade 300.**Item 2: data de entrega 12/01/2014 e quantidade 400.**Item 3: data de entrega 12/01/2014 e quantidade 500.* Nesse caso será considerada a quantidade de 500 para a inclusão do item no movimento.

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.
