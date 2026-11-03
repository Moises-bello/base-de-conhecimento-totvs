---
article_id: 360036164374
category: RH - Férias
content_hash: 263af67ddbd34f863f7854fcf682f38f1af460de291f972178188016f45fe1e2
fetched_at: '2026-06-28T22:43:59.322264+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como retirar a mensagem no Aviso de Férias - A
  remuneração correspondente às férias e, se for o caso ao abono pecuniário e ao adiantamento
  da gratificação
type: support-article
updated_at: '2025-08-07T11:32:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164374-RH-Linha-Protheus-GPE-Como-retirar-a-mensagem-no-Aviso-de-F%C3%A9rias-A-remunera%C3%A7%C3%A3o-correspondente-%C3%A0s-f%C3%A9rias-e-se-for-o-caso-ao-abono-pecuni%C3%A1rio-e-ao-adiantamento-da-gratifica%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34010063386775) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como retirar a mensagem no Aviso de Férias - A remuneração correspondente às férias e, se for o caso ao abono pecuniário e ao adiantamento da gratificação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Existe um parâmetro que determina se a mensagem será impressa ou não.   
Foi criado o parâmetro **MV\_IMPAVF**que permite o usuário escolher se deverá exibir a mensagem de pagamento em caixa no RDMAKE**- IMPFER- Aviso de Férias.**  
O relatório deve possuir os seguintes conteúdos:

**MV\_IMPAVF =1** - Exibe a mensagem:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11441420534679)

**MV\_IMPAVF =2** - Não exibe a mensagem:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11440750938775)

O parâmetro Também é utilizado para o PORTAL RH - na opção de Demonstrativos de Férias.  
  
Caso não tenha o parâmetro na base, pode criá-lo no configurador, usando como base a configuração abaixo: 

|  |  |
| --- | --- |
| **Nome da Variável** | *MV\_IMPAVF* |
| **Tipo** | *C* |
| **Descrição** | *Exibe ou não a mensagem de pagamento do Aviso de Férias* |
| **Valor Padrão** | *1* |

**Saiba mais:**  
[RH - Linha Protheus - GPE - Emissão de aviso e recibo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX%2FmYZYAQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBimh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ4MTA3ODk1NTE2MzktUkgtTGluaGEtUHJvdGhldXMtR1BFLUVtaXNzJUMzJUEzby1kZS1hdmlzby1lLXJlY2liby1kZS1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKWQwMTYzNDQ1LTYwMjktNGNiMi04ZmVjLTQzMGY5NjM2Yjk0OAY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFXJlY2libyBkZSBmZXJpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQIHBg%3D%3D--c6c16068cc6fb8b8f7be71a2c0332919bbc1c019)  
[RH - Linha Protheus - GPE - Recibo de férias com abono](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjp9NjUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBfGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzI3MzgzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUmVjaWJvLWRlLWYlQzMlQTlyaWFzLWNvbS1hYm9uby0GOwhUOg5zZWFyY2hfaWRJIilkMDE2MzQ0NS02MDI5LTRjYjItOGZlYy00MzBmOTYzNmI5NDgGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhVyZWNpYm8gZGUgZmVyaWFzBjsIVDoScmVzdWx0c19jb3VudGkCBwY%3D--c01dad9e79457c18766b33eebdbf46c5671690e2)  
[RH - Linha Protheus - GPE - Rdmake IMPFER](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjSC6jUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJuaHR0cHM6Ly9jZW50cmFsZGVhdGVuZGltZW50by50b3R2cy5jb20vaGMvcHQtYnIvYXJ0aWNsZXMvMzYwMDUwMDY4NDM0LVJILUxpbmhhLVByb3RoZXVzLUdQRS1SZG1ha2UtSU1QRkVSBjsIVDoOc2VhcmNoX2lkSSIpNGZlZTYyZjAtNDU0MS00MmZkLTg0NmItNzlkYjUyNTBiMjgxBjsIRjoJcmFua2kNOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIUYXZpc28gZGUgZmVyaWFzBjsIVDoScmVzdWx0c19jb3VudGkCEgc%3D--8b47d0cdcfebb5b5f6cd4b9908bed3d409cb6a8f)  
[RH - Linha Protheus - GPE - Dados Bancários do Funcionário não aparecem no aviso e recibo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiJszjVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBt2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1OTU0ODU1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtRGFkb3MtQmFuYyVDMyVBMXJpb3MtZG8tRnVuY2lvbiVDMyVBMXJpby1uJUMzJUEzby1hcGFyZWNlbS1uby1hdmlzby1lLXJlY2liby1kZS1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTRmZWU2MmYwLTQ1NDEtNDJmZC04NDZiLTc5ZGI1MjUwYjI4MQY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFGF2aXNvIGRlIGZlcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAhIH--039a772bdf2d123b9d3b7c21942f69711e538b03)
