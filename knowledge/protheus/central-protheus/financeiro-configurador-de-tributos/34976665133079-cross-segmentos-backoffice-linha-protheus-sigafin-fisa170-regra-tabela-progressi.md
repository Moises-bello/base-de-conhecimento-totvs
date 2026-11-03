---
article_id: 34976665133079
category: Financeiro - Configurador de Tributos
content_hash: bbe00faa6877699955326ddaee9c933e70b4814841134d570e50e6ee2da69abc
fetched_at: '2026-06-28T22:37:46.059273+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Regra Tabela
  Progressiva
type: support-article
updated_at: '2026-01-14T19:00:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34976665133079-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Regra-Tabela-Progressiva
---

**Dúvida:**  
O sistema não reconhece a tabela progressiva do IRRF vinculada ao imposto cadastrado no Configurador de Tributos.  
  
**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**

**Processo para IR Progressivo via Configurador de Tributos.**

Para o processamento do **Imposto de Renda Progressivo** no Configurador de Tributos, é necessário criar a tabela correspondente por meio da rotina **FISA170**.

O conceito permanece o mesmo utilizado anteriormente, porém, nesse caso, o sistema utilizará o menu **“Regra de Tabela Progressiva”** da FISA170.

Para esse cenário, crie a **regra da tabela progressiva** considerando os campos indicados a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34976665115287)

1. Acessar o menu **Regra de Tabela Progressiva** na FISA170.
2. Clicar em **Incluir**.
3. Informar o **código** e a **descrição**.
4. Preencher as demais informações necessárias.
5. Clicar em **Confirmar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37676558279063)

Após o cadastro da tabela progressiva, é necessário realizar o vínculo com a regra de cálculo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35827796578327)

📢️Importante

***Valores de cada faixa devem ser anualmente ajustados.***

**Saiba Mais**

[SIGAFIN - Configurador de Tributos - How to](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33852958399767-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Configurador-de-Tributos-How-to)

[SIGAFIN - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
