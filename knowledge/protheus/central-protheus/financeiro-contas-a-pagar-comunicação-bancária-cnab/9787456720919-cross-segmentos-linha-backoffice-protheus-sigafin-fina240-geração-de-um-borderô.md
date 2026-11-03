---
article_id: 9787456720919
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 673ede8cb1c65b4732dfae53a0e24cfc4e7e36df6e0cfb263acb95d708b6d8bd
fetched_at: '2026-06-28T22:37:56.489793+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Linha Backoffice Protheus - SIGAFIN - FINA240 - Geração de
  um Borderô com mais de uma filial
type: support-article
updated_at: '2022-10-26T16:00:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9787456720919-Cross-Segmentos-Linha-Backoffice-Protheus-SIGAFIN-FINA240-Gera%C3%A7%C3%A3o-de-um-Border%C3%B4-com-mais-de-uma-filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a geração de um Borderô com mais de uma filial, não habilita o Wizard de Filiais para seleção na rotina FINA240 - Borderô Pagamentos  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA240 - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o **Banco** informado no **Cadastro de Bancos(MATA070)** está com a pergunta Habilita TCB = Sim   
  
**Solução**Ajustar a pergunta no **Cadastro de Bancos** para "**Não**" e realizar novamente o processo de borderôs, com isso irá habilitar o Wizard de filiais. 

**Saiba mais**  
[Borderô Pagamentos - FINA240 - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=236605212)
