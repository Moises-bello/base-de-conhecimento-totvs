---
article_id: 27489251539223
category: Financeiro - Movimentação Bancária
content_hash: abbb9f87fa0b39efd1f2cc9d3a698cb17acc3e53b0d8863bd42102b8275a96af
fetched_at: '2026-06-28T22:38:19.471604+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Qual é o
  procedimento para alimentar a tabela SIG que utiliza o extrato bancário
type: support-article
updated_at: '2025-12-18T13:09:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27489251539223-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Qual-%C3%A9-o-procedimento-para-alimentar-a-tabela-SIG-que-utiliza-o-extrato-banc%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27489251520151) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**  
Qual é o procedimento para alimentar a tabela **SIG**, utilizada como base do **extrato bancário**? Poderia explicar o processo e apresentar um exemplo prático de como realizar?

**Ambiente:**

Cross Segmento – TOTVS Backoffice (Linha Protheus) – Financeiro - a partir da release **12.1.2210**  
  
  
**Solução**  
A tabela SIG é alimentada por meio da rotina de Manutenção de Extratos Bancários, que permite a importação manual do arquivo de extrato bancário (retorno bancário) para utilização nos processos de conciliação, especialmente no processo 0023 (Conciliação Automática).

#### 

#### Processo para importação manual do extrato bancário:

1. Acesse o menu:  
   **Atualizações → Movimentos Bancários (FINA474) → Manutenção de Extratos Bancários**
2. Selecione a **conta bancária**, **banco**, **agência** e **conta** correspondentes ao extrato;
3. Utilize a opção de **Importação** para carregar o arquivo de extrato bancário fornecido pela instituição financeira (ex.: CNAB de extrato);
4. Após a importação, o sistema:

   * Grava os lançamentos do extrato na **tabela SIG**;
   * Disponibiliza esses dados para uso no **Conciliador Backoffice**.

#### Exemplo prático de uso no conciliador:

* O extrato bancário é importado pela Manutenção de Extratos Bancários;
* Os movimentos passam a existir na **SIG**;
* No Conciliador:

  + O **processo 0023** utiliza os dados da **SIG** como base;
  + Esses dados são comparados com as movimentações da **FK5** (movimentos bancários gerados pelo financeiro);
  + Ao encontrar correspondência, o sistema efetiva a conciliação

#### 

#### Observação importante

* Sem a importação do extrato bancário, a tabela **SIG não será populada**;
* Nesse cenário, a conciliação automática (0023) **não funcionará**, sendo necessário utilizar o **processo 0024**, que tem como base a **FK5**.

Com isso, apenas serão demonstrados a visualização da SIG utilizando o processo 0023, conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37116320854295)

A exibição da SIG no setup 0024, não demonstra os dados da SIG a partir do backoffice de Março de 2025.

**Saiba Mais**  
[FINA474 - Manutenção de Extratos Bancários](https://tdn.totvs.com/pages/viewpage.action?pageId=721003882)  
[Cross Segmento - Backoffice linha Protheus - SIGAFIN - CTBA940- Novo Conciliador Bancário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22896337613463)
