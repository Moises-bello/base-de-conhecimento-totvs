---
article_id: 360058057973
category: Materiais - Compras (SIGACOM)
content_hash: 69ba79b959e3b027d6586a13ef084a0204fb0100f1749accc2ba7fe76cebbf0a
fetched_at: '2026-06-28T22:41:18.727988+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Grupo de Aprovação
  irá considerar ou não os valores do Perfil de Aprovação?
type: support-article
updated_at: '2026-02-09T19:19:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058057973-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Grupo-de-Aprova%C3%A7%C3%A3o-ir%C3%A1-considerar-ou-n%C3%A3o-os-valores-do-Perfil-de-Aprova%C3%A7%C3%A3o
---

**Dúvida**

Como definir no Grupo de Aprovação(MATA114) se ira considerar ou não os Valores do Perfil de Aprovação(COMA210)?  
  
**Ambiente**  
Microsiga Protheus – Compras – A partir da versão 12  
  
**Solução**  
Se o campo Limite Auto **(AL\_AUTOLIM)**for configurado com conteúdo = Sim Somente os documentos que estiverem dentro dos limites definidos no perfil de aprovação serão direcionados aos aprovadores.

Se o campo **(AL\_AUTOLIM)**for configurado com conteúdo =Não

SeráIgnorado os limites definidos no perfil de aprovação e, desta forma, os documentos serão direcionados para os aprovadores mesmo que estejam fora dos limites.

Exemplo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097695593/mceclip5.png)

Por exemplo no Cadastro acima o campo Limite Auto **(AL\_AUTOLIM)** da usuária Tamiris está definido = **Sim** e o Perfil de Aprovação vinculada a usuária está com Valor Mínimo 0,01 e Valor Máximo 1.000,00.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095395754/mceclip1.png)

Já para o usuário Clovis o campo Limite Auto **(AL\_AUTOLIM)**está definido = **Não** e o Perfil de Aprovação está definido com Vl.Minimo Valor Mínimo 25.000,01 e Valor Máximo 99.999.999.999,99.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097697673/mceclip6.png)

A configuração do Grupo de Aprovação está para gerar Alçada de Pedido de compras.

Nesse exemplo foi incluído um Pedido de Compras no Valor de 6.000. Ao consultar o Log de Aprovação observe que foi gerado a aprovação apenas para o usuário Clóvis, pois, como o campo Limite Auto**(AL\_AUTOLIM)** foi definido com conteúdo = **Não**, o sistema não considerou os valores do Cadastro do Perfil de Aprovação vinculado ao usuário , independente do valor que estivesse no Perfil de aprovação iria gerar a Alçada de Aprovação para o usuário Clovis.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097697953/mceclip7.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097698293/mceclip8.png)

Não foi gerada alçada de aprovação para usuária Tamiris , pois, o campo Limite Auto **(AL\_AUTOLIM)** foi configurado = **Sim** no Grupo de Aprovação, dessa forma o sistema considerou o os valores do Cadastro do Perfil de Aprovação vinculado a usuária nos valores de Valor Mínimo 0,01 e Valor Máximo 1.000,00. Como o pedido estava no valor de 6.000 por isso não entrou para alçada de aprovação.

Saiba mais sobre o Cadastro de Grupo de Aprovação: [Grupo de Aprovação (MATA114)](https://tdn.totvs.com/pages/releaseview.action?pageId=274637723)

OBS: O mesmo se aplica para a Solicitação de Compras, portanto verificar se alguns dos campos B1\_UPRCV /  B1\_CUSTD /  B2\_CM1 estão preenchidos, caso contrário não cairá para aprovação mesmo que o campo **AL\_AUTOLIM**= SIM.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
