---
article_id: 4412582201623
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 11cf81d0896fb6aca4061734fee71bad1aaf90ee3e2378ceefae7fb55a84a2cc
fetched_at: '2026-06-28T22:39:08.081453+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como alterar o tamanho
  dos campos referentes a código de produtos (B1_COD)?
type: support-article
updated_at: '2021-11-09T14:31:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412582201623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-alterar-o-tamanho-dos-campos-referentes-a-c%C3%B3digo-de-produtos-B1-COD
---

**Dúvida**Como alterar o tamanho do campos referente ao código do produto (B1\_COD)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para alterar o tamanho do campo referente ao código de produtos é necessário o uso do Grupo de Campos(030 - Tamanho do Produto), pois o tamanho do campo B1\_COD, que é o cadastro principal do código de produtos é replicado para diversos outros campos e tabelas.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412586309399/mceclip0.png)

**Importante**: Lembrando que o 'Grupo de Campos - 030 - Tamanho do Produto' tem o **tamanho mínimo de 15 caracteres e o máximo 30 caracteres**, conforme mostra a imagem abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412592844951/mceclip1.png)

Para realizar a alteração o usuário deve entrar no módulo Configurador: **SIGACFG > Base de Dados > Dicionário > Base de Dados**

Selecionar a **Empresa > Base de Dados > Grupo de Campos**Clicar em "Alterar", altere seu tamanho conforme necessidade. Lembrando que não pode ser menor que 15 caracteres e não pode ultrapassar 30 caracteres.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412593084567/mceclip2.png)

**Saiba mais:***[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
