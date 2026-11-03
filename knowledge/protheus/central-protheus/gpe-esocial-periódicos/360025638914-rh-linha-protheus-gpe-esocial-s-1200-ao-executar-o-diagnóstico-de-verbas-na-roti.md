---
article_id: 360025638914
category: GPE - eSocial - Periódicos
content_hash: b14bcd55e3a58deb6f101dd63754f8fee7e685fe936817e3e846fe9721ef68ee
fetched_at: '2026-06-28T22:45:07.654597+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Ao executar o Diagnóstico de
  Verbas na rotina eventos periódicos o sistema gera a mensagem no log "Verbas de
  Assistência Médica com a Natureza incorreta"
type: support-article
updated_at: '2025-07-21T14:46:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025638914-RH-Linha-Protheus-GPE-eSocial-S-1200-Ao-executar-o-Diagn%C3%B3stico-de-Verbas-na-rotina-eventos-peri%C3%B3dicos-o-sistema-gera-a-mensagem-no-log-Verbas-de-Assist%C3%AAncia-M%C3%A9dica-com-a-Natureza-incorreta
---

**Ocorrência**Ao executar o Diagnóstico de Verbas na rotina eventos periódicos o sistema gera a mensagem no log "Verbas de Assistência Médica com a Natureza incorreta".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
 **Causa**Verba com a natureza incorreta na rotina de plano de saúde.  
  
**Solução**Conforme determinação do **eSocial** o campo natureza (*RV\_NATUREZ*) do cadastro de verbas deve ter o código **9219** (assistência médica).

Existe cenários que a verba que está descrita no log com a natureza incorreta não trata-se da verba que é utilizada pelo usuário atualmente nos cálculos de assistência médica.

Isso se deve ao fato que de para assistência médica o sistema realizada busca nas tabelas de cálculo de plano de saúde na competência informada para geração do diagnóstico de verbas. Com isso, se algum trabalhador está com a verba descrita no log nas tabelas de plano de saúde vai ocorrer o erro.

Para correção analise se a verba incorreta apresentada no log está nas rotinas abaixo.

* Planos Ativos (*RHK*)
* Histórico Calculo Plano Saúde (*RHS*)
* Hist. Co-partic. e Reembolso (*RHP*)

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
