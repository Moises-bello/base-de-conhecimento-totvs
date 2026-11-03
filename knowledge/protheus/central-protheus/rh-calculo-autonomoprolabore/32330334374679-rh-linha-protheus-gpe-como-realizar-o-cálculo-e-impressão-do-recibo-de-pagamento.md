---
article_id: 32330334374679
category: RH - Calculo Autonomo/Prolabore
content_hash: 742aa4befd22a3e7e936e1ea6543dc995302551834a6325da9718774463290f0
fetched_at: '2026-06-28T22:43:15.175893+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar o cálculo e impressão do recibo de
  pagamento de autônomos
type: support-article
updated_at: '2025-09-02T10:49:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32330334374679-RH-Linha-Protheus-GPE-Como-realizar-o-c%C3%A1lculo-e-impress%C3%A3o-do-recibo-de-pagamento-de-aut%C3%B4nomos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32330334352535)** Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cálculo e impressão do recibo de pagamento de autônomos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Versão 12  
  
**Solução**  
Todo Autônomo deverá ser cadastrado na rotina **GPEA265** por não possuírem vínculo empregatício e não seguirem a mesma ordem de matrícula estabelecida para os empregados cadastrados no **GPEA010** - Cadastro de Funcionários.

No menu do **SIGAGPE** em **Atualizações > Funcionários > Contrib. Individual (GPEA265),** o campo  **RA\_INSSSC**= **SIM** e **Desc. INSS deve ficar = S.** Para o campo **RA\_INSSAUT** deve existir preenchimento **apenas** para o cálculo de INSS para **Autônomos.** e no campo categoria, utilizar **A - Autônomo.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331206282903)

![](https://i.imgur.com/O6ZZ5SF.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331185842199)

Verifique também a **Categoria do eSocial** cadastrada para o autônomo. O código deve ser selecionado de acordo com a **atuação** desse autônomo, caso contrário o cálculo ficará incorreto.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32330334353047)  
  
**Obs.:** As informações desta rotina serão armazenadas na tabela **SRA**.  
  
Verifique se existem verbas cadastradas na rotina Cadastro de verbasem **Atualizações > Definições Cálculo > Verbas (GPEA040)** conforme exemplos abaixo (a parametrização de **incidência** de verbas dependerá do **entendimento** de cada cliente, logo, a imagem abaixo serve apenas para **demonstrar** a configuração em base local e geração do desconto da verba de INSS).  
  
Id de cálculo 0218 - Pagamento Autônomo   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331185843223)  
  
Id de cálculo 0064 - INSS  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32371019672983)  
  
Id de cálculo 0148 - INSS Empresa  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331185851543)  
  
Id de cálculo 0167 - Dedução de INSS base IR Folha

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331206288535)  
Id de cálculo 0318 - Salário Base  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331185854999)  
  
Id de cálculo 0015 - Base IR de Salário  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331206290839)  
  
Id de cálculo 0047 - Líquido a Receber  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331206291735)  
  
As informações desta rotina serão armazenadas na tabela **SRV**.  
  
Confirme o cadastro de Período e Processo em**Atualizações > Definições Cálculos > Períodos (GPEA400).**  
Todos os Autônomos devem estar cadastrados no Processo **00003** quando seu pagamento é **mensal** ou **00004** para pagamento **semanal,** que são processos padrões do sistema, pois estes existem para realizar **apenas** os cálculos das Categorias **A** e **P**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32330334356247)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32330304835095)  
  
Para calcular a Folha de pagamento, acesse **Miscelânea > Cálculos > Por Roteiro (GPEM020)** selecione o processo **00003** ou **00004** e informe o Roteiro **AUT**. Clique em **Ok** e **Confirmar.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331206296215)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331185867671)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331185870487)  
  
  
Pra consultar o cálculo individualmente sem gerar o relatório da folha de pagamento, acesse a rotina de Lançamentos por Funcionário em **Atualizações > Lançamentos > Por Funcionário (GPEA580),** clique em **alterar > outras ações > Consultar cálculo.**  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331206300823)  
  
**OBS:** exemplo de calculo de autônomo múltiplos vínculos  
  
Para consultar recibo de pagamento do RPA - Autônomo acesse em **Relatórios > Recibos/Cheques > Recibos Autônomo (GPER1003)**;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331185874327)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331206304407)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331185877143)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32331185878039)

**Saiba Mais**

[RH - Linha Protheus - GPE - Como cadastrar um Autônomo MEI](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg%2BzsXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBf2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNTI0MTUzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWRhc3RyYXItdW0tQXV0JUMzJUI0bm9tby1NRUkGOwhUOg5zZWFyY2hfaWRJIikzMWU1NTBiYy01OGY4LTQ0NGMtOWRmMi03MWNlYjE2ZWMwZjcGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIkBSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjYWRhc3RyYXIgdW0gQXV0w7Rub21vIE1FSQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--402f76a202a9746cc7ca1b1ec69626ca3b47bc4b)

[RH - Linha Protheus - GPE - Como conferir um cálculo de autônomos semanalistas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjpur3UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTQ4OTUxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25mZXJpci11bS1jJUMzJUExbGN1bG8tZGUtYXV0JUMzJUI0bm9tb3Mtc2VtYW5hbGlzdGFzBjsIVDoOc2VhcmNoX2lkSSIpYzk2MTk3YjMtYjk1ZS00NDhhLWFkY2QtZTIzMmU3NmIwZjlhBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJVUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbW8gY29uZmVyaXIgdW0gY8OhbGN1bG8gZGUgYXV0w7Rub21vcyBzZW1hbmFsaXN0YXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--dc19234fc513614864b680f1f93ff56b805ad464)

[RH - Linha Protheus - GPE - Como calcular o novo teto do INSS para pro labore e autônomo](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi281nUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NDk1MDQ1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWxjdWxhci1vLW5vdm8tdGV0by1kby1JTlNTLXBhcmEtcHJvLWxhYm9yZS1lLWF1dCVDMyVCNG5vbW8GOwhUOg5zZWFyY2hfaWRJIikxMzJiMTk3NS1jZjM2LTRiNTUtOTQwZC0zMjY2YTcxZTQ4YjkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIl5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjYWxjdWxhciBvIG5vdm8gdGV0byBkbyBJTlNTIHBhcmEgcHJvIGxhYm9yZSBlIGF1dMO0bm9tbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--8fe30c23d46e7599ec22f4364bb827e7bd74b5e6)

[RH - Linha Protheus - GPE - Como configurar os campos que serão apresentados no cadastro de Autônomos/Contribuinte Individual](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhYc0LSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBx2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwOTg1NTgzMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLW9zLWNhbXBvcy1xdWUtc2VyJUMzJUEzby1hcHJlc2VudGFkb3Mtbm8tY2FkYXN0cm8tZGUtQXV0JUMzJUI0bm9tb3MtQ29udHJpYnVpbnRlLUluZGl2aWR1YWwGOwhUOg5zZWFyY2hfaWRJIik2Y2I4MDlkOC0xYzBhLTQ1ZDMtYjU0Yi1lMDVkNDIxOTgwYzkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgF%2FUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbW8gY29uZmlndXJhciBvcyBjYW1wb3MgcXVlIHNlcsOjbyBhcHJlc2VudGFkb3Mgbm8gY2FkYXN0cm8gZGUgQXV0w7Rub21vcy9Db250cmlidWludGUgSW5kaXZpZHVhbAY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--da823b0ca813e89ff2d86531247cea5afcac7813)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
