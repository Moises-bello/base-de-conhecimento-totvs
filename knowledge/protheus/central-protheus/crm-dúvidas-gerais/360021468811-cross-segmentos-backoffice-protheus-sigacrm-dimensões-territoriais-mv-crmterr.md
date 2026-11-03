---
article_id: 360021468811
category: CRM - Dúvidas Gerais
content_hash: b079a1687c2a79e43d94cd89a098f4bc45579ddd2af5b21a48294bc4342d0289
fetched_at: '2026-06-28T22:40:27.677730+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Dimensões Territoriais MV_CRMTERR
type: support-article
updated_at: '2024-09-25T20:09:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021468811-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Dimens%C3%B5es-Territoriais-MV-CRMTERR
---

**Dúvida**

Qual o funcionamento da rotina de Dimensões Territorias no módulo SIGACRM?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12

**Solução**

Utilizamos esta funcionalidade na gestão de vendas a divisão territorial, utilizada para atribuir responsáveis, geralmente Canais de Vendas, por determinada parte de um território.

Estes canais tem prioridade e algumas vezes, exclusividade na comercialização dentro de seu território.

O que não os exime do cumprimento de metas e atingimento de outros indicadores conforme definidos pela Matriz.

Os limites de cada território são definidos por meio de uma combinação de valores de dimensões.

**Exemplo de dimensões na divisão territorial:**

• Localização Geográfica (País, Estado, CEP);  
• Segmento ( Agroindústria, Manufatura, Varejo, Serviços, etc.);  
• Porte (Pequeno, Médio, Grande);  
• Setor (Privado, Público);  
• Faturamento;  
• Produto;  
No planejamento da divisão territorial é que são definidas as dimensões e a configuração deve acompanhar a estratégia comercial da empresa e a possibilidade é a de utilizar uma ou mais dimensões.

Configure o parâmetro MV\_CRMTERR com .T. (True/Verdadeiro) para habilitar a opção **Avaliação de Território.**

Para saber mais a respeito da funcionalidade, acesse: [CRM0040 - Dimensões Territoriais](https://tdn.totvs.com/pages/releaseview.action?pageId=447096021)

**Observação**:

O parâmetro **MV\_CRMTERR** é validado nos cadastros:

* Suspects (TMKA341)
* Prospects (TMKA260)
* Clientes (CRMA980/MATA030)
