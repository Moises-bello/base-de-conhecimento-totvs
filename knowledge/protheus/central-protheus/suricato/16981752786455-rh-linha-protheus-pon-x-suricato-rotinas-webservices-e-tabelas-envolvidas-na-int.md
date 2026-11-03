---
article_id: 16981752786455
category: Suricato
content_hash: 4343ec06086538e3313e70156299138756b62e96eccf2173b0c0bcf3e267aade
fetched_at: '2026-06-28T22:44:57.463457+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - PON x Suricato - Rotinas, Webservices e Tabelas envolvidas
  na integração do Ponto Eletrônico x Suricato
type: support-article
updated_at: '2023-12-20T17:03:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16981752786455-RH-Linha-Protheus-PON-x-Suricato-Rotinas-Webservices-e-Tabelas-envolvidas-na-integra%C3%A7%C3%A3o-do-Ponto-Eletr%C3%B4nico-x-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981767445911) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Quais são as rotinas, tabelas e *webservices* envolvidos na integração do Ponto Eletrônico com o Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - A partir da versão 12.1.23  
  
**Solução**Abaixo, temos as **rotinas** envolvidas na integração do **Ponto Eletrônico** com o **Suricato**:

|  |  |
| --- | --- |
| **Rotina** | **Descrição** |
| CTBA030 | Cadastro de Centro de Custos |
| GPEA010 | Cadastro de Funcionários |
| GPEA030 | Cadastro de Funções |
| GPEA080 | Cadastro de Turno de Trabalho |
| GPEA180 | Cadastro de Transferência de Funcionários |
| GPEA240 | Cadastro de Afastamentos |
| GPEA265 | Cadastro de Autônomos |
| PONA020 | Cadastro de Feriado |
| PONA080 | Manutenção da Tabela de Horário Padrão |
| PONA090 | Cadastro de Exceções por Período |
| PONA140 | Cadastro de Exceções por Funcionário |
| PONA160 | Troca de Turno |
| PONM430 | Integração TSA |
| PONXFUN | Biblioteca de Funções do SIGAPON |
| PONXFUN1 | Biblioteca de Funções do SIGAPON |
| PTSREPOBJ | Biblioteca de Funções do SIGAPON |
| RHUPDPON | Atualizador do Ponto Eletrônico |

Segue abaixo as **tabelas** envolvidas na integração do **Ponto Eletrônico** com o **Suricato:**

|  |  |
| --- | --- |
| **Tabela** | **Descrição** |
| CTT | Centro de Custo |
| SPA | Regra de Apontamento |
| SPJ | Tabela de Horário Padrão |
| SP2 | Exceções |
| SP3 | Feriados |
| SRJ | Funções |
| SPF | Transferência de Turno |
| SR6 | Turnos de Trabalho |
| SR8 | Controle de Ausências |
| SRA | Funcionários |

Abaixo, temos a listagem dos **principais fontes e *webservices*** envolvidos na integração:

**Carga Incial - PONM430**Para a primeira integração com o Suricato, será necessário realizar a carga inicial. A rotina de Carga Inicial (POMM430 - Miscelânea → S.r.e.p. → Integração Tsa), será responsável por enviar todas as informações necessárias para a utilização do Suricato. Nela é possível selecionar quais informações serão enviadas inicialmente, que vão desde o cadastro da empresa até Férias/Afastamentos dos Funcionários, porém, a rotina possui uma ordem de execução que **NÃO** deve ser alterada, mas não há obrigatoriedade de enviar todos os cadastros de uma vez. É recomendado enviar primeiramente os cadastrados da Empresa, Unidade e Lotação, e assim sucessivamente.  
  
![](https://tdn.engpro.totvs.com.br/download/attachments/546695095/image2020-4-29_15-30-15.png?version=1&modificationDate=1588185015927&api=v2&effects=drop-shadow)

**PTSREPOBJ**Este fonte possui todos os métodos que irão fazer a chamada de um Web Service para realizar a integração com o Suricato:  
  
**WSClient\_WSRHTSAAbsenceReason**  
O AbsenceReason é o Web Service responsável por enviar as informações referentes as ausências. O método que faz a chamada desse Web Service é o WSAbsenceReason, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações da tabela tipo de ausências (RCM), manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSAAllocationUnit**  
O AllocationUnit é o Web Service responsável por enviar as informações referentes as Unidades de Lotações. O método que faz a chamada desse Web Service é o WSAllocation, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações do cadastro de Unidade de Lotação, manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSACostCenter**  
O CostCenter é o Web Service responsável por enviar as informações referentes aos Centros de Custos. O método que faz a chamada desse Web Service é o WSCostCenter, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações da tabela dos Centros de Custos (CTT), manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSADayNotWorked**  
O DayNotWorked é o Web Service responsável por enviar as informações referentes aos Feriados. O método que faz a chamada desse Web Service é o WSDayNotWorked, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações dos Feriados cadastrados (SP3), manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSAException**  
O Exception é o Web Service responsável por enviar as informações referentes as Exceções. O método que faz a chamada desse Web Service é o WSException, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações das Exceções cadastradas (SP2), manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSALegalPerson**  
O LegalPerson é o Web Service responsável por enviar as informações referentes as Empresas. O método que faz a chamada desse Web Service é o WSLegal, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações das Empresas cadastradas, manipulará os dados e enviará para o Suricato.  
O Web Service LegalPerson também é responsável por enviar os Sindicatos cadastrados, através do método WSSindicatoLegal.  
  
**WSClient\_WSRHTSALocationIntegration**  
O LocationIntegration é o Web Service responsável por enviar as informações referentes as Localizações (Cidades). O método que faz a chamada desse Web Service é o WSLocation, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações das Localizações cadastradas, manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSANaturalPerson**  
O NaturalPerson é o Web Service responsável por enviar as informações referentes aos Funcionário. O método que faz a chamada desse Web Service é o WSNatural, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações dos Funcionário cadastrados (SRA), manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSAPositionLevel**  
O PositionLevel é o Web Service responsável por enviar as informações referentes as Funções do funcionário. O método que faz a chamada desse Web Service é o WSPositionLevel, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações das Funções cadastradas (SRJ), manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSAScaleIntegration**  
O ScaleIntegration é o Web Service responsável por enviar as informações referentes a Tabela Horário Padrão. O método que faz a chamada desse Web Service é o WSSCale, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações da Tabela de Horário Padrão cadastradas (SPJ), manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSAShiftWork**  
O ShiftWork é o Web Service responsável por enviar as informações referentes ao Turnos. O método que faz a chamada desse Web Service é o WSShiftWork, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações da tabela de Turnos cadastrados (SR6), manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSAUnit**  
O Unit é o Web Service responsável por enviar as informações referentes a Unidade. O método que faz a chamada desse Web Service é o WSUnit, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações da Unidade cadastrada, manipulará os dados e enviará para o Suricato.  
  
**WSClient\_WSRHTSAUserIntegration**

O UserIntegration é o Web Service responsável por enviar as informações referentes aos Usuários. O método que faz a chamada desse Web Service é o WSUser, localizado no fonte PTSREPOBJ. Neste método o sistema irá receber as informações dos Usuários, tais como Nome, Centro de Custo, Papéis (Permissões) e etc, manipulará os dados e enviará para o Suricato.  
**Observação:**Este Web Service é diferente dos demais, pois ele possui vários métodos para inserir informações diferentes, como por exemplo Centro de Custo e Função, utilizando os métodos insertUserShiftWork e insertUserPositionLevel respectivamente, localizados no Web Service.

Por fim, temos abaixo os nomes das **rotinas** e seus **serviços relacionados**:

|  |  |
| --- | --- |
| **Rotina** | **Web Services** |
| Schedule Empresa | LegalPerson |
| Schedule Unidade | Unit |
| Schedule Unidade de Lotação | AllocationUnit |
| Schedule Localidade | LocationIntegration |
| Schedule Tabelas 30/31 – Módulo Configurador | AbsenceReason, UnitAbsenceReason |
| Cadastro de Centro de Custos (CTBA030) | CostCenter |
| Cadastro de Funcionário (GPEA010) | UserIntegration, UserShiftWork, UserLocation, UserRoleBadge, UserCostCente, UserAllocationUnit, UserAbsenceReason, RemoveUserAbsenceReason, NaturalPerson |
| Cadastro de Funções (GPEA030) | PositionLevel |
| Cadastro de Turno de Trabalho (GPEA080) | ShiftWork |
| Cadastro de Transferência de Funcionário (GPEA180) | UserIntegration, NaturalPerson |
| Cadastro de Afastamentos (GPEA240) | AbsenceReason |
| Cadastro de Autônomos (GPEA265) | UserIntegration, UserShiftWork, UserLocation, UserRoleBadge, UserCostCente, UserAllocationUnit, UserAbsenceReason, RemoveUserAbsenceReason, NaturalPerson |
| Cadastro de Feriado (PONA020) | DayNotWorked |
| Manutenção da Tabela de Horário Padrão (PONA080) | ShiftWork,Scale |
| Cadastro de Exceções por Período (PONA090) | DayNotWorked,Exception |
| Cadastro de Exceções por Funcionário (PONA140) | Exception |
| Troca de Turno (PONA160) | UserIntegration, UserShiftWork |
| Integração TSA (PONM430) | Todos |

**Saiba Mais:**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16779731236119)  
[Pacote de Expedição Contínua - Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
