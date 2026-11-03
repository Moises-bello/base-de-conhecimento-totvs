---
article_id: 21509196576919
category: Evento S-2220
content_hash: 2cf31761c90fb312b5c215ccaf25fcf86203d09b4c46eac6ba83983d8b951fcb
fetched_at: '2026-06-28T22:45:25.557105+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - O que avaliar quando não for gerado o S-2220 na
  Admissão de Candidato
type: support-article
updated_at: '2024-02-21T17:18:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21509196576919-RH-Linha-Protheus-MDT-O-que-avaliar-quando-n%C3%A3o-for-gerado-o-S-2220-na-Admiss%C3%A3o-de-Candidato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21509204693655) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O que avaliar quando não for gerado o S-2220 na Admissão de Candidato?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**O evento S-2220 não irão disparar de fato, pois o candidato não tem vinculo com a empresa, contudo assim que houver uma admissão/ S-2200 com o mesmo CPF da ficha medica do candidato o sistema dispara na admissão o evento S-2220 caso não dispare siga a orientação abaixo: **1-** Deve ser aplicado o ultimo pacote de expedição continua:

[MP - MDT - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo medicina e segurança do trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773-RH-Linha-Protheus-MDT-Como-fazer-o-download-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-para-atualizar-o-modulo-medicina-e-seguran%C3%A7a-do-trabalho)

**2-** Necessário configurar os parâmetros **MV\_NG2FICH = 1**, **MV\_MDTGPE = S**

Para resolver este problema de não geração do S-2220, é possível alterar o atestado ASO na rotina MDTA200, importante ter o **S-2200** enviado ao TAF, após apagando a data de emissão, e alterando novamente preenchendo a data de emissão será gerado o evento S-2220.  
Para saber mais sobre o assunto clique [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=816900865):  
 **Saiba Mais**

[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
