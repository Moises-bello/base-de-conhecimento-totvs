---
content_hash: 50f0160112ded4c7beec0356d9a3ce25f6dcb899a394a86e53e09d00e5cf67a6
fetched_at: '2026-07-02T19:24:24.329976+00:00'
page_id: '489760330'
product: protheus
source: tdn-tec
title: DBAccess - Seção [Environment], chave DeadLockExit
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=489760330
version: 6
---

DeadLockExit

Esta chave permite habilitar o mecanismo de finalização automática de um uma conexão em DeadLock no true, desde que a funcionalidade de identificação de *deadlock* esteja habilitada.

| Valor | Descrição |
| --- | --- |
| 1 | Habilita a finalização automática de uma conexão envolvida em um deadlock |
| **0 (default)** | Não habllita a finalização automática de uma conexão envolvida em um deadlock |

## Observações

Esta configuração exerce influencia sobre os processo de:

* Bloqueio de registros para alteração -- dbrlock() , msrlock(), reclock() – dentro de um bloco transacionado em AdvPL
* O mecanismo de identificação de deadlock funciona para todos os SGDBs suportados pelo DBAccess.
* A partir do DBAccess Build 20191119, o valor *default* desta configuração passa a ser 1 ( habilitada ).
* A partir do DBaccess Build 20200606, o valor *default* desta configuração voltou a ser 0 ( desabilitada ).

* Funcionalidade disponível a partir do DBAccess 20181212 Build 18.2.1.0
* Quando utilizado um true em modo distribuído, esta configuração deve ser inserida nos serviços secundários (ou *Slaves*) do true , e a configuração **CheckDeadLock=1** deve estar em uso no true Primário.
* A detecção de deadlock no DBAccess funciona avaliando as conexões que não conseguiram o bloqueio de um registro por um determinado tempo, considerando a cadeia de impedimento entre processos. Se a lista de impedimentos for circular, a conexão que identificou a ocorrência de deadlock é finalizada, para dar a chance das demais serem finalizadas.
* Não é necessário reiniciar o serviço do DBAccess para tornar esta configuração ativa – porém apenas as novas conexões estabelecidas com o DBAccess consideram o valor atualizado – as conexões já existentes não mudam o seu comportamento.
* O DBAccess não corrige um deadlock. O objetivo deste mecanismo é evitar que um deadlock mantenha processos em loop infinito segurando recursos do sistema e impedindo um processamento, além de gerar uma informação de diagnóstico no DBAccess, listando os processos envolvidos no deadlock. Uma vez reproduzida uma ocorrência dessa natureza, as aplicações envolvidas devem ser analisadas e uma ação pode ser necessária na aplicação para evitar o deadlock.
* Para configurar o mecanismo de deteção de deadlock, veja a documentação
