---
content_hash: 503f1e5aa41983099ee574aaec2d983ea93d973d5627b0f214c6f1133e005412
fetched_at: '2026-06-29T00:08:40.606730+00:00'
page_id: '286226577'
product: rm
source: tdn-rm
title: Artigo 58-A paragrafo 4 - Regime de tempo parcial - Horas Extras
type: documentation
url: https://tdn.totvs.com/display/LRM/Artigo+58-A+paragrafo+4+-+Regime+de+tempo+parcial+-+Horas+Extras
version: 5
---

# Jornada de Trabalho

|  |  |
| --- | --- |
| **Produto:** | RM Chronus |
| **Versões:** |  |
| **Ocorrência:** | **Artigo 58-Aº-A § 4º**  Art. 58-A. § 4º Na hipótese de o contrato de trabalho em regime de tempo parcial ser estabelecido em número inferior a vinte e seis horas semanais, as horas suplementares a este quantitativo serão consideradas horas extras para fins do pagamento estipulado no § 3º, estando também limitadas a seis horas suplementares semanais. |
| **Ambiente:** | Calculo Horas Extras |
| **Passo a passo:** | De acordo com o Artigo 58-Aº Paragrafo 4º, o sistema irá computar as horas extras realizadas conforme cadastro e não fará controle limitando as horas sumplementares.  Segue exemplo referente parametrização cadastro de um horário com 26 horas semanais.  1º ) Acessar RM Chronus> Cadastros > Horários por intervalo. Foi cadastrado um horário com  com 26 horas semanais.      2º ) Foi associado o horário cadastro  para o funcionário e realizado as  batidas  de forma que ele teve 16:00 horas extras em uma semana. Ao recalcular, foram lançadas essas 16:00 horas para o movimento.      3º ) Após o recalculo, foi realizado  o lançamento dessas horas para a folha de pagamento: Através> Movimento > Lançar para Folha de Pagamento.          4º ) Após efetuar o  processo de lançar  os eventos  para o módulo da Folha de pagamento > Folha Mensal > Consulta movimentação da integração.        5º ) Ao lançar a folha de pagamento pelo menu Folha mensal > Lançamentos > Grupos de eventos, o evento foi incluído no envelope de pagamento do funcionário. |
| **Observações:** | - O RM Chronus não realiza o procedimento. Será realizado de acordo com procedimentos interno das empresas, pois o Chronus trabalha com importação de batidas, e não   tem  como o produto bloquear batidas efetuadas pelos funcionários e nem poderá bloquear. |
