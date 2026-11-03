---
article_id: 4409116917527
category: Gestão de Transportes (TMS)
content_hash: 2ebb9e30bf158344f8edcd2bff6543ec66c946c0f940f94b8a7d33fb94b0e8bc
fetched_at: '2026-06-28T22:45:27.509633+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Complemento Tabela de Frete
type: support-article
updated_at: '2023-02-08T14:19:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409116917527-Log%C3%ADstica-Linha-Protheus-TMS-Complemento-Tabela-de-Frete
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:40 min** **Dúvida**Como funciona o **Complemento da Tabela de Frete**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**Na  rotina **TMSA010 - Tabela de Frete**, há a aba **Complemento Tabela de Frete**, que permite definir uma regra para calcular um valor excedente à regra definida na **Tabela de Frete**, utilizando como base cálculo mínimo de excesso.  
  
O cálculo mínimo de excesso está diretamente relacionado às faixas de valores de frete definidas para os componentes que formam a tabela de frete.  
  
Observe o exemplo a seguir:

**Tabela de Frete Rodoviário - Componente - Frete Peso**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Item** | **Até (Peso)** | **Fator Peso** | **Valor** | **Fração** |
| 1 | 10 | 10 | 40,53 | 0,0000 |
| 2 | 20 | 20 | 34,44 | 0,0000 |
| 3 | 30 | 30 | 27,58 | 0,0000 |
| 4 | 50 | 50 | 20,48 | 0,0000 |

Com base na tabela de frete apresentada, verifique o cálculo efetuado pelo sistema para a seguinte situação:

* Base de Cálculo = 50 Kg - Peso transportado da nota fiscal do cliente;
* Mínimo de Excesso = 30 Kg - Dado informado no complemento da tabela de frete para o componente.

Processamento efetuado:

* **Calcula o valor da faixa a partir da base de cálculo:**
  + Base de Cálculo = 50 kg - **faixa 04 - até 50,0000**, valor obtido 40,53.
* **Calcula o valor para o mínimo de excesso**:
  + Mínimo de Excesso = 30 kg - **faixa 03  - até 30,0000**, valor obtido 34,44.
* **Calcula o peso excedido para o cálculo do valor frete:**
  + Peso Excedido = Base de Cálculo - Mínimo de Excesso (50 kg - 30 kg)
  + Peso Excedido = 20 kg
* **Fórmula de cálculo do valor do componente:**
  + **Valor Componente = (Peso Excedido \* (Valor Excedente / Fração Excedente)) + Base de Cálculo**
  + **Valor do Componente = (20 \* (34,44 / 1)) + 40,53**
  + **Valor do Componente = 729,33**
* Se o mínimo de excesso não for informado ou a base de cálculo for menor ou igual ao mínimo de excesso, o valor da faixa será referente a base de cálculo.
