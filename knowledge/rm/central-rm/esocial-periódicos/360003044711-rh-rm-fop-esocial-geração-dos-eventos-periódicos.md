---
article_id: 360003044711
category: esocial - Periódicos
content_hash: 38c866a9a862cab345a3b594b89dedbfdf56c5172d89cfa73132f25b6a0b0c79
fetched_at: '2026-06-28T22:47:09.409234+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Geração dos eventos periódicos
type: support-article
updated_at: '2024-09-23T12:12:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003044711-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-dos-eventos-peri%C3%B3dicos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26556641216791) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**  
Como gerar os eventos da 3ª fase do eSocial (eventos periódicos - S-1200 / S-1202 / S-1207 / S-1210 / S-1260 / S-1270 / S-1280 / S-1298 / S-1299) no TOTVS Folha de Pagamento?  
  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Para os eventos periódicos **não há geração automática de gatilhos**. O processo a ser seguido é:  
1. Cadastrar o período de apuração em **eSocial | Período de Apuração**;  
2. Acessar o menu **eSocial | Gerar XML**, na tela de geração dos eventos periódicos informe o período de apuração desejado e selecione os eventos desejados para geração. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006798371)

3. Para visualizar os eventos gerados, acesse o módulo **eSocial | Eventos Periódicos.**

**Importante**  
Deve-se observar a data informada no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 1/7** campo **Data de Obrigatoriedade/Adesão ao eSocial | Periódicos**. O sistema valida esta data para geração dos eventos. Desta forma, caso queira realizar testes na produção restrita, é necessário informar uma data anterior ao período de apuração para que sejam gerados os eventos.

**Saiba mais**  
Para maiores detalhes sobre a parametrização acesse:

* [Orientações eventos periódicos](http://tdn.totvs.com/pages/releaseview.action?pageId=360451503)
* [Período de apuração](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719936)
* [Eventos periódicos](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719672)
* [Gerar XML periódicos](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719232)
