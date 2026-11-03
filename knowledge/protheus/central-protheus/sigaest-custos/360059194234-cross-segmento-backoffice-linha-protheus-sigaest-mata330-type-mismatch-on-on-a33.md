---
article_id: 360059194234
category: SIGAEST - CUSTOS
content_hash: df4ca118e6774856b1473ff9509b86fa1fea5c51510c09f52138a366ae27693c
fetched_at: '2026-06-28T22:39:02.087352+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 -  type mismatch
  on $ on A330NIVCQ
type: support-article
updated_at: '2026-04-14T15:46:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059194234-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-type-mismatch-on-on-A330NIVCQ
---

O erro "type mismatch on $" ao executar o Recálculo do Custo Médio no Protheus (versão 12.1.17) está relacionado ao parâmetro MV\_M330JCM. Para resolver, é necessário alterar o tipo deste parâmetro para "C - Caractere". Caso precise, recomenda-se solicitar um analista para o ajuste.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30504023279255)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Ao executar o Recálculo do Custo Médio ou acompanha custos, ocorre o seguinte error.log

**Param 1: ERRORMESSAGE(C) : type mismatch on $**  
Param 2: ERRORSTACK(C) :  
THREAD ERROR ([7768], TP|SD|HTTP@01|TRUE\_, 1ED8FBD33CEED5479E8B4FFC975A5019) 14/10/2025 23:46:16  
**type mismatch on $ on A330NIVCQ(MATA330.PRX) 03/09/2025 16:21:32 line : 12113**

**Ambiente**

Protheus – Estoque/Custos – A partir da versão 12.1.17

**Solução**

Este problema está correlacionado com o parâmetro **MV\_M330JCM**. Quando o seu tipo está **diferente** de **C- Caractere**, ocorre este erro.

Neste caso, alterando o tipo do parâmetro para C - Caractere, ao executar o Recálculo do Custo Médio não ocorrerá mais o erro.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000840401)

**Obs:**Caso necessitar de auxílio para ajuste da tipagem do parâmetro, recomendamos fortemente que solicite um analista in loco para o ajuste.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
