---
article_id: 33772270254743
category: GPE - eSocial - Periódicos
content_hash: aebfbc74b1fc60cab304857c7003657abc2be798e4fa3c91749a158ae905f74a
fetched_at: '2026-06-28T22:45:07.373464+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210  - Como realizar a substituição
  da verba de Pensão alimentícia sobre férias
type: support-article
updated_at: '2026-06-03T16:15:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33772270254743-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-realizar-a-substitui%C3%A7%C3%A3o-da-verba-de-Pens%C3%A3o-aliment%C3%ADcia-sobre-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33772270202391) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como realizar a substituição da verba de Pensão férias, no eSocial para que não duplique os valores?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Quando a pensão é calculada apenas sobre as férias, e não sobre a folha (por falta de saldo), o S-1210 não gera o grupo de beneficiários, causando rejeição, pois há valor informado no S-1200 sem correspondente no S-1210.

Dessa forma, o esocial **não interpreta a pensão como zerada**, e por isso **exige a presença do grupo de beneficiários** no evento S-1210.

Para resolver, foi incluído um tratamento que substitui as **verbas de pensão sobre férias** (quando geradas no ideDmDev de folha) por **verbas sem incidência de IR para o eSocial.**

**Procedimento:**

1. Realize a criação da verba de substituição:

   Acesse o caminho: GPE > Atualizações > Definições Cálculo > Verbas

   **Configuração da Verba:**

   * Id de Cálculo: Sem ID
   * Tipo da Verba: 2 - Desconto
   * Natureza de Rubrica: 9989
   * Incidência IRRF: 9
   * Incidência INSS: 00
   * Incidência FGTS: 00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33772270205591)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33772270208279)

2. Entre na verba de Pensão alimentícia sobre férias e relacione a verba de substituição criada, a verba de pensão no campo de substituição (Vb Subst):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33772270213015)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33772280861591)

Na geração do evento S-1200, no grupo <ideDmDev> de Folha de Pagamento, as verbas de Pensão alimenticia de férias serão substituídas pela verba relacionada no campo Vb.Subst. (RV\_SUBST)

**Atenção**

* **Os cálculos de Férias e Folha de Pagamento não serão alterados, a modificação ocorre somente na geração dos eventos periódicos**

**Saiba Mais**

Para saber mais consulte os *links* abaixo:

[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=922698171)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
