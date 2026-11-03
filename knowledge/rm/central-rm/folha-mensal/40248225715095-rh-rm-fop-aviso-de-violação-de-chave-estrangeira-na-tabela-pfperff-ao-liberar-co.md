---
article_id: 40248225715095
category: Folha Mensal
content_hash: cf28b3f67e544dc4b29a8252d8197b143bcc5d5b63cf94473680f91b45d23a17
fetched_at: '2026-06-28T22:46:57.921938+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Aviso de violação de chave estrangeira na tabela PFPERFF ao
  liberar competência
type: support-article
updated_at: '2026-05-05T20:34:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40248225715095-RH-RM-FOP-Aviso-de-viola%C3%A7%C3%A3o-de-chave-estrangeira-na-tabela-PFPERFF-ao-liberar-compet%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40248248513943) Tempo aproximado para leitura: **00:02:33 min**  
  
**Ocorrência**  
Ao realizar o processo de liberação de competência no módulo Folha de Pagamento, o sistema apresenta o seguinte aviso: "Não foi possível transferir os dados da tabela PFPERFF. Existe algum campo nesta tabela cujo valor está violando a chave estrangeira. Verifique qual valor é este e cadastre o registro na tabela correspondente.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
O aviso ocorre porque, durante o processo de liberação de competência, o sistema realiza a transferência/cópia da movimentação e do período da ficha financeira normal (tabelas PFFINANC e PFPERFF) para a ficha financeira complementar (tabelas PFFINANCOMPL e PFPERFFCOMPL).

Este alerta de violação de dados indica que os registros que o sistema tenta copiar já existem nas tabelas complementares. Isso pode acontecer devido a importações prévias de fichas financeiras ou restaurações de dados.

Embora a mensagem seja apresentada, o processo de liberação de competência é concluído. O aviso serve para que o usuário valide se os dados nas tabelas complementares estão fidedignos. Caso os dados já estejam corretos na ficha complementar, a mensagem pode ser ignorada.

**Solução**  
Para que o sistema não emita mais o aviso, é necessário identificar e remover os registros duplicados:

1. Identifique quais registros já constam nas tabelas de ficha financeira complementar (PFFINANCOMPL/PFPERFFCOMPL) que são idênticos aos da ficha normal que está sendo liberada;
2. Solicite ao setor de T.I. ou ao DBA da empresa que realize uma consulta via banco de dados para localizar esses valores duplicados;
3. Após a conferência da integridade dos dados, realize a exclusão dos registros duplicados em uma das tabelas para que a transferência ocorra sem alertas em futuras liberações.

**Importante**

Uma vez que o processo de liberação de competência foi concluído, não será possível desfazê-lo ou posteriormente retornar para a competência anterior.

**Saiba mais**

[RH - RM - FOP - Liberação de competência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060636393-RH-RM-FOP-Libera%C3%A7%C3%A3o-de-compet%C3%AAncia)
