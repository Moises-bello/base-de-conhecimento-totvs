---
article_id: 1500004318842
category: Materiais - Compras (SIGACOM)
content_hash: 0a55422d088d8be455db25512de1bc36792709e4d53045a0d5713c0935e14795
fetched_at: '2026-06-28T22:41:20.106237+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA110 - Log dos Processos
  da Solicitação de Compras
type: support-article
updated_at: '2026-02-11T17:51:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004318842-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA110-Log-dos-Processos-da-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**

Como habilitar a visualização de LOG de processos na Solicitação de Compra?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Versão12  
  
**Solução**

O processo LOG tem como objetivo acompanhar e consultar o percurso percorrido pelo pedido de compra desde a sua geração até ao seu final, uma vez recebido o documento fiscal e para os pedidos que foram incluídos após ter ativado o parâmetro MV\_HABLOG.  
  
Na interface de visualização, são mostrados os registros de cada uma das etapas pelas quais a solicitação já passou, a data, a hora e o usuário responsável pela execução da etapa; O Log de Processamento pode ser acessado na rotina de Pedidos de Compra (MATA110) através de “Outras Ações> Log de Processos”

![log.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17116255727255)

Configuração :

Para que o Log dos Processos possa funcionar é necessário ativar o parâmetro MV\_HABLOG. Lembramos que o Log passará a gravar somente as etapas que forem concluídas após a ativação do parâmetro. As etapas anteriores não serão recuperadas.

**Etapas atendidas** e que podem ser visualizadas no LOG do Processo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Etapa** | **Evento** | **Descrição** |
| **CNTA120**  **CNTA121** | PED | 5 | Inclusão PC via Medição (GCT) |
| **COMXFUN** | ATL | 2 | Exclusão da Atualização da Cotação |
| COT | 2 | Exclusão de Cotação |
| PED | 3 | Inclusão de PC via Cotação |
| PED | 4 | Exclusão PC via Cotação |
| **GCPA200** | CTR | 3 | Inclusão de Contrato via Edital |
| EDT | 1 | Vinculo de SC com item de Edital (GCP) |
| EDT | 2 | Desvinculo de SC com item de Edital (GCP) |
| **MATA094** | LIB | 1 | Inclusão de Liberação PC |
| LIB | 3 | Estorno Liberação de PC |
| **MATA103** | CLS | 1 | Classificação da Pré-Nota |
| CLS | 2 | Exclusão da Pré-Nota classificada |
| CLS | 3 | Estorno da classificação da Pré-Nota |
| **MATA110** | APR | 1 | Aprovação da Solicitação de Compras |
| APR | 2 | Aprovação da Solicitação de Compras |
| SOL | 1 | Inclusão de Solicitação de Compras |
| SOL | 2 | Exclusão e Solicitação de Compras |
| **MATA120** | LIB | 2 | Estorno Liberação de PC |
| PED | 1 | Manutenção do Pedido de Compras |
| PED | 2 | Exclusão do Pedido de Compras |
| **MATA131** | COT | 1 | Inclusão de Cotação |
| **MATA140** | LPN | 1 | Lançamento Pré-Nota |
| LPN | 2 | Exclusão Pré-Nota |
| **MATA150** | ATL | 1 | Atualização de Cotação |
| **MATA161** | ANL | 1 | Analise da Cotação |

**Tabelas** utilizadas no LOG do Processo:

* **COH** - LOG do processo de Pedido de Compra
* **COI**  - LOG do Processo de Solicitação de Compra
* **COK** - LOG por Solicitação de compra do fornecedor

***Saiba Mais:***

[Log dos Processos da Solicitação de Compras](https://tdn.totvs.com/pages/viewpage.action?pageId=504809431)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
