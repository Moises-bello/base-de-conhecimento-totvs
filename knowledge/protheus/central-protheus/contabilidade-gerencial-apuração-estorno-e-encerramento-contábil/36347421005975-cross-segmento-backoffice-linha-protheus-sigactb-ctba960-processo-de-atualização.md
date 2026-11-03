---
article_id: 36347421005975
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 36884d0c84f414c56559b3a66c0f66546341839aa8b9ab05448a0d095285f89e
fetched_at: '2026-06-28T22:41:05.102919+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA960 - Processo de
  atualização de saldos.
type: support-article
updated_at: '2026-01-22T18:36:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36347421005975-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Processo-de-atualiza%C3%A7%C3%A3o-de-saldos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36347436688023) Tempo aproximado para leitura: 00**:10 min**

**Dúvida**  
Como realizar o ajuste dos saldos contábeis, pela rotina Fechamento Contábil (CTBA960)

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - a partir da versão 12.1.2310

**Solução**  
Para realizar a atualização de saldos contábeis pela rotina Fechamento Contábil (CTBA960), você deve:

1. Na rotina, criar uma definição na opção **Definições de Fechamento**, onde você configura responsáveis, filiais e parâmetros iniciais.
2. Volte a tela principal, e selecione **Iniciar Fechamento.**
3. Na tela principal do Fechamento, **selecione o período** (mês/ano) e a **moeda** para o qual você deseja realizar a verificação/reprocessamento de saldos.
4. Em um dos passos do Fechamento Contábil, você encontrará a opção **Verificar Saldos.** Este é o passo que substitui o Reprocessamento de Saldos.  
   **Obs: Não é obrigatório a execução dos passos anteriores e posteriores.**
5. O sistema perguntará se deseja realizar a verificação de saldos.
6. Selecione **Executar**. **O que acontece neste passo:** O Protheus recalcula os saldos com base nos lançamentos contábeis para o período e moeda selecionados. Se divergências forem encontradas, elas serão apresentadas para que você realize os ajustes ou utilize outras ferramentas de conciliação.
7. Após a verificação/reprocessamento e eventuais ajustes, você poderá avançar para a etapa de **Bloqueio de Calendário** (se for o objetivo do Fechamento), ou encerrar a rotina, pois os demais passos não são obrigatórios.

**Para mais detalhes disponibilizados um** ***How To*** **detalhado do processo para melhor compreensão:**

**Obs: Avance até o minto 1:00, para verificar o processo do Ajuste de Saldo.**

**Saiba mais:**  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA960 - Fechamento Contábil.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34334419010839-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Fechamento-Cont%C3%A1bil)  
[Fechamento Contábil (SIGACTB) - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=722662924)
