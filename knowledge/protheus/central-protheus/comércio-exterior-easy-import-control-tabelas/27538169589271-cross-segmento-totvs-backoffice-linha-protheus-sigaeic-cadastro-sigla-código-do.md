---
article_id: 27538169589271
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 03440b50c90cca6c7488c47c83a30f58a1ff45c4e5834e8c9e6c1e5010e6c194
fetched_at: '2026-06-28T22:39:47.830530+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Cadastro Sigla
  Código do País na tabela Cadastro de Países (SYA)
type: support-article
updated_at: '2024-11-22T19:35:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27538169589271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Cadastro-Sigla-C%C3%B3digo-do-Pa%C3%ADs-na-tabela-Cadastro-de-Pa%C3%ADses-SYA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27538142315415)Tempo aproximado para leitura**:00:02:00 min** **Dúvida**Como realizar o cadastro da Sigla Código do Pais no campo Cod Port Uni "**YA\_PAISDUE"** na tabela Cadastro de Países (**SYA**)?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27538142317719)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – A partir da versão 12.2210.  
  
**Solução** O cadastro de países **(SYA)**, através da rotina Atualizações\Tabelas\Países **(EICA100)**, são de carga padrão da tabela de países do Siscomex, onde o campo Sigla**"YA\_SIGLA"** vem preenchido com asterisco (\*)

O código do país Cod Port Uni **(YA\_PAISDUE)** deve ser preenchido conforme a **ISO-3166** e será  carregado automaticamente na grid Relação de Países de Origem e Fabricantes da aba Relação de Produtos x Origens/Fabricantes. O **ISO 3166** é um conjunto de três normas geográficas para codificar nomes de países e dependências e das suas principais subdivisões administrativas.

**Observação:** O cadastro e as alterações de campos são de responsabilidade dos clientes.

**Saiba mais:** [Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Cadastro Sigla Paises tabela SYA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040591674-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Cadastro-Sigla-Paises-tabela-SYA)
