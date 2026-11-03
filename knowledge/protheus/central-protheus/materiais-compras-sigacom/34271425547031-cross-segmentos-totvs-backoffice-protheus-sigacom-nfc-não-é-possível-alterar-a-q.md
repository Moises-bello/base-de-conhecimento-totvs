---
article_id: 34271425547031
category: Materiais - Compras (SIGACOM)
content_hash: c2f8ae9567b156d846b16eeccdd1b031cc3c861dceee079417178a316df889ab
fetched_at: '2026-06-28T22:41:20.273314+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC -  Não é possível
  alterar a quantidade C8_QUANT no Novo Fluxo de Compra.
type: support-article
updated_at: '2025-08-18T19:21:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34271425547031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-a-quantidade-C8-QUANT-no-Novo-Fluxo-de-Compra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34271394129687) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao realizar a Atualização da Cotação no Novo Fluxo de Compra, o sistema não permite alterar o valor do campo Quantidade da linha do item.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34271425505943)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12.1.2410  
  
**Causa**  
Independentemente da configuração atribuída ao campo **C8\_QUANT** no **SIGACFG** (seja para visualização ou alteração), não será possível modificar seu conteúdo.

Isso ocorre pois esse campo **C8\_QUANT** tem por função carregar a quantidade original da cotação. A quantidade que veio da solicitação na qual a cotação foi gerada.  
  
**Solução**  
Sendo assim, caso a quantidade a ser cotada for **menor**que o conteúdo do C8\_QUANT, deverá preencher essa informação no campo **C8\_QTDISP**. Caso a quantidade seja **maior**que a quantidade do campo C8\_QUANT, deverá ser incluída uma**nova solicitação de compra** com a nova quantidade correta.  
   
Por padrão, o campo **Quantidade a ser adquirida** já é preenchido com o mesmo valor do saldo disponível. O comprador - nesse campo - pode inserir um valor maior que zero e igual ou menor que o saldo disponível:  
 

| Valor Saldo | Valor Quantidade a ser adquirida | Resultado |
| --- | --- | --- |
| 30 | 30 | Ação será realizada, pois a quantidade inserida está de acordo com o saldo existente (quantidade a ser adquirida igual a saldo disponível). |
| 30 | 31 | O **usuário será alertado**, informando que a quantidade inserida é maior que o saldo disponível. Automaticamente, o sistema irá preencher o campo Quantidade a ser adquirida com o valor **30** (valor do saldo). **Deverá incluir nova Solicitação de Compras e Cotação.** |
| 30 | 15 | Ação será realizada, pois a quantidade inserida está de acordo com o saldo existente (quantidade a ser adquirida menor que o saldo disponível). |
| 30 | 0 | O usuário será alertado, informando que a quantidade inserida deve ser maior que zero. Automaticamente, o sistema irá preencher o campo Quantidade a ser adquirida com o valor **30** (valor do saldo). |
| 30 | -5 | O usuário será alertado, informando que a quantidade inserida deve ser maior que zero. Automaticamente, o sistema irá preencher o campo Quantidade a ser adquirida com o valor **30** (valor do saldo). |

[Novo Fluxo de Compras: Guia de Referência - Gestão de Compras - P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

**SAIBA MAIS EM :**

[**Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[**PÁGINA CENTRALIZADORA COMPRAS**](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[**Mais Artigos Materiais - Compras (SIGACOM)**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
