---
article_id: 40769115461143
category: Financeiro - Baixas a Receber
content_hash: 74be53a90397ad4026677f86d09794c3b63c3d34c51fa08c292c9e9ab2d0b156
fetched_at: '2026-06-28T22:37:43.750916+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA040 - Quando são preenchidos
  os campos E1_PORCJUR e E1_VALJUR
type: support-article
updated_at: '2026-05-27T18:47:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40769115461143-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FINA040-Quando-s%C3%A3o-preenchidos-os-campos-E1-PORCJUR-e-E1-VALJUR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40769129851415) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Quando ocorre o preenchimento dos campos E1\_PORCJUR e E1\_VALJUR referentes aos juros de um título?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
O comportamento de preenchimento dos campos E1\_PORCJUR e E1\_VALJUR varia de acordo com a origem de geração do título:

* **Títulos gerados pelo Faturamento:** O preenchimento é realizado de forma automática, baseando-se nos parâmetros de juros e multa configurados previamente no sistema.
* **Títulos incluídos via módulo Financeiro:** Por padrão, estes campos não são preenchidos no momento da inclusão do registro. Os valores de juros são calculados e gerados automaticamente pelo sistema somente no momento da baixa do título, de acordo com as parametrizações ativas.

Caso um título tenha sido incluído manualmente pelo módulo Financeiro e apresente os campos E1\_PORCJUR ou E1\_VALJUR preenchidos antes do processo de baixa, significa que a informação foi adicionada de forma manual pelo usuário durante a digitação do registro.

**Saiba Mais**

Para consultar a documentação sobre a configuração das taxas e regras de cálculo, acesse: [Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como calcular multa e juros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14635481028759-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-calcular-multa-e-juros)
