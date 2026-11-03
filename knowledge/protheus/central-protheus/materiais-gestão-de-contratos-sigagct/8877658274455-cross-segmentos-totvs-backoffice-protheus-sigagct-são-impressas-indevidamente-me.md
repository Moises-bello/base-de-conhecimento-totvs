---
article_id: 8877658274455
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 82a7350b04e39e5e7f06303f865902b62ae7bf82878201da9c10c36f82fecf55
fetched_at: '2026-06-28T22:37:24.152019+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGAGCT - São impressas  indevidamente
  Medições Realizadas no Relatório de Medições Não efetuadas  (CNTR121) o que pode
  ser?
type: support-article
updated_at: '2026-03-02T19:04:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8877658274455-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGAGCT-S%C3%A3o-impressas-indevidamente-Medi%C3%A7%C3%B5es-Realizadas-no-Relat%C3%B3rio-de-Medi%C3%A7%C3%B5es-N%C3%A3o-efetuadas-CNTR121-o-que-pode-ser
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38748641116183) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
São impressas indevidamente Medições Realizadas no Relatório de Medições Não efetuadas (CNTR121) o que pode ser?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Contratos - Todas as versões  
  
**Causa:**  
Uma das possibilidades é  a Medição estar encerrada na rotina CNTA121, porém, na rotina de Manutenção de Contratos(CNTA300) por algum motivo não ter atualizado o Cronograma financeiro e a parcela continua em aberto no Cronograma do Contrato tabela CNF.

**Solução:**

Executar a Rotina de Reajuste de Saldos (CNTA320) [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o Reajuste de Saldo em contratos, planilhas e cronograma financeiro ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020124591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-o-Reajuste-de-Saldo-em-contratos-planilhas-e-cronograma-financeiro-?source=search) para atualizar o Cronograma financeiro corretamente conforme as Medições realizadas.

**Saiba mais em :**

* [**MP - SIGAGCT - FAQ Gestão de Contratos**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115005126608-MP-SIGAGCT-FAQ-Gest%C3%A3o-de-Contratos?source=search)
* [**Manutenção de Contratos - CNTA300**](https://tdn.totvs.com/x/0rYGDg)
