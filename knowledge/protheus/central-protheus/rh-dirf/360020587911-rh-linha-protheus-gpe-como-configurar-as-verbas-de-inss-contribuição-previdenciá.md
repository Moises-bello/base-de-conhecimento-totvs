---
article_id: 360020587911
category: RH – DIRF
content_hash: 5ba41b7e794580716d2d165ca2c691c447f5f1d18d8bdeefd206beb0ec4143b5
fetched_at: '2026-06-28T22:44:06.841214+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar as verbas de INSS (contribuição
  previdenciária) para incidência DIRF
type: support-article
updated_at: '2026-06-16T18:51:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020587911-RH-Linha-Protheus-GPE-Como-configurar-as-verbas-de-INSS-contribui%C3%A7%C3%A3o-previdenci%C3%A1ria-para-incid%C3%AAncia-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33939482502935) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Como devem ser configuradas as verbas de INSS quando os valores de INSS ficam duplicados na coluna Contribuição previdenciária da DIRF?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
As verbas de INSS para DIRF devem ser configuradas da seguinte forma:

Sobre o INSS, terão **incidência para DIRF** somente as verbas tipo Base de Ded. INSS para IR.  
  
- Identificadores   
0167 = **B**   
0168 = **B**  
0169 = **B1**  
  
As verbas tipo **Desconto do INSS** devem estar com **N** para **DIRF** (identificadores 0064, 0065, 0070).  
  
**Observação**  
Havendo entendimento de que a dedução do INSS a ser declarado deverá ser o **efetivamente** **recolhido**, deve-se configurar as verbas tipo **Base de Ded. INSS** para IR (identificadores 0167 , 0168 e 0169 ) informando **N** para a DIRF. As verbas tipo **Desconto do INSS** com os identificadores **0064,** **0065** **e 0340** devem estar para DIRF com a incidência **B** e a verba do identificador **0070 e 0401** com a incidência **B1**.   
  
**Existem duas opções:**  
Configurar as verbas de INSS desconto para enviar para DIRF ou enviar as verbas de DED. INSS BASE DO IRRF (BASE).

O trecho do boletim explica que caso escolha enviar as verbas de BASE (DED INSS BASE DO IRRF) pode ser que o valor vá acima do teto.

Qualquer uma das configurações está correta. Porém ou se deixa as verbas de Base com parametrização ou de desconto, caso todas as verbas fiquem com parametrização de B ou B1, o valor será duplicado na DIRF.  
  
Observação: A verba de ID 0232 não deve ter incidência para a DIRF mesmo que o entendimento seja que as verbas de desconto de INSS que devem ser enviadas para a DIRF.

**Saiba Mais:**  
[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
