---
article_id: 360015053672
category: RH - Relatórios
content_hash: b3a27fa4c46f32a8d2ed4f0da26e637a8712bf7caf3ef82b88cfb844500faa1d
fetched_at: '2026-06-28T22:44:43.619999+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Utilização do parâmetro MV_H2D_RDN na impressão
  de Relatórios do Ponto Eletrônico
type: support-article
updated_at: '2025-10-14T13:51:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015053672-RH-Linha-Protheus-PON-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-H2D-RDN-na-impress%C3%A3o-de-Relat%C3%B3rios-do-Ponto-Eletr%C3%B4nico
---

**Dúvida**Como utilizar o parâmetro **MV\_H2D\_RDN** na impressão de relatório do Ponto Eletrônico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico – todas as versões  
  
**Solução**O parâmetro **MV\_H2D\_RDN** é utilizado para o **arredondamento de casas decimais**, na conversão das horas **sexagesimais em centesimais**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32070457161367)  
  
Na impressão do Espelho de ponto em **Atualizações> Relatórios> Espelho de Ponto**, por exemplo, quando o parâmetro está com o conteúdo **N** e a pergunta "**Horas em" = "Centesimal"**, é impresso conforme abaixo:  
![68.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360010183711)  
  
Quando geramos o Espelho de ponto com o parâmetro como **S** e deixamos a pergunta "**Horas em" = "Centesimal",** ficará conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32070447708311)  
![67.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360010183351)  
Veja que em alguns dias, como **24/07** e **01/08** o resultado final sofreu uma alteração.  
  
O parâmetro tem impacto em **qualquer relatório** que mostre horas em centesimal o sexagesimal: **Espelho de Ponto, Relatório de Banco de Horas e Relatório de Resultados.**  
  
  
  
**Saiba Mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
