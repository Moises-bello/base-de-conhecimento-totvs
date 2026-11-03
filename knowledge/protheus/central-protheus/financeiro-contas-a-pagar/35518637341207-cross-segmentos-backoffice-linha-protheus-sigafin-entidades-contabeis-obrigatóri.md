---
article_id: 35518637341207
category: Financeiro - Contas a Pagar
content_hash: e373f2f9a7c9a6401b3f60fe9e6183b02a3c6d95f65b8bdd96a09be0f2a19cef
fetched_at: '2026-06-28T22:38:08.443656+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  - Entidades Contabeis
  obrigatórias na inclusão de um titulo
type: support-article
updated_at: '2026-06-12T17:22:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35518637341207-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Entidades-Contabeis-obrigat%C3%B3rias-na-inclus%C3%A3o-de-um-titulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35518637286551) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
No **plano de contas**, é possível **habilitar a obrigatoriedade das entidades contábeis**, como **Centro de Custo**, **Classe de Valor** ou **Item Contábil**. Dessa forma, durante a **inclusão de um título**, o usuário **somente conseguirá salvar o registro** se os campos obrigatórios estiverem corretamente preenchidos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
O sistema permite definir **entidades contábeis obrigatórias** diretamente no **plano de contas (CTBA020)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35518596387095)

No entanto, durante a **inclusão de títulos**, o **preenchimento das entidades não é obrigatório por padrão (Campos obrigatórios contém o** **\*****)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35518637296919)

Assim, quando o cliente define uma entidade como obrigatória e informa o **campo de conta corrente**, o sistema passa a considerar também a obrigatoriedade conforme configurado no plano de contas, devido as validações das tabelas SE1/SE2 inseridas no configurador:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35518637296791)

Por outro lado, **caso nenhuma conta seja informada**, o sistema **permite o salvamento do título normalmente**, sem exigir o preenchimento do campo de conta, devido ao uso não obrigatório da conta contabil na inclusão do titulo.

Dessa forma, no comportamento padrão do sistema, não há obrigatoriedade de preenchimento da conta contábil na inclusão de títulos financeiros, também em outros módulos que não o Contábil.

A exigência desse campo deve ser configurada conforme a necessidade do negócio, por meio do Configurador, ajustando o respectivo campo na tabela financeira (ou na tabela do módulo correspondente) para torná-lo obrigatório via dicionário de dados (SX3).
