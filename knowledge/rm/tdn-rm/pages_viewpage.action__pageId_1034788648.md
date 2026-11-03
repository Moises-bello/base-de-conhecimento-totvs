---
content_hash: c79dcd1a260c6b1e24a164355fdcb1d042b13480f8feead6859a73ff9fc966a7
fetched_at: '2026-06-29T00:05:48.969279+00:00'
page_id: '1034788648'
product: rm
source: tdn-rm
title: Evento Financeiro - Compõe IVA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1034788648
version: 11
---

---

![Evento Financeiro - Compõe IVA](https://tdn.totvs.com/download/attachments/1025239488/1025239500/ReformaTributaria.png)


# Evento Financeiro – Compõe IVA

Reforma Tributária - Gestão de Imóveis

Dentro do cadastro do Evento Financeiro, o usuário encontrará o campo
**Compõe IVA**, que deve ser marcado quando os valores desse evento
precisarem **compor a base de cálculo do Imposto sobre Valor Agregado (IVA)**,
considerando os tributos **IBS** e **CBS**, conforme a
regra tributária aplicável ao tipo de evento.

A correta utilização desse campo é essencial para garantir a geração adequada dos
lançamentos financeiros, o cálculo correto dos tributos e a integração com os módulos
financeiros do sistema.

  


## 🧾 Campo Compõe IVA

O campo **Compõe IVA** tem como finalidade indicar se os valores de um
evento financeiro devem integrar a base de cálculo do
Imposto sobre Valor Agregado (IVA), no contexto da
Reforma Tributária, que contempla os tributos **IBS** e
**CBS**.

Ao habilitar esse campo no evento financeiro, os lançamentos gerados a partir dele
passam a conter automaticamente as informações necessárias para a correta apuração
dos impostos.

## ⚙️ Comportamento do Sistema

Quando o parâmetro **Compõe IVA** estiver habilitado no Evento Financeiro:

* Os lançamentos financeiros gerados terão automaticamente a
  base de cálculo dos impostos preenchida;
* O sistema poderá realizar o cálculo correto dos tributos IBS e CBS;
* As informações de impostos serão gravadas na tabela
  **FTRBLAN**.

## 📌 Regras de Utilização do Campo Compõe IVA

* Eventos financeiros gerados automaticamente para
  **parcelas de aluguel** e **aluguel complementar**
  serão criados com o campo **Compõe IVA** habilitado;
* Eventos financeiros de **aluguel** e **aluguel complementar**
  oriundos do legado terão o campo **Compõe IVA** habilitado automaticamente
  por meio do **atualizador que será executado no momento em que a base for atualizada**;
* Para eventos financeiros **criados manualmente**, o usuário poderá decidir
  se o campo deve ou não ser habilitado, conforme a
  regra tributária aplicável ao tipo de evento.

**⚠️ Observação:**  
A marcação do campo **Compõe IVA** deve sempre seguir a
regra tributária definida para cada tipo de evento financeiro,
garantindo a correta apuração dos impostos e evitando inconsistências fiscais.

**Mais informações sobre Evento Financeiro acesse:**
[TOTVS Construção Gestão de Imóveis - Aluguel - Evento Financeiro - Evento Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=435105273)

]]>
