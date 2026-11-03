---
article_id: 360021234092
category: Folha Mensal
content_hash: 34c32cb079f4597d24a0db1ec4d4c23b765f8c4aa7ed9f0a288317be9fa2e6fe
fetched_at: '2026-06-28T22:46:59.542831+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RM - FOP - 13º Salário: Evento de diferença (dissídio NÃO)'
type: support-article
updated_at: '2025-03-12T20:14:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021234092-RM-FOP-13%C2%BA-Sal%C3%A1rio-Evento-de-diferen%C3%A7a-diss%C3%ADdio-N%C3%83O
---

**Ocorrência**  
Ao tentar calcular a diferença de 13º salário por dissídio NÃO, o sistema não permite avançar.  
  
**Ambiente**  
RM - Folha de Pagamento - Todas as versões  
  
**Causas**  
Isto ocorre porque não existe um evento com **Código de Calculo 66** com incidência em **INSS de Folha**.  
  
**Solução**  
Se o lançamento de **13º Salário** ocorrer em janeiro, o usuário deverá criar um novo evento com de Código de Cálculo 066, com incidência em **INSS** (folha).

Isto acontece porque o provento pago em janeiro participa do cálculo de INSS da Folha e utiliza a tabela de cálculo de INSS de janeiro. Ou seja, o recolhimento de INSS será feito juntamente com a folha de janeiro (conforme legislação vigente).  
**Informações Adicionais**  
A diferença de **13º Salário** pode ocorrer quando o funcionário tiver reajuste salarial no mês de dezembro e já tiver recebido o 13º com o salário anterior. Esta diferença poderá ser paga na competência dezembro ou janeiro, dependendo do mês de competência em que o usuário se encontra.

Ao pagar a diferença de **13º Salário** no mês de dezembro o sistema assumirá o evento com Código de Cálculo 66 cadastrado no Grupo 0 no campo Evento de Diferença pasta diferença de 13º salário. Se a diferença for paga no mês de Janeiro, o sistema irá abrir um combo apresentando os eventos com CC (66) com incidência em **INSS folha**. Caso não tenha um evento com essas parametrizações, será necessário cadastrar.  
  
**Observações**  
\* O evento deverá incidir também em **IRRF 13º salário;**  
\* Ao calcular a diferença em **Janeiro,** se existir alguma média discriminada, o sistema irá lançar toda a diferença no evento de pagamento da diferença (Código de cálculo 66).
