---
article_id: 360019141111
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 916b37cb8160d4a8c1866ed469e53433cda17e056c95b1b479519ee59bfda463
fetched_at: '2026-06-28T22:39:30.519323+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Cálculo do PMC -
  Preço máximo ao consumidor '
type: support-article
updated_at: '2021-07-29T14:32:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019141111-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-do-PMC-Pre%C3%A7o-m%C3%A1ximo-ao-consumidor
---

**Dúvida**  
Como calcular o PMC - Preço Maximo ao Consumidor para produtos de medicamentos.

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
  
**Solução**

Para que seja tratado o calculo do PMC será necessário utilizar a configuração abaixo:  
  
TES:  
Aplica Marg (F4\_APLIIVA) = 5 (Out.%)  
Def. MVA/ PA (F4\_OUTPERC) =  90,00  
Mkp ICM Comp (F4\_MKPCMP)= Não  
Marg Solid (F4\_MPKSOL)= Configuração  
  
Cadastro do Produto:  
ICMS Pauta (B1\_VLR\_ICM) = Informar o Valor da Pauta (PMC)  
  
A Margem de Lucro deverá estar cadastrada no Produto ou na Exceção fiscal para sistema fazer o cálculo quando o valor atingir a porcentagem solicitada.

Documentação:

<http://tdn.totvs.com/display/public/PROT/ICMS+de+Pauta+X+MVA>
