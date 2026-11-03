---
article_id: 35814995731607
category: Materiais - Compras (SIGACOM)
content_hash: 628ce20a7cf50e86b4e1a386f14f1e7f3b5ea4cc689b5da4902dd5e3d28b0465
fetched_at: '2026-06-28T22:41:21.807654+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - FWNOWIDTH - Tamanho
  campo Email ao editar cotação no NFC
type: support-article
updated_at: '2025-10-22T19:28:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35814995731607-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-FWNOWIDTH-Tamanho-campo-Email-ao-editar-cota%C3%A7%C3%A3o-no-NFC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35814995714967) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
No Novo Fluxo de Compras, ao tentar editar uma cotação para incluir um novo participante, é apresentado erro relacionado ao campo de e-mail.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35814990377495)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310

**Causa**  
Esse incidente costuma ocorrer, quando os campos A2\_EMAIL e C8\_FORMAIL estão com tamanhos diferentes. O que gera inconsistência de dados do campo na edição da cotação ao tentar incluir um novo participante.

**Solução**  
Para solucionar essa ocorrência, é necessário que ambos os campos A2\_EMAIL e C8\_FORMAIL tenham o mesmo tamanho. Sendo assim, por favor, realize os seguintes passos:

1. Verifique o tamanho do campo A2\_EMAIL.
2. Confirme se o tamanho do campo C8\_FORMAIL é o mesmo que o do campo A2\_EMAIL.
3. Se houver diferença, ajuste o tamanho de um dos campos para que ambos fiquem iguais.

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
