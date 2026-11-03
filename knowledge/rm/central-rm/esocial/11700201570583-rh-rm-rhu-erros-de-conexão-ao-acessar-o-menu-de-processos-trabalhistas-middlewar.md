---
article_id: 11700201570583
category: eSocial
content_hash: 877a75d37dc98dbf8bde668a37b709f1d6f02b813ec6b0864d657b60c725d9ad
fetched_at: '2026-06-28T22:47:15.438501+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: RH - RM - RHU - Erros de conexão ao acessar o menu de Processos Trabalhistas
  - Middleware
type: support-article
updated_at: '2025-08-22T20:40:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11700201570583-RH-RM-RHU-Erros-de-conex%C3%A3o-ao-acessar-o-menu-de-Processos-Trabalhistas-Middleware
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15863918754327) Tempo aproximado para leitura: **00:01:30** **min** **Dúvida**Ao acessar o menu de Processos Trabalhistas, aparece mensagem(s) de erro de conexão, o que fazer quando é utilizado o Middleware?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas -**12.1.34.263**, **12.1.2205.211**, **12.1.2209.155** e superiores.  
  
**Solução**

Geralmente os incidentes relacionados a conexão, ocorre devido a parametrização de integração. Para avaliar, siga os passos abaixo:

1. Acesse no modulo de Folha de Pagamento o menu **Configurações | Parametrizador** e selecione **item e Social | Configurações Gerais**, clique em avançar. Avance até a etapa **Integração com TAF** aba **Outros Parâmetros**, e confira se os campos de Servidor e Porta já estão preenchidos, conforme as orientações abaixo:  
     
   **Servidor/Porta API:** Servidor e porta onde o serviço de API's RM está sendo executado. (APiPort do Host RM. No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a HttpPort). **Servidor/Porta APP:** Servidor e porta onde o aplicativo THF está sendo executado. (Caso o servidor seja o Host RM, informar a HttpPort).   **![](https://centraldeatendimento.totvs.com/hc/article_attachments/26718534410903)**  
   Caso tenha dúvidas do que informar, acesse a etapa **Integração com Middleware**, clique na aba **Outros****Parâmetros** e copie os dados informados de servidor e porta API e APP, e informe na aba de **Outros****Parâmetros** da etapa **Integração com TAF.**   **![](https://tdn.totvs.com/download/attachments/536720973/image2020-7-2_17-2-1.png?version=1&modificationDate=1593722445300&api=v2)**

Para mais informações acesse o link a seguir**: [O que é e como configurar a HttpPort e ApiPort.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-?source=search)**

 

Para fazer o envio das informações, deve ter a configuração da integração do webservice do RM, Para configura-lo acesse o link a seguir: **[Como Habilitar Webservice via RM Host](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003035312-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-Como-Habilitar-Webservice-via-RM-Host?source=search).**

Caso a integração já esteja habilitada, avalie se a tag **DefaultDB** nos arquivos **RM.Host.Service.exe.config** e **RM.Host.exe.config** estão com o nome (Alias) da base de dados em que irá cadastrar as informações do Processo Trabalhista. Exemplo: Nome do Alias = CorporeRM

*Tag: <add key ="DefaultDB" value="CorporeRM" />*

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15863949570839)

**Saiba Mais:**

Para maiores informações, acesse:

[- RH - RM - RHU - Como habilitar a funcionalidade de cadastro dos Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11452008640663-TOTVS-RH-Linha-RM-RHU-Como-habilitar-a-funcionalidade-de-cadastro-dos-Processos-Trabalhistas?source=search)  
[- RH - RM - FOP - eSocial - Passos para ativação do Middleware e configuração dos relatórios de conferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056069833--RH-RM-FOP-eSocial-Passos-para-ativa%C3%A7%C3%A3o-do-Middleware-e-configura%C3%A7%C3%A3o-dos-relat%C3%B3rios-de-confer%C3%AAncia)

[- RH - RM - RHU - Erros de conexão ao acessar o menu de Processos Trabalhistas (TAF e Smart)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11571907280663-TOTVS-RH-Linha-RM-RHU-S-2500-Erro-de-conex%C3%A3o-ao-acessar-o-menu-de-Processos-Trabalhistas?source=search)

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
