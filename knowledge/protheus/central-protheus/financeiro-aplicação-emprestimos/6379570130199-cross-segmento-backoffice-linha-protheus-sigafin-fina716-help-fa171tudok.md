---
article_id: 6379570130199
category: Financeiro - Aplicação / Emprestimos
content_hash: 3946aa71c3fd607cc9e505ba008eae5596697affdfdce908b3a0ea071ba045b2
fetched_at: '2026-06-28T22:37:59.316000+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA716 - Help: FA171TUDOK'
type: support-article
updated_at: '2025-07-03T19:44:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6379570130199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Help-FA171TUDOK
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33238570252439)**Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Na rotina FINA716 de Aplicação e empréstimos ao incluir uma operação de empréstimo com moeda "2" ocorre o Help: FA171TUDOK  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33238570254615)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA171 - A partir da release 12.1.17  
  
**Cenário 1:**Esse help ocorre quando o cadastro da Moeda "2" na rotina MATA090 esta sem valor na data da operação.   
  
**Solução**Cadastrar um valor na data da operação para a moeda 2.  
  
**Cenário 2:**Incluir um contrato exemplo do tipo **CDB** e informar o campo "**Numero Contr**" sem informar o campo **Qtd.Cota/Tit**  **Solução**Na rotina, ao vincular um contrato no campo **Numero Contr**, precisa ser informado também o campo  **Qtd.Cota/Tit.** Esse processo é utilizado para as operações do tipo "**FAF** → Fundo Aplic Finac" e "**FIC** → Fundos de investimento a Curto Prazo", que utilizam quantidades de cotas.  
  
Para operação que não utilizam cotas, não será possível apenas informar o número do contrato.   
 **Saiba mais**  
[Moedas - MATA090](https://tdn.totvs.com/display/PROT/Moedas+-+MATA090)  
[Aplicações - FINA716](https://tdn.totvs.com.br/pages/viewpage.action?pageId=684987286)
