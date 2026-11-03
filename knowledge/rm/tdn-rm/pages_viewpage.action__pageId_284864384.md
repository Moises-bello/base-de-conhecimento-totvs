---
content_hash: e86902da898452a8d86ca08812b48cb9c3a1d365d91e5d414dee006fe4def0bd
fetched_at: '2026-06-29T00:08:37.032056+00:00'
page_id: '284864384'
product: rm
source: tdn-rm
title: Implementações referentes as adequações da DIME/SC - 2017
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284864384
version: 12
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Fiscal |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | Implementações referentes as adequações da DIME/SC | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.18 | **Réplica** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colômbia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>* | | |

## Objetivo

Implementar as adequações referentes as atualizações da DIME/SC - A partir de Abril de 2017

Legislação:

<http://legislacao.sef.sc.gov.br/html/portarias/2017/port_17_070.htm>

**WikiHelp da rotina: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.Dime.aspx>**

**Implementações**

**Cadastro de Outros Débitos/Créditos**

Foram criados dois novos Sub-Tipos para os Lançamentos de Outros Débitos e Créditos.

Segregação Débitos com Crédito Presumido  
Segregação Crédito Presumido

**Processo de Encerramento do Período de Apuração**

Foi ajustado o Processo de Encerramento de Período de Apuração do Tributo de ICMS para poder

contemplar estes novos Sub-Tipos.

**Geração da Rotina Estadual - DIME/SC**

Registro Tipo 30 – Cálculo do Imposto a Pagar ou Saldo Credor (Quadro 09)

Inclusão do Campo 36 (+) Segregação do Crédito Presumido Utilizado em Substituição aos Créditos pelas Entradas.

Deve ser preenchido com o valor do crédito presumido apropriado em substituição aos créditos pelas entradas, informado no DCIP de crédito presumido com subtipo específico, relativas às respectivas saídas em operação ou prestação efetivamente ocorridas no período de referência da DIME. Este valor será transportado para o item 030 (Crédito Presumido Utilizado em Substituição aos Créditos pelas Entradas) do Quadro 14 (Demonstrativo da Apuração do Imposto Devido pela Utilização de Crédito Presumido em Substituição aos Créditos pelas Entradas) para apurar o imposto separadamente conforme disposto no inciso V do art. 23 do Anexo 2 do RICMS/SC-01.

**Será gerado com o Lançamento de Outros Criar um Sub Tipo “Segregação Crédito Presumido” nos Lançamentos de Outros Débitos\Credito.**

Inclusão do Campo 76 (+) Segregação dos Débitos Relativos às Saídas com Crédito Presumido em Substituição aos Créditos pelas Entradas.

Deve ser preenchido com o valor dos débitos das saídas beneficiadas pelo crédito presumido em substituição aos créditos pela entrada, contidos no Item 010 (Débitos pelas Saídas) do Quadro 04 (Resumo Apuração dos Débitos) no período de referência da DIME. Este valor será transportado para o item 020 (Débitos Relativos às Saídas com Crédito Presumido em Substituição aos Créditos pelas Entradas) do Quadro 14 (Demonstrativo da Apuração do Imposto Devido pela Utilização de Crédito Presumido em Substituição aos Créditos pelas Entradas) para apurar o imposto separadamente conforme disposto no inciso V do art. 23 do Anexo 2 do RICMS/SC-01.

**Será gerado com o Lançamento de Outros Criar um Sub Tipo “Segregação Débitos com Crédito Presumido” nos Lançamentos de Outros Débitos\Credito.**

Registro tipo 35 – Demonstrativo da Apuração do Imposto Devido pela Apropriação de Crédito Presumido em ST aos Créditos pelas Entradas (DAICP) (Quadro 14)

Criação do Novo Registro:

| Código | Descrição | Origem |
| --- | --- | --- |
| 010 | Valor da Base de Cálculo das Saídas com Crédito Presumido | Gerado conforme informação da Tela de geração da Rotina. Campo “BC da Saída com Crédito Presumido” |
| 020 | (+) Débitos Relativos às Saídas com Crédito Presumido em Substituição aos Créditos pelas Entradas | Gerado conforme o Lançamento de Outros Debito\Credito com o Tipo Crédito e Sub Tipo “Segregação Débitos com Crédito Presumido” Obs: Mesmo campo gerado no Quadro 09. Item 076. |
| 030 | (-) Crédito Presumido Utilizado em Substituição aos Créditos pelas Entradas | Gerado conforme o Lançamento de Outros Debito\Credito com o Tipo Debito e Sub Tipo “Segregação Crédito Presumido” Obs: Mesmo campo gerado no Quadro 09.Item 036. |
| 040 | (=) Saldo Devedor Apurado pela Apropriação do Crédito Presumido no Mês | Calculado preencher com o valor da diferença entre o item 030 e o item 020, se o total de débitos for maior que o total de créditos.  Preencher com 0 (zero) quando o resultado for igual a 0 (zero) ou quando o total de débitos for menor que o total de créditos. |
| 199 | (=) Imposto a Recolher pela Utilização do Crédito Presumido | Gerado com o mesmo valor do Campo 040. |

**Obs.:** Alterações validas para Período de Geração maior que Abril de 2017

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
