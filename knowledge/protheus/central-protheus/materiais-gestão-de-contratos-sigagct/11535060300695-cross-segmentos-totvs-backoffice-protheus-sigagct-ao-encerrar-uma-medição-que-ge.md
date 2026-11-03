---
article_id: 11535060300695
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 8cd648ba2a56cd6c15efb235a7ba2e897da2484e16274feedd3642e98f6d1894
fetched_at: '2026-06-28T22:37:21.330455+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao encerrar uma medição
  que gera Titulo Financeiro ocorre o Help NOCNNATMD
type: support-article
updated_at: '2023-01-09T13:02:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535060300695-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-encerrar-uma-medi%C3%A7%C3%A3o-que-gera-Titulo-Financeiro-ocorre-o-Help-NOCNNATMD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao encerrar uma Medição que gerar Titulo ocorre o Help NOCNNATMD mencionando o parâmetro MV\_CNNATMD

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11534873483671)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos Fiscal - Todas as versões

**Solução**  
Referente a mensagem, no caso, ao se encerrar uma medição na qual será gerado um titulo, pelo conceito do módulo deve ser informado um código de Natureza valido cadastrada no conteúdo do parâmetro MV\_CNNATMD.  
Caso se deseje a utilização de uma outra natureza para a geração do titulo Financeiro no encerramento da medição, esta natureza deve ser informada no cadastro do contrato no campo CN9\_NATURE.  
Mas de qualquer forma, o parâmetro MV\_CNNATMD necessita que possua um código de natureza válido cadastrada em seu conteúdo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11534972853399)

***Obs:***

o código acima informado no parâmetro necessite estar cadastrado no cadastro de Naturezas na filial em que se está sendo encerrada a medição.

***Saiba Mais :***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
