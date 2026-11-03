---
article_id: 36811351465495
category: Financeiro - Contas a Receber
content_hash: 9a62d63f394ac827a661cad846b8917ce376612600215e37cee743279d631e8c
fetched_at: '2026-06-28T22:38:13.868652+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - FINA040/FINA050
  - Tabelas e Histórico do título
type: support-article
updated_at: '2025-12-11T14:14:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36811351465495-Cross-Segmentos-Backoffice-Linha-Protheus-Financeiro-FINA040-FINA050-Tabelas-e-Hist%C3%B3rico-do-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36811351452695) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Através da rotina histórico de título da FINA040/FINA050 é possível trazer histórico do título?

**Solução**

O financeiro é estruturado em duas principais divisões: **Contas a Receber** e **Contas a Pagar**.

Os títulos de recebimento (Contas a Receber) são gerados pelas rotinas **FINA040/FINA740** e registrados na tabela **SE1**.  
Já os títulos de pagamento (Contas a Pagar) são provenientes das rotinas **FINA050/FINA750** e registrados na tabela **SE2**.

Vale reforçar que, a partir dessas rotinas, todas as ações realizadas — como baixas, contabilizações e demais movimentações — passam a alimentar novas tabelas do sistema, dependendo exclusivamente do processo executado.

**A rotina histórico do título é baseada na tabela CV8.**  
   
Esta tabela é utilizada pelo sistema para armazenar informações detalhadas sobre a execução de rotinas e processos específicos dentro do Protheus. Ela serve como um **histórico de logs** de atividades.  
   
**Ou seja, os campos não serão os mesmos da SE1/SE2,  não trazendo as mesmas informações. Tratam-se de processos diferentes.**  
   
A tabela **CV8** armazena dados essenciais para o **rastreamento** e a **análise** do andamento de rotinas, sendo frequentemente solicitada em casos de lentidão ou erros de processamento.  
   
Os principais campos da CV8 registram informações como:

**CV8\_PROC**: Identifica a **Rotina** ou **Processo** que gerou o log.

**CV8\_USER**: Identifica o **Usuário** responsável pela execução do processo.

**CV8\_DATA** e **CV8\_HORA**: Registram a **Data** e **Hora** da ocorrência do log. (Ou seja: a data e hora real, que consta em seu computador. Não é focado apenas na database do sistema).

**CV8\_MSG**: Contém a **Mensagem** ou descrição do evento registrado. (Essas mensagens são padrões do sistema, pré definidas).

**CV8\_INFO**: Indica o **Tipo de Ocorrência** no Log (Ex: 1 = Início do Processamento, 4 = Erro no Processamento, 6 = Houve Mensagem).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36811336628119)
