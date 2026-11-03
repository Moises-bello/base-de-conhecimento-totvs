---
article_id: 37665158981143
category: SIGAACD - Automação e Coleta de Dados
content_hash: ca6530c825956dca5b81daa5e21476fbf33ade9378670f4ce2033c863b6e2482
fetched_at: '2026-06-28T22:39:12.775615+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Mestre de inventário
  não carrega no Meu Coletor
type: support-article
updated_at: '2026-01-14T12:35:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37665158981143-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Mestre-de-invent%C3%A1rio-n%C3%A3o-carrega-no-Meu-Coletor
---

O Mestre de inventário pode não abrir no Meu Coletor devido a mensagens de alerta como "Inventário já iniciado por outro contador ou finalizado".

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37665158972951) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Por que o Mestre de inventário não abre no Meu Coletor (ACDV035)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

* Para casos como esse é necessário entender se o mesmo retorna alguma mensagem de alerta, como por exemplo: "Inventário já iniciado por outro contador ou finalizado..."  
    
  Nesses tipos de situação é possivel Verifica no monitor do mestre de inventário na rotina ACDA030, se o mestre já foi finalizado por outro operador
* Outra possibilidade é que não esteja devidamente configurado, neste caso a documentação abaixo pode lhe auxiliar com um breve check-list de configuração:   
  [Backoffice (Linha Protheus) - SIGAACD - Como configurar o App Meu Coletor de Dados?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30317999783703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-configurar-o-App-Meu-Coletor-de-Dados)
* Caso ainda sim persista, por favor verifique e nos envie as informações abaixo:   
  - A versão do app (na tela inicial, clicando na engrenagem e indo na informação "**Sobre"**)  
    
  - Encaminhe os dados de ambiente via Central de Diagnósticos.    
  [Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)  
    
  - Verifique como utiliza os parâmetros MV\_INTDL, MV\_INTWMS e MV\_WMSNEW. Se algum desses estiver ativo é porque há controle de WMS e aí temos outras variaveis de nivel de WMS a validar (com o time de WMS).

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
