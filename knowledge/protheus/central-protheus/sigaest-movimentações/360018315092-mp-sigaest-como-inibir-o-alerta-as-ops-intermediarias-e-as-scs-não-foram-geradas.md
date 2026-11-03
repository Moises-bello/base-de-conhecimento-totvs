---
article_id: 360018315092
category: SIGAEST - MOVIMENTAÇÕES
content_hash: c8a4f99de1448406a609c0c7749893b0205b115b141640251b850d93d63241d4
fetched_at: '2026-06-28T22:38:58.570504+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - Como inibir o alerta "As OPs intermediarias e as SCs não foram
  geradas"?
type: support-article
updated_at: '2021-04-28T15:45:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018315092-MP-SIGAEST-Como-inibir-o-alerta-As-OPs-intermediarias-e-as-SCs-n%C3%A3o-foram-geradas
---

**Dúvida**Como inibir o alerta "As OPs intermediarias e as SCs não foram geradas" ao fechar a rotina MATA650 (Ordem de Produção)?  
  
**Ambiente**Microsiga Protheus – Estoque – A partir da versão 11.80  
  
**Solução**

No módulo Estoque e Custos, através da rotina "Ordens de Produção" (MATA650), ao concluir a inclusão de uma OP e fechar a rotina o sistema apresenta uma tela com a seguinte mensagem: "As OPs intermediarias e as SCs não foram geradas". Dando a opção para gerar ou não.  
  
Para que não gere as solicitações de compras no momento da abertura da Ordem de Produção, configure o parâmetro **MV\_GERASC** = **N**  
  
Para inibir o alerta, o tratamento deverá ser efetuado através da utilização do ponto de entrada **MTA650OK**.

**Saiba mais:***[MTA650OK - Inibe diálogo confirmando criação OPs e SCs](http://tdn.totvs.com/pages/releaseview.action?pageId=331852147)*

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque.*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
