---
article_id: 360017514292
category: UBS - Unidade de Beneficiamento de Sementes
content_hash: 9ddc8b934313b116607cae51f244409d24db453d4632b74f8111ed3412e82a91
fetched_at: '2026-06-28T22:45:34.761619+00:00'
product: protheus
section_id: 360005696194
source: central-protheus
title: Agro - Linha Protheus - AGR - Lotes diferentes na nota de saída
type: support-article
updated_at: '2025-06-20T15:33:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017514292-Agro-Linha-Protheus-AGR-Lotes-diferentes-na-nota-de-sa%C3%ADda
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21989380728727)***Tempo aproximado para leitura: **00:00:41 min  
  
Dúvida**Por que ao gerar o pedido de venda e a nota de saída foram exibidos lotes diferentes dos que foram informados no registro da rotina **AGRA900 - Ordem de Carregamento**?  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para que a situação seja resolvida realize os seguintes passos:  
Acesse o **SIGACFG - Configurador**, ative o campo **C6\_RESERVA - Número da Reserva** para **Usado** e assinale a opção **utilizado por todos os módulos**;

**1.** Exclua os pedidos de venda e as notas de saída que foram gerados incorretamente, por meio das rotinas **MATA 410** - **Pedidos de Venda**e **MATA 460A - Documento de Saída**, respectivamente;

**2.** Acesse o registro de ordem de carregamento e exclua os itens;

**3.** Acesse a rotina **MATA 430** - **Controle de Reservas**e exclua as reservas geradas. É necessário excluir as que estão com o status **Reserva não Baixada**;

**4.** Acesse novamente o registro de ordem de carregamento e inclua os itens excluídos anteriormente. Em seguida gere novamente o pedido de venda.
