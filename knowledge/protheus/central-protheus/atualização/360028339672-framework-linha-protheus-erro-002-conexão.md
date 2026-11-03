---
article_id: 360028339672
category: Atualização
content_hash: 12291abbe711d7d681d52867b681b75c7d3260c357efc3ab8364ce9d4ac4a668
fetched_at: '2026-06-28T22:42:21.236874+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - ERRO 002 - Conexão
type: support-article
updated_at: '2024-03-26T13:23:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028339672-Framework-Linha-Protheus-ERRO-002-Conex%C3%A3o
---

**Dúvida**Quais medidas tomar quando ocorrer o erro de código ERR0002?  
   
 **Ambiente**Protheus - Servidor de Aplicação - Todas as versões  
   
**Solução**Ao tentar iniciar o SmartClient, ocorre o erro:  
  
ERR0002: Não foi possível estabelecer conexão com TOTVS Application Server. Verifique suas configurações (rede ou TOTVS SmartClient) ou contate o administrador do sistema.  
  
![ERR0002.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028982132)  
  
Para corrigir este erro, seguem abaixo os procedimentos:  
  
O **ERRO 002** é característico de um problema de comunicação entre o SmartClient e o Appserver. As principais causas e verificações são:  
  
**01. O Servidor de Aplicação não está iniciado, ou está travado:** Faça um teste reiniciando o serviço do Appserver.  
**02. Problema na comunicação de rede:** A comunicação de rede entre o computador onde o SmartClient foi iniciado e o servidor pode não estar OK. Verifique a comunicação de rede, e faça um teste abrindo o SmartClient no próprio servidor.  
**03. Configuração incorreta do IP e Porta nos arquivos de inicialização:** Verifique no servidor qual é o endereço IP do mesmo. Abra o arquivo appserver.ini do Servidor de Aplicação, e localize a seção [TCP]. Verifique a porta na linha Port=. Abra o arquivo smartclient.ini do SmartClient em que o erro ocorre, localize a seção [TCP], e confirme nas linhas Server= e Port= se o endereço e porta conferem com o que foi verificado no Appserver.
