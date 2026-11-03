---
article_id: 360018981691
category: Materiais - Compras (SIGACOM)
content_hash: cf81f5520b4c5d552d7938df193383683c9b38e590a0018889a3d0e5ec33a900
fetched_at: '2026-06-28T22:41:10.158482+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Permitir a Classificação
  de um Documento de Entrada pendente de Aprovação ( Bloqueado ) - MV_RESTCLA
type: support-article
updated_at: '2022-05-13T11:45:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018981691-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Permitir-a-Classifica%C3%A7%C3%A3o-de-um-Documento-de-Entrada-pendente-de-Aprova%C3%A7%C3%A3o-Bloqueado-MV-RESTCLA
---

**Dúvida**

Permitir a Classificação de um Documento de Entrada pendente de Aprovação ( Bloqueado ) - MV\_RESTCLA

**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**

Documento de Entrada está Classificado, mas também consta pendente para aprovação na rotina Liberação de Documento.

Para que a classificação da Nota não seja permitida enquanto existir bloqueio por tolerância é necessário revisar configuração do parâmetro MV\_RESTCLA (Restringe a classificação de um documento bloqueado).

A configuração do parâmetro MV\_RESTCLA=2, permite a classificação da NF bloqueada por  
tolerância de recebimento não realiza nenhuma interação na tabela SCR.  
A configuração com o parâmetro MV\_RESTCLA=1 bloqueando os  
documentos, a liberação deve ser efetuada através da rotina de Liberação - MATA094.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
