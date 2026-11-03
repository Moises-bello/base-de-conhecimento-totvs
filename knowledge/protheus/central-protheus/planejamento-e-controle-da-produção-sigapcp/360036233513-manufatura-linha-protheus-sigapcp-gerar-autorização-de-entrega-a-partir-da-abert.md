---
article_id: 360036233513
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4010751d9faa9b00c77d1c7022c3b0cf12193eef83bdda10b4221cd31f6ba537
fetched_at: '2026-06-28T22:42:43.345642+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Gerar Autorização de Entrega a partir
  da abertura de uma Ordem de Produção
type: support-article
updated_at: '2021-05-26T19:48:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036233513-Manufatura-Linha-Protheus-SIGAPCP-Gerar-Autoriza%C3%A7%C3%A3o-de-Entrega-a-partir-da-abertura-de-uma-Ordem-de-Produ%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:00 min**  
 **Dúvida**Como configurar para gerar **Autorização de Entrega** a partir da abertura de uma **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para gerar a **Autorização de Entrega** no **MATA122 - Autorização de Entrega** o produto deve ter um **Contrato de Parceria** válido, que é cadastrado na rotina **MATA125 - Contrato de Parceria** e deve-se informar no **MATA010 - Cadastro de produtos** no campo **B1\_CONTRAT - Contrato** igual á **Sim**.   
  
No **SIGACFG - Configurador**, parametrizar da seguinte forma:

* **MV\_GERASC** **- Gera Solicitação de Compras a partir da inclusão da Ordem de Produção**igual á **T**;
* **MV\_MATRIZF - Indica se utiliza matriz de fornecimento para contratos de parceria**igual á **F**;
* **MV\_PESQCTP - Indica se a pesquisa do contrato de parceria será por produto+fornecedor+loja ou somente por produto** igual á **P**.

Desta forma invés de gerar uma **Solicitação de Compra** será gerada uma **Autorização de Entrega.**
