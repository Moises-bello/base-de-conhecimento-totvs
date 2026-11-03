---
article_id: 360012545432
category: RH - Calculo Autonomo/Prolabore
content_hash: 44a12f8ffc68f15675fd974fb48f33cae000e69907ca1ecb8f5797176a4164f0
fetched_at: '2026-06-28T22:43:15.168130+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar cálculo da folha de pagamento para
  Pró-Labores
type: support-article
updated_at: '2025-05-23T20:39:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012545432-RH-Linha-Protheus-GPE-Como-realizar-c%C3%A1lculo-da-folha-de-pagamento-para-Pr%C3%B3-Labores
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20531840760855)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como realizar o cálculo e impressão do recibo de pagamento de autônomo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Versão 12  
  
**Solução**Todo Pro labore deverá ser cadastrado na rotina **GPEA265** por não possuírem vínculo empregatício e não seguirem a mesma ordem de matrícula estabelecida para os empregados cadastrados no **GPEA010** - Cadastro de Funcionários.

No menu do **SIGAGPE** em **Atualizações > Funcionários > Contrib. Individual (GPEA265),** o campo  **RA\_INSSSC**= **SIM** e **Desc. INSS deve ficar = S.** Para o campo **RA\_INSSAUT** deve existir preenchimento **apenas** para o cálculo de INSS para **Autônomos.** e no campo categoria, utilizar **P- Pro labore** (para o exemplo desta base de conhecimento) ou **A - Autônomo.**  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%209%3A52%3A46.png?version=1&modificationDate=1476964391000&api=v2)  
  
Verifique também a **Categoria do eSocial** cadastrada para o autônomo. O código deve ser selecionado de acordo com a **atuação** desse autônomo, caso contrário o cálculo ficará incorreto.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040168274)  
  
**Obs.:** As informações desta rotina serão armazenadas na tabela **SRA**.  
  
Verifique se existem verbas cadastradas na rotina Cadastro de verbasem **Atualizações > Definições Cálculo > Verbas (GPEA040)** conforme exemplos abaixo (a parametrização de **incidência** de verbas dependerá do **entendimento** de cada cliente, logo, a imagem abaixo serve apenas para **demonstrar** a configuração em base local e geração do desconto da verba de INSS).  
  
Id de cálculo 0217 - Pagamento Pró-Labore  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%209%3A57%3A54.png?version=1&modificationDate=1476964698000&api=v2)  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%209%3A58%3A55.png?version=1&modificationDate=1476964760000&api=v2)  
  
Id de cálculo 0067 - INSS  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A0%3A38.png?version=1&modificationDate=1476964863000&api=v2)  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A1%3A6.png?version=1&modificationDate=1476964891000&api=v2)  
  
Id de cálculo 0148 - INSS Empresa  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A1%3A42.png?version=1&modificationDate=1476964927000&api=v2)  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A1%3A56.png?version=1&modificationDate=1476964941000&api=v2)  
  
Id de cálculo 0167 - Dedução de INSS base IR Folha  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A2%3A41.png?version=1&modificationDate=1476964986000&api=v2)  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A2%3A59.png?version=1&modificationDate=1476965004000&api=v2)  
  
Id de cálculo 0318 - Salário Base  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A4%3A3.png?version=1&modificationDate=1476965068000&api=v2)  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A4%3A25.png?version=1&modificationDate=1476965090000&api=v2)  
  
Id de cálculo 0015 - Base IR de Salário  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A4%3A47.png?version=1&modificationDate=1476965112000&api=v2)  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A5%3A1.png?version=1&modificationDate=1476965126000&api=v2)  
  
Id de cálculo 0047 - Líquido a Receber  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A10%3A17.png?version=1&modificationDate=1476965441000&api=v2)  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A10%3A37.png?version=1&modificationDate=1476965462000&api=v2)  
As informações desta rotina serão armazenadas na tabela **SRV**.  
  
Confirme o cadastro de Período e Processo em**Atualizações > Definições Cálculos > Períodos (GPEA400).**  
Todos os Prolaboristas  devem estar cadastrados no Processo **00003** quando seu pagamento é **mensal** ou **00004** para pagamento **semanal,** que são processos padrões do sistema, pois estes existem para realizar **apenas** os cálculos das Categorias **A** e **P**.  
  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%209%3A43%3A6.png?version=1&modificationDate=1476963811000&api=v2)  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%209%3A43%3A43.png?version=1&modificationDate=1476963848000&api=v2)  
As informações desta rotina serão armazenadas nas tabelas **RCF, RFQ, RCH, RCG**.  
  
Para calcular a Folha de pagamento, acesse **Miscelânea > Cálculos > Por Roteiro (GPEM020)** selecione o processo **00003** ou **00004** e informe o Roteiro **AUT**. Clique em **Ok** e **Confirmar.**  
  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%2010%3A13%3A33.png?version=1&modificationDate=1476965638000&api=v2)  
As informações desta rotina serão armazenadas na tabela **SRC**.  
  
Pra consultar o cálculo individualmente sem gerar o relatório da folha de pagamento, acesse a rotina de Lançamentos por Funcionário em **Atualizações > Lançamentos > Por Funcionário (GPEA580),** clique em **alterar > outras ações > Consultar cálculo.**  
![](http://tdn.totvs.com/download/attachments/267805060/image2016-10-20%209%3A50%3A7.png?version=1&modificationDate=1476964231000&api=v2)  
 **Resumo do cálculo:****Verba 073:**1.000,00 conforme o campo RA\_SALARIO do cadastro de Autônomo/Pró-labore.  
**Verba 515:**1.000,00 (verba 073) X 11% (Conforme legislação Pró-labore/Autônomo, sempre será a alíquota de 11%)= 110,00.  
**Verba A06:** 1.000,00 (verba 073) - 110,00 (verba 515)= 890,00.  
**Verba A14:**1.000,00 (verba 073) - 110,00 (verba 515)= 890,00.  
**Verba A048:**1.000,00 (verba 073) X 20% (Conforme legislação Pró-labore/Autônomo, sempre será a alíquota de 11% referente a parte empresa)= 200,00.  
**Verba A53:** 110,00 (verba 515) valor que será levado para a DIRF.  
**Verba A70**: 1.000,00 (verba 073 serve de base de cálculo para a verba de INSS).  
**Verba B39:**1.000,00 (verba 073 serve de base de cálculo para o cálculo das demais verbas).  
  
Impressão do recibo de pagamento de Pró Labore: [RH - Linha protheus - GPE - Impressão de recibo de pagamento para Pro Labore](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9860164140311-RH-Linha-Protheus-GPE-Impress%C3%A3o-de-recibo-de-pagamento-para-Pro-Labore)

**Saiba Mais**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)

[RH - Linha Protheus - GPE - Como cadastrar um Autônomo MEI](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg%2BzsXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBf2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNTI0MTUzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWRhc3RyYXItdW0tQXV0JUMzJUI0bm9tby1NRUkGOwhUOg5zZWFyY2hfaWRJIikzMWU1NTBiYy01OGY4LTQ0NGMtOWRmMi03MWNlYjE2ZWMwZjcGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIkBSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjYWRhc3RyYXIgdW0gQXV0w7Rub21vIE1FSQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--402f76a202a9746cc7ca1b1ec69626ca3b47bc4b)

[RH - Linha Protheus - GPE - Como conferir um cálculo de autônomos semanalistas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjpur3UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTQ4OTUxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25mZXJpci11bS1jJUMzJUExbGN1bG8tZGUtYXV0JUMzJUI0bm9tb3Mtc2VtYW5hbGlzdGFzBjsIVDoOc2VhcmNoX2lkSSIpYzk2MTk3YjMtYjk1ZS00NDhhLWFkY2QtZTIzMmU3NmIwZjlhBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJVUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbW8gY29uZmVyaXIgdW0gY8OhbGN1bG8gZGUgYXV0w7Rub21vcyBzZW1hbmFsaXN0YXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--dc19234fc513614864b680f1f93ff56b805ad464)

[RH - Linha Protheus - GPE - Como calcular o novo teto do INSS para pro labore e autônomo](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi281nUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NDk1MDQ1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWxjdWxhci1vLW5vdm8tdGV0by1kby1JTlNTLXBhcmEtcHJvLWxhYm9yZS1lLWF1dCVDMyVCNG5vbW8GOwhUOg5zZWFyY2hfaWRJIikxMzJiMTk3NS1jZjM2LTRiNTUtOTQwZC0zMjY2YTcxZTQ4YjkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIl5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjYWxjdWxhciBvIG5vdm8gdGV0byBkbyBJTlNTIHBhcmEgcHJvIGxhYm9yZSBlIGF1dMO0bm9tbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--8fe30c23d46e7599ec22f4364bb827e7bd74b5e6)

[RH - Linha Protheus - GPE - Como configurar os campos que serão apresentados no cadastro de Autônomos/Contribuinte Individual](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhYc0LSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBx2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwOTg1NTgzMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLW9zLWNhbXBvcy1xdWUtc2VyJUMzJUEzby1hcHJlc2VudGFkb3Mtbm8tY2FkYXN0cm8tZGUtQXV0JUMzJUI0bm9tb3MtQ29udHJpYnVpbnRlLUluZGl2aWR1YWwGOwhUOg5zZWFyY2hfaWRJIik2Y2I4MDlkOC0xYzBhLTQ1ZDMtYjU0Yi1lMDVkNDIxOTgwYzkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgF%2FUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbW8gY29uZmlndXJhciBvcyBjYW1wb3MgcXVlIHNlcsOjbyBhcHJlc2VudGFkb3Mgbm8gY2FkYXN0cm8gZGUgQXV0w7Rub21vcy9Db250cmlidWludGUgSW5kaXZpZHVhbAY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--da823b0ca813e89ff2d86531247cea5afcac7813)
