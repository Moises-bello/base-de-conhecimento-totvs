---
article_id: 360055977674
category: Escrita Fiscal - CIAP
content_hash: 93f38d9eabf5d287435ade0cd8c11af2755e136a24b069b349d71cd071c6e0d1
fetched_at: '2026-06-28T22:39:33.717420+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Parâmetro para habilitar/desabilitar
  tratamento do pro rata die durante o cálculo mensal do CIAP'
type: support-article
updated_at: '2021-07-28T17:36:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055977674--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Par%C3%A2metro-para-habilitar-desabilitar-tratamento-do-pro-rata-die-durante-o-c%C3%A1lculo-mensal-do-CIAP
---

**Dúvida**Qual o parâmetro para Habilitar/desabilitar tratamento do pro rata die durante o cálculo mensal do CIAP?

**Ambiente**Microsiga Protheus - Livros Ficais - a partir da versão 12  
  
**Solução**

Para tratativa do pro rata die durante o cálculo mensal do CIAP se faz necessário configurar o parâmetro MV\_PRORDIE (habilita/desabilita tratamento do *pro rata die* durante o cálculo mensal do CIAP).

T = para considerar tal tratamento;  
F = para não considerar.

Importante

Esse parâmetro trabalha em conjunto com o campo Fração Mensal (FA\_FRACAOM), citado a seguir, portanto, é de extrema necessidade que esse campo também esteja criado.

O campo **Fração Mensal (FA\_FRACAOM)** armazena o fator para cálculo da Fração pro rata die

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097275053/mceclip0.png)

O campo **Fator Prop. (FA\_FATPRO)** armazena o fator proporcional do cálculo da Apropriação do CIAP.

Exemplo:

Fator cheio 0.9967

Fator Proporcional (0.9967/48) = 0.02014

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094974334/mceclip1.png)

Para os casos em que o tratamento do pro rata die durante o cálculo do CIAP deve ser efetuado em mais de uma filial, nesse contexto deve-se configurar um parâmetro para cada filial em que será considerado o tratamento de pro rata die.

Informações Adicionais:

CIAP – Crédito ICMS sobre Ativo Permanente - P12

<https://tdn.totvs.com/pages/releaseview.action?pageId=187532625>
