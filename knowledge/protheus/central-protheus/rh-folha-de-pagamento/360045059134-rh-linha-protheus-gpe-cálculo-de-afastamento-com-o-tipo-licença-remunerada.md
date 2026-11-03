---
article_id: 360045059134
category: RH - Folha de Pagamento
content_hash: ade9c70b504391a6812db98141f13813ef7a148eea70c2326efc7eaf75e5ef1f
fetched_at: '2026-06-28T22:44:12.036704+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de afastamento com o tipo licença remunerada
type: support-article
updated_at: '2026-03-17T13:45:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045059134-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-afastamento-com-o-tipo-licen%C3%A7a-remunerada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26240657209879) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como calcular um afastamento com o tipo licença remunerada ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para calcular a licença remunerada, é necessário seguir os seguintes passos:  
  
1. Analisar o cadastro da ausência padrão 015 - Licença Remunerada, se está de acordo com necessidade da empresa, ou cadastrar um tipo de afastamento conforme a documentação: [RH - Linha Protheus - GPE - Cadastro tipos de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg%2FO2nTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBe2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyOTE3NDU5MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tdGlwb3MtZGUtYXVzJUMzJUFBbmNpYQY7CFQ6DnNlYXJjaF9pZEkiKWZjMGNlOWVmLTRhMGMtNDlhZi04NmE4LTJhZGJmOWU4YmE4YgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiHmNhZGFzdHJvIHRpcG8gZGUgYXVzZW5jaWEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--a1db4f65d667561375f82343bbb8b0f2b81a3de7)  
  
O campo Tp. Ausência “RCM\_TIPOAF” poderá ser :  
  
**-Afastamento**, neste caso o sistema irá **pedir o motivo campo Motivo** Afast. “RCM\_TPEFD” , os campos para ausências férias, provisão e 13º ficaram habilitados para ajustes conforme necessidade da empresa.   
  
**-Outras ausências**, neste caso as opções para férias e 13º ficaram bloqueadas e o sistema grava automaticamente a informação "**não perde"**.  
  
A verba vinculada no campo Cod. Verba "RCM\_PD"  deverá possuir o ID **0103**.  
A verba de ID 0103 deve ter o campo REF a Férias = Não, caso contrario a verba não será calculada na folha de pagamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39097149356183)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39097149359255)  
  
2. Incluir o afastamento de acordo com a documentação: [RH - Linha Protheus - GPE - Como Lançar Ausências para um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhz5FrSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMTQ1NzY1MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1MYW4lQzMlQTdhci1BdXMlQzMlQUFuY2lhcy1wYXJhLXVtLUZ1bmNpb24lQzMlQTFyaW8GOwhUOg5zZWFyY2hfaWRJIik4YzJiMzFiZS0zNDQzLTRiNGYtOTllNS01ODUzOWMzMTg5ZGMGOwhGOglyYW5raQs6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhbDp2Fuw6dhciBhdXNlbmNpYQY7CFQ6EnJlc3VsdHNfY291bnRpAk8E--b76c463e4c2bbc72b9171327ee10f702beccd2d1) 

3. Calcular a folha de pagamento, onde o sistema irá calcular o saldo de salário proporcional de acordo com o cadastro de ausências e irá lançar a verba informada no tipo de ausências com sua devida proporção.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Campos no cadastro de Tipos de Ausência desabilitados/bloqueados](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXwvXzAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBomh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDY0MzQ0NDgwMjMtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNhbXBvcy1uby1jYWRhc3Ryby1kZS1UaXBvcy1kZS1BdXMlQzMlQUFuY2lhLWRlc2FiaWxpdGFkb3MtYmxvcXVlYWRvcwY7CFQ6DnNlYXJjaF9pZEkiKTZmZjRjZmQ4LTgxOTQtNDYwNy1hZmJhLTVjYTAwOGIyNTIxMgY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFXRpcG8gYWZhc3RhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--d8a0cceae4c4b3f45d2fd999f1d1d2c583ee77e3)  
[RH - Linha Protheus - GPE - Como alterar tipo de afastamento quando solicitado pelo INSS](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiQnHLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMzAxMjExMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1hbHRlcmFyLXRpcG8tZGUtYWZhc3RhbWVudG8tcXVhbmRvLXNvbGljaXRhZG8tcGVsby1JTlNTBjsIVDoOc2VhcmNoX2lkSSIpNmZmNGNmZDgtODE5NC00NjA3LWFmYmEtNWNhMDA4YjI1MjEyBjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVdGlwbyBhZmFzdGFtZW50bwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--0aa7952aa61637fe077ada669970ea81dae26f2f)  
[RH - Linha Protheus - GPE - Como prescrever férias quando o funcionário possui Licença Remunerada](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXA1Q4Ggk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEwMDA4MjE4ODI5NzE5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLXByZXNjcmV2ZXItZiVDMyVBOXJpYXMtcXVhbmRvLW8tZnVuY2lvbiVDMyVBMXJpby1wb3NzdWktTGljZW4lQzMlQTdhLVJlbXVuZXJhZGEGOwhUOg5zZWFyY2hfaWRJIik5NzYxMDQzYS1hYjZhLTRkYjgtYjI1ZS1jZWUyNDZmYjZhYTcGOwhGOglyYW5raQs6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhsaWNlbsOnYSByZW11bmVyYWRhBjsIVDoScmVzdWx0c19jb3VudGkC6QM%3D--d25988f8588ff35f2a9ec3fc04c700edad797d1d)  
[RH - Linha Protheus - GPE - Dias de Licença Remunerada calculados nas férias coletivas não aparecem nos lançamentos de ausência do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiC9B3VUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB7Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1Nzc5NTcxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtRGlhcy1kZS1MaWNlbiVDMyVBN2EtUmVtdW5lcmFkYS1jYWxjdWxhZG9zLW5hcy1mJUMzJUE5cmlhcy1jb2xldGl2YXMtbiVDMyVBM28tYXBhcmVjZW0tbm9zLWxhbiVDMyVBN2FtZW50b3MtZGUtYXVzJUMzJUFBbmNpYS1kby1mdW5jaW9uJUMzJUExcmlvBjsIVDoOc2VhcmNoX2lkSSIpOTc2MTA0M2EtYWI2YS00ZGI4LWIyNWUtY2VlMjQ2ZmI2YWE3BjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYbGljZW7Dp2EgcmVtdW5lcmFkYQY7CFQ6EnJlc3VsdHNfY291bnRpAukD--d5612ea8e91fa1a7dc8461a78fc3713a116b8a9d)
