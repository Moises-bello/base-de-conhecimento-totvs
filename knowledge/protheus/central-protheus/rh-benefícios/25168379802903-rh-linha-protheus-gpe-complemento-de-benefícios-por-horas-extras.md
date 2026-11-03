---
article_id: 25168379802903
category: RH - Benefícios
content_hash: 6bab8d1c4757a23b04d385fed50ebcf23f6901aa569e5f784472eb3830d47c4b
fetched_at: '2026-06-28T22:44:04.868517+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Complemento de benefícios por horas extras
type: support-article
updated_at: '2025-08-21T20:00:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25168379802903-RH-Linha-Protheus-GPE-Complemento-de-benef%C3%ADcios-por-horas-extras
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25168388176023) Tempo aproximado para leitura: 00:03:00 min****Dúvida**É possível calcular automaticamente o **complemento de benefícios** em decorrência de **horas extras** apontadas no **SIGAPON**?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2210

**Solução**Foi implementada a possibilidade de efetuar o cálculo do **complemento do benefício** (VT/VR/VA), quando o funcionário possuir **horas extras** apontadas no módulo **SIGAPON,** e estiverem previamente definidas na **Tabela Auxiliar S151,** conforme exemplo abaixo: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/25175325251991)**

**Preenchimento dos campos:****- Filial:** Preenchimento não obrigatório;  
**- Cód da CTT:** Preenchimento não obrigatório;  
**- Cód do Sindicato:** Preenchimento não obrigatório;  
**- Tipo do Benefício:** Preenchimento obrigatório, sendo 0=Vale Transporte, 1=Vale Refeição e 2=Vale Alimentação;  
**- Código do Benefício:** Preenchimento não obrigatório;  
**- Tipo do Dia:** Preenchimento obrigatório, sendo S=Trabalhado, C=Compensado, D=DSR, N=Não Trabalhado, F=Feriado;  
**- Qtdade. Min. H.E:** Preenchimento obrigatório, informar as horas no padrão centesimal.

**Atenção:**Antes de realizar o processamento do cálculo complementar, é necessário **concluir o pedido de compra do mês** para que o novo cálculo não sobrescreva o anterior:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25175325255831)

**>Exemplo** de cálculo:

O funcionário realizou **horas extras** em dois dias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25175309296663)

Nos parâmetros de cálculo, a pergunta **Complemento por H.E** deve estar como **Sim:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25175309303447)**

O cálculo foi efetuado com o pagamento de **dois vales adicionais:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25175325278999)

**Saiba Mais**[Documento Técnico - Complemento de benefícios (VA, VR e VT) por horas extras](https://tdn.totvs.com/pages/viewpage.action?pageId=776129138)  
[R](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX%2FdNr4RY6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzI1MTU3NDMyNTA3Nzk5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1SZWMlQzMlQTFsY3Vsby1EaWZlcmVuJUMzJUE3YS1kZS1WYWxlLVRyYW5zcG9ydGUGOwhUOg5zZWFyY2hfaWRJIiljZDU2Mzk2My03MjRkLTQzNmQtODdiZS00NzUxNWU1NDhjOTEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIktSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUmVjw6FsY3VsbyAoRGlmZXJlbsOnYSkgZGUgVmFsZSBUcmFuc3BvcnRlBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--bf505d177e212060cc09cc40cf25053a77183ce5)[H - Linha Protheus - GPE - Recálculo (Diferença) de Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX%2FdNr4RY6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzI1MTU3NDMyNTA3Nzk5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1SZWMlQzMlQTFsY3Vsby1EaWZlcmVuJUMzJUE3YS1kZS1WYWxlLVRyYW5zcG9ydGUGOwhUOg5zZWFyY2hfaWRJIiljZDU2Mzk2My03MjRkLTQzNmQtODdiZS00NzUxNWU1NDhjOTEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIktSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUmVjw6FsY3VsbyAoRGlmZXJlbsOnYSkgZGUgVmFsZSBUcmFuc3BvcnRlBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--bf505d177e212060cc09cc40cf25053a77183ce5)  
[RH - Linha Protheus - GPE - Cálculo e Integração de benefício considerando os dias do próximo período da folha](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX8X5XyQ46D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE2MjU3OTE5MTUyNDA3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZS1JbnRlZ3JhJUMzJUE3JUMzJUEzby1kZS1iZW5lZiVDMyVBRGNpby1jb25zaWRlcmFuZG8tb3MtZGlhcy1kby1wciVDMyVCM3hpbW8tcGVyJUMzJUFEb2RvLWRhLWZvbGhhBjsIVDoOc2VhcmNoX2lkSSIpYmVmYzEwMDctMTc4ZC00NGEzLTk0ZmEtMzJmOWYxZjVlYTAwBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ5UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIEPDoWxjdWxvIGUgSW50ZWdyYcOnw6NvIGRlIGJlbmVmw61jaW8gY29uc2lkZXJhbmRvIG9zIGRpYXMgZG8gcHLDs3hpbW8gcGVyw61vZG8gZGEgZm9saGEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--ee2d8aeb668d1f9d24dd99a02a032e98e9b67a7c)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
