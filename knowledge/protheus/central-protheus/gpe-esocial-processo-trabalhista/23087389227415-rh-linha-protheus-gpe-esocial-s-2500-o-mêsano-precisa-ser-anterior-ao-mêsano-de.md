---
article_id: 23087389227415
category: GPE - eSocial - Processo Trabalhista
content_hash: 012d8646ef64ed03e98a38e5f94da7bc039d153186e9aab71a13fd68941148cc
fetched_at: '2026-06-28T22:45:00.516575+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - O mês/ano precisa ser anterior
  ao mês/ano de "data da sentença" ou Data da conciliação.
type: support-article
updated_at: '2024-04-29T13:21:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23087389227415-RH-Linha-Protheus-GPE-eSocial-S-2500-O-m%C3%AAs-ano-precisa-ser-anterior-ao-m%C3%AAs-ano-de-data-da-senten%C3%A7a-ou-Data-da-concilia%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23087389185943) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo SIGAGPE, ao editar o processo trabalhista incluindo um contrato de trabalho na rotina **Dados do eSocial (TAFA552D)** e informar a **Competência Final** é apresentada a mensagem **O mês/ano precisa ser anterior ao mês/ano de "data da sentença" ou Data da conciliação.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23087421545495)  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Essa mensagem é apresentada quando o preenchimento do campo **Competência Final** foi com um mês e ano posterior ao mês e ano da data da sentença ou data da conciliação.  
  
**Solução**Conforme regra do eSocial, o campo Competência Final deve ser preenchido com a data que se refere o processo ou conciliação, no formato AAAA-MM e tem a seguinte validação:  
**Validação:** Deve ser igual ou posterior a [compIni](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr_compIni) e igual ou anterior ao mês/ano de [dtSent](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/index.html#2500_infoProcesso_dadosCompl_infoProcJud_dtSent) ou [dtCCP](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/index.html#2500_infoProcesso_dadosCompl_infoCCP_dtCCP).  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23087389192599)  
  
Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847-RH-Linha-Protheus-GPE-eSocial-Processos-Trabalhistas-Premissas-para-gera%C3%A7%C3%A3o-dos-eventos-do-eSocial-para-Processos-Trabalhistas?source=search)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
