---
article_id: 360024745852
category: RH - RAIS
content_hash: 02b25d87310a252924ff072671afb2a66b3f1bef690b57d8f5e9e2475d7e44ae
fetched_at: '2026-06-28T22:44:05.698168+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - Erro quantidade de dias de afastamento maior que
  365 ou negativo no cabeçalho da RAIS
type: support-article
updated_at: '2025-09-05T12:31:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024745852-RH-Linha-Protheus-GPE-Erro-quantidade-de-dias-de-afastamento-maior-que-365-ou-negativo-no-cabe%C3%A7alho-da-RAIS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34709190729879) Tempo aproximado para leitura: 00:01:00 min  
  
Ocorrência**Sistema demonstra uma quantidade de dias de afastamento maior que 365 dias ou negativo no cabeçalho da RAIS, rotina manutenção arquivo (GPEM510).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 11  
  
**Causa**Esse erro pode ser gerado por uma falha na migração dos dados de afastamento ou atualização incorreta dos dias pagos na rotina de lançamentos/ ausência.  
  
**Solução**1. Verifique na tabela SR8 se estas matrículas para os quais constam o erro, estão com os campos:  
-R8\_DIASEMP ou R8\_DPAGOS com valores maiores que 15 dias. Estes campos não podem conter mais do que 15 dias. Necessário solicitar ao departamento pessoal a quantidade dias que a empresa deveria pagar e a quantidade de dias foram pagos efetivamente na folha do funcionário. Se o afastamento for maior que 15 dias, deve ser avaliado se é continuação de algum outro, para entender se estes campos devem estar preenchidos com 15, zerados ou com outra quantidade.

Só precisam ser ajustados os afastamentos com campo R8\_TIPO igual a O, P, Q, R ou X.  
  
Esse ajuste também pode ser realizado através do RDMAKE UPDDPGSR8:  
Doc.:*<https://tdn.totvs.com/display/public/PROT/DRHGCH-9769+-+Ajuste+campo+R8_DPAGOS+com+valor+negativo>*  
  
2. Acessar a tabela SX1 desta empresa em questão, filtrar no grupo de perguntas "GPM510", esses são os parâmetros da RAIS. O correto é ter apenas 1 pergunta neste campo, caso seu filtro retorne mais de uma pergunta, delete uma delas.  
  
3. Depois das correções acima, deve ser efetuada novamente a Geração dos dados para a RAIS (GPEM500) e depois a geração do Magnético (GPEM530).

No programa da RAIS, o arquivo importado deve ser excluído e importado novamente para não gerar duplicidade de informações.  
  
**Saiba Mais**<http://tdn.totvs.com/x/DpjHEw>
