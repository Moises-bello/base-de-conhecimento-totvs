---
article_id: 360036104953
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 02eadeb27cc3eec09318f3f7c5434f489179e0d68d6d337d50e11e160f120386
fetched_at: '2026-06-28T22:38:33.143045+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - TMK - Histórico de Atendimento gera error.log - variable is not an object
  on TK273CARGAITEM(TMKA273A.PRW)
type: support-article
updated_at: '2021-04-28T15:54:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036104953-MP-TMK-Hist%C3%B3rico-de-Atendimento-gera-error-log-variable-is-not-an-object-on-TK273CARGAITEM-TMKA273A-PRW
---

**Ocorrência**

Ao entrar na rotina Agenda ou Consultar Histórico de Ligações gera error.log

**Ambiente**

Protheus  - Faturamento - a partir da versÃO 12.1.17  
   
 **Causa**

Erro de Binário.  
   
 **Solução**

Correção de binário e geramos uma versão release candidate.

Aplicamos uma correção em nosso binário e geramos uma versão release candidate.

Em teste nos nossos ambientes o erro foi sanado.

A orientação é que seja que seja atualizado o AppServer pela versão que disponibilizamos em nosso ftp :

Em : URL: [<ftp://totvscli@ftp.totvs.com.br/totvstec/Ariel/MTEC-3334/AppServer-13.2.3.46_RC2-win32-rpo32.zip>]

usuário: totvscli

senha: totvscli

Para o teste, proceda da seguinte forma:

* Pare o AppServer que será utilizado para testes
* Faça um backup deste AppServer.exe
* Descompacte o arquivo disponibilizado no FTP na pasta do AppServer
* Apague o arquivo console.log

Em seguida, inicie este AppServer
