---
article_id: 10959656894487
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1af434fb0503a59c1f01c80accb1dec9223ea3f3796558099de541547de5d8b2
fetched_at: '2026-06-28T22:38:42.618269+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Depuração automática do controle de reservas
type: support-article
updated_at: '2022-12-14T18:42:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10959656894487-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Depura%C3%A7%C3%A3o-autom%C3%A1tica-do-controle-de-reservas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o comportamento e configuração da funcionalidade de depuração automática de reservas no Faturamento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.  
  
  
**Solução**

No faturamento temos a Depuração Automática, na qual o sistema detecta as reservas vencidas (C0\_VALIDA) da rotina [Controle de Reservas - MATA430] e as exclui, atualizando também as reservas (B2\_RESERVA).

**Parâmetros e processos utilizados na opção de depurar:**

* **MV\_RESERVA == T:** Depura automaticamente as reservas vencidas ao entrar em módulos que usam o controle de reservas, atualizando o ***B2\_RESERVA***.
* **MV\_PZRESER:** Prazo fixo configurado da validade da reserva a partir do campo C0\_EMISSAO.  
  (Validade da Reserva) C0\_VALIDA == C0\_EMISSAO (Emissão da Reserva) + MV\_PZRESER (Dias do Parâmetro)
* **MV\_ULRESER:** É gravado com a última depuração automática da reserva.
* **MV\_DELRES:**

  **T** - Na exclusão do Pedido de Vendas o Sistema excluirá a reserva. Na alteração do pedido de Vendas o Sistema limpará o campo Num.Reservae excluirá a reserva.  
  **F** - Na exclusão do Pedido de Vendas o Sistema não excluirá a reserva, apenas alterará o status para não baixada. Na alteração do Pedido de Vendas o Sistema manterá a reserva no pedido.

    
  1. Esse comportamento não se aplica quando o parâmetro **MV\_RESAUT** estiver ativo.  
   2. O estorno deverá ser feito através da rotina de Prep. Documento de Saída (MATA460A), através da opção "Estor. Docs.". (.T. - Exclui / .F. - Não exclui, apenas deixa a reserva como não baixada)

**Saiba mais:**

[FAT0131 Rotina Controle de Reservas (MATA430)](https://tdn.totvs.com/x/P5AjDw)
