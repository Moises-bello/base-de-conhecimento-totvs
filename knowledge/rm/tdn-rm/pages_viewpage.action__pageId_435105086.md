---
content_hash: 573eda2df5d6495c86d758bb746d84a506c7163c248ccb078e5a226998e85e36
fetched_at: '2026-06-29T00:09:47.847177+00:00'
page_id: '435105086'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Integral - Processo - Calcular Fechamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105086
version: 7
---

Esta tela permite realizar os processos para Calcular o Fechamento dos empreendimentos para o módulo de Condomínios. Os itens que são processados neste cálculo são:

* Cobrança Direta
* Reservas
* Consumo (Medições)
* Despesa Financeira
* Orçamento

**Refazer cálculos existentes:** Ao marcar este parâmetro, serão realizados os cálculos selecionados no processo, mesmo que tenham sido processados anteriormente. Quando esse parâmetro não é marcado, o sistema irá processar somente os cálculos ainda não realizados selecionados, mesmo que eles estejam marcados. Esse parâmetro deverá ser utilizado sempre que for necessário refazer o cálculo do fechamento já realizado

Como os cálculos são realizados? O sistema verifica a **Data de Competência** informada no **Fechamento** com o período dos cadastros de Cobrança Direta, Reservas, Consumo (Medições), Despesa Financeira e Orçamentos, sendo que o Fechamento e os cadastros citados devem ter o mesmo **Empreendimento**. Por exemplo, se a **Data de Competência** do **Fechamento** é 01/2018, então o sistema irá verificar os cadastros citados anteriormente que foram realizados no período de 01/01/2018 e 31/01/2018.Destacamos também que cada um dos itens acima, pode ser calculado de forma separada.

Ao executar esse processo em um Fechamento que está com status "Em Preparação", ele será alterado para "Em Cálculo", onde indicará que pelo menos um dos cálculos foi realizado. O Fechamento estando na situação "Em Cálculo", poderá ser executado o processo de Geração de Lançamento, onde será alterado o status para "Integrado".   
Quando o Fechamento está na situação "Em Cálculo", o processo "Calcular Fechamento" poderá ser executado novamente quantas vezes for necessário.

**Para obter informações dos Cálculos do Fechamento separadamente, clique nos respectivos links abaixo:**
