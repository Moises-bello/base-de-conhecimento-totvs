---
article_id: 13635453599127
category: Materiais - Compras (SIGACOM)
content_hash: cbc7950bc440ee298fc406aec86b0a06ab314fbaf829de09b89173f9a4e8491c
fetched_at: '2026-06-28T22:41:16.060921+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como são preenchidos
  os campos de Prazo na rotina de Liberação de Documentos(MATA094)?
type: support-article
updated_at: '2023-04-06T12:24:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13635453599127-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-s%C3%A3o-preenchidos-os-campos-de-Prazo-na-rotina-de-Libera%C3%A7%C3%A3o-de-Documentos-MATA094
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais informações são utilizadas para preencher as informações de prazo dentro da aprovação de documentos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - A partir da versão 11.80  
  
**Solução**Os campos são preenchidos quando utilizado controle de alçada por entidade contábil e item (SC e IP). Abaixo segue maiores detalhes referente ao preenchimento:  
   
**CR\_PRAZO:**Para solicitação de compra é preenchido com a database do sistema + prazo informado no campo DHK\_PRAZO. Para o pedido com o campo DHK\_PRAZOP.  
   
**CR\_AVISO:**Para solicitação de compra é preenchido com a data calculada para o prazo subtraído o aviso informado no campo DHK\_AVISO. Para pedido utiliza o mesmo cálculo porém como referência o campo DHK\_AVISOP.  
   
Obs: Para preenchimento dos campos é necessário a utilização de tipos de compra. Quando não utilizado, a rotina considera 99 dias para ambos.

**Saiba mais:**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o Controle de Alçadas Padrão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006822671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-Controle-de-Al%C3%A7adas-Padr%C3%A3o-?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Controle de Alçadas no Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9058852149399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Trilha-de-Videos-Controle-de-Al%C3%A7adas-no-Compras?source=search)
