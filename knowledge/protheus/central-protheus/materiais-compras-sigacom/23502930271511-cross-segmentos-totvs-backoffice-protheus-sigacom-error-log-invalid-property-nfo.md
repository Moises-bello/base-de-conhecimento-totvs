---
article_id: 23502930271511
category: Materiais - Compras (SIGACOM)
content_hash: 9d9a1432477e769e99d3a17d24b973f204454bf838281676b8f1c13a58cf40cb
fetched_at: '2026-06-28T22:41:17.638613+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Error Log invalid
  property NFONTHEADER on {|x|self:NFONTHEADER := x}(FWSERIALIZE.PRW)  line : 343'
type: support-article
updated_at: '2024-09-18T15:02:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23502930271511-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Error-Log-invalid-property-NFONTHEADER-on-x-self-NFONTHEADER-x-FWSERIALIZE-PRW-line-343
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23502939932439) Tempo aproximado para leitura: **00:02:00 min** **Ocorrência**Ao executar algumas rotinas de Compras como Documento de Entrada por exemplo e rotinas de outros módulos do sistema apresenta o Error Log abaixo:

***invalid property NFONTHEADER on {|x|self:NFONTHEADER := x}(FWSERIALIZE.PRW) line : 343***

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões

**Solução**

Aplicar a última Lib do Portal para validação em ambiente de homologação.

Baixar o pacote o pacote de LIB disponível na Central de Downloads por meio do caminho:  
*Home -> TOTVS Linha Protheus -> TOTVSTEC-FRAMEWORK -> LIB*

Na lista apresentada, selecione o arquivo com data mais recente,   
Por exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23504074498455)

   
Link Ambiente LIB Harpia: <https://suporte.totvs.com/portal/p/10098/download?e=1050526>

Abaixo também link de pagina para download do Pacote Acumulado do módulo de Compras, que é recomendado sempre possuir atualizado:

COM: <https://tdn.totvs.com/pages/viewpage.action?pageId=522011099>

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
