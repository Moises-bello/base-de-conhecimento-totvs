---
article_id: 33373045691543
category: Financeiro - Conciliação de Vendas
content_hash: 111074fa31c2bf064b94b26c2be3eabc969ea81a3346d502c137fb37a50d686a
fetched_at: '2026-06-28T22:37:26.301882+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) SIGAFIN - Contas a Receber
  - Conciliação FINA918 - HELP: A918NOFIELDS'
type: support-article
updated_at: '2026-03-04T17:11:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33373045691543-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Contas-a-Receber-Concilia%C3%A7%C3%A3o-FINA918-HELP-A918NOFIELDS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33373045670807) Tempo aproximado para leitura: **00:10:00 min**

**Ocorrência**  
No módulo Financeiro, ao tentar acessar a rotina FINA918, ocorre a mensagem de erro **A918NOFIELDS**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33373044602007)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a Receber - Todas as versões homologadas  
  
**Causa**  
O incidente ocorre devido à falta de campos de **Filiais de Inclusão** nas tabelas **FIF - ARQUIVO CONCILIAÇÃO SITEF e MEP - Parcelamento SITEF.**

Campos: **FIF\_MSFIL, MEP\_MSFIL**

**Solução**  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
Acesse o **Configurador (SIGACFG) e navegue até Base de dados >> Dicionários de dados >> Base de dados.**

1. Encontre a tabela **FIF** e clique em **Editar**.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33373045671447)  
   2.1. Adicionar campo **"Filial de Inclusão"** em **Campos Reservados.**  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33373044602263)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33373044602391)  
  
2.2 O campo **FIF\_MSFIL** será criado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33373045671831)  
  
  
3. Localize a tabela **MEP** e clique em "**Editar**".  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33373045671959)

3.1 Adicionar campo **"Filial de Inclusão"** em **Campos Reservados.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33373045672215)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33373045673623)

3.2 O campo **FIF\_MSFIL** será criado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33373044602903)

Salve o dicionário de dados e retome a rotina **FINA918**.  
  
**Saiba mais**  
[Conciliador Pagamentos e Vendas - Financeiro (Contas a Receber) - P12](https://tdn.totvs.com/display/public/PROT/Conciliador+Pagamentos+e+Vendas+-+Financeiro+%28Contas+a+Receber%29+-+P12)
