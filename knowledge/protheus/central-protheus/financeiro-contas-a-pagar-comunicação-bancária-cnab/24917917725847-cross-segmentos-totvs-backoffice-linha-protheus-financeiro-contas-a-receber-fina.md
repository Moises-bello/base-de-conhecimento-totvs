---
article_id: 24917917725847
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: ca2141d8398d174151b92062b7416f29d3f69b0aeed4c73dc51041b789f22b7a
fetched_at: '2026-06-28T22:37:56.497470+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice (Linha Protheus) - Financeiro - Contas a
  Receber - FINA200 - Como adicionar dias a despesa bancária pelo PE F200VAR
type: support-article
updated_at: '2024-07-16T11:13:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24917917725847-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Financeiro-Contas-a-Receber-FINA200-Como-adicionar-dias-a-despesa-banc%C3%A1ria-pelo-PE-F200VAR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24917917685399) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como adicionar dias de retenção a despesa bancária pelo PE F200VAR

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**No arquivo de retorno **FINA200 / FINR650** para a despesa bancária não possui a posição de **Data de Crédito** preenchido, mas em alguns bancos esse crédito é depositado na conta bancária um dia depois do retorno bancário.

Por padrão, o Protheus valida duas datas **(data de ocorrência = Data do Movimento) e (data do crédito = data que o dinheiro foi depositado na conta)**

Caso a data de crédito do movimento de despesa bancária esteja vazia, o protheus irá pegar a database para preencher as movimentações de data na SE5

Podemos trabalhar com o ponto de entrada **F200VAR** para gravar dias a mais de credito para a despesa bancária  
-- <https://tdn.totvs.com/pages/releaseview.action?pageId=235308494>

Exemplo:

dDataCred+1,.T. = Neste exemplo estamos colocando a data de crédito + um dia, ou seja

Caso esteja vazia = Pega a database do processamento do retorno + um dia

Caso esteja preenchida = Pega a data de crédito do arquivo + um dia

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24917917687831)  
  
O teste deve ser efetuado conforme o exemplo publicado pelo Desenv. no TDN variáveis restritas em fontes customizados não estão previstas pelo suporte padrão, dado ao fato de que as mesmas não estão documentadas, assim sendo, podem vir a ser descontinuadas ou sofrer alterações de comportamento sem prévio aviso.   
  
Saiba mais  
[Comunicação Bancária](https://tdn.totvs.com/pages/releaseview.action?pageId=240288856)  
[F200VAR - CNAB Receber - Manipular variáveis no processamento do retorno](https://tdn.totvs.com/pages/releaseview.action?pageId=235308494)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Como gerar despesa bancária no retorno do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016697191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-gerar-despesa-banc%C3%A1ria-no-retorno-do-CNAB)  
[Cross Segmentos - Backoffice Protheus - SIGAFIN - CNAB - Dias Retenções(A6\_RETENCA) não soma a Data Disponibilidade(E5\_DTDISPO)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028890832-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-CNAB-Dias-Reten%C3%A7%C3%B5es-A6-RETENCA-n%C3%A3o-soma-a-Data-Disponibilidade-E5-DTDISPO?source=search)
