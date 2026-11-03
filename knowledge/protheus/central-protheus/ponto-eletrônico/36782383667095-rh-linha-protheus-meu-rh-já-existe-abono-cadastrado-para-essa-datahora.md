---
article_id: 36782383667095
category: PONTO ELETRÔNICO
content_hash: 7b7071810d2c9a264bdc683331042a1e9b8048bd80d87ecac3a5f71162cf41d7
fetched_at: '2026-06-28T22:44:36.441383+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Já existe abono cadastrado para essa data/hora
type: support-article
updated_at: '2025-12-04T19:50:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36782383667095-RH-Linha-Protheus-Meu-RH-J%C3%A1-existe-abono-cadastrado-para-essa-data-hora
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36782383654807) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao incluir abono é apresentada a mensagem: Já existe abono cadastrado para essa data/hora  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36785083717655)  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Causa**  
O sistema realiza uma validação por meio da função *GetJustification*, que verifica se já existe **abono cadastrado** para o funcionário na data e horário informados. Durante essa validação, são consultadas as tabelas **RH3**/**RH4 e RF0**, caso sejam encontradas informações correspondentes, a mensagem de aviso é apresentada ao usuário.  
  
**Solução**  
Recomenda-se que seja realizada uma verificação, por meio da **Consulta Genérica**, para identificar se existem registros relacionados nas tabelas mencionadas.  
[RH - Linha Protheus - Meu RH - Como emitir um Relatório para acompanhamento das solicitações feitas no App Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXgtCkexE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBwmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE5MjIyNzQzNzc3OTQzLVJILUxpbmhhLVByb3RoZXVzLU1ldS1SSC1Db21vLWVtaXRpci11bS1SZWxhdCVDMyVCM3Jpby1wYXJhLWFjb21wYW5oYW1lbnRvLWRhcy1zb2xpY2l0YSVDMyVBNyVDMyVCNWVzLWZlaXRhcy1uby1BcHAtTWV1LVJIBjsIVDoOc2VhcmNoX2lkSSIpYWZmZTRlZTYtMjdiYy00MTA4LWIzZWYtZDUyNjBiYTE5NjA2BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ5UkggLSBMaW5oYSBQcm90aGV1cyAtIE1ldSBSSCAtIENvbW8gZW1pdGlyIHVtIFJlbGF0w7NyaW8gcGFyYSBhY29tcGFuaGFtZW50byBkYXMgc29saWNpdGHDp8O1ZXMgZmVpdGFzIG5vIEFwcCBNZXUgUkgGOwhUOhJyZXN1bHRzX2NvdW50aQLrAw%3D%3D--e0c7fece4399fc256e8dbfeef772592d73ec12e1)  
  
Para a RF0:  
Acessar no Ponto Eletrônico a rotina em **Atualizações > Cadastro de Funcionários > Pré-Abonos.**  
  
Caso sejam encontradas informações para a data e hora informadas, os registros deverão ser **excluídos** para que o lançamento possa prosseguir corretamente.  
  
**Saiba Mais:**  
[**RH - Linha Protheus - MEU RH - Como incluir manualmente a marcação de Ponto?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050367293)  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
