---
article_id: 360045460153
category: RH - Ponto Eletrônico
content_hash: f9c341d2298721f75137c22f7f0449b254fb4212accc7b18c9f41b256e49f99e
fetched_at: '2026-06-28T22:44:58.307079+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como utilizar os parâmetros de Leitura e a tabela
  SPO, responsável pelo fechamento mensal
type: support-article
updated_at: '2026-03-16T14:39:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045460153-RH-Linha-Protheus-PON-Como-utilizar-os-par%C3%A2metros-de-Leitura-e-a-tabela-SPO-respons%C3%A1vel-pelo-fechamento-mensal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39070572981015) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Orientação sobre como utilizar os parâmetros de Leitura e a tabela SPO, responsável pelo fechamento mensal.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A tabela SPO é responsável pelos **períodos fechados** em seu ambiente. O conteúdo que constar nesta tabela, **somente** poderão ter os períodos já fechados (legenda de cor vermelha) e **nunca**, os que ainda encontram-se abertos.   
  
Para configuração correta e que não ocorra nenhum erro no fechamento mensal siga as recomendações abaixo: Existem duas formas para configuração do sistema referente ao período de apontamento. Pode utilizar de forma totalmente **Compartilhada (C C C)** ou**Totalmente Exclusiva (E E E), segue:**  
  
No compartilhamento da SX2, esta tabela deve estar obrigatoriamente totalmente **Compartilhada (C C C):**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29429631538455)**  
  
Se a **SPO for C C C, nos parâmetros da SX6** será necessário existir apenas **um parâmetro MV\_PAPONTA e um MV\_PONMES com filial em branco:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29429631542295)**  
  
Veja na rotina de **período de apontamento(PONA290),** como ficam os períodos fechados nesta configuração compartilhada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29429631544855)

**OU**  
Totalmente **Exclusiva (E E E):**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29429593948823)  
  
Se a **SPO for E E E** **nos parâmetros da SX6** será necessário existir **MV\_PAPONTA e MV\_PONMES com filial preenchida e configurado exclusivo para cada filial da empresa** e não poderá existir nenhum com a filial em branco.   
Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29429593951127)  
  
Veja na rotina de **período de apontamento(PONA290),** como ficam os períodos fechados nesta configuração compartilhada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29429593954583)  
  
**IMPORTANTE:** Muito erros de Leitura e Apontamento são originados pela divergência do compartilhamento da tabela com os parâmetros.  
  
**Saiba Mais:**  
[RH - Linha Protheus - PON - Orientação sobre como utilizar os parâmetros de Leitura e a tabela SPO, responsável pelo fechamento mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045460153-RH-Linha-Protheus-PON-Orienta%C3%A7%C3%A3o-sobre-como-utilizar-os-par%C3%A2metros-de-Leitura-e-a-tabela-SPO-respons%C3%A1vel-pelo-fechamento-mensal)  
[RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
