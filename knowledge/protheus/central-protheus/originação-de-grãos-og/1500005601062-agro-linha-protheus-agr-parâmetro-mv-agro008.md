---
article_id: 1500005601062
category: Originação de Grãos (OG)
content_hash: ef2b2795b39c78c050718fffe4b480916cd7258ec3b1e9b258f0e3661903befb
fetched_at: '2026-06-28T22:45:41.211142+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetro MV_AGRO008
type: support-article
updated_at: '2025-04-23T14:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005601062-Agro-Linha-Protheus-AGR-Par%C3%A2metro-MV-AGRO008
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20477370488215)**Tempo aproximado para leitura:**00:00:35 min**  
**Dúvida**Para que serve o parâmetro **MV\_AGRO008**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O parâmetro **MV\_AGRO008 - Modalidades pagto exp sem dados documentacionais** é do tipo caractere e serve para armazenar os códigos das modalidades de pagamento que não solicitam os dados documentais da instrução de embarque.  
  
**Importante**  
Ao informar uma modalidade de pagamento na instrução de embarque, o Sistema verifica se este código não está informado no parâmetro **MV\_AGRO008** e se estiver, bloqueia a edição dos campos da pasta **Exportação Dados Documentais**.
