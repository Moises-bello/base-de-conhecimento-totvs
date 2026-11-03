---
content_hash: 8c62ba36d017a9073d5db5bffaadaf60781f251ce21ccac12ef3785126b487cd
fetched_at: '2026-06-29T00:05:47.145808+00:00'
page_id: '1008212461'
product: rm
source: tdn-rm
title: Serviço de tributos CBS/IBS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008212461
version: 11
---

# 1.**Serviço de dados da regra e de seus tributos CBS/IBS**

1.1. **O que é**

O **Serviço de Tributação CBS/IBS** é um recurso do **TOTVS Gestão Fiscal** responsável por **retornar automaticamente as informações tributárias** associadas a uma regra de tributação.  
Ele permite recuperar dados como:

* CST/Situação tributária
* Classificação tributária
* Percentual de redução de alíquota
* Código e percentual de crédito presumido
* Percentual de diferimento

Essas informações são essenciais para o **preenchimento automático** dos campos correspondentes nos movimentos e itens de movimento, garantindo **padronização e integridade das regras tributárias aplicadas**.

> 🔍 O serviço busca esses dados a partir dos cadastros já existentes na **entidade de Regras Tributárias** e em seu **anexo de tributos**, definidos previamente no sistema.

1.2. **Exemplo**

#### Cadastro da regra e anexo de tributos

No **cadastro de Regra de Tributação**, o usuário define as condições fiscais e associa os tributos correspondentes (CBS/IBS) no **anexo de tributos**.

Tela do sistema

#### Utilização no movimento

Ao incluir um item no movimento:

1. O sistema identifica o produto e carrega os tributos conforme a **parametrização do tipo de movimento**.
2. Ao selecionar a **Regra Tributária**, o sistema utiliza o **Serviço de Tributação CBS/IBS** para preencher automaticamente as informações dos tributos (CBS/IBS) nos campos específicos do item.
3. Os valores são então calculados conforme as definições da regra.

> 💡 Esse processo garante consistência no tratamento tributário, reduz erros manuais e agiliza o cálculo automático de tributos sobre bens e serviços.

Tela do sistema
