---
article_id: 360049532813
category: MDT - EPI
content_hash: 6972316e45b84c7a05a99a7fa0ae9fb09f2b4216effb3899e76fe4c83f1f624a
fetched_at: '2026-06-28T22:44:25.521091+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Quais são os principais parâmetros de EPI
type: support-article
updated_at: '2024-11-05T11:20:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049532813-RH-Linha-Protheus-MDT-Quais-s%C3%A3o-os-principais-par%C3%A2metros-de-EPI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25311537975575)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais são os principais parâmetros da rotina de entrega de  EPI ?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as Versões  
  
**Solução  
MV\_MDTEPIV** Permite a configuração de alertas em situações de entrega de Epi’s com data de vencimento ultrapassada.  
**MV\_NGFORPD** define um fornecedor padrão para os EPIs (Equipamentos de Proteção Individual), entregues aos funcionários.  
**MV\_NGEPIEN** alerta ou bloqueia as entregas de EPI para os funcionários caso os mesmos estejam afastados, de férias, ou tenha sido demitidos.  
**MV\_NG2EPDU** controla a emissão do alerta de Epi vencido.  
**MV\_NG2SA** habilita a geração de solicitação ao armazém ao invés de baixa no estoque.  
**MV\_NG2EPIB** indica se o EPI será bloqueado após a impressão do relatório.  
**MV\_NGMDTES** para realizar a integração com o módulo Estoque.  
**MV\_RASTRO** para controle de rastreabilidade de Lote e Sub-Lote.  
**MV\_LOCALIZ** para controle de endereçamento. Para tal controle, é necessário informar no Cadastro de Produto, qual tipo de controle será utilizado.  
**MV\_ESTNEG** Identifica se o sistema permitira que os saldos em estoque dos produtos fique negativo através de movimentação.  
**MV\_NG2U696** Indica quais são os usuários do modulo Medicina e Segurança do Trabalho podem acessar a rotina de histórico de EPI.  
**MV\_NG2KEPI** Indica se a empresa utiliza EPI em caráter complementar, mesmo quando o EPC for eficaz.   
**MV\_NG2CEPI** Indica se a empresa consiste o EPI  
**MV\_NG2CEPC**Indica se a empresa consiste o EPC  
**MV\_MDTPEPI** Tipo que define se um produto é EPI. Esse tipo deve estar definido na tabela genérica 02.  
**MV\_DBLQMOV** Data para bloqueio de movimentos. Não podem ser alterados / criados / excluídos movimentos com data menor ou igual a data informada no parâmetro.  
**MV\_NG2INTE** Indica a integração existente com o Modulo SIGAMDT com outros produtos. 1= Nao contem; 2= Logix  
**MV\_ARQPROD** O parâmetro configura se os dados de indicadores de produto serão considerados pela tabela "SB1" ou se serão considerados pela da tabela "SBZ" 

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT)  
[Artigos EPI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945554-MDT-EPI)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
