---
article_id: 360018605091
category: RH - Cadastros
content_hash: 54c3db882bfb7064ed0b2fb70c301b9d2b3c2650944c421cfcd343fc9b28d7f8
fetched_at: '2026-06-28T22:44:53.059277+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Parâmetros que controlam o DSR no módulo SIGAPON
type: support-article
updated_at: '2025-12-29T12:02:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018605091-RH-Linha-Protheus-PON-Par%C3%A2metros-que-controlam-o-DSR-no-m%C3%B3dulo-SIGAPON
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37314053348503)****Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Relação dos parâmetros que controlam o DSR no módulo SIGAPON  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O desconto do DSR conforme cadastro na regra de apontamento, aba Apuração, é Semanal, então a cada falta ou evento que tenha cadastro Desconta DSR = SIM o sistema fará essa contabilização e apontamento do desconto.  
  
Os parâmetros envolvidos são:  
  
**MV\_ARRINTE**  
Define se o Arredondamento de Horas será feito pela parte Decimal das Horas (Padrão, Conteúdo "N") ou pelo total de Horas Integral (Conteúdo "S")   
Documentação para as demais informações de arredondamento:  
[RH - Linha Protheus - PON - Como utilizar o arredondamento do Cálculo das Horas de DSR e das Faltas Utilizando o parâmetro MV\_ARRINTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011378111-RH-Linha-Protheus-PON-Como-utilizar-o-arredondamento-do-C%C3%A1lculo-das-Horas-de-DSR-e-das-Faltas-Utilizando-o-par%C3%A2metro-MV-ARRINTE)  
  
**MV\_DDSRFER**  
Desconta DSR quando o dia for Feriado.  
Conteúdo: 1 = Desconta; 2 = Não desconta  
  
**MV\_DSRPPER**  
Gerar Evento para Desconto de DSR no Próximo Período.  
Conteúdo: S = Gera Evento para Desconto do DSR no Próximo Período  
N = Desconta do Período Atual  
  
**MV\_DSRPROP**  
Desconta o DSR baseado nos Dias Trabalhados.  
Conteúdo: S = Sim; N = Não  
  
**MV\_DSRTAB**  
Efetua a apuração do DSR de feriado com base na quantidade de horas da tabela.  
Conteúdo: .T. = Sim; .F. = Não  
  
**MV\_LIMDSR**  
Desconta o DSR limitado ao período de apuração.  
Conteúdo: S = Sim; N = Não  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Sistema não respeita o cadastro de Arredondamento de DSR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21081126008215-RH-Linha-Protheus-PON-Sistema-n%C3%A3o-respeita-o-cadastro-de-Arredondamento-de-DSR)
