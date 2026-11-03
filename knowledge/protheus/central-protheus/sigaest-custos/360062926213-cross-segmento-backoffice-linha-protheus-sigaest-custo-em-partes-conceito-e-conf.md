---
article_id: 360062926213
category: SIGAEST - CUSTOS
content_hash: e26e98344d0fe8d5d89e4b7b66efc8b86e8fb9f6e8abe8692fdc57663bf3a9d3
fetched_at: '2026-06-28T22:39:00.862593+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Custo em Partes -
  Conceito e Configuração
type: support-article
updated_at: '2026-06-09T15:52:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062926213-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-em-Partes-Conceito-e-Configura%C3%A7%C3%A3o
---

O artigo explica como configurar e utilizar o recurso de Custo em Partes (MA330CP) no TOTVS Protheus, detalhando o recálculo do custo médio, a criação de regras customizadas para rateio dos custos, recomendações de implantação, procedimentos e relatórios para validação, além de orientações para customizações e suporte.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26136545489559)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como configurar o Custo em Partes - MA330CP para utilização?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O **Recálculo do Custo Médio (MATA330)** possibilita dividir o custo de produtos fabricados em mais de uma parte, facilitando a visualização da composição de custos dos produtos acabados.

Este processo é chamado de **Custo em Partes**. Nele, o sistema permite dividir o custo de produtos fabricados em **até 99** partes diferentes, cada parte nas **5 moedas padrão do sistema**.

O usuário deve, através do ponto de entrada **MA330CP**definir as regras que irão classificar suas partes em decorrencia de suas movimentações. O número de partes é sempre acrescido de mais uma parte, a qual contempla os materiais que não se encontram em nenhuma regra, chamamos essa parte de "Parte Outros".

Basicamente, o Custo em partes é basicamente o desmenbramento da composição do custo médio de um produto produzido, facilitando a visualização dos custos de cada parte utilizada na produção **e não esta relacionado com o custo de reposição** **de um produto**, que envolve o custo de compra ou aquisição para reposição do estoque.

O custo das partes será apurado e distribuído durante a execução da rotina de custo médio (MATA330), por meio da chamada ao Ponto de Entrada **MA330CP**. Este ponto de entrada tem como finalidade receber e ratear os custos entre as partes, conforme as regras previamente definidas pelo cliente. Ressalta-se que essa distribuição será aplicada **exclusivamente para os custos oriundos de "notas de entrada" ou "saldos iniciais"**, não abrangendo movimentações de outros tipos.

**Wizar para criação dos campos Após compilação do ponto de entrada.**

[DT MATA330 - Wizard para criação dos campos quando utilizado o conceito Custo em Partes](https://tdn.totvs.com/pages/releaseview.action?pageId=372540775)

Deve-se aplicar o Wizard, do contrario não conseguira seguir com a instalação das procedures, sera apresentado HELP "**Não foram criados os campos no dicionario compativeis com a regra do ponto de entrada MA330CP**".

**Exemplo Hipotetico, para saber o custos das partes produzidas de um notebook de acordo com a REGRA de custo em partes usada (aqui teriamos 3 partes ja considerando que a parte 3 é a parte outros, pois no exemplo do PE usamos apenas 2 partes):**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27434890182935)

*Exemplificando o esquema acima, após ja ter COMPILADO o PE e processado o WIZARD para criação das partes.*

**Foi criado os produtos representando as partes em questão(para a parte 1  e parte 2, aqui não tratamos nada na parte sistemica "outros" no caso a parte 3).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905824523031)

**Gerado uma NOTA DE ENTRADA para os itens com exceção do PA e PI.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905824526999)

**Observe que as partes ainda não foram distribuidas, pois isso só vai ocorrer após processamento do CUSTO MÉDIO:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905824532887)

**No relatorio abaixo, demonstra-se que o produto PI e PA foram produzidos(10UNIDADES), assim sendo ocorreu o consumo dos componentes, veja como a produção ficou, ja EFETUADO O PROCESSAMENTO DO CUSTO MÉDIO: (**[**MATR860**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012330641-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR860-Interpretando-Custos-em-Ordem-de-Produ%C3%A7%C3%A3o-OP)**)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28084357750551)**

**Agora veja também, como ficou a relação do MATR979 após o processo produtivo e processamento de custo médio, observe que os custos estão distribuidos corretamente em conformidade ao que foi calculado no custo médio, onde o seu totalizador é exatamente o custo médio, e a distribuição esta efetivada corretamente de acordo a regra do ponto de entrada padrão.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905817872535)**

**Com a efetivação da virada de saldos, é assim que os custos finais/inicias do próximo período ficariam(Validação através da SB9 , mas você pode considerar a rotina "MATA225 Atual" com a criação dos campos do custo em partes como BROWSER).**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905817873687)**

**Como posso configurar cada parte do tipo do produto no ponto de entrada de custo em partes?**

Para que o sistema saiba em qual parte do custo cada tipo de produto deve ser considerado, é necessário configurar o ponto de entrada **MA330CP**. Nele, o usuário define as regras que irão classificar as matérias-primas conforme as partes do custo desejadas.

Vale lembrar que o sistema sempre inclui uma parte adicional para os materiais que não se encaixarem em nenhuma das regras definidas.

Abaixo, compartilhamos um exemplo de como esse ponto de entrada pode ser utilizado, conforme nossa documentação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31579181759511)

[MA330CP - Define regras para classificação de matéria-prima](https://tdn.totvs.com/pages/releaseview.action?pageId=6087631)

**Eu tenho saldo INICIAL dos produtos com quantidade e valores, e desejo usar o custo em partes, no próximo período em aberto, oque fazer?**

**Por boas praticas**, o custo em partes deve ser aplicado, **após a virada de saldos(ou seja em um novo periodo que ainda não tenha nenhuma movimentação)**, para que o próximo período em decorrência das novas movimentações, possuam o calculo aplicado da regra que elegeu para suas partes, assim fazendo com que no final do período, **os saldos iniciais sejam gravados corretamente.**

**Caso desejar implantar o custo em partes, em um período já aberto, onde o seus produtos ja possuam SALDOS INICIAIS no fechamento anterior**, **os saldos iniciais precisam ser ajustados previamente, de acordo sua regra de forma manual. e caso queira prosseguir dessa maneira, sugerimos o auxilio de um consultor in loco.**

**Motivo:** O custo em partes, efetiva a regra com o calculo de "Entradas", se você ja começa o periodo com saldos iniciais, e passa a ter o custo em partes no periodo em aberto, o saldo inicial ainda não tem o custo correto das partes, para que elas sejam dadas como histórico para as proximas movimentações, e isso pode ocasionar o não calculo correto das partes em suas movimentações internas.

# **As procedures do custo em partes são padrões?**

**Não**, as procedure do custo em partes **são customizadas**, o exemplo de como criar o ponto de entrada **MA330CP**, bem como configurar o uso das procedures customizadas, o cliente deve ajustar de acordo a regra que utiliza, o exemplo contido no boletim, **é apenas um exemplo estrutural de como fazer**, **por isso sempre sera solicitado que efetue o calculo de custo SEM PROCEDURES PADRÕES DE (14 a 22)**

**Isso mesmo, as procedures PADRÕES !**

Quando você POSSUI CUSTO EM PARTES, para que não sejam acionadas as procedures do CUSTO EM PARTES, e a valiação seja apenas com o ponto de entrada compilado em processamento ADVPL, pois se o problema de custeio das partes ocorrer ja SEM AS PROCEURES ATIVAS de 14 A 22, é algo pertinente a avaliação do suporte padrão e até mesmo da consultoria se necessario.

|  |
| --- |
| **Orientamos que para a validação do calculo do custo em partes, e gravações dos saldos, seja realizado sem uso das procedures de 14 a 22 (entenda, se voce tem custo em partes e as procedures estão ativas, isso significa que as procedures CUSTOMIZADAS vão ser acionadas!!! então efetuar sempre teste de processamento COM AS PROCEDURES 14 A 22 Desinstaladas).** |

**Mas eu tenho um problema, que ocorre somente com uso das procedures, sem as procedures fica certo, qual a medida a ser tratada?**

Uma vez as procedures customizadas, devera solicitar ao seu **ESN(Gerente de contas)**, a alocação de um recurso(Consultor In loco), especialista em estoque/custos e banco de dados (DBA), para identificar o calculo e gravação realizado na camada das procedures.

Importante: A partir da release 12.1.2310 é necessario reajustar as procedures customizadas

Trocando o alis da SB2 por TR2, detalhes no boletim abaixo.

[Custo em Partes - Recálculo do Custo Médio](https://tdn.totvs.com/x/tFwBLw)

**Quais relatorios podem ser utilizados para validar o custo das partes?**

* MATR978 - Kardex
* MATR979 - Custo em partes x custo medio

**Estou implantando o custo em partes agora, e enfrento duvidas com valores calculados nas partes, após efetuar um documento de entrada, ou preciso de ajuda para customizar as PROCEDURES, oque fazer?**

Para assuntos sobre **customizações TOTVS**, o time de Suporte consistirá em fornecer as documentações que possibilitem a utilização de pontos de entrada e rotinas automáticas documentadas  no portal TDN para uso no produto padrão, ou seja apenas fazemos a validação de **acionamento** do PE se esta sendo efetivado no calculo ou não.  
Caso utilize estes e o resultado seja diferente do documentado ou apresente falha na sua customização, e caso não disponha de analista programador para realizar os ajustes, dispomos do serviço do time **Hub Plataformas** (hub.plataformas@totvs.com.br).

Esta equipe oferece os serviços de criação e manutenção de fontes Protheus, que tem como característica a disponibilidade de um recurso remoto para realização desta atividade em horários comerciais (dias úteis das 08:00 às 18:00).

**Conforme detalhes em "Suporte ADVPL":** <https://tdn.totvs.com/x/R1gjIw>

**Desejo fazer a LIMPEZA das procedures customizadas do banco, como fazer?**

Se o seu objetivo é **REMOVER** as procedures customizadas, ou seja, deletar a procedure do banco, voce ira perder toda a regra existente na procedure, então **REALIZE O BACKUP** antes de fazer isso, se por alguma razão interna, voce queira remover as procedures, considere o parametro a seguir ativado, caso voce **NÃO QUEIRA REMOVER** as procedures, deixe o parametro como esta > F. [MV\_DROPPE](https://tdn.totvs.com/x/xiabEg)

**Saiba mais:**

[*MP - SIGAEST - Custo em Partes - Wizard para Criação dos Campos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062945273)

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
