---
article_id: 360025032173
category: Gestão de Transportes (TMS)
content_hash: ccb4b9cf85e5c2c013f420ae7e0529058209dabfc7525cebe5ea05e2bcae49e8
fetched_at: '2026-06-28T22:45:29.226441+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Geração CT-e com mais de uma NF
type: support-article
updated_at: '2024-10-23T18:10:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025032173-Log%C3%ADstica-Linha-Protheus-TMS-Gera%C3%A7%C3%A3o-CT-e-com-mais-de-uma-NF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27280283606935)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Quais parametrizações para gerar **CT-e - Conhecimento de Transporte Eletrônico**  com mais de uma **NF - Nota Fiscal**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução  
1.** Em **Gestão de Transportes - SIGATMS**, acesse **Atualizações/Comercial/Perfil de Cliente - TMSA480** e verificar se o cliente devedor possui **Perfil de Cliente** cadastrado. Caso encontre o cadastro, verificar se os campos **DUO\_AGRNFC - A****grupa Nfc =  1 - Sim**e **DUO\_NFCTR - Nfs por CTRC = 9999.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043728713)**

**2.** Caso o Sistema não encontre o cadastro de **Perfil de Cliente,** ele irá buscar esta regra no **Contrato de cliente.** Em **Gestão de Transportes - SIGATMS**, acesse **Atualizações/Comercial/Contrato de Cliente - TECA250** e ajuste oscampos **AAM\_AGRNFC - Agrupa Nfc = 1 - Sim** e**AAM\_NFCTR - Nfs por CTRC = 9999.** Se não encontrar contrato de cliente para cliente devedor, **será considerado o contrato de cliente Genérico**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043728793)
