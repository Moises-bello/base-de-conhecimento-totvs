---
article_id: 39825247087639
category: Requisições
content_hash: d5a2469a1bffdd30fac682fd0d98b8e44ac56f85f10f5b3eff0c949ff704baa5
fetched_at: '2026-06-28T22:47:25.273388+00:00'
product: rm
section_id: 1500000861382
source: central-rm
title: 'RH - RM - RHU - Requisições: Envio automático de e-mails'
type: support-article
updated_at: '2026-04-17T15:47:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39825247087639-RH-RM-RHU-Requisi%C3%A7%C3%B5es-Envio-autom%C3%A1tico-de-e-mails
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39825261262999) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Qual a parametrização necessária para realizar o envio automático de e-mails nas rotinas de Requisições do módulo de Gestão de Pessoas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **Todas as versões.**  
  
**Solução**  
Para que sejam disparados e-mails automáticos para Gestores nos processos de criação, aprovação, reprovação ou cancelamento de Requisições, as seguintes parametrizações deverão estar aplicadas no módulo de Gestão de Pessoas:

1. Preenchimento do Nome do usuário e Endereço do usuário no parametrizador do módulo de Gestão de Pessoas na guia Configurações | menu Parametrizador | Etapa E-mail

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39825261263895)

2. Definição do envio automático de e-mails nas rotinas de Requisições mediante marcação do parâmetro "Envio automático de e-mail" no parametrizador do módulo de Gestão de Pessoas na guia Configurações | menu Parametrizador | Etapa Requisições - 1

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39825247067543)

3. Cadastro de Funcionário do Gestor (Chefe) deverá possuir e-mail e usuário válidos preenchidos.

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39825261264791)

4. Envio global de e-mails deverá estar funcional. Para verificação acesse a parametrização global na guia Ambiente | menu Parâmetros | Parâmetros Globais e execute o processo de envio de Mensagem Teste clicando sobre o ícone de raio.

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39825247070999)

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39825261270167)

**Saiba Mais**

Para mais informações, acesse:

[RH - RM - RHU - Parametrizador RHU](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415356976919-RH-RM-RHU-Parametrizador-RHU)  
[Framework - Linha RM - Frame - Configurar Envio de E-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001046067-Framework-Linha-RM-Frame-Configurar-Envio-de-E-mail)
