---
content_hash: 8109d140f3ad3e51ab5c43691e94a12fc2e94080c4cb68bceab5b3d80035d419
fetched_at: '2026-06-29T00:09:17.717307+00:00'
page_id: '421388626'
product: rm
source: tdn-rm
title: Fórmulas da Aplicação Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388626
version: 5
---

As fórmulas disponíveis são:  
   
1.     APLFINSALDODISP(DateTime Data)   
Descrição: Calcula o Saldo Disponível para Resgate na Data informada.  
Contexto Exigido: Registro com os Campos CODCOLIGADA e IDTIPOAPLFIN.  
   
2.     APLFINSALDOREAL(DateTime Data)  
Descrição: Calcula o Saldo Real na Data informada.  
Contexto Exigido: Registro com os Campos CODCOLIGADA e IDTIPOAPLFIN.  
   
3.     APLFINIRRESGATE(DateTime Data)  
Descrição: Calcula o Imposto de Renda para um Resgate Total na Data informada. Contexto Exigido: Registro com os Campos CODCOLIGADA e IDTIPOAPLFIN.  
   
4.     APLFINIOFRESGATE(DateTime Data)  
Descrição: Calcula o Imposto sobre Operação Financeira para um Resgate Total na Data informada.   
Contexto Exigido: Registro com os Campos CODCOLIGADA e IDTIPOAPLFIN.  
   
5.     APLFINIRCOMECOTA(DateTime Data)  
Descrição: Calcula o IR Come Cotas do período corrente até a data informada. Caso ainda não tenha nenhum encerramento de período, calcula usando como base a data da aplicação.  
Contexto Exigido: Registro com os Campos CODCOLIGADA e IDTIPOAPLFIN.  
   
6.     APLFINRENDIMENTO(DateTime DataIni, DateTime DataFim)  
Descrição: Calcula o Rendimento do período passado.  
Contexto Exigido: Registro com os Campos CODCOLIGADA e IDTIPOAPLFIN.  
   
7.     TRUNCVALOR(double Valor, int CasasDecimais)  
Descrição: Trunca um valor com o número de casas decimais informado.

Esta fórmula foi implementada por globais e por isso não foi incluída nas fórmulas do TOTVS Gestão Financeira.  
   
8.     ARREDVALOR(double Valor, int CasasDecimais)  
Descrição: Arredonda um valor com o número de casas decimais informado.

Esta fórmula foi implementada por globais e por isso não foi incluída nas fórmulas do TOTVS Gestão Financeira.  
  
9.     APLFINVALORMOV (int IDAPLFIN)  
Descrição: Retorna o valor monetário de um movimento. No caso de movimentos de impostos o valor é positivo.  
Contexto Exigido: Registro com os Campos CODCOLIGADA, IDTIPOAPLFIN e IDAPLFIN.
