---
article_id: 4410249729687
category: SIGAEST - CUSTOS
content_hash: b32243641973abb768450886accdc4acb6a29f2ceb5b0e5101226e558c4bf6cd
fetched_at: '2026-06-28T22:39:02.099274+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como Contabilizar
  Devolução de Pedido de Venda?
type: support-article
updated_at: '2021-10-07T16:54:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410249729687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-Contabilizar-Devolu%C3%A7%C3%A3o-de-Pedido-de-Venda
---

**Dúvida**Como posso contabilizar a devolução de pedido de venda no Recálculo do Custo Médio ou na Rotina de Contabilização Offline?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Para contabilizar a devolução de pedido de vendas, primeiro precisa criar um lançamento padrão do código 641 para isso deve seguir o caminho abaixo:

Acessar o módulo de Estoque/Custos e ir em "Atualizações -> Cadastro -> Lançamentos Padronizados" e clicar em incluir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410249208471/mceclip0.png)

OBS: O Suporte Padrão não valida regra de negócio colocado no campo CT5\_VLR01, para isso utilizamos a regra simples de apenas contabilizar o custo do produto colocando a regra "SD1->D1\_CUSTO":

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410252951575/mceclip2.png)

Após isso, acessar o módulo de Faturamento e efetuar um pedido de venda e finalizar conforme exemplo abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410252982679/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410252996631/mceclip4.png)

Após isso fazer a devolução dessa nota fiscal no módulo de Compras e confirmar, conforme exemplo abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410253071895/mceclip5.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410253095575/mceclip7.png)

Após isso, basta acessar à rotina de Custo Médio (MATA330) ou a rotina de Contabilização Offline (MATA331) e deixar o parâmetro "Gerar Lancto Contábil = Sim":

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410249512855/mceclip8.png)

Após a finalização da contabilização, basta acessar à tabela CT2 e validar que o movimento do Lançamento Padrão 641 que é a devolução de pedido de vendas foram contabilizados:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410253223319/mceclip9.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-MP-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-?source=search)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Contabilizar as Movimentações Internas do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791)*
