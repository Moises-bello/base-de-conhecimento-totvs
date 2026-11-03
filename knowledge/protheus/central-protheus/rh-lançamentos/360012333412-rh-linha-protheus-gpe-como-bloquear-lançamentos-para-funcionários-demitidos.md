---
article_id: 360012333412
category: RH - Lançamentos
content_hash: da25582d8e8ed2927e7eb65556031b9953fa3fc19d3005c29e11cee9230668c4
fetched_at: '2026-06-28T22:43:31.150436+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como bloquear lançamentos para funcionários demitidos
type: support-article
updated_at: '2025-04-17T17:59:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012333412-RH-Linha-Protheus-GPE-Como-bloquear-lan%C3%A7amentos-para-funcion%C3%A1rios-demitidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26248145888535) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como bloquear lançamentos para funcionários demitidos, seja pelo lançamentos por verba, por funcionário, fixos ou valores variáveis?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O sistema permite que sejam feitos lançamentos para funcionários desligados para agilizar o processo do RH, como por exemplo, para calcular uma rescisão complementar. Ao lançar a verba para o funcionário Demitido e calcular uma Rescisão, o sistema puxa automaticamente esse lançamento para o *grid.*  
  
Para bloquear os lançamentos para funcionários demitidos através das rotinas de **Lançamentos por Funcionário, Lançamentos por Verba, Valores Fixos** e/ou **Valores Futuros** é necessário alterar o parâmetro **MV\_DEMISRC** para **N.** Desta maneira os lançamentos **somente serão permitidos através da rotina de rescisão.**

Para ajuste do parâmetro acesse o **Configurador SIFACFG** em **Ambiente > Cadastros > Parâmetros (CFGX017)**, pesquise pelo parâmetro e configure conforme e necessidade:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31490700707607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31490700710039)  
  
**MV\_DEMISRC = S** o lançamento para funcionários demitidos estará liberado através das rotinas de lançamentos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31490747089175)  
**MV\_DEMISRC = N** o lançamento para funcionários demitidos estará bloqueado através das rotinas de lançamentos.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31490700713239)

Caso seja necessário a **criação do parâmetro**, deve ser feito através do **Configurador**, com **senha de administrador** do Sistema, e incluir as seguintes características:  
  
**Filial**: Em Branco para todas as filiais ou informado código da única filial que terá esta configuração para o parâmetro)  
**Nome da Var**.: MV\_DEMISRC  
**Tipo:** C  
**Conteúdo:** S ou N  
**Descrição:** Permitir a Alteracao ou Inclusao, em Valores Variaveis  
**Cont.Descric:** ou Valores Por Verba, para Funcionarios Demitidos  
**Cont.Descric:** S=Sim, N=Nao.

**Saiba Mais**

[RH - Linha Protheus - GPE - Como controlar as movimentações de Lançamentos Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiQShDSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwNjU2ODU5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb250cm9sYXItYXMtbW92aW1lbnRhJUMzJUE3JUMzJUI1ZXMtZGUtTGFuJUMzJUE3YW1lbnRvcy1WYWxvcmVzLUZ1dHVyb3MGOwhUOg5zZWFyY2hfaWRJIikyMmEwZGQ2OC1lY2IxLTQxNjUtOTg4ZS0wNjY4OTdkZWNlMTYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJImJSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjb250cm9sYXIgYXMgbW92aW1lbnRhw6fDtWVzIGRlIExhbsOnYW1lbnRvcyBWYWxvcmVzIEZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQLrAw%3D%3D--5c52fb5b61f4abd4062bc2af40c38fc84b1bedac)

[RH - Linha Protheus - GPE - Como suspender valores lançados na rotina de Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj877fSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzU1NTQ1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1zdXNwZW5kZXItdmFsb3Jlcy1sYW4lQzMlQTdhZG9zLW5hLXJvdGluYS1kZS1WYWxvcmVzLUZ1dHVyb3MGOwhUOg5zZWFyY2hfaWRJIikyMmEwZGQ2OC1lY2IxLTQxNjUtOTg4ZS0wNjY4OTdkZWNlMTYGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJImJSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjb250cm9sYXIgYXMgbW92aW1lbnRhw6fDtWVzIGRlIExhbsOnYW1lbnRvcyBWYWxvcmVzIEZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQLrAw%3D%3D--d0cea1364dc47f0488c1f9f46c8bb5e5f292877d)

[RH - Linha Protheus - GPE - Relatório Valores Futuros em planilha (GPER570)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgpBd7UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzYwNTY3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUmVsYXQlQzMlQjNyaW8tVmFsb3Jlcy1GdXR1cm9zLWVtLXBsYW5pbGhhLUdQRVI1NzAGOwhUOg5zZWFyY2hfaWRJIik1ZDUyMjNkNy0wMmJjLTQxY2YtODNhNC1kMDcwNzc4NzQ1ZDQGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhR2YWxvcmVzIGZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQI7BA%3D%3D--4b27245a85ed8d99cae6c192bb3941d90bca491d)

[RH - Linha Protheus - GPE - Como visualizar as verbas integradas para folha com a pergunta Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXELvJhQw6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEzNzY4NzU0NjYzNDQ3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLXZpc3VhbGl6YXItYXMtdmVyYmFzLWludGVncmFkYXMtcGFyYS1mb2xoYS1jb20tYS1wZXJndW50YS1WYWxvcmVzLUZ1dHVyb3MGOwhUOg5zZWFyY2hfaWRJIik1ZDUyMjNkNy0wMmJjLTQxY2YtODNhNC1kMDcwNzc4NzQ1ZDQGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhR2YWxvcmVzIGZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQI7BA%3D%3D--93070b4169ffffa249dec21b9e02ae378a29fbe4)

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
