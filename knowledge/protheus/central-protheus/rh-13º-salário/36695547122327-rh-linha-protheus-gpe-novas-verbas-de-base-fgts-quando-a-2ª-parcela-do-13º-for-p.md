---
article_id: 36695547122327
category: RH - 13º salário
content_hash: feedf94968a5a9cdce6b11a2103bc8da34cba71385afe16f122bc6ac8e690f40
fetched_at: '2026-06-28T22:44:00.861074+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Novas verbas de Base FGTS quando a 2ª parcela do
  13º for paga antes do mês de dezembro
type: support-article
updated_at: '2025-12-01T17:40:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36695547122327-RH-Linha-Protheus-GPE-Novas-verbas-de-Base-FGTS-quando-a-2%C2%AA-parcela-do-13%C2%BA-for-paga-antes-do-m%C3%AAs-de-dezembro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36695530583191)  Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Criação de identificadores de cálculo para gerar o FGTS sobre o líquido e auxiliar a conferência entre folha de pagamento e eSocial.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2310  
  
**Solução**  
Para auxiliar na conferência entre folha de pagamento e eSocial de BASE FGTS e FGTS recolhido, foi criado o **Id 1962 (base provento)** e o **Id 1963 (base desconto)**, para gravar o valor do **FGTS 13º sobre o líquido**, quando a segunda parcela do 13º for paga **antes do mês de dezembro.**

Deverão ser criadas as seguintes verbas, com as respectivas configurações:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36695530585239)

**Exemplo de cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36695530589719)

Cálculo: (Base FGTS 13º - FGTS recolhido) x 8%

Base FGTS 13º: 5.000,00 (verba 722 - Id 0108 )  
Recolhimento FGTS: 400,00 (verba 723 - Id 0109)  
  
(5000,00 - 400,00) \* 8% =  **368,00** (verbas 985 e 986 - **Ids 1962 e 1963**)

**Obs.:** Os id's serão gerados apenas quando a segunda parcela do 13º for paga **antes do mês de dezembro.**

**Saiba Mais**  
[Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=861550227)  
[RH - Linha Protheus - GPE - 13º Parcela Única](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057320354-RH-Linha-Protheus-GPE-13%C2%BA-Parcela-%C3%9Anica)
