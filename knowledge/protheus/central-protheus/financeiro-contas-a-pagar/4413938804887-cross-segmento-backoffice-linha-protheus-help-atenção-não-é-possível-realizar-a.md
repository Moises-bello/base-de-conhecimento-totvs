---
article_id: 4413938804887
category: Financeiro - Contas a Pagar
content_hash: 9dea5f68687c102fd9d7c4cb8b59d81ef4d1ad6ce6b8e2597bfba00228847e03
fetched_at: '2026-06-28T22:38:06.882379+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -  HELP  ATENÇÃO Não é possível
  realizar a baixa de uma pagamento antecipado sem movimentação. '
type: support-article
updated_at: '2023-07-04T01:44:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413938804887-Cross-Segmento-Backoffice-Linha-Protheus-HELP-ATEN%C3%87%C3%83O-N%C3%A3o-%C3%A9-poss%C3%ADvel-realizar-a-baixa-de-uma-pagamento-antecipado-sem-movimenta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05min****Dúvida**Ao tentar compensar um título do tipo PA é apresentado **HELP** **ATENÇÃO** Não é possível realizar a baixa de uma pagamento antecipado sem movimentação. Verifique se os motivos de baixas padrão estão disponíveis **FINA490**.  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Corrija os **PA's** (Pagamento Antecipado) que não aparecem na relação dos **títulos** a serem **compensados** com a mensagem  **HELP** **ATENÇÃO** Não é possível realizar a baixa de uma pagamento antecipado sem movimentação. Verifique se os motivos de baixas padrão estão disponíveis **FINA490**, realize os seguintes passos:  
  
1. Acesse a rotina **FINA090** (Baixas Automáticas) e clique no botão **+AUTOMATICA**.   
2. Marque a opção **TITUTOS**= preencha os dados necessários como **Vencimentos**, **Banco** e **motivo de Baixa**.   
3. Quando a seleção de **títulos** apresentar, selecione o **PA** com erro e peça para **baixar**.  
4. Neste momento o sistema **NÃO** irá baixar o **PA** de fato, apenas irá movimentar a tabela **SE5** para que o **PA** fique disponível para a **compensação** com outros **títulos.**
