---
article_id: 4412561395095
category: Materiais - Compras (SIGACOM)
content_hash: 42472ac5b4ba2404b0efac2c75e09dff57d57f3e71163d780fa526e043fc9c43
fetched_at: '2026-06-28T22:41:11.777516+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Conceito
  do Parâmetro MV_PCEXCOT
type: support-article
updated_at: '2024-09-10T13:31:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412561395095-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Conceito-do-Par%C3%A2metro-MV-PCEXCOT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Qual o tratamento do parâmetro **MV\_PCEXCOT** na exclusão do **Pedido de Compra** gerado pela rotina**Análise de Cotação**?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Versão 12

**Solução**

* **MV\_PCEXCOT=2**

Após executar todo o processo de cotação (**SC->Gera Cot.->Atu. Cot.->An. Cot.->PC**), ao excluir o **PC** gerado pela **Análise de Cotação** o sistema restaura a **SC** utilizada no inicio do processo, deixando-a com status de **SC****Pendente** (legenda verde). A cotação realizada até a geração do **PC** excluído não é alterada, ela continuará gravada na tabela **SC8** e aparecerá na rotina **Atualização/Análise de Cotação** com legenda vermelha (Analisada) apenas para fins de histórico. Com o parâmetro configurado desta forma o tratamento é o mesmo independente de uma cotação ter gerado nos **PCs**. Sendo assim é possível realizar todo o processo de cotação novamente com a **SC** que foi restaurada.

* **MV\_PCEXCOT=1**

Após executar todo o processo de cotação (**SC->Gera Cot.->Atu. Cot.->An. Cot.->PC**) temos dois tratamentos:

* + **A ANÁLISE GERA APENAS UM PC**: Neste caso se o **PC** for excluído a **Cotação** será reaberta e podem ser alterados os valores e ela pode ser reanalisada. Não é realizada nenhuma alteração da **SC** que continua indisponível para utilização;
  + **A ANÁLISE GERA MAIS DE UM PC**: Neste caso ao excluir um dos **PCs** gerados pela análise de cotação, o sistema restaura a **SC** utilizada no inicio do processo, deixando-a com status **SC****Pendente** (legenda verde). A cotação realizada até a geração do PC excluído não é alterada, ela continua gravada na tabela **SC8** e aparece na rotina **Atualização/Análise de Cotação** com legenda vermelha (Analisada), apenas para fins de histórico.

Saiba mais em : [Parâmetro MV\_PCEXCOT](https://tdn.totvs.com/x/8830E)
