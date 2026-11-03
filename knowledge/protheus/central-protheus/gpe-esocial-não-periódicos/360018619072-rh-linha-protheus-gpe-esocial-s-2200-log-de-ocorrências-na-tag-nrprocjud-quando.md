---
article_id: 360018619072
category: GPE - eSocial - Não Periódicos
content_hash: 3bcf9cb49bfe2450d86595fe26d6df12bf6820c6e69b5099f757cf7dacce52fd
fetched_at: '2026-06-28T22:45:04.433747+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200  - Log de ocorrências na Tag nrProcJud
  quando cliente não possui processos para menores de 14 anos
type: support-article
updated_at: '2026-06-16T13:35:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018619072-RH-Linha-Protheus-GPE-eSocial-S-2200-Log-de-ocorr%C3%AAncias-na-Tag-nrProcJud-quando-cliente-n%C3%A3o-possui-processos-para-menores-de-14-anos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41262163422103) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Quando solicitada geração do evento S-2200 é gerado log de ocorrências na Tag nrProcJud quando cliente não possui processos para contratação de menores de 14 anos, em qualquer categoria, e de maiores de 14 e menores de 16, em categoria diferente de Aprendiz.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Necessário verificar se o campo **ProcMenor14 (RA\_NJUD14)** referente a identificação de processo judicial para trabalhadores menores de 14 anos está preenchido no cadastro do funcionário.

Conforme regra do eSocial é obrigatório enviar o grupo **nrProcJud** com a tag **alvaraJudicial. Quando:** Contratação de menores de 14 anos, em qualquer categoria, e de maiores de 14 e menores de 16, em categoria diferente de "Aprendiz".  
  
Caso esteja preenchido, obriga informar os outros campos referentes ao processo para permitir a contratação destes trabalhadores, lembrando que é **necessário também preencher a tabela S-1070 no TAF, neste caso.**  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
