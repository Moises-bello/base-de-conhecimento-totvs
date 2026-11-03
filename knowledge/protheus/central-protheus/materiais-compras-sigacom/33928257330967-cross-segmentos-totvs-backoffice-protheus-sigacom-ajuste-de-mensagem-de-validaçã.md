---
article_id: 33928257330967
category: Materiais - Compras (SIGACOM)
content_hash: d6630387e6dd8333d249b69edfd466b89d06c3141373d4bec20050abcc140a4a
fetched_at: '2026-06-28T22:41:13.112835+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ajuste de mensagem
  de validação Help A12006 incorreto
type: support-article
updated_at: '2025-08-04T14:21:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33928257330967-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ajuste-de-mensagem-de-valida%C3%A7%C3%A3o-Help-A12006-incorreto
---

**Ocorrência**  
No módulo Compras, ao tentar incluir uma Solicitação de Compras e é identificado um problema no Help **A12006** ao incluir uma solicitação de compra conforme o print abaixo, o texto a que ele se refere não corresponde a uma mensagem compreensível ao usuário final, pois indica uma validação referente à "tabela de filiais do sistema, fala sobre impostos genéricos e seu valor".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33928219618071)

**Ambiente**  
Protheus – Compras – A partir da versão 12  
  
**Solução**  
Para resolver este problema, siga estes passos:  
1. No módulo Configurador, vá exclusivamente ao menu Banco de Dados > Dicionário > Manutenção de Helps.  
2. Insira o código da Ajuda que será mantido e clique em Avançar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33928257304727)

Na próxima tela, insira os textos corretos para a Ajuda. Substituir Para os seguintes textos:

Ajuda de variável: Há alguns campos obrigatórios no item que não foram informados.

Ajuda com a solução: Verifique se os campos código do produto, quantidade, preço ou data prevista estão preenchidos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33928219619223)

Confirmar a gravação das modificações

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33928219620759)

Entre na rotina de Pedido de Compra e confirme que ao acionar o Help, ele exiba os textos corretos.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33928219621271)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[DMANMAT02-28927 Ajuda para Ajuste de DT Pedido de Compra](https://tdn.totvs.com/display/public/PROT/9431946+DMANMAT02-28927+DT+Ajuste+Help+Pedido+de+compras)
