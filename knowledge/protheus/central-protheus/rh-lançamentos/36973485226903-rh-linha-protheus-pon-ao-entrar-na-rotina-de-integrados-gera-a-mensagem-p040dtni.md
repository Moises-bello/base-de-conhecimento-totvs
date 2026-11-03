---
article_id: 36973485226903
category: RH - Lançamentos
content_hash: 9737bfab80d780f769d5aafe3a5ae98f725815d07367e70b4e86e10c3a03737e
fetched_at: '2026-06-28T22:44:46.748276+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: 'RH - Linha Protheus - PON -  Ao entrar na rotina de integrados gera a mensagem:
  P040DTNIL "A data não pode ficar em branco ou já existir para este funcionário",
  e posteriormente gera error log'
type: support-article
updated_at: '2026-02-03T13:30:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36973485226903-RH-Linha-Protheus-PON-Ao-entrar-na-rotina-de-integrados-gera-a-mensagem-P040DTNIL-A-data-n%C3%A3o-pode-ficar-em-branco-ou-j%C3%A1-existir-para-este-funcion%C3%A1rio-e-posteriormente-gera-error-log
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36973501763095) Tempo aproximado para leitura: **01:00:00 min**  
  
**Dúvida**  
Ao entrar na rotina de integrados (PONA280) gera a mensagem: **P040DTNIL "A data não pode ficar em branco ou já existir ára este funcionário"**, e posteriormente gera *error log*: ***Transform*****(*****Self*****:aCOLS[Iif( Len(** ***Self*****:aCOLS ) >=** ***Self*****:o*****Browse*****:nAt,** ***Self*****:o*****Browse*****:nAt,** ***Len*****( Self:aCOLS ) )][25],*****Trim*****(*****Self*****:a*****Header*****[25][3]))}(APLIB170.PRW)**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973501763607)**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para correção, será necessário verificar as propriedades dos campos no padrão, conforme abaixo:  
No **Configurador (SIGACFG)**, acesse o dicionário de dados em **Base de Dados > Dicionário > Base de Dados**, abra o dicionário da empresa e filtre as tabelas **SP8 e SPC:**  
Garanta que os campos estejam conforme o padrão abaixo:

**P8\_DATA:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973501764759)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973501767575)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973485197719)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973501769239)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973485198999)  
  
**PC\_DATA**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973501771415)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973501773463)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973501774871)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973485204247)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36973501776023)  
  
**Saiba mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
