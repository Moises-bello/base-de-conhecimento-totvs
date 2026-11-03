---
article_id: 360004560531
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: bcdd56e92ef42c49e26f2f5600c0d19078c868b95930176a36f79ab392abc2b8
fetched_at: '2026-06-28T22:38:32.703524+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Valor de Desconto Duplicado na geração do Título
type: support-article
updated_at: '2021-04-28T15:56:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004560531-MP-FAT-Valor-de-Desconto-Duplicado-na-gera%C3%A7%C3%A3o-do-T%C3%ADtulo
---

**Ocorrência**

Valor de desconto aplicado no item do pedido de vendas é duplicado no momento da geração do titulo e documento de saída, exemplo, se incluir um item com valor de 1000,00, aplicar um desconto de 10% no item, ao acessar a planilha, o valor da duplicata será de 900,00, conforme esperado, porém quando efetuamos o faturamento a nota e o titulo é gerado com valor de 800,00, duplicando o desconto aplicado.

**Ambiente**

Microsiga Protheus - a partir da versão 12.1.17.  
   
 **Causa**

O erro de desconto duplicado na nota fiscal de saída, ocorria com o valor do desconto que era  subtraído do preço unitário quando não há rateio no cabeçalho da nota, o que fazia com que a nota e titulo fossem gerados com desconto duplicados.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Aplique o pacote de correção:[Principais Pacotes de Correção - Faturamento - SIGAFAT - Desconto duplica ao Faturar - ocorrência 46](http://tdn.totvs.com/pages/viewpage.action?pageId=235334710);

2. Reinicie o smartclient;

3. Acesse o Faturamento e refaça o processo da nota de saída.
