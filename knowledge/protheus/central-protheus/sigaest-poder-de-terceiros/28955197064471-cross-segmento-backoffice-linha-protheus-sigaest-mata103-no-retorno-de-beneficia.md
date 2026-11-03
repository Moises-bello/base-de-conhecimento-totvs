---
article_id: 28955197064471
category: SIGAEST - PODER DE TERCEIROS
content_hash: c88c72aa57bfa87419e6b94e69bf30df20982c4d212a6fb2a308249ca63e6e0c
fetched_at: '2026-06-28T22:39:03.203580+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 - No retorno
  de beneficiamento é possível inserir a mesma série (endereço) de uma remessa?
type: support-article
updated_at: '2025-01-03T18:44:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28955197064471-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-No-retorno-de-beneficiamento-%C3%A9-poss%C3%ADvel-inserir-a-mesma-s%C3%A9rie-endere%C3%A7o-de-uma-remessa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28955197036183) Tempo aproximado para leitura: **00:03:12 min** **Dúvida**No processo de Retorno de Beneficiamento é possível inserir a mesma série (endereço) de uma remessa?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O fundamento do numero de serie é ter uma rastreabilidade e ser unico, logo uma matéria prima que tem um numero de serie que é usada na produção de outro produto não deveria herdar esta serie, pois por exemplo, o material A e serie ABC depois de produzido pode ter uma serie ABCD; salvo casos, apenas como exemplo, o numero do motor veicular como serie, onde o motor pode necessitar de um acabamento diferenciado e o proprio motor é usado em um processo produtivo e seu numero de serie não será modificado após o processo de produção, porem o sistema não tem como saber se será adotado ou não o mesmo numero de serie no produto produzido.  
  
Assim como numa produção normal de uma OP, ao ser incluida a OP, pode ser gerado o empenho deixando que o sistema use e atribua uma serie automaticamente, ou pode ser informado uma serie especifica na tela de empenhos da OP, ou ainda ser feito um empenho simples para a OP informando a serie da MP.  
  
Porem no apontamento de produção não é possivel informar uma serie do produto produzido, e o sistema não tem como saber, qual é a serie que vai ser gerada.  
  
Caso o produto produzido na OP tiver endereçamento, a produção do mesmo ficará em saldos a endereçar, e neste endereçamento é que poderá ser informado a serie e será atualizado na tabela SDB.  
  
No Processo de beneficiamento e retorno, é usado o facilitador de apontar a produção automaticamente, igual ao processo acima de apontar a produção, e no endereçamento em saldos a endereçar é que poderá ser informada a serie gerada, seja ela uma nova serie ou a mesma da materia prima usada."  
  
Desta forma, de fato por ser compreendido o processo do beneficiamento um facilitador, e a série de um produto consumida de maneira automatizada a partir do documento de entrada, a partir da sua propria entrada (SD1) e movimento interno (SD3 - RE5), o Sistema hoje possui o recurso de validar o endereço da remessa, mas não a série (esta dependeria de um endereçamento mas ele não faz parte do processo). A menos que o processo fosse manual, ou seja, o retorno fosse por fora do "Retorno Ben", entraria com o material, serializaria, e depois apontaria a produção. Mas, como este processo em si é um facilitador, o Protheus não dispõe de recurso que além de entrar com a nota, enderece e serialize para depois também automaticamente gere o RE5 e produza (tudo dentro do beneficiamento - MATA103).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)
