---
article_id: 33173177098647
category: Materiais - Compras (SIGACOM)
content_hash: f8b90a082f9d13f02873b0a97535e3f5849c28c5ab6a3afc450fa6c82092f7f4
fetched_at: '2026-06-28T22:41:10.400638+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual é o compartilhamento
  correto das tabelas do Novo Fluxo de Compras (PGCA010)?
type: support-article
updated_at: '2025-07-01T13:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33173177098647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-%C3%A9-o-compartilhamento-correto-das-tabelas-do-Novo-Fluxo-de-Compras-PGCA010
---

**Dúvida:**  
Qual é o compartilhamento correto das tabelas do Novo Fluxo de Compras (PGCA010)?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2210.  
  
**Solução:**

Para assegurar o correto funcionamento do Novo Fluxo de Compras (NFC), é necessário atentar-se ao compartilhamento adequado das tabelas relacionadas aos processos de análise e geração de cotação/pedidos. Esse controle visa garantir a integridade dos dados e a fluidez das etapas do processo.

O controle de saldos, juntamente com outras características específicas do NFC (Novo Fluxo de Compras), é fundamental para a utilização adequada de tabelas exclusivas. Esses aspectos garantem a integridade e a consistência dos dados, permitindo que cada tabela atenda às particularidades do ambiente NFC

|  |  |  |  |
| --- | --- | --- | --- |
| Tabela | X2\_MODO | X2\_MODOUN | X2\_MODOEMP |
| Produtos da Cotação (DHV) | E | E | E |
| Pedidos de Compra (SC7) | E | E | E |
| Cotações (SC8) | E | E | E |
| Cabeçalho da Cotação (DHU) | E | E | E |

* **Atenção**  
  **Alterações no compartilhamento das tabelas listadas podem impactar o funcionamento do Novo Fluxo de Compras, comprometendo seu processo.**

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
