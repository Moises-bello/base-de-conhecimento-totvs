---
article_id: 4408218946199
category: Suricato
content_hash: 2cd8940fee68d28f99574a9933f4c1c3cf3d85be2935021047f862813fefccef
fetched_at: '2026-06-28T22:46:26.402339+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: RH - RM - PTO - Erro Timeout nas rotinas de integração Suricato x Automação
  de Ponto
type: support-article
updated_at: '2025-09-05T19:42:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408218946199-RH-RM-PTO-Erro-Timeout-nas-rotinas-de-integra%C3%A7%C3%A3o-Suricato-x-Automa%C3%A7%C3%A3o-de-Ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19408982148759) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao executar algumas rotinas e processos no Automação de Ponto que envolvem integração com Suricato, é apresentado erro de Timeout, o que fazer?

Erro: Erro no Agente de Envio (mensagem assíncrona). The operation has timed out  
**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Causa**O incidente ocorre pois na execução do processo e/ou rotina ficam executando por um determinado tempo e este é ultrapassado pelo tempo de execução padrão do banco de dados.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Deverá acessar o local de instalação do RM, pasta RM.Net. Normalmente o caminho padrão é o C:\TOTVS\CorporeRM\RM.Net, mas pode ser que esteja diferente dependendo de como a instalação do sistema foi realizada.

**2.** Na pasta RM.Net procurar e editar os arquivos:

* Rm.Host.exe.config
* Rm.Host.Service.exe.config
* Rm.exe.config
* Rm.Host.JobRunner.exe.config

**3.** Deverá inserir a tag **<add key="ConEAITimeOut" value="390000000"/>** conforme exemplo abaixo:

![img1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408224548759)

A tag de timeout deve ser inserida dentro da estrutura <appSettings></appSettings>.

**Importante**Após ajustes efetuados, deverá reiniciar o serviço do RM apagando o arquivo \_broker.dat.

**Saiba mais**Para maiores informações de como reiniciar o serviço do RM acesse o link [reiniciar host](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000095827-RM-Frame-Reiniciar-Host).
