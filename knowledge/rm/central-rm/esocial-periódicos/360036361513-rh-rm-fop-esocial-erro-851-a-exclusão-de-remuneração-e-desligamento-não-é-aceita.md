---
article_id: 360036361513
category: esocial - Periódicos
content_hash: e61c056187809566113d9e8d31392c936b270cc76df7189017f22906537a65d2
fetched_at: '2026-06-28T22:47:09.290857+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 851: A exclusão de remuneração e desligamento
  não é aceita quando houver pagamento relacionado'
type: support-article
updated_at: '2024-12-18T15:29:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036361513-RH-RM-FOP-eSocial-Erro-851-A-exclus%C3%A3o-de-remunera%C3%A7%C3%A3o-e-desligamento-n%C3%A3o-%C3%A9-aceita-quando-houver-pagamento-relacionado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24179809545751)****Tempo aproximado para leitura:** **00:01:00 min****Ocorrência**  
Ao transmitir o evento **S-3000** de exclusão para o governo é retornado a inconsistência **A exclusão de remuneração e desligamento não é aceita quando houver pagamento relacionado. Ação Sugerida: Antes de excluir a remuneração ou desligamento exclua as informações de pagamento relacionadas.**

![851.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047732953)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Conforme mensagem apresentada, a inconsistência ocorre quando é transmitido a exclusão do evento de remuneração (S-1200,S-1202) e/ou desligamento (S-2299, S-2399), mas existem eventos de **Pagamentos de Rendimentos do Trabalho (S-1210)** vinculados e que não foram excluídos no eSocial Web.  
  
**Solução**  
Para correção da ocorrência será necessário a exclusão do S-1210 antes do envio do evento de remuneração/desligamento. Para excluir o evento S-1210, acesse **eSocial | Eventos Periódicos**e localize o evento que corresponde ao valor líquido presentes no evento S-1200.

![22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047737813)

Quando o evento de desligamento possuir verbas rescisórias existirá um evento de **Pagamento de Rendimentos** associado, e caso tenha sido transmitido ao eSocial também deve ser excluído através do evento S-3000 de Exclusão.

**Importante**  
Para a exclusão de eventos de remuneração deverá certificar-se que não haja eventos de Pagamentos de Rendimentos associados à esses eventos no eSocial Web, pois serão impactados diretamente com essa ação.  
Caso a sua empresa trabalhe com **Regime Caixa ,** será necessário verificar o período de apuração do evento **S-1210** que está levando o valor líquido, podendo não ser do mesmo período de apuração S-1200 e S-1202.   
  
**Saiba Mais**Para mais informações acesse:  
   • [S-3000 - Exclusão de Eventos](https://tdn.totvs.com/pages/releaseview.action?pageId=364908560)  
   • [Como visualizar o S-3000 de um registro na fila de eventos?](https://tdn.totvs.com/pages/releaseview.action?pageId=501476328)
