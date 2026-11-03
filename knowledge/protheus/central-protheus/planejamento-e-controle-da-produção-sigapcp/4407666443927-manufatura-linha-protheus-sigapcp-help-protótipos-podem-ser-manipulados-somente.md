---
article_id: 4407666443927
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fbb6bfcfa4d9635d1901c1824abf719410629b1dfac8b7de029bcf39a852cd07
fetched_at: '2026-06-28T22:42:43.376258+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Help: Protótipos podem ser manipulados
  somente através do módulo Desenvolvedor de Produtos (DPR)'
type: support-article
updated_at: '2021-09-02T17:24:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407666443927-Manufatura-Linha-Protheus-SIGAPCP-Help-Prot%C3%B3tipos-podem-ser-manipulados-somente-atrav%C3%A9s-do-m%C3%B3dulo-Desenvolvedor-de-Produtos-DPR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min** **Ocorrência**Ao tentar alterar um produto empenhado no **MATA380 - Empenho Simples** ou no **MATA381 - Empenho Múltiplo** no módulo do **PCP - Planejamento e Controle da Produção** é apresentado o *help* **Protótipos podem ser manipulados somente através do módulo Desenvolvedor de Produtos (DPR)**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**  
Essa mensagem ocorre pois a alteração deve ser realizada diretamente no componente no módulo do **SIGADPR - Desenvolvedor de Produto**.  
  
**Solução**Para conseguir alterar o empenho será necessário excluir a ordem protótipo e após reabrir a estrutura.  
Desta maneira a versão ficará disponível para alteração e o componente poderá ser alterado.  
  
Para isso siga os seguintes passos no módulo do **SIGADPR**:

1. Acesse a rotina **DPRA340 - Ordem Protótipo**;
2. Selecione o produto desenvolvido e a versão desejada;
3. Clique em **Outras Ações** > **Ordem Relacionadas**;
4. Selecione a ordem que deseja alterar o empenho;
5. Clique em **Outras Ações** > **Excluir**;
6. Clique em **Confirmar**, para que seja excluído;
7. Acesse a rotina **DPRA341 - Aprovação Versão**;
8. Selecione o produto desenvolvido e a versão desejada;
9. Clique em **Outras Ações** > **Reabrir Estrutura**;
10. Acesse a rotina **DPRA300 - Versão Produto**;
11. Selecione o produto desenvolvido e a versão desejada;
12. Altere os componentes desejados.
