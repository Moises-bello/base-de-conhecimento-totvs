---
article_id: 360035659113
category: 'RH - Verbas '
content_hash: 72d48d44be6400b9f140afdd817d657d39e591075cdc681d7601ae384355694d
fetched_at: '2026-06-28T22:43:19.871987+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - Ao cadastrar ou alterar uma verba, aparece uma
  tela de Grupo de Verbas para seleção
type: support-article
updated_at: '2025-07-14T11:46:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035659113-RH-Linha-Protheus-GPE-Ao-cadastrar-ou-alterar-uma-verba-aparece-uma-tela-de-Grupo-de-Verbas-para-sele%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15269225876759) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**No módulo Gestão de Pessoal, ao cadastrar ou alterar uma verba, aparece uma tela de Grupo de Verbas para seleção  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046589333)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de pessoal - A partir da versão 12.1.17  
  
**Causa**Isso ocorre pois existe uma validação incorreta no Modo de Edição do Campo RV\_GRPVERB  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse através do ambiente Configurador o menu: **Base de Dados/ Dicionário/ Base de Dados**;  
2. Busque pela tabela SRV e clique em editar;  
3. Clique no menu "Campos" do lado esquerdo e localize campo **RV\_GRPVERB**;  
4. Clique em editar;  
5. Na aba Opções, limpe o conteúdo do campo Modo de Edição;  
  
![](https://totvssuporte.zendesk.com/attachments/token/GQpDDQhV6j6ZqhFvInObJ8pl3/?name=inline633030271.png)​

6. Clique em salvar;  
7. Clique em confirmar no ícone ![](https://totvssuporte.zendesk.com/attachments/token/JeJRw250IklolLb235GTi4uN2/?name=inline-1811721178.png);  
8. Clique em atualizar Base de Dados, no ícone  ![](https://totvssuporte.zendesk.com/attachments/token/NYOkZLo38IAtBm2eYkDgfkv1E/?name=inline1158847852.png);  
  
9. Aparecerá tela de confirmação de alterações. Clique em avançar e finalizar em seguida;

![](https://totvssuporte.zendesk.com/attachments/token/MPMkp7BmaAHOMlxBa6fWrkdNF/?name=inline116459932.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/2bmlwH6QnJ7sFQxhE03UOvljE/?name=inline-1382893990.png)

​

Ao retornar para ambiente GPE, a mensagem não será mais apresentada ao incluir nova verba.

**Saiba Mais**[RH - Linha Protheus - GPE - Como criar campo no cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgaXJfUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0ODk3NDg3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jcmlhci1jYW1wby1uby1jYWRhc3Ryby1kZS12ZXJiYXMGOwhUOg5zZWFyY2hfaWRJIillOWI4ZjdhNy1jMTg2LTQ1ZTYtYTQ1ZS03NDUzMGJiMmE2YjIGOwhGOglyYW5raQs6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhdjYWRhc3RybyBkZSB2ZXJiYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--d435724bdbac9d1b1fe9c3c42be236af3b83cef1)  
[RH - Linha Protheus - GPE - Como gerar relatório com todo o cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgUPlLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMDg5MDc3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1nZXJhci1yZWxhdCVDMyVCM3Jpby1jb20tdG9kby1vLWNhZGFzdHJvLWRlLXZlcmJhcwY7CFQ6DnNlYXJjaF9pZEkiKWRlODRiNGI5LWJhYzItNDI1YS1hZTVmLWFkNzFkNmM3MjFhOAY7CEY6CXJhbmtpDDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiCFNSVgY7CFQ6EnJlc3VsdHNfY291bnRpaA%3D%3D--259666229cd023f67d79949bbc2abb18e3bd2e0e)  
[RH - Linha Protheus - GPE - Como gerar lista em planilha contendo os códigos e descrições dos identificadores de cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXyLFAlQc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzgzMzc2MTY5MTQ0NTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZ2VyYXItbGlzdGEtZW0tcGxhbmlsaGEtY29udGVuZG8tb3MtYyVDMyVCM2RpZ29zLWUtZGVzY3JpJUMzJUE3JUMzJUI1ZXMtZG9zLWlkZW50aWZpY2Fkb3Jlcy1kZS1jJUMzJUExbGN1bG8GOwhUOg5zZWFyY2hfaWRJIilkZTg0YjRiOS1iYWMyLTQyNWEtYWU1Zi1hZDcxZDZjNzIxYTgGOwhGOglyYW5raQ06C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIghTUlYGOwhUOhJyZXN1bHRzX2NvdW50aWg%3D--9224c3731c57ab6976bc69852559ded7c31c3ba8)
