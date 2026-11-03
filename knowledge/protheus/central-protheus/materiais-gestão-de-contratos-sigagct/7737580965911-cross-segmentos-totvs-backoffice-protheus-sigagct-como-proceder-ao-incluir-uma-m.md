---
article_id: 7737580965911
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 81bd11f53cfec58f2a36400f8100804d29fb0f1d7bfb15e43e401928bd30409a
fetched_at: '2026-06-28T22:37:20.250543+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT  - Como proceder ao incluir
  uma medição que não carrega todos os itens do contrato?
type: support-article
updated_at: '2026-06-19T12:28:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7737580965911-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-proceder-ao-incluir-uma-medi%C3%A7%C3%A3o-que-n%C3%A3o-carrega-todos-os-itens-do-contrato
---

O artigo orienta que, ao incluir uma medição que não carrega todos os itens do contrato no TOTVS Gestão de Contratos, deve-se verificar se os tamanhos dos campos de descrição (CNE\_DESCRI, B1\_DESCR, CNB\_DESCRI) estão compatíveis no dicionário e banco de dados. Outra causa é a falta de saldo para medição no item (CNB\_QTDMED igual a CNB\_QUANT, ficando CNB\_SLDMED com zero), exigindo revisão do contrato para incluir saldo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37218727401239) Tempo aproximado para leitura: 02**min**  
  
**Dúvida**  
Como proceder ao incluir uma medição que não carrega todos os itens do contrato?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução:**

1 - Uma das possibilidades ocorre quando existe divergência do tamanho de campos onde são gatilhadas as informações da planilha, na qual  possivelmente o tamanho do campo de Descrição do Item da Medição (**CNE\_DESCRI**) está com um tamanho menor que os campos de Descrição dos processo anteriores como o **B1\_DESCR (Cadastro de Produto)**e **CNB\_DESCRI (Item da Planilha no Cadastro do Contrato)**por exemplo.  
  
Dessa forma, orienta-se a verificação dos tamanhos dos campos de Descrição do Produto das tabelas SB1, CNB e também CNE e ajustando-os (principalmente o campo da CNE) no ambiente **(no Dicionário e Banco de Dados)** para estarem todos com o mesmo tamanho (o tamanho maior utilizado entre os campos).  
  
***Obs:***  
Deve-se analisar na base de dados os tamanhos de campos ***tanto no Dicionário de Dados como também no Banco de Dados***, os quais devem estar compatíveis.

2 - Outra possibilidade de um item da planilha não ser trazido ao se realizar uma medição é este item não possuir mais saldo de quantidade para ser medida.

No caso, para ser medido, no item, o valor do campo CNB\_QTDMED (Quantidade Medida) precisa estar menor que o CNB\_QUANT (Quantidade), e assim ficando o CNB\_SLDMED (Saldo para ser Medido) com alguma quantidade a ser medida.

Não estando desta forma acima, por padrão, a rotina de medição não exibe este item da planilha sem saldo quando ela é selecionada, e caso se deseje medir o item, se faz necessário a realização de revisão do contrato para inclusão de novo item com saldo na planilha.

***Saiba Mais:***

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
