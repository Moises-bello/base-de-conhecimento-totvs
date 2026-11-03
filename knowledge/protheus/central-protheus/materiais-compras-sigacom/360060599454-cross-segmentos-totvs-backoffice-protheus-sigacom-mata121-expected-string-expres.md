---
article_id: 360060599454
category: Materiais - Compras (SIGACOM)
content_hash: b454c90b6e95d5c39b6fbfd8e01e1e93b8e53d440cffaffe72512640656e3412
fetched_at: '2026-06-28T22:41:20.158013+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA121 expected string
  expression in FieldPut C7_WF in file D:\bamboo-agent-5
type: support-article
updated_at: '2022-05-16T23:03:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060599454-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA121-expected-string-expression-in-FieldPut-C7-WF-in-file-D-bamboo-agent-5
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min**  
**Dúvida**Ao incluir um pedido de compras, o sistema apresenta erro fatal expected string expression in FieldPut C7\_WF in file D:\bamboo-agent-5

**Ambiente**Microsiga protheus - Compras - Versão 12

**Solução**Este incidente ocorre, pois o campo C7\_WF não é nativo no SX3, porem caso necessário implementar validações de workflow no pedido de compras, a criação do campo C7\_WF na tabela SC7 deve obrigatoriamente ser do tipo lógico, devido integração com o campo C8\_WF, validado pela tabela cotação (SC8).

1. No módulo SIGACFG, acesse o menu Base de dados> dicionário> base de dados> dicionário de dados. Filtre a tabela SC8>C8\_WF, salve as configurações em um arquivo de imagens;

2. Acesse a tabela SC7. Caso o campo C7\_WF já exista no arquivo SX3, exclua-o e efetue nova inclusão conforme modelo C8\_WF.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
