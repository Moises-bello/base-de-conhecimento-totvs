---
article_id: 360025549851
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 13ce2b7bccde7c2ed82cc1086269d1d1a53b9194a055b46b2b4ff45c4da4da3b
fetched_at: '2026-06-28T22:42:42.231555+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Em quais condições o empenho não é
  gerado
type: support-article
updated_at: '2026-04-06T11:58:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025549851-Manufatura-Linha-Protheus-SIGAPCP-Em-quais-condi%C3%A7%C3%B5es-o-empenho-n%C3%A3o-%C3%A9-gerado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:05 min**  
**Dúvida**Em quais condições o **empenho** não é gerado?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O **empenho** não é gerado quando:

* O componente em questão está indicado como fantasma no campo **B1\_FANTASM - Fantasma**;
* O componente está indicado como sendo do tipo **BN**, no campo **B1\_TIPO - Tipo**, e o parâmetro **MV\_EMPBN - Indica se devem ser gerados empenhos de Ordens de Produção para componentes do tipo BN** está desativado;
* O componente não é valido para a data inicial da produção da **OP - Ordem de produção**;
* O componente não é valido para a revisão da estrutura indicada na **OP** no campo **C2\_REVISAO - Revisão Estr**;
* O componente está bloqueado no campo **B1\_MSBLQL - Blq. de Tela**;
* O item em questão possui opcional preenchido na rotina **MATA200 - Cadastro de Estrutura**, porém não há seleção de opcional, o que pode ocorrer se o parâmetro **MV\_SELEOPC** **- Indica se sistema utiliza seleção de Opcionais na abertura de OPs, SCs, Prev. Vendas, Plano Mestre de Produção, etc** estiver com o conteúdo igual a **N.**
