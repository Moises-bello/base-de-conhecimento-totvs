---
article_id: 360036293133
category: esocial - Periódicos
content_hash: b21cdc982b3fcdfade1acb1a2a6454803763293e4cc04025065900f17aea8acf
fetched_at: '2026-06-28T22:47:09.145392+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao transmitir S-1200, S-1202 ou S-2299 ocorre o
  erro 269: Rubrica de código #39;XXXX#39; e Identificador de tabela #39;YYYYY#39;
  não existe no cadastro do empregador para o período #39;ZZZZ-ZZ#39'
type: support-article
updated_at: '2024-06-25T16:30:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036293133-RH-RM-FOP-eSocial-Ao-transmitir-S-1200-S-1202-ou-S-2299-ocorre-o-erro-269-Rubrica-de-c%C3%B3digo-39-XXXX-39-e-Identificador-de-tabela-39-YYYYY-39-n%C3%A3o-existe-no-cadastro-do-empregador-para-o-per%C3%ADodo-39-ZZZZ-ZZ-39
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24413744826903) Tempo aproximado para leitura: 00:03:30 min**

**Ocorrência**Ao transmitir o evento S-1200 para o governo é retornado a inconsistência **Rubrica de código #39;XXXX#39; e Identificador de tabela #39;YYYYY#39; não existe no cadastro do empregador para o período #39;ZZZZ-ZZ#39**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24421159978647)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
 **Causa**Este erro ocorre quando é gerado no evento **S-1200, S-1202** ou **S-2299** uma rubrica cujo o início de validade não contempla o período de apuração indicado na *tag* **infoPerApur** ou o período de referência indicado na *tag* **perRef**  
  
**Solução**  
Para correção da ocorrência favor realizar os passos abaixo:

* **Início validade**

1. Verifique na mensagem de erro o código da rubrica e o período de referência indicados;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24421058628119)

2. Acesse o **Portal do Governo - Empregador - Tabelas  - Tabelas de Rubricas**,  identifique a rubrica que consta com erro e verifique qual sua validade;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24420868096279)

3. Caso a validade da rubrica seja posterior ao período do evento de remuneração, será necessário enviar um **S-1010** com período igual ou anterior à remuneração. Para isto, acesse**Folha de Pagamento | eSocial | Fila de Eventos** e realize a inclusão do XML ajustando para igual ou anterior a competência que contempla no erro. Gere, integre e transmita o evento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24421058639511)

4. Envie o XML o **S-1010** e após aceito envie **S-1200** novamente.

* **Identificador da tabela de rubricas**

1. É necessário verificar também se o Identificador da Tabela de rubrica, condiz com o que consta no Governo. No exemplo abaixo os valores que estão sendo enviados no XML de remuneração é rubrica = 0048 e identificador de tabelas = 1;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24421030659863)

2. Acesse o **Portal do Governo - Empregador - Tabelas  - Tabelas de Rubricas** identifique a rubrica que consta com erro e verifique qual é o identificador de tabelas. No exemplo abaixo a rubrica 0048, consta com identificador de tabelas = 000001;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24420868124951)

3. Para correção do identificador é necessário:

**Cliente TAF**

Gerar novamente o XML S-1010 da rubrica que consta com o identificador incorreto e integrar com o TAF governo;

Após integre o S-1200;

**Cliente Middleware**:

Acesse **Configurações - Parametrizador - eSocial - Integração com o Middleware - Outros Parâmetros** e informe a identificação de tabela de rubrica constante no governo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24413744836375)

Regere o XML S-1200 e integre com o Governo. 

**Saiba mais**  
Para mais informações acesse:   
[S-1010 - Tabela de Rubricas](http://tdninterno.totvs.com/display/public/LRM/S-1010+-+Tabela+de+Rubricas)
