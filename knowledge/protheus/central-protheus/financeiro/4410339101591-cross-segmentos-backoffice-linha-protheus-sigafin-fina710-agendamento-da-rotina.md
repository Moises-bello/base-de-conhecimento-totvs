---
article_id: 4410339101591
category: Financeiro
content_hash: 473660f3ac4616b6c1ad272e47eaa4f0bb7d876a82036739a0ec61713de12cdb
fetched_at: '2026-06-28T22:38:03.053290+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710  - Agendamento
  da Rotina (WIZARD configuração)
type: support-article
updated_at: '2024-07-26T19:32:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410339101591-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Agendamento-da-Rotina-WIZARD-configura%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25200047948055) Tempo aproximado para leitura: **00:05 min****Dúvida**Como gerar agendamento da Rotina **FINA710** (Novo gestor Financeiro )?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA710  -  A partir da versão 12.1.33  
  
**Solução**O **Wizard (****Job FINA711)** será configurado no **Schedule** do módulo **Configurador** do ambiente em uso.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410338734103)  
O **JOB** será configurado para execução com intervalos no padrão de 15 minutos

A alteração do intervalo de execução pode ser realizado diretamente pelo agendamento do **schedule** no **Configurador** - **SIGACFG**. (Saiba mais)

Caso não existir o **AGENT** configurado, após a criação do Schedule (**Agendamento da Rotina FINA710**) será necessário criar um **AGENT** para o correto funcionamento conforme a orientação abaixo:

![20220524_153108.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6303103347991)

**Importante**  
É necessário estar com o serviço de *Schedule* ativo no ambiente para que o Job seja executado.

**Saiba mais**

[Novo Painel Gestor](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335) **[-](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)** [FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA710 - Novo Gestor Financeiro - Tempo de Execução](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410338012055-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Novo-Gestor-Financeiro-Tempo-de-Execu%C3%A7%C3%A3o?source=search)  
[Wizard de configuração - FINA711](https://tdn.totvs.com/pages/releaseview.action?pageId=602610545)

[PSIGAPON0037 - MSSCHEDULE - Procedimento para leitura automática das marcações do ponto através da configuração do Schedule.](https://tdn.totvs.com/pages/viewpage.action?pageId=233735618)
