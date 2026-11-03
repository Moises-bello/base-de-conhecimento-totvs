---
article_id: 360051996134
category: RH - Tipos de Ausências
content_hash: eb3c65b501a35af2722634624a2f46de109b3400d4f21b2d522c02bca7e513e3
fetched_at: '2026-06-28T22:43:21.016536+00:00'
product: protheus
section_id: 360011967353
source: central-protheus
title: RH - Linha Protheus - GPE - Modificações para abatimento de cálculos em casos
  de Ausência na versão 12
type: support-article
updated_at: '2025-08-14T18:26:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051996134-RH-Linha-Protheus-GPE-Modifica%C3%A7%C3%B5es-para-abatimento-de-c%C3%A1lculos-em-casos-de-Aus%C3%AAncia-na-vers%C3%A3o-12
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30045956073239)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Modificações para abatimento de cálculos em casos de Ausência na versão 12  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Recursos Humanos - A partir da versão 12.1.7  
  
**Solução:**Melhoria realizada na versão 12, onde foi criada a rotina Tipos de Ausência para tratar todo tipo de ausência e abatimentos nos cálculos do funcionário como: cálculo dos encargos, abatimento de férias, 13º. Nas versões anteriores, eram utilizados parâmetros para tais configurações.

O cadastro vinculado ao lançamento de Ausências é responsável por conter as definições de parametrizações para o cálculo: 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084759173)

**Alterações:**

* Modificada rotina para tratar **todo tipo** de ausência do funcionário;
* Definições das ausências localizadas em: **Atualizações > Definições de Cálculo > Tipo Ausências** no menu padrão;
* Possui **histórico** dos dias **pagos** pela empresa, saldo a pagar, etc.
* Visualização dos **lançamentos** das ausências em: **Atualizações > Lançamentos > Ausências no menu padrão**.

**Segurança:**

* **Não** é mais permitida a **alteração/exclusão** após **pagamento** do afastamento;
* **Não** é mais permitida a **alteração** de dados de **cálculo/exclusão** de Tipos de Ausências que estão sendo utilizados por funcionários.
* Foi criado o Cadastro de **Tipo de Ausências** para a **configuração** da quantidade de **dias pago pela empresa,** verba que deverá ser calculada para esse pagamento, informação para pagamento de **FGTS, encargos patronais,** informações para **férias, 13º salário, provisão** e códigos para **SEFIP, Homolognet** e **e-Social.**

Desta forma, alguns parâmetros antes utilizados nos cálculos e provisão deixaram de ser usados, como: 

* **MV\_PDCALAC** - Indica se deve abater avos de afastamento para funcionários que se afastaram por Acidente de Trabalho no Ano.
* **MV\_PDCALAD** - Indica se deve abater avos de afastamento para funcionários que se afastaram por Auxílio Doença no Ano.
* **MV\_PDCADOC** - Indica se deve ser cancelada a licença para os funcionários que utilizaram a licença por Adoção.
* **MV\_PFCALAC** - Indica opção de calculo de provisões para funcionário afastado por Acidente de Trabalho.
* **MV\_PFCALAD** - Indica opção de calculo de provisões para funcionário afastado por Aux. Doença.
* **MV\_TCONGAF** - Trata congelamento por período Aquisitivo ou por Afastamento.
* **MV\_TAFAFR** - Trata congelamento por período Aquisitivo ou por Afastamento.
* **MV\_PGSALMA** - Indica se deve pagar o salário maternidade na folha de pagamento.
* **MV\_ABATAFA** - Abatimento dos afastamentos no 13º Salario.
* **MV\_MCOMISS** - Numero de meses utilizados para cálculo da média de comissão paga a funcionárias afastadas por motivo de Licença Gestante.

Tipos de ausência cadastrados no sistema nativamente:

* 001  Férias
* 002  Recesso
* 003  Afastamento Temporário Acidente Trabalho
* 004  Afastamento Temporário por Doença
* 005  Afastamento Temporário para Prestação Serviço Militar
* 006  Afastamento Temporário por Motivo de Licença-Maternidade Pago pela Empresa
* 007  Afastamento Temporário por Motivo de Licença-Maternidade Pago pelo INSS
* 008  Prorrogação do Afastamento Temporário por Motivo de Licença-Maternidade
* 009  Afastamento Temporário por Motivo de Aborto não Criminoso
* 010  Licença-Maternidade Decorrente de Adoção (120 Dias)
* 011  Licença-Maternidade Decorrente de Adoção Criança Entre 1 e 4 Anos (60 Dias)
* 012  Licença-Maternidade Decorrente de Adoção Criança Acima 4 Anos (30 Dias)
* 013  Afastamento Temporário Mandato Sindical
* 014  Licença sem Vencimentos
* 015  Licença Remunerada
* 016  Outros Motivos de Afastamento Temporário
* 017  Aposentadoria por Invalidez
* 018  Mudança por Regime Estatuário

**Importante**  
Na rotina de lançamento de Ausências também foi realizado alguns ajustes, os campos **Continuação de Afastamento Anterior**, **Empresa Paga** e o mnemônico **cLimAuxE15** não serão mais utilizados.

**Saiba Mais**[RH - Linha Protheus - GPE - Quando o funcionário perde direito ao Período Aquisitivo após o retorno do Afastamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwht9CnTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBwWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNTAyNzY5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhbmRvLW8tZnVuY2lvbiVDMyVBMXJpby1wZXJkZS1kaXJlaXRvLWFvLVBlciVDMyVBRG9kby1BcXVpc2l0aXZvLWFwJUMzJUIzcy1vLXJldG9ybm8tZG8tQWZhc3RhbWVudG8GOwhUOg5zZWFyY2hfaWRJIiliMTU4OGExZS1lMmQ0LTRjMTMtOTU4Ni1hNWQwMjA0M2VlMzIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh9Db21vIG8gc2lzdGVtYSBzZSBjb21wb3J0YQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--1aac7d25c2110f681251d4849bcc1661d3025e5b)  
[RH - Linha Protheus - GPE - Como o sistema se comporta quando o afastamento é superior a 15 dias sem data de retorno](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjJgWg%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBumh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDczOTk4ODEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tby1zaXN0ZW1hLXNlLWNvbXBvcnRhLXF1YW5kby1vLWFmYXN0YW1lbnRvLSVDMyVBOS1zdXBlcmlvci1hLTE1LWRpYXMtc2VtLWRhdGEtZGUtcmV0b3JubwY7CFQ6DnNlYXJjaF9pZEkiKWIxNTg4YTFlLWUyZDQtNGMxMy05NTg2LWE1ZDAyMDQzZWUzMgY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiH0NvbW8gbyBzaXN0ZW1hIHNlIGNvbXBvcnRhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--11444870017559232b27892162b988cf8d7c9259)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
