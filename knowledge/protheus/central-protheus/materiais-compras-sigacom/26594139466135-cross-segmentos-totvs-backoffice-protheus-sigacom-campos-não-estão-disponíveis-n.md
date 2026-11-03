---
article_id: 26594139466135
category: Materiais - Compras (SIGACOM)
content_hash: c5ad0936201c6e6c877472376dbf9419ca502f6f22725e747143300870d47eaf
fetched_at: '2026-06-28T22:41:14.356885+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Campos não estão disponíveis
  na tabela DKD
type: support-article
updated_at: '2024-09-24T17:34:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26594139466135-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Campos-n%C3%A3o-est%C3%A3o-dispon%C3%ADveis-na-tabela-DKD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26594127790359) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Após criar campos na tabela DKD não estão disponíveis no Documento de Entrada

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Para visualizar os campos, siga os procedimentos abaixo:

* Ao criar um novo campo **(usado e real)** na tabela complementar (DKD), o mesmo já será apresentado na tela de pré - nota (MATA140)  e/ou documento de entrada (MATA103).
* Para adicionar gatilhos da SD1 para a tabela complementar (DKD), utilizar a função **A103DKDGAT**
* Ao criar gatilhos da DKD, adicionar a condição para que não gere inconsistência ao adicionar documento pela rotina (MATA910 - Notas Fiscais de Entrada)

![gifdkd.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26594127793559)

Saiba mais em :

[Exemplo de Gatilhos](https://tdn.totvs.com/pages/releaseview.action?pageId=699820173)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
