---
article_id: 40914935675927
category: Financeiro - Contas a Receber
content_hash: 5008420adcc9276881bad1bd527b3cd676448ce7b0ec58d945550b729cd91517
fetched_at: '2026-06-28T22:38:13.823042+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro (SIGAFIN) -
  Mensagem de tipo inexistente ao utilizar o título NDF no Contas a Receber
type: support-article
updated_at: '2026-06-02T16:52:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40914935675927-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-SIGAFIN-Mensagem-de-tipo-inexistente-ao-utilizar-o-t%C3%ADtulo-NDF-no-Contas-a-Receber
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40914935647127)** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Ao tentar criar um título no Contas a Receber utilizando o tipo NDF, que já se encontra cadastrado na tabela genérica SX5, o sistema impossibilita a gravação e apresenta uma mensagem informando que o tipo de título não existe.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40914921157783)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as releases  
  
**Solução**

O título NDF (Nota de Débito de Fornecedor) é destinado à devolução de crédito ao fornecedor e, por regra de negócio do sistema, a sua utilização está vinculada ao módulo de Contas a Pagar. Por esse motivo, o tipo NDF não é permitido na rotina FINA040 (Contas a Receber), não sendo possível a sua inclusão nesse módulo.

Quando a necessidade for registar um crédito para o cliente, o procedimento correto é a utilização de uma NCC (Nota de Crédito ao Cliente), que foi desenvolvida especificamente para esse tipo de operação no Contas a Receber.

Dessa forma, caso seja necessário utilizar o tipo NDF, existem duas alternativas dentro do padrão do sistema:

* Inclusão manual do título no módulo Contas a Pagar;
* Geração do título por meio do processo padrão de devolução de compras, com uma TES que gere duplicata ao financeiro (Contas a Pagar) quando aplicável.

Portanto, o comportamento apresentado é esperado e está de acordo com as regras de utilização previstas para cada tipo de título no sistema.
