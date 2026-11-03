---
content_hash: c35d3c6ad57bd2ec633159492a0ebd702ebd55f097fed66d43bd50655bb51b49
fetched_at: '2026-06-29T00:10:25.169119+00:00'
page_id: '501473448'
product: rm
source: tdn-rm
title: FISCAL01-9796 ER - EFD-REINF - Eventos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501473448
version: 111
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Fiscal |
| **Segmento Executor** | Backoffice | | |
| **Requisito/Story/Issue** | FISCAL01-9796 | **Subtarefa** | FISCAL01-10185 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Objetivo

 Detalhar as alterações necessárias no módulo TOTVS Gestão Fiscal para a implementação dos Eventos Periódicos R-2010 à R-2060 e R-5011 da EFD-REINF.

# Período dos Eventos Periódicos

De acordo com o manual da EFD-REINF o Evento R-5011 é o totalizador do período. Após o encerramento do período no ambiente da RFB este evento pode ser consultado para retornar os totalizadores calculados no ambiente da RFB com base nos Eventos transmitidos.

No TOTVS Gestão Fiscal iremos inverter a relação dos Eventos periódicos com o totalizador tornando o Evento R-5011 "pai" dos Eventos periódicos conforme abaixo.

truetruefalseEFD-REINF-PERIODOSfalse4433

Com esta mudança o R-5011 passa a ser utilizado como "Período dos Eventos Periódicos" e seus filhos serão os Eventos Periódicos.

Detalhes dos campos do R-5011:

* **Id. Evento Pai** deverá ser exibido um lookup para cadastro do Evento R-1000, mas não poderá ser editado;
* **Tipo:** será preenchido com o código do evento R-5011 e não deve ser editável;
* **Status:** deverá apresentar as opções abaixo e não ser editável.
  + Aberto: os Eventos Periódicos ainda podem ser inseridos
  + Encerrado: os Eventos Periódicos não podem ser inseridos
* **XML de Envio**: não deve ser exibido para este Evento

Ao acessar o menu "Eventos Periódicos" devem ser apresentados todos os Eventos R-5011 e o mesmo deverá disponibilizar um anexo com todos os Eventos Periódicos. Os processos de "Transmitir", "Consultar", "R-9000 Excluir" e "Gerar Eventos Periódicos" devem ser disponibilizados na lista de processos da visão do R-5011 e na lista de processos dos Eventos filhos permitindo a execução individual ou em lote. Ao ser acionado no R-5011 o processo será executado para todos os Eventos filhos obedecendo as regras de cada processo.

## Regras

* O Evento deverá ser mensal;
* Não podem existir mais de um Eventos por período;
* Ao ser cadastrado o Evento assumirá o status de "Aberto";
* O Cadastro poderá ser excluído somente se não existirem Eventos filhos com status diferente de "Não Transmitido", "Inconsistente" ou "Rejeitado".

# Processos

Os processos "R-2098 Reabertura dos Eventos Periódicos", "R-2099 Fechamento dos Eventos Periódicos" e "R-5011 Consultar Totalizador" são de controle do Evento R-5011 e devem se disponibilizados somente na lista de processos da visão do R-5011.

## R-5011 Consultar Totalizador

Ao executar o processo "R-5011 Consultar Totalizador" o sistema deverá consultar junto a RFB o evento R-5011, gravar os dados de retorno.

### Regras

* Antes de executar o encerramento é necessário ter autorizado o Evento R-2099 Fechamento dos Eventos Periódicos;
* O processo só pode ser executado para Períodos com Status "Encerrado".

Os processos "R-2098 Reabertura dos Eventos Periódicos" e "R-2099 Fechamento dos Eventos Periódicos" serão detalhados em especificação própria.

# Eventos Periódicos

Serão tratados neste tópico os Eventos periódicos R-2010 à R-2060.

* **Id. Evento Pai** deverá ser exibido um lookup para cadastro do Evento R-5011, mas não poderá ser editado;
* **Tipo:** será preenchido com o código do Evento Periódico em questão (R-2010, R-2020 etc.) e não deve ser editável.

## Gerar Eventos Periódicos

Deverá ser criado o processo "Gerar Eventos Periódicos" no qual os Eventos Periódicos serão incluídos conforme sua origem deixando-os no ponto de transmissão. Este processo será executado automaticamente ao encerrar o Período de Apuração dos tributos envolvidos na EFD-REINF (INSS, FUNRURAL e CPRB) ou de forma manual através de um processo na tela de cadastro do Período de Eventos Periódicos (R-5011). Além disso o processo deve ser criado com possibilidade de agendamento através de job, portanto o processo precisa ser capaz de identificar os Eventos 5011 em aberto e criar os Eventos de forma autônoma.

### Alteração

Internamente o processo "Gerar Eventos Periódicos" também deverá atualizar Eventos já criados comparando a data do status do mesmo com a data do log de alteração no cadastro de origem ou novas origens relacionadas ao mesmo Evento (conforme regra definida para cada Evento). No caso de um Evento com status “Não Transmitido” ou "Alterado" basta atualizar os dados do mesmo sem a necessidade de registrar histórico. No caso do Evento já ter sido autorizado o Status deverá ser modificado para "Alterado" e seus dados atualizados na íntegra, ou seja com base em todas as origens relacionas a este Evento.

## Exclusão de cadastro

Somente os Eventos com status "Não Transmitido", "Inconsistente" e "Rejeitado" podem ser excluídos;

## Regras

* Um Evento com Status "Excluído" deverá ser desprezado para fins de atualização, mas sua origem ainda será considerada para inclusão.

# Anexo Origem dos dados

Os eventos periódicos serão gerados com base em cadastros do BackOffice conforme abaixo. Cada evento deverá disponibilizar através de anexo uma consulta das origens relacionadas ao evento.

## Lançamentos Fiscais

Para os Eventos cuja a Origem é o Lançamento Fiscal deverá ser adicionar um Anexo "Lançamentos Fiscais" e nele devem ser apresentados os campos

* Id Laf;
* Série;
* Número do Documento;
* Cliente/Fornecedor;
* Código da Filial do Lançamento;
* Data de emissão;
* Data de Entrada/Saída.

### Eventos com Origem Lançamento Fiscal são:

* R-2010 – Retenção Contribuição Previdenciária - Serviços Tomados;
* R-2020 – Retenção Contribuição Previdenciária - Serviços Prestados;
* R-2050 – Comercialização da Produção por.. Produtor Rural PJ/Agroindústria;

**Origem Período de apuração:**

* R-2060 – Contribuição Previdenciária sobre a Receita Bruta – CPRB.

## Movimentos

Para os Eventos cuja a Origem é o Movimento deverá ser adicionar um Anexo "Movimentos" e nele devem ser apresentados os campos

* Id Mov;
* Série;
* Número do Documento;
* Cliente/Fornecedor;
* Código da Filial do Movimento;
* Data de emissão;
* Data de Entrada/Saída.

### Eventos com Origem Movimento

* R-2030 – Recursos Recebidos por Associação Desportiva;
* R-2040 – Recursos Repassados p/ Associação Desportiva.

## Estrutura de Tabelas para as origens

truetruefalseEFD-REINF-Relac-Origemfalse4024

### Tabela de Relacionamento entre Lançamento e Evento

Sugestão de nome: DEVENTOREINFLANC

* **Cód. Coligada:** Código da Coligada
* **IdLaf:** Identificador do Lançamento
* **IdEvento:** Identificador do Evento

**Foreign key:** Cód. Coligada - FK com a tabela de coligada, IdEvento - FK com a tabela de Evento, IdLaf - FK com a tabela de Lançamento.

### Tabela de Relacionamento entre Movimento e Evento

Sugestão de nome: DEVENTOREINFMOV

* **Cód. Coligada:** Código da Coligada
* **IdMov:** Identificador do Movimento
* **IdEvento:** Identificador do Evento

**Foreign key:** Cód. Coligada - FK com a tabela de coligada, IdEvento - FK com a tabela de Evento, IdMov - FK com a tabela de Movimento.

# Layout dos Eventos Periódicos

false3left0R-2010

**Retenção Contribuição Previdenciária - Serviços Tomados**

Para geração desse evento devem ser selecionados os lançamentos fiscais de entrada que possuem retenção do INSS.

xmlExemplo R-2010


{...}
{...}

{...}
]]>

## Regra

* O Evento deve agrupar todos os lançamentos do período por cliente fornecedor.
1R-2020

**Retenção Contribuição Previdenciária - Serviços Prestados**

Para geração desse evento devem ser selecionados os lançamentos fiscais de saída que possuem o Tributo INSS informado para retenção pelo contratante.

xmlExemplo R-2020


{...}
{...}

{...}
]]>

## Regra

* O Evento deve agrupar todos os lançamentos do período por cliente fornecedor.
2R-2030

**Recursos Recebidos por Associação Desportiva**

A origem dessas informações é um serviço criado pela Módulo de Materiais uma vez que não há documento fiscal envolvido (verificar o nome do serviço através do processo que gera os dados para o TAF).

xmlExemplo R-2030


{...}

5
str1234
{...}
]]>

## Regra

* O Evento deve agrupar todos os lançamentos do período por cliente fornecedor.

ideContri

Utiliza um grupo **ideEstab** específico para este tipo

## ideEstab

xmlideEstab
5
str1234
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpInscEstab | Preenchimento de acordo com o campo abaixo |
| nrInscEstab | GFILIAL.CGC |

3R-2040

**Recursos Repassados para Associação Desportiva**

A origem dessas informações é um serviço criado pelo Módulo de Materiais uma vez que não há documento fiscal envolvido (verificar o nome do serviço através do processo que gera os dados para o TAF).

xmlExemplo R-2040


{...}

5
str12340
{...}
]]>

## Regra

* O Evento deve agrupar todos os lançamentos do período por cliente fornecedor.

ideContri

Utiliza um grupo **ideEstab** específico para este tipo

## ideEstab

xmlideEstab
5
str1234
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpInscEstab | Preenchimento de acordo com o campo abaixo |
| nrInscEstab | GFILIAL.CGC |

4R-2050

**Comercialização da Produção por Produtor Rural PJ/Agroindústria**

Para geração desse evento devem ser selecionados os lançamentos fiscais de saída que possuem o Tributo Funrural informado.

xmlExemplo R-2050


{...}
{...}

{...}
]]>

Regra

* O Evento deve agrupar todos os lançamentos do período por filial.

ideContri

Utiliza um grupo **ideEstab** especifico para este tipo

## ideEstab

xmlideEstab
5
str1234
str1234
str1234
str1234
str1234
str1234
str1234
str1234
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpInscEstab | Preenchimento de acordo com o campo abaixo |
| nrInscEstab | GFILIAL.CGC |
| vlrRecBrutaTotal | Totalizador da receita bruta informada no registro {tipoCom} |
| vlrCPApur | Somatório do campo DTRBITEM.VALORTRB do todos os lançamentos com o tributo  para a Filial |
| vlrRatApur | Somatório do campo DTRBITEMCALCCONTRPREV.VALORCONTGILRAT de todos os lançamentos com o tributo para a Filial |
| vlrSenarApur | Somatório do campo DTRBITEMCALCCONTRPREV.VALORCONTSENAR de todos os lançamentos com o tributo para a Filial |
| vlrCPSuspTotal | Totalizador do Funrural suspenso informada no registro {infoProc} |
| vlrRatSuspTotal | Totalizador do Gilrat suspenso informada no registro {infoProc} |
| vlrSenarSuspTotal | Totalizador do Senar suspenso informada no registro {infoProc} |

5R-2060

**Contribuição Previdenciária sobre a Receita Bruta - CPRB**

  
Para geração desse evento deverá ser realizada a apuração da contribuição previdenciária, o evento será gerado com os valores do período de apuração.xmlExemplo R-2060


{...}
{...}

{...}
]]>

Regra

* O Evento deve agrupar todos os lançamentos do período por cliente fornecedor.

ideContri

Utiliza um grupo **ideEstab** especifico para este tipo

## ideEstab

xmlideEstab
123
str1234
str1234
str1234
str1234
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpInscEstab | Preenchimento de acordo com o campo abaixo |
| nrInscEstab | GFILIAL.CGC |
| vlrRecBrutaTotal | DPERIODO.VLRRECEITAFINANCEIRA |
| vlrCPApurTotal | Somatório dos grupos "filhos" |
| vlrCPRBSuspTotal | Não aderência |

## Origem dos dados

Abaixo seguem as estruturas e o mapeamento das origens campo a campo.

falseinfoCadastroleft0ideEstabObra

## Identificação do Estabelecimento/obra contratante dos Serviços

xmlideEstabObra
5
str1234
5
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpInscEstab | Gerado de acordo com o campo {nrInscEstab} |
| nrInscEstab | MPRJ.CNOPRJ |
| indObra | MPRJ.INDPRESTSRV |

1idePrestServ

## Identificação do prestador de serviços mediante cessão de mão de obra ou empreitada.

xmlidePrestServ
str1234
str1234
str1234
str1234
str1234
str1234
str1234
5
{...}
{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| cnpjPrestador | FCFO.CGCCFO |
| vlrTotalBruto | Somatório do valor bruto de todos os lançamentos fiscais do mesmo fornecedor. |
| vlrTotalBaseRet | Somatório da base de cálculo do INSS de todos os lançamentos fiscais do mesmo fornecedor. |
| vlrTotalRetPrinc | Somatório dos valores de todos os lançamentos fiscais do mesmo fornecedor. |
| vlrTotalRetAdic | Somatório dos valores de todos os lançamentos fiscais do mesmo fornecedor. |
| vlrTotalNRetPrinc | Somatório dos valores de todos os lançamentos fiscais do mesmo fornecedor. |
| vlrTotalNRetAdic | Somatório dos valores de todos os lançamentos fiscais do mesmo fornecedor. |
| indCPRB | Verificar a alíquota do Tributo INSS: - Se for 11%, gera o campo com "0" - Se for 3,5 % gera o campo com "1" |

2nfs

## Notas Fiscais

xmlnfs
str12
str1234
2012-12-13
str1234
str1234
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| serie | DLAF.SERIEDOC |
| numDocto | DLAF.DOCINI |
| dtEmissaoNF | DLAF.DATAEMISSAO |
| vlrBruto | Somatório do valor mercadoria de todos os itens do lançamento. |
| obs | DHISTLAF.OBSERVACAO |

4infoTpServ

## Informações sobre os tipos de Serviços constantes da NF

xmlinfoTpServ
str123400
str1234
str1234
str1234
str1234
str1234
str1234
str1234
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpServico | TPRDFISCAL.CLASSIFSERVICO |
| vlrBaseRet | DTRBITEM.BASETRB |
| vlrRetencao | DTRBITEMCALCCONTRPREV.VALORRETENCAO |
| vlrRetSub | DTRBITEMCALCCONTRPREV.VLRRETSERVSUBCONT |
| vlrNRetPrinc | DTRBITEMCALCCONTRPREV.VLRRETSUSPDEPJUIZO |
| vlrServicos15 | DTRBITEMCALCCONTRPREV.VLRSERVPREST15ANOS |
| vlrServicos20 | DTRBITEMCALCCONTRPREV.VLRSERVPREST20ANOS |
| vlrServicos25 | DTRBITEMCALCCONTRPREV.VLRSERVPREST25ANOS |
| vlrAdicional | DTRBITEMCALCCONTRPREV.VLRRETADIC15ANOS +  DTRBITEMCALCCONTRPREV.VLRRETADIC20ANOS +  DTRBITEMCALCCONTRPREV.VLRRETADIC25ANOS |
| vlrNRetAdic | DTRBITEMCALCCONTRPREV.VLRRETADICSUSPDEPJUIZO |

5infoProcRetPr

## Informações de processo

Gerar um registro para cada Processo Jud/Admin associado aos lançamentos fiscais do Cliente/Fornecedor relacionado no registro anterior que esteja sendo discutido o valor principal do tributo ou ambos, conforme especificação (2.1.2, "f", iii).

xmlinfoProcRetPr
5
str1234
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpProcRetPrinc | DPROCESSOJUDICIAL.TIPOPROCESSO |
| nrProcRetPrinc | DPROCESSOJUDICIAL.NUMERO |
| codSuspPrinc | DTRIBDISCUTIDOSPROCJUDICIAL.IDTRIBDISCUTIDOS |
| valorPrinc | Somatório do campo  DTRBITEMCALCCONTRPREV.VLRRETSUSPDEPJUIZO de todos os lançamentos fiscais que possuem o processo associado. |

6infoProcRetAd

## Informações de processo

Dados do Cliente/Fornecedor associado ao lançamento fiscal da retenção e do próprio lançamento. Este grupo totaliza os valores das notas fiscais informadas no Grupo {nfs} por CNPJ/CNO do prestador.

Gerar um registro para cada Processo Jud/Admin associado aos lançamentos fiscais do cli/for relacionado no registro anterior que esteja sendo discutido o valor adicional do tributo ou ambos, conforme especificação (2.1.2, "g", iii).

xmlinfoProcRetAd
5
str1234
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpProcRetAdic | DPROCESSOJUDICIAL.TIPOPROCESSO |
| nrProcRetAdic | DPROCESSOJUDICIAL.NUMERO |
| codSuspAdic | DTRIBDISCUTIDOSPROCJUDICIAL.IDTRIBDISCUTIDOS |
| valorAdic | Somatório do campo  DTRBITEMCALCCONTRPREV.VLRRETADICSUSPDEPJUIZO de todos os lançamentos fiscais que possuem o processo associado. |

7ideEstabPrest

## Registro que identifica o estabelecimento "prestador" de serviços mediante cessão de mão de obra

xmlideEstabPrest
123
str1234
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpInscEstabPrest | Valor fixo "1" gerado pelo sistema. |
| nrInscEstabPrest | GFILIAL.CGC |

8ideTomador

## Identificação dos tomadores dos serviços

Dados do Cliente/Fornecedor associado ao lançamento fiscal da retenção e do próprio lançamento. Este grupo totaliza os valores das notas fiscais informadas no Grupo {nfs} por CNPJ/CNO do prestador

xmlideTomador
5
str1234
5
str1234
str1234
str1234
str1234
str1234
str1234
{...}
{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpInscTomador | Preenchimento de acordo com o campo abaixo |
| nrInscTomador | MPRJ.CNOPRJ |
| indObra | MPRJ.INDPRESTSRV |
| vlrTotalBruto | Somatório do valor bruto de todos os lançamentos fiscais emitidos para o mesmo cliente. |
| vlrTotalBaseRet | Somatório da base de cálculo do INSS de todos os lançamentos fiscais emitidos para o mesmo cliente. |
| vlrTotalRetPrinc | Somatório dos valores de todos os lançamentos fiscais emitidos para o mesmo cliente. |
| vlrTotalRetAdic | Somatório dos valores de todos os lançamentos fiscais emitidos para o mesmo cliente. |
| vlrTotalNRetPrinc | Somatório dos valores de todos os lançamentos fiscais emitidos para o mesmo cliente. |
| vlrTotalNRetAdic | Somatório dos valores de todos os lançamentos fiscais emitidos para o mesmo cliente. |

10recursosRec

## Recursos recebidos por associação desportiva que mantenha equipe de futebol profissional

xmlrecursosRec
str1234
str1234
str1234
str1234
{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| cnpjOrigRecurso | FCFO.CGCCFO |
| vlrTotalRec | Somatório dos registros filhos. |
| vlrTotalRet | Somatório dos registros filhos. |
| vlrTotalNRet | Somatório dos registros filhos. |

11infoRecurso

## Detalhamento dos recursos recebidos

xmlinfoRecurso
5
str1234
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpRepasse | Essas informações serão providas pela Gestão de Materiais através de serviço. |
| descRecurso | Essas informações serão providas pela Gestão de Materiais através de serviço. |
| vlrBruto | Essas informações serão providas pela Gestão de Materiais através de serviço. |
| vlrRetApur | Essas informações serão providas pela Gestão de Materiais através de serviço. |

12infoProc

## Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte

xmlinfoProc
5
str1234
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpProc | DPROCESSOJUDICIAL.TIPOPROCESSO |
| nrProc | DPROCESSOJUDICIAL.NUMERO |
| codSusp | DTRIBDISCUTIDOSPROCJUDICIAL.IDTRIBDISCUTIDOS |
| vlrNRet | Somatório do campo  DTRBITEMCALCCONTRPREV.VLRRETADICSUSPDEPJUIZO de todos os lançamentos fiscais que possuem o processo associado. |

13recursosRep

## Recursos repassados para associação desportiva

xmlrecursosRep
str1234
str1234
str1234
str1234
{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| cnpjAssocDesp | FCFO.CGCCFO |
| vlrTotalRep | Somatório dos registros filhos. |
| vlrTotalRet | Somatório dos registros filhos. |
| vlrTotalNRet | Somatório dos registros filhos. |

14tipoCom

## Registro que apresenta o valor total da Receita Bruta por "tipo" de comercialização.

xmltipoCom
5
str1234
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| indCom | SE for uma operação para o exterior (CFOP 7xxx) ENTÃO o indicador será "9"  SENÃO  SE o campo FCFO.ENTIDADEEXECUTORAPAA do Cliente/Fornecedor estiver marcado ENTÃO o indicador será "8"  SENÃO o indicador será "1". |
| vlrRecBruta | Valor Líquido dos itens dos lançamentos selecionados. |

15tipoCod

## Registro que apresenta o valor total da receita por tipo de código de atividade econômica

As informações desse Grupo serão originadas da pasta "Contribuição Previdenciária" do Período de Apuração de cada uma das Filiais.

xmltipoCod
str12340
str1234
str1234
str1234
str1234
str1234
{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| codAtivEcon | DPERIODOCONTRIBPREV.CODATIVECONOMIC |
| vlrRecBrutaAtiv | DPERIODOCONTRIBPREV.BASECALCULO (VALORRECEITAS impedida pela validação\*) |
| vlrExcRecBruta | Não aderência |
| vlrAdicRecBruta | Não aderência |
| vlrBcCPRB \* | DPERIODOCONTRIBPREV.BASECALCULO |
| vlrCPRBapur | DPERIODOCONTRIBPREV.VALORCONTRIBUICAO |

* Validação: Deve ser igual a {vlrRecBrutaAtiv} + {vlrAdicRecBruta} - {vlrExcRecBruta}.
16tipoAjuste

## Tipo do ajuste da CPRB

Este grupo será gerado com os lançamentos de Outros Débitos/Créditos inseridos para o Tributo "Contribuição Previdenciária" no período.

xmltipoAjuste
5
1234
str1234
str1234
1999-05
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpAjuste | Se o lançamento for de Crédito, recebe valor “0”.  Se for do Tipo Débito recebe valor “1”. |
| codAjuste | Recebe o valor gravado no campo "Código Ajuste SPED" da tela de inclusão de Outros Débitos e Créditos. |
| vlrAjuste | Recebe o valor do lançamento de Outros Débitos/Créditos |
| descAjuste | Recebe o valor do campo Histórico do lançamentos de Outros Débitos/Créditos. |
| dtAjuste | Não aderência. |

As demais estruturas não destacadas irão seguir o padrão geral dos eventos

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
