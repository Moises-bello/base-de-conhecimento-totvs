---
article_id: 360018354991
category: Materiais - Compras (SIGACOM)
content_hash: e9c2ac6d30bffefe63ae07d1a1770e77bfab5eeb08f11ef16a1f0e9f346849d6
fetched_at: '2026-06-28T22:41:15.926209+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como impedir o Solicitante
  de aprovar a própria Solicitação de Compras ?
type: support-article
updated_at: '2022-10-03T11:48:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018354991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-impedir-o-Solicitante-de-aprovar-a-pr%C3%B3pria-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**Como impedir o Solicitante de aprovar a própria Solicitação de Compras ?  
  
**Ambiente**Microsiga Protheus - Compras - A partir da versão P12.1.17  
  
**Solução**Por padrão do sistema, se a liberação da solicitação de compras for realizada pela própria rotina (MATA110), o sistema não validará o controle de alçadas de compras, assim o próprio usuário poderá realizar a aprovação do documento. A possibilidade será restringir o acesso do usuário ao botão 'APROVAÇÃO' contido em 'Outras Ações'. através do Módulo Configurador no cadastro do usuário, restringindo o acesso à esta opção do Menu.

### **Importante:** O processo de Bloqueio Simples está descontinuado a partir da versão**12.1.27**

Para aprovação pelo Controle de Alçadas, é necessário ter o cadastro de grupo de aprovação (MATA114) e que a Solicitação de Compras seja liberada pela rotina "liberação de documento" (MATA094), assim o solicitante não sendo o aprovador, não terá acesso a liberação.

***Saiba Mais :***

[MATA110: Bloqueio de Solicitações de Compras (Bloqueio Simples)](https://tdn.totvs.com/pages/releaseview.action?pageId=493631141)

[PCOM09002 - Configuração para Controle de Alçadas por Entidade Contábil - Solicitação de Compras e Armazém](https://tdn.totvs.com/pages/viewpage.action?pageId=284348332)

[MP - SIGACOM - Como é definido cadastro de Solicitantes ( MATA084 ) no Módulo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007049611)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
