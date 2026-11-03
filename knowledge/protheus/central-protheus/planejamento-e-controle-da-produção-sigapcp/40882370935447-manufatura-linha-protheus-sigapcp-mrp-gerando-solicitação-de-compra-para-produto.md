---
article_id: 40882370935447
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3db126469249f73a82a07c12407e2f50d97f6625f4b5805bb4dca34fb9fda0df
fetched_at: '2026-06-28T22:42:44.566489+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - MRP gerando solicitação de compra para
  produto com estrutura
type: support-article
updated_at: '2026-06-02T18:12:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40882370935447-Manufatura-Linha-Protheus-SIGAPCP-MRP-gerando-solicita%C3%A7%C3%A3o-de-compra-para-produto-com-estrutura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40882370900119) Tempo aproximado para leitura: **00:01:28 min**  
  
**Dúvida**  
Em quais condições o **MRP - Material Requiriment Planning** gera solicitação de compra para produto com estrutura cadastrada no **PCPA200 - Cadastro de Estrutura**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O **MRP** pode ter esse comportamento em algumas situações como:

* A estrutura não constar na tabela **T4N - MRP Estrutura;**
* A estrutura não ser válida para a data na qual há necessidade do produto. Na rotina **PCPA200 - Cadastro de Estrutura** avalie a data de validade dos componentes da estrutura;
* Todos os produtos componentes da estrutura estarem identificados como sendo produtos fantasma. Na rotina **MATA010 - Cadastro de produtos**, verifique se o o campo **B1\_FANTASM - Fantasma** está preenchido com **S;**
* Todos os produtos componentes da estrutura do item em questão estão bloqueados. Na rotina **MATA010 - Cadastro de produtos**, verifique se o campo **B1\_MSBLQL - Bloquei de Tela** está preenchido com **1.**

**Saiba Mais**  
Sobre a atualização da tabela T4N, verifique a documentação do [link](https://tdn.totvs.com.br/display/public/PROT/Sincronizador+do+MRP+-+PCPA140) que trata sobre a rotina **PCPA140 - Sincronizador do MRP**, e também verifique a documentação do [link](https://tdn.totvs.com.br/pages/releaseview.action?pageId=515690922) que trata da rotina **PCPA142 - Pendências do MRP**
