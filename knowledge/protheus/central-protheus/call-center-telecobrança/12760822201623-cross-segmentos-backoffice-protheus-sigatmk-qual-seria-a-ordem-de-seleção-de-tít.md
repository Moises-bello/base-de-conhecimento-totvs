---
article_id: 12760822201623
category: Call Center - Telecobrança
content_hash: f6a0df21fae25c86d7f8035a8db61843e07ddf261b1283b860e8081689909294
fetched_at: '2026-06-28T22:41:28.548584+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK -  Qual seria a ordem de seleção
  de títulos ao incluir um novo Pré atendimento na rotina TMKA280
type: support-article
updated_at: '2026-03-11T19:16:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12760822201623-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Qual-seria-a-ordem-de-sele%C3%A7%C3%A3o-de-t%C3%ADtulos-ao-incluir-um-novo-Pr%C3%A9-atendimento-na-rotina-TMKA280
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38969659526935) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Qual seria ordem de seleção de títulos ao incluir um novo Pré atendimento na rotina TMKA280?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões  
  
**Solução**  
  
Na rotina de pré-atendimento ao efetuar o processo de Novo pré-atendimento (F6) que tem como objetivo realizar a seleção automática do atendimento.  
A seleção desses atendimentos utiliza como referencia dois parâmetros "MV\_TMKSELV" e "MV\_TMKSELN", cujo a funcionalidade seria de priorizar a ordem de seleção dos atendimentos efetuados pelos operadores.  
  
Contudo essa ordem pode ser diferente caso esses parâmetros não estejam ativos. Ocorre que quando esses parâmetros não estiverem ativos, o sistema priorizará o atendimento de acordo com a data de vencimento mais distante, levando em consideração o titulo vencido a mais tempo.   
  
A seleção dos atendimentos também é influenciada de acordo com a regra de seleção (TMKA160) estabelecida no grupo de atendimento vinculado ao operador em questão.

OBS: Caso o cliente já esteja sendo atendido por um operador, o sistema agrupa as cobranças para o mesmo operador. Conforme explicação realizada no vídeo explicativo do [How To | MP - SIGATMK - Telecobranças - Grupo de Cobrança #TOTVS Backoffice Linha Protheus](https://www.youtube.com/watch?v=zwZO6C6m8n0)

Funcionalidade dos parâmetros mencionados na documentação:  
**MV\_TMKSELV** (Indica se na solicitação de novo pré-atendimento, o sistema prioriza os títulos mais antigos com maior valor.  
**MV\_TMKSELN**(Indica se na solicitação de novo pré-atendimento o sistema prioriza os títulos mais novos com maior valor)  
  
**Saiba mais:**

* [Pré-Atendimento Telecobrança TMKA280](https://tdn.totvs.com/pages/releaseview.action?pageId=6787686)
* [Busca de títulos mais antigos de maior valor](https://tdn.totvs.com/pages/releaseview.action?pageId=6787683)
* [Procedimento de Seleção de Títulos ao utilizar o Grupo de Cobrança](https://tdn.totvs.com/pages/releaseview.action?pageId=225262693)
