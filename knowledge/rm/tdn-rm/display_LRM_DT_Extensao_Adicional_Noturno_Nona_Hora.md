---
content_hash: be662e483ecdef4eb0ce11eda07d44025860a1e142471b13646025908b8a6436
fetched_at: '2026-06-29T00:06:15.017498+00:00'
page_id: '210051451'
product: rm
source: tdn-rm
title: DT_Extensao_Adicional_Noturno_Nona_Hora
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Extensao_Adicional_Noturno_Nona_Hora
version: 4
---

# EXTENSÃO DE ADICIONAL NOTURNO E NONA HORA

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | | Rotina | Nome Técnico | | --- | --- | | *Parâmetros* | *Cálculo do Ponto* | |
| **Versões/Release:** | *12.1.5* |

## Descrição

Foram implementados dois parâmetros dentro dos Parâmetros do Sindicato para realizar a extensão do adicional noturno.

## Procedimento para Utilização

##### Parâmetro 1 – Considera adicional noturno até o fim da jornada

Ao marcar este parâmetro, o sistema estende o adicional noturno até o fim da jornada do funcionário, caso a mesma tenha interseção com o adicional noturno

Exemplo: Horário Planejado [22:00E 05:00S]  
                 Horário Executado [22:00E 07:00S]  
                 Adicional Noturno [22:00E 05:00s]

Com o parâmetro marcado, será calculado 09:00 de adicional noturno. Caso contrário, será calculado somente 07:00 de adicional noturno.

##### Parâmetro 2 – Para Jornadas iniciadas até xx:xx horas.

Ao incluir o número de horas será definido até quando a jornada pode ser iniciada para obter o adicional noturno estendido. O número de horas deverá estar dentro do intervalo de adicional noturno. Só será editável se o parâmetro considera adicional noturno até o fim da jornada estiver marcado.

Exemplo: Horário Planejado [22:00E 05:00S]  
                 Horário Executado [23:00E 07:00S]  
                 Adicional Noturno [22:00E 05:00s]  
 Para jornadas iniciadas até 22:00 horas

Nesse exemplo não é considerado o adicional noturno estendido, é considerado como adicional noturno somente o intervalo de 22:00 – 05:00 – 07 horas de adicional noturno

Horário Executado [22:00E 07:00S]  
Adicional Noturno [22:00E 05:00s]  
Para jornadas iniciadas até 22:00 horas

Nesse exemplo é considerado o adicional noturno estendido, será considerado adicional noturno o intervalo de 22:00 – 07:00 – 09 horas de adicional noturno
