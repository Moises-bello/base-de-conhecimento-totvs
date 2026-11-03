---
article_id: 38693892159767
category: TOTVS Backoffice (Linha Protheus)
content_hash: 0676ab3a84ee73b735a48fe54705b5d95a09aa2d02e638b3ff42ffe35625da11
fetched_at: '2026-06-28T22:36:19.668764+00:00'
product: protheus
section_id: 1500001529881
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - MATA030- A1_ATR não
  atualiza
type: support-article
updated_at: '2026-03-02T12:28:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38693892159767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-MATA030-A1-ATR-n%C3%A3o-atualiza
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38693899528727) Tempo aproximado para leitura: **10:00 min**  
  
**Dúvida**  
Campo A1\_ATR permanece zerado no cadastro de Clientes, no entanto constam titulos em atraso e a rotina FINA410 (Refaz Dados Cli/For), foi executada e  não atualizou.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - 2410  
  
**Solução**  
O campo **A1\_ATR** é atualizado ao executar o processamento da rotina **FINA410**.   
  
Se o campo **A1\_MOEDALC** estiver preenchido com **0 (zero)** ou vazio, o sistema não identifica a base monetária para o cálculo, resultando em um saldo final zerado, independentemente da existência de títulos em aberto.  
  
O campo **A1\_MOEDALC**  - Moeda do controle de credito define a moeda para base e limite de credito do cliente.

### **Passos**

Para corrigir o comportamento:

1. Acesse o módulo **Financeiro (SIGAFIN)**;

   1. Vá em **Atualizações > Cadastros > Clientes (MATA030)**;
2. Selecione o cliente em questão e clique em **Alterar**;
3. Localize o campo **Moeda do LC (A1\_MOEDALC)**;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38693892147991)
4. Informe o código da moeda correspondente à operação do cliente (Exemplo: **1** para Moeda Corrente/Real);
5. **Confirme** a alteração do cadastro;
6. Acesse **Miscelânea > Acertos > Execute a rotina >  Refaz Dados Cliente/Fornecedor (FINA410)**;
7. Parametrize a rotina para processar o cliente específico e execute o reprocessamento;
8. Verifique novamente o cadastro do cliente; o campo **A1\_ATR** deverá exibir o valor atualizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38736178034455)

**Saiba Mais:**  
  
[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Composição dos Campos de saldo e vendas na tabela SA1 (MATA030)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000676288-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Composi%C3%A7%C3%A3o-dos-Campos-de-saldo-e-vendas-na-tabela-SA1-MATA030)  
[Cross Segmento - Backoffice Linha Protheus - FINA410 - Como recalcular saldo cliente e fornecedor?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37559494551319-Cross-Segmento-Backoffice-Linha-Protheus-FINA410-Como-recalcular-saldo-cliente-e-fornecedor)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINC010 - Consulta Posição de título a receber](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041295493-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINC010-Consulta-Posi%C3%A7%C3%A3o-de-t%C3%ADtulo-a-receber)
