---
article_id: 360021667552
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: d60861a377e999f89f1b9b025197c461f824886b7535d9eaf402380c07560c7b
fetched_at: '2026-06-28T22:37:55.272939+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  CNAB - Configuração
  Multicontas Correntes
type: support-article
updated_at: '2022-06-24T00:46:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021667552-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Configura%C3%A7%C3%A3o-Multicontas-Correntes
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00min**

**Dúvida**Como configurar as Multicontas Correntes?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões  
  
**Solução**O **modelo 2**(240 posições) permite configurar para processar o arquivo de retorno com lotes de pagamentos em diferentes contas bancárias.  
Essa configuração faz com que os dados de banco, agência e conta passe a ser verificado no *Header* do Lote ao invés dos parâmetros (F12) da rotina de Retorno **CNAB a Pagar** (FINA430).

Exemplo 1:

1- *Header* de Lote conta: 0001-000001

2- Detalhe(s) do Lote;

3- *Trailler* de Lote;

Exemplo 2:

1- *Header* de Lote conta: 0001-000002

2- Detalhe(s) do Lote;

3- *Trailler* do Lote;

Para tratamento no retorno **CNAB** considera as contas correntes do *Header* do Lote é necessário configurar *Header* do Lote com as variáveis conforme imagem abaixo:  
  
![multicontas.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360018635811/multicontas.PNG)  
  
**Importante:**

Caso as contas correntes tenham sido cadastradas utilizando caracteres especiais (hifens, pontos etc...), será necessário adequar a informação retornada pelo banco ao código da conta corrente cadastrada no **cadastro Banco** (SA6.)
