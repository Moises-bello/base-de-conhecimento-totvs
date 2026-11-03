---
article_id: 40775909060631
category: Financeiro - Compensação entre Carteiras
content_hash: 4eef28c86488b691e147a41cdbc6401188dad73a04f588a61e83901956a4eb67
fetched_at: '2026-06-28T22:37:27.000384+00:00'
product: protheus
section_id: 35058659965079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice(Linha Protheus) - SIGAFIN - Comportamento
  do recurso Pesquisar na rotina FINA450
type: support-article
updated_at: '2026-05-27T19:04:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40775909060631-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Comportamento-do-recurso-Pesquisar-na-rotina-FINA450
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40775909041943)** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Ao utilizar o retorno "pesquisar" por indice na rotina FINA450, o sistema exibe uma falha na exibição, demonstrando a ordenação incorreta.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as releases  
  
**Solução**

O recurso Pesquisar, existente na rotina FINA450, funciona como um localizador de registros dentro da lista atual. Sua função é posicionar o cursor sobre o item, conforme filtro no indice desejado, sem aplicar filtros de ocultação nos demais dados apresentados na tela.

Ao final da ordenação e busca, o sistema posicionará o ponteiro no primeiro registro físico (RECNO) encontrado com o índice correspondente. Devido a esse comportamento padrão do componente visual, o registro localizado pode ser exibido no meio ou no fim do grid, mantendo informações acima do ponteiro posicionado na tela. Esse comportamento é nativo da interface e não indica uma falha de processamento.  
  
**Veja um exemplo:**

Tela de seleção FINA450:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40775897376663)

Na tela de seleção da rotina FINA450, o primeiro registro localizado pelo sistema através do campo **R\_E\_C\_N\_O\_** corresponde ao título **"ZZZ-ZZZZZ"**, que está posicionado na última linha do grid, conforme demonstrado no filtro aplicado abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40775909043863)

Dessa forma, ao utilizar o recurso de pesquisa, o sistema poderá posicionar automaticamente nesse registro localizado, mesmo que os demais registros fiquem fora da área inicialmente visível da grid.

Com isso, torna-se necessário, clicar na página e realizar a rolagem para visualizar completamente todo o filtro ordenado, conforme apresentado no GIF encaminhado.

![FINA450.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/40775909044631)

Saiba Mais:

[Compensação entre carteiras - FINA450 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=516194467)
