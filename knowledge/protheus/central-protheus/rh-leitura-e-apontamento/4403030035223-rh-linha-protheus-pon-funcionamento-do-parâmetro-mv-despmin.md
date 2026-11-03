---
article_id: 4403030035223
category: RH - Leitura e Apontamento
content_hash: f07d9260bf48ffc82b53c8243f4ceb0fdc66e64d6800940beb07c8bf26726916
fetched_at: '2026-06-28T22:44:45.951569+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Funcionamento do Parâmetro MV_DESPMIN
type: support-article
updated_at: '2025-10-03T19:08:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403030035223-RH-Linha-Protheus-PON-Funcionamento-do-Par%C3%A2metro-MV-DESPMIN
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35393333689623) Tempo aproximado para leitura: 00:01:00 min******Dúvida**Para que serve, e como funciona o parâmetro **MV\_DESPMIN?**  
  
**Ambiente**TOTVS RH - TOTVS RH (linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O parâmetro **MV\_DESPMIN** é utilizado no Ponto Eletrônico para definir uma quantidade de **minutos** que serão utilizados para **desprezar marcações em horários dentro do intervalo definido.**  
Para acessar o parâmetro, entre no **Configurador (SIGACFG)** e siga o caminho: **Ambiente > Cadastros > Parâmetros**. Em seguida, filtre e edite o parâmetro **MV\_DESPMIN**.  
Realize o ajuste necessário. A sugestão é que o parâmetro esteja configurado com, **no mínimo 05 minutos de intervalo**: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/20682364728215)**  
O sistema vai considerar apenas uma marcação feita dentro deste intervalo, por exemplo:  
Se o parâmetro for definido com **05** e o funcionário realizar marcações às **15h31** e **outra às 15h32**, o sistema manterá apenas a primeira e desprezará a segunda.  
  
Importante ressaltar que as marcações desprezadas serão **lidas e gravadas na tabela SP8** - Marcações, por se tratarem de registros originais que devem estar disponíveis para eventuais fiscalizações trabalhistas, porém, essas marcações não serão apontadas e ficarão como **Rejeição Automática** conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20682326556567)

****Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**[RH - Linha Protheus - PON - Ao realizar a leitura e apontamento, as marcações de um ou mais funcionários aparecem em duplicidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007611772-RH-Linha-Protheus-PON-Ao-realizar-a-leitura-e-apontamento-as-marca%C3%A7%C3%B5es-de-um-ou-mais-funcion%C3%A1rios-aparecem-em-duplicidade)
