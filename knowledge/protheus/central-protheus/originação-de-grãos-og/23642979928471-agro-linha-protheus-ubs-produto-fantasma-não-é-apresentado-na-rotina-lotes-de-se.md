---
article_id: 23642979928471
category: Originação de Grãos (OG)
content_hash: d12b4ad0fa6111eab76c29e0b267d90ddb051549894060a82076ca41a8948377
fetched_at: '2026-06-28T22:45:45.987769+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - UBS - Produto fantasma não é apresentado na rotina
  Lotes de Sementes - AGRA840
type: support-article
updated_at: '2025-06-24T14:41:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23642979928471-Agro-Linha-Protheus-UBS-Produto-fantasma-n%C3%A3o-%C3%A9-apresentado-na-rotina-Lotes-de-Sementes-AGRA840
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23643001458711) Tempo aproximado para leitura: **00:01:20 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, após realizar o cadastro de um **produto fantasma** através do módulo **Estoque e Custos**, o comportamento do **produto fantasma** ocorre conforme esperado, mas quando utilizado no módulo **Agro** na rotina **Lote de Sementes** é apresentada a ocorrência **Produto fantasma não é apresentado na rotina Lotes de Sementes - AGRA840**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois ao realizar o cadastro de um **produto fantasma** no módulo **Estoque e Custo**, o mesmo não é apresentado na rotina **Lotes de Sementes - AGRA840**.  
  
**Solução**

Na rotina de **Lotes de Sementes - AGRA840** existe uma regra de negócio para não considerar os componentes do tipo **produto fantasma**.  
  
Como alternativa, é sugerido utilizar o ponto de entrada **AGR840P** e ajustar os insumos utilizados no reporte de produção.

Documentação do do ponto de entrada **AGR840P PE: <https://tdn.totvs.com/pages/viewpage.action?pageId=844241681>**
