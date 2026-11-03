---
content_hash: 9d823a888a4672603eb803bb390b447ead67a1d9efb286f91455331824ae8f1e
fetched_at: '2026-06-29T00:11:53.828266+00:00'
page_id: '852299397'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Processo - Apurar Condomínio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852299397
version: 6
---

### Processo de apuração individual do cálculo do condomínio

#### **Visão Geral**

A funcionalidade de apuração é o processo de calcular e distribuir as despesas entre os proprietários ou condôminos de um empreendimento imobiliário ou shopping. Neste processo, é possível apurar de duas maneiras: Considerando todo o empreendimento ou individualmente por loja/unidade.

#### **Funcionamento:**

**Apuração Individual:**Já a apuração individual implica no cálculo do condomínio considerando apenas as subunidades que foram selecionadas pelo usuário durante o processo de configuração ou seleção. Por exemplo, se o gestor escolheu apenas algumas lojas para participar do rateio de determinados custos (como água, limpeza, etc.), a apuração individual reflete apenas os valores associados a essas lojas selecionadas.  
  
**Cálculos a serem apurados:**Esta tela permite realizar os processos para Calcular o Fechamento dos empreendimentos para o módulo de Condomínios. Os itens que são processados neste cálculo são:

* Cobrança Direta
* Reservas
* Consumo (Medições)
* Despesa Financeira
* Orçamento

**Refazer cálculos existentes:** Ao marcar este parâmetro, serão realizados os cálculos selecionados no processo, mesmo que tenham sido processados anteriormente. Quando esse parâmetro não é marcado, o sistema irá processar somente os cálculos ainda não realizados selecionados, mesmo que eles estejam marcados. Esse parâmetro deverá ser utilizado sempre que for necessário refazer o cálculo do fechamento já realizado

Como os cálculos são realizados?  
O sistema verifica a **Data de Competência** informada no **Fechamento** com o período dos cadastros de Cobrança Direta, Reservas, Consumo (Medições), Despesa Financeira e Orçamentos, sendo que o Fechamento e os cadastros citados devem ter o mesmo **Empreendimento**. Por exemplo, se a **Data de Competência** do **Fechamento** é 01/2018, então o sistema irá verificar os cadastros citados anteriormente que foram realizados no período de 01/01/2018 e 31/01/2018.  
Destacamos também que cada um dos itens acima, pode ser calculado de forma separada.

Ao executar esse processo em um Fechamento que está com status "Em Preparação", ele será alterado para "Em Cálculo", onde indicará que pelo menos um dos cálculos foi realizado. O Fechamento estando na situação "Em Cálculo", poderá ser executado o processo de Geração de Lançamento, onde será alterado o status para "Integrado".  
Quando o Fechamento está na situação "Em Cálculo", o processo "Calcular Fechamento" poderá ser executado novamente quantas vezes for necessário.

**Para obter informações dos Cálculos do Fechamento separadamente, clique nos respectivos links abaixo:**

* [Cálculo de Cobrança Direta](https://tdn.totvs.com/pages/viewpage.action?pageId=435104836)
* [Cálculo de Consumo (Medições)](https://tdn.totvs.com/pages/viewpage.action?pageId=435105134)
* [Cálculo de Reservas](https://tdn.totvs.com/pages/viewpage.action?pageId=435105162)
* [Cálculo de Despesas Financeiras](https://tdn.totvs.com/pages/viewpage.action?pageId=435105147)
* [Cálculo de Orçamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105332)
