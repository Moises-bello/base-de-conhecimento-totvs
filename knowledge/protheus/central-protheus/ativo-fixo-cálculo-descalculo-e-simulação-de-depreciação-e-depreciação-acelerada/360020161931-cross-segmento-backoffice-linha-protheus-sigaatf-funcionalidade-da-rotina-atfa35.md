---
article_id: 360020161931
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 1fffc95a54a072fbed8a5fa1787db82e967f49afdc95534978981dcc5ccf1290
fetched_at: '2026-06-28T22:41:43.319242+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -SIGAATF  - FUNCIONALIDADE  DA
  ROTINA ATFA350 SIMULAÇÃO DEPRECIAÇÃO '
type: support-article
updated_at: '2023-10-31T15:30:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020161931-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-FUNCIONALIDADE-DA-ROTINA-ATFA350-SIMULA%C3%87%C3%83O-DEPRECIA%C3%87%C3%83O
---

**Dúvida:**

FUNCIONALIDADE DA ROTINA ATFA350 SIMULAÇÃO DEPRECIAÇÃO

**Ambiente**Microsiga Protheus – Contabilidade Gerencial  – A partir da versão 11.80  
  
  
**Solução**

A rotina **ATFA350**,  efetua a projeção da depreciação.

A projeção de depreciação consiste em gerar os movimentos de depreciação com base nas informações atualmente disponíveis no Módulo Ativo Fixo para um período igual ou superior a um mês.

Esta funcionalidade é importante para o processo de orçamento, pois permite estimar de forma mais precisa o impacto da depreciação nas despesas do próximo exercício.

**Procedimentos**

Para efetuar a Simulação da Depreciação:

1. Em **Simulação e Projeção de Depreciação**, clique em **Incluir**.  
   É apresentada a tela com os objetivos da rotina. Clique em **Avançar**.
2. O sistema apresenta a tela para configuração dos parâmetros para a execução da rotina.

Informe nos seguintes campos:

* Código: código da Simulação.
* Revisão: versão da Simulação.
* Período Inicial: o sistema apresenta a data da última depreciação na filial corrente.
* Períodos a processar: informe os períodos a serem processados.
* Base do Bem Modificador: informe o código base dos bens modificadores dessa simulação.
* Filial de: filial inicial dos Bens a serem simulados.
* Filial Até: filial final dos Bens a serem simulados.
* Considera Bens: informe quais bens devem ser considerados na Simulação da Depreciação, que podem ser: Reais, Planejados ou Ambos.

3. Clique em **Avançar**.

4. Informe as entidades que são parte da simulação da depreciação e clique em **Avançar**.

5. Configure os modificadores da simulação, de acordo com a necessidade.

Observe o preenchimento dos campos:

* **Tipo de modificação**: selecione se o bem modificador irá influenciar positivamente (Aquisição) ou negativamente a depreciação.
* **Ação Modificadora:** selecione a ação a ser realizada:
* **Replicar:** informe se deve ser simulada a criação/baixa de um bem com o valor informado, a cada mês..
* **Dividir:** informe se o bem modificador deverá ser dividido igualmente, entre os meses da simulação e a cada mês será simulado a criação/baixa desse bem com o valor rateado.
* **Num. Período:** informe o número do período em que será simulada a criação/baixa do bem com o valor informado.
* Revisão: versão da Simulação.

|  |
| --- |
| ***Help_buttonImportante:***  Essa operação não cria o bem modificador, apenas as movimentações simulando assim as aquisições/baixas previstas no período selecionado. |

6. Clique em **Avançar**.

7. Para iniciar o processamento da Simulação, marque **Sim**. Caso queira apenas gravar as configurações, marque **Não**.

8. Clique em **Finalizar**.

A Simulação será processada.

|  |
| --- |
| ***Help_buttonImportante:***  Caso o parâmetro **F12 – Contabiliza**, esteja configurado com **Sim**, é executada a Contabilização On Line dos lançamentos 890 e 891. |

Mais informações:

[Simulação Depreciação (ATFA350 - SIGAATF)](https://tdn.totvs.com/pages/viewpage.action?pageId=312160589)

[Relatório simulação de depreciação - ATFR350](https://tdn.totvs.com/pages/viewpage.action?pageId=306852106)

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/atfa350_simulacao.htm>

* SN1 – Ativo Imobilizado
* SN3 – Saldos e Valores
* SNQ – Simulação da Depreciação
* SNR – Modificadores da Simulação da Depreciação
* SNS – Movimento da Simulação da Depreciação
