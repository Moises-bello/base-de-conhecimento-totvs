---
article_id: 25974847892631
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 984392564a6f3f56a13e5c6de2763d3b4a0e4ba203443cb4ea55fc4b360c2afc
fetched_at: '2026-06-28T22:38:57.195021+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MV_PDEVLOC - Estorno
  de Endereçamento na Exclusão do Documento de Saída e Apontamento de Produção
type: support-article
updated_at: '2025-12-08T16:54:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25974847892631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-PDEVLOC-Estorno-de-Endere%C3%A7amento-na-Exclus%C3%A3o-do-Documento-de-Sa%C3%ADda-e-Apontamento-de-Produ%C3%A7%C3%A3o
---

O sistema TOTVS Protheus, ao excluir uma nota com produto endereçado ou estornar apontamento de produção, pode devolver o produto ao estoque conforme o parâmetro MV\_PDEVLOC: 0 para redistribuir (novo endereçamento), 1 para retornar à localização original, ou 2 para perguntar ao usuário. O tempo da mensagem pode ser ajustado pelo parâmetro MV\_PERGDLT.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25974809244951) Tempo aproximado para leitura: **00:01:23 min**  
  
**Dúvida**

Ao excluir uma nota que possui produto com endereçamento, ou um estorno do apontamento de Produção, quais tratamentos o sistema pode realizar para devolver o produto ao estoque?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Isso depende da configuração do parâmetro MV\_PDEVLOC ele pode determinar:

* MV\_PDEVLOC = 0 (Redistribuir): O produto volta ao estoque para redistribuição, sendo necessário realizar um novo endereçamento;
* MV\_PDEVLOC = 1 (Localização Original): O produto retorna ao Endereço que estava antes, dessa forma não é necessário realizar um novo endereçamento;
* MV\_PDEVLOC = 2 (Perguntar): O sistema exibe uma tela perguntando se deseja redistribuir ou retornar o produto ao endereço que estava antes:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25974847875479)

O tempo de apresentação da mensagem na tela por padrão é de 5 segundos. Caso o usuário queira aumentar o tempo em segundos, basta modificar o parâmetro **MV\_PERGDLT** para o numero em segundos que deseja manter a mensagem na tela

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31110957018135)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
