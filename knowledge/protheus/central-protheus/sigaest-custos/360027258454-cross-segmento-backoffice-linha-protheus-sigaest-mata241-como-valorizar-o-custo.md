---
article_id: 360027258454
category: SIGAEST - CUSTOS
content_hash: 9e92fd5b753f52ccbae2635c897042ccbf5bd360739442d78ec5771146a492e7
fetched_at: '2026-06-28T22:39:02.051951+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Como valorizar
  o custo de um subproduto que foi criado por estrutura negativa?
type: support-article
updated_at: '2025-03-12T12:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027258454-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Como-valorizar-o-custo-de-um-subproduto-que-foi-criado-por-estrutura-negativa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503817837335)** Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Ao efetuar [o processo de criação de um subproduto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025539152-MP-SIGAPCP-Como-cadastrar-e-qual-%C3%A9-o-funcionamento-do-subproduto) pode-se ter dúvidas sobre a valorização do custo desse subproduto. Como proceder?   
  
**Ambiente**Protheus – Estoque – A partir da versão 11.80  
  
**Solução**

**Exemplo para um produto novo ainda sem saldo**

Ao criar o subproduto na rotina cadastro de produtos (MATA010), antes de executar o procedimento indicado no [artigo,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025539152-MP-SIGAPCP-Como-cadastrar-e-qual-%C3%A9-o-funcionamento-do-subproduto) pode-se efetuar o acerto de custo do produto pela rotina movimentos internos como destacado abaixo:

**1º -** Incluir um tipo de movimentação via MATA230:

• Tipo TM = Devolução / Valorizado (F5\_VAL) = SIM / Qtd. Zero (F5\_QTDZERO) = SIM

**2º -** Após ter definido o valor correto, incluir uma movimentação interna com o tipo de movimentação criada anteriormente, informando o valor a devolver no campo D3\_CUSTO1  na rotina de Movimentações Internas (MATA240).

**Exemplo par****a um produto que já contém saldo**

**1º -** Incluir um tipo de movimentação via MATA230:

• Tipo TM = Devolução / Valorizado (F5\_VAL) = SIM / Qtd. Zero (F5\_QTDZERO) = SIM

**2º -** Verificar via tabela SB2, no campo B2\_VATU, o valor dos produtos em estoque. Este campo armazena o valor total do produto em estoque com relação à quantidade informada no campo B2\_QATU1. Sendo assim o valor unitário do produto seria B2\_VATU1 / B2\_QATU.

Exemplo: B2\_QATU = 100,00, B2\_VATU = 200,00, o custo unitário é 2,00.

**3º -** Após verificar o valor que consta na SB2, e ter definido o valor correto, incluir uma movimentação interna com o tipo de movimentação criada anteriormente, informando o valor a requisitar ou devolver no campo D3\_CUSTO1. Na rotina MATA240

Após efetuado o processo acima todas as próximas movimentações que gerarem saldo do subproduto serão valorizadas conforme o valor indicado no campo B2\_CM1.

**Saiba mais:**

*[MP - SIGAEST - Acerto de Custo dos Produtos em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614)*

*[MP - SIGAPCP - Como cadastrar e qual é o funcionamento do subproduto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025539152-MP-SIGAPCP-Como-cadastrar-e-qual-%C3%A9-o-funcionamento-do-subproduto)*

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
