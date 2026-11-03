---
article_id: 4413885286807
category: ADVPL - Ponto de Entrada
content_hash: 7183e0602bcaceb1a62cc7ffe0fefd15bc00adce8f52b6d0e5828c5aaa876f1d
fetched_at: '2026-06-28T22:40:12.957528+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Execução do ponto
  de entrada M410lDel '
type: support-article
updated_at: '2021-11-22T21:07:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413885286807-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execu%C3%A7%C3%A3o-do-ponto-de-entrada-M410lDel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que o ponto de entrada M410lDel é executado duas vezes?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**O PE **M410lDel** é chamado na função A410ValDel e esta por sua vez é chamada via MSGetDados na posição 17 (*cDelOk*). De acordo com equipe de Framework este é o comportamento devido que ocorre desde a versão 10, onde a execução da função chamada no parâmetro 17 da msgetdados é executada no delok do browse e no bloco de delete do browse.  
Pode-se utilizar a função PROCNAME() para validar a fila da chamada e assim só executar uma vez.  
  
**Saiba mais**  
[M410lDel - Validar a exclusão de itens na alteração do PV](https://tdn.totvs.com/pages/releaseview.action?pageId=6784565)  
[ProcName](https://tdn.totvs.com/display/tec/ProcName)
