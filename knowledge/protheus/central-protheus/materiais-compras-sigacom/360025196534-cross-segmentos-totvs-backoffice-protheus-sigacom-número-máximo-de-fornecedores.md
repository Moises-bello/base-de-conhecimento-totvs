---
article_id: 360025196534
category: Materiais - Compras (SIGACOM)
content_hash: 6afbf3260978a729f1418a8c39b77a6ffd8d06870b2ecc2a4a7bc4b990567825
fetched_at: '2026-06-28T22:41:21.957847+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Número Máximo de Fornecedores
  ao Gerar Cotação
type: support-article
updated_at: '2022-05-18T21:06:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025196534-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%BAmero-M%C3%A1ximo-de-Fornecedores-ao-Gerar-Cota%C3%A7%C3%A3o
---

**Dúvida**Como são selecionados os Fornecedores para Gerar Cotação?

**Ambiente**Microsiga Protheus – Estoque/Custos – A partir da versão 12.1.017  
  
**Solução**Na rotina de ***Geração de Cotação (MATA131***), com o ***MV\_SELFOR= S***, o primeiro parâmetro  ***'Nro Maximo de Forn.?***,  será necessário informar quantos fornecedores no máximo deseja que a cotação apresente.

O segundo parâmetro Qtos Últimos Forn.? determina se a rotina irá considerar os fornecedores com fornecimento por último dos produtos da solicitação, os demais fornecedores serão buscados na tabela de amarração produto x fornecedor SA5 até atingir a quantidade máxima.  
  
Exemplo:  
Caso seja informado 10 no primeiro parâmetro e 0 no segundo, a rotina irá buscar 10 fornecedores na SA5;

Caso seja informado 10 no primeiro parâmetro e 5 no segundo, a rotina irá trazer os 5 últimos fornecedores que geraram nota fiscal e 5 da tabela SA5;

Agora, se determina que o número máximo de fornecedores é 0, a rotina não permitirá que informe nem ao menos 1 fornecedor.

***Saiba Mais :***

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
