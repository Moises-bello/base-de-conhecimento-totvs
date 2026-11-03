---
article_id: 360036577853
category: Materiais - Compras (SIGACOM)
content_hash: 0c4e1ecc2732c9a123ee42ebcf2388616269e16ec6dccd8ef7aaa1b9f6b46696
fetched_at: '2026-06-28T22:41:20.038832+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Limitar número de Fornecedores
  na cotação
type: support-article
updated_at: '2022-10-27T11:08:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036577853-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Limitar-n%C3%BAmero-de-Fornecedores-na-cota%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:01:10 min**  
**Dúvida** Limitar número de Fornecedores na cotação

**Ambiente**Microsiga Protheus – Compras – A partir da versão 12  
  
**Solução**

Esta validação é obtida através da configuração abaixo:

Parâmetro MV\_SELFOR=S

Perguntas no F12 da rotina Gera Cotação (MATA131).

Primeiro parâmetro 'Nro Máximo de Forn.?' Necessário informar quantos fornecedores no máximo deseja que a cotação tenha;

O segundo parâmetro 'Qtos Últimos Forn.?' determina se a rotina irá considerar os fornecedores que forneceram por último os produtos da solicitação e os demais fornecedores, até atingir a quantidade máxima, \*será buscado na tabela de amarração produto X fornecedor (SA5).

EXEMPLOS APLICADOS:

Caso seja informado 10 no primeiro parâmetro e 0 no segundo, a rotina irá buscar 10 fornecedores na tabela de amarração produto x fornecedor **SA5**.

Caso seja informado 10 no primeiro parâmetro e 5 no segundo, a rotina irá trazer os 5 últimos fornecedores que geraram nota fiscal e 5 da tabela **SA5**.

Agora, se determinar que o número máximo de fornecedores é 0, a rotina não permitirá que informe nem ao menos 1 fornecedor.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao Gerar Cotação não habilita a inclusão de um Fornecedor (Inclusão Manual)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028439891)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
