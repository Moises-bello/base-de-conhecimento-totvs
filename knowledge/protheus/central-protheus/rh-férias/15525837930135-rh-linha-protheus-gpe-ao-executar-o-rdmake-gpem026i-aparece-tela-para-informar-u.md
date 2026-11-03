---
article_id: 15525837930135
category: RH - Férias
content_hash: 863e2cf518b823cd95fc80142f05fae1a92bb8a9a349d409e9f4f44a222277dc
fetched_at: '2026-06-28T22:43:57.948282+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Ao executar o Rdmake GPEM026I aparece tela para
  informar uma verba de diferença entres os id's 1870 e 0013, quando o MV_DINSSFM
  =N
type: support-article
updated_at: '2023-07-06T14:08:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15525837930135-RH-Linha-Protheus-GPE-Ao-executar-o-Rdmake-GPEM026I-aparece-tela-para-informar-uma-verba-de-diferen%C3%A7a-entres-os-id-s-1870-e-0013-quando-o-MV-DINSSFM-N
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15525796534935) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao executar o Rdmake GPEM026I aparece tela para informar uma verba de diferença entres os id's 1870 e 0013, quando o MV\_DINSSFM =N  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.33  
  
**Solução**Caso o parâmetro MV\_DINSSFM esteja preenchido com N a tela abaixo será apresentada, neste momento deve-se selecionar uma verba em que será gravado o valor da diferença entre o Identificador de cálculo 1870 e 0013.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15525414963223)

A verba selecionada deve estar configurada como tipo **4 - Base Desconto** e **Natureza 9901** e **não ter ID** de cálculo relacionado para que o relatório apresente os valores corretamente.  
  
Exemplo da configuração da verba:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15525507947159)**

Para verificar um exemplo do cálculo, acesse: [Relatório de conferência de INSS do Esocial está incorreto](https://tdn.totvs.com/pages/viewpage.action?pageId=708111796)

**Saiba Mais:**[Rdmake UPDBINFER](https://tdn.totvs.com/display/PROT/DRHROTPRT-6153+DT+Rdmake+UPDBINFER)  
[Ajuste nas Bases INSS Ferias e FGTS no leiaute S-1.0 do eSocial](https://tdn.totvs.com/display/PROT/14477238+DRHCALCPRT-4940+DT+Ajuste+nas+Bases+INSS+Ferias+e+FGTS+no+leiaute+S-1.0+do+eSocial)  
[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_DINSSFM](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhEGKfSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBj2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjQ1MTY1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmlndXJhJUMzJUE3JUMzJUEzby1kby1wYXIlQzMlQTJtZXRyby1NVi1ESU5TU0ZNBjsIVDoOc2VhcmNoX2lkSSIpZjNjNmQyMWQtZWUyYi00NGFhLTgzMDItNGVmYmZlYzZiYTRjBjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPTVZfRElOU1NGTQY7CFQ6EnJlc3VsdHNfY291bnRpAggF--4f7960a4580e3907e99e35490202a2d1319c7acf)   
[RH - Linha Protheus - GPE - Como conferir o calculo do INSS de Férias na folha quando o MV\_DINSSFM=N](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhif7PUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDgxODkxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25mZXJpci1vLWNhbGN1bG8tZG8tSU5TUy1kZS1GJUMzJUE5cmlhcy1uYS1mb2xoYS1xdWFuZG8tby1NVi1ESU5TU0ZNLU4GOwhUOg5zZWFyY2hfaWRJIilmM2M2ZDIxZC1lZTJiLTQ0YWEtODMwMi00ZWZiZmVjNmJhNGMGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg9NVl9ESU5TU0ZNBjsIVDoScmVzdWx0c19jb3VudGkCCAU%3D--a6ce2d8d6d11d597c908b48b59e17d80be4c59b8)  
[RH - Linha Protheus - GPE - eSocial - S-1200 - O INSS, FGTS e IRRF fica incorreto no eSocial (DCTFWEB) quando existe Férias no mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422759630487-RH-Linha-Protheus-GPE-eSocial-S-1200-O-INSS-FGTS-e-IRRF-fica-incorreto-no-eSocial-DCTFWEB-quando-existe-F%C3%A9rias-no-m%C3%AAs?source=search)
