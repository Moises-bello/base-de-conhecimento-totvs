---
article_id: 360028075854
category: Inspeção de Entradas (SIGAQIE)
content_hash: b5ea83be3cb360acf0c53c9084b74131baf4508854f95096a00ff0e9f346b569
fetched_at: '2026-06-28T22:42:27.033988+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Help Q_010FAOBR ao salvar especificação
  de produto
type: support-article
updated_at: '2021-09-08T12:58:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028075854-Manufatura-Linha-Protheus-SIGAQIE-Help-Q-010FAOBR-ao-salvar-especifica%C3%A7%C3%A3o-de-produto
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**Ao salvar o registro, na rotina **Especificação de Produto - QIEA010** é apresentado o help **Q\_010FAOBR - Tipo de conversão aplicada à Unidade de Medida e Amostragem Primárias, via Fator de conversão primário**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**Esta mensagem é apresentada quando a unidade de medida informada no campo **Un. Medida 1 - QE6\_UNMED1** é diferente da unidade de medida da amostra informada no campo **Un. Amostra 1 - QE6\_UNAMO1**.  
  
**Solução**  
Quando a unidade de medida for diferente da unidade de medida amostra, é obrigatório informar o fator de conversão nos campos **Fat. Conv. 1 - QE6\_FATCO1** e **Tipo Conv. 1 - QE6\_TIPCO1**.
