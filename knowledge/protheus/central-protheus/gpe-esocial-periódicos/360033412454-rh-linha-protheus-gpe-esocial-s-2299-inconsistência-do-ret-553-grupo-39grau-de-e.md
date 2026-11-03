---
article_id: 360033412454
category: GPE - eSocial - Periódicos
content_hash: e010852902d820fcecdb80b606145beea36a91c6f302b205597a08219e67cc6a
fetched_at: '2026-06-28T22:45:09.124892+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2299 - Inconsistência do RET - 553
  - Grupo #39;Grau de Exposição e Agentes Nocivos#39; não deve ser preenchido. Verifique
  as condições de preenchimento no leiaute'
type: support-article
updated_at: '2025-07-25T20:47:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033412454-RH-Linha-Protheus-GPE-eSocial-S-2299-Inconsist%C3%AAncia-do-RET-553-Grupo-39-Grau-de-Exposi%C3%A7%C3%A3o-e-Agentes-Nocivos-39-n%C3%A3o-deve-ser-preenchido-Verifique-as-condi%C3%A7%C3%B5es-de-preenchimento-no-leiaute
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30375695118871) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Inconsistência do RET 553 - Grupo #39;Grau de Exposição e Agentes Nocivos#39; não deve ser preenchido. Verifique as condições de preenchimento no leiaute.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**   
O Grau de Exposição (tag **grauExp**)que está sendo enviado não está de acordo com o regime de previdência (tag **tpRegPrev**) que foi informado na transmissão do S-2200.  
Conforme no leiaute a tag **grauExp** (Grau de Exposição) vinculado ao grupo de tag  **infoAgNocivo**é um registro preenchido exclusivamente em relação a remuneração de trabalhador amparado pelo RGPS - Regime Geral de Previdência Social.  
  
**Regra leiaute:**

S-2200  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043718153)  
S-2299  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042884294)  
  
**Solução**Para correção verifique no **SIGAGPE**, **TAF** e **S-2200** no site do [eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica) está definido o regime de previdência correto.  
  
Caminho Sigagpe: *atualizações > funcionários >**funcionários*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043718033)  
  
Caminho **SIGATAF**: atualizações > eventos eSocial > Trabalhador > **Cadastro Trabalhador**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042884014)  
  
**Site [eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)**  
Deve ser verificado no cadastro do trabalhador S-2200, se o regime de previdência está correto e igual ao GPE e TAF.

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
