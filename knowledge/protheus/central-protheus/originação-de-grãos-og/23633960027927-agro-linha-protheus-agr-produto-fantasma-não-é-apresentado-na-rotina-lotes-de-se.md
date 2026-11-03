---
article_id: 23633960027927
category: Originação de Grãos (OG)
content_hash: fe60425b0a10bedd203db2c4299d1d2abb3f1e61c57a4893abd0146991dd8498
fetched_at: '2026-06-28T22:45:44.725334+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Produto fantasma não é apresentado na rotina
  Lotes de Sementes AGRA840
type: support-article
updated_at: '2025-06-24T20:43:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23633960027927-Agro-Linha-Protheus-AGR-Produto-fantasma-n%C3%A3o-%C3%A9-apresentado-na-rotina-Lotes-de-Sementes-AGRA840
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23633960003351) Tempo aproximado para leitura: **00:00:35 min** **Dúvida**Após realizar o cadastro de um produto fantasma, através do módulo **Estoque e Custos** o comportamento do produto fantasma ocorre conforme esperado, mas quando utilizado no módulo **Agro** na rotina **Lote de Sementes** o **produto fantasma** não é apresentado.  
  
**Ambiente**

TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Na rotina de **Lotes de Sementes - AGRA840** existe uma regra de negócio para não considerar os componentes do tipo **produto fantasma**.  
  
Como alternativa, é sugerido utilizar o ponto de entrada **AGR840P** e ajustar os insumos utilizados no reporte de produção.

Documentação do do ponto de entrada **AGR840P PE:** <https://tdn.totvs.com/pages/viewpage.action?pageId=844241681>
