---
article_id: 35787478103319
category: Materiais - Compras (SIGACOM)
content_hash: f78eab757b443c4706986049421994da425eb44c9b3775a5c08f6a8e99e48b4d
fetched_at: '2026-06-28T22:41:21.719176+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como determinar
  quantidade mínima e máxima de fornecedores ao gerar cotação no NFC?
type: support-article
updated_at: '2025-10-23T17:59:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35787478103319-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-determinar-quantidade-m%C3%ADnima-e-m%C3%A1xima-de-fornecedores-ao-gerar-cota%C3%A7%C3%A3o-no-NFC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35787478076439) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**

No Novo Fluxo de Compra, existe a possibilidade de determinar a quantidade mínima e máxima de fornecedores ao gerar cotação, conforme existia na rotina legada? Segue print abaixo da antiga rotina de Gera Cotação MATA131 onde era possível determinar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35787478077847)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
Por padrão no Novo Fluxo de Compras, não existe a possibilidade de determinar a quantidade mínima e máxima de fornecedores ao gerar cotação. Existe apenas três possibilidades, são elas: listar todos os fornecedores, listar os últimos fornecedores ou fornecedores retornados no Ponto de Entrada NFCFILFOR.

Na aba **Todos os fornecedores**será exibido uma lista com todos os fornecedores já cadastrados no Protheus, já na aba **Últimos fornecedores** podemos acessar de forma fácil os últimos fornecedores listados, conforme as últimas notas fiscais de compras, com o código do produto igual as encontradas para desta cotação. E o ponto de entrada pode customizar os fornecedores que serão listados.

**Atenção**: Para visualizar essa tela é necessário possuir o parâmetro **MV\_SELFOR** ativo (S).

![](https://tdn.totvs.com.br/download/attachments/680260500/Sele%C3%A7a%C3%B5%20de%20Fornecedores.gif?version=1&modificationDate=1712772433970&api=v2)

Referente o Ponto de Entrada mencionado acima para Filtrar meus fornecedores, seguem informações abaixo:  
**Nome do ponto de entrada**: NFCFILFOR  
**Objetivo**: Este ponto de entrada é utilizado para escolher fornecedores conforme os filtros previamente definidos. Os fornecedores filtrados serão exibidos na aba **“Meus Fornecedores”**.  
**Documentação**: [Clique Aqui - Documentação NFCFILFOR](https://tdn.totvs.com.br/display/PROT/NFCFILFOR+-+Filtrar+meus+fornecedores+NFC)

Outro ponto importante é que na **aba Todos os Fornecedores**, o parâmetro **MV\_SELFOR** é determinante na listagem de fornecedores.

Quando está **ativo como (S)**,  Na aba Todos os fornecedoresserá exibido uma lista com **todos os fornecedores já cadastrados no Protheus**

Caso o ambiente esteja configurado com parâmetro **MV\_SELFOR** inativo (N) a tela de Seleção de fornecedores será alterada e habilitará a amarração de produto x fornecedor. Exibindo os produtos e os fornecedores vinculados a ele. Para este ambiente não será possível adicionar fornecedores participantes.

![](https://tdn.totvs.com.br/download/attachments/680260500/fornecedor%20x%20produto.gif?version=1&modificationDate=1712879356293&api=v2)

Na tela Seleção de Fornecedores X Produto selecione os fornecedores vinculados ao produto como mostra a imagem abaixo.

![](https://tdn.totvs.com.br/download/attachments/680260500/fornecedor%20x%20produto%20selecionar.gif?version=1&modificationDate=1712879619353&api=v2)

**Obs.** Se o campo de Fornecedor (C1\_FORNECE) estiver preenchido na Solicitação de Compra, o sistema vai trazer somente o fornecedor que está preenchido nesse campo. Para maiores informações, consulte a documentação abaixo.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo fluxo de Compras PGCA010 (NFC) - Não é possivel visualizar alguns fornecedores ao iniciar cotação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19870973846551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-fluxo-de-Compras-PGCA010-NFC-N%C3%A3o-%C3%A9-possivel-visualizar-alguns-fornecedores-ao-iniciar-cota%C3%A7%C3%A3o)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo fluxo de Compras PGCA010 (NFC) - Não é possivel visualizar alguns fornecedores ao iniciar cotação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19870973846551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-fluxo-de-Compras-PGCA010-NFC-N%C3%A3o-%C3%A9-possivel-visualizar-alguns-fornecedores-ao-iniciar-cota%C3%A7%C3%A3o)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
