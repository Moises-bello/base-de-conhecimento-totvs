---
article_id: 13257607839511
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f8398557bf9bf22b2a7e375ee76832758555ceab6b982cc91dd21e0c6ee54033
fetched_at: '2026-06-28T22:38:42.759855+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Movimentação
  da tabela "SD3 - Movimentações Internas" no faturamento
type: support-article
updated_at: '2023-03-21T18:42:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13257607839511-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Movimenta%C3%A7%C3%A3o-da-tabela-SD3-Movimenta%C3%A7%C3%B5es-Internas-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como movimentar a tabela SD3 nos processos do faturamento?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**Há duas maneiras de movimentar a tabela SD3 no faturamento.

* Maneira A: [**P****rocesso de transferência de armazém**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020343832-MP-SIGAEST-Funcionalidade-dos-par%C3%A2metros-MV-CONTERC-e-MV-ALMTERC-para-controle-do-poder-EM-terceiros) (ao faturar o pedido com as devidas configurações). Para controle de estoques que possuem poder de/em terceiros que saem da empresa (podendo voltar em algum momento ou não): [**Processo de transferência de armazém**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020343832-MP-SIGAEST-Funcionalidade-dos-par%C3%A2metros-MV-CONTERC-e-MV-ALMTERC-para-controle-do-poder-EM-terceiros)

**Dúvidas nesse processo orientamos que entre em contato com a Equipe Protheus Estoque.**

* Maneira B: Liberação completa de um pedido de venda para análise, que não tem saldo no estoque colocado no pedido de venda.

**Premissas:**

1 - Ter o campo C9\_SD3SEQ criado. Seja [manualmente](https://tdn.totvs.com/x/cwXLHg) ou por [atualização de dicionário via backup](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/FAT_expedicao_continua) das últimas expedições contínuas.

2 - Ter Produtos [MATA010] (sem controle de lote/endereço)

3 - Nesse produto, ter saldo inicial em dois armazéns, por exemplo:  
Armazém 01: B2\_QATU = 5 (com saldo)   e   Armazém 02: B2\_QATU = 0 (sem saldo)

4 - No pedido de venda [MATA410], deixar os campos:  
"Tipo de liberação (C5\_TIPLIB)" = 1 (Por item)  
"Quantidade (C6\_QTDVEN) = 10" (5 a mais do que tem juntando os dois armazéns)  
"Armazém (C6\_LOCAL)" = 02 (Colocar armazém sem saldo para que haja a transferência)

5 - Na rotina de liberação do pedido de vendas [MATA440], apertar F12 e configurar os perguntes todos como "Sim":  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13257562634135)

6 - Na rotina de liberação do pedido de vendas [MATA440], liberar o pedido.

**A liberação será feita com os itens que possuírem saldo no estoque.**

**Neste momento, será feita a transferência (SD3):**

1. Tabela SD3: "RE4"/"DE4" do armazém "01" para o "02"
2. Nas rotinas [MATA410/MATA460A], faturar o pedido parcialmente com quantidade "5"
3. Há a liberação do pedido com o item não faturado (Há "5" de quantidade pendente na SC9)

**OBSERVAÇÃO:** Estorne a liberação do pedido de venda (Ajustar quantidade pendente na SC9)

O sistema considera o item do pedido e sua sequência de liberação, no momento do **estorno da liberação do Pedido de Venda****.**

No momento da transferência da **SD3**, o campo **C9\_SD3SEQ** é alimentado com o campo **D3\_NUMSEQ.**

No momento da transferência da **SD3**, o campo **D3\_DOC** é alimentado com o **C5\_NUM.**

**Saiba mais:**

[Criação do campo Seq. SD3 (C9\_SD3SEQ) na rotina de Pedidos Liberados](https://tdn.totvs.com/x/cwXLHg)
