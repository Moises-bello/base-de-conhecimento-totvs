---
content_hash: 302cb2297c18cbe80c6f7c01445a34114036a4d2cdfb39233ba2961ee49032eb
fetched_at: '2026-06-29T00:05:57.617459+00:00'
page_id: '173084139'
product: rm
source: tdn-rm
title: RMFIS00021_Geração do registro C197 com dois códigos de ajustes distintos,
  FECP e Dif. Alíquota.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=173084139
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal             **Versão:***11.82* |
| **Processo** | **:** | EFD Contribuições - SPED FISCAL |
| **Subprocesso** | **:** | Geração do registro C197 |
| **Data da publicação** | **:** | 21/11/2014 |

***Definição do Processo***

 O objetivo deste documento é oferecer orientações sobre a implementação realizada no TOTVS Gestão Fiscal para a geração do registro C197com dois códigos de ajustes distintos, FECP e Dif. Alíquota.

***Regras Gerais***

 O sistema de Gestão Fiscal foi alterado para tratar o registro C197 quando existir situação onde é necessário informar o código de ajuste FECP referente ao diferencial de alíquotas: RJ70000006 e também o código de ajuste ICMS Diferencial de Alíquota: RJ70000002 no mesmo lançamento fiscal.

Essa alteração será aplicada para atender a nova sistemática dos débitos extra apuração. Os seguintes débitos passaram a ser feitos no Registro C197 (nota a nota):

- Imposto de Importação (RJ70000001) e seu FECP (RJ70000005)

- Diferencial de ICMS Ativo (RJ70000003), Diferencial Uso Consumo (RJ70000002) e seus respectivos FECP's (RJ70000006)

***Parametrização Necessária***

**1.** **Cadastro de Campo Complementar**

É necessário criar os seguintes campos complementares no Lançamento Fiscal:

Nome da Coluna: CODAJUSTESPEDFECP

Descrição: Código Ajuste FECP

Tipo: Alfanumérico

Tamanho: 10

Tipo Texto: Texto

Nome da Coluna: CODAJUSTESPED

Descrição: Código de Ajuste SPED

Tipo: Alfanumérico

Tamanho: 10

Tipo Texto: Texto

**2.****Realizar o lançamento que possui Dif. Alíquota e FECP sobre o Dif. Alíquota.**

Realizar o lançamento onde existe FECP sobre o Dif. Alíquota e informar os dois Códigos de Ajustes nos campos complementares criados:

       

***Geração da Rotina***

Gerar a rotina SPED Fiscal no período do lançamento fiscal criado. Como resultado o sistema gera o arquivo com dois registros C197, cada um com seu código de ajuste e valores específicos.

**Observação:**

Os somatórios de todos estes débitos extra apuração são totalizados no campo E110-15.

Todos estes débitos, juntamente com ICMS próprio a recolher (E110-13), devem ter suas guias de recolhimento descritas no Registro E116.

Este Ajuste Estará Disponível no próximo release 11.82

Versão 11.82.36
