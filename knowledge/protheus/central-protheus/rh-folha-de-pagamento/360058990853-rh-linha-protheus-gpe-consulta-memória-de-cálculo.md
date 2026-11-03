---
article_id: 360058990853
category: RH - Folha de Pagamento
content_hash: a1487c8afad5d7c1ad50c3e5311bdeb4174a74a6eff37217cbef1dfdbcf2912b
fetched_at: '2026-06-28T22:44:14.855821+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Consulta Memória de Cálculo
type: support-article
updated_at: '2026-04-08T16:43:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058990853-RH-Linha-Protheus-GPE-Consulta-Mem%C3%B3ria-de-C%C3%A1lculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26397725830167)** Tempo aproximado para leitura: **02:00:00 min**  
 **Dúvida**Consulta da Memória de Cálculo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Na memória gerada pelo Sistema é possível consultar cálculos de:

* Médias
* Pensão
* INSS
* FGTS
* IRRF

Neste relatório é informando os **valores** e **verbas** utilizados para **composição das bases,** e **como** o sistema fez para chegar no valor descontado, facilitando a conferência do cálculo, podendo ser consultado nas rotinas abaixo:

* **Consulta de Cálculo por Funcionário** (GPEA090 - SRC)
* **Lançamentos Por Funcionário** (GPEA580)
* **Cálculo de Férias** (GPEM030)
* **Cálculo de Rescisão** (GPEM040)

**Com usar**

Para habilitar a memória de cálculo é necessário

* Habilitar o mnemônico **P\_LMEMCALC**, informando **.T.** em seu conteúdo
* Estar com ambiente atualizado de acordo com as últimas liberações do [Portal do Cliente](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)

Após atualizar o ambiente e ativar o mnemônico, é necessário **realizar o cálculo novamente** para que sejam gerados dados do cálculo para Consulta.

**Exemplo**

* No cálculo de Férias, **selecione** o funcionário desejado no *browser*  da rotina
* Acione a opção: **Outras Ações > Consultar Memória de Cálculo**
* Será apresentada uma tela listando os logs gravados para o funcionário selecionado.
  + Na rotina de Férias, serão listados apenas os logs do roteiro de Férias.

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-34-55.png?version=1&modificationDate=1565613295597&api=v2)

* + Na rotina de Rescisão, serão listados apenas os logs do roteiro de **Rescisão**
  + Na rotina de **Consulta de Cálculo** serão listados **todos** os logs existentes.
* Os registros serão listados em ordem cronológica, do cálculo mais novo para o mais antigo, de cima para baixo

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-28-41.png?version=1&modificationDate=1565612921137&api=v2)

* Ao selecionar o registro desejado, **dê duplo clique** ou ***Enter*** para visualizar em detalhe o *log*.
  + Será aberta uma nova janela com detalhes do *log*.

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-29-43.png?version=1&modificationDate=1565612983317&api=v2)

* + A tela é dividida em 3 partes.
    - Superior: possui as seguintes informações:

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-30-22.png?version=1&modificationDate=1565613023010&api=v2)

- Matrícula e Nome do Funcionário

- Data de admissão

- Situação do funcionário no momento do cálculo

- Data e hora de geração

- Usuário do sistema que realizou o cálculo

- Período, Nr. Pagamento, Processo e Roteiro do cálculo realizado.

 - Inferior Esquerda:

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-32-32.png?version=1&modificationDate=1565613152797&api=v2)

- Lista das fórmulas com log gravado.

- Ao selecionar o registro, o detalhe do log é exibido no painel direito.

  - Inferior Direita:

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-33-27.png?version=1&modificationDate=1565613208047&api=v2)

- Exibição do log da fórmula selecionada no painel esquerdo.

**Saiba Mais**  
[Melhorias Memória de Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=857576510)
