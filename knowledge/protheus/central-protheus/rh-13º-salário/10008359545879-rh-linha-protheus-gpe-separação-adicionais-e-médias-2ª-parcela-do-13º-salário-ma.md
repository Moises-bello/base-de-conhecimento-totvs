---
article_id: 10008359545879
category: RH - 13º salário
content_hash: ce8efcc0003ff28c61fb487e4a2f33b2c68e7e2e846593766f8e888fca4f41a8
fetched_at: '2026-06-28T22:44:01.610653+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Separação Adicionais e Médias 2ª Parcela do 13º
  Salário Maternidade (Criação IDs de cálculo 1434 ao 1447 e IDs 1651 a 1652)
type: support-article
updated_at: '2025-07-25T19:34:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10008359545879-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-Adicionais-e-M%C3%A9dias-2%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-Maternidade-Cria%C3%A7%C3%A3o-IDs-de-c%C3%A1lculo-1434-ao-1447-e-IDs-1651-a-1652
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17677133436695) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**Sistema não efetua a separação do valor de 13º salário adquirido no período da licença maternidade.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Devido a isso, a geração dos valores das rubricas **4051** (Valor correspondente ao 13° salário pago pelo contratante ou órgão público, no período de licença maternidade), **5001** (Valor relativo ao 13° salário de trabalhador, inclusive as médias de 13° salário (horas extras, adicional noturno, etc.), exceto se relativo à primeira parcela ou se pago em rescisão contratual - nessa opção devem ser classificadas também o valor pago mensalmente ao trabalhador avulso, a título de 13° salário) e **6002** (Valor correspondente ao 13° salário proporcional pago na rescisão do contrato de trabalho, exceto o pago sobre o aviso-prévio indenizado) ficam incorretas.  
  
**Solução**Ajuste nos cálculos de 13º salário (roteiros **131** e **132**) para separar os valores de 13º salário adquiridos no período da licença maternidade. Dessa forma, houve a necessidade de criação dos Ids abaixo:  
  
**A criação dos ID's é obrigatória.**- **ID de cálculo 1434** - 1ª Parc. 13º Sal. Maternidade: irá conter o valor da 1ª parcela do 13 salário relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar a configuração da verba de ID de cálculo 0022;

- **ID de cálculo1435** - Parcela Final 13º Sal Maternidade: irá conter o valor da 2ª parcela do 13 salário relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1436** - Total de Medias em Valor Maternidade: irá conter o valor da média em valor do 13º salário relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1437** - Total de Medias em Horas Maternidade: irá conter o valor da média em horas do 13º salário relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1438** -ATS 13. Salário Maternidade: irá conter o valor do adicional por tempo de serviço relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1439** - ATS 13. Salário sobre verbas Maternidade: irá conter o valor do adicional por tempo de serviço sobre verbas relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1440** - Periculosidade 13. Salario Maternidade: irá conter o valor do adicional de periculosidade relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1441** - Periculosidade 13. Salario sobre verbas Maternidade: irá conter o valor do adicional de periculosidade sobre verbas relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1442** - Insalubridade 13. Salario Maternidade: irá conter o valor do adicional de insalubridade relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1443** - Insalubridade 13. Salario sobre verbas Maternidade: irá conter o valor do adicional de insalubridade sobre verbas relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1444** - Adicional Cargo de Confiança 13.Salário Maternidade: irá conter o valor do adicional por cargo de confiança relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1445** - Adicional Transferencia 13.Salário Maternidade: irá conter o valor do adicional por transferência relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1446** - 13º na Indenizacao Rescisao Maternidade: irá conter o valor do 13º salário indenizado pago na rescisão relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0114;

- **ID de cálculo1447** - Media 13º Salario Rescisao Maternidade: irá conter o valor da média do 13º salário indenizado pago na rescisão relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0251.

- **ID de cálculo1651** - Pagto Peric. Sobre Medias 13o. Sal. Maternidade: irá conter o valor da periculosidade sobre médias relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;

- **ID de cálculo1652** - Pagto Insal. Sobre Medias 13o. Sal. Maternidade: irá conter o valor da insalubridade sobre médias relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0024;  
  
**Saiba Mais:**[RH - Linha Protheus - GPE - Primeira parcela do 13º com licença](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg5C7TUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDg1NDcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUHJpbWVpcmEtcGFyY2VsYS1kby0xMyVDMiVCQS1jb20tbGljZW4lQzMlQTdhLW1hdGVybmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpMjFjMmQ2ZmQtNjFjYy00NmQ4LTllMWItZDRmMmNkYzBlOTE1BjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVMTPCuiBtYXRlcm5pZGFkZQY7CFQ6EnJlc3VsdHNfY291bnRpAvkD--d3dbee49fa66ac0ec58589d63da30f8df8706a63) [maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg5C7TUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDg1NDcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUHJpbWVpcmEtcGFyY2VsYS1kby0xMyVDMiVCQS1jb20tbGljZW4lQzMlQTdhLW1hdGVybmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpMjFjMmQ2ZmQtNjFjYy00NmQ4LTllMWItZDRmMmNkYzBlOTE1BjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVMTPCuiBtYXRlcm5pZGFkZQY7CFQ6EnJlc3VsdHNfY291bnRpAvkD--d3dbee49fa66ac0ec58589d63da30f8df8706a63)  
[RH - Linha Protheus - GPE - Como o Sistema calcula a referência de 13º salário da Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgNsDrVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBuWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1OTY3ODczMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1vLVNpc3RlbWEtY2FsY3VsYS1hLXJlZmVyJUMzJUFBbmNpYS1kZS0xMyVDMiVCQS1zYWwlQzMlQTFyaW8tZGEtTGljZW4lQzMlQTdhLU1hdGVybmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpMjFjMmQ2ZmQtNjFjYy00NmQ4LTllMWItZDRmMmNkYzBlOTE1BjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVMTPCuiBtYXRlcm5pZGFkZQY7CFQ6EnJlc3VsdHNfY291bnRpAvkD--d982260f3e73c4046a932e67ea476e544a826f9d)  
[RH - Linha Protheus - GPE - Separação Adicionais e Médias 1ª Parcela do 13º Salário Maternidade (Criação IDs de cálculo 1639 ao 1648 e IDs 1653 a 1654)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhgpsXSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSICAwFodHRwczovL2NlbnRyYWxkZWF0ZW5kaW1lbnRvLnRvdHZzLmNvbS9oYy9wdC1ici9hcnRpY2xlcy8zNjAwMTg0NTQxMTItUkgtTGluaGEtUHJvdGhldXMtR1BFLVNlcGFyYSVDMyVBNyVDMyVBM28tQWRpY2lvbmFpcy1lLU0lQzMlQTlkaWFzLTElQzIlQUEtUGFyY2VsYS1kby0xMyVDMiVCQS1TYWwlQzMlQTFyaW8tTWF0ZXJuaWRhZGUtQ3JpYSVDMyVBNyVDMyVBM28tSURzLWRlLWMlQzMlQTFsY3Vsby0xNjM5LWFvLTE2NDgtZS1JRHMtMTY1My1hLTE2NTQtBjsIVDoOc2VhcmNoX2lkSSIpYWIyMzMyMTctNmU2YS00MWFhLWE2NmYtYjZmZWNiNmJmMmNjBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBn1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBTZXBhcmHDp8OjbyBBZGljaW9uYWlzIGUgTcOpZGlhcyAxwqogUGFyY2VsYSBkbyAxM8K6IFNhbMOhcmlvIE1hdGVybmlkYWRlIChDcmlhw6fDo28gSURzIGRlIGPDoWxjdWxvIDE2MzkgYW8gMTY0OCBlIElEcyAxNjUzIGEgMTY1NAY7CFQ6EnJlc3VsdHNfY291bnRpAtEE--a3230a4a7fbeee2fcbec1a54a37c1af23c287839)

Para informações sobre a separação dos valores de 13º salário adquiridos durante a licença maternidade, consultar a documentação a seguir: <http://tdn.totvs.com/pages/viewpage.action?pageId=351386320>

Para informações sobre a separação dos valores da 1ª parcela do 13º salário, consultar a documentação a seguir: <http://tdn.totvs.com/pages/viewpage.action?pageId=403745443>

#
