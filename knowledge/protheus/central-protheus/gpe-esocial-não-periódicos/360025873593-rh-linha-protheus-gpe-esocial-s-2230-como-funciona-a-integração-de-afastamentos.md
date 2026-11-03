---
article_id: 360025873593
category: GPE - eSocial - Não Periódicos
content_hash: bf99d4eecbd7d5260fdb7cc186837097b2397e6927be423ff27f4fa31985d3bc
fetched_at: '2026-06-28T22:45:05.696289+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2230 - Como funciona a integração de
  afastamentos sequenciais
type: support-article
updated_at: '2026-06-16T13:33:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025873593-RH-Linha-Protheus-GPE-eSocial-S-2230-Como-funciona-a-integra%C3%A7%C3%A3o-de-afastamentos-sequenciais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30375528886167) Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**S-2230 - Como funciona a integração de afastamentos sequenciais?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**As sequencias de afastamentos são informadas no lançamento de ausências do GPE preenchendo a informação de **Nr. Sequência**, porém essas informações serão integradas com o TAF conforme exemplos previstos no leiaute do eSocial.  
Cada tipo de afastamento tem uma regra para integração, por exemplo, afastamento temporário ocasionado por acidente de qualquer natureza ou doença não relacionada ao trabalho, será enviando com duração a partir de 3 (três) dias, vide [MOS - Manual de Orientações do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica).  
  
Seguindo o exemplo acima, um empregado tem os seguintes afastamentos, motivados por uma mesma doença relacionada ao trabalho:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040874833)  
  
No momento em que foram cadastrados os afastamentos de sequência 001, 002 e 003 as informações foram gravadas no GPE, mas nenhum evento S-2230 foi integrado com o TAF.  
No momento em que foi cadastrado os afastamentos de sequência 004 a informação foi gravada no GPE e foram integrados com o TAF 4 (quatro) eventos S-2230, um evento para cada sequência de afastamento cadastrado.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040046554)  
  
**Observação:** O cenário narrado acima é um dos diversos cenários previstos no [MOS - Manual de Orientações do eSocial,](https://www.gov.br/esocial/pt-br/documentacao-tecnica) mas o importante é verificar a quantidade de dias do 1º afastamento e em qual dos exemplos sua situação se enquadra.

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
