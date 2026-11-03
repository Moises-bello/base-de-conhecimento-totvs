---
article_id: 34497900282903
category: Financeiro - Aplicação / Emprestimos
content_hash: 5f522827971116d71f07fa42dfc997e2307d0dc532984a366c1c493a02f0b126
fetched_at: '2026-06-28T22:37:59.322012+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA716 - Valor Campo
  Natureza Inválido
type: support-article
updated_at: '2025-08-28T12:07:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34497900282903-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Valor-Campo-Natureza-Inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34497898070935) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Na rotina **FINA716 - Aplicação e Empréstimo**, ao realizar um resgate de uma aplicação, ocorre a mensagem: **"Valor Campo Natureza Inválido".**  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA716 - A partir da release 12.1.2310  
  
**Causa**  
Ao realizar o resgate de uma aplicação, o sistema valida a natureza definida no parâmetro ****MV\_NATRAPL****. Caso este parâmetro esteja vazio, será exibida a seguinte mensagem de aviso:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34497900268439)  
  
**Solução**  
Preencher a natureza financeira correta via configurador **(SIGACFG)** no parâmetro **MV\_NATRAPL.**

**Saiba mais**  
[Aplicações - FINA716](https://tdn.totvs.com.br/pages/viewpage.action?pageId=684987286)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - Parâmetros de naturezas de Aplicações e Empréstimos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19945319268759-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Parametros-de-naturezas-de-Aplica%C3%A7%C3%B5es-e-Emprestimos)
