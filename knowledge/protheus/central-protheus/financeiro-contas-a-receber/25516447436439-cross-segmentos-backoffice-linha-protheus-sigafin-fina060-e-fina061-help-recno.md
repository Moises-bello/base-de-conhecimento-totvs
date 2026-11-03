---
article_id: 25516447436439
category: Financeiro - Contas a Receber
content_hash: 9865491c136f5018510d3c1094d7f013a61f8fdbd59590ddc1f0b043e67aa805
fetched_at: '2026-06-28T22:38:13.971919+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA060 e FINA061 -
  HELP RECNO
type: support-article
updated_at: '2026-03-24T17:31:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25516447436439-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA060-e-FINA061-HELP-RECNO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25516459364759) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Help RECNO sendo apresentado, mesmo preenchendo corretamente os filtros nas rotinas para gerar o borderô  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25516459365527)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
O Help pode estar sendo apresentado porque os títulos já foram transferidos para outra Situação e não está mais na "0 - Carteira"

- Para verificar selecione o título, **clique em** Visualizar > Outras Ações > Posição e verifique se a **Situação** do título está diferente de "Carteira" como o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25516447421975)  
  
**Solução**  
**1.** Caso esteja diferente de Carteira, será necessário transferir o título novamente para essa Situação.  
  
**2.** Para transferir o título, acesse a rotina FINA060 Transferências, ou se estiver na rotina Funções do Contas a Receber pode acessar através do botão Transf/Borderô:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25516459367319)  
  
**3.** Ao **Selecionar** Transferir, será aberta a caixa abaixo. **Apague** os dados do portador, **altere** a Situação para zero e **clique** em Ok:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25516447423127)  
  
**4.** Após a alteração será possível colocar o título em borderô e o Help não será mais apresentado

**Outro cenário comum é a Geração de Borderô para Títulos Liquidados:**

 A ocorrência do HELP RECNO ao gerar borderôs contendo títulos provenientes de liquidação pode ocorrer devido à restrição de documentos na parametrização da rotina (F12). Verifique se a pergunta "Seleciona Tipos?" está configurada como "SIM", pois isso limita as espécies de títulos elegíveis para o processamento, ocasionando a inconsistência. Para solucionar o incidente e permitir a inclusão correta desses registros, altere o valor desta pergunta para "NÃO", garantindo que os títulos gerados por liquidação sejam considerados na geração do borderô.

![bordero-recno-liq.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39264144022423)  
  
**Saiba mais**  
**-** [Transferências - FINA060](https://tdn.totvs.com/pages/viewpage.action?pageId=387286612)  
**-** [Borderô de Recebimento com Impostos - FINA061](https://tdn.totvs.com/pages/viewpage.action?pageId=95617838)
