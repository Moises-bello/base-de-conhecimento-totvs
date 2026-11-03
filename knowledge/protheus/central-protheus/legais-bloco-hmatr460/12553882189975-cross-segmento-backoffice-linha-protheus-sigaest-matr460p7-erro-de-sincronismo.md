---
article_id: 12553882189975
category: LEGAIS - BLOCO H/MATR460
content_hash: 0223d17beffca59b98be93a78099f3468e2ca7ae43c95ed344d04965570c810e
fetched_at: '2026-06-28T22:42:15.173655+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460/P7 - Erro
  de Sincronismo
type: support-article
updated_at: '2023-03-29T13:24:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12553882189975-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-P7-Erro-de-Sincronismo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:20 min****Ocorrência**Ao gerar o relatório P7 (MATR460) ocorre queda do Sistema, apresentando erro de Sincronismo.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Este erro acontece por causa da existência do arquivo "libctreecb.so" e "ctreecb.dll" na pasta *AppServer*.  
  
**Solução**

Estes arquivos relacionados ao CTREE foram descontinuados: [<https://tdn.totvs.com/display/tec/Application+Server+-+LIBCTREECB>]

Para que não ocorra este erro de sincronismo, remova o arquivo **libctreecb.so** e a dll **ctreecb.dll** da pasta *AppServer*, reinicie o serviço do mesmo para que seja feito um novo teste de geração do relatório P7.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre o relatório MATR460*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)

[*Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
