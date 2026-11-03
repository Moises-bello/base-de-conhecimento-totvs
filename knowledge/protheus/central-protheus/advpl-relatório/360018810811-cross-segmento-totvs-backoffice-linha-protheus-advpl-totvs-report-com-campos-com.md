---
article_id: 360018810811
category: ADVPL - Relatório
content_hash: 7c5d07f351c9f7889e74eed11a4f3b5a35f394f9bd672622bf310b867243e71d
fetched_at: '2026-06-28T22:40:22.920808+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Totvs report com
  campos complexos
type: support-article
updated_at: '2021-12-30T19:00:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018810811-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Totvs-report-com-campos-complexos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:10:00 min  
  
Dúvida**Como inserir um excerto de código ADVPL (*Advanced Protheus Language*) no TOTVS Report?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.8  
 **Solução**Criar uma função de usuário que retorne o valor desejado.  
  
**Exemplo**Temos um relatório de pedidos de venda sintético (resumo de valores por pedido) e outro analítico (exibição de valor por item, e itens por pedido).  
  
Em nosso relatório sintético, não temos a necessidade de utilizar de itens (SC6), apenas a tabela (SC5), porém os valores dos itens do pedido estão contidos na SC6, assim sendo, é necessário acumular os valores por número de pedido (C6\_NUM).

1. Crie um campo do tipo Fórmula:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014287991/mceclip0.png)
2. Crie a e compile função de usuário informada, recebendo no cabeçalho o número do pedido:

   ```
   // BIBLIOTECA NECESSÁRIA  
   #Include "TOTVS.ch"  
     
   // FUNÇÃO: RETORNA VALORES DO PEDIDO DE COMPRA  
   User Function RetValPC(cNumPed) // RECEBE O NÚMERO DO PEDIDO CORRENTE  
       Local nTotal :=0                // VALOR TOTAL POR PEDIDO DE COMPRA  
       Local aArea := SC6->(GetArea()) // ARMAZENA A ÁREA PARA RESTAURAR APÓS OPERAÇÕES  
     
       SC6->(DbGoTop())                          // MOVE O CURSOR PARA O TOPO DA TABELA  
       SC6->(DbSetOrder(1))                      // ALTERA PARA O ÍNDICE 1: C6_FILIAL + C6_NUM + (...)  
       SC6->(MsSeek(FwXFilial("SC6") + cNumPed)) // USA O NÚMERO DO PEDIDO PARA PESQUISAR  
     
       // ENTÃO O NÚMERO DO PEDIDO FOR IGUAL AO NÚMERO CORRENTE NA  
       // TABELA SC6, ADICIONE O VALOR TOTAL DO ITEM A VARIAVEL NTOTAL  
       While (SC6->C6_NUM == cNumPed)  
           nTotal += SC6->C6_VALOR  
           SC6->(DbSkip())  
       End  
     
       // RESTAURA A ÁREA ORIGINAL (EVITA ERROS DE POSICIONAMENTO)  
       RestArea(aArea)  
   Return (nTotal) // RETORNA O VALOR PARA A COLUNA
   ```
3. Adicione uma função de usuário que receba o campo de número do pedido (C6\_NUM):  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014285232/mceclip0.png)
4. Impressão de relatório sintético:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014287532/mceclip1.png)
5. Impressão de relatório analítico:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014287672/mceclip2.png)  
    **Saiba mais**  
   [Configurando Relatórios Personalizáveis](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/padrao_de_operacao_configuracao_relatorio_personalizado.htm)
