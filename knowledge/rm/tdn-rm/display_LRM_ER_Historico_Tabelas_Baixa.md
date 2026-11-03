---
content_hash: 45e87f25a853e9ecdae81d5e9cd7db034d18b392b95bdc590e2c4c3640214971
fetched_at: '2026-06-29T00:06:25.646983+00:00'
page_id: '224442648'
product: rm
source: tdn-rm
title: ER_Historico_Tabelas_Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Historico_Tabelas_Baixa
version: 133
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS RM | **Módulo** | Gestão Financeira |
| **Segmento Executor** | Educacional | | |
| **Projeto** | PDR\_EDU\_CTB005-48 | **IRM** | PCREQ-4112 |
| **Requisito** | [PCREQ-9775](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9775 "PCREQ-9775") | **Subtarefa** | PDR\_EDU\_CTB005-49 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## Objetivo

Definir as regras para o controle de histórico de alteração das tabelas de baixa de lançamentos financeiros, consulta de posição financeira num determinado dia e funções de fórmula.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Histórico de Lançamentos | Alteração | Contas a pagar/receber -> Operações Financeiras -> Lançamentos -> Histórico de alterações | Visualização dos dados de histórico de baixa |
| Liberação de Período | Alteração | Utilitários -> Outros -> Liberação de Período | Apagar histórico de baixa quando da exclusão do lançamento na liberação. |
| Habilitação de Histórico de Alterações | Alteração | Utilitários -> Outros | Inclusão da carga de histórico para as tabelas de baixa |
| Funções de Fórmula | Alteração | Serviços Globais -> Administração -> Cadastros -> Fórmulas | Criadas funções de fórmula específicas para buscar dados do histórico de baixa. |

* Criado os campos "Tipo Baixa Pendente" (FLANHST.BAIXAPENDENTE) e "Valor Devolução" (FLANHST.VALORDEVOLUCAO), preenchidos com o valor do campo com o mesmo nome do registro na tabela de Lançamentos Financeiros (FLAN) ao criar registro de histórico de alteração de lançamento.
* Criado o valor *Reprovação Acordo* para o campo "Processo" (FLANHST.PROCESSO) que será usado no registro de histórico de lançamento criado ao ser executado o processo que reprova um acordo financeiro. Também criado o valor *Inclusão Acordo não Efetivado* a ser usado para o registro de histórico de lançamentos origem da geração de acordo cujo template está parametrizado para efetivar "Ao aprovar" ou "Pagamento da primeira parcela". Nesse caso os lançamentos origem tem o campo FLAN.BAIXAPENDENTE alterado para *Efetivação Acordo* para não permitir alterar ou executar processos sobre os mesmos até que a situação de efetivação do acordo mude.
* Criadas tabelas para armazenar histórico da baixa: Histórico de alteração da baixa do lançamento financeiro, Histórico de alteração dos valores de integração da baixa, Histórico de Rateio por Centro de Custo da Baixa, Histórico de Rateio por Departamento da Baixa e Histórico de Tributos da Baixa. Os registros serão criados quando for habilitado o controle de histórico e nos processos do sistema que já criam o histórico do lançamento. As mesmas serão visualizadas no anexo *Histórico de Lançamentos* da visão de lançamentos. Vide detalhes na especificação de requisitos no link *Outros* do tópico "Informações Gerais".
* No cálculo do valor líquido baseado na posição financeira (numa data específica) será alterada a lógica para buscar os valores baixados da tabela de histórico de baixa ao invés dos valores baixados da tabela de histórico de lançamento (campos terminados em BX, como por exemplo, FLANHST.VALORDESCONTOBX). Isso não irá afetar os valores finais já que os campos de valores baixados da tabela de histórico de lançamento contém o somatório dos valores correspondentes baixados presentes no histórico de baixa.
* Quando ocorrer a liberação de período também devem ser excluídos todos os registros das tabelas de histórico de baixa (FLANBAIXAHST, FLANBAIXAINTEGRACAOHST, FLANBAIXARATCCUHST, FLANBAIXARATDEPHST, FLANBAIXATRBHST) com*Data do Processo*(campo da FLANHST) anteriores ou iguais à data de liberação.
* Serão criadas novas funções de fórmula para trazer a posição financeira da baixa do lançamento numa data específica. Serão baseadas nos dados das tabelas de histórico com o registro selecionado como indicado no tópico “”.

  + TABLANBAIXAPF: Valor de um campo do item de baixa do lançamento numa determinada data. Tabela FLANBAIXAHST.
  + TABLANBAIXARATCCUPF: Valor de um campo do rateio por centro de custo do item de baixa do Lançamento numa determinada data. Tabela FLANBAIXARATCCUHST.
  + TABLANBAIXARATDEPPF: Valor de um campo do rateio por Departamento do item de baixa do lançamento numa determinada data. Tabela FLANBAIXARATDEPHST.
  + VALORTRBLANBAIXAPF: Valor do tributo do item de baixa do lançamento numa determinada data. Tabela FLANBAIXATRBHST.
  + VALORINTEGRACAOLANBAIXAPF: Valor para um campo de integração do item de baixa do lançamento numa determinada data. Tabela FLANBAIXAINTEGRACAOHST.

  As funções de fórmula acima, terão o mesmo conjunto de parâmetros de entrada da sua correspondente, que exibe os dados do estado atual do lançamento acrescentando somente o parâmetro de data da posição financeira desejada. O retorno será sempre sobre os dados das tabelas de histórico correspondente.

**Tabelas Utilizadas**

* FLANBAIXAHST– Histórico de alteração da baixa do lançamento financeiro
* FLANBAIXAINTEGRACAOHST– Histórico de alteração dos valores de integração da baixa
* FLANBAIXARATCCUHST - Histórico de Rateio por Centro de Custo da Baixa
* FLANBAIXARATDEPHST - Histórico de Rateio por Departamento da Baixa
* FLANBAIXATRBHST - Histórico de Tributos da Baixa

## Dicionário de Dados

**Arquivo ou Código do Script:** FLANBAIXAHST - Histórico de alteração da baixa do lançamento financeiro

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFLANBAIXAHST: CODCOLIGADA, IDHISTORICO, IDBAIXA |
| **02** | IX\_FLANBAIXAHST: CODCOLIGADA, IDLAN |

| Campo | Tipo | Tamanho | Descrição |
| --- | --- | --- | --- |
| CODCOLIGADA | DCODCOLIGADA |  | Código da Coligada |
| IDHISTORICO | Inteiro |  | Identificador do Histórico |
| IDLAN | Inteiro |  | Referência do Lançamento |
| IDBAIXA | Inteiro |  | Identificador da Baixa |
| CODCOLXCX | DCODCOLIGADANULL |  | Coligada Extrato |
| IDXCX | Inteiro |  | Identificador do Extrato |
| IDFORMAPAGTO | Inteiro |  | Identificador da Forma de Pagamento |
| CODCOLCXA | DCODCOLIGADANULL |  | Coligada da Conta Caixa |
| CODCXA | String | 10 | Conta Caixa |
| IDTRANSACAO | Inteiro |  | Identificador da Transação |
| DATABAIXA | Data/Hora |  | Data da Baixa |
| DATACANCELBAIXA | Data/Hora |  | Data de Cancelamento |
| DATACONTABILIZBX | Data/Hora |  | Data Contabilização |
| NUMCONTABILBX | String | 20 | Número Contábil |
| CODEVENTOBAIXA | SmallInt |  | Evento Contábil |
| VALORBAIXA | RMDVALOR4 |  | Valor Baixa |
| VALORORIGINAL | RMDVALOR4 |  | Valor Original |
| VALORDESCONTO | RMDVALOR4 |  | Valor Desconto |
| VALORJUROS | RMDVALOR4 |  | Valor Juros |
| VALORMULTA | RMDVALOR4 |  | Valor Multa |
| VALORCAP | RMDVALOR4 |  | Valor Capitalização |
| VALOROP1 | RMDVALOR4 |  | Valor Opcional 1 |
| VALOROP2 | RMDVALOR4 |  | Valor Opcional 2 |
| VALOROP3 | RMDVALOR4 |  | Valor Opcional 3 |
| VALOROP4 | RMDVALOR4 |  | Valor Opcional 4 |
| VALOROP5 | RMDVALOR4 |  | Valor Opcional 5 |
| VALOROP6 | RMDVALOR4 |  | Valor Opcional 6 |
| VALOROP7 | RMDVALOR4 |  | Valor Opcional 7 |
| VALOROP8 | RMDVALOR4 |  | Valor Opcional 8 |
| VALORINSS | RMDVALOR4 |  | Valor INSS |
| VALORIRRF | RMDVALOR4 |  | Valor IRRF |
| VALORSESTSENAT | RMDVALOR4 |  | Valor SESTSENAT |
| VALORDEVOLUCAO | RMDVALOR4 |  | Valor Devolução |
| VALORNOTACREDITO | RMDVALOR4 |  | Valor Nota Crédito |
| VALORNOTACREDITOADIANTAMENTO | RMDVALOR4 |  | Valor Crédito Adiantamento |
| VALORVINCULADO | RMDVALOR4 |  | Valor Vinculado |
| VALORJUROSVENDOR | RMDVALOR4 |  | Valor Juros Vendor |
| VALORRETENCOES | RMDVALOR4 |  | Valor Retenções |
| VALORPERDAFINANCEIRA | RMDVALOR4 |  | Valor Perda Financeira |
| VALORDESCONTOACORDO | RMDVALOR4 |  | Valor Desconto Acordo |
| VALORJUROSACORDO | RMDVALOR4 |  | Valor Juros Acordo |
| VALORACRESCIMOACORDO | RMDVALOR4 |  | Valor Acréscimo Acordo |
| COTACAOBAIXA | Numérico |  | Cotação da Moeda na Baixa |
| CODMOEDABAIXA | String | 10 | Moeda da Baixa |
| USUARIO | String | 20 | Usuário da Baixa |
| NUMEROCHEQUE | String | 20 | Número Cheque |
| IDOPERACAO | Inteiro |  | Identificador da Operação Contábil |
| TIPOBAIXA | Inteiro |  | Tipo Baixa |
| STATUS | Inteiro |  | Status |
| TIPOFORMAPAGTO | SmallInt |  | Tipo Forma de Pagamento |
| PAGREC | SmallInt |  | Pagar ou Receber |
| MODELOCONTABILIZACAO | SmallInt |  | Modelo Contabilização |
| DIFBAIXAPARCIAL | RMDVALOR4 |  | Diferença Baixa Parcial |
| CODTB1FLX | String | 25 | Tabela Opcional 1 |
| CODTB2FLX | String | 25 | Tabela Opcional 2 |
| CODTB3FLX | String | 25 | Tabela Opcional 3 |
| CODTB4FLX | String | 25 | Tabela Opcional 4 |
| CODTB5FLX | String | 25 | Tabela Opcional 5 |
| STATUSEXTRATO | SmallInt |  | Status Extrato |
| TIPORETORNOBANCARIO | Inteiro |  | Tipo Retorno Bancário |
| ORIGEMVALORDESCONTO | Inteiro |  | Origem Valor Desconto para cálculo do valor líquido |
| ORIGEMVALORJUROS | Inteiro |  | Origem Valor Juros para cálculo do valor líquido |
| ORIGEMVALORMULTA | Inteiro |  | Origem Valor Multa para cálculo do valor líquido |
| ORIGEMVALORCAP | Inteiro |  | Origem Valor Capitalização para cálculo do valor líquido |
| ORIGEMVALOROP1 | Inteiro |  | Origem Valor Opcional 1 para cálculo do valor líquido |
| ORIGEMVALOROP2 | Inteiro |  | Origem Valor Opcional 2 para cálculo do valor líquido |
| ORIGEMVALOROP3 | Inteiro |  | Origem Valor Opcional 3 para cálculo do valor líquido |
| ORIGEMVALOROP4 | Inteiro |  | Origem Valor Opcional 4 para cálculo do valor líquido |
| ORIGEMVALOROP5 | Inteiro |  | Origem Valor Opcional 5 para cálculo do valor líquido |
| ORIGEMVALOROP6 | Inteiro |  | Origem Valor Opcional 6 para cálculo do valor líquido |
| ORIGEMVALOROP7 | Inteiro |  | Origem Valor Opcional 7 para cálculo do valor líquido |
| ORIGEMVALOROP8 | Inteiro |  | Origem Valor Opcional 8 para cálculo do valor líquido |
| VALORDIFERENCA | RMDVALOR4 |  | Diferença Baixa Parcial |
| CAMPODIFERENCA | String | 30 | Campo utilizado para aplicar o valor da diferença |
| TIPODIFERENCA | Inteiro |  | Tipo de Diferença: 0 (Diferença a menor), 1 (Diferença a maior) |
| DATACHEQUE | Data/Hora |  | Data de emissão cheque |
| DATAVENCIMENTOLANCAMENTO | Data/Hora |  | Data de vencimento lançamento |
| STATUSCONTABIL | SmallInt |  | Status Contábil da Baixa |
| STATUSEXPORTACAO | SmallInt |  | Status da exportação |
| RECCREATEDBY | String | 50 | Usuário criador do registro |
| RECCREATEDON | Data/Hora |  | Data de criação do registro |
| RECMODIFIEDBY | String | 50 | Autor da última modificação no registro |
| RECMODIFIEDON | Data/Hora |  | Data da última modificação no registro |
| DATAOP1 | Data/Hora |  | Data Opcional 1 |
| DATAOP2 | Data/Hora |  | Data Opcional 2 |
| DATAOP3 | Data/Hora |  | Data Opcional 3 |
| DATAOP4 | Data/Hora |  | Data Opcional 4 |
| DATAOP5 | Data/Hora |  | Data Opcional 5 |
| CAMPOALFAOP1 | String | 100 | Campo Alfa Opcional 1 |
| CAMPOALFAOP2 | String | 100 | Campo Alfa Opcional 2 |
| CAMPOALFAOP3 | String | 100 | Campo Alfa Opcional 3 |
| CODFILIAL | Inteiro |  | Código da filial |
| CODCCUSTO | String | 25 | Código do centro de custo |
| CODDEPARTAMENTO | String | 25 | Código do departamento |

**Arquivo ou Código do Script:** FLANBAIXAINTEGRACAOHST - Histórico de alteração dos valores de integração da baixa

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFLANBAIXAINTEGRACAOHST: CODCOLIGADA, IDHISTORICO, IDBAIXA, IDCAMPO |
| **02** | IX\_FLANBAIXAINTEGRACAOHST: CODCOLIGADA, IDLAN |

| Campo | Tipo | Tamanho | Descrição |
| --- | --- | --- | --- |
| CODCOLIGADA | DCODCOLIGADA |  | Código da Coligada |
| IDHISTORICO | Inteiro |  | Identificador do Histórico |
| IDLAN | Inteiro |  | Referência do Lançamento |
| IDBAIXA | Inteiro |  | Identificador da Baixa |
| IDCAMPO | Inteiro |  | Identificador do Campo |
| VALOR | RMDValor4 |  | Valor |
| RECCREATEDBY | String | 50 | Usuário criador do registro |
| RECCREATEDON | Data/Hora |  | Data de criação do registro |
| RECMODIFIEDBY | String | 50 | Autor da última modificação no registro |
| RECMODIFIEDON | Data/Hora |  | Data da última modificação no registro |

**Arquivo ou Código do Script:** FLANBAIXARATCCUHST - Histórico de Rateio por Centro de Custo da Baixa

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFLANBAIXARATCCUHST: CODCOLIGADA, IDHISTORICO, IDRATCCU |
| **02** | IX\_FLANBAIXARATCCUHST: CODCOLIGADA, IDLAN |

| Campo | Tipo | Tamanho | Descrição |
| --- | --- | --- | --- |
| CODCOLIGADA | DCODCOLIGADA |  | Código da Coligada |
| IDHISTORICO | Inteiro |  | Identificador do Histórico |
| IDLAN | Inteiro |  | Referência do Lançamento |
| IDBAIXA | Inteiro |  | Identificador da Baixa |
| IDRATCCU | Inteiro |  | Identificador do Rateio |
| CODCCUSTO | String | 25 | Código do Centro de Custo |
| VALOR | RMDValor4 |  | Valor |
| PERCENTUAL | RMDValor4 |  | Percentual |
| CODCOLNATFINANCEIRA | DCODCOLIGADANULL |  | Coligada Natureza Financeira |
| CODNATFINANCEIRA | String | 40 | Código Natureza Financeira |
| IDPRJ | Inteiro |  | Identificador do Projeto |
| IDTRF | Inteiro |  | Identificador da Tarefa |
| CODTBGRUPOORC | String | 40 | Grupo Orçamentário |
| RECCREATEDBY | String | 50 | Usuário criador do registro |
| RECCREATEDON | Data/Hora |  | Data de criação do registro |
| RECMODIFIEDBY | String | 50 | Autor da última modificação no registro |
| RECMODIFIEDON | Data/Hora |  | Data da última modificação no registro |

**Arquivo ou Código do Script:** FLANBAIXARATDEPHST - Histórico de Rateio por Departamento da Baixa

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFLANBAIXARATDEPHST: CODCOLIGADA, IDHISTORICO, IDRATDEP |
| **02** | IX\_FLANBAIXARATCCUHST: CODCOLIGADA, IDLAN |

| Campo | Tipo | Tamanho | Descrição |
| --- | --- | --- | --- |
| CODCOLIGADA | DCODCOLIGADA |  | Código da Coligada |
| IDHISTORICO | Inteiro |  | Identificador do Histórico |
| IDLAN | Inteiro |  | Referência do Lançamento |
| IDBAIXA | Inteiro |  | Identificador da Baixa |
| IDRATDEP | Inteiro |  | Identificador do Rateio |
| CODFILIAL | Inteiro |  | Código da Filial |
| CODDEPARTAMENTO | String | 25 | Código do Departamento |
| VALOR | RMDValor4 |  | Valor |
| PERCENTUAL | RMDValor4 |  | Percentual |
| RECCREATEDBY | String | 50 | Usuário criador do registro |
| RECCREATEDON | Data/Hora |  | Data de criação do registro |
| RECMODIFIEDBY | String | 50 | Autor da última modificação no registro |
| RECMODIFIEDON | Data/Hora |  | Data da última modificação no registro |

**Arquivo ou Código do Script:** FLANBAIXATRBHST - Histórico de Tributos da Baixa

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFLANBAIXATRBHST: CODCOLIGADA, IDHISTORICO, IDBAIXA, CODTRB |
| **02** | IX\_FLANBAIXARATCCUHST: CODCOLIGADA, IDLAN |

| Campo | Tipo | Tamanho | Descrição |
| --- | --- | --- | --- |
| CODCOLIGADA | DCODCOLIGADA |  | Código da Coligada |
| IDHISTORICO | Inteiro |  | Identificador do Histórico |
| IDLAN | Inteiro |  | Referência do Lançamento |
| IDBAIXA | Inteiro |  | Identificador da Baixa |
| CODTRB | String | 10 | Código do Tributo |
| ALIQUOTA | RMDValor4 |  | Código da Filial |
| BASEDECALCULO | RMDValor4 |  | Base de Cálculo |
| VALOR | RMDValor4 |  | Valor |
| CODRETENCAO | String | 10 | Código de Retenção |
| RECCREATEDBY | String | 50 | Usuário criador do registro |
| RECCREATEDON | Data/Hora |  | Data de criação do registro |
| RECMODIFIEDBY | String | 50 | Autor da última modificação no registro |
| RECMODIFIEDON | Data/Hora |  | Data da última modificação no registro |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
