---
article_id: 26594137781911
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: 6a7345332005ba3beabe20dc6cd05a4b685317ba794e64d2f78cec1f424ab3f2
fetched_at: '2026-06-28T22:39:45.363069+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Problema: Valor
  Atribuído difere do tamanho do campo (Descrição), no catálogo de produtos.'
type: support-article
updated_at: '2025-01-24T13:02:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26594137781911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Problema-Valor-Atribu%C3%ADdo-difere-do-tamanho-do-campo-Descri%C3%A7%C3%A3o-no-cat%C3%A1logo-de-produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26594092597271) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Apresentado mensagem: **Help: Descrição - Problema: Valor Atribuído difere do tamanho do campo (Descrição)**, no catálogo de produtos![](https://centraldeatendimento.totvs.com/hc/article_attachments/26594137744919)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – *Easy Import Control* – A partir da versão 12.2210.  
  
**Solução**

A mensagem é apresentada por conta dos campos **EKA\_DESC\_I** e **EK9\_DESC\_I**, estarem com tamanhos diferentes. Para não ocorrer o incidente, deve ser feito o ajuste do tamanho dos campos **EKA\_DESC\_I** e **EK9\_DESC\_I** no **SIGACFG** 'Configurador', estes precisam ter o mesmo tamanho.

1. Acessar Configurador - SIGACFG - Base de Dados - Dicionário - Base de Dados.
2. Posicionar nas tabelas **EKA** e **EK9**, pesquisar os campos **EKA\_DESC\_I** e **EK9\_DESC\_I**, fazer a comparação e igualar o tamanho dos campos.

![0cbcc5cf-2261-4e5f-932a-2f5fe76121cd.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26594137748503)
