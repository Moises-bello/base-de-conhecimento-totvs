---
content_hash: 1aada1d846bdb5d261445ec2b87ab2a446c793f953f1e7e3e56f4ded9ed6a0fe
fetched_at: '2026-06-29T00:10:02.599669+00:00'
page_id: '452718973'
product: rm
source: tdn-rm
title: Horas Trabalhadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Horas+Trabalhadas
version: 2
---

**Horas Trabalhadas**

**Pagar horas trabalhadas:** Determina se será exportado para o Totvs Folha de Pagamento o número de horas trabalhadas. No cálculo deste valor, o Totvs Automação de Ponto já compensa os atrasos e horas extras, de modo a lançar exatamente o número de horas trabalhadas pelo funcionário no período. Desta maneira, o valor aqui calculado não pode ser lançado no evento horas normais do Totvs Folha de Pagamento e serem também lançados os atrasos e horas extras, pois ocorrerá duplicação de informações, e consequentemente erros no cálculo da folha do funcionário. Este valor é mais utilizado para geração de relatórios no controle de assiduidade dos funcionários.

**Exemplo:**

Um funcionário trabalhou 05:00 horas em um dia, 08:00 horas no dia seguinte, 10:00 horas no próximo e 06:00 horas em outro dia. O sistema irá lançar 29:00 horas no evento Horas Trabalhadas. Observe que, independente do horário do funcionário, este evento já tem implicitamente debitado o total de atraso e somado o total de extras. Por isto, não se deve exportar para a folha de pagamento o evento Horas Trabalhadas como sendo Horas Normais e, ao mesmo tempo, exportar os outros eventos: atrasos, extras, horas abonadas, etc.
