---
content_hash: 1a62ca3b8a5b4d7fdb1573398de750e30d78928a9f0095951fc6f972a16177fc
fetched_at: '2026-06-29T00:08:47.103654+00:00'
page_id: '318606081'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01-664 Evento de Prestação de Serviço em Desacordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=318606081
version: 92
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATFATCMPCRM01 | **IRM/EPIC1** | MATFATCMPCRM01-664 |
| **Requisito/Story/Issue1** | MATFATCMPCRM01-671 | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

Descrever a implementação do evento de Prestação de Serviço em Desacordo para atender aos processos envolvidos à transmissão de CT-e, conforme orientações contidas no Manual de Orientações do Contribuinte - MOC Versão 3.00 de julho de 2016.

## 

## Definição da Regra de Negócio

Foi criado um evento para que o tomador possa informar ao fisco que o documento CT-e emitido em seu nome está em desacordo com a prestação de serviço. Esse evento deve ser enviado pelo tomador do serviço indicado no CT-e, sendo que a mensagem XML do evento será assinada com o certificado digital que tenha o CNPJ base do tomador do serviço do CT-e.

Trata-se de um processo síncrono e pelas regras de validação para anulação de um CT-e com tomador contribuinte é necessário existir um evento de Prestação de Serviço em Desacordo.

De acordo com o Ajuste SINIEF 09/07, o evento de Prestação de Serviço em Desacordo pode ser utilizado em duas situações:

1. Anulação de valores relativos à prestação de serviço de transporte, em virtude de erro devidamente comprovado como exigido em cada unidade federada, e desde que não descaracterize a prestação:

Tomador contribuinte de ICMS:

* O tomador deverá emitir documento fiscal próprio, pelos valores totais do serviço e do tributo,  utilizando a natureza especifica de Anulação de Valores e informando o número do CT-e emitido com erro, os valores anulados e o motivo.
* Ao receber o documento de anulação, o transportador deverá emitir um CT-e substituto, referenciando o CT-e emitido com erro e também informando seu motivo.

Tomador não contribuinte de ICMS:

* O tomador deverá emitir uma declaração informando o número e a data de emissão do CT-e inconsistente, assim como o motivo da inconsistência.
* Ao receber o documento de anulação, o transportador deverá emitir um CT-e de anulação, adotando os mesmos valores totais do serviço e do tributo, utilizando a natureza especifica de Anulação de Valores e informando o número do CT-e emitido com erro e o motivo.
* Após emitir o documento anterior, o transportador deverá emitir um CT-e substituto, referenciando o CT-e emitido com erro e também informando seu motivo.

Opção alternativa às informadas anteriormente:

* O tomador deverá registrar o evento de “Prestação de Serviço em Desacordo”, justificando o porquê do serviço executado não ter sido como o acordado.
* A partir deste evento, o transportador deverá emitir um CT-e de Anulação, adotando os mesmos valores totais do serviço e do tributo, utilizando a natureza especifica de Anulação de Valores e informando o número do CT-e emitido com erro e o motivo.
* Após emitir o documento anterior, o transportador deverá emitir um CT-e substituto, referenciando o CT-e emitido com erro e também informando seu motivo.

**Observação**: De acordo com o Manual de Orientação ao Contribuinte do CT-e Versão 3.00 de julho de 2016, quando o Tomador for contribuinte é obrigatória a emissão do Evento de Prestação de Serviço em Desacordo.

2. Alteração de tomador de serviço informado indevidamente no CT-e, em virtude de erro devidamente comprovado como exigido em cada unidade federada:

* O tomador deverá registrar o evento de “Prestação de Serviço em Desacordo”, justificando o porquê do serviço executado não ter sido como o acordado.
* A partir deste evento, o transportador deverá emitir um CT-e de Anulação, adotando os mesmos valores totais do serviço e do tributo, utilizando a natureza especifica de Anulação de Valores e informando o número do CT-e emitido com erro e o motivo.
* Após emitir o documento anterior, o transportador deverá emitir um CT-e substituto, referenciado o CT-e emitido com erro e registrar seu motivo como “Este documento substitui o CT-e “número” de “data” em virtude de tomador informado erroneamente".

Para atender à legislação, será necessário:

Visão de Movimentos

* Em Processos deverá ser criada uma nova opção chamada "Enviar Prestação em Desacordo". Ao executar esse processo, o usuário deverá informar a justificativa referente a prestação do serviço em desacordo. A justificativa deve possuir um tamanho entre 15 e 255 caracteres. Esse evento será enviado para a SEFAZ de acordo com o leiaute definido no Manual de Orientações do Contribuinte Versão 3.00 de julho de 2016 e será vinculado ao(s) CT-e(s) ao(s) qual(is) está(ão) relacionado(s).
* Em Processos deverá ser criada uma nova opção chamada "Consultar Prestação em Desacordo". Ao selecionar essa opção, será realizada a consulta do evento de prestação de serviço em desacordo, retornando as informações referentes aos envios de prestação em desacordo que estiverem pendentes de retorno.
* Esses processos deverão ser exibidos somente na visão dos movimentos cujo tipo de movimento esteja parametrizado para Cadastrar CTRC/CTE (parâmetros do tipo de movimento **Tipo de Operação do Conhecimento de Transporte** igual a "Cadastrar CTRC/CTE".
* O processo "Enviar Prestação em Desacordo" somente poderá ser executado se houver um movimento selecionado.
* O processo "Consultar Prestação em Desacordo" pode ser executado mesmo que não haja movimento selecionado, pois ele não depende de parâmetros para execução.

Leiaute do Evento

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome** | **Pai** | **Tipo** | **Tam.** | **Ocor.** | **Observações** |
| **detEvento** | Eventos | G | - | 1-N | Tag raiz |
| tpEvento | detEvento | A | 6 | 1-1 | Tipo de Evento  Informar : **610110** |
| chNFe | detEvento | N | 44 | 1-1 | Chave de Acesso do CT-e ou CT-e OS. |
| indDesacordoOper | detEvento | A | 1 | 1-1 | Indicador de prestação do serviço em desacordo. |
| xOBS | detEvento | A | 15-255 | 0-1 | Observações do tomador |

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

**Tabelas Utilizadas**

* TMOV - Movimento

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
