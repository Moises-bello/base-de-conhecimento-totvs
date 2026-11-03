---
article_id: 360018285391
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: e3628f24deab76a926c2ecb300a7fd1f8b87566367ba8fc258a459729bbf27f1
fetched_at: '2026-06-28T22:40:32.574991+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Rastreamento contábil
  conceito da tabela CV3'
type: support-article
updated_at: '2022-06-20T19:48:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018285391-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Rastreamento-cont%C3%A1bil-conceito-da-tabela-CV3
---

**Dúvida**Rastreamento contábil conceito da tabela CV3

**Ambiente**Protheus  – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução**A tabela **CV3** **- Rastreamento Contábil**, tem sua funcionalidade e conceito focados somente para geração de registros de contabilizações realizadas via integração, ou seja, contabilizações provenientes de outros módulos/processos (Contas a Pagar, Faturamento, Compras, etc) e somente gera o rastreio contábil referente a moeda origem(01).   
  
Em casos de estornos contábeis realizados diretamente no módulo **Contabilidade Gerencial** **- SIGACTB**, não é considerada uma operação de integração, ou seja, não será gerado registro na tabela CV3.   
  
Em casos de estornos, deve ser contabilizado o estorno da operação original para constar na tabela **CT2**- **Lançamentos Contábeis** e também nos registros da tabela **CV3**.
