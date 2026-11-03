---
article_id: 360035497774
category: GPE - eSocial - Periódicos
content_hash: 594dd92684c3ea86a814de4c6737d15ca8feb54463be210f1f894d0d6e250fa8
fetched_at: '2026-06-28T22:45:09.053965+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1299 - Inconsistência RET 162 - Descrição:
  O Trabalhador com CPF X e Matricula Y consta na base de dados do Ambiente Nacional
  do eSocial, mas não foi informada sua remuneração'
type: support-article
updated_at: '2025-07-24T15:01:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035497774-RH-Linha-Protheus-GPE-eSocial-S-1299-Inconsist%C3%AAncia-RET-162-Descri%C3%A7%C3%A3o-O-Trabalhador-com-CPF-X-e-Matricula-Y-consta-na-base-de-dados-do-Ambiente-Nacional-do-eSocial-mas-n%C3%A3o-foi-informada-sua-remunera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23084391295511) Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**S-1299 - Inconsistência do RET - 162 - Descrição: O Trabalhador com CPF X e Matricula Y consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Essa é uma mensagem de inconsistência retornada pelo RET (Governo) no envio do evento S-1299, normalmente ela ocorre quando:

1. Existe um Trabalhador com S-2200 na base do eSocial e ainda não foi enviado o seu evento S-1200 ou seu evento S-2299;
2. Existe um Trabalhador com S-2200 na base do eSocial e não foi enviado o S-1200 pois não há valores calculados, em um cenário onde apesar de estar afastado no Protheus não consta S-2230 transmitido ao eSocial.
3. Porque foram enviados indevidamente dois eventos S-2200 para o mesmo CPF com Matriculas do eSocial distintas;

**Solução**Para cada cenário acima realize os procedimentos indicados em cada passo com mesmo número:

1. Verifique como está o cálculo da Folha de Pagamento deste Trabalhador no GPE.  
   Caso ele seja Ativo, tente realizar uma nova integração do evento S-1200 filtrando somente esse Trabalhador e análise a mensagem do log de Integração.  
     
   Caso ele seja Inativo, verifique se o cálculo da Rescisão foi efetivado na Folha de Pagamento do GPE e, se for o caso, realize uma nova integração do evento S-2299 e análise se é apresentada alguma mensagem de erro na Integração.  
     
   Temos mapeados cenários em que o Trabalhador foi Transferido para uma outra Empresa, porém essa informação não foi enviada para o eSocial. Neste caso realize o procedimento indicado no artigo: [MP - GPE - eSocial - S-2200/S-2206/S-2299 - Como reprocessar a transferência no SIGAGPE para integração com o TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029098714/)
2. Verifique se o afastamento em questão consta no portal eSocial:  
   Caso não estiver no portal eSocial e pendente de envio no TAF, realize a transmissão do evento S-2230.  
   Caso o afastamento constar somente no GPE, realize a integração do afastamento para o TAF utilizando o schedule/job e realize a transmissão do S-2230 ao eSocial: [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como funciona o Job/Schedule na prática referente a integração das Alterações Salariais, fim de afastamento, trocas de turno e alteração na função com o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035063413-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-funciona-o-Job-Schedule-na-pr%C3%A1tica-referente-a-integra%C3%A7%C3%A3o-das-Altera%C3%A7%C3%B5es-Salariais-fim-de-afastamento-trocas-de-turno-e-altera%C3%A7%C3%A3o-na-fun%C3%A7%C3%A3o-com-o-TAF)
3. Acesse o portal do eSocial, filtre o CPF deste Trabalhador com Vínculo e verifique a quantas matriculas ele está associado, caso indevidamente exista mais de uma matricula você terá que excluir a matricula errada.   
   No GPE essa informação fica localizada no campo RA\_CODUNIC e no TAF no campo C9V\_MATRIC;

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
