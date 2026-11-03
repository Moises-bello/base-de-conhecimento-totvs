---
article_id: 360022043091
category: Materiais - Compras (SIGACOM)
content_hash: 50437e75d65b9748c102272880bcf4e00edef2e6b1186cac6ef3f06255ee71e9
fetched_at: '2026-06-28T22:41:07.600720+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como deixar o campo
  Natureza (CNATUREZA) na aba Duplicatas obrigatório ao inserir uma Nota Fiscal de
  Entrada?
type: support-article
updated_at: '2024-12-11T18:09:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022043091-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-deixar-o-campo-Natureza-CNATUREZA-na-aba-Duplicatas-obrigat%C3%B3rio-ao-inserir-uma-Nota-Fiscal-de-Entrada
---

**Dúvida**Como deixar o campo **Natureza** (CNATUREZA) na aba **Duplicatas** obrigatório ao inserir uma Nota Fiscal de Entrada?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
  
**Solução**

O controle é realizado pelo parâmetro **MV\_NFENAT**, que define se o preenchimento da natureza é obrigatório durante a inclusão de um documento de entrada.

Para alterar o parâmetro, siga o procedimento abaixo:

1. Acesse o Configurador através do caminho: SIGACFG -> Base de Dados -> Dicionário -> Base de Dados -> Parâmetro.
2. Digite o parâmetro **MV\_NFENAT**.
3. Altere o conteúdo do parâmetro para "T"

![cNaturez.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28452925309847)

***Saiba Mais :***

[MP - SIGACOM - Pontos de Entrada - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000169747-MP-SIGACOM-Pontos-de-Entrada-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
