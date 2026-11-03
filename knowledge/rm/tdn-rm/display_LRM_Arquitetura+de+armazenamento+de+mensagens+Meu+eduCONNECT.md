---
content_hash: 92c086f034a9957af10d90de1a82d18835c6d7dae831159dfde3c13769ed15af
fetched_at: '2026-06-29T00:05:52.963398+00:00'
page_id: '1062864360'
product: rm
source: tdn-rm
title: Arquitetura de armazenamento de mensagens Meu eduCONNECT
type: documentation
url: https://tdn.totvs.com/display/LRM/Arquitetura+de+armazenamento+de+mensagens+Meu+eduCONNECT
version: 9
---

**Visão geral**

Até a versão 12.1.2602.164, o envio de notificações para o aplicativo Meu eduCONNECT (e suas versões customizadas) era enviado do TOTVS RM Educacional para a nuvem Microsoft Azure. Nessa estrutura, as mensagens permaneciam armazenadas na nuvem por até 1 ano antes de serem excluídas automaticamente, e o aplicativo se encarregava de baixá-las no dispositivo (celular ou tablet) conforme o contexto do usuário logado.

A partir da versão 12.1.2602.165 e superiores, essa arquitetura mudou: as notificações deixam de ser enviadas para a nuvem e passam a ser armazenadas diretamente no ambiente local (banco de dados) do TOTVS RM. Com isso, o cliente ganha total autonomia para definir o período de retenção das mensagens, podendo eliminá-las quando desejar por meio do processo de exclusão de notificações (). Para viabilizar esse novo padrão, foram disponibilizadas novas APIs no TOTVS RM, permitindo que o aplicativo acesse as mensagens diretamente da base local.

Aviso

Com este novo modelo de armazenamento, torna-se imprescindível garantir que o ambiente do TOTVS RM permaneça sempre online e estável. Recomendamos fortemente a execução frequente de rotinas de manutenção no banco de dados e um período de retenção das mensagens () para assegurar a total integridade e a alta disponibilidade dos dados.

**Fluxo de envio e armazenamento das notificações até a versão 12.1.2606:**

Neste modelo:

1. O Sistema TOTVS RM realiza o envio das notificações.
2. As informações são armazenadas e processadas na plataforma Microsoft Azure.
3. O aplicativo Meu eduCONNECT consulta os dados diretamente nos serviços hospedados no Azure.
4. As mensagens são disponibilizadas aos usuários conforme seu contexto de acesso.

**Fluxo de envio e armazenamento das notificações após a versão 12.1.2606:**

Neste modelo:

1. O Sistema TOTVS RM realiza o envio das notificações.
2. As informações passam a ser armazenadas diretamente no banco de dados do TOTVS RM.
3. O cliente passa a ter total autonomia sobre retenção e exclusão das mensagens.
4. As informações permanecem sob responsabilidade do ambiente local do cliente.

**Fluxo de transição da arquitetura:**

Durante o período de migração da arquitetura, o armazenamento das mensagens ocorre diretamente no banco de dados do TOTVS RM.

Entretanto, para manter compatibilidade com as versões atuais do aplicativo, os serviços hospedados no Microsoft Azure continuam sendo utilizados como camada intermediária de integração.

Nesse cenário:

1. O Sistema TOTVS RM realiza o envio das notificações.
2. As mensagens são armazenadas no banco de dados do TOTVS RM.
3. O Azure consulta as APIs disponibilizadas pelo TOTVS RM para recuperar as informações necessárias.
4. O aplicativo Meu eduCONNECT continua consumindo os serviços da plataforma Azure.
5. Os dados são apresentados ao usuário conforme seu contexto de acesso.

Essa estratégia permite uma migração gradual da arquitetura, reduzindo impactos para usuários e instituições durante o processo de transição.
