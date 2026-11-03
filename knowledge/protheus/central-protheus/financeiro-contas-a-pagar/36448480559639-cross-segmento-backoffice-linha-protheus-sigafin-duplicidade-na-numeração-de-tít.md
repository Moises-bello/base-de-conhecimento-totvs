---
article_id: 36448480559639
category: Financeiro - Contas a Pagar
content_hash: 75199b976411f23e5751d7113f810a79ece55fbdc698c361168358eeec57fd5a
fetched_at: '2026-06-28T22:38:06.943663+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Duplicidade na numeração
  de títulos entre as filiais
type: support-article
updated_at: '2025-11-19T18:09:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36448480559639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Duplicidade-na-numera%C3%A7%C3%A3o-de-t%C3%ADtulos-entre-as-filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36448510184599) Tempo aproximado para leitura: **08:00 min**

**Dúvida:**  
Geração de duplicidade na numeração de títulos entre as filiais do mesmo grupo

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.33 e superiores  
  
**Solução:**

O sistema pode aceitar numerações de títulos iguais entre empresas diferentes quando o compartilhamento é **exclusivo.**

Isso acontece porque a validação de duplicidade não considera apenas o número do título, mas sim **toda a chave única** definida no índice principal da tabela. Para que o sistema identifique um título como duplicado, **todos os campos da chave precisam ser exatamente iguais**.

**Exemplo prático:**

> Em um ambiente, utilizando a rotina FINA050 onde a SE2 é exclusiva, a chave do índice único é composta por: **(****E2\_FILIAL****+****E2\_PREFIXO****+****E2\_NUM****+****E2\_PARCELA****+****E2\_TIPO****+****E2\_FORNECE****+****E2\_LOJA****)**
>
> Assim, se em minha empresa ficticia 99, filial 01, eu tenho um título com a seguinte combinação:  
> ![](https://centraldeatendimento.totvs.com/hc/article_attachments/36448510186775)
>
> Essa é a chave completa do meu titulo:
>
> **(01** **+** **TST** **+** **0000001** **+** **01** **+** **NF** **+** **001** **+** **01)**

Caso eu tente lançar outro título **com a mesma combinação**, o sistema identificará como duplicidade.

Por outro lado, se **qualquer parte da chave for diferente** — como filial, tipo, fornecedor, loja etc. — o sistema entende que **não é o mesmo título**, mesmo que o número do título seja igual, e, portanto, permite o lançamento sem erro.

#### **Como consultar os índices da tabela?**

1. Acesse o **Configurador (SIGACFG)**.
2. Localize a tabela — no exemplo, a **SE2**, que guarda os títulos do Contas a Pagar (FINA050).
3. Selecione **Índices**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36448510190359)
