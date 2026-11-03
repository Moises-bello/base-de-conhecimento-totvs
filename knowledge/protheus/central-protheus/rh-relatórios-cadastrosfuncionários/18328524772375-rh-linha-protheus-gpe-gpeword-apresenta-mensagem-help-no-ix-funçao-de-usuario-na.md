---
article_id: 18328524772375
category: RH - Relatórios Cadastros/Funcionários
content_hash: 6e68fd17e7a26c0ef67f13fb3e2365e6c4125fe0723bc37c5abd9447e72a4c64
fetched_at: '2026-06-28T22:43:18.431955+00:00'
product: protheus
section_id: 360010843654
source: central-protheus
title: 'RH - Linha Protheus - GPE - GPEWORD apresenta mensagem: HELP NO_IX - Funçao
  de usuario nao esta compilada no repositorio'
type: support-article
updated_at: '2025-07-29T11:48:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18328524772375-RH-Linha-Protheus-GPE-GPEWORD-apresenta-mensagem-HELP-NO-IX-Fun%C3%A7ao-de-usuario-nao-esta-compilada-no-repositorio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18328485729815)** Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**HELP NO\_IX - Funçao de usuario nao esta compilada no repositorio  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução****:**Devido a conversão do Rdmake (GPEWORD) para fonte padrão do módulo (GPER987) é necessário analisar a alteração de item no menu do modulo SIGAGPE seguindo as orientações conforme exemplo abaixo:  
  
1. Entre no módulo SIGACFG:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328061321751)  
  
2. Acesse **Ambiente > Cadastros > Menus:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328040905367)  
  
3. Selecione Gestão de Pessoal e clique o botão OK:![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328508732439)  
  
4. Selecione a pasta Gestão de Pessoal e pressionar o botão **Adicionar >>**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328514560407)

5. Selecione a pasta **Atualizações > Integrações > Word**, e click em **Detalhes**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328103991831)

6. Preencha os campos conforme a imagem abaixo:![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328124255639)

7. Pressione o botão **Gerar** e preencha o campo arquivo como SIGAGPE:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328132252695)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328485735703)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328498040215)

8. No módulo SIGAGPE acesse: **Atualizações > Integrações > Word**  
Clique em Shift+F6 e veja se a chamada do fonte está correta de acordo com o Menu![](https://centraldeatendimento.totvs.com/hc/article_attachments/18328330965143)  
  
Estando correto a chamada do fonte, efetuar o processo normal de geração do Word.  
  
**Saber Mais:**[RH - Linha Protheus - GPE - Configuração para Impressão de Documentos no Word (GPEWORD)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021565472-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-Impress%C3%A3o-de-Documentos-no-Word-GPEWORD-?source=search)  
[RH - Linha Protheus - GPE - Variáveis que podem ser usadas na Integração com o WORD](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh6KJQ%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBo2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMTAyNjA2MDItUkgtTGluaGEtUHJvdGhldXMtR1BFLVZhcmklQzMlQTF2ZWlzLXF1ZS1wb2RlbS1zZXItdXNhZGFzLW5hLUludGVncmElQzMlQTclQzMlQTNvLWNvbS1vLVdPUkQGOwhUOg5zZWFyY2hfaWRJIikwM2Q2MjA5MC1kOWNkLTRiMWMtOTAxMC00MzkzMDdhYWNjYmEGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhNncGV3b3JkIHJkbWFrZQY7CFQ6EnJlc3VsdHNfY291bnRpAnkB--f7ccc2fb1388f09f24b49a041694ea099a333bd0)  
[RH - Linha Protheus - GPE - Como gerar documentos na rotina Imprime Modelos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXXaDGBQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MjI4NTM3NDU5NDMtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZ2VyYXItZG9jdW1lbnRvcy1uYS1yb3RpbmEtSW1wcmltZS1Nb2RlbG9zBjsIVDoOc2VhcmNoX2lkSSIpMDNkNjIwOTAtZDljZC00YjFjLTkwMTAtNDM5MzA3YWFjY2JhBjsIRjoJcmFua2kLOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSITZ3Bld29yZCByZG1ha2UGOwhUOhJyZXN1bHRzX2NvdW50aQJ5AQ%3D%3D--7d40f74e1eb7e5acf19ab15b04228822e91a1e11)  
[RH - Linha Protheus - GPE - Ao gerar a integração com WORD, de várias matrículas, é salvo apenas a última matrícula no arquivo de saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025940474-RH-Linha-Protheus-GPE-Ao-gerar-a-integra%C3%A7%C3%A3o-com-WORD-de-v%C3%A1rias-matr%C3%ADculas-%C3%A9-salvo-apenas-a-%C3%BAltima-matr%C3%ADcula-no-arquivo-de-sa%C3%ADda?source=search)
