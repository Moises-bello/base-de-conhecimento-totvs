---
content_hash: 05b2014abbfe47b681c1ac223079e5298cfa2dc62b41a2c412cf3d8e86530332
fetched_at: '2026-06-29T00:08:15.867634+00:00'
page_id: '244926085'
product: rm
source: tdn-rm
title: 4. Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244926085
version: 3
---

|  |  |
| --- | --- |
| Descrição | Contabilização |
| Observações | Serão identificados os processos que poderão gerar contabilização. |

|  |  |
| --- | --- |
| **Processo** | **Ação** |
| **Contrato de Locação** | Efetivar  Desbloquear Lançamento Financeiro  Excluir Lançamento Financeiro  Voltar Situação |
| **Reajuste** | Após a execução |
| **Aditivos** | Efetivar |
| **Escalonamento** | Salvar |
| **Rescisão** | Efetivar  Cancelar |
| **Evento Financeiro Avulso** | Gerar Lançamento Financeiro  Cancelar Lançamento Financeiro  Excluir Lançamento Financeiro |

O Evento Contábil poderá ser associado ao Modelo de Contrato de Locação que por sua vez leva o default para o Contrato de Locação, ou diretamente ao Contrato de Locação. Uma vez informado um default o mesmo pode ser alterado a qualquer tempo mesmo que  o contrato de locação esteja efetivado. A contabilização sempre usará o evento contábil associado na ocasião da geração contábil, ou seja, não guardará histórico de alteração nos eventos contábeis associados ao contrato de locação, assim não será possível buscar eventos no tempo.

Terão Eventos Contábeis os processos de Contrato de Locação e Rescisão. Os demais processos como reajuste, Aditivos, Escalonamento e Evento Financeiro usarão o evento contábil associado ao contrato de locação.

Ao gerar o laçamento contábil serão consideradas como datas de referência as seguintes:

|  |  |
| --- | --- |
| **Processo** | **Data de Referência** |
| Contrato de locação | Data do contrato |
| Reajuste | Data Base do Reajuste |
| Aditivo | Data do Aditivo |
| Escalonamento | Data Inicio do Escalonamento |
| Rescisão | Data de Enceramento/ Rescisão |

**Restrições**

* Se o processo não tiver um evento contábil associado não será gerada contabilização, não será gerada mensagem de aviso da não contabilização, mantendo o padrão dos demais processos TIN.
* O contrato de locação **não** deve permitir a associação de eventos contábeis com destinações de venda, poc ou seguro prestamista.
* Em cada uma das visões de cadastros no Menu processos haverá as opções de: contabilizar, Excluir Contabilidade, Estornar Contabilidade e Solicitar Exclusão (Solicitação de Tarefa).
* A contabilização só será apresentada se o parâmetro  da coligada “**Exibe Contabilização”**estiver marcado, exceto em processos em lote como reajuste.

* Os lançamentos contábeis apresentados na tela de pré-contabilização podem ser cancelados, ter sua data de contabilização alterada assim como demais dados de acordo com permissão do perfil do usuário.
* Para contabilização linear serão gerados os valores para todos os meses do contrato de locação independente dos meses de carência, ou seja, mesmo que não haja cobrança financeira em determinado mes haverá contabilização e o valor será linearizado.
