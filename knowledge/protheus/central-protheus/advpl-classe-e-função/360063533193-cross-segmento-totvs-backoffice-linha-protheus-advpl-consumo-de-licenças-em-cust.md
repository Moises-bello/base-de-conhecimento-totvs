---
article_id: 360063533193
category: ADVPL - Classe e Função
content_hash: c28b267a6b98755a0a7eac10cff69c3211bd9a5d5d4db0c885d90a8a5b984417
fetched_at: '2026-06-28T22:40:15.666597+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Consumo de licenças
  em customizações. '
type: support-article
updated_at: '2021-05-18T17:26:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063533193-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consumo-de-licen%C3%A7as-em-customiza%C3%A7%C3%B5es
---

**Dúvida**Qual licença é consumida em customizações (*User Function*)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução****Consumo de licenças:**  
Realizado uma consulta do **DBAccess**será consumida uma licença **DBAccess**.  
  
Toda rotina customizada consome licenças seja ***Light*,** ***Full*** ou especifica quando chamado dentro do menu **Protheus**  ou na preparação do ambiente.

**Visão geral:**Rotinas customizadas executadas de dentro do Protheus sempre consomem a mesma licença que o módulo, seja ***Light**, **Full*** ou específica, exemplo:   
Uma rotina **u\_MinhaRotina** para executar a partir do menu do Financeiro, será utilizada a regra de escala do financeiro para consumir a licença.

Cada módulo do sistema tem uma regra de escala, que nada mais é do que as licenças que podem ser utilizadas naquele módulo, sendo que a escala começa da licença mais específica indo para a mais generalista.

* Para os módulos **NG** Medicina, **NG** Manutenção e **Trade *Easy Comex***a licença ***Full***não escala estes somente utilizam licenças ***Light***.

**Nota.:**  
**RpcSetType**(3) é de uso interno e restrito.  
As rotinas de usuário no sistema mesmo se utilizado do tipo 3, continuam consumindo licenças.

**Saiba mais**

[TOTVS License Server Virtual](https://tdn.totvs.com/display/framework/TOTVS+License+Server+Virtual)   
[RPCSETENV](https://tdn.totvs.com/pages/releaseview.action?pageId=6814927)
