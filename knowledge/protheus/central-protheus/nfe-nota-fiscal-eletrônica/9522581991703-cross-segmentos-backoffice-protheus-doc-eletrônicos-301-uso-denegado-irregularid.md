---
article_id: 9522581991703
category: NFe - Nota Fiscal Eletrônica
content_hash: 55aa1056e98594884ca0b893097e31838343d7e6dfcee381902969b5b9c25a3e
fetched_at: '2026-06-28T22:40:03.828909+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 301: Uso Denegado:
  Irregularidade fiscal do emitente'
type: support-article
updated_at: '2025-06-25T12:25:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9522581991703-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-301-Uso-Denegado-Irregularidade-fiscal-do-emitente
---

**Dúvida**Como solucionar o retorno: 301: Uso Denegado: Irregularidade fiscal do emitente  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Uma NF-e pode ser denegada por irregularidade fiscal do emitente.

Assim, se uma empresa que estiver em situação regular emitir uma NF-e, mas informar nos dados do destinatário uma Inscrição Estadual baixada, então essa nota está sujeita a ser denegada.

Neste caso, o emitente pode corrigir os dados do destinatário e emitir uma nova nota.

Lembrando que a denegação é diferente da rejeição. Uma nota que foi rejeitada pode ser corrigida e retransmitida com o mesmo número.

**Uma nota que foi denegada não pode ser retransmitida com o mesmo número**.

O que o emitente pode fazer é corrigir os dados do destinatário e emitir uma nova nota com uma nova numeração.

* **O correto para Sefaz é consultar o CCC:**

Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual);

* **Cadastro Centralizado de Contribuinte (CCC):**

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11705318944535)

* **Processo:**

No sistema **Protheus** a nota Denegada deve ser excluídas para que o sistema estorne as movimentações da nota (estoque, financeiro, contabilização, entre outros processos).

Com essa ação não levará valores para outras obrigações acessórias, como Apurações de ICMS e IPI ou arquivos magnéticos como Sped Fiscal, EFD Contribuições, entre outros.

No Livro Fiscal existe tratamento para que a nota fique como denegada, pois essa numeração não pode ser utilizada por já constar na base da SEFAZ. Dessa forma, esse número não pode ser mais utilizado, cancelado ou inutilizado.

Com isso, essa nota ficará com situação de **“Denegada”**.

No Livro Fiscal existe tratamento para que esta nota fique como denegada, no campo**F3\_CODRSEF** que verifica se o código de retorno foi o citado acima, então retorna a mensagem para o livro (MATR930).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33041148082071)

<http://tdn.totvs.com/pages/viewpage.action?pageId=134152528>
