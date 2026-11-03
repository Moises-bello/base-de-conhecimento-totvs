---
article_id: 16347752937623
category: Materiais - Compras (SIGACOM)
content_hash: ad7ce6255dcfd02ee57358c3d843a2d5e2baf1d2f08b4f64056646e898b66e7a
fetched_at: '2026-06-28T22:41:11.806011+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Totvs Backoffice Linha Protheus - SIGACOM - É possível incluir
  Dois Documentos de Entrada com mesmo Número, Série, Fornecedor e Loja na mesma Filial
  ?
type: support-article
updated_at: '2023-07-27T20:04:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16347752937623-Cross-Segmento-Totvs-Backoffice-Linha-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-incluir-Dois-Documentos-de-Entrada-com-mesmo-N%C3%BAmero-S%C3%A9rie-Fornecedor-e-Loja-na-mesma-Filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16347730778007) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

É Possível haver no sistema Dois Documentos de Entrada com mesmo Número, Série, Fornecedor e Loja na mesma Filial ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras Fiscal - Todas as versões

**Solução**

Uma possibilidade existente no Padrão do sistema é quando uma das NFs é de "Formulário Próprio = Sim", e a outra NF é de "Formulário Próprio = Não"

Pois o campo de formulário também faz parte da chave única da tabela SF1 conforme print abaixo :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16347705629335)

Logo o sistema também valida se a NF é de formulário próprio ou não permitindo caso sejam este campos seja diferente entre as NFs em questão.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
