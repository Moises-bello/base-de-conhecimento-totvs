---
article_id: 29009366772631
category: SIGAEST - MOVIMENTAÇÕES
content_hash: cf3aa08e5343c7ae0a295d714d83c19a49d4ebffd5078c315b272378b45bddff
fetched_at: '2026-06-28T22:38:53.903852+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Campo D1_LOTECTL para
  produtos com controle de Rastro é possível tornar a digitação obrigatória?
type: support-article
updated_at: '2025-03-12T12:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29009366772631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campo-D1-LOTECTL-para-produtos-com-controle-de-Rastro-%C3%A9-poss%C3%ADvel-tornar-a-digita%C3%A7%C3%A3o-obrigat%C3%B3ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29009342729623) Tempo aproximado para leitura: **00:03:25 min** **Dúvida**

Ao incluir um Documento de Entrada é possível obrigar a digitação do Lote (D1\_LOTECTL) para que ***não gere*** registro de Lote Automático?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Atualmente, no Protheus padrão ao incluir um Documento de Entrada para produtos que controlam Rastreabilidade (B1\_RASTRO=L/S), caso o usuário não informar um Número de Lote é gerado um registro automático.

É possível alterar esse comportamento customizando com o apoio de seu Analista Desenvolvedor com os pontos de entrada [**MTA103OK**](https://tdn.totvs.com/x/buRc%C2%A0) e [**MT100LOK**](https://tdn.totvs.com/x/Fdtc%C2%A0) conforme sua necessidade específica. Segue abaixo link dos Ponto de entrada

**MTA103OK - Altera o resultado da validação padrão para inclusão/alteração de registros de entrada, por customizações do cliente**  
***<https://tdn.totvs.com/x/buRc>***

**MT100LOK - Alterações de Itens da NF de Despesas de Importação**  
[***https://tdn.totvs.com/x/Fdtc***](https://tdn.totvs.com/x/Fdtc)  
  
**Veja também:**  
**MT100TOK - Valida a inclusão de NF**  
[***https://tdn.totvs.com/x/GNtc***](https://tdn.totvs.com/x/GNtc)

Saiba Mais:

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[Campos D1\_LOTEFOR (Lote Fornecedor) e D1\_LOTECTL (Lote) do Documento de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8836419922455-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Campos-D1-LOTEFOR-Lote-Fornecedor-e-D1-LOTECTL-Lote-do-Documento-de-Entrada)

[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus?source=search)
