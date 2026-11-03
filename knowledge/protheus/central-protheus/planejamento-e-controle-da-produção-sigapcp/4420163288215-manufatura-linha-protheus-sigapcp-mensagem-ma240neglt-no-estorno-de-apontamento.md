---
article_id: 4420163288215
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a87d91a54bdabab8686a6bdd578c21b3b1c19dc6e936b20eeef89b74ad08e491
fetched_at: '2026-06-28T22:42:44.494060+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MA240NEGLT no estorno de apontamento
type: support-article
updated_at: '2022-01-27T11:35:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420163288215-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MA240NEGLT-no-estorno-de-apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Ao tentar estornar um apontamento ocorre a mensagem **MA240NEGLT - Não existe saldo por lote suficiente**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem é apresentada no estorno quando o item produzido não possui mais saldo disponível para o lote e armazém no qual está o apontamento, ou se neste apontamento há uma outra entrada no estoque via subproduto, para o qual o saldo não está mais disponível no lote e armazém no qual ocorreu a entrada.  
  
**Solução**  
1. Para solucionar essa ocorrência, através do relatório **MATR860 - Detalhamento da Ordem de produção**, verifique todos os registos que contém **Tipo RE/DE** com **PR0** ou **DE1** do apontamento que deseja estornar;  
2. Para estes itens, através do **MATR435 - Kardex por Lote/Sub Lote** verifique se o lote e quantidade ainda encontra-se disponível no armazém no qual o apontamento deu entrada;  
3. Ao identificar qual produto, lote e quantidade não encontra-se mais disponível, analise a possibilidade de estornar o movimento que retirou essa quantidade do armazém no qual ocorreu o apontamento.
