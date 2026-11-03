---
article_id: 360052837513
category: Escrita Fiscal - Impostos - Cálculos
content_hash: be24e2c1d6981bb1e61f9c0dcc598391ecffd7a2aefbc8243e909cd82de22c23
fetched_at: '2026-06-28T22:39:30.581835+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Inclusão manual
  de impostos na inclusão do documento de entrada '
type: support-article
updated_at: '2021-07-29T13:28:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052837513-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Inclus%C3%A3o-manual-de-impostos-na-inclus%C3%A3o-do-documento-de-entrada
---

**Dúvida**Inclusão Manual de Impostos na Inclusão do Documento de Entrada  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Quando o parâmetro MV\_VALDESP é habilitado, o sistema permite incluir os impostos na linha do item e após ser incluído na aba "Impostos", é possível realizar alteração nesta aba. Houveram alterações nos fontes responsáveis pelos cálculos de impostos para que a pilha de recalculo seja efetuado a partir da segunda alteração manual no sistema, ou seja, após a segunda alteração manual o sistema é recalculado de acordo com as configurações de cadastros.   
  
O ideal é que os cadastros estejam corretos de acordo com a operação e cálculos de impostos necessários.  
  
O sistema valida se o campo F4\_ICM = SIM para que permita a inclusão manual de impostos. Porque entende-se que necessita dos impostos calculados para efetuar o rateio e caso o campo esteja igual a "NÃO" entende-se que não haverá impostos a ratear.  
  
Foi permitida a inclusão manual através da linha do item quando o campo F4\_ICM = Não, já que poderiam haver algumas exceções onde o usuário precisaria informar um imposto manualmente e não seria possível através da aba impostos. Foi solicitado essa exceção, já que existe notas fiscais onde o usuário possui muitos itens e tenha que cancelar o processo por causa da configuração de um item apenas.  
  
Cabe ao analista fiscal entender se no lançamento da nota fiscal analisar as configurações de impostos, para que sejam levados corretamente para aba impostos, mas se houver alguma divergência, é possível pela linha do item para que não seja cancelado todo o processo efetuado.
