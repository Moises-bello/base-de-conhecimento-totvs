---
article_id: 4409525022871
category: Contabilidade Gerencial - Relatórios Demonstrativos
content_hash: 89abf858f97c5998a9620d8dec0fc1a35ce096198a8b2cb4b3d9dd2cdf29b723
fetched_at: '2026-06-28T22:40:38.872533+00:00'
product: protheus
section_id: 1500001548882
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR510 - Parâmetros
  DRE
type: support-article
updated_at: '2023-03-24T17:11:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409525022871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR510-Par%C3%A2metros-DRE
---

**Dúvida**Parâmetros do relatório DRE  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - Todas as versões  
  
**Solução**

A emissão do relatório se dará de acordo com a parametrização informada.

Observe as seguintes perguntas: 

* [Posição Anterior L/P ?   e Data Lucros/Perdas ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061200054?source=search)

• Pergunta Posição antes de L/P? = SIM  - o sistema apresenta a situação da entidade antes da apuração (desconsiderando o lançamento de zeramento / apuração a entidade) , e o relatório é gerado  com saldo • Pergunta Posição antes de L/P? = NAO  - o sistema  apresenta a situação atualmente da entidade ( considerando o lançamento de zeramento / apuração a entidade) ,e o relatório é gerado  com Zerado

* Cod. Config. Livros ?

Determine qual a Configuração de Livro será utilizada neste relatório. É obrigatória a utilização de um Livro que tenha uma Visão Gerencial associada.

* Dem.Periodo Anterior?

Ao informar Sim, o Sistema considera a data atual (final) e a anterior da seguinte forma:

Considera?

* + Calendário

* + - Na pergunta Data de referência informada, temos:

Data Atual = Data de Referência

Data Anterior = Data de Referencia - (menos) 1 ano

* + - A pergunta Data de referência não informada, temos:

Data Atual = Data final do último período do calendário

Data Anterior = Data final do último período do calendário - (menos) 1 ano

* + Período

Ao preencher a pergunta Data de referência:

1. A Data Atual = Data de Referencia

2. Executa um vínculo no calendário para encontrar o período correspondente à data de referencia.

3. A Data Anterior = Data de inicio do período (mas o processo ainda não está concluido).

4. Na pergunta Considera saldo?, as opções são:

* + Mov. Período, com:

Data Anterior = Data anterior - (menos) 1 dia

* + Saldo acumulado, com:

Data Anterior - Data de inicio do período

Se a pergunta - Data de referencia não estiver informada, a impressão do relatório é cancelada.

Se a pergunta Dem. Período Anterior? estiver informada com Não, as regras anteriores valem para a data atual e anterior, porém não será impressa no relatório a coluna Período anterior.

* Consolidar Saldo

Informe se o saldo deve ou não ser consolidado.

* Saldos a Consolidar

Informe os saldos a serem consolidados. Permite selecionar de mais de um tipo de saldo, para compor o saldo das entidades gerenciais.

|  |
| --- |
| *Importante**:*  Ao informar Sim na pergunta Consolidar Saldo, o relatório será emitido de acordo com a informação da pergunta Saldos a consolidar. Se esta pergunta não for informada ou informada com outros valores, o relatório não exibirá nenhum dado. |

* Título como nome da visão

Ao configurar esta pergunta com "Sim", será impresso o nome da visão gerencial, definido na tabela CTS - Itens da Visão Gerencial.

**Saiba mais:**

[DRE parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=347445199)

[DRE Trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006850892-MP-SIGACTB-Dre-trimestral-)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA161 /CTBA130 - Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)
