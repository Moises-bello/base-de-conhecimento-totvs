---
article_id: 18915115305879
category: MDT - Atendimento Médico
content_hash: faed1aaf4873a065e837512fcf900d21331be004689fead6d9f91bae24792125
fetched_at: '2026-06-28T22:44:20.547309+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Como cadastrar Atestado Médico para funcionários
  com horário noturno
type: support-article
updated_at: '2025-08-14T19:06:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18915115305879-RH-Linha-Protheus-MDT-Como-cadastrar-Atestado-M%C3%A9dico-para-funcion%C3%A1rios-com-hor%C3%A1rio-noturno
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18915093640599)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como Cadastrar Atestado Médico para Funcionários com horário Noturno?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Ao realizar a o cadastramento de um Atestado Médico (MDTA685) no módulo de Medicina e Segurança do Trabalho (SIGAMDT), para um funcionário com turno Noturno deve ser observado que o atestado esteja abrangendo todo o período de trabalho do funcionário assim caracterizando 1 (um) dia de trabalho.  
O parâmetro **MV\_NG2IPON** deverá estar com o conteúdo igual a 1 para que o cadastro da sequência de turno possa ser configurada.  
  
**Exemplo**:

1. Cadastramento do Turno **001 na sequência 001: 8h as 12h e das 13h as 17h. (horário Normal)**
2. Cadastramento do Turno **001 na sequência 002: 22h as 2h e das 3h as 5h. (horário Noturno)**
3. Através da rotina Tabela de Horário Padrão no modulo de Ponto Eletrônico (**SIGAPON**) é determinado o horário do funcionário.

**Observação:** Se tiver duvidas no cadastro de turno para procurar a equipe do SIGAPON

Para lançar o atestado acesse: **SIGAMDT>Atualizações>Atendimento médico>Atestado médico**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18915122938647)

**Importante:** O funcionário está atualmente cadastrado no turno **Noturno**onde o campo de **Turno Trab. (RA\_TNOTRAB**) está preenchido como **001** e o campo **Seq. Ini. Turn. (RA\_SEQTURN)** está preenchido como **002**.

**Atestado 1: Onde o campo de Dias Afast. (TNY\_QTDIAS) = 0**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18915115241623)**

Lançar um atestado médico com a data **Inic. Afast.(TNY\_DTINIC) = 08/11/2023** com **Hora Inic.(TNY\_HRINIC) = 12h e****Data Fim** **(TNY\_DTFIM)= 09/11/2023 com Hora Fim(TNY\_HRFIM) = 4h**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18915106319767)**

**Atestado 2: Onde o campo de Dias Afast. (TNY\_QTDIAS) = 1**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18915122946455)**

Lançar um atestado médico com a data **Inic. Afast.(TNY\_DTINIC) = 08/11/2023** com **Hora Inic.(TNY\_HRINIC) = 12h e****Data Fim** **(TNY\_DTFIM)= 09/11/2023 com Hora Fim(TNY\_HRFIM) = 4h**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18915122946455)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18921076176535)**

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho)  
[RH - Linha Protheus - MDT - Quais as principais documentações sobre a rotina Atestado Médico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415329074583-RH-Linha-Protheus-MDT-Quais-as-principais-documenta%C3%A7%C3%B5es-sobre-a-rotina-Atestado-M%C3%A9dico)
