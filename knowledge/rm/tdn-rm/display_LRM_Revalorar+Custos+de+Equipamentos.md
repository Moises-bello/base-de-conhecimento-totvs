---
content_hash: efa64b4020ad6fffe3069ada6d22f536839d4352f422de2b4b429127f01c022a
fetched_at: '2026-06-29T00:09:16.412642+00:00'
page_id: '421385535'
product: rm
source: tdn-rm
title: Revalorar Custos de Equipamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Revalorar+Custos+de+Equipamentos
version: 2
---

---

Após receber os apontamentos e os custos dos equipamentos vindos do Manutenção de Ativos, deve ser executada a rotina de Apropriar Custos, que funcionará como um processo de revaloração dos custos de equipamentos Através do menu Cadastros| Apropriação de Serviços/Insumos, o usuário acessa a opção Processos | Mobilidade | Revalorar Custos de Equipamentos, seleciona o período para o qual deseja efetuar a revaloração e o sistema efetua validações. Caso sejam encontradas informações inválidas o sistema armazena informações no log, mas não aborta a execução. A revaloração é executada e a rotina atualiza o valor das apropriações existentes. O cálculo do valor da apropriação é realizado da seguinte forma: para cada equipamento calcula-se o valor do Ticket médio acrescido dos custos indiretos. Os custos indiretos serão rateados proporcionalmente, conforme o número de horas de cada frente de trabalho. Será considerada a parametrização de quais custos indiretos devem ser considerados para compor o custo final do equipamento. O valor do Ticket Médio será calculado dividindo-se o custo total pelo volume de horas (produtivas e improdutivas).
