---
article_id: 4410336871575
category: Financeiro - Novo Gestor Financeiro
content_hash: 8c3b7bb00ea0be25ae59346647018f8e70518c521934edaa80f65e02dec7950e
fetched_at: '2026-06-28T22:37:41.464232+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710  - HELP:FINA710JOB
type: support-article
updated_at: '2026-03-04T18:56:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410336871575-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-HELP-FINA710JOB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37510953806871) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
No módulo Financeiro, ao acessar a rotina FINA710, mensagem **HELP: FINA710JOB**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410326912663)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA710  - A partir da versão 12.1.33

**Causa**  
O JOB não concluiu o processo, ou não foi configurado em ambiente correto.

O JOB é criado automaticamente ao acessar a rotina **FINA710 Novo Gestor Financeiro**, pela primeira vez, desde que as informações do appserver.ini estejam configuradas corretamente conforme na seção **GENERAL**. Deve-se incluir a chave “**App\_Environment**”, cujo valor deve ser o nome do ambiente em que os serviços rodarão.   
Na seção **DRIVERS**, deve-se habilitar a porta multiprotocolo na chave **“MultiProtocolPort”** com o valor = 1.  
Por padrão, a conexão SSL está ativa na porta multiprotocolo, os detalhes das configurações estão disponíveis na documentação **Application Server** - Porta Multiprotocolo.  
Para desabilitar a conexão por SSL é necessário informar a chave **“MultiProtocolPortSecure = 0”**  
  
**Solução**  
**1.** Inicialmente avaliar se as tabelas **F75 e F76** estão com o mesmo nível de compartilhamento.

**2. A**valiar se as tabelas **F75 e F76** foram populadas.  
  
3**.** Validar se o agente está iniciado no **Schedule - Módulo Configurador - (Caso não utilize o Smart Schedule).**

**4. Limpar tarefas na rotina schedule, pois tarefas travadas podem ocasionar falhas na execução de outros agendamentos e até mesmo do próprio FINA711.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38528899259415)**  
  
5**.** Iniciar o **JOB FINA711** manualmente pelo **Schedule** e agendar o horário de execução automática.  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Agendamento da Rotina (WIZARD configuração)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410339101591-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Agendamento-da-Rotina-WIZARD-configura%C3%A7%C3%A3o)  
   
6**.** Verificar se o parâmetro **MV\_TFCJOBT**foi preenchido**.**  
   
7**.** Acessar novamente a **rotina FINA710 após finalizar a execução do JOB FINA711**

**Importante:**  
O ambiente deverá estar atualizado **(Módulo Financeiro(06)-DBacess - SmartClient - AppServer - Lib)**

**Saiba mais**

[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Configuração e Funcionalidade do Novo Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7019775569047)
