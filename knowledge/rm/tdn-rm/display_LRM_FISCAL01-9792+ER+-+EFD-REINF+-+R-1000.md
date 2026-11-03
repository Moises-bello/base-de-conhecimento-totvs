---
content_hash: 45cf005b362db8f33dd5d7853d77f9737c924856a13c29ff45aac236a2132ed5
fetched_at: '2026-06-29T00:10:25.014279+00:00'
page_id: '501123918'
product: rm
source: tdn-rm
title: FISCAL01-9792 ER - EFD-REINF - R-1000
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-9792+ER+-+EFD-REINF+-+R-1000
version: 116
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

 Detalhar as alterações necessárias no modulo TOTVS Gestão Fiscal para a implementação do Evento Cadastral R-1000 da EFD-REINF

# Cadastro

Ao acessar o menu EFD-REINF → “Eventos Cadastrais” devem ser listados todos os Eventos do tipo R-1000. O cadastro poderá ser acionado somente pela Filial Matriz ou Filial SCP. Os campos seguirão o padrão de estrutura definidos para os Eventos da EFD-REINF.

A inclusão do registro R-1000 será realizada conforme a estrutura padrão dos eventos da EFD-REINF, porém com os detalhes abaixo.

* **Id. Evento Pai** não deve ser visível;
* **Tipo:** será preenchido com o código do evento R-1000 e não deve ser editável;
* **Início do Período:**deverá ser informado a data de início da vigência da EFD-REINF ou deste Evento;
* **Código da Filial:** não deve ser editável.

## Validações

* Não pode ser incluído um Evento R-1000 enquanto existir outro R-1000 não encerrado, ou seja com a data de fim de período preenchida;
* Não pode existir mais de um R-1000 para o mesmo período, ou seja o inicio do novo R-1000 deverá ser posterior ao fim do período do último R-1000;
* Apenas o R-1000 mais recente pode ser alterado.

# Dados do Responsável pelo Software

Para o Evento R-1000 é necessário informar dados do responsável pelo software no grupo softHouse do XML para isso deverá ser criado um cadastro conforme abaixo.

## Mashup

Deverá ser criado através dos mashup da TOTVS um cadastro para informar os dados do responsável pelo software com os seguintes campos:

* CNPJ da empresa desenvolvedora do software;
* Razão Social da empresa desenvolvedora do software;
* Nome do contato na empresa;
* Informar o número do telefone, com DDD;
* Endereço eletrônico (e-mail);
* Versão minima da EFD-REINF;
* Versão minima do Release.

## Estrutura no ERP

Deverá ser criada uma tabela no ERP para armazenar os dados sincronizados com o mashups da TOTVS contendo os mesmos campos do cadastro no mashups e mais um campo de controle para evitar manutenções indevidas no cadastro. Sugiro utilizar o mesmo nome de tabela utilizado no mashups. Além disso é necessário criar um processo de sincronismos com os dados do mashups na tela da EFD-REINF. O processo funcionará de forma semelhante aos processo integrados com o mashup já existente no fiscal. Apenas a alteração deste dados não deve interferir no status do Eventos já transmitidos, contudo terá efeito para todas as novas transmissões.

# Layout do Evento

O xml do Evento deverá ser gerado conforme abaixo.

xmlExemplo R-1000


{...}
{...}

{...}
{...}
{...}
]]>

No grupo infoContri poderá ter apenas um dos seguinte Grupos

falseinfoContrileft0inclusaoxmlinclusao
{..}
{...}
]]>1alteracaoxmlalteracao
{..}
{...}
{...}
]]>2exclusaoxmlexclusao
{...}
]]>

## Origem dos dados

Este evento será gerado com base no cadastro da Filial e todos os campos envolvido precisam do controle de alteração do log da filial. Sempre que estes campos forem atualizados  e o Evento já estiver autorizado o status do registro R-1000 em vigência deverá ser modificado para “Alterado”.

falseinfoCadastroleft0infoCadastro

## infoCadastro

xmlinfoCadastro
st
123
123
123
123
{...}
{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| classTrib | DFILIAL.CLASSIFTRIBUTARIA |
| indEscrituracao | DFILIAL.EMPOBRIGADAECD |
| indDesoneracao | DFILIAL.DESONERACAOFOLHACPRB |
| indAcordoIsenMulta | DFILIAL.ACORDOINTISENCAOMULTA |
| indSitPJ | **Avaliar a possibilidade de criar um campo no cadastro da Filial** |

1contato

## contato

xmlcontato
str1234
str1234
str1234
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| nmCtt | DFILIAL.NOMECONTADOR |
| cpfCtt | DFILIAL.CPFCONTADOR |
| foneFixo | DFILIAL.DDDCONTADOR + DFILIAL.TELCONTADOR |
| foneCel | DFILIAL.DDDCELCONTADOR + DFILIAL.CELULARCONTADOR |
| email | DFILIAL.EMAILCONTADOR |

2softHouse

## softHouse

xmlsoftHouse
str1234
str1234
str1234
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| cnpjSoftHouse | Dados do Responsável pelo Software |
| nmRazao | Dados do Responsável pelo Software |
| nmCont | Dados do Responsável pelo Software |
| telefone | Dados do Responsável pelo Software |
| email | Dados do Responsável pelo Software |

3infoEFR

## infoEFR

xmlinfoEFR
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| ideEFR | Se o campo abaixo estiver preenchido, então este campo deve ser preenchido com "N" |
| cnpjEFR | DFILIAL.CNPJENTEFEDERATIVO |

As demais estruturas não destacadas irão seguir o padrão geral dos eventos

# Log do Cadastro de Filial

Os campos abaixo precisam registrar log de alteração.

* **Dados Fiscais | Obrigatoriedade da ECD** Hoje este campo registra somente quando o checkbox é habilitado é necessário registrar quando o mesmo for desabilitado também;
* **Dados Fiscais | Desoneração da folha** Hoje este campo registra somente quando o checkbox é habilitado é necessário registrar quando o mesmo for desabilitado também;
* **Dados Fiscais | Acordo Internacional para isenção de multa** Hoje este campo registra somente quando o checkbox é habilitado é necessário registrar quando o mesmo for desabilitado também.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
