---
article_id: 360059188613
category: RH - 13º salário
content_hash: 7312e104422e41da155f112a260a383fe42be0ff4a0fbba0363ceea01950fea8
fetched_at: '2026-06-28T22:44:00.438732+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo da contribuição Assistencial para o roteiro
  132 - 2ª parcela do 13º
type: support-article
updated_at: '2026-06-25T11:32:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188613-RH-Linha-Protheus-GPE-C%C3%A1lculo-da-contribui%C3%A7%C3%A3o-Assistencial-para-o-roteiro-132-2%C2%AA-parcela-do-13%C2%BA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17900510083735)** Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Cálculo da contribuição Assistencial para o roteiro 132 (2ª parcela do 13º).  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Alguns sindicatos determinam que a **Contribuição Assistencial** seja descontada também sobre a **2º Parcela do 13º Salário**. Desta forma, para atender a esses casos, foi realizada uma implementação que permitirá realizar o cálculo da contribuição Assistencial no roteiro de cálculo 132.  
  
**O Desconto ocorrerá no ID 0069 - Contribuição Assistencial**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41478337498775)

Para que esse cálculo seja possível foi criado o mnemônico:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097201374)   
  
Nele deve ser definida as **verbas que irão compor a base de cálculo da contribuição Assistencial** para o seu respectivo roteiro, sendo o mnemônico **P\_VCASS132**utilizado no cálculo da 2ª Parcela do 13º Salário.

Se a base de cálculo for composta pelo valor de **uma única verba**, por exemplo, com o código 001, ela deve ser informada da seguinte maneira: **"001"**. Caso haja mais de uma verba, cada código deve ser separado por vírgulas. Exemplo: Se a base de cálculo for composta pelas verbas 001, 002, 003, 004 e 005, o mnemônico deve ser informado da seguinte maneira: **"001,002,003,004,005"**

**Observação:** as regras de cálculo são aquelas existentes no **cadastro do Sindicato**, que são as mesmas regras utilizadas no cálculo da contribuição Assistencial na Folha de Pagamento.

## Procedimento para Utilização

Exemplo:

Informar em cada Mnemônico as verbas que irão compor a base de cálculo

1. No Gestão de Pessoal (SIGAGPE), acesse Atualizações / Definições de Cálculo / Mnemônicos (GPEA300), posicione no mnemônico **P\_VCASS132**clique no botão Alterar e informe as verbas que irão compor a base de cálculo na 2º Parcela do 13º Salário entre " " (aspas duplas e separe com (,) **virgula** caso indique mais de uma verba)  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10937851352855)

 2.  No Gestão de Pessoal (SIGAGPE), acesse Atualizações / Definições de Cálculo / Roteiros (GPEA160), posicione no roteiro **132** - Cálculo da 2ª Parcela do 13º Salário - e clique no botão alterar.  Localize a linha "**CALCULO BASE E INSS DE 13º**" que possui a fórmula "**S\_INSS13()**", que no roteiro padrão está na sequencia 00430. Como a contribuição Assistencial será calculada imediatamente antes dos impostos, então devemos incluir uma nova linha na sequencia 00429, com as seguintes informações:

"Seq. Calculo" (RM\_SEQ)  = **00429**  
"Descrição" (RM\_DESCRIC)  = **Contribuição Assistencial no 13º Salario**  
"Fórmula" (RM\_FORMULA)  = **S\_CONASSIS()**  
"Habilitado" (RM\_HABILIT)  = **Sim**       
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10937936953751)

**Observação:** nesse exemplo, a contribuição será calculada antes dos impostos, por isso, foi cadastrada na sequencia 00429. Mas se alguma outra verba vier a ver utilizada talvez seja necessário informar uma outra sequencia. É preciso avaliar cada caso específico.

3. Realize o cálculo da 2ª Parcela do 13º Salário e verifique se a contribuição Assistencial foi calculada corretamente conforme a base de cálculo definida, e de acordo com os percentuais informados no Sindicato.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10948216298263)

No exemplo acima no cadastro do Sindicato, aba Assistencial, foi parametrizado 1% sobre Salario Base

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10948221266711)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como cadastrar contribuição assistencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052024613-RH-Linha-Protheus-GPE-Como-cadastrar-contribui%C3%A7%C3%A3o-assistencial-?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXpNm%2FAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4NTUxNTczOTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZGEtMSVDMiVBQS1wYXJjZWxhLWRvLTEzLVNhbCVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKWRjYWI1MmQ5LWRiZmUtNDZjZC1iNDZjLTFiMjJhNGZkMmNiNgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkid1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBRdWFpcyBzw6NvIGFzIGRvY3VtZW50YcOnw7VlcyByZWxhY2lvbmFkYXMgYW8gY8OhbGN1bG8gZGEgMcKqIHBhcmNlbGEgZG8gMTPCsCBTYWzDoXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAscH--c91422874fbccbf85ee395b48199f1b147e1039e)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do Décimo Terceiro](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXmUm%2BAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4Mjg5NDAwNTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRvcy1hby1jJUMzJUExbGN1bG8tZGEtMiVDMiVBQS1wYXJjZWxhLWRvLUQlQzMlQTljaW1vLVRlcmNlaXJvBjsIVDoOc2VhcmNoX2lkSSIpNjBhNTkyMDUtMmVjNS00YmMwLWE1MGUtNDU2N2EyMTM1OWQ5BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ6UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIFF1YWlzIHPDo28gYXMgZG9jdW1lbnRhw6fDtWVzIHJlbGFjaW9uYWRvcyBhbyBjw6FsY3VsbyBkYSAywqogcGFyY2VsYSBkbyBEw6ljaW1vIFRlcmNlaXJvBjsIVDoScmVzdWx0c19jb3VudGkCpQc%3D--88d76e207d08b7b01ec6773ce36d8ac13ccc4711)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXkGzzAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA3MjA0MjM5NTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZG8tY29tcGxlbWVudG8tZGUtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIillN2I1MjRkYi01MDkxLTQyOGQtYTk2NC0zMTcyYmVmZTg4MzUGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIm5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUXVhaXMgc8OjbyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGFvIGPDoWxjdWxvIGRvIGNvbXBsZW1lbnRvIGRlIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--2e656483d6bae129abcc17c08bc1cd4ef2f221a1)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
