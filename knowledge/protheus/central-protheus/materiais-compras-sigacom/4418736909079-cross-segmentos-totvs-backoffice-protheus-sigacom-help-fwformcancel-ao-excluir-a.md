---
article_id: 4418736909079
category: Materiais - Compras (SIGACOM)
content_hash: a6d4c1b5c8dfe289f86bc624f16a701df19eca9f56ad4981abe63afb8cfbb01a
fetched_at: '2026-06-28T22:41:18.923769+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help FWFORMCANCEL ao
  excluir amarração Produto x Fornecedor
type: support-article
updated_at: '2024-10-15T17:41:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418736909079-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-FWFORMCANCEL-ao-excluir-amarra%C3%A7%C3%A3o-Produto-x-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25339096018967) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Ao excluir a amarração Produto x Fornecedor é apresentado o Help FWFORMCANCEL.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418743076887)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27087134450839)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12

**Solução**

Quando a amarração Produto x Fornecedor estiver associada à Solicitação de Compras ou a uma Tabela de Preços não será possível a exclusão. Conforme a mensagem apresentada essa amarração foi utilizada em uma Solicitação de Compra, ou em outras rotinas. Dessa forma, uma vez excluída afetaria a integridade do sistema.

![20220111_140951.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4418729303447)

Caso a amarração do produto x fornecedor não necessite mais ser utilizada, nossa sugestão, seria bloquear essa informação.

Segue passo a passo abaixo para Bloqueio do cadastro.

1.Acesse o configurador -> Base de Dados -> Dicionário -> Base de dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25339096023447)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25339096026519)

2.Localize a tabela SA5 ( produto x fornecedor ).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25339096033559)

3.Marque o campo Bloqueio automático e clique em Finalizar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25339096038423)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25339096043543)

4.Atualize a Base de dados (Para esse processo, é necessário ter acesso exclusivo ao sistema).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25339103160983)

5.Acesse novamente o Protheus e vá até o cadastro de amarração produto x fornecedor. O campo de Bloqueado aparecerá na última posição da linha. Basta clicar em Sim, e essa amarração ficará bloqueada e o sistema não a considerará mais, nas rotinas padrão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25339103162519)

6.A amarração bloqueada será apresentada na cor cinza no browser da rotina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25339103165975)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
