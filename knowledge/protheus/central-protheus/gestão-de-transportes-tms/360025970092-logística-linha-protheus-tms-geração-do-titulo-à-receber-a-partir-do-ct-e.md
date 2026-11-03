---
article_id: 360025970092
category: Gestão de Transportes (TMS)
content_hash: 60fe8bdbbbe5fc0af602b577920ae1279b0e261ff30986aab9fa96a0c0720510
fetched_at: '2026-06-28T22:45:29.242516+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Geração do titulo à receber a partir do
  CT-e
type: support-article
updated_at: '2026-05-04T19:51:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025970092-Log%C3%ADstica-Linha-Protheus-TMS-Gera%C3%A7%C3%A3o-do-titulo-%C3%A0-receber-a-partir-do-CT-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22471471209111)*** Tempo aproximado para leitura: **00:01:55 min**  
  
**Dúvida**  
Como gerar títulos à receber a partir do **CT-e - Conhecimento de Transporte**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões   
  
**Solução**  
O momento da geração do titulo à receber é definido a partir do parâmetro **MV\_TMSMFAT.**  
  
Se **MV\_TMSMFAT = 1 :**

* Na geração de um **CT-e** será gerado automaticamente um titulo no financeiro;
* Cada documento **(CT-e)** terá uma fatura individual, logo, os campos **DT6\_DOC - Número do CT-e**, **DT6\_NUM - Numero da Fatura do CT-e**, **E1\_NUM** **- Numero da Fatura** serão iguais;

Se **MV\_TMSMFAT = 2 :**

* O Sistema não gera fatura ao gerar o **CTe**, e sim é necessário gerar a fatura através das rotinas **TMSA850 - Fatura por documento** ou **TMSA491 -** **Fatura Automática.**
* O Sistema poderá utilizar vários documentos e então, desta forma, terá uma única fatura para os documentos.
* Com **MV\_TMSMFAT** **= 2**, teremos vários **CT-es** em uma única fatura. Neste caso, para identificar o vinculo entre **CT-e** e Fatura temos, **DT6\_NUM = E1\_NUM;**

**Importante**  
O TMS utiliza a condição de pagamento informada no **Contrato do Cliente - TECA250**, campo **Cond.Pag.PV** - **AAM\_CPAGPV** referente ao tomador de serviço. Nesta condição de pagamento, nunca se deve utilizar Condição de Pagamento do Tipo = 9 ou B, pois ao utilizar qualquer um destes dois tipos, o Sistema não gera registros na **SE1 - Financeiro**.   
Para validar qual foi a condição de pagamento de um documento calculado, valide na tabela **SF2**, campo **Cond. Pagto - F2\_COND.**  
  
**Saiba mais**  
Maiores detalhes sobre **Fatura por Documento** acessar o artigo disponível no *link*: [Logística - Linha Protheus - TMS - Fatura por Documento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026231891-MP-TMS-Fatura-por-Documento-)
