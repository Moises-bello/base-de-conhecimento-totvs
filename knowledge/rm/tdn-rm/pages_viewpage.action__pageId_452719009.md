---
content_hash: 8a10a514a88b8f44d1a9c89c02f4a8f89fe918850c6a1802f31717e4bc8baa8f
fetched_at: '2026-06-29T00:10:03.108501+00:00'
page_id: '452719009'
product: rm
source: tdn-rm
title: Código de Cálculo 32 - Total Entregue de Vale Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719009
version: 4
---

Base de Cálculo do tipo valor. Este evento deverá estar em chave desativada (Opções | Parâmetros | RM Labore | Outros Parâmetros).   
   
Para considerar os feriados no cálculo os parâmetros "Considera Feriado no Cálculo" no cadastro do horário e "Considera Feriado" no Parametrizador do Funcionário devem estar marcados. Se pelo menos um desses estiver desmarcado o sistema não irá considerar os feriados no cálculo.

O sistema lançará automaticamente ou você poderá informar o valor que a empresa entregou em vales-transporte aos funcionários.

Caso o funcionário utilize "Apenas um vale para todo mês" (Cadastros | Tabelas Auxiliares | Linhas de Vale Transporte), o sistema lançará no evento com código de cálculo 032 – Total Entregue Vale Transporte o valor da tarifa.

O cálculo será feito da seguinte forma:

No. DIAS UTEIS \* somatória (No. PASS. \* VALOR PASSAGEM.)

O sistema buscará o número de viagens informado no cadastro do Funcionário (pasta Vale-Transporte) multiplicado pelo valor da tarifa (cadastro de Linhas de Transporte).

No mês da admissão o sistema verifica os dias trabalhados do funcionário, não considerando o campo dias uteis para o cálculo do Total entregue de vale transporte. Somone nos meses posteriores a admissão é que este campo é verificado.

**Atenção**

Este código não deve ser confundido com o código de cálculo 006 - Vale Transporte. Este último calcula o valor efetivamente a descontar e não o valor entregue.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
