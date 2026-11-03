---
article_id: 360028891312
category: RH - Contrato Intermitente
content_hash: 2dad4be7ad5a7a7e6539d9d92b726454929eb1fb2c61c68c883ebdfc57751210
fetched_at: '2026-06-28T22:43:39.999885+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Benefícios para Funcionários com Contrato
  Intermitente
type: support-article
updated_at: '2025-06-27T17:48:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028891312-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Benef%C3%ADcios-para-Funcion%C3%A1rios-com-Contrato-Intermitente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25963519208471)** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao cadastrar os benefícios para funcionários com **Contrato Intermitente** e tentar realizar o cálculo, o sistema exibe *log* de ocorrências com Registros Não Processados.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Por padrão, o Protheus **não possui tratativa** para **Plano de Saúde, Outros Benefícios, PLR, Adiantamento, 1ª e 2ª Parcela do 13º Salário** para funcionários com **Contrato Intermitente**, apenas para cálculo de **Vale Transporte, Vale Refeição, Vale Alimentação** quando houver **lançamento de convocação.****Solução**Foi implementado o Ponto de Entrada **GPM020ROT** que permite definir quais roteiros **NÃO** deverão ser validados para o calculo de funcionários com Contrato Intermitente.

****Exemplo:****

#INCLUDE "PROTHEUS.CH"  
  
User Function GPM020ROT()  
  
Local cRotInter  := PARAMIXB[1]  
  
// Roteiros que NÃO serão calculados para funcionários com contrato intermitente

// PLA, BEN, 131, 132, ADI, PLR

cRotInter := ( fGetCalcRot('C') + "\*"  + fGetCalcRot('I') + "\*" + fGetCalcRot('5') +   
"\*" + fGetCalcRot('6') + "\*" + fGetCalcRot('2') + "\*" + fGetCalcRot('F') )  
  
Return cRotInter

No exemplo acima, é definido que os roteiros PLA, BEN,131, 132, ADI e PLR **NÃO** serão validados para o cálculo de funcionários com Contrato Intermitente.   
Esta definição é feita na variável de tipo caracter ***cRotInter*** e seu conteúdo é retornado no próprio Ponto de Entrada.

**Saiba Mais**  
[RH - Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)  
[Ponto de Entrada - GPM020ROT](https://tdn.totvs.com/pages/releaseview.action?pageId=599619544)
