---
article_id: 11901702933655
category: Materiais - Compras (SIGACOM)
content_hash: 7601555c49cbd8c6eec33734f7df2384440270c6cdf4ce5e9329b29aaeee133b
fetched_at: '2026-06-28T22:41:11.693148+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Ocorrência
  na Integração com Ativo: "Este documento não será gravado devido a inconsistências
  na gravação do ativo fixo"'
type: support-article
updated_at: '2026-05-14T17:19:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11901702933655-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Ocorr%C3%AAncia-na-Integra%C3%A7%C3%A3o-com-Ativo-Este-documento-n%C3%A3o-ser%C3%A1-gravado-devido-a-inconsist%C3%AAncias-na-grava%C3%A7%C3%A3o-do-ativo-fixo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20149002860951) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao incluir uma Nota de entrada normal com a espécie CTE ou uma nota de entrada do tipo Complemento e o tipo de complemento Frete, o sistema exibe a tela contendo a mensagem "Este documento não será gravado devido a inconsistências na gravação do ativo fixo"

![fig_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11901619900311)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - A partir da versão 12  
  
**Solução**

Foi implementado um novo processo / controle nas inclusões de Notas de Entrada, onde os valores podem ser acrescentados/aglutinados ao valor do Ativo de origem. Parâmetro **MV\_AGVLATF = .T.**

O TES em uso está configurado para controlar ativo (F4\_ATUATF = S).

O sistema conseguirá efetuar a aglutinação dos valores da compra do CTE e da compra de um serviço de garantia estendida por exemplo, no ativo de origem, porém em ambas as situações a aglutinação só ocorrerá se o ativo não estiver classificado, no módulo 01, ativo fixo.

**Nota Normal, com Compra de Garantia Estendida (Nota fiscal de serviço)**

Criada e desenvolvida nova solução que permite a inclusão de NF normal de garantia estendida ou similar vinculando ao ativo para agregar valor ao mesmo.

* Exemplo:  
  Compramos uma garantia estendida para um notebook no valor de 100,00  
  Realizamos a inclusão da NF normal inserindo o código do ativo no campo D1\_CBASEAF  
  O ativo terá o seu valor somado com o valor da garantia estendida de R$ 100,00  
  Obs: Caso preencha o campo D1\_CBASEAF com somente a base do ativo, o valor da Nota Fiscal será rateado e agregado para todos os itens  
  Caso preencha com a base + item, o valor da NF será agregado somente para o item digitado.

Caso **MV\_AGVLATF = .T.** (default), funcionará o novo comportamento descrito acima, ou seja, aglutinando o valor do cte no bem/ativo da nota de origem.  
Caso **MV\_AGVLATF = .F.** funcionará o comportamento do legado, gerando um novo bem ao incluir uma CTE com TES que controla ativo.

**Cenários a serem avaliados, quando da exibição do help na inclusão da nota :**

**1-) Para que a mensagem não seja apresentada a mensagem "Esse documento não será gravado devido a inconsistências na gravação do ativo fixo" o Ativo de origem não pode estar classificado, pois por uma validação do próprio módulo de Ativo, ativos já classificados não podem ser alterados no tocante a valores.**

**2-) Para casos onde o CTE seja incluído diretamente pelo documento de entrada e com o tipo Normal, porque por algum motivo é necessário que seja vinculado um Pedido de compras e, com isso não há vínculo da NF de origem ( compra do CTE ), o parâmetro MV\_AGVLATF precisará ficar com conteúdo .F. para que, se o TES estiver configurado como atualiza ativo = Sim, o sistema gere um novo ativo desse CTE e a aglutinação ocorra diretamente na rotina ATFA251.** [**ATFA251**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006767052-MP-SIGAATF-ATFA251-Agregar-Aglutinar-Desmembrar-bens-do-ativo?source=search)

**3-) Um outro motivo que pode gerar a exibição do help, é na reclassificação da nota de entrada. Pois se no estorno da classificação se o campo D1\_CBASEAF não foi limpo, ou seja, o número do ativo não foi apagado, o sistema tenta gravar um novo código de ativo na 2a classificação, porém como ele já encontra o D1\_CBASEAF gravado, ele não consegue gravar novamente. Nesse cenário, ou seja, do estorno da classificação é interessante garantir que o ativo inicialmente gerado, esteja deletado nas tabelas SN1 e SN3 ( processo esse que deve ocorrer com o estorno da classificação do documento de entrada ).**

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [D1\_CBASEAF](https://tdn.totvs.com/pages/viewpage.action?pageId=754968770)
* [Nota de Compra de Garantia Estendida](https://tdn.totvs.com.br/display/public/PROT/DT+Agrega+valor+de+conhecimento+de+frete+e+NF+de+garantia+estendida+em+bens+do+ativo+fixo)
* [MV\_AGVLATF](https://tdn.totvs.com/pages/viewpage.action?pageId=837857735)
