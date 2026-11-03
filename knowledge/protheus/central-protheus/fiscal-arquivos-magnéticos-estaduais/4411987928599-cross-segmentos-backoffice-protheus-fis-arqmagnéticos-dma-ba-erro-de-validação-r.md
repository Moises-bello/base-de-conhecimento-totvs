---
article_id: 4411987928599
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 7dd2df624b8b6a204a4560bcbc90f5306d248aceb5dea0a56aa2f64dbf148bc0
fetched_at: '2026-06-28T22:42:10.833660+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DMA - BA - Erro
  de validação - Registro Tipo 01 - Município inválido
type: support-article
updated_at: '2022-08-17T19:39:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411987928599-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DMA-BA-Erro-de-valida%C3%A7%C3%A3o-Registro-Tipo-01-Munic%C3%ADpio-inv%C3%A1lido
---

**Dúvida**

 DMA - BA - Erro de validação - Registro Tipo 01 - Município inválido.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Livros Fiscais - Todas as versões  
  
**Solução**

De acordo com o layout da DMA 2012 o campo código do município no Registro Tipo 01 ( Identificação da empresa do DMA) deve ser informado o código conforme tabela de municípios do Estado da Bahia.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411986482071/mceclip0.png)

Para ser escriturado o código corresponde a tabela de municípios do Estado da Bahia, é necessário informar na wizard dos parâmetro da DMA na rotina Instruções Normativas(MATA950) o parâmetro **Código de Mun. Contribuinte**informando o **código 29 referente a UF Bahia e o respectivo Código da tabela de municípios do Estado da Bahia.**

No exemplo abaixo foi informado o código de Salvador

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411986547223/mceclip1.png)

**Observação:**

O layout DMA fica disponível na pasta DOC no diretório instalado o validador.

**Informações complementares:**

DMA – Declaração e Apuração Mensal do ICMS - BA

[https://tdn.totvs.com/pages/viewpage.action?pageId=634645198#DMA%E2%80%93Declara%C3%A7%C3%A3oeApura%C3%A7%C3%A3oMensaldoICMS-BA-01.VIS%C3%83OGERALhttps://tdn.totvs.com/pages/viewpage.action?pageId=634645198#DMA%E2%80%93Declara%C3%A7%C3%A3oeApura%C3%A7%C3%A3oMensaldoICMS-BA-ProcedimentoparaGera%C3%A7%C3%A3o](https://tdn.totvs.com/pages/viewpage.action?pageId=634645198#DMA%E2%80%93Declara%C3%A7%C3%A3oeApura%C3%A7%C3%A3oMensaldoICMS-BA-ProcedimentoparaGera%C3%A7%C3%A3o)

Tabela Municípios do Estado da Bahia

<https://www.sefaz.ba.gov.br/contribuinte/informacoes/codigo_municipios.htm>
