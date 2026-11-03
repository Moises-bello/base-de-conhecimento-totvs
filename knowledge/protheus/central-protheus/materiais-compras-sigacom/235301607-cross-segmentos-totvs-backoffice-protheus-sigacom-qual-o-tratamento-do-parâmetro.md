---
article_id: 235301607
category: Materiais - Compras (SIGACOM)
content_hash: 8322c0c89572d68a62080559af3d844ae9cfd29e7df2c7ea93a3d860d7952e33
fetched_at: '2026-06-28T22:41:24.322511+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o tratamento do
  parâmetro MV_PCEXCOT na exclusão do Pedido de Compra gerado pela rotina Análise
  de Cotação ?
type: support-article
updated_at: '2023-02-02T18:32:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235301607-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-tratamento-do-par%C3%A2metro-MV-PCEXCOT-na-exclus%C3%A3o-do-Pedido-de-Compra-gerado-pela-rotina-An%C3%A1lise-de-Cota%C3%A7%C3%A3o
---

**Dúvida**

Qual o tratamento do parâmetro MV\_PCEXCOT na exclusão do Pedido de Compra gerado pela rotina Análise de Cotação ?  
  
**Ambiente**

Protheus – Compras – A partir da 12.1.17  
  
**Solução**

* **MV\_PCEXCOT=2**

Após executar todo o processo de cotação (**SC->Gera Cot.->Atu. Cot.->An. Cot.->PC**), ao excluir o **PC** gerado pela **Análise de Cotação** o sistema restaura a **SC** utilizada no inicio do processo, deixando-a com status de **SC** **Pendente** (legenda verde). A cotação realizada até a geração do **PC** excluído não é alterada, ela continuará gravada na tabela **SC8** e aparecerá na rotina **Atualização/Análise de Cotação** com legenda vermelha (Analisada) apenas para fins de histórico. Com o parâmetro configurado desta forma o tratamento é o mesmo independente de uma cotação ter gerado nos **PCs**. Sendo assim é possível realizar todo o processo de cotação novamente com a **SC** que foi restaurada.

* **MV\_PCEXCOT=1**

Após executar todo o processo de cotação (**SC->Gera Cot.->Atu. Cot.->An. Cot.->PC**) temos dois tratamentos:

* + **A ANÁLISE GERA APENAS UM PC**: Neste caso se o **PC** for excluído a **Cotação** será reaberta e podem ser alterados os valores na rotina "Atualiza Cotação" e ela pode ser reanalisada. Não é realizada nenhuma alteração da **SC** que continua indisponível para utilização;
  + **A ANÁLISE GERA MAIS DE UM PC**: Neste caso ao excluir um dos **PCs** gerados pela análise de cotação, o sistema restaura a **SC** utilizada no inicio do processo, deixando-a com status **SC** **Pendente** (legenda verde). A cotação realizada até a geração do PC excluído não é alterada, ela continua gravada na tabela **SC8** e aparece na rotina **Atualização/Análise de Cotação** com legenda vermelha (Analisada), apenas para fins de histórico.

***Saiba Mais :***

[Nova legenda para cotações analisadas pelo processo de auditoria e que possua pedido de compra/contratos excluído parcialmente](https://tdn.totvs.com/x/1q4pJw)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
