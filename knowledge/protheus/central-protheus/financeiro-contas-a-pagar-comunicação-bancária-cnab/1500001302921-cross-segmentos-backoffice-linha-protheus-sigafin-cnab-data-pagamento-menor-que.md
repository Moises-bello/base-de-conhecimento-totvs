---
article_id: 1500001302921
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 11b333b2a9596269634cb7eecb335186aba8713810c5dc95e7859babd3c6d66e
fetched_at: '2026-06-28T22:37:55.334265+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Data pagamento
  menor que emissão
type: support-article
updated_at: '2022-06-24T00:50:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001302921-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Data-pagamento-menor-que-emiss%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00min**

**Dúvida**Ao efetuar o retorno do CNAB nas rotinas Retorno de Cobranças (FINA200), Retorno de Pagamentos (FINA430), ou  SISPAG (FINA300) retorna a mensagem "Data do pagamento não pode ser menor que a data de emissão do título correspondente", ao emitir os relatórios de CNAB FINR650 ou FINR850, como podemos corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões

**Causa**   
Esse incidente ocorre, pois a parametrização do sistema está incorreta para o Formato da data que é usado pelo sistema no retorno.   
  
**Solução**Abra os **Parâmetros de Banco (FINA130)** em **Atualizações** -> **Cadastros** -> **Parâmetros de Bancos**. No campo **Formato da Data**, altere para tipo de data 4 que é ddmmaaaa.  
  
**Exemplo da tela do Parâmetros de Banco**

![par_metros_de_Banco.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102378273/par_metros_de_Banco.png)

**Exemplo**Caso o Formata da data esteja como 1 (ddmmaa) e a data do retorno seja seja 04/01/2021 irá usar só 04/01/20 e dará a mensagem. Mudando para 4 (ddmmaaaa) ficará correto.
