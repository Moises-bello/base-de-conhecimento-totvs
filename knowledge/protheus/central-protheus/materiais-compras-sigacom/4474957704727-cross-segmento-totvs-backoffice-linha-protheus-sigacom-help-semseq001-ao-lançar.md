---
article_id: 4474957704727
category: Materiais - Compras (SIGACOM)
content_hash: 4c1526befab1b83b01d6fb730aba416355e581528c019c341b078725b7d47ed2
fetched_at: '2026-06-28T22:41:11.675697+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Help SEMSEQ001
  ao lançar uma Despesa de Importação
type: support-article
updated_at: '2022-12-14T14:31:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4474957704727-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Help-SEMSEQ001-ao-lan%C3%A7ar-uma-Despesa-de-Importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao lançar uma Despesa de Importação é apresentado o Help SEMSEQ001

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4474901379351/imagem1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

Essa mensagem pode ocorrer quando o registro em questão na tabela SD7 foi deletado e o sistema perdeu a referência do próximo número da sequência.  
  
Abaixo algumas inconsistências de quando este help é exibido:

* Validar a existência de todos os registros deste processo na tabela SD7 (campos D7\_SEQ e D7\_TIPO) e verificar se alguma linha foi deletada, caso encontre alguma nesta situação deverá restaurar este registro.

* Quando os campos D7\_NUMERO (SD7) e QEK\_CERFOR (QEK) estiverem com conteúdo diferentes.   
  Exemplo: D7\_NUMERO = SK00006 e o QEK\_CERFOR = SK00008

* Assim deverá realizar a verificação dos registros nas tabelas envolvidas e realizar o ajuste dos campos.

* Quando o registro na QEK (QEK\_CEROR) está ativo e o registro referência na SD7 (D7\_NUMERO) está deletado.

* Verificar também os campos D3\_DOC (SD3) e D1\_NUMCQ (SD1) que podem influenciar também no processo.

* Verificar também se o Local de CQ, campo D7\_LOCAL está igual ao local informado no parâmetro MV\_CQ.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
