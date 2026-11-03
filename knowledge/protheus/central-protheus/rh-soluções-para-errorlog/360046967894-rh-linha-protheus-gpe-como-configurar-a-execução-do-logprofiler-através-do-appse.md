---
article_id: 360046967894
category: RH - Soluções para error.log
content_hash: 92ce1546137642a27881f6af1d6ff09d4bf17466687031e60dba4e329598fed1
fetched_at: '2026-06-28T22:44:08.810468+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar a execução do LogProfiler através
  do appserver.ini
type: support-article
updated_at: '2025-08-21T18:50:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046967894-RH-Linha-Protheus-GPE-Como-configurar-a-execu%C3%A7%C3%A3o-do-LogProfiler-atrav%C3%A9s-do-appserver-ini
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34352652082839)** Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**Como configurar a execução do LogProfiler através do appserver.ini?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) – Gestão de Pessoal – A partir da versão 12.  
  
**Solução**Existem situações onde pode ser solicitado pelo Suporte um log mais detalhado. Um desses logs é o LogProfiler, utilizado principalmente para detectar problemas de lentidão. Segue abaixo o procedimento para configuração no appserver.ini para sua correta geração:

**Nota:****O procedimento deve ser executado em um Appserver dedicado e em modo exclusivo, ou seja, onde nenhum outro usuário esteja acessando o ambiente, e nenhum *Job* esteja em execução.**- Primeiramente, pare o serviço do **Appserver**  
- Abra o arquivo **appserver.ini** deste *Server* e inclua, na seção do **ambiente,** o comando **LogProfiler=1**. Exemplo:

|  |
| --- |
| `[Environment]`  `...`  `LogProfiler=1` |

- Certifique-se que existe, no arquivo appserver.ini, na seção **[General]**, a linha **Consolelog=1**. Se não existir, insira esta linha;  
- Na pasta Appserver, renomeie o arquivo **console.log** para **console.bak;**  
- Reinicie o serviço do Appserver;  
- Acesse apenas a rotina em que está ocorrendo a lentidão;  
- Feche o Smartclient;  
- Pare o serviço do Appserver;  
- Renomeie o novo arquivo **console.log** gerado para **console\_lentidao.log;**  
- Reinicie o serviço do Appserver;  
- Envie os arquivos **console\_lentidao.log** e **console.bak** para o suporte avaliar.

**Saiba Mais:**Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>
