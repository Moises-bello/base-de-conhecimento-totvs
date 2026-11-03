---
article_id: 28732811663639
category: Financeiro - Cadastros
content_hash: 4cc4bd05fe2c5bca3cada3b5cb96ba47adbd85124b2a665ee8daa4aa86769e36
fetched_at: '2026-06-28T22:37:53.124699+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA010 - Como criar
  o código de uma Natureza financeira?
type: support-article
updated_at: '2026-03-25T20:15:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28732811663639-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA010-Como-criar-o-c%C3%B3digo-de-uma-Natureza-financeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28732811655191) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
No relatório de Contas a Pagar por Natureza (FINR150), o código da Natureza cadastrado não confere com o código impresso, como criar corretamente o código da Natureza financeira?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**

A falta de definição de **máscara** ou formato de código de **Natureza** financeira é o que gera divergência entre a impressão e o cadastro de **Natureza**. Essa definição é feita com a a utilização do parâmetro**MV\_MASCNAT** **que contempla a quantidade de níveis e de caracteres e que definem o formato do código, ou seja, a cada nível é possível classificar a origem e o destino de cada movimentação financeira.**

**Exemplos:**

1. Se o conteúdo do parâmetro for **242**, o código será tratado em três níveis:

* 1º nível com dois dígitos: identifica a despesa do departamento.
* 2º nível com quatro dígitos: identifica o departamento.
* 3º nível com dois dígitos: identifica o centro de custo.

**99.9999.99**

2. Se o conteúdo do parâmetro for **19**, como no exemplo a seguir:

**2..1.13.004**

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28732811656343)**](https://centraldeatendimento.totvs.com/hc/article_attachments/28732811656343)

Entendo o resultado:[![](https://centraldeatendimento.totvs.com/hc/article_attachments/28732804322327)](https://centraldeatendimento.totvs.com/hc/article_attachments/28732804322327)

Podemos observar que a máscara foi composta por apenas dois niveis, primeiro nível com **2 .**e o segundo nível com **.1.13.004** considerando os pontos,  como resultado a máscara será:  **2..1.13.004**.

**Saiba mais:**

[O que é Natureza financeira](Cross%20Segmentos%20-%20Backoffice%20Linha%20Protheus%20-%20SIGAFIN%20-%20FINA010%20-%20O%20que%20%C3%A9%20natureza%20financeira)

[Cadastro de Natureza - FINA010](https://tdn.totvs.com/display/public/PROT/Naturezas+-+FINA010+-+Financeiro+-+P12)
