---
content_hash: e6d05ee41c3a8dd61bbe596301f6b27618a1f6eab7047416945b727a888f59a6
fetched_at: '2026-06-29T00:10:21.991847+00:00'
page_id: '496012330'
product: rm
source: tdn-rm
title: Cálculo da Diferença de Pensão Alimentícia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496012330
version: 20
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Folha de Pagamento |
| Função: | Diferença Salarial quando existe Pensão Alimentícia |
| Ticket: | [Ticket #4467178](https://totvssuporte.zendesk.com/agent/tickets/4467178 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue | [FOPCALCULO01-5646](http://jiraproducao.totvs.com.br/browse/FOPCALCULO01-5646); [FOPCALCULO01-7218](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-7218) |

## **02. SITUAÇÃO/REQUISITO**

Em caso de mudança no percentual de pensão alimentícia, o funcionário tenha aumento retroativo e seja necessário calcular a diferença de meses anteriores, o sistema busca  o valor de incidência de pensão atual preenchido no cadastro de dependente e não o valor de incidência utilizado nos cálculos anteriores, já que não existe um histórico para armazenamento dos respectivos cálculos.

## **03. SOLUÇÃO**

Para atender a solicitação foram adicionados no 'Movimento da Pensão de Dependente' novos campos para armazenar possíveis uso de fórmulas nos cálculos de pensão, além do percentual e ordenado bruto.

Também foi criado o "histórico de eventos não considerados" para o cálculo de pensão alimentícia vinculado ao movimento da pensão de dependentes considerando os eventos cadastrados para não ser considerados no processo do cálculo para cada mês/tipo de movimento.

O sistema passar a considerar estes campos/históricos para todas as diferenças calculadas (Salarial, Férias e 13º Salário), quando o parâmetro "Diferença de Pensão considera dados do cálculo armazenados no histórico de movimentação", estiver marcado, e a partir do mês e ano informados no parametrizador. 

Campos criados no cadastro Movimento da Pensão de Dependentes:

* **Percentual**: Armazena o percentual que está cadastrado no campo Percentual dos Dados de Pensão do cadastro do dependente e que foi utilizado para calcular a pensão do dependente.
* **Ordenado Bruto**: Retorna marcado se no cadastro do dados do dependente estiver marcado no momento do cálculo
* **Fórmula de Cálculo**: Armazena o código a fórmula de calculo utilizado para o cálculo da pensão se for o caso
* **Fórmula adicional**: Armazena o código a fórmula adicional utilizado para o cálculo da pensão se for o caso

Histórico de eventos não considerados. Ele armazena um cópia de todos os eventos e não incidências consideradas no cálculo. O mesmo é acessado através do cadastro Movimento da Pensão de Dependentes | Anexo | Históricos de eventos não considerados.

Parâmetro criado no Parametrizador em Folha Normal | Pensão Alimentícia. Também é possível definir um mês  e ano competência para considerar os dados armazenados para o cálculo:

Abaixo exemplificaremos o processo de Cálculo de diferença de pensão, usando o histórico:

Percentual, Ordenado Bruto, Eventos não Considerados, Fórmula de Cálculo, Fórmula Adiconalpasso1,passo2,passo3,passo4,passo5yespasso1nopasso2nopasso3nopasso4nopasso5
