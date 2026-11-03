---
article_id: 360015988951
category: RH - 13º salário
content_hash: 9b903fae716c4dafe68d6c06ea9154a2f826f321dda7a9abd571b823e885c514
fetched_at: '2026-06-28T22:44:01.552481+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Quais as principais conferências em caso de inconsistências
  no cálculo da segunda parcela do 13º
type: support-article
updated_at: '2025-08-15T18:59:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015988951-RH-Linha-Protheus-GPE-Quais-as-principais-confer%C3%AAncias-em-caso-de-inconsist%C3%AAncias-no-c%C3%A1lculo-da-segunda-parcela-do-13%C2%BA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29315718613783) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Quais as principais conferências em caso de inconsistências no cálculo da segunda parcela do 13º ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

A princípio verifique se o cálculo da primeira parcela do 13º salário esta correto, após isso verifique outras questões abaixo:

1. Verifique se Existem afastamentos no Ano Corrente para este Funcionário.Acesse: Atualizações / Lançamentos / Ausências (GPEA240).  
Se existir afastamento devemos considerá-lo para o abatimento dos avos, lembrando que os primeiros 15 dias da empresa devem contar como direito do funcionário. E se houver continuações dos afastamentos os mesmos devem estar devidamente cadastrados com sequência e com SIM para continuação.  
  
Exemplo: Funcionário afastado por Doença. Período de 02/02/23 á 15/03/23  
No mês 02 o funcionário possui 1 dia trabalhado + 15 dias pagos pela empresa - Tem direito ao Avo de Fevereiro.  
No mês 03 o funcionário esteve afastado 15 dias, porém trabalhou 15 (16/03 á 30/03) - Tem direito ao Avo de Março.  
  
2. Verifique se há faltas e atrasos no Ano Corrente.  
Acesse: Relatórios / Lançamentos / Ficha Financeira (GPER270) e Imprima uma ficha financeira do ano em questão para identificar a existência de faltas ou atrasos que possam estar deduzindo Avos de direito.  
Abaixo as verbas que são consideradas para abatimento do 13º salário:  
0054 - Desconto de Faltas  
0055 - Desconto de Atrasos  
0203 - Desconto de falta mês anterior  
0242 - Desconto de Faltas (II)  
0243 - Atrasos (II)  
  
3. Verifique se o Funcionário possui admissão no ano corrente.Acesse: Atualizações / Funcionários / Funcionários (GPEA010) e verifique a data de admissão do funcionário (RA\_ADMISSA).  
Se o funcionário possuir admissão dentro do ano os avos de 13º salário podem ser proporcionais;  
Exemplo: Funcionário admitido em 02/02/23;  
Não possui direito aos 12 avos, pois iniciou em fevereiro na empresa. (O funcionário precisa ter pelo menos 15 dias trabalhados no mês para ter direito ao Avo).

4. Verifique a data de referência dos parâmetros de cálculo do 13º salário.  
A data de referência dos parâmetros deve ser sempre o ultimo dia do ano, para que o sistema considere 12 avos completos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18891135750167)

5. Verifique o Percentual de cálculo da 1ª Parcela do 13º salário.  
Acesse Consultas>Cadastros>Acumulados (GPEA120).  
Caso a primeira parcela tenha sido gerada integralmente, no momento da segunda possivelmente será gerado um valor negativo no cálculo da segunda parcela do 13º por conta dos encargos ou não será calculado.

**Saiba Mais:**[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Memória de Cálculo das Médias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiasMjTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNTQzMDU1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTWVtJUMzJUIzcmlhLWRlLUMlQzMlQTFsY3Vsby1kYXMtTSVDMyVBOWRpYXMGOwhUOg5zZWFyY2hfaWRJIik1NzdmNTQxYS03NjllLTRkNjgtYjY1NS05ODY5YTA2MDgxZmUGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIkFSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gTWVtw7NyaWEgZGUgQ8OhbGN1bG8gZGFzIE3DqWRpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--2c637b1ae8fc28b688452e6004a584f742d1d87e)  
[RH - Linha Protheus - GPE - Geração da Memória de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjqkRPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzExNTExNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtR2VyYSVDMyVBNyVDMyVBM28tZGEtTWVtJUMzJUIzcmlhLWRlLUMlQzMlQTFsY3VsbwY7CFQ6DnNlYXJjaF9pZEkiKTJmZjAzODRmLTUxNDYtNDkxMS04ODgzLWI4OGQ5ZjU0MjAzNAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiQlJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBHZXJhw6fDo28gZGEgTWVtw7NyaWEgZGUgQ8OhbGN1bG8GOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--261c01401a9522cb5e139ceb70216518e0cf7afb)  
[RH - Linha Protheus - GPE - Como imprimir relatório de memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZUsrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjMxNDcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pbXByaW1pci1yZWxhdCVDMyVCM3Jpby1kZS1tZW0lQzMlQjNyaWEtZGUtYyVDMyVBMWxjdWxvLWRhcy1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTlkMDc0MjM0LTFiZDMtNGI0NC04NjI2LTRmMzdmOTY0NjVjZQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiXVJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGltcHJpbWlyIHJlbGF0w7NyaW8gZGUgbWVtw7NyaWEgZGUgY8OhbGN1bG8gZGFzIGbDqXJpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--69bc71cdcc2cdbc1c5628944339a857e77c00f94)  
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>**
