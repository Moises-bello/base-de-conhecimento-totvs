---
content_hash: e512941615eb668b7f4f5ed759a5f230364caee6c2120865fc0e506e6d7970b6
fetched_at: '2026-06-29T00:08:15.768306+00:00'
page_id: '244924117'
product: rm
source: tdn-rm
title: 1. Parametros
type: documentation
url: https://tdn.totvs.com/display/LRM/1.+Parametros
version: 3
---

|  |  |
| --- | --- |
| Descrição | Parâmetros |
| Observações | Parâmetros que deverão ser criados para permitir a contabilização dos processos da Gestão de Locação |

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Onde** | ***Opções*** | **Comportamento** |
| Habilitar Integração Contábil | Coligada  *(opções excludentes)* | Marcado | Entra na  rotina de contabilização;  Habilita associação do Evento Contábil no Contrato de Locação. |
| Desmarcado(default) | Não entra na  rotina de contabilização;  Desabilita associação do Evento Contábil no Contrato de Locação, evitando que o usuário entenda que haverá contabilização.  Não mostra a pasta de contabilização anexa ao contrato de locação e anexa ao modelo de contrato. |
| Contabilização Automática  (*On Line*) | Coligada  *(opções excludentes)* | Marcado(default) | Se a integração contábil estiver habilitada, permite habilitar este parâmetro e o sistema passa a disparar contabilização de todos os processos que tenham lançamento contábil associado. (via contrato de locação).  O período de contabilização será sempre “Período Total do Contrato de Locação”. |
| Desmarcado | A contabilização deverá ser feita manualmente através de processos na visão do contrato de locação ou no menu principal pelo Recurso de Contabilização Global.  Permite que o usuário defina o Período de Contabilização conforme parâmetro do contrato. |
| Período de Contabilização Contrato de Locação | Coligada  *------------------------------*  Modelo do Contrato de Locação  ------------------------------  Contrato de Locação | Período do Contrato de Locação | Gera todos os lançamentos contábeis para todos os períodos (meses) até o final do contrato de locação  e sempre que re-contabilizar fará a alteração de todos os lançamentos contábeis a partir da data de alteração (data fato gerador) até o período final. |
| Informar Períodos  *(manualmente)* | Gera todos os lançamentos contábeis para o período (data inicial e final) que o Usuário informar, respeitando a data inicial e Prorrogação do contrato;  Sempre que re-contabilizar fará a alteração apenas dos lançamentos contábeis já gerados a partir da data de alteração (data fato gerador). |
| Bloqueia Edição do Periodo no Contrato | Coligada |  | Se marcado não permite que o usuário altere a parametrização de período de contabilização do contrato prevalecendo sempre o que foi parametrizado na Coligada |
| Exibe Tela de Contabilização | Coligada | Marcado | Apresenta tela com a previa da contabilização, sempre que o processo de integração for disparado. Esta tela não será apresentada quando a contabilização for feita para processos em lote como reajuste e neste caso o resultado da contabilização (ok ou não) deve ser registrado em log de processo. |
| Desmarcado | Não apresenta tela com a prévia da contabilização em nenhum processo. |
| Evento contábil default para Eventos financeiros avulsos | Coligada | Evento Contábil | O usuário deverá informar o evento contábil padrão para que o sistema. |
| Aplicar Linearização | Modelo do Contrato de Locação  (excludente)  ------------------------------ Contrato de Locação  (excludente) | Marcado | Apresenta as opções de valor Linearizados, ou seja, valor médio conforme competência.  Contabiliza os valores distribuídos de forma linear, ou seja, em todos os períodos do contrato independente de ter carência ou períodos sem lançamentos Contábeis. |
| Desmarcado(default) | Apresenta as opções de valor conforme competência e permite contabilização mês a mês. |
| Executar para | Modelo do Contrato de Locação  (excludente)  ------------------------------ Contrato de Locação  (excludente) | Contrato de Locação (default) | Indica em qual processo será disparada a contabilização do contrato de locação.  Se marcada a opção de Contrato de Locação o processo de contabilização será disparado ao efetivar o contrato de locação. |
| Geração de lançamentos financeiros | Ao marcar esta opção o disparo de contabilização será feito no processo de “Gerar Lançamentos Financeiros” |
| Contrato de Locação | O contrato de Locação terá o mesmo funcionamento indicado acima mas seu default será a opção marcada no campo correspondente no modelo de contrato. |
| Geração de lançamentos financeiros |
| Competência do Lançamento Contábil | Modelo do Contrato de Locação  (excludente)  ------------------------------ Contrato de Locação  (excludente) | Mês Vencido | Gera os lançamentos com a competência no mês anterior ao mês de cobrança.  Se não houver cobrança no período (carência) e a contabilização for linear, o primeiro período a ser contabilizado será o inicio da vigência do contrato de locação. |
| Mês Vincendo | Gera os lançamentos com a competência no mês de cobrança.  Se não houver cobrança no período (carência) e a contabilização for linear, o primeiro período a ser contabilizado será o inicio da vigência do contrato de locação. |
| Evento Contábil | Modelo do Contrato de Locação  (excludente)  ------------------------------ Contrato de Locação  (excludente) | Contrato de Locação | Podem ser informados os eventos Contábeis que serão responsáveis pelo disparo e modelo de contabilização.  Se não houve Evento Contábil associado ao processo, o sistema não contabilizara o mesmo. |
| Rescindir Contrato |
| Data para início da contabilização | Modelo do Contrato de Locação  (excludente)  ------------------------------ Contrato de Locação  (excludente) | Início da vigência do contrato | A contabilização começará a partir da data de início do vigência  Contrato de Locação; |
| Início da locação do contrato | A contabilização começará a partir da data de início da Locação; |
| Data-base de contabilização  (default = data do sistema) | O usuário deverá informar uma data a partir da qual o contrato de locação passará a contabilizar.  Esta opção permite que contratos anteriores a implantação do sistema TIN ou anterior a ativação da contabilização no aluguel, não tenham seus lançamnetos gerados para períodos antigos e já tiveram a contabilidade feita por outros sistemas. |

**Protótipos de tela**

Parâmetros por Coligada

Parâmetros por Modelo de Contrato

Parâmetros por Contrato de Locação
