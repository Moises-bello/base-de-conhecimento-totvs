---
content_hash: b1ff47d98e4c1547a5d04a062ffbafd551ef3bd91b047b9ee9bd5eb0d4030a54
fetched_at: '2026-06-29T00:05:48.250599+00:00'
page_id: '1024340579'
product: rm
source: tdn-rm
title: Percentual do imóvel no contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024340579
version: 13
---

![Reforma Tributária](https://tdn.totvs.com/download/attachments/1025239488/1025239500/ReformaTributaria.png)


# Percentual do imóvel no contrato

Reforma tributária
Gestão de Imóveis

Após o cadastro do imóvel, o usuário configura o
**Contrato de Locação**, que é responsável por centralizar todas
as informações do processo.

## 📌 Definição no Contrato

No contrato é definido o **Percentual do Imóvel no Contrato**.

Esse percentual representa a participação de cada imóvel no valor total do
aluguel e é utilizado pelo sistema para realizar o
**rateio correto dos valores financeiros e fiscais**,
especialmente quando um mesmo contrato possui mais de um imóvel vinculado.

## ⚙️ Comportamento do Sistema

O comportamento do sistema varia conforme o tipo de contrato:

### 🔄 Contratos já existentes

(Cadastrados antes da implementação desta regra)

* **Contrato com um único imóvel:**  
  O sistema preenche automaticamente o percentual com
  **100%**, mantendo o comportamento anterior para garantir
  compatibilidade e evitar impactos em contratos já ativos.
  
* **Contrato com mais de um imóvel:**  
  O usuário deve informar manualmente os percentuais de cada imóvel,
  assegurando que a **soma total seja igual a 100%**.

### 🆕 Novos contratos

* O campo **Percentual do Imóvel** é apresentado em branco,
  independentemente da quantidade de imóveis vinculados ao contrato.
* O usuário é responsável por informar manualmente os percentuais,
  garantindo que o rateio reflita corretamente a participação de cada imóvel
  no contrato.
* O sistema poderá validar se a soma dos percentuais informados corresponde a
  **100%**, evitando inconsistências no rateio financeiro e fiscal.

![Percentual do Imóvel no Contrato](https://tdn.totvs.com.br/download/attachments/1024340579/image-2025-12-22_15-11-56.png?version=1&modificationDate=1766427117067&api=v2)


  


## ➡️ Resultado desta etapa

Ao final da configuração, o contrato estará devidamente preparado para:

* Realizar o **rateio correto dos valores de aluguel** entre os
  imóveis vinculados;
* Garantir a **correta geração dos movimentos financeiros**;
* Aplicar a **tributação adequada conforme a regra tributária associada**,
  garantindo consistência fiscal e contábil em todo o processo.

]]>
