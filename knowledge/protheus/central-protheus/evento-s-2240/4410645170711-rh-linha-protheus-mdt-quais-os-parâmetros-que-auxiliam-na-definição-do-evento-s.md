---
article_id: 4410645170711
category: Evento S-2240
content_hash: 4c5bdf5afc718d337ab69698e2f801a3fcd807cf281372588c0381525023aba9
fetched_at: '2026-06-28T22:45:23.491510+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - Quais os parâmetros que auxiliam na definição do
  evento S-2240
type: support-article
updated_at: '2024-11-27T21:27:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410645170711-RH-Linha-Protheus-MDT-Quais-os-par%C3%A2metros-que-auxiliam-na-defini%C3%A7%C3%A3o-do-evento-S-2240
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25676762501527) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Quais os parâmetros que auxiliam na definição do evento S-2240?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Cada empresa pode ter um cenário específico portanto é importante avaliar nossa documentação centralizadora sobre a geração do eventos S-2240, os parâmetros que podem interferir ou configurar para atender as diferentes necessidades de cada empresa.  
Consulte a documentação no link <https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2240>  
  
**Parâmetros:  
  
\* MV\_NG2ESOC=** Indica se o sistema de Medicina e Segurança do Trabalho irá gerar registros no SIGATAF ou Middleware. 1 = Sim, 2 = Não.

**\* MV\_MID=** Habilita a integração de dados do eSocial com o Middleware. Se .T. Integra e se .F. não integra.

**\* MV\_NG2DTES=** Define a data incial de obrigatoriedade de envio dos eventos de SST ao eSocial.

**\* MV\_NG2AVIS=** Na ocorrência de inconsistência no envio ao eSocial. 0= Emite Aviso; 1= Avisa e impede processo; 2= Não emite aviso.

**\* MV\_NG2NENV=** Indica quais categorias de funcionários não terão os eventos de SST comunicados ao SIGATAF/Middleware.

**\* MV\_NG2TDES=** Indica qual descrição pegar e considerar na rotina de Condições Ambientais de Trabalho no TAF. 1= Tarefa; 2= Cargo; 3= Função; 4= Cargo + Tarefa.

**\* MV\_NG2RIST=** Indica os tipos de Riscos que serão enviados ao TAF, além dos Riscos obrigatórios. 0=Nenhum;1=Ergo;2=Mec/Acid;3=Ergo/Mec/Acid;4=Perig;5=Todos.

**\* MV\_NG2VLAU=** Indica se somente irá enviar ao TAF Riscos que estejam vinculados a um Laudo PPRA no momento de envio. 1- Sim; 2- Não.

**\* MV\_NG2EPIR=**  Indica se pega as caraterísticas dos EPIs da entrega ou do Risco, para envio no evento S-2240. 1= Entrega; 2= Risco.

**\* MV\_NG2REST=** Indica que tipo de Responsável Ambiental será enviado ao TAF. 1=Médico Trab.;2=Engenheiro Trab.;3=Ambos;4=Todos.

**\* MV\_NG2EAMB=** Indica qual entidade será relacionada ao ambiente, para envio da tag <infoAmb> ao eSocial. 1- Centro Custo; 2- Depto; 3- Função; 4- Tarefa; 5- Func.

**\* MV\_NG2TPAG=** Indica se a qualificação do agente será buscada do cadastro de agentes ou de riscos. 1- Agentes; 2- Riscos.

**\*** **MV\_NG2RAMB=** Indica se serão enviados no S-2240 todos os resp. ambientais ou apenas os vinculados a laudos relacionados ao risco. 1- Todos; 2- Vinculados.

**\* MV\_NG2VEVP=** Indica se os eventos predecessores (S-1005/S-2190/S-2200/S-2300) devem ser validados na integração dos eventos de SST. 1- Sim; 2- Não.

**\*** **MV\_NG2DENO=** Indica a data em que os eventos não obrigatórios (S-2220/S-2240) para funcionários sem exposição a agentes nocivos devem começar a ser enviados.

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
