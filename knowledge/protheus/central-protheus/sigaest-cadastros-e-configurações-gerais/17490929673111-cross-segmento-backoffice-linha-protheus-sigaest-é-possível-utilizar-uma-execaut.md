---
article_id: 17490929673111
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: af12e72a8d45a3d63dbf8f867c2098eae00a37837206efc4d8732e05748f8883
fetched_at: '2026-06-28T22:39:08.205747+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível utilizar
  uma ExecAuto com um Ponto de Entrada ?
type: support-article
updated_at: '2023-09-13T16:58:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17490929673111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-utilizar-uma-ExecAuto-com-um-Ponto-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17490919870103) Tempo aproximado para leitura: **00:01:47 min** **Dúvida**Precisamos utilizar uma ExecAuto porém como utilizar ela em conjunto com Pontos de Entrada dentro da Rotina ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

É importante esclarecer que a ExecAuto nada mais é do que uma forma de automatizar a digitação ou uma tarefa que normalmente o usuário faria pela rotina/tela principal do sistema, como incluir uma Transferência entre filiais, por exemplo.

A vantagem é que ele utiliza exatamente os mesmos campos, tabelas, fluxos e principalmente validações que teria ao digitar na tela. Por exemplo, você não consegue efetivar uma transferência entre filiais via ExecAuto se passar um campo em branco que é obrigatório na tela do sistema.

Já os pontos de entrada servem para manipular, de alguma forma, as informações e fluxos do sistema, sejam em rotinas padrão (o mais comum) ou em customizadas.

Sabendo que a ExecAuto segue o mesmo fluxo do processo realizado em tela, basta ter o ponto de entrada compilado no ambiente que naturalmente ele vai ser acionado conforme o fluxo da rotina, não sendo necessário realizar tratamento especifico.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
