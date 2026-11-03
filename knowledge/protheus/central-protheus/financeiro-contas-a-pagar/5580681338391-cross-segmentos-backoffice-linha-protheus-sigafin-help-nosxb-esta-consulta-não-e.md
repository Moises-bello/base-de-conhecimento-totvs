---
article_id: 5580681338391
category: Financeiro - Contas a Pagar
content_hash: 2293508431f466801b056f4e37bc0f4b985ac7f63283ca6a6a7540abeb19b609
fetched_at: '2026-06-28T22:38:07.142349+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Help NOSXB - Esta consulta
  não esta cadastrada no SXB
type: support-article
updated_at: '2026-02-27T12:04:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5580681338391-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Help-NOSXB-Esta-consulta-n%C3%A3o-esta-cadastrada-no-SXB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21002434299031) Tempo aproximado para leitura: **00:03 min**  
  
**Ocorrência**  
Help **NOSXB -**Esta consulta não está cadastrada no SXB  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Versões.  
  
**Causa**  
O help é exibido com a mensagem **“Help NOSXB – Esta consulta não está cadastrada no SXB”** quando, na consulta padrão de determinado campo, não é encontrada uma vinculação de consulta associada a esse campo. Essa situação, em geral, ocorre em decorrência de falha na execução do **UPDDISTR** no ambiente.  
  
**Solução**  
Executar o Compatibilizador **UPDDISTR** correspondente ao último acumulado do módulo Financeiro, disponível na Central de Downloads do Portal do Cliente.

[Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - Atualização do Ambiente Modulo 06 Financeiro Acumulado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005363562-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-Atualiza%C3%A7%C3%A3o-do-Ambiente-Modulo-06-Financeiro-Acumulado?source=search)

***ATENÇÃO***

***O patch deverá ser aplicado inicialmente no ambiente de homologação, devidamente atualizado conforme o portal. Somente após a validação nesse ambiente, a aplicação deverá ser realizada em produção.***

**Saiba Mais**  
[SXB - LookUps(Consulta Padrão)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=22479685)
