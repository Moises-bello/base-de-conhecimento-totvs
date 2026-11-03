---
article_id: 4413951797015
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 1eda97709a96d480ef019580160cdd7a534375b3eda5ae355319e466f3a90734
fetched_at: '2026-06-28T22:37:21.679026+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como Vincular uma Solicitação
  de Compras a um Contrato ?
type: support-article
updated_at: '2025-09-08T18:54:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413951797015-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-Vincular-uma-Solicita%C3%A7%C3%A3o-de-Compras-a-um-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18258053003287) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como Vincular uma Solicitação de Compras a um Contrato no Gestão de Contratos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**

No sistema padrão, o vinculo de uma Solicitação de Compras ocorre apenas na tela de inclusão do contrato.

Atualmente não existe vinculo Solicitação de Compras com Medição do Contrato.

Na inclusão do Contrato, no momento da inclusão de um item em uma planilha, podem ser utilizadas as opções para vinculo de Solicitação de Compras ou de Item de Solicitação de compras, conforme sequência das imagens abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413951559703)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413939501975)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413939511959)

Com este vínculo a SC em questão fica com o status cor Marrom conforme imagem abaixo na rotina de Solicitações de Compras:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413939613207)

***Obs1:***

O campo C1\_QUJE é preenchido conforme as quantidades que são medidas do Contrato.

***Obs2:***

O campo C1\_XNUMCT não possui funcionalidade no padrão no SIGAGCT, não sendo utilizado no padrão do módulo.

No caso, no padrão do Gestão de Contratos, na Tabela ***SC1 - Solicitações sde Compras***, quando é feita uma importação de SC no cadastro de um contrato no SIGAGCT, nesta tabela, é gravado apenas o campo ***C1\_FLAGGCT*** com o conteúdo "1".

E além disso no Item do Contrato, na tabela ***CNB***, são gravados os dados da SC que foi importada nos campos ***CNB\_NUMSC***, ***CNB\_ITEMSC*** e ***CNB\_QTDSOL*** com o "numero", "item" e "quantidade" do item da SC vinculada no item da planilha.

***Obs3:***

O uso das opções para vínculo/importação do itens de Solicitação de Compras para os itens da planilha na inclusão do contrato, fica impossibilitado caso esteja sendo usado o tipo de planilha de Serviço do artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais as configurações para utilização de Contrato / Planilha de Serviço no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053570234-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-as-configura%C3%A7%C3%B5es-para-utiliza%C3%A7%C3%A3o-de-Contrato-Planilha-de-Servi%C3%A7o-no-Gest%C3%A3o-de-Contratos)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
