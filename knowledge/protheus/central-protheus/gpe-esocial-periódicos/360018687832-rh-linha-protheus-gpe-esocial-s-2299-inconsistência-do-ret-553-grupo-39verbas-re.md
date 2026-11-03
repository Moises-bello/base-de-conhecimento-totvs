---
article_id: 360018687832
category: GPE - eSocial - Periódicos
content_hash: b9e47057bf42e50a0e7069791650f477e3e3712f0d674b4f0e0dfffe7b39647d
fetched_at: '2026-06-28T22:45:09.129224+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Inconsistência do RET - 553
  - Grupo #39;Verbas Rescisorias#39; nao deve ser preenchido. Verifique as condicoes
  de preenchimento no leiaute
type: support-article
updated_at: '2025-03-03T19:47:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018687832-RH-Linha-Protheus-GPE-eSocial-S-2299-Inconsist%C3%AAncia-do-RET-553-Grupo-39-Verbas-Rescisorias-39-nao-deve-ser-preenchido-Verifique-as-condicoes-de-preenchimento-no-leiaute
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30375601374231) Tempo aproximado para leitura: 00:03:00 min  
  
Ocorrência**Inconsistência do RET 553 - Grupo #39;Verbas Rescisorias#39; nao deve ser preenchido. Verifique as condicoes de preenchimento no leiaute.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**   
O erro ocorre pois está sendo enviado para o governo o evento **S-2299 (Deligamento)** com rubricas (verbas) na fase dos eventos **não periódicos**.  
Conforme regra do leiaute abaixo na fase dos eventos Não Periódicos não deve ser transmitido o S-2299 com as rubricas. Quando o parâmetro **MV\_FASESOC**está com 1, o sistema entende que a empresa está na fase dos Eventos Não Periódicos e gera o S-2299 sem as **rubricas (verbas)**, não ocorrendo o erro.  
  
**Regra do leiaute:**tag verbasResc -*N (se {mtvDeslig} = [11, 12, 13, 25, 28, 29, 30, 34] OU se {dtDeslig} for anterior ao início de obrigatoriedade dos eventos periódicos para o empregador)***Solução**1. Caso pertença ao grupo das empresas que está na fase dos eventos **não periódicos** deverá alterar o parâmetro **MV\_FASESOC** para 1.  
[MP - GPE - eSocial - Parâmetros 2ª Fase esocial (Não Periódicos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980892)  
  
2. Acessar a rescisão calculada como a opção visualizar, clicar em outras ações **Integração TAF**. Esse procedimento vai integrar novamente a rescisão que já estava calculada com o TAF.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
