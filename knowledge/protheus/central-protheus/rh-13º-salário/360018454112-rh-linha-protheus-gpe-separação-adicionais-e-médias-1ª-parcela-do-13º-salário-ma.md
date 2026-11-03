---
article_id: 360018454112
category: RH - 13º salário
content_hash: f7d899f3d84b00bee5b5e79da1012085f51f4f39077baa87e8f91c3ce82b4586
fetched_at: '2026-06-28T22:44:01.604185+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Separação Adicionais e Médias 1ª Parcela do 13º
  Salário Maternidade (Criação IDs de cálculo 1639 ao 1648 e IDs 1653 a 1654)
type: support-article
updated_at: '2025-07-25T19:35:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454112-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-Adicionais-e-M%C3%A9dias-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-Maternidade-Cria%C3%A7%C3%A3o-IDs-de-c%C3%A1lculo-1639-ao-1648-e-IDs-1653-a-1654
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17686930999319) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**No módulo Gestão de Pessoal, sistema não efetua a separação do valor da 1ª parcela do 13º salário adquiridos durante a licença maternidade, gerando o cálculo nas mesmas verbas que são geradas na 2ª parcela do 13º salário.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Sistema não efetua a separação do valor da 1ª parcela do 13º salário adquiridos durante a licença maternidade, gerando o cálculo nas mesmas verbas que são geradas na 2ª parcela do 13º salário.

O correto seria ter outras verbas pois a 1ª parcela não possui tributação de INSS e IRRF.  
  
**Solução**Ajuste no cálculo da 1ª parcela 13º salário (roteiro 131) para separar os valores de 13º salário adquiridos durante a licença maternidade relativos a 1ª parcela. Dessa forma, houve a necessidade de criação dos IDs abaixo.   
**A criação dos ID's é obrigatória.**

- **ID de cálculo 1639** - Total de Medias em Valor Maternidade 1ª Parc: irá conter o valor da média em valor do 13º salário relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo 1640** - Total de Medias em Horas Maternidade 1ª Parc: irá conter o valor da média em horas do 13º salário relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo 1641** - ATS 13. Salário Maternidade 1ª Parc: irá conter o valor do adicional por tempo de serviço relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo 1642** - ATS 13. Salário sobre verbas Maternidade 1ª Parc: irá conter o valor do adicional por tempo de serviço sobre verbas relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo 1643** - Periculosidade 13. Salario Maternidade 1ª Parc: irá conter o valor do adicional de periculosidade relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo 1644** - Periculosidade 13. Salario sobre verbas Maternidade 1ª Parc: irá conter o valor do adicional de periculosidade sobre verbas relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo 1645** - Insalubridade 13. Salario Maternidade 1ª Parc: irá conter o valor do adicional de insalubridade relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo 1646** - Insalubridade 13. Salario sobre verbas Maternidade 1ª Parc: irá conter o valor do adicional de insalubridade sobre verbas relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo 1647** - Adicional Cargo de Confiança 13.Salário Maternidade 1ª Parc: irá conter o valor do adicional por cargo de confiança relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo 1648** - Adicional Transferência 13.Salário Maternidade 1ª Parc: irá conter o valor do adicional por transferência relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo1653** - Pagto Peric. Sobre Medias 13o. Sal. Maternidade 1ª Parc.: irá conter o valor da periculosidade sobre médias relativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

- **ID de cálculo1654** - Pagto Insal. Sobre Medias 13o. Sal. Maternidade 1ª Parc.: irá conter o valorda insalubridade sobre médiasrelativo aos avos adquiridos durante a licença maternidade. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo 0022;

**Importante**Também foi disponibilizado o ***rdmake* UPDVB131** que irá efetuar o processamento de todos os funcionários conforme filtro definido na geração (filial, matrícula e período de/até) para atualizar a tabela de histórico SRD, campo RD\_PD, com a execução da instrução *UPDATE*, efetuando um de/para conforme a tabela abaixo:

| ID origem | Descrição | ID destino | Descrição |
| --- | --- | --- | --- |
| 1445 | Adicional Transferência 13.Salário Maternidade | 1648 | Adicional Transferência 13.Salário Maternidade 1ª Parc. |
| 1444 | Adicional Cargo de Confiança 13.Salário Maternidade | 1647 | Adicional Cargo de Confiança 13.Salário Maternidade 1ª Parc. |
| 1443 | Insalubridade 13. Salario sobre verbas Maternidade | 1646 | Insalubridade 13. Salario sobre verbas Maternidade 1ª Parc. |
| 1442 | Insalubridade 13. Salario Maternidade | 1645 | Insalubridade 13. Salario Maternidade 1ª Parc. |
| 1441 | Periculosidade 13. Salario sobre verbas Maternidade | 1644 | Periculosidade 13. Salario sobre verbas Maternidade 1ª Parc. |
| 1440 | Periculosidade 13. Salario Maternidade | 1643 | Periculosidade 13. Salario Maternidade 1ª Parc. |
| 1439 | ATS 13. Salário sobre verbas Maternidade | 1642 | ATS 13. Salário sobre verbas Maternidade 1ª Parc. |
| 1438 | ATS 13. Salário Maternidade | 1641 | ATS 13. Salário Maternidade 1ª Parc. |
| 1437 | Total de Medias em Horas Maternidade | 1640 | Total de Medias em Horas Maternidade 1ª Parc. |
| 1436 | Total de Medias em Valor Maternidade | 1639 | Total de Medias em Valor Maternidade 1ª Parc. |

Exemplo de atualização:  
  
Antes da atualização:

| RD\_PD | ID | Desc |
| --- | --- | --- |
| A13 | 1440 | Periculosidade 13. Salario Maternidade |
| A98 | 1436 | Total de Medias em Valor Maternidade |
| A99 | 1437 | Total de Medias em Horas Maternidade |

Após a atualização:

| RD\_PD | ID | Desc |
| --- | --- | --- |
| C13 | 1643 | Periculosidade 13. Salario Maternidade 1ª Parc. |
| C98 | 1639 | Total de Medias em Valor Maternidade 1ª Parc. |
| C99 | 1640 | Total de Medias em Horas Maternidade 1ª Parc. |

  

**Para a utilização da rotina, deverá ser efetuado a inclusão manual no menu do módulo SIGAGPE, cadastrando o item como função de usuário.**

**Ao término do processamento, o *log* de ocorrências irá listar os funcionários que foram verificados.**

**Aviso**O *rdmake***somente** deverá ser executado se já foi efetuado o cálculo da 1ª parcela do 13º salário pois efetua atualização do histórico de movimentos.

O *rdmake***NÃO** atualiza valores, referência e/ou outras informações dos registros nem cria registros; apenas irá alterar o código da verba (campo RD\_PD) dos registros existentes.  
  
Para baixo o *rdmake* **UPDVB131** acesse o link : <https://tdn.totvs.com/pages/viewpage.action?pageId=527388984>

**Saiba Mais:**[RH - Linha Protheus - GPE - Primeira parcela do 13º com licença](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg5C7TUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDg1NDcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUHJpbWVpcmEtcGFyY2VsYS1kby0xMyVDMiVCQS1jb20tbGljZW4lQzMlQTdhLW1hdGVybmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpMjFjMmQ2ZmQtNjFjYy00NmQ4LTllMWItZDRmMmNkYzBlOTE1BjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVMTPCuiBtYXRlcm5pZGFkZQY7CFQ6EnJlc3VsdHNfY291bnRpAvkD--d3dbee49fa66ac0ec58589d63da30f8df8706a63) [maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg5C7TUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDg1NDcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUHJpbWVpcmEtcGFyY2VsYS1kby0xMyVDMiVCQS1jb20tbGljZW4lQzMlQTdhLW1hdGVybmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpMjFjMmQ2ZmQtNjFjYy00NmQ4LTllMWItZDRmMmNkYzBlOTE1BjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVMTPCuiBtYXRlcm5pZGFkZQY7CFQ6EnJlc3VsdHNfY291bnRpAvkD--d3dbee49fa66ac0ec58589d63da30f8df8706a63)[RH - Linha Protheus - GPE - Como o Sistema calcula a referência de 13º salário da Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgNsDrVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBuWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1OTY3ODczMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1vLVNpc3RlbWEtY2FsY3VsYS1hLXJlZmVyJUMzJUFBbmNpYS1kZS0xMyVDMiVCQS1zYWwlQzMlQTFyaW8tZGEtTGljZW4lQzMlQTdhLU1hdGVybmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpMjFjMmQ2ZmQtNjFjYy00NmQ4LTllMWItZDRmMmNkYzBlOTE1BjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVMTPCuiBtYXRlcm5pZGFkZQY7CFQ6EnJlc3VsdHNfY291bnRpAvkD--d982260f3e73c4046a932e67ea476e544a826f9d)  
[RH - Linha Protheus - GPE - Separação Adicionais e Médias 2ª Parcela do 13º Salário Maternidade (Criação IDs de cálculo 1434 ao 1447 e IDs 1651 a 1652)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXLLdAGgk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSICBQFodHRwczovL2NlbnRyYWxkZWF0ZW5kaW1lbnRvLnRvdHZzLmNvbS9oYy9wdC1ici9hcnRpY2xlcy8xMDAwODM1OTU0NTg3OS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtU2VwYXJhJUMzJUE3JUMzJUEzby1BZGljaW9uYWlzLWUtTSVDMyVBOWRpYXMtMiVDMiVBQS1QYXJjZWxhLWRvLTEzJUMyJUJBLVNhbCVDMyVBMXJpby1NYXRlcm5pZGFkZS1DcmlhJUMzJUE3JUMzJUEzby1JRHMtZGUtYyVDMyVBMWxjdWxvLTE0MzQtYW8tMTQ0Ny1lLUlEcy0xNjUxLWEtMTY1Mi0GOwhUOg5zZWFyY2hfaWRJIilkN2IzNTQ3OS04NDg1LTRjMmUtODYzNS05YmFiMDNlODNiZGYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgGgUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIFNlcGFyYcOnw6NvIEFkaWNpb25haXMgZSBNw6lkaWFzIDLCqiBQYXJjZWxhIGRvIDEzwrogU2Fsw6FyaW8gTWF0ZXJuaWRhZGUgKENyaWHDp8OjbyBJRHMgZGUgY8OhbGN1bG8gMTQzNCBhbyAxNDQ3IGUgSURzIDE2NTEgYSAxNjUyKQY7CFQ6EnJlc3VsdHNfY291bnRpAtAE--7e6ef3a8eea02fa6adfca2b19bb5fcf5bdd82cf1)

Para informações sobre a separação dos valores de 13º salário adquiridos durante a licença maternidade, consultar a documentação a seguir: <http://tdn.totvs.com/pages/viewpage.action?pageId=351386320>

Para informações sobre a separação dos valores da 1ª parcela do 13º salário, consultar a documentação a seguir: <http://tdn.totvs.com/pages/viewpage.action?pageId=403745443>
