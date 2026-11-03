---
article_id: 36323009088791
category: Contabilidade Gerencial - Reprocessamento
content_hash: 06151868232867b74600eede9aa744412693644f859eb846c49a384f35f99edf
fetched_at: '2026-06-28T22:40:41.979320+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA980 - Correção automática
  de Saldos.
type: support-article
updated_at: '2025-11-14T17:21:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36323009088791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA980-Corre%C3%A7%C3%A3o-autom%C3%A1tica-de-Saldos
---

A rotina **"Correção de saldos**" (CTBA980 ), trabalha de forma automática, tendo sido desenvolvida para otimizar e garantir a precisão dos saldos contábeis, eliminando a necessidade de intervenção manual constante.

Integrada ao ***schedule*** do Protheus, essa ferramenta é configurada para analisar e corrigir automaticamente quaisquer discrepâncias nos saldos contábeis, assegurando que os dados contábeis estejam sempre consistentes e atualizados.

##### **AGENDANDO A CORREÇÃO AUTOMÁTICA DE SALDOS NO SCHEDULE**

Acessando a opção de agendamentos do *Schedule*, cadastre a rotina **CTBA980**e escolha a periodicidade: **Sempre ativo**.

**![](https://tdn.totvs.com/download/attachments/851295422/agendamento1.gif?version=2&modificationDate=1719858859457&api=v2)**

Na próxima etapa, defina para quais Empresas e Filiais deseja que a rotina seja executada.  
Além disso, preencha na sessão de parâmetros qual o período, moeda e tipo de saldo deseja utilizar.

**![](https://tdn.totvs.com/download/attachments/851295422/agendamento-2.gif?version=1&modificationDate=1719857544883&api=v2)**

**![(ideia)](https://tdn.totvs.com/s/5bn9pn/8804/xgjkrn/_/images/icons/emoticons/lightbulb_on.svg) Parâmetro "Período a retroagir ?" e "Quantidade (Meses/Dias) ?"**  
A verificação de saldos considera sempre o dia anterior à data atual (D-1) para trás.   
Essa abordagem evita concorrência com as atividades do dia vigente, como inclusões, exclusões e alterações de lançamentos contábeis.  
  
Estes dois parâmetros são complementares, em Período a retroagir é informado se serão retroagidos Meses ou Dias, no parâmetro seguinte é informado a quantidade a retroagir.  
  
Se você selecionar a opção "Meses" e informar a quantidade "2", serão contados dois meses retroativamente a partir da data do calendário contábil aberto no período que você escolheu. Por exemplo, se o período atual é o mês 3 e você escolheu 2 meses, a data de início será dois meses atrás, começando a contar a partir da data atual, menos 1, para a verificação e correção.  
Se você selecionar a opção "Dias" e informar a quantidade "15", serão contados 15 dias retroativamente para a verificação e correção.  
  
A verificação por meses é realizada sempre para o ano corrente da data atual, caso sejam informados mais meses do que o ano atual possui, serão processados os meses do ano corrente apenas. A verificação por meses também é particionada por cada mês, se for informado mais de 1 mês, os processamentos serão divididos por cada mês.  
A verificação por dias, é realizada de uma vez só, considerando data inicial e data final (Data atual - 1)

Importante
