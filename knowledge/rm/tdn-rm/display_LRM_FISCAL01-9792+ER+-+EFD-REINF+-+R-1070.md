---
content_hash: 5304dd4c340ae912ee47323b4103a399a1c64b4a2ff129a118693f08a707d05e
fetched_at: '2026-06-29T00:10:25.060280+00:00'
page_id: '501458074'
product: rm
source: tdn-rm
title: FISCAL01-9792 ER - EFD-REINF - R-1070
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-9792+ER+-+EFD-REINF+-+R-1070
version: 80
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Fiscal |
| **Segmento Executor** | Backoffice | | |
| **Requisito/Story/Issue** | FISCAL01-9792 | **Subtarefa** | FISCAL01-10115 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Objetivo

 Detalhar as alterações necessárias no modulo TOTVS Gestão Fiscal para a implementação do Evento Cadastral R-1070 da EFD-REINF

# Cadastro

O Evento R-1070 será um anexo ao Evento R-1000. A inclusão do registro R-1070 será realizada conforme a estrutura padrão dos eventos da EFD-REINF, porém com os detalhes abaixo.

* **Id. Evento Pai** deverá ser exibido um lookup para cadastro do Evento R-1000, mas não poderá ser editado;
* **Tipo:** será preenchido com o código do evento R-1070 e não deve ser editável;
* **Id. Processo:** deverá ser exibido um lookup para o cadastro de processo.

## Validações

* Cada Evento poderá ter somente um processo associado;
* O campo **Id. Processo** só poderá ser editado quando o Evento estiver com o Status "Não Transmitido", "Inconsistente" ou "Rejeitado";
* Os campos **Início do Período** e **Fim do Período** devem estar compreendidos no inicio e fim do período do R-1000 associado.

# Estrutura de Tabelas

Deverá ser criado na tabela de Eventos o campo **Id. Processo:** Identificador do processo associado. Este campo será preenchido somente no Registro R1070 e portanto deverá ser visível somente para este Evento.

truetruefalseEFD-REINF Evento campo Id Processofalse1621

**Foreign key:** Id. Processo - FK com a tabela de cadastro de Processos.  
**Campos Nullable:** Id. Processo

# Layout do Evento

O xml do Evento deverá ser gerado conforme abaixo.

xmlExemplo R-1000


{...}
{...}

{...}
{...}
{...}
]]>

No grupo infoProcesso poderá ter apenas um dos seguinte Grupos

falseinfoContrileft0inclusaoxmlinclusao
{...}
]]>1alteracaoxmlalteracao
{...}
{...}
]]>2exclusaoxmlexclusao
{...}
]]>

## Origem dos dados

Este evento será gerado com base no Cadastro de Processo e todos os campos envolvidos precisam de controle de alteração (semelhante ao log da Filial). Sempre que estes campos forem atualizados e o Evento já estiver autorizado o status do registro R-1070 será modificado para “Alterado”.

falseinfoCadastroleft0ideProcesso

## ideProcesso

xmlideProcesso
5
str1234
1999-05
1999-05
5
{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpProc | DPROCESSOJUDICIAL.TIPOPROCESSO |
| nrProc | DPROCESSOJUDICIAL.NUMERO |
| iniValid | Campo "Início do Período" do Cadastro do Evento |
| fimValid | Campo "Fim do Período"  do Cadastro do Evento |
| indAutoria | DPROCESSOJUDICIAL.TERCEIRO Se este campo estiver marcado, então preencher este campo com "2". |

1infoSusp

## infoSusp

xmlinfoSusp
str1234
str1234
2012-12-13
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| codSusp | DTRIBDISCUTIDOSPROCJUDICIAL.IDTRIBDISCUTIDOS |
| indSusp | DTRIBDISCUTIDOSPROCJUDICIAL.CODINDICSUSPEXIG |
| dtDecisao | DTRIBDISCUTIDOSPROCJUDICIAL.DATADECISAO |
| indDeposito | DTRIBDISCUTIDOSPROCJUDICIAL.CODINDICDEPMONT |

2dadosProcJud

## dadosProcJud

xmldadosProcJud
st
str1234
str1
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| ufVara | DPROCESSOJUDICIAL.CODETD |
| codMunic | DPROCESSOJUDICIAL.CODMUNICIPIO |
| idVara | DPROCESSOJUDICIAL.VARA |

As demais estruturas não destacadas irão seguir o padrão geral dos eventos

# Log do Cadastro de Processos

O campo **Vara** precisa registrar log de alteração no cadastro de processo.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
