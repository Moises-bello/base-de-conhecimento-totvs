---
article_id: 360019332812
category: Originação de Grãos (OG)
content_hash: 5927f7fae66764d320208ad0cfacd3af56cf0d55934a7a3176fc2de7b9887c45
fetched_at: '2026-06-28T22:45:37.376278+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ausência de natureza nos romaneios de entrada
type: support-article
updated_at: '2025-04-09T11:52:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019332812-Agro-Linha-Protheus-AGR-Aus%C3%AAncia-de-natureza-nos-romaneios-de-entrada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20140149185431)*** Tempo aproximado para leitura: **00:00:35 min  
  
Ocorrência**Na rotina **OGA250 -****Romaneio com Pesagem** ao tentar Confirmar um romaneio do tipo **Entrada**, por meio das **Ações Relacionadas,** é exibida a mensagem: **A103NATURE - O código da natureza financeira não foi informado**. O parâmetro **MV\_2DUPNAT** está configurado com o conteúdo **SA2 > A2\_NATUREZ**.   
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Essa mensagem é exibida porque não foi informado conteúdo no campo de **Natureza do cadastro de Fornecedor.**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Acesse o **cadastro do Fornecedor** que está sendo utilizado no **Contrato**. O cadastro do fornecedor **deve ser acessado por meio do módulo de Compras;**

**2.** Abra a aba **Adm/Fin**, procure o campo **Natureza** e informe o conteúdo necessário;

**3.** Confirme essa alteração efetuada no cadastro de fornecedor e em seguida tente **Confirmar** o romaneio novamente.
