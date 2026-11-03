---
article_id: 360053753653
category: RH - Desoneração
content_hash: 1dca768aaa1d2b676f1266aca1040b21929d3d356feff5cb73e6c1c7689a0f0b
fetched_at: '2026-06-28T22:43:42.302583+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Quais são os principais parâmetros utilizados no
  cálculo da desoneração
type: support-article
updated_at: '2025-08-06T14:49:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053753653-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-principais-par%C3%A2metros-utilizados-no-c%C3%A1lculo-da-desonera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33987283692311) Tempo aproximado para leitura: **00:01:30 min  
  
Ocorrência**Quais são os principais parâmetros utilizados no cálculo da desoneração?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**

**Gestão de pessoal**

**MV\_DESFOL**- Ano e Mês de competência do início da desoneração da folha de pagamento.  
  
**MV\_FDESFOL** – Ano e Mês de competência do fim da desoneração da folha de pagamento, deverá ser preenchido com o último Ano e Mês em que a empresa ficou desonerada.  
  
**MV\_RECDES** - Determina quais valores serão abatidos na composição das bases de cálculo para a Contribuição Previdenciária sobre a Folha de Pagamento (CPP)  
  
**MV\_RAT0973** - Define se efetua a gravação da verba de Id 0973 na tabela SRC

.F. – define que o sistema não irá efetuar a gravação da CPRB no movimento mensal da Folha (tabela SRC)

.T. – define que o sistema irá efetuar a gravação da CPRB no movimento mensal da Folha (tabela SRC) rateada entre os funcionários, de acordo com o salário base de cada um. A gravação do valor será feita na verba de Id 0973

**Faturamento, Financeiro e Fiscal**

**MV\_CFAREC** - CFOPs de saída que serão considerados como receita;  
  
**MV\_CFEREC** - CFOPs de saída que não serão considerados como receita.  
  
**MV\_CFIND** - Determina os CFOP´s que são utilizados para produtos industrializados pela empresa. 

Obs: Todos CFOP que começam com 7 deverão aparecer na Coluna Exportações na tabela S033.

Mais detalhes sobre esses parâmetros podem ser encontrados no link: [FIS0001\_Apuração\_EFD\_Contribuições](https://tdn.totvs.com/pages/viewpage.action?pageId=212896468)

**Saiba mais:**

[RH - Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)
