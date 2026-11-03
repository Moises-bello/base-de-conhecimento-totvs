---
article_id: 4409207883287
category: RH - Controle Disciplinas
content_hash: 9e1b2122f6cf3e28b9fddaae3ab3a61e28dcac49c58bb33f60a37d701135f450
fetched_at: '2026-06-28T22:43:10.254237+00:00'
product: protheus
section_id: 360012003633
source: central-protheus
title: 'RH - Linha Protheus - GPE - Na impressão da disciplina ocorre mensagem: \samples\documents\disciplina\modelo.html
  não encontrado no servidor'
type: support-article
updated_at: '2026-06-25T12:56:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409207883287-RH-Linha-Protheus-GPE-Na-impress%C3%A3o-da-disciplina-ocorre-mensagem-samples-documents-disciplina-modelo-html-n%C3%A3o-encontrado-no-servidor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33609288484631) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**No módulo Gestão de Pessoal, na rotina Gestão disciplinar - GPEA643, ao tentar incluir uma Disciplina ou Imprimir o formulário de uma disciplina já cadastrada ocorre mensagem: **\samples\documents\disciplina\modelo.html não encontrado no servidor. O arquivo é necessário para geração do formulário de disciplina  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14446506338327)**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre pois o arquivo modelo.html não foi encontrado no caminho especificado  
  
**Solução**Para solucionar esta ocorrência, realize os seguintes passos:  
  
**1.** Baixe o **arquivo modelo.html,** clicando **[Aqui;](https://tdn.totvs.com/pages/viewpage.action?pageId=393361992)**  
**2.** Verifique se existe o caminho **Protheus\_Data/ Samples/ Documents/ Disciplina** no ambiente, caso não exista, crie exatamente este caminho no servidor. 

**3.** Com o caminho criado e o arquivo modelo.html baixado, coloque-o dentro da pasta Disciplina;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14446592194967)  
  
Após estes passos, a mensagem não ocorrerá mais ao fazer a impressão da Disciplina.  
  
  
  
**Saiba Mais**[RH - Linha Protheus - GPE - Controle Disciplinar](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjq1afUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ1aHR0cHM6Ly9jZW50cmFsZGVhdGVuZGltZW50by50b3R2cy5jb20vaGMvcHQtYnIvYXJ0aWNsZXMvMzYwMDUwMDU0NjM0LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db250cm9sZS1EaXNjaXBsaW5hcgY7CFQ6DnNlYXJjaF9pZEkiKWJmOGQ5MDIxLWQzOTAtNDc1Yi05ODhjLWM4ZjU4MzU0MGU1MwY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDEdQRUE2NDMGOwhUOhJyZXN1bHRzX2NvdW50aQHu--31b6d7eed75de61941d105d110d0a3f27471b1af)  
[RH - Linha Protheus - GPE - Afastamento por motivo disciplinar](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjtpIA%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBf2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDg5ODE3NDEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUFmYXN0YW1lbnRvLXBvci1tb3Rpdm8tZGlzY2lwbGluYXIGOwhUOg5zZWFyY2hfaWRJIiliZjhkOTAyMS1kMzkwLTQ3NWItOTg4Yy1jOGY1ODM1NDBlNTMGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxHUEVBNjQzBjsIVDoScmVzdWx0c19jb3VudGkB7g%3D%3D--7be6d3cde2ea714d2930ff2e93e66d0a5c3e8f90)  
[RH - Linha Protheus - GPE - Alteração do HTML do Controle Disciplinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051018014-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-do-HTML-do-Controle-Disciplinar?source=search)  
[RH - Linha Protheus - GPE - O que verificar quando não imprime a disciplina](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXvP5DAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDM0ODIyNDYyOTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLU8tcXVlLXZlcmlmaWNhci1xdWFuZG8tbiVDMyVBM28taW1wcmltZS1hLWRpc2NpcGxpbmEGOwhUOg5zZWFyY2hfaWRJIiliZjhkOTAyMS1kMzkwLTQ3NWItOTg4Yy1jOGY1ODM1NDBlNTMGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxHUEVBNjQzBjsIVDoScmVzdWx0c19jb3VudGkB7g%3D%3D--9b56aebd30c4862ff85d7f1ddbf918fe91a5db08)  
[RH - Linha Protheus - GPE - Controle Disciplinar - Como imprimir formulário de Disciplina aplicada](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXwjyZAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDkyMDczNDE3MTktUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbnRyb2xlLURpc2NpcGxpbmFyLUNvbW8taW1wcmltaXItZm9ybXVsJUMzJUExcmlvLWRlLURpc2NpcGxpbmEtYXBsaWNhZGEGOwhUOg5zZWFyY2hfaWRJIiliZjhkOTAyMS1kMzkwLTQ3NWItOTg4Yy1jOGY1ODM1NDBlNTMGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxHUEVBNjQzBjsIVDoScmVzdWx0c19jb3VudGkB7g%3D%3D--3e8c1416f9183c0e5ab6c02fa75ba885c310e112)
