---
article_id: 38166965059351
category: Financeiro - Contas a Pagar
content_hash: 1e48b4a19b3bd8489b4de980fee778dfdd07e88becb5da94129100c3a5af17c5
fetched_at: '2026-06-28T22:38:08.340103+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINI050 - Como gravar
  as informações que vem no XML referente ao banco nas tagas -> BankCode, BankBranch
  e BranchKey
type: support-article
updated_at: '2026-02-04T19:33:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38166965059351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINI050-Como-gravar-as-informa%C3%A7%C3%B5es-que-vem-no-XML-referente-ao-banco-nas-tagas-BankCode-BankBranch-e-BranchKey
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38167002228887) Tempo aproximado para leitura: 00:03 min  
  
**Dúvida**  
Como gravar as informações que vem no XML referente ao banco nas tagas -> BankCode, BankBranch e BranchKey  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**  
Necessário utilizar o ponto de entrada **FA050GRV**, esse ponto de entrada sera utilizado apos a gravacao de todos os dados na **inclusão do título** e antes da sua contabilização

E para localizar as informações do XML, é necessário posicionar-se no array **AAUTOCAB**. Nesse array, é possível localizar as posições de banco, agência e digito que são enviadas no XML, para então configurar o ponto de entrada **FA050GRV** e gravar as informações bancárias na inclusão do título.

[FA050GRV - Grava dados](https://tdn.totvs.com/display/public/mp/FA050GRV+-+Grava+dados+--+11855)
