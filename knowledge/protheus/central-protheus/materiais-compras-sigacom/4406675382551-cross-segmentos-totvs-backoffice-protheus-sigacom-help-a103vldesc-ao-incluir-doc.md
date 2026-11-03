---
article_id: 4406675382551
category: Materiais - Compras (SIGACOM)
content_hash: 4e387071e25bd30bb365e01bfea2fadfffed8471085bb18379e399797ff2627b
fetched_at: '2026-06-28T22:41:18.849090+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP A103VLDESC ao
  incluir Documento de Entrada MATA103
type: support-article
updated_at: '2022-05-16T22:33:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406675382551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-A103VLDESC-ao-incluir-Documento-de-Entrada-MATA103
---

**Ocorrência**

Ocorrência do HELP A103VLDESC exibido ao tentar fazer a entrada do documento de entrada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406675024791/mceclip0.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões.  
  
**Causa**É exibido quando algum item tem o valor de desconto maior ou igual ao valor total do documento. Ficando assim com o total do documento zerado.

**Solução**

Por padrão o usuário consegue apenas gerar um desconto máximo de 99,99% ficando com uma pequena sobra de valor.

Para correção desse HELP pode-se fazer a entrada do documento com CFOP de bonificação e na baixa do título aplicar o desconto financeiro.

Não há parametrização ou configuração que iniba este alerta na função do fonte quando realizado o processo da forma mencionado na causa.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
