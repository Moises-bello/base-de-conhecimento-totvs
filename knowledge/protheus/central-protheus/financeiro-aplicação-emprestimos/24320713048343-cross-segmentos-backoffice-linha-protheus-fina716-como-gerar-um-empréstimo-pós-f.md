---
article_id: 24320713048343
category: Financeiro - Aplicação / Emprestimos
content_hash: a9222bf1fac61f20654e40016b8eda5e78882088a8363162d74d1e9f66ceb698
fetched_at: '2026-06-28T22:37:59.352075+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA716 como gerar um empréstimo
  pós fixado?
type: support-article
updated_at: '2026-01-07T19:34:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24320713048343-Cross-Segmentos-Backoffice-Linha-Protheus-FINA716-como-gerar-um-empr%C3%A9stimo-p%C3%B3s-fixado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24320712977559) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Cross Segmentos - Backoffice Linha Protheus - FINA716 como gerar um empréstimo pós fixado?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
  
Cadastro do template na rotina FINA716   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24320734646807)  
  
Exemplo de configuração do template usando o indice CDI  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24320712983063)  
  
Configuração do indice financeiro  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24320712987799)  
Obs. Configure o indice na rotina FINA017  
  
Na rotina FINA018 precisa ter as taxas cadastradas, no exemplo abaixo existe no dia 10/06, 11/06 e 12/06.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24320712991255)  
  
No exemplo a seguir será incluido um contrato de empréstimo na rotina FINA716 na data base 01/05/2024 utilizando o tipo de operação "TEM" Template, para gerar 2 parcelas.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24320734667031)  
  
Na projeção de valor das parcelas o CDI por não ter uma taxa fixa, com isso hoje no produto não será demonstrado o valor de juros conforme o print abaixo.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24320712997399)

O juros será calculado no momento do resgate, conforme o exemplo a seguir, logado na data base 12/06/2024  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24320734673943)

Apenas para comparação exemplo com o simulador do banco central com a taxa do CDI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24320734675991)

Saiba mais:  
[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=680254799)

[Cadastro de templates - FINA716](https://tdn.totvs.com/display/public/PROT/Cadastro+de+templates+-+FINA716)
