---
content_hash: 50686d9617ab6d82ac64a315001218839731925779dd6f4a3b7fbd1c906637f1
fetched_at: '2026-06-29T00:09:45.439022+00:00'
page_id: '433248968'
product: rm
source: tdn-rm
title: Contas (Lalur Parte B)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=433248968
version: 4
---

**Parte A**  
A Parte A do Lalur é atendida através do Evento Tributário, pelos grupos de Adições e Exclusões do Lucro e, também, pelo novo grupo de Compensação do Prejuízo / Base Negativa.  
O Evento foi evoluído para permitir vincular uma conta da Parte B. Será preciso que o lançamento de ajuste já tenha sido incluído pelo usuário, manualmente, na Parte B para que a apuração o considere no encerramento do Período.

**Parte B**  
Acesse: Nova MDI | BackOffice | Gestão Fiscal - Obrigações Principais | Lalur - Parte B.  
No Cadastro do Plano de Contas da Parte B do Lalur, deve ser definido Código, Descrição e Máscara.   
Os saldos das contas na Parte B do Lalur serão controlados por tributo.   
Os lançamentos nas contas do Lalur - Parte B devem ser incluídos pelo Anexo "Lançamentos do Lalur Parte B". Eles devem ser inseridos pelo usuário antes do encerramento do Período de Apuração.

***Observação***: No cadastro da Conta do Lalur Parte B na aba Obrigações Principais | Lalur Parte B | Contas | Aba Tributos, no campo “Código da Tabela Padrão RFB - Parte B” será apresentado apenas os Códigos da tabela padrão importados no menu ECF - Tabela Dinâmica associados ao Grupo "Lalur Parte B".  
Este campo será utilizado na geração do campo 5- COD\_PB\_RFB do Registro M010.

IMPORTANTE

Implementação realizada oficialmente na versão 12.1.25 e disponível nas versões 12.1.22 e superiores mediante a execução do script de marcação LI.2019.04\_01
