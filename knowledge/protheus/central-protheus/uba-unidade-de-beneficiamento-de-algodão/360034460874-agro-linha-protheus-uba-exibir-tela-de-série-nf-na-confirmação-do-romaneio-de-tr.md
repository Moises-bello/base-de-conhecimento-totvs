---
article_id: 360034460874
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 1a939985182cce17cfc6ffcccffb27990b92d7f1675444328f9ad4907dd6ec90
fetched_at: '2026-06-28T22:45:35.603068+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Exibir tela de série NF na confirmação do romaneio
  de transferência
type: support-article
updated_at: '2025-06-18T20:02:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034460874-Agro-Linha-Protheus-UBA-Exibir-tela-de-s%C3%A9rie-NF-na-confirma%C3%A7%C3%A3o-do-romaneio-de-transfer%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21893688609943)**Tempo aproximado para leitura: **00:00:40 min**  
 **Dúvida**Como faço para que seja exibida a tela referente à série da **Nota Fiscal** ao confirmar um romaneio de transferência na rotina **AGRA500 - Romaneio Unificado**?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - A partir da versão 12.1.17  
  
**Solução**Para que a tela corresponde à série da **Nota Fiscal** seja exibida ao confirmar um romaneio de transferência é necessário acessar o parâmetro **MV\_AGRORI - Utiliza Módulo de Originação**e inserir **.F.** em seu conteúdo.É necessário também acessar o parâmetro **MV\_OGASERS - Define a série padrão a ser utilizada na geração dos documentos de saída** deixando-o sem conteúdo.
