---
article_id: 360053690814
category: GPE - eSocial - Periódicos
content_hash: d269960262f0fa3c3e2211acb6ed40927472555771090d8e1208ee724dd2550b
fetched_at: '2026-06-28T22:45:08.868031+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200/S-2299/S-1210 - Inconsistência
  do RET - 620 - Descrição : A folha de pagamento do período xxxxxx já foi fechada,
  para altera-la será necessário reabri-la'
type: support-article
updated_at: '2025-07-17T18:59:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053690814-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-S-1210-Inconsist%C3%AAncia-do-RET-620-Descri%C3%A7%C3%A3o-A-folha-de-pagamento-do-per%C3%ADodo-xxxxxx-j%C3%A1-foi-fechada-para-altera-la-ser%C3%A1-necess%C3%A1rio-reabri-la
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16485987579159) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**Ao enviar os eventos remuneratórios para o eSocial, é retornada a inconsistência do governo: Inconsistência do RET - 620 - Descrição : A folha de pagamento do período xxxxxx já foi fechada, para altera-lá será necessário reabri-la  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26109130894999)  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Causa**Esse incidente ocorre, pois o **período do evento** que está sendo transmitido encontra-se **fechado**.  
Ressaltamos que também não é possível excluir nenhum dos eventos periódicos relativos a um período de apuração que esteja fechado (ou seja, para o qual já exista evento S-1299) antes do envio do **evento de reabertura** respectivo **(S-1298)** para o período de apuração  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Realize a reabertura do período transmitindo o evento S-1298 conforme artigo:  
[MP - GPE - eSocial - S-1298 - Como reabrir um período no eSocial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025816453-MP-GPE-eSocial-S-1298-Como-reabrir-um-per%C3%ADodo-no-eSocial-?source=search)  
  
**2.** Após realizar a abertura do período e encaminhar os eventos remuneratórios e de pagamento, é necessário realizar o fechamento com o evento S-1299 conforme artigo:  
[MP - GPE - eSocial - S-1299 - Como gerar o evento S-1299 (fechamento periódicos) para transmitir ao RET](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022286212-MP-GPE-eSocial-S-1299-Como-gerar-o-evento-S-1299-fechamento-peri%C3%B3dicos-para-transmitir-ao-RET?source=search)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos **eventos futuros**, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
