---
article_id: 36290703148311
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: b7ca48286687b675215533643d6f4c8d3648045487b8ae6916d4f178bed6cc84
fetched_at: '2026-06-28T22:39:55.187179+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Rejeição
  432 (UF do Destinatário não aceita ISENTO com Inscrição Estadual)
type: support-article
updated_at: '2025-11-12T19:40:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36290703148311-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Rejei%C3%A7%C3%A3o-432-UF-do-Destinat%C3%A1rio-n%C3%A3o-aceita-ISENTO-com-Inscri%C3%A7%C3%A3o-Estadual
---

**Ocorrência**  
Ao realizar a transmissão de uma NFCOM ocorre a rejeição: **432 - UF do Destinatário não aceita ISENTO com Inscrição Estadual.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Essa rejeição ocorre pois a **Sefaz não permite** que seja gerada a tag <IE> do destinatário com **o literal 'ISENTO'** quando a UF do mesmo for: **AM, BA, CE, GO, MG, MS, MT, PE, RN, SE ou SP.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36290710836759)  
  
Fonte: <https://dfe-portal.svrs.rs.gov.br/Nfcom/ConsultaRegrasValidacao>   
  
Portanto, para correção **precisará ser configurado no Cadastro do Cliente** da seguinte maneira:  
  
- **A1\_INSCR** = EM BRANCO / SEM CONTEÚDO  
- **A1\_CONTRIB** = 2  
  
Dessa forma o XML será gerado com a tag indIEDest=9 (Não Contribuinte, que pode ou não possuir Inscrição Estadual no Cadastro de Contribuintes do ICMS) e sem gerar a tag IE para o destinatário.
