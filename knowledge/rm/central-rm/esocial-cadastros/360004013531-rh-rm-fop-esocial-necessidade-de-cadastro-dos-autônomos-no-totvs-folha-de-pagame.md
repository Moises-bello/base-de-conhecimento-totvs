---
article_id: 360004013531
category: eSocial - Cadastros
content_hash: 9a5cf56fd561bf780246ca0e83befb41f3f0ba3e3807dbad43f281f4587da7af
fetched_at: '2026-06-28T22:47:14.528046+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Necessidade de cadastro dos autônomos no TOTVS Folha
  de Pagamento
type: support-article
updated_at: '2025-02-11T21:23:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004013531-RH-RM-FOP-eSocial-Necessidade-de-cadastro-dos-aut%C3%B4nomos-no-TOTVS-Folha-de-Pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24339501363863) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Preciso cadastrar todos os meus autônomos no TOTVS Folha de Pagamento?  
  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Não. Caso o autônomo esteja enquadrado em uma das categorias abaixo, deverá obrigatoriamente gerar o evento S-2300, sendo necessário seu cadastro no TOTVS Folha de Pagamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29916798134423)

Caso o autônomos possua categoria diferente das supracitadas, poderá ser transmitido somente seus eventos de remuneração. Neste caso, não há necessidade de cadastro no Folha de Pagamento, podendo o autônomo ser registrado como Externo ou no TOTVS Gestão Financeira. Assim, no momento da geração do XML dos eventos periódicos é necessário marcar a flag **Gerar Autônomos Fluxus/Externos** para que o sistema busque as informações de remuneração.

![](https://totvssuporte.zendesk.com/attachments/token/0rA38bwMNeaS05eqT3cRaHFjY/?name=inline1604144822.png)​

Caso utilize o Middleware, a flag supracitada não será exibida, pois o sistema já buscará automaticamente os autônomos do Fluxus/Externos na geração dos XMLs periódicos.  
  
**Importante**   
Para gerar os XMLs dos eventos periódicos referentes a autônomos, é necessário cadastrar e parametrizar os eventos de provento e desconto com suas devidas rubricas em: **Configurações | Parametrizador | Autônomos e Externos 1/2.**Para os autônomos carreteiros (categorias 711 e 712) deve ser feito o cadastro dos eventos e parametrização dos **Autônomos e Externos** **2/2.**

As informações sobre os autônomos que não fazem necessário o envio do S-2300 serão levadas na *tag* **infoComplem**.

Caso seja necessário geração de XML de autônomos de outras linhas de produto ou softwares terceiros, não é possível utilizar o Middleware, sendo necessário uso do TAF Padrão para consolidação dos eventos periódicos.  
  
**Saiba mais**Para maiores informações acesse:   
     • [Ativar Integração com o Middleware (eSocial do Futuro)](https://tdn.totvs.com/pages/releaseview.action?pageId=519722143)   
     • [Passos para ativação do Middleware e configuração dos relatórios de conferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056069833)  
     • [Parametrizador eSocial - Configurações Gerais](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719832)  
     • [Códigos de cálculo](http://tdn.totvs.com/pages/releaseview.action?pageId=452719279)
