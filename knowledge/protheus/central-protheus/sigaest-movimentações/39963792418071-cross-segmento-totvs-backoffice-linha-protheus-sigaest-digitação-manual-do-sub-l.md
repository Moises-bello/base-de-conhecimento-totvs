---
article_id: 39963792418071
category: SIGAEST - MOVIMENTAÇÕES
content_hash: ccd146f293c800908452889df60b0d477bfe13e1904ae109ab4777b9232c2bb3
fetched_at: '2026-06-28T22:38:58.480849+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Digitação manual
  do Sub-lote na Pré-Nota/Nota fiscal de entrada
type: support-article
updated_at: '2026-04-23T18:04:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39963792418071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Digita%C3%A7%C3%A3o-manual-do-Sub-lote-na-Pr%C3%A9-Nota-Nota-fiscal-de-entrada
---

No TOTVS Backoffice (Linha Protheus), o campo Sub-lote é gerado automaticamente e sequencialmente para garantir integridade e rastreabilidade, controlado pela função NextLote. Não é possível alterar essa regra nativamente; para numeração manual, é necessário customizar via pontos de entrada (XPROXLOT) ou sugerir melhoria na Central Colaborativa.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39963792407959) Tempo aproximado para leitura: 0**0:01:00 min**  
  
**Dúvida**  
Como realizar a digitação manual do campo Sub-lote durante o processo de recebimento via Pré-Nota/Documento de entrada, evitando a geração automática sequencial pelo sistema?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
No comportamento padrão do sistema, o campo de Sub-lote é gerado de forma automática e sequencial nas rotinas de entrada para garantir a integridade dos dados e a rastreabilidade, evitando duplicidades. Essa geração é controlada pela função NextLote, que utiliza o conteúdo do parâmetro MV\_PRXLOTE para definir e incrementar o próximo valor a ser gravado.

Não é possível alterar essa regra nativamente através de configurações de parâmetros, uma vez que o sistema é projetado para manter a unicidade do registro. Caso a necessidade do negócio exija uma numeração específica ou manual, as alternativas são:

* **Customização via Pontos de Entrada:** Utilização de pontos de entrada específicos [XPROXLOT](https://tdn.totvs.com/pages/releaseview.action?pageId=6089445) para manipular a numeração ou o comportamento do lote/sub-lote.

* **Abertura de Sugestão de Melhoria:** Registro da necessidade na [Central Colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics) para avaliação pelo time de Produto sobre a viabilidade de implementação no padrão.

Saiba Mais:

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Campo D1\_LOTECTL para produtos com controle de Rastro é possível tornar a digitação obrigatória?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29009366772631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campo-D1-LOTECTL-para-produtos-com-controle-de-Rastro-%C3%A9-poss%C3%ADvel-tornar-a-digita%C3%A7%C3%A3o-obrigat%C3%B3ria)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como ativar o controle de Lote/Rastro para produtos com saldo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020672612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-ativar-o-controle-de-Lote-Rastro-para-produtos-com-saldo)
