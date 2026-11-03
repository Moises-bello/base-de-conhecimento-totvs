---
article_id: 115014827327
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: d9e37d9a42d6dbfe4d2ecf53bec08b2e8046e4e8063b4dab24329f1111f05a85
fetched_at: '2026-06-28T22:38:45.207105+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP-FAT- Erro ao gerar o documento de saída - Array out of bounds (1 of 0) on
  MAPVL2SD2
type: support-article
updated_at: '2021-04-28T15:14:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115014827327-MP-FAT-Erro-ao-gerar-o-documento-de-sa%C3%ADda-Array-out-of-bounds-1-of-0-on-MAPVL2SD2
---

**Ocorrência**  
  
Erro ao gerar documento saída :  
**array out of bounds ( 1 of 0 ) on MAPVL2SD2(MATA461.PRX) 22/06/2017 14:39:48 line : 4804**

**Ambiente**  
  
Microsiga Protheus - Versão 12.  
  
**Causa**  
  
O ambiente tem  integração com o módulo SIGAEEC, neste caso, o sistema valida o parâmetro MV\_EEC0052.  
O parâmetro recebe por default conteúdo 1 sem aspas, e se refere a Sincronizar a cotação de moedas pelo módulo  SIGAEEC.   
Opção 1: SIM, opção 2: NÃO.  
Provavelmente está em branco e com isso , é passado a informação ao sistema que o conteúdo é 0, gerando o erro.  
  
**Solução**  
  
Acesse o configurador e atribua a informação no parâmetro, seja 1 ou 2, o importante é que o parâmetro não fique vazio, depois reinicie o protheus para acatar as configurações e refaça o processo.
