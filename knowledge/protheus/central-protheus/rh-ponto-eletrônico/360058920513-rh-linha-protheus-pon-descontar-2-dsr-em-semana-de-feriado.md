---
article_id: 360058920513
category: RH - Ponto Eletrônico
content_hash: 8d3fd0cbe347c9ecc55fdf1e066503bd049fe8f48a401c5b2d90ad76a3d5239a
fetched_at: '2026-06-28T22:44:58.310230+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Descontar 2 DSR em semana de feriado
type: support-article
updated_at: '2021-09-17T19:09:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058920513-RH-Linha-Protheus-PON-Descontar-2-DSR-em-semana-de-feriado
---

**Dúvida**Como descontar 2 DSR em semana de feriado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Primeiramente, precisamos ter o cadastro de Feriado feito no Ponto Eletrônico e, que o funcionário tenha o campo Trabalha Feriado na Regra de Apontamento como Não.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096834134/mceclip0.png)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096834174/mceclip1.png)  
  
Após essa configuração, iremos ao cadastro do evento, onde na primeira aba o campo Desc. DSR precisará estar como SIM, neste exemplo, irei trazer o evento de SAÍDA NO EXPEDIENTE.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096834194/mceclip2.png)  
  
Evento de DSR:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099149813/mceclip3.png)  
  
Precisamos ter também, um arredondamento para DSR cadastrado.  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099149853/mceclip4.png)  
  
Por fim, iremos configurar três parâmetros da seguinte maneira:

MV\_DDSRFER = 1  
MV\_LIMDSR = N  
MV\_DSRPROP = N  
  
Veja mais em:  
[Parâmetros que controlam o DSR no módulo SIGAPON](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018605091-MP-PON-Par%C3%A2metros-que-controlam-o-DSR-no-m%C3%B3dulo-SIGAPON)  
  
Com isso, já temos nossa base configurada para o desconto de 2 DSR, caso o funcionário tenha um evento de saída no expediente em semana de feriado.  
  
Veja abaixo que, o feriado do dia 02/11 está cadastrado na base e no dia 05/11, o funcionário teve um evento de 30 minutos de saída no expediente.  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099150133/mceclip5.png)  
  
Assim, realizando o cálculo mensal para este funcionário, teremos além do desconto do evento SAÍDA EXPEDIENTE, dois DSR levando em contato a semana de feriado e o arredondamento cadastrado.  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099150213/mceclip6.png)  
  
Lembrando que, essa configuração é válida com outros eventos de desconto, como FALTA INTEGRAL, ATRASO ou SAÍDA ANTECIPADA.  
Neste exemplo, fiz a configuração com o Saída no Expediente, mas a parametrização é igual para todos os demais.
