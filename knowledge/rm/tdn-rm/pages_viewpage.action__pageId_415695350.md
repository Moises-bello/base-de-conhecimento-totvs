---
content_hash: 6fa524c782a39810599f6ea17ad65d724d157ed15c2931e8c5a952ff95959b7e
fetched_at: '2026-06-29T00:09:11.658957+00:00'
page_id: '415695350'
product: rm
source: tdn-rm
title: Horários Obrigatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415695350
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Automação de Ponto |
| **Passo a passo:** | Neste módulo, podemos consultar e/ou alterar os horários obrigatórios cadastrados para os funcionários.  O horário obrigatório deve ser cadastrado para o funcionário quando o mesmo deve estar na empresa em um horário determinado, mesmo se este dia for dia de descanso ou compensado. Este horário deve ser cadastrado apenas para funcionários com banco de horas diário por ocorrência.  **Observação:**  Caso o dia do horário obrigatório for cadastrado para um dia de descanso ou compensado do funcionário, as horas extras calculadas para este dia serão de descanso ou de compensado.  Caso o dia do horário obrigatório for cadastrado para um dia de feriado, se houver batida, gera extra de feriado, caso contrário, não é gerado ocorrência de falta.  **Exemplo:**  Se cadastrarmos para o funcionário X os seguintes horários obrigatórios:  No dia 31/03/2018:  Início Fim  1- 14:00 18:00  No dia 01/04/2018   Início Fim  1- 14:00 18:00  No dia 07/04/2018   Início Fim  1- 14:00 18:00    Sabendo-se que os dias 31/03 e 07/04/2018, de acordo com o horário do funcionário, são dias de compensadoe o dia 01/04/2018 é um dia de descanso*.* No movimento do funcionário cadastrar as seguintes batidas:  Para o dia 31/03/2018:  08:00E 12:00S 14:00E 18:00S  Para o dia 01/04/2018:  14:00E 18:00S    O sistema irá apresentar a seguinte movimentação:  31/03/2018 - 04:00 horas extras de compensado.  01/04/2018 - 04:00 horas trabalhadas.  07/04/2018 - 04:00 horas de faltas.        **Observação:**  Caso o funcionário tivesse no dia 01/04/2018 as seguintes batidas: 08:00E 12:00S 14:00E 18:00S o sistema irá calcular 04:00 horas extras de descanso. |
