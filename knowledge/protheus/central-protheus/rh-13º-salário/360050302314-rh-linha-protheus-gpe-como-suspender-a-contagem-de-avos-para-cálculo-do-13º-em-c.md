---
article_id: 360050302314
category: RH - 13º salário
content_hash: 929ed33bc3d7683458e10209a53ac86f38daba1ce49b762f79a4b48f50495774
fetched_at: '2026-06-28T22:44:00.728161+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como suspender a contagem de avos para cálculo
  do 13º em casos de afastamento
type: support-article
updated_at: '2025-08-12T19:59:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050302314-RH-Linha-Protheus-GPE-Como-suspender-a-contagem-de-avos-para-c%C3%A1lculo-do-13%C2%BA-em-casos-de-afastamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16635176951959) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como suspender a contagem de avos para cálculo do 13º em casos de afastamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**É possível parametrizar o sistema para que os avos de 13º sejam suspensos em casos de afastamentos.   
Para isso será necessário cadastrar o afastamento através do menu **Tipos de Ausências**.

1. Acesse: **Atualizações/ Definição Cálculo/ Tipos de Ausência,** localize a ausência em questão e clique em **Alterar.**  
  
2. Informe no campo Abat. Avos 13, **Sim** para que os dias de afastamento sejam considerados.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078013573)  
  
3. Preencha o campo Provisão conforme necessidade.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076858994)  
  
4. No campo **Dias Afa 13**, se informarmos 15 (quinze) o sistema irá considerar o abatimento somente se a quantidades de dias de afastamento dentro do mês for maior que 15 dias, conforme legislação.  
Caso entenda que os primeiros 15 dias não devem ser considerados para o abatimento de avos de 13º, temos que deixar o campo RCM\_DIAS13 como 0.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076859434)  
  
5. Após realizar o cadastro do tipo de ausência, será necessário **lançar a ausência** para o funcionário acessando **Atualizações/ Lançamentos/ Ausências**  
  
Nos casos de **afastamentos que sejam sequencias**, será necessário **informar** essa **sequencia** no **lançamento da ausência**. No exemplo abaixo o afastamento 002 faz sequencia com o 001. Essa informação pode mudar, de acordo com a quantidade de afastamentos do funcionário. A sequencia deve ser preenchida de acordo com o código do afastamento que gerou a continuidade.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094820914)  
  
**Caso contrario** o sistema considerará por exemplo, 15 dias pagos pela empresa nos dois afastamentos.

**Saiba Mais**[Avos de 13 salário 1 parcela quando há afastamentos.](https://tdn.totvs.com/pages/viewpage.action?pageId=439697878)  
[RH - Linha Protheus - GPE - Cadastro tipos de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg%2FO2nTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBe2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyOTE3NDU5MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tdGlwb3MtZGUtYXVzJUMzJUFBbmNpYQY7CFQ6DnNlYXJjaF9pZEkiKWY4MDM4MjY3LWI5MGEtNDIzZi05NzZiLTM1MDU5ZjQwMzg0OQY7CEY6CXJhbmtpCjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGWNhZGFzdHJvIGRlIGF1c2VuY2lhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--409d34e59a6a659df2bdea8dc34756f307fe9111)  
[RH - Linha Protheus - GPE - Como Lançar Ausências para um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhz5FrSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMTQ1NzY1MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1MYW4lQzMlQTdhci1BdXMlQzMlQUFuY2lhcy1wYXJhLXVtLUZ1bmNpb24lQzMlQTFyaW8GOwhUOg5zZWFyY2hfaWRJIilkYjJiNmIzYi1hNzJlLTQ2NTktOGRhNi03YWVjNzcyYTI5NjAGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIk1SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBMYW7Dp2FyIEF1c8OqbmNpYXMgcGFyYSB1bSBGdW5jaW9uw6FyaW8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--95bc688dc7ab9a859dea6e3da7d645e6a20e0451)
