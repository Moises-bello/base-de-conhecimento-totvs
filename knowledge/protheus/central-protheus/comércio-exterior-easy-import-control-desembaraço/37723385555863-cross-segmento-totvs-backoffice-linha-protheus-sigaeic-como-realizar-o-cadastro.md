---
article_id: 37723385555863
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 19781b0d85429b822ff69c5e3e8b8b5cc85bd43fb2c581574146433b4a59517d
fetched_at: '2026-06-28T22:39:51.058597+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro da Regra de Alíquota no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-16T19:24:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37723385555863-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-da-Regra-de-Al%C3%ADquota-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37723385537559) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro da Regra de Alíquota no Configurador de Tributos (FISA170)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.  
  
**Solução**  
A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração das  Regras de Base de Alíquota.

**REGRAS DE BASE DE ALÍQUOTA**

**Acesse:** Regras de Cálculo Documento Fiscal → Regra de Alíquota

Criar uma regra para alíquota de Importação conforme exemplo abaixo:

| **Campo** | **Descrição** | Valor Origem |
| --- | --- | --- |
| EICICALI | Alíquota Importação SIGAEIC | 06 - Fórmula Manual |

**Aba Detalhamento da Fórmula de Cálculo:**

1. Clique em **Editar Fórmula**
2. **Tipo da Regra:** 01 - Valores de Origem
3. **Consulta de Regra:** `O:ALIQUOTA_INTEGRACAO`
4. Clique em **Adicionar**
5. Clique em **Validar Fórmula**

![40c4512a-2371-44dc-9bf6-c2749005308c.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37723399128471)

**Vídeo** ***How to***

|  |
| --- |
|  |

**Saiba mais:**  
[Configurador de Tributos (CFGTRIB) na Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)  
[Guia Prático - Configurador de Tributos na Importação - SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)

**Vídeos:**  
[How To TRADE COMÉRCIO EXTERIOR - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=766411901)
