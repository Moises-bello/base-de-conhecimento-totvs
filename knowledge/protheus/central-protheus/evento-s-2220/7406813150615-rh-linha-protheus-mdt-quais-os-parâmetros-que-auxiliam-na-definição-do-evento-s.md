---
article_id: 7406813150615
category: Evento S-2220
content_hash: 29dfacdb89a0229a840e2183627cd35a01bdb96eb4699f7ed0f25183ab172ef5
fetched_at: '2026-06-28T22:45:25.560799+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - Quais os parâmetros que auxiliam na definição do
  evento S-2220
type: support-article
updated_at: '2025-03-11T18:55:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7406813150615-RH-Linha-Protheus-MDT-Quais-os-par%C3%A2metros-que-auxiliam-na-defini%C3%A7%C3%A3o-do-evento-S-2220
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25287344526487) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais os parâmetros que auxiliam na definição do evento S-2220?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Cada empresa pode ter um cenário específico portanto é importante avaliar nossa documentação centralizadora sobre a geração do eventos S-2220, os parâmetros que podem interferir ou configurar para atender as diferentes necessidades de cada empresa.  
Consulte a documentação no link <https://tdn.totvs.com/display/PROT/S-1.0-+eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2220>  
  
**Parâmetros:**

**\* MV\_NG2ESOC=**  Indica se o sistema de Medicina e Segurança do Trabalho irá gerar registros no SIGATAF ou Middleware. 1 = Sim, 2 = Não.

**\* MV\_MID=** Habilita a integração de dados do eSocial com o Middleware. Se .T. Integra e se .F. não integra.

**\* MV\_NG2DTES=** Define a data incial de obrigatoriedade de envio dos eventos de SST ao eSocial.

**\* MV\_NG2AVIS=** Na ocorrência de inconsistência no envio ao eSocial. 0= Emite Aviso; 1= Avisa e impede processo; 2= Não emite aviso.

**\*** **MV\_NG2NENV=** Indica quais categorias de funcionários não terão os eventos de SST comunicados ao SIGATAF/Middleware.

**\*** **MV\_NG2RASO=** Indica na geração do ASO, como deve-se considerar a opção "Apto com restrição". 1= Apto; 2= Inapto.

**\* MV\_NG2INDR=** Indica se a tag <indResult> será enviada no evento S-2220. 1- Sim; 2- Não.  
  
**Saiba Mais**

[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico?page=1#articles)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
