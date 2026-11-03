---
article_id: 360044448933
category: Portal
content_hash: 6444409141e219379d54a2f15f122c0554b548633822b21e3a894c4ffa162b2b
fetched_at: '2026-06-28T22:46:37.893873+00:00'
product: rm
section_id: 1500000835141
source: central-rm
title: RH - RM - PTO - Bloquear o acesso de funcionários de férias ou em afastamento
  para visualizar espelho ponto no portal
type: support-article
updated_at: '2025-02-21T19:04:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044448933-RH-RM-PTO-Bloquear-o-acesso-de-funcion%C3%A1rios-de-f%C3%A9rias-ou-em-afastamento-para-visualizar-espelho-ponto-no-portal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16980740595223) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como impedir o acesso ao espelho de ponto, de funcionários de férias ou em afastamento no RM Portal?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões

**Solução**Para impedir o acesso de funcionários de férias ou em afastamento no RM Portal, siga os passos abaixo:

1. Acesse no modulo de Automação de Ponto o menu **Configurações | Parametrizador,** ao abrir o assistente clique em avançar. Selecione o processo **RM Portal** e avance novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30151181514007)

2- Selecione o grupo de acesso ao portal desejado, e clique no botão parametrizar;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30151181517335)

3- Ao abrir o novo assistente clique no botão avançar. E avance até a etapa "**Permissões"** e desmarque a flag do parâmetro "**Permitir acesso ao RM Portal para funcionários de férias/ em afastamento."**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30151181522327)  
  
Desta forma o usuário não terá acesso apenas ao espelho do cartão de Ponto e exibirá a mensagem: "Usuários em período de Férias ou Afastados não tem acesso ao Espelho." Após alteração, realize novo login no Portal RM.

Observação: Caso o funcionário selecione datas que não estejam contidas no período de gozo de férias o mesmo poderá proceder com a inclusão das batidas. Entretanto se pelo menos uma data estiver contida dentro do período de gozo, o sistema não permitirá a inclusão de batidas. O mesmo ocorrerá caso nenhuma data seja selecionada e o período possua interseção com o período de gozo.

**Saiba Mais:**  
[Permissões](https://tdn.totvs.com/pages/viewpage.action?pageId=452720001)
