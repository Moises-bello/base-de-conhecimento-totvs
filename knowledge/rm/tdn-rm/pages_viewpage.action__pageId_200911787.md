---
content_hash: f80a686f8355774647bd0a1f5122928472606df85df321c6153b9884c81122c4
fetched_at: '2026-06-29T00:06:04.835530+00:00'
page_id: '200911787'
product: rm
source: tdn-rm
title: RMFIS00003_11.003 - Dicas para criação dos períodos de apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=200911787
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: 11.82.39 e superiores** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 01/09/2015 |

Para correta geração da ECF é imprescindível que os tributos IRPJ e CSLL sejam apurados pela Gestão Fiscal. É preciso ficar atento às regras abaixo para obter sucesso no processo.

**REGAS GERAIS**

1. O Tipo dos Tributos deve ser "IRPJ" e "CSLL".
2. Deve existir período de apuração encerrado para a Filial Matriz da empresa.
   1. Para confirmar a Filial Matriz, vá aos Parâmetros da Gestão Fiscal, acesse o Processo "03.02.03 - IRPJ" e vá para a Etapa "Filial Matriz".
   2. Tanto os períodos de apuração como os Parâmetros da ECF devem existir para a Filial ali encontrada.
3. Para identificar se os períodos de apuração foram encerrados no novo modelo, execute o seguinte select no banco:

*SELECT DPERIODO.IDEVCTRB*  
 *FROM DTRIBUTO, DPERIODO*  
 *WHERE DTRIBUTO.CODCOLIGADA = DPERIODO.CODCOLIGADA*  
 *AND DTRIBUTO.CODTRB = DPERIODO.CODTRB*  
 *AND DTRIBUTO.TIPOTRIBFISC IN (7, 9)*  
 *AND DPERIODO.CODCOLIGADA = 1 --altere para o valor correto dentro do seu ambiente*  
 *AND DPERIODO.CODPER >= '01/01/2014' --*altere para o valor correto dentro do seu ambiente**  
 *AND DPERIODO.FIMPER <= '31/12/2014' --*altere para o valor correto dentro do seu ambiente**

Se o campo retornado estiver NULL quer dizer que o período não foi encerrado no novo modelo. Será preciso reabrir os períodos e encerrá-los novamente para que seja o campo seja prenchido (somente a partir da versão 11.82.38). Assim o sistema irá conseguir gerar corretamente o Registro 0010 da ECF.  
   
 Na impossibilidade de execução do select, é possível verificar se o campo está preenchido pela própria visão do Período de Apuração. Basta colocar a coluna "Evento Tributário" na grid.

**REGRAS ESPECÍFICAS**

**Lucro Presumido**

* O Cadastro do tributo IRPJ/CSLL deve possuir periodicidade "Trimestral" e devem existir quatro períodos de apuração (com exceção para empresas que iniciaram a atividade no decorrer do ano).
* O Evento Tributário utilizado no encerramento dos períodos de apuração do IRPJ/CSLL deve possuir a Forma de Tributação "Lucro Presumido".

**Lucro Real Trimestral**

* O Cadastro do tributo IRPJ/CSLL deve possuir periodicidade "Trimestral" e devem existir quatro períodos de apuração (com exceção para empresas que iniciaram a atividade no decorrer do ano).
* O Evento Tributário utilizado no encerramento dos períodos de apuração do IRPJ/CSLL deve possuir a Forma de Tributação "Lucro Real".

**Lucro Real Anual**

* O Cadastro do tributo IRPJ/CSLL deve possuir periodicidade "Mensal" e devem existir 13 (treze) períodos de apuração, a saber:
  + 12 períodos para as estimativas mensais (período mensal)  
    O Evento Tributário utilizado no encerramento dos períodos de apuração das estimativas mensais deve possuir a Forma de Tributação "Lucro Real - Estimativa", podendo ou não ter levantamento de balanço.
  + 1 período para o ajuste anual (período anual)  
    O Evento Tributário utilizado no encerramento do período de apuração anual, deve possuir a Forma de Tributação "Lucro Real".

**Imune / Isenta**

* Sendo toda a atividade da empresa imune/isenta:

1. Criar o tributo IRPJ/CSLL com periodicidade anual.
2. Criar um Evento Tributário, com a Forma de Tributação "Imune" ou "Isenta". Não é preciso parametrizar as Regras Tributárias.
3. Criar um período de apuração para os tributos, com período anual e encerrar utilizando o Evento criado.

* Se houver alguma atividade que não esteja amparada pela imunidade/isenção:

1. Criar os tributos de acordo com a periodicidade de apuração: Trimestral ou Anual (seguir o exemplo do lucro real trimestral e anual).
