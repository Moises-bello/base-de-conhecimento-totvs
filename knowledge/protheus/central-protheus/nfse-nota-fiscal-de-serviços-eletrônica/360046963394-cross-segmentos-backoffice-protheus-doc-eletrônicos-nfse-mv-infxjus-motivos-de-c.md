---
article_id: 360046963394
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a2ff551fc281f2fa8d9b9f7d833933a72971aeba2bae4b0f17740f05fc34fa58
fetched_at: '2026-06-28T22:39:57.558196+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - MV_INFXJUS
  (Motivos de Cancelamento)
type: support-article
updated_at: '2025-06-25T21:23:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046963394-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-MV-INFXJUS-Motivos-de-Cancelamento
---

**Dúvida**Qual a função do parâmetro MV\_INFXJUS?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**O parâmetro **MV\_INFXJUS**tem como objetivo informar o **Motivo de Cancelamento** **no XML** na transmissão de cancelamento de uma nota.  
  
Ao habilitar o parâmetro, no momento da transmissão do cancelamento é apresentado uma tela como essa de exemplo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069112773/mceclip1.png)  
O conteúdo informado nesse campo é gravado no campo MOTCANC na SPED051.  
  
**Atenção**  
A justificativa digitada manualmente é algo exigido **por algumas prefeituras apenas**, onde é necessário informar algo específico, por isso a disponibilização do parâmetro.  
Para as demais, essa informação dentro da tag é levada em branco ou alguma padrão exigida pela prefeitura, não sendo necessário a utilização do parâmetro. **Configuração do parâmetro:****Nome da Var**: MV\_INFXJUS  
**Tipo**: 1 - Caracter  
**Conteúdo**: S (N ou "vazio" para desabilitar a tela)  
**Descrição**: "Habilita a tela para selecionar o código de cancelamento da NFS-e em determinados municípios."

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069113733/mceclip2.png)  
  
Obs.: A rotina FISA022 deverá estar atualizada para contemplar essa configuração.**[- Clique aqui para baixar o pacote de atualização.](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)Mais detalhes:  
- <https://tdn.totvs.com/pages/releaseview.action?pageId=501481434>
