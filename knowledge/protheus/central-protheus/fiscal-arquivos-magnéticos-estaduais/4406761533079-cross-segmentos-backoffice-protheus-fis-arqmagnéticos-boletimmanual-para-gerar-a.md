---
article_id: 4406761533079
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 970f6aebca1ae2bfadfb3bd4fb690a0f6f8c7be3aefb99509da85e03ede7d041
fetched_at: '2026-06-28T22:42:10.263911+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Boletim/Manual
  para gerar arquivo DOT/GI-ICMS  de ES (DOTGIES) '
type: support-article
updated_at: '2022-08-17T19:28:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406761533079-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Boletim-Manual-para-gerar-arquivo-DOT-GI-ICMS-de-ES-DOTGIES
---

**Dúvida**Como gerar o arquivo **DOTGIES** - Declaração de Informações Tributáveis - ES

**Ambiente**  
TOTVS Backoffice (**Linha Protheus**) - A partir da versão **12.1.25.**  
  
**Solução**

**Atualizações do compatibilizador**

1. Criação de **Parâmetros** no arquivo **SX6 – Parâmetros**:

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_DOTMNEM |
| **Tipo** | Caracter |
| **Descrição** | Cód. Município Contribuinte – DOT/GI-ICMS |
| **Valor Padrão** | <código do município onde está localizado o contribuinte> |

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_DOTMNA1 |
| **Tipo** | Caracter |
| **Descrição** | Cód. Município SA1 – DOT/GI-ICMS |
| **Valor Padrão** | <campo da tabela SA1 que contém o código do município do cliente> |

Obs.: Conteúdo de parâmetro deve ser preenchido entre aspas. Exemplo: "A1\_MUNDOT" 

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_DOTMNA2 |
| **Tipo** | Caracter |
| **Descrição** | Cód. Município SA2 – DOT/GI-ICMS |
| **Valor Padrão** | <campo da tabela SA2 que contém o código do município do fornecedor> |

Obs.: Conteúdo de parâmetro deve ser preenchido entre aspas. Exemplo: "A2\_MUNDOT"

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| Nome | MV\_MUNDUE |
| Tipo | Caracter |
| Cont. Por. | <Definido pelo Cliente> |
| Descrição | Informe o campo para informar a UF|Cod. Municipio que sera utilizado . |

Este parâmetro deve ser preenchido com o campo da Tabela DUE em que será definido o município  de Inicio de Transporte.

Utilizado quando o campo “Selec.Origem (DTC\_SELORI)” esteja como “3-Local Coleta” e não possua Seq.Endereco (DT5\_SEQEND).

Caso não seja informado o sistema utilizará o campo DUE\_CODMUN por padrão, para localizar o município.

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| Nome | MV\_MUNDUL |
| Tipo | Caracter |
| Cont. Por. | <Definido pelo Cliente> |
| Descrição | Informe o campo para informar a UF|Cod. Municipio que sera utilizado . |

Este parâmetro deve ser preenchido com o campo da Tabela DUL em que será definido o município  de Inicio de Transporte.

Utilizado quando o campo “Selec.Origem (DTC\_SELORI)” esteja como “3-Local Coleta” e possua Seq.Endereco(DT5\_SEQEND).

Caso não seja informado o sistema utilizará o campo DUL\_CODMUN por padrão, para localizar o município.

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| Nome | MV\_SOLDT5 |
| Tipo | Caracter |
| Cont. Por. | <Definido pelo Cliente> |
| Descrição | Campo da tabela DT5 contendo o código+loja do solicitante da coleta. |

Este parâmetro deve ser preenchido com o campo da Tabela DT5, que deverá conter o código+loja do solicitante da coleta.

Utilizado quando o campo “Selec.Origem (DTC\_SELORI)” esteja como “3-Local Coleta” e possua Seq.Endereco(DT5\_SEQEND).

Caso não seja informado o sistema utilizará o campo DT5\_DDD+DT5\_TEL por padrão, para localizar o solicitante.

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| Nome | MV\_INTTMS |
| Tipo | Lógico |
| Cont. Por. | <Definido pelo Cliente> |
| Descrição | Identifica se o Modulo do TMS esta integrado aos  outros modulos. |

Este parâmetro deve ser preenchido com verdadeiro T ou falso F.

Caso não seja informado o sistema não utilizará as informações do modulo TMS, para a montagem do quadro B - detalhamento de transporte.

### Procedimentos para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Configurador (SIGACFG)** acesse **Ambientes/ Cadastros/ Parâmetros (CFGX017)**. Configure o(s) parâmetro(s) a seguir:

|  |  |
| --- | --- |
| Nome | MV\_DOTMNEM |
| Tipo | Caracter |
| Cont. Por. | <código do município onde está localizado o contribuinte> |
| Descrição | Cód. Município SA1 – DOT/GI-ICMS |

**Importante**

**O parâmetro MV\_ DOTMNEM deve ser configurado com o código do município do contribuinte, para que seja possível a geração do registro 2 (Principal). Caso o parâmetro tenha conteúdo ele terá prioridade sobre o campo M0\_CODMUN do cadastro de empresas.**

|  |  |
| --- | --- |
| Nome | MV\_DOTMNA1 |
| Tipo | Caracter |
| Cont. Por. | <campo da tabela SA1 que contém o código do município do cliente> |
| Descrição | Cód. Município SA1 – DOT/GI-ICMS |

Obs.: Conteúdo de parâmetro deve ser preenchido entre aspas. Exemplo: "A1\_MUNDOT"

**Importante**

O parâmetro **MV\_DOTMNA1** deve ser configurado com o nome do campo da tabela SA1 que contém o código do município do cliente, para que seja possível a geração dos registros 3 e 4. Será utilizado apenas para movimentações com o estado do Espírito Santo.

|  |  |
| --- | --- |
| Nome | MV\_DOTMNA2 |
| Tipo | Caracter |
| Cont. Por. | <campo da tabela SA2 que contém o código do município do cliente> |
| Descrição | Cód. Município SA2 – DOT/GI-ICMS |

Obs.: Conteúdo de parâmetro deve ser preenchido entre aspas. Exemplo: "A2\_MUNDOT"

**Importante**

O parâmetro **MV\_DOTMNA2** deve ser configurado com o nome do campo da tabela SA2 que contém o código do município do fornecedor, para que seja possível a geração dos registros 3 e 4. Será utilizado apenas para movimentações com o estado do Espírito Santo.

1. Criação de **Campos** no arquivo**SX3 – Campos****:**

* **Tabela SA1- Clientes**

|  |  |
| --- | --- |
| **Campo** | <campo a critério do cliente> |
| **Tipo** | Caracter |
| **Tamanho** | 5 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Cód. Munic. |
| **Descrição** | Código do Município |
| ***Help*** | Informar o código do município em que o cliente está situado. |

* **Tabela SA2- Fornecedores**

|  |  |
| --- | --- |
| **Campo** | <campo a critério do cliente> |
| **Tipo** | Caracter |
| **Tamanho** | 5 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Cód. Munic. |
| **Descrição** | Código do Município |
| ***Help*** | Informar o código do município em que o Fornecedor está situado. |

**Procedimentos para Utilização**

1. Copie o arquivo **DOTGIES**.INI para o diretório **\SYSTEM**
2. No ambiente **Livros Fiscais**, opção **Miscelânea/ Arquivos Magnéticos/ Instruções Normativas (MATA950)**, configure os parâmetros da rotina conforme instruções a seguir:

**Data Inicial ?**

Informe a data inicial para processamento da Instrução Normativa.

**Data Final ?**

Informe a data final para processamento da Instrução Normativa.

**Instr. Normativa ?**

Informe o nome da instrução normativa a ser processada: DOTGIES.

**Arq. Destino ?**

Informe o arquivo de destino em que serão geradas as informações: Exemplo: DOTGIES.XML

**Diretório. Destino ?**

Informe o nome do diretório em que será gravado o arquivo texto gerado a partir da apuração. Exemplo: C:\

**Seleciona Filiais ?** (disponível a partir da versão 8.11)

Informe se deseja selecionar as filias que serão processadas. Ao informar “**Não**”, apenas a filial corrente será considerada; ao informar “**Sim**”, o sistema apresenta uma tela para seleção das filiais a serem consideradas.

1. Confira os dados e **confirme.**
2. Serão apresentadas as perguntas específicas da DOT/GI-ES.
3. Clique no botão “**Avançar**”.
4. Serão apresentadas as perguntas específicas.

Forma de Apresentação:

Indique a forma de apresentação da declaração:

1 -     Normal, no prazo regulamentar: para declarações normais entregues dentro do prazo definido pela SEFA-ES.

2 -     Normal, fora do prazo regulamentar: para declarações normais entregues fora do prazo definido pela SEFA-ES.

3 -     Por substituição: para substituir uma declaração entregue anteriormente.

4 -     Por pedido de baixa de inscrição: para indicar o encerramento das atividades da empresa.

5 -     Por transferência de município: para indicar que no período a empresa transferiu-se para outro município.

6 -     Processar Valores em Estoque?

Escolha “1 - Sim” caso deseje inserir os valores em estoque. Essa pergunta foi criada devido ao fato de os valores em estoque somente serem exigidos quando há mudança de município ou a empresa é autuada a apresentar. Desta forma o valor default desta pergunta será sempre 2-NÃO.

Para a geração de Valores em Estoque, são consideradas as informações da tabela SB9 – Saldos Iniciais, campo **B9\_VINI1**  - Sld.Ini.Mes;

**Realiza Operações com Geração e Distribuição de energia elétrica, Prestação de Serviços de Transporte, Serviços de Comunicação, Extração de petróleo ou Serviço de tratamento e distribuição de água canalizada?**

Escolha Sim, quando realizar operações de Energia Elétrica, Serviços de Transporte, Serviços de Comunicação, Extração de Petróleo, Tratamento e Distribuição de agua e Outras Atividades.

                Deve ser escolhido Não quando não realizar essas operações.

1. Clique no botão “**Avançar**”.
2. Serão apresentadas os Campos para informar os CFOPs a serem considerados em cada situação

**Energia Elétrica/Geração:** Devem ser informados os CFOPs a serem considerados como Geração de Energia Elétrica.

**Energia Elétrica/Distribuição:** Devem ser informados os CFOPs a serem considerados como Distribuição de Energia Elétrica

**Serviços de Transporte:** Devem ser selecionados os CFOPs a serem considerados como Serviços de Transporte

**Serviços de Comunicação:** Devem ser selecionados os CFOPs a serem considerados como Serviços de Comunicação.

**Extração de Petróleo:** Devem ser selecionados os CFOPs a serem considerados como Extração de Petróleo

**Água Canalizada:**Devem ser selecionados os CFOPs a serem considerados como Água Canalizada.

**Outras Atividades:** Devem ser selecionados os CFOPs a serem considerados como Outras Atividades.

**Outras Atividades Transporte:** Devem ser selecionados os CFOPs a serem considerados como Outras Atividades de Transporte.

**Informações Complementares:** Devem ser informadas as informações Complementares.

**Não processar nas entradas:** Devem ser informadas os CFOPs de entrada a serem desconsiderados.

**Não processar nas saídas:** Devem ser informadas os CFOPs de saídas a serem desconsiderados.

Clique em “Finalizar” que o arquivo será gerado em formato de XML no caminho informado anteriormente.

**Informações Importantes**

O Quadro A destina-se à apuração do valor adicionado obedecendo ao critério “Resultado com Mercadorias”. Não poderão preencher este quadro os contribuintes que realizam operações com energia elétrica, serviços de transporte, distribuição de água canalizada e prestação de serviços exclusivamente de comunicação, cujas informações serão prestadas e detalhadas no Quadro B.

        O Quadro B destina-se à informação do valor total das operações de geração e distribuição de energia elétrica, prestação de serviços de transporte, prestação de serviços de comunicação, extração de petróleo, serviço de tratamento e distribuição de água canalizada, e outras atividades realizadas no ano base.

**Importante**

Desta forma, se a opção “*Realiza Operações com Geração e Distribuição de energia elétrica, Prestação de Serviços de Transporte, Serviços de Comunicação, Extração de petróleo ou Serviço de tratamento e distribuição de água canalizada?*”

escolhida for “Sim”, serão geradas as informações referente a Energia Elétrica, Serviços de Transporte, Serviços de Comunicação, Extração de Petróleo, Tratamento e Distribuição de agua e Outras Atividades. Se for escolhido “Não” serão geradas as demais informações.

O quadro C destina-se à informação do valor correspondente aos serviços de transporte contratados de pessoas físicas (transportadores autônomos) ou de empresas de transportes estabelecidas em outras unidades da federação nos quais o contribuinte contratante assume a responsabilidade pelo recolhimento do imposto devido.

O quadro D destina-se à prestação de informações complementares, nos casos em que as informações prestadas nos campos anteriores não sejam suficientes.

**Importante**

Para geração de cada tipo de Nota Fiscal é necessário verificar as condições descritas a seguir:

**1. Compras, transferências e devoluções do Estado:**

* O Estado da NF deve ser igual ao MV\_ESTADO.
* O CFOP utilizado deve ser iniciado por “1”.
* No cadastro de Fornecedor:
  + O campo Tp. Contr.Soc (SA2->A2\_TIPORUR) deve estar Vazio.
  + O Fornecedor não pode estar definido como Pessoa Física (Campo SA2->A2\_TIPO).
  + O Fornecedor tem que possuir Inscrição Estadual.

**2. Entrada de produção Rural própria:**

* O Estado da NF deve ser igual ao MV\_ESTADO.
* O CFOP utilizado deve ser iniciado por “1”.
* O Campo Tp. Contr.Soc (SA2->A2\_TIPORUR)  não pode estar Vazio.

**3. Compras de pessoa física ou não contribuinte de ICMS:**

* O Estado da NF deve ser igual ao MV\_ESTADO.
* O CFOP utilizado deve ser iniciado por “1”.
* O Campo Tp. Contr.Soc (SA2->A2\_TIPORUR) deve estar Vazio.

**4. Compras, Transferências e devoluções de outros Estados:**

* O Estado da NF deve ser diferente do MV\_ESTADO.
* O CFOP utilizado deve ser iniciado por “2”.

**5. Compras, Transferências e devoluções do exterior:**

* O Estado da NF deve ser diferente do MV\_ESTADO e definido como EX.
* O CFOP utilizado deve ser iniciado por “3”.

**6. Vendas, transferências e devoluções internas:**

* O Estado da NF deve ser igual ao MV\_ESTADO.
* O CFOP utilizado deve ser iniciado por “5”.

**7. Vendas, transferências e devoluções para outros estados:**

* O Estado da NF deve ser diferente do MV\_ESTADO.
* O CFOP utilizado deve ser iniciado por “6”.

**8. Vendas para o exterior**:

* O Estado da NF deve ser diferente do MV\_ESTADO e Igual a EX.

O CFOP utilizado deve ser iniciado por “7”.

**Informações Adicionais**

|  |  |
| --- | --- |
| **A quem se Destina** | Contribuintes do ICMS inscritos no Cadastro de Contribuintes - SEFA/ES. |
| **Objetivo** | Disciplinar a coleta de dados em meio magnético referente às operações tributáveis estaduais, interestaduais e do exterior. |
| **Prazo de Entrega** | Anual. As informações sobre as operações e prestações deverão compreender o período entre 1 de janeiro e 31 de dezembro, e deverão ser apresentadas do dia 1 até o dia 30 de junho do ano subsequente ao ano de referência. |
| **Competência** | Estadual – Espírito Santo. |
| **Aplicativo Disponibilizado pelo Fisco** | Sistema de Informações Tributárias - DOT/GI-ICMS |
| **Versão do Aplicativo Contemplado pela Totvs** | 3.0 |

**Informações Técnicas**

|  |  |
| --- | --- |
| **Tabelas Utilizadas** | SF3 – Livros FiscaisSA1 – Cadastro de ClientesSA2 – Cadastro de FornecedoresSB9 – Saldos Iniciais |
| **Rotinas Envolvidas** | MATA950 – Instrução Normativa |
| **Sistemas Operacionais** | Windows®/Linux® |

  
Arquivo **DOTGIES.INI** em anexo.
