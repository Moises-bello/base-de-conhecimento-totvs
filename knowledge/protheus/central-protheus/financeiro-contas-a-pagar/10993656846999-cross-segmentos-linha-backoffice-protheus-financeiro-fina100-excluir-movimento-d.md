---
article_id: 10993656846999
category: Financeiro - Contas a Pagar
content_hash: 0b725914025da5246f1aa2246a66a1ab3a4ec55d5ee4f34e76ca993943bc5d2f
fetched_at: '2026-06-28T22:38:09.844275+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - Financeiro - FINA100 - Excluir
  Movimento de Pagamento Antecipado
type: support-article
updated_at: '2023-03-03T19:21:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10993656846999-Cross-Segmentos-Linha-BackOffice-Protheus-Financeiro-FINA100-Excluir-Movimento-de-Pagamento-Antecipado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min****Dúvida**É possível excluir uma movimentação de pagamento antecipado ( PA ) para não apresentar seu movimento na **Conciliação Bancária ( FINA380 )** e **Extrato Bancário ( FINR470 )**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Visando a integridade dos registros de movimentações bancárias e auditoria pela FINA100 sobre os tipos de movimento que atualizam saldo, ao incluir um **PA** com **F12 - Gera Movimentação Bancária**, irá gerar o movimento e ao excluir irá gerar o movimento de **exclusão/estorno** conforme data de exclusão retornando o saldo para o banco, diferente do processo de exclusão de baixa de títulos que deleta a linha da SE5 com relação a baixa.  
  
Somente ajustando os registros em base de dados para não exibir na conciliação ou extrato bancário, no qual foge do escopo de atendimento do Suporte Padrão

A manipulação da base de dados não é contemplada em nosso escopo de atendimento de Suporte Técnico, esse tipo de procedimento é efetuado apenas por analista in loco.

Confira nosso Escopo -  <https://tdn.totvs.com/pages/releaseview.action?pageId=547876496>  
  
**Saiba mais**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA100 - Exclusão da movimentação bancaria apresenta a mensagem HELP FA100BAIXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060831754-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Exclus%C3%A3o-da-movimenta%C3%A7%C3%A3o-bancaria-apresenta-a-mensagem-HELP-FA100BAIXA?source=search)  
  
**Movimentos Bancários - FINA100 - Financeiro - P12**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=501480542>
