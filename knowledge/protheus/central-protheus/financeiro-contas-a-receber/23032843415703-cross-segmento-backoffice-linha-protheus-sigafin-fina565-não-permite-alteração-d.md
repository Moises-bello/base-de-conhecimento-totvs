---
article_id: 23032843415703
category: Financeiro - Contas a Receber
content_hash: 2d2657a795be7f1b2c4168113c1257833d8ba8b42991039117f352abd573b709
fetched_at: '2026-06-28T22:38:12.850831+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA565 - Não Permite
  Alteração do Valor da liquidação
type: support-article
updated_at: '2024-04-25T17:21:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23032843415703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA565-N%C3%A3o-Permite-Altera%C3%A7%C3%A3o-do-Valor-da-liquida%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23032897445143) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**O campo valor está bloqueado para edição/alteração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23052711889815)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA565 - Todas as versões  
  
**Causa**O problema é o campo E2\_VLCRUZ que não está mais habilitado para realizar a alteração.  
  
**Solução**1 - Execute o dicionário **UPDDISTR** para que o sistema habilite novamente o campo para **edição/alteração** **"Caso o ambiente esteja mais atualizado que o dicionário"**

2 - Se após executar o **dicionário** e **campo** ainda permanecer bloqueado, acesse o **Configurador -> Base de dados-> Dicionário -> Base de dados**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23032897446807)

Após esse processo localize pela tabela **SE2**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23032897449495)

Clique em alterar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23032897451927)

Localize pela campo **E2\_VLCRUZ**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23032843376663)

Selecione o **campo** e clique em **alterar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23032897456151)

Ajuste o campo **Propriedade** de **Visualizar** para **Alterar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23032843385495)

Na aba **Opção** insira no **Modo de edição .T.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23032897464343)

Após esse processo salve para que o campo volte a ser editado.

**SAIBA MAIS**[Liquidação a pagar - FINA565](https://tdn.totvs.com/pages/releaseview.action?pageId=312167645)[Liquidação a pagar automática - FINA565](https://tdn.totvs.com.br/pages/releaseview.action?pageId=514431886)
