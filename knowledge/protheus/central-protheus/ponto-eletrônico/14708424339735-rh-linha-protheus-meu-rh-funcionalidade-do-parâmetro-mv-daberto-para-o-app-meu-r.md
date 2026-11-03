---
article_id: 14708424339735
category: PONTO ELETRÔNICO
content_hash: 18cc029d5ec3d2aa1d8305af9dc3217d9467292300177c0d875d2959d6e13f02
fetched_at: '2026-06-28T22:44:36.608251+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Funcionalidade do parâmetro MV_DABERTO para
  o App Meu RH
type: support-article
updated_at: '2025-12-08T20:16:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14708424339735-RH-Linha-Protheus-Meu-RH-Funcionalidade-do-par%C3%A2metro-MV-DABERTO-para-o-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24442825783447) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Funcionalidade do parâmetro MV\_DABERTO para o App Meu RH  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
O parâmetro **MV\_DABERTO**, permite informar a **quantidade de dias corridos** após o **fim do período do Ponto,** para manutenção das marcações pelos funcionários.  
  
Por exemplo, se o período aberto do Ponto estiver como **01/04/2023 a 30/04/2023**, cadastrado nos parâmetros **MV\_PAPONTA** e **MV\_PONMES**, e o usuário precisar realizar manutenção neste período, **já no mês de Maio**, precisaremos ter o parâmetro **MV\_DABERTO** cadastrado com quantos dias, **após 30/04/2023** é permitido que o funcionário realize manutenção, **pois se o mesmo estiver como 0** no conteúdo, após o dia 30/04/2023, que é o último dia do período, **o ponto já não permitirá ajustes ou inclusões**.  
  
Exemplo 1:  
MV\_PAPONTA:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707804427415)  
  
MV\_PONMES  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707842083223)  
  
MV\_DABERTO = 0  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707862336535)  
  
Hoje, dia **19/05/2023 (data da criação deste artigo)**, o período de Abril, cronologicamente falando, já finalizou-se, com isso, ao tentar incluir uma marcação neste cenário, **o Meu RH trará este** ***log***:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707937583895)  
  
Exemplo 2:  
MV\_DABERTO = 15  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707970715543)  
\*\*\* Lembrando que hoje, data da criação deste artigo é 19/05/2023.  
  
Ao inserir uma marcação com este cenário com o **MV\_DABERTO = 15**, ainda temos o *log*:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14708012015895)  
  
Exemplo 3:  
MV\_DABERTO = 20  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14708049366039)  
\*\*\* Lembrando que, hoje data da criação deste artigo é 19/05/2023.  
  
Ao inserir uma marcação com este cenário com o **MV\_DABERTO = 20**, a inclusão é permitida:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14708341027351)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14708329158807)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
