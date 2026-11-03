---
article_id: 360059174393
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 760fcbc971c86c89b6ef496e42095375abca1fb32b2c8e512dab058a2c4d0df3
fetched_at: '2026-06-28T22:37:21.606229+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a Configuração
  e Revisão de Reajuste em Contratos ?
type: support-article
updated_at: '2026-04-20T17:02:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059174393-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-Configura%C3%A7%C3%A3o-e-Revis%C3%A3o-de-Reajuste-em-Contratos
---

**Dúvida**  
Como realizar a Configuração e Revisão de Reajuste em Contratos ?  
  
**Ambiente**  
Protheus – Gestão de Contratos – A partir da versão 12  
  
**Solução**

***Segue procedimentos abaixo para Configuração Na inclusão de um Contrato com Reajuste.***

**1.** Realize o Cadastro do Índice onde serão definidos os índices de correção que serão disponibilizados para escolha no cadastramento nos reajustes dos contratos.

Acesse Atualizações>Cadastros>Financeiro>Índices Econômicos**(CNTA070)**.O índice pode ser Diário Ou Mensal.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099478333)

 Índices Econômicos(CNTA070) -<https://tdn.totvs.com/pages/releaseview.action?pageId=224450512>

**2.** Realize o Cadastro do Histórico do Índice**(CNTA080)** Permite o cadastramento e a manutenção dos valores dos índices financeiros utilizados nos cálculos de reajustes de contratos.

Acesse Atualizações>Cadastros>Financeiro>Histórico de Índices**(CNTA080)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099478253)**

Histórico de Índices(CNTA080) - <https://tdn.totvs.com/pages/releaseview.action?pageId=225950359>

**3.** Na Inclusão do Contrato realize as configurações abaixo:

**a)** Configurações que devem ser realizadas na **Aba Cadastrais do Cabeçalho do Contrato**.

Acesse a Rotina Manutenção**(CNTA300)** Preencha o Campo Reajuste S/N**(CN9\_FLGREJ)=Sim** e preencha o campo Índice**(CN9\_INDICE)** com o Índice cadastrado na rotina Índices Econômicos**(CNTA070)**

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099498933)

**b)** Configurações  que devem ser  realizadas na **Planilha do Contrato**.

Na Aba **Planilha** poderá definir se a Planilha irá ou não Sofrer Reajuste para que possa ter reajuste na planilha configure os campos conforme abaixo:

Preencha o Campo Reajuste**(CNA\_FLREAJ)=** Sim

Un.Per.Reaj **(CNA\_UNIPERI)=** Se o cálculo para Data do próximo Reajuste Prox.Reaj**(CNA\_PROXRJ)** será em 1-Dias,2-Meses ou 3-Anos contando a partir da Data de início da Planilha**(CNA\_DTINI)**

Ìndice **(CNA\_INDICE)=**Vincule o Índice cadastrado na Rotina Índices Econômicos**(CNTA070)**

Períod.Reaju **(CNA\_PERI)=** Número de Dias , Meses ou Anos para Calculo da Data do Próximo Reajuste de acordo com o que foi definido no campo Un.Per.Reaj **(CNA\_UNIPERI)**

Modo **(CNA\_MODORJ)** = Se selecionar por Data, só poderá realizado o Reajuste na Data Informada no campo Prox.Reaj**(CNA\_PROXRJ).**Se no campo Modo **(CNA\_MODORJ)** = caso seja selecionado Competência, o Reajuste poderá realizado no Mês de Competência da Data Informada no campo Prox.Reaj**(CNA\_PROXRJ).**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099483493)

**c)** Configurações a serem realizadas nos **Itens da Planilha do Contrato.**

Nos Itens da Planilha poderá definir se terá ou não Reajuste nos Itens da Planilha, por padrão o campo Reajuste **(CNB\_FLREAJ)** vem em branco que é o mesmo que Sim , caso não queira que o Reajuste seja efetuado para o item em questão altere para Reajuste **(CNB\_FLREAJ)**  Não.

Também poderá ser informado um Índice**(CNB\_INDICE)** diferente para cada produto caso desejado.

**4.** Cadastre um Tipo de Revisão**(CNTA010)** em Atualizações>Cadastros>Tipos>Revisões Contrato para cadastrar um tipo de Revisão do Tipo Reajuste no campo Tipo **CN0\_TIPO = o conteúdo deve ser igual a  2**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099763533)

**Exemplo:**

**Configuração do Contrato para Realização do Reajuste**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9321316777239)

**Valor unitário do Item do Contrato antes do Reajuste**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097339374)

**Cronograma Financeiro do Contrato antes do Reajuste**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097339594)

*Dados do Contrato Antes da Revisão de Reajuste*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Índice** | **Un.Per.Reaj(CNA\_UNIPERI)** | **Períd.Reaju(CNA\_PERI)** | **Modo(CNA\_MODORJ)** | **Data do próximo Reajuste Prox.Reaj(CNA\_PROXRJ)** | **Valor unitário do Item(CNB\_VLUNIT)** |
| IGPM | Meses | 1 | Por Data | 13/12/2020 | 1.000 |

**5.** Acesse a  rotina Manutenção(CNTA300) Selecione o Contrato que será reajustado e clique em Outras>Ações>Revisões>Reajuste

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097200434)

No campo Tipo de Revisão**(CN9\_TIPREV)** selecione o Tipo de Revisão cadastrado no item 4 da Documentação.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099646073)

Na Aba Parâmetros/Revisão no campo "Data de Reajust." **(CN9\_DTREAJ)** preencha com o conteúdo do campo "Prox. Reaj" **(CNA\_PROXRJ)** da Planilha do contrato**,** pois na Planilha o campo Modo está igual a "Por Data" e o parâmetro "Ref Reajuste" **(CN9\_DREFRJ)** preencha conforme o cadastro do Histórico do Índice **(CNTA080)** desejado.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099647213)

Nesse exemplo preencher no campo Ref Reajuste**(CN9\_DREFRJ)** com uma Data do mês 12, pois, temos a competência do mês 12 cadastrado na rotina Histórico de Índices **(CNTA080)** , mas poderia-se ter escolhido a competência de outros meses caso tenha cadastro na rotina de Histórico de Índices **(CNTA080)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099478253)**

Cadastro da Planilha do Contrato

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097342854)

Parâmetros para realização do Reajuste

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099647213)

***Obs1:***

Se o campo campo Modo da Planilha  **(CNA\_MODORJ)** tivesse com conteúdo "**Por Competência"** nos Parâmetros da Revisão do Reajuste  no campo "Data de Reajust" **(CN9\_DTREAJ)** poderia ter sido preenchido com qualquer Data do mês do campo "Prox.Reaj" **(CNA\_PROXRJ)** e "Ref Reajuste"**(CN9\_DREFRJ)** o preenchimento da Data é conforme o cadastro do Histórico do Índice (CNTA080) desejado como referência para realização do Reajuste.

Para executar o Reajuste Acesse Outras>Ações>Executar Reajuste:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097343954)

*Dados do Contrato Após Reajuste*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Índice** | **Un.Per.Reaj(CNA\_UNIPERI)** | **Períd.Reaju(CNA\_PERI)** | **Modo(CNA\_MODORJ)** | **Data do próximo Reajuste Prox.Reaj(CNA\_PROXRJ)** | **Valor unitário do Item(CNB\_VLUNIT)** |
| IGPM | Meses | 1 | Por Data | 13/01/2021 | 1.110 |

**Valor unitário do Item do Contrato após Reajuste Realizado.**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099650593)

**Cronograma Financeiro do Contrato após Reajuste**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097345654)**

***Obs2:***

Vale ressaltar que o campo Próx. Reajuste **(CNA\_PROXRJ)**  é atualizado tomando como base a data informada no campo Data Reajust **(CN9\_DTREAJ)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001110862)

***Obs3:***

**Pergunta:** Um contrato depois de já cadastrado e com movimentações, tem como se alterar os campos de "Data Próximo Reajuste" (***CN9\_PROXRJ** / **CNA\_PROXRJ***) ?

**Resposta:** No caso, a alteração diretamente do campo ***CN9\_PROXRJ*** ou ***CNA\_PROXRJ*** não há disponivel no padrão do sistema, mas pode-se, através de uma revisão no Contrato do tipo "Aberta" realizar a alteração do campos ***CN9\_UNPERI*** (Un.Per.Reaju) e ***CN9\_PERI*** (Period.Reaju) cuja alteração, modificam o campo ***CN9\_PROXRJ*** e também alterar os campos ***CNA\_UNPERI*** (Un.Per.Reaju) e ***CNA\_PERI*** (Period.Reaju) cuja modificação alteram o ***CNA\_PROXRJ***.

**Obs4:**

**O que fazer quando já seguiu os passos acima  porém o contrato não sofreu reajuste como esperado?**

**R:** Uma das possibilidades é:

Não ter cadastrado o Histórico de índice na mesma competência/mês do próximo Reajuste da planilha.

Exemplo abaixo:

Data do Próximo Reajuste da Planilha "01/11/2025"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37513228034455)

Ao visualizar a rotina de histórico de índice só tinha cadastrado para mês "10/2025".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37513207565463)

Nesse caso a solução é cadastradar um Histórico de índice para competência 11/2025.

***Importante1:***

***Caso o contrato tenha medições realizadas ao executar a revisão de Reajuste o sistema cria uma nova linha com a quantidade restante que ainda não foi medida com seu novo valor reajustado e mantém como histórico na outra linha o valor antigo para as medições ja realizadas, conforme exemplo abaixo:***

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/32329292316695)***

***Importante2:***

***Se na inclusão do Contrato forem configurados os campos Reajuste S/N(CN9\_FLGREJ)=Não e o campo Índice(CN9\_INDICE) não tiver preenchido com o índice, não terá como realizar o Reajuste no Contrato e não existe Tipo de Revisão para alteração destes campos, sendo que esta configurações devem ser definidas na Inclusão do Contrato.***

***Mantenha a data base***

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099498933)

***Importante3:***

**Reajuste Retroativo**

**O reajuste retroativo está disponível apenas para revisão de contrato de compra.**

**Após a informação no Tipo de Revisão do Campo "Retroativo" (CN0\_RETRO) como "Sim",  a opção de reajustar valores de medições de compra recebidas que possuem nota de entrada será gerado um item adicional na planilha com o valor da diferença entre o medido e o reajustado, adicionando saldo a planilha e, caso exista cronograma, na próxima parcela disponível do cronograma.**

**Saiba Mais:**

* [Índices Econômicos(CNTA070)](https://tdn.totvs.com/pages/releaseview.action?pageId=224450512)
* [Histórico de Índices(CNTA080)](https://tdn.totvs.com/pages/releaseview.action?pageId=225950359)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como devo cadastrar o Histórico de Índices?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24035266833815-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-devo-cadastrar-o-Hist%C3%B3rico-de-%C3%8Dndices?source=search)
* [Revisão de Índices](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035192133-MP-SIGAGCT-Revis%C3%A3o-de-%C3%8Dndices)
* [Reajuste Automático(CNTA310)](https://tdn.totvs.com/pages/releaseview.action?pageId=333777355)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
