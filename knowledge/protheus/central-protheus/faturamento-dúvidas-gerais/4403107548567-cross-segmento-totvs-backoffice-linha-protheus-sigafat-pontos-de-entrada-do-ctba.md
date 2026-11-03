---
article_id: 4403107548567
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 134cc1ad96881c70d92c499158f5efb20ec37a20b2aabfda4923c6485a61c598
fetched_at: '2026-06-28T22:38:28.645309+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de entrada
  do CTBANFS
type: support-article
updated_at: '2021-06-23T11:34:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403107548567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-do-CTBANFS
---

**Dúvida**Quais são os pontos de entrada do **CTBANFS** -  contabilização do módulo faturamento?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Os  pontos de entrada existentes na rotina CTBANFS são:

**CTBNFS** - permite a manipulação da query . 

Exemplo de uso:

User Function CTBNFS()

If PARAMIXB<>Nil

aSelect := PARAMIXB[1]

aFrom : PARAMIXB[2]

cWhere := PARAIXB[3]

//Aqui eu adiciono o campo especifico da TES.

Aadd(aSelect,{”F4\_MEUTS”,"C",3,0})

//Aqui eu adiciono o campo especifico do Produto

Aadd(aSelect,{”B1\_MEUPRD”,"C",15,0})

//Aqui eu adiciono o campo especifico do Cliente

Aadd(aSelect,{”B1\_MEUSA1”,"C",6,0})

Return({aSelect,aFrom,cWhere})

Else

Return(PARAMIXB)

EndIf

**CTNFSFIL**- o campo **F2\_DTLANC** sempre será atualizado com a data de processamento, mesmo que não seja gerado lançamento contábil na tabela CT2. Esse procedimento é utilizado para evitar reprocessamento indevidos de movimentos já avaliados pela rotina. Existe a opção de contorno utilizando o ponto de entrada **CTNFSFIL**  
  
Segue exemplo de utilização do ponto :  
*User Function CTNFSFIL()*  
*Local cFilAux := ParamIxb[1]*  
*Local lRet := .T.*  
*If "RPS" $ (cFilAux)->F2\_ESPECIE*  
*lRet := .F.*  
*EndIf*  
*Return lRet*  
O retorno *falso* não contabiliza.

**CTNFSDT**- permite alterar a data base para que o lançamento do documento de saída seja contabilizado(Off Line) com a data desejada. - [https://tdn.totvs.com/x/EIAnBQ O ponto de entrada](https://tdn.totvs.com/x/EIAnBQ)

**CTBAPED** - O ponto de entrada CTBAPED realiza a customização no momento de contabilizar os itens do pedido de vendas (SC6) - <https://tdn.totvs.com/x/KIZn>

Saiba mais de Contabilização offline: ***[Integração Faturamento X SigaCtb (SIGAFAT)](https://tdn.totvs.com/x/W2nXIQ)***
