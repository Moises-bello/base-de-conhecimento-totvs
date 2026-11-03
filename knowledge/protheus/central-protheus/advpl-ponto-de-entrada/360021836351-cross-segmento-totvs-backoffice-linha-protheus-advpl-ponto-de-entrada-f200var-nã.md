---
article_id: 360021836351
category: ADVPL - Ponto de Entrada
content_hash: 066409b8089512af4848d9e4efaab846aabacd13b6b538950434b7099a2e1671
fetched_at: '2026-06-28T22:40:11.800381+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  F200var não chamado em modelo 1
type: support-article
updated_at: '2022-04-06T13:20:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021836351-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-F200var-n%C3%A3o-chamado-em-modelo-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao utilizar um CNAB (Centro Nacional de Automação Bancária) modelo 1 (400 *bytes*) o ponto de entrada F200VAR não é chamado.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Durante a execução da rotina FINA200 (Retorno de Cobranças), o Protheus efetua uma validação verificando se a primeira posição do tipo do registro é diferente de 1, F, J, 7 ou 2, ou se a variável lCustodia é igual a verdadeiro (.T.).

O ponto só será chamado se estas condições forem atendidas.  
  
**Solução**Pode ser utilizado o ponto de entrada F200CUS para forçar o sistema a ignorar a validação de tipo de registro, desta forma, o ponto de entrada F200VAR será chamado.  
  
**Saiba mais**  
[F200CUS e F650CUS - Ignora a validação de tipo de registro](http://tdn.totvs.com/display/PROT/DT_F200CUS_E_F650CUS_NAO_VALIDA_TIPO_DE_REGISTRO)  
[F200VAR - CNAB a receber](http://tdn.totvs.com/display/public/mp/F200VAR+-+CNAB+a+receber+--+11718)  
[FIN0025\_CNAB\_Array\_utilizado\_no\_ponto\_de\_entrada\_F200VAR](http://tdn.totvs.com/display/PROT/FIN0025_CNAB_Array_utilizado_no_ponto_de_entrada_F200VAR)
