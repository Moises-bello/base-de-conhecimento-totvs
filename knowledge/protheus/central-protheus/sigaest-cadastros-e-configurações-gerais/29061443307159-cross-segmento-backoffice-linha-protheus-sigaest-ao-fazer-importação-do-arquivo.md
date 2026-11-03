---
article_id: 29061443307159
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: d9d3979a3aabc88c105a023c820d7e2cb2d3ffd894fd9f7c654ed7e832baf0a1
fetched_at: '2026-06-28T22:39:08.026857+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao fazer importação
  do arquivo Mile para mais de uma filial é gerado o help: "Já gravado: Já existe
  registro com esta informação"'
type: support-article
updated_at: '2025-03-12T12:41:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29061443307159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-fazer-importa%C3%A7%C3%A3o-do-arquivo-Mile-para-mais-de-uma-filial-%C3%A9-gerado-o-help-J%C3%A1-gravado-J%C3%A1-existe-registro-com-esta-informa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29061443298327) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

Ao fazer uma importação de dados via Mile para mais de uma filial é gerado o help: "Já gravado: Já existe registro com esta informação", como fazer para corrigir?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

No Mile, não é possível passar conteúdo para o campo "filial", pois o sistema ***sempre utiliza a** **Filial Corrente*** no momento do processamento.

Mesmo que o compartilhamento de tabelas seja configurado de forma exclusiva, o sistema considerará a filial corrente para a importação.

Dessa forma, será necessário inserir os dados diretamente em cada filial ou utilizar um execauto para realizar a importação dos dados de forma automatizada.

Para mais informações sobre o Mile acesse nossa documentação:

***<https://tdn.totvs.com/x/kYQbCQ>***

**Saiba Mais:**  
*[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
