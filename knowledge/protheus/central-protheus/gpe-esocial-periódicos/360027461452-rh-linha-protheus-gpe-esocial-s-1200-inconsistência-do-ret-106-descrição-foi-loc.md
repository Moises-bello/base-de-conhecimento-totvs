---
article_id: 360027461452
category: GPE - eSocial - Periódicos
content_hash: b0123c95d9508a902129d506fc6f3b63a81f35bf104a9b0e308154b3edb8b44d
fetched_at: '2026-06-28T22:45:07.258097+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200 - Inconsistência do RET - 106
  - Descrição: Foi Localizado no sistema um evento em duplicidade com o evento a ser
  enviado, mesmo Tipo de Inscrição, CPF do Trabalhador, Período de Apuração'
type: support-article
updated_at: '2026-06-26T10:41:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027461452-RH-Linha-Protheus-GPE-eSocial-S-1200-Inconsist%C3%AAncia-do-RET-106-Descri%C3%A7%C3%A3o-Foi-Localizado-no-sistema-um-evento-em-duplicidade-com-o-evento-a-ser-enviado-mesmo-Tipo-de-Inscri%C3%A7%C3%A3o-CPF-do-Trabalhador-Per%C3%ADodo-de-Apura%C3%A7%C3%A3o
---

**Ocorrência**Foi Localizado no sistema um evento em duplicidade com o evento a ser enviado, mesmo Tipo de Inscrição, CPF do Trabalhador, Período de Apuração.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**A inconsistência apresentada é um erro de retorno do RET (Governo) na tentativa de envio de um **evento já existente na base do Esocial** para mesma Empresa, mesmo Trabalhador e mesmo Período de Apuração.  
  
Por **exemplo**: um Pró-labore que tem registro e recebe remuneração por duas Filiais (01 e 02) de mesma Raiz de CNPJ, no Protheus ele possui dois registros, um para cada Filial e seria necessário processar a Folha de Pagamento para cada Filial, mas ao enviar ao RET (Governo) o evento S-1200 da filial 01 e depois tentar enviar um novo evento da Filial 02 o Esocial recusará esse segundo com a mensagem indicada acima.  
  
**Solução**Para o eSocial só deve existir um **único Evento Periódico para mesma raiz de CNPJ e mesmo CPF** por período, ou seja, no exemplo narrado acima o Protheus deve considerar esse Trabalhador como Múltiplos Vínculos e gerar um único evento S-1200 aglutinando as informações da Filial 01 e 02.  
  
Para que o Evento Periódico de um Trabalhador seja gerado como Múltiplos Vínculos é necessário realizar as parametrizações e validações da documentação disponível no *link* abaixo:  
[MP - GPE - eSocial - S-1200 - Como gerar funcionários com múltiplos vínculos no evento S-1200](http://tdn.totvs.com/pages/releaseview.action?pageId=374317457)Seguindo o exemplo narrado acima, para solucionar o erro será necessário **excluir** do RET (Governo) **com um evento S-3000 o evento S-1200 enviado**, ajustar o Trabalhador como Múltiplos Vínculos e gerar um novo evento S-1200 Através do GPE.[MP - GPE - eSocial - S-3000 - Como realizar a exclusão de um Evento Periódico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027742231)  
Segue abaixo um exemplo de geração do XML do evento S-1200 de Múltiplos Vínculos com remuneração em duas Filiais de mesma raiz de CNPJ.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027346231)  
**Verifique** também o mnemônico **P\_ESOCMV**: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039554533>  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
