---
article_id: 9162967709463
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 554178598bcdf804efcfd7440d105b32088e36d6df81818cc0572d03f5895e7a
fetched_at: '2026-06-28T22:42:43.516031+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Limpar campo C6_OP com valor 05
type: support-article
updated_at: '2022-09-27T13:44:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9162967709463-Manufatura-Linha-Protheus-SIGAPCP-Limpar-campo-C6-OP-com-valor-05
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:49 min****Dúvida**Como limpar o campo **C6\_OP** quando está com o valor igual a **05** para que seja possível gerar uma no **OP**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Ao gerar uma **OP** **por vendas** através da rotina **MATA650** quando já possui o saldo suficiente em determinado armazém para atender o pedido, a ordem de produção não é gerada e o campo **C6\_OP** é preenchido com o valor **05**.  
Para que essa informação seja limpa e possa tentar gerar novamente a **OP** utilizando o **Pedido de Venda**, é necessário que os parâmetros estão configurados como:  
**Considerar Armazém Padrão? Não**  
**Cons. Saldos de Armazéns? Não  
MV\_PVCOMOP = T  
  
Importante**Sugerimos a ativação do parâmetro **MV\_PVCOMOP** para que num eventual estorno de **OP** o Sistema consiga fazer os ajustes pertinentes na tabela **SC6**, como limpar o conteúdo do campo **C6\_OP**. **Saiba mais**Para mais informações sobre o campo **C6\_OP** acesse a documentação: [MP-FAT-Quais conteúdos o campo C6\_OP pode ter](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013175268-MP-FAT-Quais-conte%C3%BAdos-o-campo-C6-OP-pode-ter)  
E para mais informações sore o parâmetro **MV\_PVCOMOP** acesse a documentação: [Manufatura - Linha Protheus - SIGAPCP - Tabela SGJ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025813734-Manufatura-Linha-Protheus-SIGAPCP-Tabela-SGJ)  
  
**Glossário**  
**OP** - Ordem de Produção  
**SC6** - Itens dos Pedidos de Venda  
**C6\_OP** - **OP** Gerada  
**MATA650** - Ordens de Produção  
**MV\_PVCOMOP** - Ativa a gravação na tabela **SGJ** - Amarração Pedido de Venda x Ordem de Produção.
