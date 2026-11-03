---
article_id: 1500004523481
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b372537af4f47e82973741eb7586c86550c6c455bd5f66066d0152883ecd9373
fetched_at: '2026-06-28T22:38:58.583522+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - MATA105 - "Alias does not exist on MSGETDADOS:NEW(MSGETDAD.PRW)"
  ao excluir S.A
type: support-article
updated_at: '2021-04-28T15:44:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004523481-MP-SIGAEST-MATA105-Alias-does-not-exist-on-MSGETDADOS-NEW-MSGETDAD-PRW-ao-excluir-S-A
---

**Dúvida**Ao acessar à rotina MATA105 - Solicitação ao Armazém - e excluir uma SA, ocorre o error.log "*Alias does not exist:* *on MSGETDADOS:NEW(MSGETDAD.PRW)*". O que fazer para resolver este erro?  
  
**Ambiente**Microsiga Protheus – Estoque/Custos – A partir da versão 12.1.17  
  
**Solução**Este problema ocorre normalmente quando está tentando Alterar ou Excluir uma Solicitação ao Armazém em um módulo **diferente** da qual ela foi criada. Pode ser também por ter algum insumo preso à SA que ainda está em aberto, como Ordem de Serviço ou Solicitação de Compras.

**Exemplo**

Por exemplo: Se a Solicitação ao Armazém ou Solicitação de Compras foi originada através do módulo Manutenção de Ativos, deve-se acessar às rotinas: Alteração de O.S ou Programação de O.S, para exclusão do insumo que originou a S.A.  
  
Caminho para acesso à rotina: *Atualizações / Controle de Oficina / Plano de Manutenção / Alteração de O.S* -> Selecionar a O.S que originou a S.A -> Selecionar o insumo e excluir o registro que está vinculado a S.A. Após este procedimento será cancelada a S.A no Estoque.

**[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=549191358)** para visualizar o boletim técnico que aborda este bloqueio de exclusão/alteração em módulos diferentes.

**Importante:**

Sempre manter o acumulado do módulo Manutenção de Ativos e Estoque/Custos atualizados.

**[Acumulado Manutenção de Ativos (selecionar conforme sua release)](https://tdn.totvs.com/pages/releaseview.action?pageId=522005297)**

**[Acumulado Estoque/Custos (selecionar conforme sua release)](https://tdn.totvs.com/pages/releaseview.action?pageId=522000602)**

Observação: Sempre aplicar pacotes primeiramente em ambiente de homologação.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
