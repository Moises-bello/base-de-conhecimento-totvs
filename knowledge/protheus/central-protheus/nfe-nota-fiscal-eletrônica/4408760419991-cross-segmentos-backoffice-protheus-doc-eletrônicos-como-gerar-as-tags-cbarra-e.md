---
article_id: 4408760419991
category: NFe - Nota Fiscal Eletrônica
content_hash: e7490ee77828f0f9fc8a24cc79b31e2ab5cdfa9b1a135865aa3c7b67630573ee
fetched_at: '2026-06-28T22:40:06.695704+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar as TAGS
  cBarra e cBarraTrib
type: support-article
updated_at: '2025-06-26T14:36:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408760419991-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-TAGS-cBarra-e-cBarraTrib
---

**Dúvida**Como gerar as TAGS cBarra e cBarraTrib ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em incluir **MV\_CAMPBAR**

O parâmetro deverá ser do tipo *string* (1- Caractere) para que sejam adicionados **dois campos customizados** da tabela **SB1.**Os campos deverão ser separados por pipe  "|".

**Exemplo:**  MV\_CAMPBAR  = B1\_BARRA|B1\_BARTRIB

![](https://tdn.totvs.com/download/attachments/649997342/image2021-11-16_10-51-52.png?version=1&modificationDate=1637070713130&api=v2&effects=drop-shadow)

**DEMAIS INFORMAÇÕES**

*Criação* de **Parâmetros manual**no arquivo **SX6 – Parâmetros .**

| **Nome da Variável** | MV\_CAMPBAR |
| --- | --- |
| **Tipo** | CARACTERE |
| --- | --- |
| **Descrição** | Informa campo na tabela SB1 que contem os campos para pegar  as informação para preenher a tag(cBarra) e a tag (cBarraTrib) |
| **Valor Padrão** |  |

**Criação do campo de Manual na Tabela SB1 -conforme exemplo abaixo: B1\_BARRA e B1\_BARTRIB**

**Observação:** poderá ser criado com outros nomes ou aproveitar campos existentes na SB1 caso se enquadre nos requisitos dos campos cBarra e cBarraTrib.

|  |  |
| --- | --- |
| **Campo** | B1\_BARRA |
| **Tipo** | Caractere |
| **Tamanho** | 30 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | B1\_BARRA |
| **Descrição** | Código de barras diferente do padrão GTIN |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Preencher com o Código de Barras próprio ou de terceiros que seja diferente do padrão GTIN |

|  |  |
| --- | --- |
| **Campo** | B1\_BARTRIB |
| **Tipo** | Caractere |
| **Tamanho** | 30 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | B1\_BARTRIB |
| **Descrição** | Código de Barras da unidade tributável que seja diferente do padrão GTIN |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Preencher com o Código de Barras próprio ou de terceiros, que seja diferente do padrão GTIN, correspondente àquele da menor unidade comercializável identificado por Código de Barras |
