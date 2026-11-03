---
content_hash: 457ad5510c074e355385cec0151829773aae684c02a53e1e81b0f0d9eb4f5f94
fetched_at: '2026-06-29T00:08:10.474762+00:00'
page_id: '240304260'
product: rm
source: tdn-rm
title: Reprogramação Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240304260
version: 1
---

**1º Passo - Parâmetros da Reprogramação.**

* **Período da Reprogramação:** a partir do período informado serão verificadas as atividades alocadas aos professores com vigência dentro deste período.
* **Quebra de Seção:** Informar a quebra ou a seção específica para reprogramação.
* **Seleção de funcionários:** Pode criar filtros, selecionar uma chapa e filtrar a situação/tipo e recebimento do funcionário.

* **Tipo de Reprogramação “Salarial” ou “Eventos Relacionados”:** Marcando o tipo “Salarial”, será apresentado na tela seguinte os parâmetros de reprogramação dos eventos de “Atividades que Compõe Salário” e “Atividades que não Compõe Salário”. Ambos ou apenas um deles poderá ser selecionado.
  + O Tipo de Reprogramação “Eventos Relacionados” estará habilitado apenas se o parâmetro “Reprogramação Salarial detalhada por centro de Custo” estiver marcado em “RH | Folha de Pagamento | Configurações | Integrações | Educacional”. Mais adiante iremos detalhar o funcionamento deste parâmetro.
    - Os eventos relacionados são eventos que poderão ser definidos como adicional de um evento que será reprogramado.  
             Exemplo:  
                          Para o Professor da Turma/Disciplina, A103, esta grupado no TOTVS Folha de Pagamento, o evento de salário 0255. Deverá ser pago ao professor, a título de adicional, um evento de Gratificação.  
                 Desta forma, no TOTVS Folha de Pagamento, no cadastro do evento 0255 deverá ser relacionado, em Anexos | Eventos Relacionados, o evento 0099 – Gratificação e com a fórmula de cálculo. Caso não informe a                      fórmula de cálculo, o valor poderá ser informado manualmente, após a Reprogramação do Evento Relacionado em “RH | Folha de Pagamento | Folha Educacional | Consultas | Composição Salarial”. A reprogramação                do Evento Relacionado deverá ser executado sempre após a Reprogramação Salarial.
* **Histórico Salarial:** A data de mudança e o motivo de mudança devem ser preenchidos para que, na Reprogramação Salarial seja gerado o novo histórico de salário caso os valores da reprogramação salarial e de jornada do mês atual for diferente dos valores reprogramados no mês anterior.

---

**2º Passo** - Opções Reprogramar Atividades que Compõe Salário e Reprogramar Atividades que Não Compõe Salário. É possível realizar a Reprogramação Salarial dos eventos, utilizando cálculo por fórmula. Desta forma, será ignorado os cálculos originais do Salário e da Jornada e serão assumidos os valores obtidos pelas fórmulas, respectivamente para Alteração do Salário e Jornada.

---

**3º Passo** - Selecionar os eventos que serão processados durante a reprogramação. Serão listados todos os eventos que foram associados no Agrupamento Salarial ou na Associação do Grupo de Atividades.

Origem dos Eventos:

---
