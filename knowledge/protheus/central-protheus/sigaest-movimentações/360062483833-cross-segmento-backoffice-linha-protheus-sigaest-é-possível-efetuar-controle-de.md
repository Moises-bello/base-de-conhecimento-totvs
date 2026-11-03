---
article_id: 360062483833
category: SIGAEST - MOVIMENTAÇÕES
content_hash: eea3f9e4f62778f2dc2b89876c6b2ad51d4fb3fbe1193c340696b8df9621de0c
fetched_at: '2026-06-28T22:38:55.466134+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível efetuar
  controle de rastreabilidade por lote em apenas uma Filial?
type: support-article
updated_at: '2026-03-17T20:47:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062483833-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-efetuar-controle-de-rastreabilidade-por-lote-em-apenas-uma-Filial
---

No Protheus, é possível ativar o controle de rastreabilidade por lote para uma filial específica, desde que a tabela SB1 (Cadastro de Produtos) e o parâmetro MV\_RASTRO na tabela SX6 estejam configurados como exclusivos. Caso contrário, o controle será replicado para todas as filiais ou poderá causar erros no sistema. Recomenda-se consultoria in loco para empresas com movimentações já existentes ao implementar essa configuração.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39111714469143)** **Tempo aproximado para leitura:** 00:03:00 min

**Dúvida**

No Protheus, é possível ativar o controle de Rastreabilidade (`MV_RASTRO`) por lote para apenas uma filial específica?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus - SIGAEST - Todas as versões.

**Solução**

Sim, é possível realizar o controle de rastreio por filial. No entanto, para que essa configuração funcione de forma isolada sem afetar as demais unidades do grupo, é imprescindível o cumprimento das seguintes premissas de arquitetura de dados:

**OBRIGATÓRIO**

* **Tabela SB1 (Cadastro de Produtos):** Deve estar configurada como **Exclusiva** no dicionário de dados. Se a tabela for compartilhada, a ativação do controle de lote em um registro será replicada automaticamente para todas as filiais que compartilham a mesma tabela, isso vai gerar problemas internas de compatibilidade da validação de saldos para filiais que venham ou não a controlar saldos por lote.
* **Parâmetro MV\_RASTRO:** O parâmetro deve estar configurado como **Exclusivo** na tabela **SX6** (Parâmetros). Isso permite que cada filial possua seu próprio conteúdo para a variável, habilitando o rastreio apenas onde for desejado.

**Importante:**

Caso as premissas acima não sejam atendidas, o sistema poderá apresentar inconsistências na gravação dos lotes ou impedir movimentações de estoque. Para empresas que já possuem movimentações e desejam iniciar esse controle apenas em filiais específicas, **recomendamos o acompanhamento de uma consultoria** ***in loco*** **para validação dos saldos e alinhamento das configurações.**

**Saiba Mais**

[*Clique aqui e veja mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)

[*MP - SIGAEST - Como desabilitar o Controle de Rastreabilidade (Lote - Sub-lote) no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011959471)

[*MP - SIGAEST - Como ativar o controle de Lote/Rastro para produtos com saldo?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020672612)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
