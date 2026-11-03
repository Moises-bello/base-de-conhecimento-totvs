---
article_id: 360020313191
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 384b094785ea7fbf95e932adee611b310f00b1f9f5caad565137d1aa8f59bfea
fetched_at: '2026-06-28T22:38:29.859876+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Operação Triangular no faturamento
  (SIGAFAT)
type: support-article
updated_at: '2026-03-24T11:40:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020313191-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Opera%C3%A7%C3%A3o-Triangular-no-faturamento-SIGAFAT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29321856295063) Tempo aproximado para leitura: 00:03:30 min**

**Dúvida**  
Qual o conceito de utilização para Operação Triangular?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
A Operação Triangular consiste em uma transação que envolve mais de 2 empresas para um processo de beneficiamento.

![Triangular.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360016053792)

Uma empresa **A** envia um material à empresa **B** para beneficiamento e esta envia à empresa **C**, que deverá efetuar o trabalho e devolver o material diretamente à empresa **A**.

1 - Faça uma entrada de documentos (rotina **MATA103**) com o fornecedor "**A**" do tipo (**C103TIPO**) "**N - Normal**" ou "**B - Beneficiamento**".

***Importante:**A TES de Entrada precisa estar com o campo '**Poder Terc. (F4\_PODER3)**' como '**R - Remessa**'*

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/29321856302359)*

2 - Entre na rotina de pedidos de venda (**MATA410**) e aperte a tecla F12.  
   
3 - Vá na opção "Operação Triangular" e habilite igual a "Sim":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22557761670935)  
 

4 - Entre no pedido de vendas, configure o tipo do pedido de venda (**C5\_TIPO**) como tipo "**N - Normal**" ou "**B - Utiliza Fornecedor**", selecione o fornecedor "**C"** (E não o "**A**" que está na entrada do passo 1) e tente localizar a nota como qualquer movimentação de terceiros no campo "**Quantidade (C6\_QTDVEN**)" apertando a tecla F4 no campo.

**A nota aparecerá. Assim, pode devolver agora à qualquer fornecedor e não apenas ao fornecedor que efetivou a entrada!**

***Importante:** A TES de Saída precisa estar com o campo '**Poder Terc. (F4\_PODER3)**' como '**D - Devolução**'*

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/29321903752471)*

**OBSERVAÇÃO:**  
No módulo de faturamento não há um processo específico de venda a ordem, este processo deve ser realizado em  notas distintas e não existe uma forma automatizada  no sistema:

[**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Venda Ordem (Venda de mercadoria adquirida, Remessa Simbólica e Remessa por conta e ordem de terceiros)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405005140887)

Caso não atenda, valide se uma consignação não se encaixaria dentro desse tipo de venda, cheque no Saiba mais baixo a documentação completa do Poder DE/EM Terceiro.

**Saiba Mais:**  
[**Conceito de utilização para Operação Triangular**](http://tdn.totvs.com/pages/releaseview.action?pageId=238038517)

[**FAT0285 - Poder DE/EM Terceiro**](https://tdn.totvs.com/x/xyCgGg)
