---
article_id: 360034126414
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: dabca213b279015989a61b19f4aa19c696d87efcc85c6934d88b748175be5bae
fetched_at: '2026-06-28T22:37:21.639469+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar Adiantamentos
  no Gestão de Contratos ?
type: support-article
updated_at: '2026-06-05T17:32:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034126414-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-Adiantamentos-no-Gest%C3%A3o-de-Contratos
---

O artigo explica como realizar adiantamentos no módulo Gestão de Contratos do Microsiga Protheus. O processo envolve incluir um contrato vigente, configurar a natureza financeira, cadastrar o adiantamento via rotina CNTA300, vincular o adiantamento a uma medição e encerrar a medição para gerar pedidos. Destaca limites para valores, possibilidade de customizações, ausência de workflow nativo para aprovação financeira e compatibilidade com contratos flexíveis que possuam previsão financeira. Links e observações complementam o procedimento.

**Dúvida**  
Como realizar Adiantamentos no Gestão de Contratos ?  
  
**Ambiente**  
Microsiga Protheus – Gestão de Contratos – A partir da versão 11.80  
  
**Solução**  
Os adiantamentos gerados por contratos, serão provisionados no financeiro com geração de titulo de pagamento antecipado (PA) para contrato de compra e (RA) para contrato de venda.

Segue procedimento para efetuar Adiantamento (PA) e /ou (RA) no financeiro, utilizando módulo de GCT.

**1.** Incluir um contrato no sistema e torná-lo vigente. Ao torná-lo vigente será gerado um título com o tipo=PR, caso o parâmetro MV\_CNPROVI esteja configurado = Sim

**2.** Incluir uma Natureza e informá-la no parâmetro **MV\_CNNATAD**. (Natureza financeira usada pelos títulos de adiantamento.) ou informar a natureza no cabeçalho do contrato o campo Natureza **CN9\_NATURE**

**3.** Incluir um adiantamento para esse contrato. Para incluir o adiantamento acesse a rotina CNTA300 > No browse da rotina posicione no  contrato ->  Outras Ações>Adiantamentos>Aba Adiantamentos conforme imagens abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044164754)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045027833)

***Obs.1:***

Referente ao valor de adiantamento que se pode realizar a inclusão, no exemplo de um contrato que já possua adiantamentos incluidos, o valor deste adiantamento que está sendo incluido no contrato **somado** aos saldos existentes dos adiantamentos neste contrato, não pode ser maior que o saldo das planlhas do contrato no momento da inclusão do adiantamento (abaixo imagem do campo que fica o saldo dos adiantamentos existentes de um contrato).

Saldos dos Adiantamentos existentes do Contrato:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31220846787095)

Saldo do Contrato:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31220846787607)

Caso esta somatória do "valor do adiantamento incluido + saldos adiantamentos existentes" seja maior que o saldo do contrato, o sistema retorna a mensagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20326042707863)

**Obs.2:**

Na inclusão do Adiantamento para que se possa gravar a data de vencimento diferente da data de emissão do PA, acesse o Configurador, selecione a tabela CNX, campo: ***CNX\_DTADT***, e em Propriedade, informe Alterar, conforme print abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407274796311)

Na manutenção do contrato, aba adiantamento, será habilitado o campo Dt. Adiant, o qual poderá informar a data de vencimento.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407274879255)

**4.** Incluir uma medição para o contrato, onde pode-se na Aba "Adiantamentos" da medição verificar o Adiantamento existente para o contrato e informar um valor do adiantamento cadastrado a ser vinculado nessa medição realizada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40609097120919)

Ao realizar este vínculo e ser confirmada a medição, será "baixado" o saldo do Adiantamento na aba "Adiantamentos" do Contrato.

**5.** Encerrar a medição para geração do pedido de compras ou vendas

**6.** Ao encerrar a medição, através do parâmetro ***MV\_CNADIA*** poderá ser configurado se o valor de adiantamento será descontado no pedido de compra ou venda gerado.

***Obs.3:***

Existe algum parâmetro ou funcionalidade para  alteração do número do título de adiantamento que será gerado no financeiro?

**R:** No padrão não existe nenhum parâmetro ou funcionalidade , caso tenha interesse em personalização do sistema. Segue abaixo os pontos de entrada do processo de adiantamento:

[CN100ANT - Gravação de Campos Customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=6089710)

[CN100ADI - Gravação dos campos customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=6089624)

***Obs.4:***

**Nova Funcionalidade.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11378298241815)

Saiba como cadastrar Adiantamento em Contratos (Nova Funcionalidade) x Compensação Automática do Título PA do Contrato com Título do Documento de Entrada através do link:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Adiantamento em Contratos (Nova Funcionalidade) x Compensação Automática do Título PA do Contrato com Título do Documento de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11735592546583-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Adiantamento-em-Contratos-Nova-Funcionalidade-x-Compensa%C3%A7%C3%A3o-Autom%C3%A1tica-do-T%C3%ADtulo-PA-do-Contrato-com-T%C3%ADtulo-do-Documento-de-Entrada-?source=search)

***Obs.5:***

**Pergunta:** Nos adiantamentos do contrato, tem como o sistema considerar a Natureza da Planilha e não o do Contrato ?

**Resposta:** Atualmente o Adiantamento do contrato não possui uma parametrização que seja considerada a natureza informada na planilha, sendo que no padrão como reportado no inicio do artigo é considerada a natureza do cabeçalho do contrato (campo **CN9\_NATURE**) e caso este esteja vazio, busca a natureza informada no parâmetro **MV\_CNNATAD** (Natureza financeira usada pelos títulos de adiantamento).

Caso se deseje pode-se avaliar a possibilidade de alteração do titulo gerado no adiantamento através de customização:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ponto de Entrada Padrão MVC para a rotina de Manutenção de Contratos CNTA300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021875031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ponto-de-Entrada-Padr%C3%A3o-MVC-para-a-rotina-de-Manuten%C3%A7%C3%A3o-de-Contratos-CNTA300)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Acervo de Pontos de Entrada do módulo Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016678671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Acervo-de-Pontos-de-Entrada-do-m%C3%B3dulo-Gest%C3%A3o-de-Contratos)

***Obs.6:***

Ao se realizar e inserir um Adiantamento no contrato, no caso contrato que possui alçada, por padrão do sistema, o contrato não retorna a alçada para ser aprovado novamente o fluxo de aprovação.

***Obs.7:***

Existe alguma forma de, ao gerar um adiantamento no SIGAGCT, ser gerado um fluxo de aprovação (workflow) para que o título financeiro do tipo PA passe por aprovação antes de ser integrado/efetivado no módulo Financeiro?

**R:** Ao incluir o título PA pelo módulo SIGAGCT (Gestão de Contratos), o título é gravado automaticamente no módulo Financeiro. Atualmente, o módulo de Gestão de Contratos não possui processo nativo de workflow de aprovação ou bloqueio do título antes da integração com o Financeiro.

Como o processo de inclusão utiliza o mesmo ExecAuto do módulo Financeiro, recomendamos validar com a equipe responsável pelo Protheus Financeiro a possibilidade de existir algum recurso, parâmetro ou customização que permita implementar um fluxo de aprovação nesse cenário.

***Obs.8:***

Existe a possibiliade de inclusão de adiantamento para Contratos do Tipo Flexível ?

R: Para contratos do Tipo Flexível do artigo abaixo

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a inclusão de um Contrato Flexível ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037640253-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-inclus%C3%A3o-de-um-Contrato-Flex%C3%ADvel)

É possível a inclusão de Adiantamento para o contrato somente se o Contrato Flexível possuir Previsão Financeira, a qual irá compor seu saldo, visto que o Adiantamento só é possivel ser realizado com valor no máximo até o saldo do contrato.

***Saiba Mais:***

[GCT0025\_Adiantamento\_GCT](https://tdn.totvs.com/display/PROT/GCT0025_Adiantamento_GCT)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Adiantamento em Contratos (Nova Funcionalidade) x Compensação Automática do Título PA do Contrato com Título do Documento de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11735592546583-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Adiantamento-em-Contratos-Nova-Funcionalidade-x-Compensa%C3%A7%C3%A3o-Autom%C3%A1tica-do-T%C3%ADtulo-PA-do-Contrato-com-T%C3%ADtulo-do-Documento-de-Entrada-?source=search)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Adiantamento no Pedido de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015664151-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Adiantamento-no-Pedido-de-Compras?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Mensagem: Documento de Entrada atrelado a título do tipo PA ao incluir uma Nota com Pedido vinculado a um PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567072-MP-SIGACOM-Documento-de-Entrada-atrelado-a-t%C3%ADtulo-do-tipo-PA-)

[CN100ANT - Gravação de Campos Customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=6089710)

[CN100ADI - Gravação dos campos customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=6089624)

[CN100ANT - Gravação de Campos Customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=6089710)

[CN100ADI - Gravação dos campos customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=6089624)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
