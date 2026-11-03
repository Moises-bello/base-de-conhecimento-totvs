---
article_id: 360025830231
category: UBS - Unidade de Beneficiamento de Sementes
content_hash: 236eca84b4b8b8c84c39a797eaeb143af331ec83e47544bb22916831b465e661
fetched_at: '2026-06-28T22:45:34.729519+00:00'
product: protheus
section_id: 360005696194
source: central-protheus
title: Agro - Linha Protheus - AGR - Apontamento de perda
type: support-article
updated_at: '2025-06-20T15:28:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025830231-Agro-Linha-Protheus-AGR-Apontamento-de-perda
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21988176665879)***Tempo aproximado para leitura: **00:00:31 min****Dúvida**Como apontar perdas na estrutura da rotina **AGRA840 - Lote de Sementes**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Quando é informada a perda para algum dos produtos da estrutura do Lote de Sementes, caso o parâmetro da rotina **MATA685 - Apontar Perda**, do módulo **SIGAPCP - Planejamento e Controle da Produção**, esteja assinalado com **Não**, nenhum registro de perda é registrado na tabela **SD3**, e sim na tabela **SBC**. Se este parâmetro estiver assinalado com **Sim**, o registro é apontado na tabela **SD3**.  
  
**Importante**  
O parâmetro é chamado ao acionar a tecla**F12**, na rotina **MATA685**, que está no caminho **Atualizações** **>** **Movimentações** **>** **Produção**.
