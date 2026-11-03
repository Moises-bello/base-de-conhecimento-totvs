---
article_id: 25270213948183
category: Chão de Fábrica (SIGASFC)
content_hash: 77b85c0102eba2e6b6a5c3533394832510918fafeb1d60d713e02230b46850da
fetched_at: '2026-06-28T22:42:49.875676+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Os empenhos não são atualizados ao
  apontar a produção
type: support-article
updated_at: '2024-07-30T15:02:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25270213948183-Manufatura-Linha-Protheus-SIGASFC-Os-empenhos-n%C3%A3o-s%C3%A3o-atualizados-ao-apontar-a-produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25270207608983)***Tempo aproximado para leitura: **00:00:55 min  
  
Dúvida**Por que os empenhos não são atualizados ao apontar a produção no módulo **Chão de Fábrica**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12   
  
**Solução**  
Essa situação ocorre quando o parâmetro **MV\_REQAUT- Verifica se o Sistema deve ou não gerar requisições automáticas** está como **D** e no cadastro da **TM - Tipo de Movimentação** de requisição o campo **F5\_ATUEMP - Atu. Empenho** está igual a **N- Não**.É preciso nesse caso, verificar a **TM** informada no parâmetro **MV\_SFRQMB - Tipo de Movimento a ser utilizado pelo módulo Chão de Fábrica ao fazer requisições e apontamentos de mão de obra**, e no cadastro dessa **TM** ajustar o campo **F5\_ATUEMP** para **S- Sim**.  
  
**Importante**  
As **TM's** são cadastradas no **MATA230 - Tipo de Movimentação.**  
  
**Saiba Mais**  
Para mais informações sobre o comportamento do parâmetro **MV\_REQAUT** no módulo **Chão de Fábrica,** acesse o link: [Manufatura - Linha Protheus - SIGASFC - Funcionalidade do parâmetro MV\_REQAUT no Chão de Fábrica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045164793-Manufatura-Linha-Protheus-SIGASFC-Funcionalidade-do-par%C3%A2metro-MV-REQAUT-no-Ch%C3%A3o-de-F%C3%A1brica)
