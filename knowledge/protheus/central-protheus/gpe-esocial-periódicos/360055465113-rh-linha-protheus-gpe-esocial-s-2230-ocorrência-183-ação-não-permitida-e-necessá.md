---
article_id: 360055465113
category: GPE - eSocial - Periódicos
content_hash: cdd4ad89d79b3d6406aac916e30fb17ec48fa72c3f6a6551fb9c35e0a0370813
fetched_at: '2026-06-28T22:45:09.119085+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2230 - Ocorrência 183 - Ação não permitida.
  E necessário que o trabalhador esteja em atividade na data do afastamento. Ação
  Sugerida: Verificar se a data do afastamento esta correta.'
type: support-article
updated_at: '2024-09-06T17:47:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055465113-RH-Linha-Protheus-GPE-eSocial-S-2230-Ocorr%C3%AAncia-183-A%C3%A7%C3%A3o-n%C3%A3o-permitida-E-necess%C3%A1rio-que-o-trabalhador-esteja-em-atividade-na-data-do-afastamento-A%C3%A7%C3%A3o-Sugerida-Verificar-se-a-data-do-afastamento-esta-correta
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26173811452183)** Tempo aproximado para leitura:**00:01:00 min** **Ocorrência**Na transmissão do envio do evento **S-2230** para o eSocial é apresentada inconsistência de retorno Código da **Ocorrência: 183** - Descrição : Ação não permitida. E necessário que o trabalhador esteja em atividade na data do afastamento. Ação Sugerida: Verificar se a data do afastamento esta correta.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26173811459223)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Causa**Normalmente esse erro ocorre pois esta sendo enviado um afastamento sem que o trabalhador tenha retornado do anterior, ou seja, o afastamento anterior não foi finalizado no eSocial. Também ocorre quando o afastamento está sendo enviado de forma completa (início e fim) porém no esocial já encontra-se a informação do início.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Consultar no portal do eSocial a existência de afastamento para o trabalhador [RH - Linha Protheus - GPE - eSocial - S-2230 - Como consultar no site do eSocial dados do evento S-2230 (Afastamento Temporário)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040817794-RH-Linha-Protheus-GPE-eSocial-S-2230-Como-consultar-no-site-do-eSocial-dados-do-evento-S-2230-Afastamento-Tempor%C3%A1rio)  
  
2. Caso exista afastamento no portal, verificar no módulo TAF pelo menu **->Atualizações ->Eventos Esocial ->Não periódicos ->Afastamento temporário** se existe também o evento com a data fim a ser transmitido   
3. Caso não exista o término do afastamento no TAF a integração poderá ser realizada de duas formas:  
  
3.1 Para realizar a integração automática da data fim do término do afastamento deve ser configurado o *job/schedule* conforme artigo:  
[RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job schedule GPEM026B na tela PO UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21979795766167-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B-na-tela-PO-UI)  
  
3.2 Também é possível incluir a data fim de afastamento no módulo TAF pelo menu **->Atualizações ->Eventos Esocial ->Não periódicos ->Afastamento temporário.** Clique em incluir, selecione apenas o **id do funcionário** e informe apenas a **data fim do afastamento.**Salve e transmita ao eSocial.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26173811460631)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26173811461783)  
  
Para que o sistema integre o S-2230 de afastamentos temporários **completos (início e fim)** mesmo para casos de **data de retorno futura** é necessário que o parâmetro **MV\_DTFIMA**esteja habilitado.  
Para entender como funciona o *Job/Schedule* na prática e executar manualmente após a configuração acesse os artigos:

* [MP - GPE - eSocial - S-2206/S-2230 - Como funciona o Job/Schedule na prática referente a integração das Alterações Salariais e Fim de Afastamento com o TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035063413)
* [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como executar o Job/Schedule manualmente na tela PO UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025368951)

Dúvidas relacionadas a retificação de afastamento verifique o artigo abaixo:

* [MP - GPE - eSocial - S-2230 - Como alterar/retificar um Afastamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025813493)

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos".Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
