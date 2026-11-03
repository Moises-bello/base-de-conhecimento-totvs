---
article_id: 360052346974
category: Chão de Fábrica (SIGASFC)
content_hash: 6d7b9a79e94751e90750bc6e8fa56068362259a52fe5514597ad5cfdfe982daf
fetched_at: '2026-06-28T22:42:49.898601+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: MP - SIGASFC - Cancelar o início de um apontamento no módulo SIGAACD, quando
  existir integração com o SIGASFC
type: support-article
updated_at: '2020-08-20T12:05:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052346974-MP-SIGASFC-Cancelar-o-in%C3%ADcio-de-um-apontamento-no-m%C3%B3dulo-SIGAACD-quando-existir-integra%C3%A7%C3%A3o-com-o-SIGASFC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:15 min**  
 **Dúvida**Como cancelar o início de um apontamento no módulo **SIGAACD - ACD**, quando existir integração com o **SIGASFC - Chão de Fábrica**?  
   
 **Ambiente**Microsiga Protheus – Chão de Fábrica - Versão 12  
  
**Solução**Se for necessário estornar o início de um apontamento do módulo **SIGAACD**, deverá ser utilizado o programa **ACDV315** **- Gerenciar Apont Pr**, opção **Cancelar Movimento**.  
  
A opção **Cancelar Movimento** irá cancelar os movimentos realizados no módulo **SIGAACD** que ainda não foram integrados com o **Chão de Fábrica**. Os movimentos possíveis de cancelamento são o início de apontamento, e apontamentos que foram realizados utilizando uma transação parametrizada para não finalizar o início **CBI\_FIMINI - Finaliza Inicio** igual a **2**. Somente serão consideradas as movimentações que ainda não foram enviadas ao **Chão de Fábrica**, identificadas pelo campo **CZH\_STTR - Situação** igual a **1**.  
  
Para cancelar os movimentos, é necessário informar a ordem de produção, e opcionalmente o código da operação e código do *Split*.  
  
Se for informada apenas a ordem de produção, serão cancelados todos os movimentos da ordem de produção, independentemente da operação ou *Split* existentes.  
  
Se for informada a ordem de produção e o código da operação, serão cancelados todos os movimentos relacionados a operação da ordem de produção que foi informada.  
  
Se for informada a ordem de produção, código da operação e *Split*, serão cancelados apenas os movimentos que pertencem ao *Split* informado.  
  
Esta funcionalidade é importante quando é necessário realizar a exclusão da ordem de produção no programa **MATA650 - Ordem de Produção**, ou quando é realizado o início de uma produção de forma errada.
