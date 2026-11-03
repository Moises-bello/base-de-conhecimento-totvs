---
content_hash: 834486326884943c779736a4daef5137e83e560f9d8c714f5e213fd7b1c87134
fetched_at: '2026-07-02T19:24:23.452298+00:00'
page_id: '450142687'
product: protheus
source: tdn-tec
title: Seção [BTMonitorAppD] - Chave InitTimeoutMs
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450142687
version: 4
---

Define o tempo de espera inicial máximo em milissegundos do agente SDK C++ da AppDynamics para obter e processar as configurações do controlador e iniciar a captura de transações de negócio.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 60.000 milissegundos (Padrão) | **Define como 60.0****00 milissegundos (60 segundos) o tempo de espera** inicial máximo do agente SDK C++ da AppDynamics para obter configurações do controlador e iniciar a captura de transações de negócio. |
| <número\_de\_milissegundos> > 0 (zero) | **Define como <número\_de\_milissegundos>** **o tempo de espera** inicial máximo do agente SDK C++ da AppDynamics para obter configurações do controlador e iniciar a captura de transações de negócio. |
| 0 (zero) | Faz com que o agente SDK C++ da AppDynamics **não espere** por configurações do controlador e inicie a captura de transações de negócio imediatamente. Até que o agente obtenha as configurações do controlador, todas as transações de negócio terão handle inválido e não serão contabilizadas. |
| <= -1 | Faz com que o agente SDK C++ da AppDynamics **espere indefinidamente** para obter configurações do controlador e iniciar a captura de transações de negócio. |

## Observações

* Esta chave somente será considerada se e somente se a chave [Seção [BTMonitorAppD] - Chave LogEnable](http://tdninterno.totvs.com/pages/viewpage.action?pageId=448600725) estiver habilitada;
* Esta configuração existe para fazer com que o agente aguarde até receber e processar a configuração do controlador e esteja pronto para capturar transações de negócio. Deve ser usada quando for necessária a captura de transações de curta duração que ocorrem durante a inicialização da aplicação;
* O agente retornará imediatamente após receber e processar as configurações do controlador, mesmo que o tempo configurado ainda não tenha sido atingido;
* Caso o tempo configurado seja menor do que o necessário e o agente retorne antes de receber e processar as configurações do controlador, as transações de negócio terão o handle nulo, serão consideradas inválidas e não serão contabilizadas;
* O valor informado é inteiro e sem separador de milhar.

Atenção

Habilitar esta configuração fará com que a inicialização do AppServer seja preterida por alguns milissegundos, até que o agente receba e processe a configuração do controlador, ou até que o tempo de espera seja atingido, o que acontecer primeiro.

Exemplo

Define como 10.000 milissegundos (10 segundos) o tempo de espera inicial do agente SDK C++ da AppDynamics para capturar transações de negócio:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
