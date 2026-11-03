---
article_id: 360036976793
category: ADVPL - Ponto de Entrada
content_hash: 720947580be88d7dce472c9b4203a191889345a2e8d6a54f05169de5ac4b45fe
fetched_at: '2026-06-28T22:40:12.822604+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Pontos de Entrada
  MVC FORMPRE na P12.1.17
type: support-article
updated_at: '2021-12-30T17:01:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036976793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Pontos-de-Entrada-MVC-FORMPRE-na-P12-1-17
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min****Dúvida**O Ponto de entrada FORMPRE - MVC, não permite desativar um campo em especifico?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – A partir da versão 12.1.17  
  
**Solução**A estrutura **MVC** da tela **MATA070**, não aceita a alteração do Modo de exibição dos campos no momento de execução do ponto **FORMPRE**, no caso a tratativa tem que vir direto **SX3**, ou seja, do campo **X3\_WHEN**, Este campo é lógico, então quando ele recebe Falso fica inativo a edição do campo e quando verdadeiro é possível a edição do campo.
