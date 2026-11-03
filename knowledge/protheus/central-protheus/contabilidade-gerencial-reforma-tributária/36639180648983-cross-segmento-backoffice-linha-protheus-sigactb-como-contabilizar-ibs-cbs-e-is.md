---
article_id: 36639180648983
category: Contabilidade gerencial - Reforma Tributária
content_hash: 91d78c9ffb3c82a6f918d116c021c6ea334cbb13d5a083c82bae7bf16b7dd192
fetched_at: '2026-06-28T22:40:29.672999+00:00'
product: protheus
section_id: 37095816599831
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como Contabilizar IBS,
  CBS e IS?
type: support-article
updated_at: '2026-01-16T15:01:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36639180648983-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-Contabilizar-IBS-CBS-e-IS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36639210358679) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Como realizar a contabilização dos novos impostos da Reforma Tributária (**IBS, CBS e IS**) no módulo de Contabilidade Gerencial (SIGACTB) do Protheus, utilizando as duas metodologias disponíveis?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - A partir da versão 12.1.2210

**Visão geral**

Esta documentação detalha as duas formas possíveis de realizar a contabilização dos novos tributos Imposto sobre Bens e Serviços (**IBS**), Contribuição Social sobre Bens e Serviços (**CBS**) e Imposto Seletivo (**IS**) no sistema.

O módulo SIGACTB foi atualizado para contemplar a contabilização destes impostos por meio de duas opções: por **Classificação do Tributo** ou por **Sigla do Tributo**.

**Conteúdo Principal**

As regras e comportamentos apresentados nesta documentação aplicam-se a:

* Lançamentos de entrada (base para os exemplos).
* Lançamentos de saída.
* Lançamentos de exclusão.
* Lançamentos em modo *offline*.

Para que o processo ocorra de maneira adequada, é imprescindível que o ambiente esteja atualizado de acordo com o último pacote Backoffice:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=334342777>

A contabilização dos novos impostos pode ser feita de duas formas:

**1. Contabilização com Base na Classificação do Tributo**

Esta modalidade foi desenvolvida para utilizar a função **CTBVLTRIB** diretamente nos lançamentos padrão. O sistema realiza a contabilização do IBS, CBS e IS com base na classificação fiscal configurada.

* **Exemplo de Configuração do Lançamento Padrão:** O processo envolve a definição do Lançamento Padrão.

  ![lancamento padrao.gif](https://tdn.totvs.com/download/attachments/979806887/lancamento%20padrao.gif?version=1&modificationDate=1756154548273&api=v2)
* **Exemplo de Lançamento Documento de Entrada - Contabilização:** O artigo demonstra como o lançamento do Documento de Entrada é refletido na contabilização.

  ![contabilizacao - doc de entrada.gif](https://tdn.totvs.com/download/attachments/979806887/contabilizacao%20-%20doc%20de%20entrada.gif?version=1&modificationDate=1756154545530&api=v2)

**2. Contabilização com Base na Sigla do Tributo**

Esta modalidade utiliza a sigla do tributo (IBS, CBS, IS) para identificar e realizar o lançamento contábil.

**Atenção:** Nos casos de Contabilização de Documentos de Saída com Base na Sigla do Tributo, deve-se utilizar a **tabela SD2** em vez da **tabela SD1**.

* **Exemplo de Configuração do Lançamento Padrão:** O processo envolve a definição do Lançamento Padrão.

  ![lançamentos com posicione.gif](https://tdn.totvs.com/download/attachments/979806887/lan%C3%A7amentos%20com%20posicione.gif?version=1&modificationDate=1756227919207&api=v2)
* **Exemplo de Lançamento Documento de Entrada - Contabilização:** O artigo demonstra como o lançamento do Documento de Entrada é refletido na contabilização.

  ![contabilizacao - doc de entrada posicione.gif](https://tdn.totvs.com/download/attachments/979806887/contabilizacao%20-%20doc%20de%20entrada%20posicione.gif?version=1&modificationDate=1756228521927&api=v2)

---

**Saiba Mais:**

[Contabilização com Base na Classificação do Tributo - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=977835821)  
[Contabilização com Base na Sigla do Tributo - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=977835583)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Reforma tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35707320972439-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reforma-tribut%C3%A1ria)
