---
article_id: 20649122233239
category: Originação de Grãos (OG)
content_hash: f9f36e8a1cac0418b8c206d5eda413be7f144b1787985a413802090e738439e9
fetched_at: '2026-06-28T22:45:41.093005+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - OGA250 - Romaneio gera pedido mas não altera
  o status
type: support-article
updated_at: '2025-06-23T20:08:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20649122233239-Agro-Linha-Protheus-AGR-OGA250-Romaneio-gera-pedido-mas-n%C3%A3o-altera-o-status
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20649112421527) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**  
No módulo Faturamento, ao realizar o processo para confirmar o registro do romaneio o **Pedido de Venda no Romaneio com Pesagem**é apresentada a ocorrência **Romaneio gera pedido mas não altera o status**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para confirmar o registro do romaneio o **Pedido de Venda no Romaneio com Pesagem** no sistema.  
  
**Solução**  
Para solucionar essa ocorrência, esse problema pode ocorrer porque o campo **C6\_CODROM** não está marcado para a utilização em todos os módulos, portanto a opção **Utilizado por Todos os Módulos** deve ser assinalada para este campo.  
É necessário também verificar o tamanho do campo**C6\_CODROM** e comparar com os demais campos referentes ao **Código do Romaneio**, pois todos os campos devem ter o mesmo tamanho.  
Caso seja alterado o tamanho do campo **C6\_CODROM**, será necessário após a alteração, efetuar um b*ackup* da tabela, d*ropar* para que seja recriada com o tamanho correto e em seguida, efetuar um *append* dos dados.
