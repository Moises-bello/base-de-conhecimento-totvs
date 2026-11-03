---
article_id: 20401089632919
category: Faturamento - Cadastros
content_hash: 42ca7d36de9a11b319f40cf56e2daf4d4fc9d63aac1f0f5a946a5bda9a61af7d
fetched_at: '2026-06-28T22:38:36.678554+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Numeração incorreta
  em integrações EAI
type: support-article
updated_at: '2024-01-08T15:55:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20401089632919-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Numera%C3%A7%C3%A3o-incorreta-em-integra%C3%A7%C3%B5es-EAI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20401075496599) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como arrumar uma numeração incorreta em integrações EAI?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**1 - Identifique como se fosse um cadastro manual, qual tabela é a reponsável pelo registro que está tentando integrar. Exemplos:

* MATA410 - Pedidos de venda: Tabela SC5
* CRMA980 - Cadastro de Clientes: Tabela SA1

2 - Ajuste a numeração pelo License Server: **[FAT0046 Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](https://tdn.totvs.com/x/P4YKDg)**

3 - Verifique na tabela responsável pela numeração, se o campo de código está com as configurações no padrão. Exemplos:

* Se integrar um pedido de venda, cheque se o campo "Código (C5\_NUM)" está no padrão.
* Se integrar um cliente, cheque se o campo "Código (A1\_COD)" está no padrão.

4 - Abra o XML ou JSON de envio EAI e busque pela tag <InternalId>.

Ao encontrar, filtre pelo valor encontrado no campo/tabela "Identificador externo (XXF\_EXTVAL)". Caso retorne algum dado, significa que já foi integrado anteriormente a mesma transação, então o sistema sempre vai alterar o registro criado na época e não criar um novo, dando a impressão do erro da numeração

Quando isso ocorrer, há duas soluções: No sistema origem que leva ao Protheus muda-se a tag <InternalId>, ou na rotina " De/para de mensagem única (APCFG070)" do configurador excluir o de/para de mensagem única para que o sistema inclua um registro novo e não altere um já criado, perdendo assim o histórico e possibilidade de alteração via EAI do registro antigo.
