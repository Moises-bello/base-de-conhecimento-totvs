---
content_hash: 035bef300b0d6bf4c783db3208e23cc5e33a425f33b6910018fc45dc20b0152a
fetched_at: '2026-06-29T00:09:35.286111+00:00'
page_id: '425459295'
product: rm
source: tdn-rm
title: TOTVS Business Connect - Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459295
version: 3
---

**Serviços**

---

Os Serviços disponíveis no TOTVS Business Conector permitem processar as mensagens trocadas entre os aplicativos integrados. Eles podem ser executados manualmente ou de forma programada. Estão disponíveis os serviços:

* **Agente de Envio (via TOTVS ESB):** O serviço envia todas as mensagens de integração que estão pendentes no Monitor da Fila de Integração.
* **Agente de Recebimento (via TOTVS ESB):** O serviço processa todas as mensagens que chegaram na fila (sentido entrada), e que estão pendentes de processamento.
* **Integrar TOTVS Folha x Tools:** O serviço verifica de tempo em tempo, conforme programado, se existe requisição pendente na fila do Tools para ser processada, e realiza o processamento da mesma. Veremos mais sobre este serviço no módulo da Integração TOTVS Folha de Pagamento x Gestor AVB (Tools).

**Agendamento do Serviço**  
    
 Ao selecionar os serviços, é aberto o Executor de Agendamento do Serviço, para que possa ser feito o agendamento da execução do serviço solicitado.   
 A visão é composta pelos campos:  
 Hora de execução (1ª execução)

* **Agora:** Executa o processo uma única vez e imediatamente na data corrente.
* **Executar em:** Executa o processo uma única vez e na data e hora especificada. Essa opção possui como padrão a data corrente do dia sendo possível alterá-la.
* **Sob demanda:** Sempre que existir uma demanda, o serviço será executado na hora. Ou seja, sempre que uma mensagem estiver na fila de integração (entrada ou saída) a mensagem será processada imediatamente.

Repetir a execução: Deve ser utilizada quando houver a necessidade de executar o processo de forma recorrente.

* **Semanal:** Todas as semanas no mesmo horário e no(s) dia(s) de acordo com o definido.
* **Mensal:** Todos os meses, no mesmo horário e no(s) dia(s) de acordo com o definido.
* **Diário:** Diariamente, a cada intervalo (em horas) de acordo com o definido.

**Observação:**

Para que o agendamento dos serviços estejam disponíveis, é necessário que a tag "JobServer3Camadas" esteja com valor igual a "True".  
 <add key="JobServer3Camadas" value="True" />

Esta tag deve ser alterada nos arquivos de configuração de cada aplicativo, e também no RM.Host.
