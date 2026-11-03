---
article_id: 4410079346455
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 8ab6f638638fc749fb7361443fed0d236a8758e024c5e2ef6a341d216738f623
fetched_at: '2026-06-28T22:45:35.580170+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Ajuste Estorno de endereçamento
type: support-article
updated_at: '2025-06-18T14:02:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410079346455-Agro-Linha-Protheus-UBA-Ajuste-Estorno-de-endere%C3%A7amento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21896214847383) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**No módulo **Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão**, ao realizar a rotina **AGRA840 - Lote de Sementes**, ao escolher a opção **excluir** e **estornar** o insumo com **endereçamento**, mesmo utilizando o parâmetro **Inibe pergunta ref. localiza - MV\_PDEVLOC** com o valor **2**, que pergunta se deseja redistribuir ou voltar ao saldo original, não mostra a tela para escolher a opção e o saldo volta a redistribuir.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - A partir da versão 12.1.17  
  
**Causa**O parâmetro **MV\_PDEVLOC** em rotinas automáticas considera apenas os valores **0** e **1**.  
  
**Solução**Foi implementado para que ao realizar o estorno da **ordem de produção** via rotina automática **MATA250 -** **Produção**, que é utilizada ao escolher a opção **excluir** na rotina **AGRA840**, se o conteúdo do parâmetro for diferente de **0** e **1**, considere o valor **1** como padrão.
