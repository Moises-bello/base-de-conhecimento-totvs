---
content_hash: e60c512f472df9a51ecdb3887f1a98bd8e3552ac1123a225fccf368ed912ca8d
fetched_at: '2026-06-29T00:10:25.074166+00:00'
page_id: '501460561'
product: rm
source: tdn-rm
title: FISCAL01-9797 ER - EFD-REINF - R-9000
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-9797+ER+-+EFD-REINF+-+R-9000
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
| **Requisito/Story/Issue** | FISCAL01-9797 | **Subtarefa** | FISCAL01-10161 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Objetivo

 Detalhar as alterações necessárias no módulo TOTVS Gestão Fiscal para a implementação do Evento de Exclusão R-9000 da EFD-REINF

# Processo R-9000 Exclusão de Evento

O Evento R-9000 será incluído através de um processo próprio com o nome "**R-9000 Exclusão de Evento**" e durante a inclusão o mesmo já será integrado com o TSS. Diferentemente dos demais Eventos, o histórico deste deverá ser registrado no histórico do Evento pai vinculado.

Evento Principal

O Evento R-9000 é executado para outro Evento já existente, contudo para facilitar o entendimento vamos nos referir ao Evento Pai como Evento Principal

Durante a inclusão do Evento R-9000 deverão ser observados os comportamentos dos campos abaixo.

* **Id. Evento Pai** deverá ser exibido um lookup para cadastro do "Evento Principal", mas não poderá ser editado;
* **Tipo:** será preenchido com o código do evento R-9000 e não deve ser editável;
* **Status**: Receberá o status resultante da integração com o TSS. "Pendente" ou "Inconsistente".

Se o processo for executado com sucesso o "Evento Principal" terá o seu status alterado para "Pendente Exclusão" e um registro do R-9000 deverá ser incluído com status "Pendente". Em caso de erro deverá ser registrado um R-9000 "Inconsistente" e nada deverá ser alterado no "Evento Principal". Em ambos os casos um histórico deverá ser gravado no "Evento Principal".

Sempre que o "Evento Principal" estiver com o Status "Pendente Exclusão" ou "Excluído" o mesmo deverá apresentar um lookup para o Evento de Exclusão R-9000 no qual ele está associado.

O processo poderá ser executado em lote e através dos associados no Evento R-5011 para vários Eventos Periódicos simultaneamente (detalhes na especificação do R-5011).

## Regras

* Cada "Evento Principal" poderá ter somente um R-9000 associado e no caso de já existir um "Inconsistente" ou "Rejeitado" o mesmo deverá ser substituído.
* O R-9000 poderá ser gerado somente para Eventos com Status "Autorizado";
* O Evento R-9000 deve ser executado somente para os eventos do tipo: R-2010 a R-2070 e R-3010.

# Layout do Evento

O xml do Evento deverá ser gerado conforme abaixo.

xmlExemplo R-1000


{...}
{...}
{...}
]]>

## Origem dos dados

Este evento será gerado com base nos dados do "Evento Principal" que esta sendo "excluído".

## infoExclusao

xmlinfoExclusao
str123
str1234000000000
2019-01
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpEvento | Informar o tipo de Evento que esta sendo excluído  Deve ser um dos eventos: R-2010 a R-2070 e R-3010. |
| nrRecEvt | Preencher com o número do recibo do "Evento Principal" que será excluído.  Protocolo do "Evento Principal" que está sendo Excluído |
| perApur | Informar o período de referência das informações no formato AAAA-MM |

As demais estruturas não destacadas irão seguir o padrão geral dos eventos

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
