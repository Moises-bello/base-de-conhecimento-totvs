---
article_id: 24510713815959
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 8c0dc09959d3fdf31e4b45a3111aaa07eebb80c3070c364f64958c2b38e6000c
fetched_at: '2026-06-28T22:37:56.291064+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Ao disparar
  o JOB, o titulo ainda fique com status "A REGISTRAR" e não é enviado ao banco
type: support-article
updated_at: '2024-08-01T20:40:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24510713815959-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Ao-disparar-o-JOB-o-titulo-ainda-fique-com-status-A-REGISTRAR-e-n%C3%A3o-%C3%A9-enviado-ao-banco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24510713764119) Tempo aproximado para leitura: **00****:08:00 min** **Dúvida**Ao disparar o JOB FINA713, o titulo ainda fique com status "A REGISTRAR" e não é enviado ao banco  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Sugestão**

Verificar se existe algum problema no layout dos bancos utilizados no processo.

Procurar pelas expressões conforme exemplo a seguir:

Expressão - **CValToChar( \* 100)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24510713765143)

Caso tenha algum banco com tal expressão, necessário editar o layout com problemas.

Exemplo da mensagem que é apresentada no **console.log** quando esta com as TAGS necessárias ativas no **appserver.ini** que é responsável por executar o **JOB FINA713**

**[General]**  
**LogHttpFuncs=1**  
**tlpp\_rest\_log=1**  
**ConsoleMaxSize=300888999**  
**Consolelog=1**

**\*\*\* Warning - Mismatched parameters type calling FINA713 at parameter 1 - expected L->C**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24510713766551)

Segue o passo a passo para corrigir caso tenha algum layout com a expressão **CValToChar( \* 100)**

1- Acessa a rotina **FINA710 - Novo Gestor Financeiro**, acessar o **layout** e **Editar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24510703155479)

2- Colocar um conteúdo no campo "**Valor Abatimento**" e **Salvar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24510713769111)

3- Clicar em **Salvar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24510703161751)

4- Edite novamente o **layout**, e no campo "**Valor Abatimento**" cliquei na **engrenagem** e apague o conteúdo deixando como estava antes da alteração e **salvar** novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24510713771799)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24510703166359)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24510703167767)

E após isso poderá enviar novamente e não irá mais apresentar o erro no **console.log** ao disparar o **JOB FINA713**

**\*\*\* Warning - Mismatched parameters type calling FINA713 at parameter 1 - expected L->C**

**Saiba mais:**   
[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)
