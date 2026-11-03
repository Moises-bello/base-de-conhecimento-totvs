---
article_id: 360044895133
category: Inspeção de Entradas (SIGAQIE)
content_hash: 95d62039099bc0128af5ed4421ff0d11647fee8e623f439dfd87ef11c14edbba
fetched_at: '2026-06-28T22:42:26.899456+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Calcular automaticamente o tamanho
  da amostra no QIEA200
type: support-article
updated_at: '2021-07-12T16:33:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044895133-Manufatura-Linha-Protheus-SIGAQIE-Calcular-automaticamente-o-tamanho-da-amostra-no-QIEA200
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:50 min**  
**Dúvida**Na rotina **QIEA200 - Entradas** é possível calcular automaticamente o tamanho da amostra, exibido no campo **Tam. Amostra**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Na rotina **QIEA200**o campo **Tam. Amostra** é calculado automaticamente quando no **QIEA010 - Especificação de Produtos**, o conteúdo dos campos **Un. Medida 1**e **Un. Amostr. 1** são diferentes. Ou seja, que as unidades de medida sejam diferentes, e que tenham sido informados os campos: **Fat. Conv. 1**, **Tipo Conv. 1**, **Un. Medida 2**, **Fat. Conv. 2** e **Tipo Conv. 2**. Além disso, no cadastro do produto na rotina **MATA010 - Atualização de Produtos**, deve ser informada a segunda unidade de medida no campo **Seg. Un. Medi.**.
