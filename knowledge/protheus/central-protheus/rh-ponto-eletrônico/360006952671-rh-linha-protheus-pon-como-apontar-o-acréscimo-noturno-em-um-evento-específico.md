---
article_id: 360006952671
category: RH - Ponto Eletrônico
content_hash: 487f7e373385d88600bc97e838dee2f1c5acabea4a8af7ce376ede38e439cf06
fetched_at: '2026-06-28T22:44:58.172043+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON -  Como apontar o acréscimo noturno em um evento
  específico 
type: support-article
updated_at: '2025-12-18T18:58:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006952671-RH-Linha-Protheus-PON-Como-apontar-o-acr%C3%A9scimo-noturno-em-um-evento-espec%C3%ADfico
---

**Dúvida**Como apontar o acréscimo noturno em um evento específico?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Cada 52,5 minutos trabalhados durante o horário noturno, correspondem a 01h trabalhada.  
A diferença em minutos - 7,5 minutos, entre a hora noturna e a hora normal, corresponde ao acréscimo noturno, exemplo: um funcionário trabalhou no seguinte horário: das 22h às 05h. Embora ele tenha trabalhado durante 07h, por se tratar do horário noturno, essas horas serão convertidas para horas noturnas como abaixo:  
  
Horas Noturnas convertidas: 08h (420 min / 52,5 \* 60)  
Adicional Noturno: 08h  
  
Com a conversão, chegamos ao total de horas de acréscimo:  
Horas Noturnas convertidas: 08h  
Adicional Noturno: 08h  
Acréscimo Noturno: 01h  
Ou seja, o funcionário trabalhou por 07h, porém, com a conversão para hora noturna, ele ganhou o acréscimo de mais 01h, este total de horas é o que será apresentado em evento específico.  
  
Para isso, siga os passos abaixo:  
1 - acesse Atualizações - Cadastro do Ponto / Eventos, e cadastre o ID de Ponto 037A;  
2 - acesse Atualizações - Cadastros Gerais - Turnos de Trabalho, selecione o Turno que terá este tratamento e na aba Informações Ponto, altere os campos Apenas Ac. No. e Id. Acre. Not. para Sim:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409386003991/mceclip0.png)  
  
Desta maneira, o apontamento irá destacar o acréscimo noturno para o turno configurado em 08h trabalhadas (Dessas 08h, 01h é de acréscimo).  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409391580055/mceclip1.png)  
  
Importante ressaltar que as horas extras noturnas não terão o acréscimo noturno destacado.
