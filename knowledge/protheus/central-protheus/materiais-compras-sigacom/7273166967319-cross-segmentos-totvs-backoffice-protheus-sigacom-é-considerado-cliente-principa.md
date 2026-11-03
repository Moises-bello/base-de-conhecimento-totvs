---
article_id: 7273166967319
category: Materiais - Compras (SIGACOM)
content_hash: 0caa76f812b3ce07fe773aee1e49b73d27c7d92a78e03c783d4c5d14d49e5e8b
fetched_at: '2026-06-28T22:41:17.407393+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É considerado cliente
  Principal C5_CLIENTE ou Cliente Entrega C5_CLIENT  ao utilizar a opção Retornar
  do Documento de entrada?
type: support-article
updated_at: '2024-05-24T17:08:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7273166967319-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-considerado-cliente-Principal-C5-CLIENTE-ou-Cliente-Entrega-C5-CLIENT-ao-utilizar-a-op%C3%A7%C3%A3o-Retornar-do-Documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida** É considerado Cliente Principal C5\_CLIENTE ou Cliente entrega C5\_CLIENT ao utilizar a opção Retornar do Documento de entrada?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**No padrão ao utilizar a opção Retornar do Documento de entrada , é considerado o campo C5\_CLIENTE ,pois,todas devoluções devem ser feitas via Cliente de Faturamento, pelo Cliente de entrega não é possível, pois, para quem foi gerado o título da venda, para que a NCC seja gerada e a compensação possa ocorrer normalmente.

Como alternativa é possível utilizar opção Incluir do Documento de entrada, informando, o código do Cliente de entrega, o número da nota de origem e a série.

Nesse caso não ocorrerá compensação de títulos no financeiro visto que o título da venda foi para um Cliente e a entrada da nota para outro cliente e o sistema não conseguirá efetuar um vínculo entre saída e entrada em virtude da devolução não estar sendo efetuada pelo cliente principal,  porém os dados da origem, podem ser informados manualmente.  
   
O item da origem não pode ser preenchido, caso contrário, o sistema efetua a validação da nota.   
  
Caso deseje que o item seja digitado, pode verificar o parâmetro : MV\_VLDNFO. Abaixo documento.  
   
[MP - SIGACOM - Como configurar o sistema para não validar a Nota de Origem no processo de Devolução?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022252571-MP-SIGACOM-Como-configurar-o-sistema-para-n%C3%A3o-validar-a-Nota-de-Origem-no-processo-de-Devolu%C3%A7%C3%A3o-?source=search). 

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
