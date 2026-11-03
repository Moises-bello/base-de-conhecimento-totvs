---
article_id: 360050726154
category: RH - Férias
content_hash: 27828a6bc5648552ebc58a6e2aca56c647307977d02669d6e22089148ec3b25d
fetched_at: '2026-06-28T22:43:59.297514+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de médias
type: support-article
updated_at: '2025-05-08T19:43:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16105588652183) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como é realizado o Cálculo de Médias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –  A partir da versão 12  
  
**Solução**Hoje existem algumas formas de calcular as médias no sistema e existem diferentes cadastros que podem definir isto, segue abaixo:  
  
- Cadastro de verbas;  
- Cadastro de sindicatos;  
- Mnemônico P\_MEDDIREN  
  
Entendimento básico sobre o cálculo das médias:  
  
**Para férias:**Buscar o período aquisitivo do funcionário;  
Totalizar as médias dos meses;  
Dividir por 12 ou dividir pelos avos de direito.  
  
**Para 13º salário:**Buscar as médias do ano vigente;  
Totalizar as médias do ano vigente;  
Dividir por 12 ou dividir pelos avos de direito.  
  
**Para aviso prévio:**Buscar os últimos 12 meses para o calculo;  
Totalizar as médias;  
Dividir por 12 ou pelos meses proporcionais as médias.

Para aviso prévio soma-­se às verbas dos últimos 12 meses ou da data da admissão à rescisão (na hipótese de empregado com menos de 1 ano de serviço) e divide-se por 12, ou pelo número de meses trabalhados, se inferior, ou o previsto em documento coletivo de trabalho.

a) Empregado com 1 ano e 3 meses de serviço  
­ número de horas extras realizadas nos 12 últimos meses de trabalho .. 480,00  
­ média mensal do número de horas extras (480 : 12) .............................. 40

b) Empregado com menos de 1 ano de serviço  
­ meses trabalhados na empresa .............................................................. 3  
­ nº de horas extras realizadas ................................................................. 96  
­ média mensal do nº de horas extras (96 : 3) ......................................... 32

**Busca de Médias:**  
Para calcular médias o sistema precisa que as verbas que incidem médias estejam devidamente configuradas no cadastro de verbas e sindicato 

**1- Cadastro de verbas**

Aba Médias campos **"Media 13o.", "Media Ferias" e "Med.Av.Prev."**

![](https://totvssuporte.zendesk.com/attachments/token/ygDJfp6BYgdwfYC4SxpvRK4Pn/?name=inline-907192873.png)

**Configuração dos campos:**

* **Preenchimento com "S"-** Informa que a verba será considerada para o respectivo cálculo de média e que a composição das médias irá considerar os últimos meses definidos no cadastro do sindicato do funcionário.
* **Quantidade numérica de meses -** Se informado por exemplo "6", a composição das médias irá considerar os últimos 6 meses.
* **Preenchimento com "SP" no campo "Media Ferias"-** Informa que a verba será considerada para o cálculo de média de férias e que a composição das médias irá considerar os meses do período aquisitivo das férias (Funciona apenas para o campo Médias Férias).

**Observação:**

Cada campo pode possuir uma configuração diferente. Por exemplo, uma verba pode entrar apenas na composição de médias de 13º salário, ou então, uma verba pode ter configuração para ser apurada conforme os 6 últimos meses para 13º salário, enquanto que para férias deve ser apurada conforme os últimos 12 meses.

**Exemplos:**

* **Se definir S / S / S,** o sistema irá olhar o cadastro de sindicatos e verificar se há alguma informação cadastrada.
* **Se definir S / SP / S,** o sistema irá olhar a configuração do sindicato para Média 13º, irá considerar o PERÍODO AQUISITIVO para férias e olhar o cadastro de sindicatos para média de aviso prévio.
* **Se definir S / 12 / 6**, o sistema irá olhar a configuração do sindicato para Média 13º, irá considerar os últimos 12 meses para médias de férias e 6 últimos meses para média de aviso prévio.

**2- Cadastro de sindicatos:**

Na pasta "Media", nos campos "Meses Med 1o", "Meses Med 2o", "Meses Med 3o" e "Meses Med 4o", deve ser informado **quantos meses serão considerados para apuração das médias**, sendo possível haver a configuração para apenas um período ou até 4 períodos.

![](https://totvssuporte.zendesk.com/attachments/token/FiyatIyFEuWYJ8v94V2OjEszl/?name=inline-926475501.png)

**Observação:**

**Não é obrigatório** possuir o preenchimento dos campos "Meses Med 2o", "Meses Med 3o" e "Meses Med 4o" se somente houver**uma configuração de composição de médias.**

Por exemplo, se a convenção coletiva determinar que a composição de médias será efetuada com base nos últimos 12 meses, apenas deve-se preencher o campo "Meses Med 1o" com "12", sem o preenchimento dos demais campos.

Agora, caso a convenção coletiva determine que deve haver a composição de médias com base nos últimos 3, 6, 9 e 12 meses e que seja efetuado o **pagamento da maior média**, então o campo "Meses Med 1o" deve ser preenchido com "3", o campo "Meses Med 2o" deve ser preenchido com "6", o campo "Meses Med 3o" deve ser preenchido com "9" e o campo "Meses Med 4o" deve ser preenchido com "12".

Isso definirá a regra de busca dos valores, **MAS NÃO A REGRA PARA DIVISÃO**.

**Regra de Divisão:**  
A regra de divisão é definido pelo Mnemônico **P\_MEDDIREN**

O mnemônico P\_MEDDIREN, anteriormente utilizado como parâmetro MV\_MEDDIRE, é utilizado como regra de divisão das médias e pode ser configurado de formas diferentes de acordo com a necessidade da empresa.

**Exemplos:**

* **S** - Sim, para que a soma das verbas com incidência para médias seja dividida pela quantidade de meses de direito.
* **N -** Não, para que a soma das verbas com incidência para médias seja dividida por 12 e em seguida multiplicado pelos meses de direito.
* **M** - Misto, para que o mnemônico seja alterado em tempo de execução de acordo com o tipo de contrato do funcionário.
  + Se o tipo de contrato for por tempo indeterminado ou for por tempo determinado e contrato superior a 12 meses, o mnemônico é utilizado como "N".
  + Se o tipo de contrato for por tempo determinado e o contrato igual ou inferior a 12 meses, o mnemônico é utilizado como "S".

**Exemplo:** **P\_MEDDIREN = S**Cadastro da verba = S  
Cadastro de sindicatos = 0  
**Cálculo:** Total das médias / Avos de direito = Valor média

**Exemplo:** **P\_MEDDIREN = N**Cadastro da verba = S  
Cadastro de sindicatos = 0  
**Calculo:** Total Médias (Somatório das verbas com incidência para média) / Meses considerados para média\* = Média

Média / 12 \* Avos de Direito = Valor Média PAGAMENTO.

Ambas as formas estão corretas, quem define como deseja realizar o pagamento é a própria empresa, de acordo com seu acordo coletivo.

**Parametros Específicos:**

* **P\_BUSMEDI** (antigo MV\_BUSMEDI): define o mês inicial de busca das médias.
* **P\_COMISSA** (antigo MV\_COMISSA): define a quantidade de meses que será considerado para a apuração das médias de comissões para funcionários comissionados.
* **P\_DTMDFER** (antigo MV\_DTMDFER): define se será considerado como mês inicial para a composição das médias o período de início das férias ou o período da folha em aberto.
* **P\_M13ANOC** (antigo MV\_M13ANOC): define se a composição de médias de 13º salário apenas irá considerar os meses do ano corrente.
* **P\_MEDORIG** (antigo MV\_MEDORIG): define se será considerado o valor atual da média (mesmo que menor que o original) ou ao menos o valor original (caso o valor atual seja menor).
* **P\_NMESPER** (antigo MV\_NMESPER): define quantos meses será utilizados para o cálculo da médias dentro do período aquisitivo de férias, quando utilizado configuração de apuração de médias sobre o período aquisitivo.
* **P\_REFMED** (antigo MV\_REFMED): define se será utilizado referência diferente para o cálculo das médias no 13º salário.

**Saiba Mais:**

[Utilização do Mnemônico P\_MEDDIREN (Antigo MV\_MEDDIRE)](https://tdn.totvs.com/pages/viewpage.action?pageId=224112471)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de médias para férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXLXHuBgc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzc3MjYzNTE1OTI4NTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZ2VyYXItby1kZW1vbnN0cmF0aXZvLWRlLW0lQzMlQTlkaWFzLXBhcmEtZiVDMyVBOXJpYXMGOwhUOg5zZWFyY2hfaWRJIikwM2FmZTI3ZS02MjJjLTRmNTgtYjk3ZC02NGViY2IzMjgyMTcGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxHUEVSMDgwBjsIVDoScmVzdWx0c19jb3VudGkC7QM%3D--83d730077e25e69719eebcd24557865227a62001)  
[RH - Linha Protheus - GPE - Como imprimir relatório de memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052314713-RH-Linha-Protheus-GPE-Como-imprimir-relat%C3%B3rio-de-mem%C3%B3ria-de-c%C3%A1lculo-das-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Pontos de entrada disponíveis na rotina de Médias - GPEXMED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450454935-RH-Linha-Protheus-GPE-Pontos-de-entrada-dispon%C3%ADveis-na-rotina-de-M%C3%A9dias-GPEXMED)  
[RH - Linha Protheus - GPE - Como demonstrar o salário Incorporado no Relatório de Médias de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgRyX4%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBt2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDg4NTk5MjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZGVtb25zdHJhci1vLXNhbCVDMyVBMXJpby1JbmNvcnBvcmFkby1uby1SZWxhdCVDMyVCM3Jpby1kZS1NJUMzJUE5ZGlhcy1kZS1GJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKWRlNTAzMDU4LWUzNDAtNDg3My1iOGNhLTM0MGE2OTI4ZDg4OQY7CEY6CXJhbmtpDDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFG1lZGlhIGRlIGZlcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--7ecb4b0632203ff6f04a92ac2d408f7a9eaf439d)  
[RH - Linha Protheus - GPE - O que analisar quando o Relatório de Médias de Férias apresenta valor diferente do Cálculo das Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhyxirUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB2mh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0MTg1ODY3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTy1xdWUtYW5hbGlzYXItcXVhbmRvLW8tUmVsYXQlQzMlQjNyaW8tZGUtTSVDMyVBOWRpYXMtZGUtRiVDMyVBOXJpYXMtYXByZXNlbnRhLXZhbG9yLWRpZmVyZW50ZS1kby1DJUMzJUExbGN1bG8tZGFzLUYlQzMlQTlyaWFzBjsIVDoOc2VhcmNoX2lkSSIpYWNiMzZlOWItODllZS00ZmEzLTkxODctMmI0ZTliN2UxMjZiBjsIRjoJcmFua2kOOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIXcmVsYXRvcmlvIGRlIG1lZGlhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--3cade786302b03bdf9aecbfa373dea3227757d5e)

#
