---
article_id: 41328818452247
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7259b9b0b99ad7485ee35b38b5a79a2c862d3f2bd2632af246de8828704ea51b
fetched_at: '2026-06-28T22:42:43.393108+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Importação de empenhos de projeto para
  o MRP
type: support-article
updated_at: '2026-06-18T18:45:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41328818452247-Manufatura-Linha-Protheus-SIGAPCP-Importa%C3%A7%C3%A3o-de-empenhos-de-projeto-para-o-MRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41328786426647) Tempo aproximado para leitura: **00:01:26 min**  
  
**Dúvida**  
A importação de empenhos de projeto para o **MRP - Material Requiriment Planning** através da rotina **PCPA136 - Demandas do MRP** faz a leitura e importação de dados de qual tabela do módulo **SIGAPMS - Gestão de Projetos**?   
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Na importação de empenhos de projeto a tabela que é lida e tem seus dados importados para a demanda é a tabela **AFJ - Empenhos do projeto,** na importação de empenhos de projeto nenhuma outra tabela além da **AFJ** é lida.  
  
**Saiba mais**  
Neste processo de importação é possível adicionar filtros customizados através do ponto de entrada P136FIL documentado em [P136FIL - Adicionar filtros nas importações de demandas](https://tdn.totvs.com/pages/releaseview.action?pageId=658764093)
