---
article_id: 360044884633
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ae7315c0cd8190bb00ea4336ccd3b918cd963c2485dd61cc52d85c9ce4260c1c
fetched_at: '2026-06-28T22:42:43.507456+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Leitura de saldo disponível dos produtos
  alternativos
type: support-article
updated_at: '2021-05-27T10:55:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044884633-Manufatura-Linha-Protheus-SIGAPCP-Leitura-de-saldo-dispon%C3%ADvel-dos-produtos-alternativos
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:05 min**  
**Dúvida**Quando um produto possui alternativos, como é feita a leitura do **saldo disponível dos alternativos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Para determinar os armazéns que serão considerados, o Sistema avalia o conteúdo do parâmetro **MV\_ARMALTE**, se o conteúdo desse parâmetro for **2**, o Sistema fará a leitura dos armazéns cadastrados na tabela **NNR** , avaliando o conteúdo do campo **NNR\_ARMALT** e se este campo possuir o conteúdo igual a **1** o saldo disponível será considerado.  
Se o parâmetro **MV\_ARMALTE** possui o conteúdo **1**, somente o armazém padrão, definido no campo **B1\_LOCPAD** ou o armazém de apropriação indireta, informado no parâmetro **MV\_LOCPROC** para os casos dos produtos de apropriação indireta, serão considerados.   
Desses armazéns, o Sistema avaliará o saldo disponível conforme o conteúdo do parâmetro **MV\_TPSALDO** e a este valor será somado o conteúdo do campo **B2\_SALPEDI** e subtraído o conteúdo do campo **B2\_QEMPN**.  
  
**Importante**  
Para que o Sistema avalie a disponibilidade do produto alternativo, é necessário que o parâmetro **MV\_CONSEST** tenha o conteúdo **S**.  
  
**Saiba mais**  
Para saber qual o critério utilizado para o empenho de produto alternativo acesse a documentação: [Manufatura - Linha Protheus - SIGAPCP - Qual o critério para empenhar o produto alternativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024982271-MP-SIGAPCP-Qual-o-crit%C3%A9rio-para-empenhar-o-produto-alternativo)  
E para saber como cadastrar um produto alternativo acesse a documentação: [Manufatura - Linha Protheus - SIGAPCP - Como cadastrar um produto alternativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024680772-MP-SIGAPCP-Como-cadastrar-um-produto-alternativo)  
  
**Glossário**  
**NNR** - Locais de Estoque  
**B2\_QEMPN** - Qtd. Emp. NF  
**B1\_LOCPAD** - Armazem Pad. **B2\_SALPEDI** - Qtd.Prevista   
**NNR\_ARMALT** - Ver Sld Alt  
**MV\_TPSALDO** - Tipo de Saldo a ser considerado nos movimentos internos: (S) Utiliza a função SaldoSB2() (Q) Utiliza o valor **B2\_QATU-B2\_QACLASS-B2\_RESERVA**  
**MV\_CONSEST** - Considera Estoque na Geração de Ordem de Produção? **MV\_LOCPROC** - Local padrão a ser enviado os materiais indiretos em processo.    
**MV\_ARMALTE** - Considera o saldo dos produtos alternativos em todos os armazéns durante a criação das ordens de produção. 1=Não ;2=Sim
