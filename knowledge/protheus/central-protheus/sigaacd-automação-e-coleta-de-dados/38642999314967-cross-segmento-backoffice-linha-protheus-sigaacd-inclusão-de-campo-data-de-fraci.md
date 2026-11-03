---
article_id: 38642999314967
category: SIGAACD - Automação e Coleta de Dados
content_hash: 9b313a4476048b8e92f8dbdd04b04484ee8aeb7b59dcf8d7e1c2cbd9424a36c4
fetched_at: '2026-06-28T22:39:12.756268+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Inclusão de campo
  Data de Fracionamento na rotina ACDI011
type: support-article
updated_at: '2026-02-25T19:47:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38642999314967-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Inclus%C3%A3o-de-campo-Data-de-Fracionamento-na-rotina-ACDI011
---

O artigo explica que a rotina Wizard de Etiqueta (ACDI011) do TOTVS Protheus não possui um campo padrão para "Data de Fracionamento", mas permite a inclusão dessa informação por meio de customização utilizando o ponto de entrada ACDI11PA.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38642999308567) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
É possível  incluir uma campo **Data de Fracionamento** na rotina Wizard de Etiqueta(ACDI011)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
A rotina ACDI011 permite a emissão de etiquetas de produtos fracionados, mas não há menção a um campo padrão que grave a data de fracionamento. Para incluir essa informação na etiqueta, é possível utilizar pontos de entrada para customização.

A rotina ACDI011 possui o ponto de entrada [ACDI11PA](https://tdn.totvs.com/pages/releaseview.action?pageId=871526719), que permite manipular as opções de origem das informações na tela de impressão de etiquetas.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
