---
article_id: 37723088236567
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: e5179af96e915d40e4f1f3c2ffe9226f38d8368381553e998da82628fcf848c9
fetched_at: '2026-06-28T22:39:51.064767+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro da Regra de Base de Cálculo no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-16T19:21:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37723088236567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-da-Regra-de-Base-de-C%C3%A1lculo-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37723118741527) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro da Regra de Base de Cálculo no Configurador de Tributos (FISA170)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.  
  
**Solução**  
A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração das Regras de Base de Cálculo.

**REGRAS DE BASE DE CÁLCULO**

**Acesse:** Regras de Cálculo Documento Fiscal → Regra de Base de Cálculo

Criar uma regra para base de Cálculo de Importação conforme exemplo abaixo:

| **Campo** | **Descrição** | Valor Origem |
| --- | --- | --- |
| EICICAL | Base de Cálculo Importação - SIGAEIC | 11 - Fórmula Manual |

**Aba Detalhamento da Fórmula de Cálculo:**

1. Clique em **Editar Fórmula**
2. **Tipo da Regra**: `01 - Valores de Origem`.
3. **Consulta de Regra:** `O:BASE_INTEGRACAO`
4. Clique em **Adicionar**
5. Clique em **Validar Fórmula**

![200c9f36-0d46-41b0-b52d-633ef947ab86.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37723118742551)

**Vídeo** ***How to***

|  |
| --- |
|  |

**Saiba mais:**  
[Configurador de Tributos (CFGTRIB) na Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)  
[Guia Prático - Configurador de Tributos na Importação - SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)

**Vídeos:**  
[How To TRADE COMÉRCIO EXTERIOR - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=766411901)
