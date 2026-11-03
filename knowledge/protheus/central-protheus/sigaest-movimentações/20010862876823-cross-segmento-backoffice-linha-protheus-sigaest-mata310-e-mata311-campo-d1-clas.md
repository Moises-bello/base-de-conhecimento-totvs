---
article_id: 20010862876823
category: SIGAEST - MOVIMENTAÇÕES
content_hash: c315e5b05f4ebc3dce3cf2f7131afa2e871f5d02d201a34baafa9f82e24d939f
fetched_at: '2026-06-28T22:38:57.101584+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 e MATA311
  campo D1_CLASFIS não recebe o conteúdo Situação tributaria (F4_SITTRIB) ao gerar
  Documento de entrada Classificado
type: support-article
updated_at: '2025-03-12T12:28:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20010862876823-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-e-MATA311-campo-D1-CLASFIS-n%C3%A3o-recebe-o-conte%C3%BAdo-Situa%C3%A7%C3%A3o-tributaria-F4-SITTRIB-ao-gerar-Documento-de-entrada-Classificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20010894131863) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**

Ao efetuar uma Transferência entre Filiais pelas rotinas MATA310 ou MATA311 já Cçlassificado o Documento de Entrada no Destino, transfere a mesma situação tributária da saída **D2\_CLASFIS** para a Entrada **D1\_CLASFIS**.   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

O comportamento do sistema para esse cenário apresentado esta correto. Devido a classficação da Nota Fiscal de Saída da Filial Origem ser a mesma para a Nota de Entrada da Filial Destino.  
   
Caso tenha necessidade de alterar este comportamento, utilizar o ponto de entrada M310ITENS.

**M310ITENS - Permite manipulação do arrey aItens**

**<https://tdninterno.totvs.com/pages/viewpage.action?pageId=6087583>**

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

*[Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-)*
