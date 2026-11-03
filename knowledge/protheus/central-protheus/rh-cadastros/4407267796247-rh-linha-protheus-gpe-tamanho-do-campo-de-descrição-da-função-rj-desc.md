---
article_id: 4407267796247
category: RH - Cadastros
content_hash: b444ee10fd456d04a912c1391dc60e3b4a29671aa1b0f8545a48a4c107b23b7c
fetched_at: '2026-06-28T22:43:25.985044+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Tamanho do campo de Descrição da Função - RJ_DESC
type: support-article
updated_at: '2025-10-31T12:09:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407267796247-RH-Linha-Protheus-GPE-Tamanho-do-campo-de-Descri%C3%A7%C3%A3o-da-Fun%C3%A7%C3%A3o-RJ-DESC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26764363285271)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Tamanho do campo de Descrição da Função - RJ\_DESC  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O tamanho dos campos **R7\_DESCFUN e RJ\_DESC** por **padrão é 20**, pois são campos relacionados, se for necessário alterar os campos, a orientação é sempre que **os dois tenham o mesmo tamanho**, como por exemplo **40 de tamanho.**  
  
Porém, por uma questão de **fontes e impressão em relatórios**, quando executado um **reajuste salarial**, **dissídio** ou **alteração direto pela SRA**, o Sistema só gravará **30 posições** de descrição, mais que 30 posições só será gravado se inserido **um aumento salarial diretamente na rotina GPEA250 - Histórico de Salário,** porém, mesmo assim, pode haver corte de dados nos relatórios.  
  
Na tela abaixo, um exemplo de reajuste de dissídio com data em 26/08/2021 e diretamente pela SRA, com data em 27/08/2021, nas duas opções é gravado somente 30 caracteres de descrição da função, mas se selecionarmos uma seta para baixo, incluindo diretamente pela rotina de Histórico Salarial, as 40 posições são apresentadas.  
  
![](https://totvssuporte.zendesk.com/attachments/token/EXNH92x7HpFv5PagdDBt8T05J/?name=inline-1041331237.png)​  
  
Nossa orientação é sempre no máximo, **estes dois campos estarem com 30**, se for necessário uma função com descrição maior, é orientado abreviar.  
  
Nestes casos, o que indicamos seria a solicitação de uma melhoria via Central Colaborativa TOTVS, para indicar atualização para campo virtual sempre conforme a descrição da SRJ, ou seja, para que exista um update para apagar o que está gravado no campo e gravar novamente com o tamanho completo.  
  
Sobre o campo **R7\_DESCFUN** o mesmo é gravado na tabela SR7 e, apenas aumentando o tamanho do campo, o histórico dos registros não é atualizado, ele somente será atualizado se for modificado **diretamente na rotina** ou seja, através do **Histórico de Salário**, se realizar a alteração pela SRA, **não será gravado os 40**, por este motivo, ao abrir uma alteração de um registro, caso o campo já havia sido preenchido anteriormente através da SRA, **o conteúdo não estará atualizado** e ao criar uma nova linha diretamente na rotina de Histórico Salarial o registro é gravado com a descrição completa.  
  
Veja mais como acessar a Central Colaborativa TOTVS:  
[Central Colaborativa - Como Acessar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039467434-Central-Colaborativa-Como-Acessar)

**Saiba mais**[RH - Linha Protheus - GPE - Cadastro de CBO e Função](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZXtzUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBfmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzQ5NzQzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tZGUtQ0JPLWUtRnVuJUMzJUE3JUMzJUEzbwY7CFQ6DnNlYXJjaF9pZEkiKWJjODMxYmQwLTVhNmItNGViMy1hMmJiLWU0YTJkZTU0OWY3ZAY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDFJKX0RFU0MGOwhUOhJyZXN1bHRzX2NvdW50aQKEBA%3D%3D--8438e77591e3c7c0a9844128962ff57685209619)  
[RH - Linha Protheus - GPE - Cadastro de função](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwieHafUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ9aHR0cHM6Ly9jZW50cmFsZGVhdGVuZGltZW50by50b3R2cy5jb20vaGMvcHQtYnIvYXJ0aWNsZXMvMzYwMDUwMDA3NDU0LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DYWRhc3Ryby1kZS1mdW4lQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpYmM4MzFiZDAtNWE2Yi00ZWIzLWEyYmItZTRhMmRlNTQ5ZjdkBjsIRjoJcmFua2kOOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMUkpfREVTQwY7CFQ6EnJlc3VsdHNfY291bnRpAoQE--b812d8dcdd1d6bf7948f9bf37c242f4df62e5d6e)  
[RH - Linha Protheus - GPE - Local de gravação do conteúdo dos Requisitos das funções - RJ\_MEMOREQ](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj5epQ%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBumh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMTAyODE3MjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUxvY2FsLWRlLWdyYXZhJUMzJUE3JUMzJUEzby1kby1jb250ZSVDMyVCQWRvLWRvcy1SZXF1aXNpdG9zLWRhcy1mdW4lQzMlQTclQzMlQjVlcy1SSi1NRU1PUkVRLQY7CFQ6DnNlYXJjaF9pZEkiKWUxYWVmNjYwLTQ5MmEtNGIyNS1hMWQ1LTM0N2E2Njg4YzAyNgY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDFJKX0RFU0MGOwhUOhJyZXN1bHRzX2NvdW50aQKEBA%3D%3D--37ff6e1bb02758bb41845ece0af099afde4e2b4c)  
[RH - Linha Protheus - GPE - Como gerar um relatório onde consta a relação das funções cadastradas no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiOASPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBxWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1ODEyNjczNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1nZXJhci11bS1yZWxhdCVDMyVCM3Jpby1vbmRlLWNvbnN0YS1hLXJlbGElQzMlQTclQzMlQTNvLWRhcy1mdW4lQzMlQTclQzMlQjVlcy1jYWRhc3RyYWRhcy1uby1zaXN0ZW1hBjsIVDoOc2VhcmNoX2lkSSIpYmM4MzFiZDAtNWE2Yi00ZWIzLWEyYmItZTRhMmRlNTQ5ZjdkBjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMUkpfREVTQwY7CFQ6EnJlc3VsdHNfY291bnRpAoQE--cbf9e07a9dc9250fb806caccccc953a344eeb444)  
[RH - Linha Protheus - GPE - Como gerar um relatório onde consta a relação das funções cadastradas no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiOASPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBxWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1ODEyNjczNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1nZXJhci11bS1yZWxhdCVDMyVCM3Jpby1vbmRlLWNvbnN0YS1hLXJlbGElQzMlQTclQzMlQTNvLWRhcy1mdW4lQzMlQTclQzMlQjVlcy1jYWRhc3RyYWRhcy1uby1zaXN0ZW1hBjsIVDoOc2VhcmNoX2lkSSIpYmM4MzFiZDAtNWE2Yi00ZWIzLWEyYmItZTRhMmRlNTQ5ZjdkBjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMUkpfREVTQwY7CFQ6EnJlc3VsdHNfY291bnRpAoQE--cbf9e07a9dc9250fb806caccccc953a344eeb444)
