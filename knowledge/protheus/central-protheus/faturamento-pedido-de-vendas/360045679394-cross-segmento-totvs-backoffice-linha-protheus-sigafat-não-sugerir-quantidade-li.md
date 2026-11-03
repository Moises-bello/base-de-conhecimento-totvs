---
article_id: 360045679394
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 5650822da7fdf53e329c40513c67df02053a294e6a68d9266dd86102261d14a1
fetched_at: '2026-06-28T22:38:38.570589+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Não sugerir
  quantidade liberada no Pedido de Vendas
type: support-article
updated_at: '2023-04-20T13:11:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045679394-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-N%C3%A3o-sugerir-quantidade-liberada-no-Pedido-de-Vendas
---

**Dúvida**

Não sugerir quantidade liberada no Pedido de Vendas.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

No SIGACFG (Configurador) é possível setar a resposta "**Não**" para a pergunta "**Sugere Qtde Liber.?**" nos parâmetros acessados via "F12":

1. Acessar o Configurador (SIGACFG);  
2. Usuários > Senhas > Config. Perguntas;  
3. Incluir > Grupo: **MTA440**;  
4. Selecionar o usuário ou grupo de usuários (obrigatório);  
5. Clicar na **Pergunta 03 (Sugere Qtde Liber.?)** e clicar em deletar em seu teclado (a linha deixará de ficar com sombreado cinza);  
6. Na coluna "**Conteúdo**" registrar com a resposta = **2 - Não** (para este caso);  
7. Confirmar;

Saiba Mais: **[FAT0009\_Impedir\_Liberação\_Parcial\_do\_Pedido\_de\_Vendas](https://tdn.totvs.com/pages/viewpage.action?pageId=225264398)**
