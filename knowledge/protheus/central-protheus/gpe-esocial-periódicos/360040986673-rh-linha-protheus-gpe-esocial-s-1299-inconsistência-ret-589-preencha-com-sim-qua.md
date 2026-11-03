---
article_id: 360040986673
category: GPE - eSocial - Periódicos
content_hash: 78808b75c7966f9b80fd27539dd669443c59d48d291019f773ef536ecfc54080
fetched_at: '2026-06-28T22:45:09.059242+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1299 - Inconsistência RET 589 - Preencha
  com Sim quando existir informação de pagamento de rendimento do trabalho no período
  e Não quando não existir
type: support-article
updated_at: '2025-07-22T12:11:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040986673-RH-Linha-Protheus-GPE-eSocial-S-1299-Inconsist%C3%AAncia-RET-589-Preencha-com-Sim-quando-existir-informa%C3%A7%C3%A3o-de-pagamento-de-rendimento-do-trabalho-no-per%C3%ADodo-e-N%C3%A3o-quando-n%C3%A3o-existir
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27174353255191) Tempo aproximado para leitura: 00:01:00 min****Ocorrência**Inconsistência RET 589 - Preencha com Sim quando existir informação de pagamento de rendimento do trabalho no período e Não quando não existir  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**Essa inconsistência ocorre porque é preenchido o campo **Pagamento Diversos** com SIM, porém não existe nenhum evento **S-1210** enviado nesse **período de apuração**, ou vice-versa.  
  
Esse erro é muito comum no **período de apuração** do 13º Salário que é **anual (AAAA)**, pois não existe evento **S-1210** para esse **período de apuração**. O IR retido no 13º Salário será enviado junto ao evento **S-1210** do **período de apuração** **12/AAAA**.  
  
**Solução**Acesse a rotina de Fechamento de Período (S-1299) no TAF pelo menu: Atualizações > Eventos Esocial > Periódicos > Fechamento Periódicos.  
  
![tmR5mBGtck.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001148061)  
  
Após acessar a rotina, localize o S-1299 com erro e ajuste as perguntas do evento conforme a realidade da sua Empresa e conforme eventos aguardados pelo eSocial para cada período de apuração.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27174332385943)  
  
Segue abaixo nossas documentações sobre a geração do evento S-1299 mensal e para o 13º Salário.

* [RH - Linha Protheus - GPE - eSocial - S-1299 - Como gerar o evento S-1299 (fechamento periódicos) para transmitir ao RET](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022286212)
* [RH - Linha Protheus - GPE - eSocial - S-1299 - Como integrar o evento S-1299 da folha do décimo terceiro para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021047432-MP-GPE-eSocial-S-1299-Anual-Criar-o-registro-do-fechamento-da-folha-anual-do-d%C3%A9cimo-para-o-TAF?source=search)

**Saiba Mais**

Para adquirir mais conhecimento acesse os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
