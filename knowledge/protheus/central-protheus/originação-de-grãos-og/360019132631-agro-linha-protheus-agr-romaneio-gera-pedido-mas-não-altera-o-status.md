---
article_id: 360019132631
category: Originação de Grãos (OG)
content_hash: 662a298cf4d5fda4d7d6ae2779222905587bfbee099e32726fab20d6b65ff575
fetched_at: '2026-06-28T22:45:44.833051+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Romaneio gera pedido mas não altera o status
type: support-article
updated_at: '2025-06-24T11:36:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019132631-Agro-Linha-Protheus-AGR-Romaneio-gera-pedido-mas-n%C3%A3o-altera-o-status
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20642639417751)***Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Na rotina **OGA250 -** **Romaneio com Pesagem** ao **Confirmar** o registro do romaneio o **Pedido de Venda** é gerado, porém o **Status do Romaneio** não é alterado?   
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Esse problema pode ocorrer porque o campo **C6\_CODROM** não está marcado para a utilização em todos os módulos, portanto a opção **Utilizado por Todos os Módulos** deve ser assinalada para este campo.  
É necessário também verificar o tamanho do campo**C6\_CODROM** e comparar com os demais campos referentes ao **Código do Romaneio**, pois todos os campos devem ter o mesmo tamanho.  
Caso seja alterado o tamanho do campo **C6\_CODROM**, será necessário após a alteração, efetuar um b*ackup* da tabela, d*ropar* para que seja recriada com o tamanho correto e em seguida, efetuar um *append* dos dados.
