---
article_id: 360007396331
category: Ativo Fixo - Refaz Saldos
content_hash: 0e546ddfddfbf53a9a840d7b97f6403bf27694d8b3db28d9f1925ffb0acdb555
fetched_at: '2026-06-28T22:41:45.996771+00:00'
product: protheus
section_id: 1500001536321
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF -  ATFA120 - REFAZ SALDOS '
type: support-article
updated_at: '2023-04-14T13:24:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007396331-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA120-REFAZ-SALDOS
---

**Ocorrência**Refaz saldos não considera movimentos de baixas  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - a partir da versão 12  
  
**Solução**Execute a rotina utilizando a opção analítica

Refaz saldos

Esta rotina reconstrói a tabela SN5 - Saldos que pode ser efetuada de duas formas:

•Sintético - os saldos são reconstruídos através do Cadastro de Bens (SN1-Cadastro de Ativo Imobilizado + SN3-Arquivo de Saldos), gerando saldos atualizados (resumido).

•Analítico - os saldos são reconstruídos através do Cadastro de Movimentações (SN4-Movimentações do Ativo Fixo), gerados com valores históricos (baixas, depreciações, etc.).  
O ideal é utilizar a forma analítica, isso possibilita a geração dos saldos através de cada movimento registrado no sistema (parâmetro Considera? = Movimentações).

Link com informações referente a rotina de refaz saldos do ativo

Importante - não é indicado a execução desta rotina caso as tabelas não estejam com o saldos corretos , após execução da rotina não é possível cancelar, com isso caso as tabelas não estejam com o saldos corretos ,após e execução da rotina será apresentado saldo incorretos .

Somente voltando backup será possível "cancelar" .

<http://tdn.totvs.com/display/PROT/Refaz+Saldos+do+Ativo+-+ATFA120>

<https://tdn.totvs.com/display/public/PROT/ATFA120+-+Refaz+Saldos+-+Conceito>
