---
article_id: 1500005071101
category: eSocial - Tabelas/Não Periódicos
content_hash: f6da8d1e6f7af72d9f83a6b26ded93e52b00217fd3fb9cb96aafe33c8c90a440
fetched_at: '2026-06-28T22:47:10.588782+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RM - eSocial - Erro 553 no envio do S-2200: Grupo Trabalho Temporário não
  deve ser preenchido'
type: support-article
updated_at: '2022-02-24T00:57:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005071101-RM-eSocial-Erro-553-no-envio-do-S-2200-Grupo-Trabalho-Tempor%C3%A1rio-n%C3%A3o-deve-ser-preenchido
---

**Ocorrência**Ao transmitir o XML do S-2200 de um funcionário cujo registro no RM possui os campos de **Trabalho Temporário** preenchido é apresentado a inconsistência **Código da Ocorrência: 553: Grupo #39;Trabalho Temporário#39; não deve ser preenchido**.  
**Ambiente**RM - eSocial - A partir do patch 12.1.29  
  
**Causa**De acordo com o Layout eSocial, informações sobre trabalhadores temporários só devem ser preenchidos quando a Categoria do eSocial for igual a **106 - Trabalhador Temporário - contrato nos termos da Lei 6.019/74**.

![esocial.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007064861/esocial.PNG)

**Solução**Primeiramente, é necessário validar se no cadastro do funcionário o **Código da Categoria eSocial** está preenchido corretamente. Lembrando que categorias diferentes de **106 - Trabalhador Temporário****não devem** possuir registros de **Trabalho Temporário** preenchidos.  
  
Caso o a categoria do funcionário seja **106 - Trabalhador Temporário**, e o erro ainda sim está sendo apresentado, valide se o XML está sendo gerado com as tags abaixo:

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006879462/2.png)

**Saiba mais**  
Para mais informações, acesse:  
      • [Portal eSocial](https://www.gov.br/esocial/pt-br)
