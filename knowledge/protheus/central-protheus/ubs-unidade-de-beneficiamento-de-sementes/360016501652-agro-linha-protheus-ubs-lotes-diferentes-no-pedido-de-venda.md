---
article_id: 360016501652
category: UBS - Unidade de Beneficiamento de Sementes
content_hash: c32cd84e76bf8fcbcd2b9fe3fae8f4d44324b2ee43f9985a2e2e2b3910219736
fetched_at: '2026-06-28T22:45:34.815147+00:00'
product: protheus
section_id: 360005696194
source: central-protheus
title: Agro - Linha Protheus - UBS - Lotes Diferentes no Pedido de Venda
type: support-article
updated_at: '2025-06-20T15:03:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016501652-Agro-Linha-Protheus-UBS-Lotes-Diferentes-no-Pedido-de-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22274325511447) Tempo aproximado para leitura: **00:00:50 min****Dúvida**Foi efetuada uma **Ordem de Carregamento**, e nela foram informados dois lotes, mas quando foi gerado o **Pedido de Venda** e a nota, saíram lotes diferentes. Como proceder?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBS - Unidade de Beneficiamento de Sementes - A partir da versão 12.1.17  
  
**Solução**O problema ocorre em decorrência do campo **C6\_RESERVA**, que no dicionário de dados está como **Não Usado**, e então no momento de gerar o **Pedido de Venda** não há **Reserva** para tal, e o Sistema se perde.  
Para corrigir a situação é necessário efetuar o seguinte procedimento, respeitando a sequência dos passos abaixo:

**1.** Ative a via **SIGACFG - Configurador**, o campo **C6\_RESERVA** para **usado** e marcar para que ele seja utilizado por todos os módulos;

**2.** Exclua os **Pedidos de Venda** no programa **MATA410** e as notas geradas erroneamente no programa  **MATA460A**  por meio das rotinas do módulo de **Faturamento**;

**3.** Acesse as **Ordens de Carregamento** e excluir os itens delas;

**4.** Acesse a rotina de **Controle de Reservas** no programa **MATA430** e excluir as reservas geradas - as que estão com o *status* **Reserva não Baixada**;

**5.** Acesse novamente a **Ordem de Carregamento** e incluir os itens excluídos anteriormente. Em seguida gerar novamente o **Pedido de Venda**.
