---
content_hash: 34d79ed26f9b6913b65478f7411e6f45f40a5c4a4a9f60ac4319131cc125b42f
fetched_at: '2026-06-29T00:10:25.107580+00:00'
page_id: '501466393'
product: rm
source: tdn-rm
title: FISCAL01-9799 ER - EFD-REINF - Integração com o TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501466393
version: 87
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Fiscal |
| **Segmento Executor** | Backoffice | | |
| **Requisito/Story/Issue** | FISCAL01-9799 | **Subtarefa** | FISCAL01-10176 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Objetivo

 Detalhar as alterações necessárias no modulo TOTVS Gestão Fiscal para a implementação a integração dos Eventos da EFD-REINF com os webservices (WS) TOTVS Service Soa (TSS)

# WebService do TSS

Na integração com o TSS deverá ser utilizado o WS TSSWSREINF onde são disponibilizados os serviços abaixo.

A documentação do TSS pode ser consultada através do link  <http://tdn.totvs.com/display/TSS/WebService+-+TSSWSREINF>. As parametrizações de integração com o TSS já estão disponíveis no parâmetro da Filial do modulo de Estoque nas etapas referentes à integração com o módulo Fiscal.

## Configurar Ambiente

Antes de utilizar o WS da EFD-REINF listados acima é necessário configurar o TSS utilizando os WS abaixo.

* **SpedAdm** para configurar a filial que está emitindo os Eventos através do serviço **AdmEmpresas**. Este Serviço já está implementado e disponível através da interface IFisSpedAdm do projeto RM.Fis.TSS.IService;
* **SpedCfgNfe** para configurar o certificado digital através dos serviços **CFGCERTIFICATE**, **CFGCERTIFICATEPFX** ou **CFGHSMEX**. Este serviço já está implementado e disponível através do server FisCertificadoService do projeto RM.Fis.TSS.Service.

SUGESTÃO

Para manter o padrão deverá ser criado uma interface (IFisTssWsReinf) no projeto RM.Fis.TSS.IService para o WS TSSWSREINF com os serviços WsValidarSchema, WsEnviarEventos, WsConsultarEventos. Esta interface deve ser implementada de forma semelhante a IFisSpedAdm. Esta prática evita que outros projetos tenham referências diretas ao TSS.

## VALIDARSCHEMA

truetruefalseVALIDARSCHEMAfalse5653

Através deste WS é realizada a validação da estrutura do XML do Evento conforme o schema disponibilizado pela RFB. Segue abaixo os parâmetros de entrada e saída do serviço. Para mais detalhes consulte a documentação do TSS <http://tdn.totvs.com/x/HUhZEg>

falseVALIDARSCHEMAleft0Parâmetros de Entrada

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Tipo** | **Tam** | **Observação** |
| AMBIENTE | Alfanumérico | 1 | Conforme definido para o Evento  2 – Produção Restrita Dados Reais.  3 - Produção Restrita Dados Fictícios. |
| CODIGO | Alfanumérico | 10 | Código do evento, conforme disponibilizado pela Receita Federal. R-1000, R-2010 etc. |
| ENTIDADE | Alfanumérico | 6 | Código da entidade registrada no TSS.  Retornado pelo serviço AdmEmpresas |
| ID | Alfanumérico | 100 | Identificador do evento.  Este identificador é gerado pelo ERP emissor do evento. |
| USERTOKEN | Alfanumérico | 6 | Fixo **TOTVS**. |
| VERSAO | Alfanumérico | 15 | Versão do Evento.  Conforme definido nos parâmetros da EFD-REINF |
| XML | BASE64Binary |  | Lista de XMLs dos eventos, conforme layout do Evento.  O layout de cada Evento está definido na especificação do mesmo. |

ATENÇÃO

Cada requisição poderá ser realizada com no máximo 100 Eventos.

1Parâmetros de Saída

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Tipo** | **Tam** | **Observação** |
| AMBIENTE | Alfanumérico | 1 | Ambiente do envio:  2 – Produção Restrita Dados Reais.  3 - Produção Restrita Dados Fictícios. |
| ENTIDADE | Alfanumérico | 6 | Código da entidade registrada no TSS. |
| ERRO | Alfanumérico | 6 | Retorno Sefaz com a descrição da rejeição. |
| ID | Alfanumérico | 100 | Identificador do evento.  Este identificador é gerado pelo ERP emissor do evento. |
| STATUS | Booleano | 1 | Indicador de envio com sucesso. |
| VERSAO | Alfanumérico | 15 | Versão do Evento. |

## ENVIAREVENTOS

truetruefalseENVIAREVENTOSfalse9162

Através deste WS é realizado o envio dos XMLs dos Eventos ao TSS. Segue abaixo os parâmetros de entrada e saída do serviço. Para mais detalhes consulta a documentação do TSS <http://tdn.totvs.com/x/EUJZEg>

falseVALIDARSCHEMAleft0Parâmetros de Entrada

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Parâmetro** | **Tipo** | **Tam** | **Pai** | **Observação** |
| ENVIAREVENTOS | Estrutura | - | - | - |
| REINFENVIO | Estrutura | - | ENVIAREVENTOS | - |
| CABEC | Estrutura | - | REINFENVIO | - |
| AMBIENTE | Alfanumérico | 1 | CABEC | Conforme definido para o Evento  2 – Produção Restrita Dados Reais.  3 - Produção Restrita Dados Fictícios. |
| ENTIDADE | Alfanumérico | 6 | CABEC | Código da entidade registrada no TSS.  Retornado pelo serviço AdmEmpresas |
| USERTOKEN | Alfanumérico | 6 | CABEC | Fixo **TOTVS**. |
| VERSAO | Alfanumérico | 15 | CABEC | Versão do Evento.  Conforme definido nos parâmetros da EFD-REINF |
| EVENTOS | Estrutura | - | REINFENVIO | Lista de Eventos |
| REINFENVIOEVENTO | Estrutura | - | EVENTOS | - |
| CODIGO | Alfanumérico | 10 | EVENTOS | Código do evento, conforme disponibilizado pela Receita Federal. R-1000, R-2010 etc. |
| ID | Alfanumérico | 100 | EVENTOS | Identificador do evento.  Este identificador é gerado pelo ERP emissor do evento. |
| XML | BASE64Binary |  | EVENTOS | Deverá ser enviado o XML que foi validado através do serviço VALIDARSCHEMA |

ATENÇÃO

* Cada requisição poderá ser realizada com no máximo 100 Eventos.
* Só podem ser enviados os XML válidos, ou seja, aqueles que passaram pela validação de schema sem erros.
1Parâmetros de Saída

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Tipo** | **Tam** | **Observação** |
| AMBIENTE | Alfanumérico | 1 | Ambiente do envio:  2 – Produção Restrita Dados Reais.  3 - Produção Restrita Dados Fictícios. |
| ENTIDADE | Alfanumérico | 6 | Código da entidade registrada no TSS. |
| ERRO | Alfanumérico | 6 | Retorno Sefaz com a descrição da rejeição. |
| ID | Alfanumérico | 100 | Identificador do evento.  Este identificador é gerado pelo ERP emissor do evento. |
| STATUS | Booleano | 1 | Indicador de envio com sucesso. |
| VERSAO | Alfanumérico | 15 | Versão do Evento. |

## CONSULTAREVENTOS

truetruefalseCONSULTAREVENTOSfalse5731

CONSULTAREVENTOS

Para o serviço CONSULTAREVENTOS sugiro que seja utilizado o serviço **SpedAdm.****GetAdmEmpresasId** para recuperar o código da entidade do TSS conforme documentação do TSS <http://tdn.totvs.com/x/cZhSDg>

Neste serviço é desnecessário a utilização do WS **SpedCfgNfe**

Através deste WS é realizada a consulta do XMLs dos Eventos no TSS. Segue abaixo os parâmetros de entrada e saída do serviço. Para mais detalhes consulta a documentação do TSS <http://tdn.totvs.com/x/EkBZEg>

falseVALIDARSCHEMAleft0Parâmetros de Entrada

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Parâmetro** | **Tipo** | **Tam** | **Pai** | **Observação** |
| CONSULTAREVENTOS | Estrutura | - | - | - |
| REINFCONSULTA | Estrutura | - | - | - |
| CABEC | Estrutura |  | REINFCONSULTA | - |
| ID\_ENT | Alfanumérico | 06 | CABEC | Código da entidade registrada no TSS.  Retornado pelo serviço AdmEmpresas |
| RETORNAXML | Lógico | - | CABEC | Fixo true |
| USERTOKEN | Alfanumérico | 06 | CABEC | Fixo **TOTVS**. |
| EVENTOS | Estrutura | - | REINFCONSULTA | Lista de ID dos Eventos |
| REINFID | Estrutura | - | EVENTOS | - |
| ID | Alfanumérico | 100 | REINFID | Identificador do evento.  Este identificador é gerado pelo ERP emissor do evento |

ATENÇÃO

Cada requisição poderá ser realizada com no máximo 100 Eventos.

1Parâmetros de Saída

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Parâmetro** | **Tipo** | **Tam** | **Pai** | **Observação** |
| CONSULTAREVENTOSRESULT | Estrutura | - | - | - |
| REINFRETCONSULTA | Estrutura | - | CONSULTAREVENTOSRESULT | - |
| CHAVE | Alfanumérico | 36 | REINFRETCONSULTA | Chave Evento. |
| CODEVENTO | Alfanumérico | 10 | REINFRETCONSULTA | Código Evento. |
| CODRECEITA | Alfanumérico | 10 | REINFRETCONSULTA | Código da Receita |
| DETSTATUS | Alfanumérico | 1 | REINFRETCONSULTA | Detalhe do evento, conforme disponibilizado pela Receita Federal. |
| DSRECEITA | Alfanumérico | 30 | REINFRETCONSULTA | Descrição do Código Receita. |
| DTENTRADA | Date | 8 | REINFRETCONSULTA | Data Entrada Evento. |
| DTPROC | Date | 8 | REINFRETCONSULTA | Data Processamento Evento. |
| DTTRANS | Date | 8 | REINFRETCONSULTA | Data Transação Evento. |
| HRENTRADA | Alfanumérico | 8 | REINFRETCONSULTA | Hora Entrada Evento. |
| HRPROC | Alfanumérico | 8 | REINFRETCONSULTA | Hora Processamento Evento. |
| HRTRANS | Alfanumérico | 8 | REINFRETCONSULTA | Hora Transação Evento. |
| ID | Alfanumérico | 100 | REINFRETCONSULTA | Identificador do evento.  Este identificador é gerado pelo ERP emissor do evento. |
| LOTE | Alfanumérico | 32 | REINFRETCONSULTA | Número do Lote. |
| PROTOCOLO | Alfanumérico | 40 | REINFRETCONSULTA | Número do Protocolo. |
| RECIBO | Alfanumérico | 30 | REINFRETCONSULTA | Número do Recibo. |
| STATUS | Alfanumérico | 1 | REINFRETCONSULTA | Status do documento no TSS. |
| VERSAO | Alfanumérico | 8 | REINFRETCONSULTA | Versão do Evento. |
| XMLEVENTO | Alfanumérico |  | REINFRETCONSULTA | Detalhes do xml do evento |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
