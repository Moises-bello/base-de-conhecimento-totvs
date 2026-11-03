---
article_id: 360015664151
category: Materiais - Compras (SIGACOM)
content_hash: d57285768d9ab74e2bd68fbba3ac9a045ea64b6819b402c1955d1ad19578421d
fetched_at: '2026-06-28T22:41:07.357274+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - Adiantamento no Pedido
  de Compras
type: support-article
updated_at: '2026-05-14T18:34:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015664151-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Adiantamento-no-Pedido-de-Compras
---

**Dúvida**  
Como Incluir ou Excluir o relacionamento do Pagamento Antecipado ( PA ) no Pedido de Compras ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as Versões  
  
**Solução**

Os seguintes dados devem ser cadastrados previamente, antes de incluir um Pedido de Compras:

1. Acesse o módulo Compras, selecione Atualizações / Cadastros / Fornecedores (MATA020) e inclua um fornecedor;
2. Em Atualizações /Cadastros / Produtos (MATA010), inclua um produto;
3. Em Atualizações /Cadastros / Cond. De Pagamento (MATA360), inclua uma condição de pagamento e informe “Sim” no campo Adiantamento;
4. Em Atualizações /Cadastros / Tipos de Ent./Saída (MATA080), inclua uma TES com código 001 e que gere duplicata.
5. Para compensação automática do titulo PA com o titulo gerado na NF com o Pedido de Compras ([Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Mensagem: Documento de Entrada atrelado a título do tipo PA ao incluir uma Nota com Pedido vinculado a um PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567072-MP-SIGACOM-Documento-de-Entrada-atrelado-a-t%C3%ADtulo-do-tipo-PA-)), antes da inclusão do Título PA, na rotina de "Contas a Pagar" (FINA050), é uma premissa e deve-se configurar os parâmetros F12 da rotina conforme abaixo:

**Gerar Chq. p/Adiant.?= NÃO**  
**Mov. Banc. sem Cheque?= SIM**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14325928877591)

**Obs**:

Ao Configurar os perguntes conforme Acima, quando incluir o Título do PA , ao visualizar o título na rotina FINA050 e clicar em Outras Ações>posição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26897901758871)

Conforme imagem acima é demonstrado que foi incluso o Movimento do Pagamento Antecipado na Inclusão do Título do PA, pois, o pergunte **Mov.Bancário Sem cheque** está igual a **Sim**, somente com o Movimento de Pagamento Antecipado será realizado a compensação automática na entrada da nota com o título Gerado.

Esta configuração dos perguntes F12 da inclusão de título (FINA050), se trata de uma Premissa para o uso da funcionalidade de Adiantamento no Pedido de compras e Compensação Automática dos títulos ao incluir do Doc de Entrada onde em caso de não utilização pode-se não ocorrer a compensação automatica por não ocorre corretamente o vínculo de Pedido e PA, ou outras intercorrências.

**Importante**:

O adiantamento é relacionado a **Filial** em que se esta inserindo o pedido de compra, independente da filial de entrega.

Para garantir o correto processo de compensação no documento de entrada, todas as informações devem estar na mesma filial, ou seja, o Pedido com Adiantamento, Pedido de Compras e a Nota Fiscal precisam estar associados à mesma Filial.

         6.Pedido de Compras;

Em Atualizações / Pedidos / Pedidos de Compras (MATA121) e inclua um Pedido de Compras com as seguintes características:

* Selecione o Fornecedor código 000001 e loja 01;
* Selecione a Condição de pagamento código 001, com campo Adiantamento = “Sim”;
* Selecione o Produto código PRODUTO1 e utilize o preço unitário de R$10,00;

Defina a quantidade de 10 unidades. Valor total do Pedido R$100,00.

1. 1. Clique em "Outras Ações – Adiantamento" para incluir ou relacionar adiantamentos deste fornecedor e loja.
   2. Caso não exista adiantamento para este fornecedor e loja, marque a opção Incluir adiantamento.
   3. É exibida a tela de Contas a Pagar (FINA050), inclua um título a pagar usando tipo de título “PA”.

![20211025_075630.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411436704663)

Se houver tentativa de alterar o título na rotina Contas a Pagar, o sistema apresentará o alerta abaixo:

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010622172)

Caso após criar o PA houver necessidade de desvincular, é possível retirando a seleção do PA na mesma tela de adiantamento no Pedido em Outras Ações:

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010643831)

         7. Documento de Entrada;

Ao realizar a inclusão de um Documento de Entrada, vinculando o Pedido de Compras, uma TES que gera duplicata e a Cond. Pagto do Pedido com Adiantamento, incluidos conforme as instruções acima, haverá a compensação automatica do Titulo PA vinculado ao Pedido, com o Título a Pagar da NF que acabou de ser incluida.

***Observações :***

**1)** O vínculo entre o Pedido de Compras e os Adiantamentos são gravados dentro da tabela FIE. Quando a nota for incluída, com esse PC vinculado, aí o sistema grava as informações na tabela FR3.

**2)** Pelo conceito da rotina, no caso de pedido/título inseridos em outra Moeda (Dólar, por exemplo) na tela de vinculo dos Titulos com o Pedido ela traz os valores dos documentos com o valor convertido em Reais que é moeda corrente do sistema, e não em Dolar (Moeda 2).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18909913223191)

Dessa forma, na tela tanto o "Valor Limite" quanto o "Valor Selecionado", pelo padrão, são trazidos no valor convertido em Reais e assim é feita a comparação desses valores, sendo que se o "Valor Selecionado" for maior que o limite haverá a mensagem impedindo vinculo de valor maior que o Pedido.

No caso, se os documentos forem de datas diferentes em que a taxa de conversão for diferente, poderá ocorrer a mensagem de valor limite excedido, visto que essa comparação é realizada no valor convertido em Reais.

**3)** Caso seja necessário desabilitar a opção de incluir Pagamento antecipado e somente deixar disponível a opção de vincular, há um ponto de entrada dentro da rotina **FINXAPI**, a qual é chamada nesse momento, é o **PVADTINC** :

<https://tdn.totvs.com/pages/releaseview.action?pageId=160105847>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4459033755287)

**4)** No momento de marcar o título PA que precisa ser vinculado ao Pedido de compras, o sistema solicitará através da abertura da tela abaixo, que o usuário preencha de forma manual, qual o valor do PA deve ser vinculado ao PC, considerando que o título PA tenha um valor maior que o PC.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22148180500631)**

Porém ao tentar vincular o valor o PA, maior que o pedido de compras, em um primeiro momento, ele permite o vínculo, porém ao clicar em salvar,  o sistema não permite, emitindo uma tela de alerta e a partir do daí, o usuário precisa verificar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22148197408151)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22148180528919)**

**5)** Para situações onde o PA possui um valor maior que a parcela, o sistema baixa o valor da primeira parcela automaticamente. Porém, para que haja baixa das próximas parcelas, será necessário que o usuário baixe manualmente na rotina FINA340 no módulo do financeiro.

No exemplo abaixo, inclui um pedido de compras com valor total de 10.000,00 reais com PA de 4.000,00 reais. Utilizei uma condição de pagamento para 5 parcelas (sendo que a primeira é à vista).

Após incluir o pedido de compras com a PA, a tabela FIE foi populada com o registro do print abaixo (com o valor total do PA vinculado ao Pedido):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18503956408599)

Após incluir o documento de entrada, o registro foi atualizado da seguinte forma (ficando com apenas o valor compensado automaticamente da primeira parcela):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18503956418455)

Para que a segunda parcela seja baixada com o saldo do PA, será necessário acessar a rotina FINA340 Compensação de títulos do módulo financeiro e realizar a compensação manual da parcela B.

**Obs:**

* O saldo que sobrará no título do PA poderá ser utilizado para compensação em outras notas, por isso que as demais parcelas não são compensadas automaticamente.
* Caso se necessite apoio na utilização das rotinas de Compensação Manual do módulo Financeiro (FINA340, FINA750), orienta-se a verificação junto ao suporte ao módulo SIGAFIN.

**6) Para desfazer o processo da compensação automática entre o título PA e o título NF, gerado pela nota, é necessário excluir a nota de entrada ou estornar a classificação da mesma, sendo esta a única possibilidade de estorno da compensação automática no padrão do sistema nesta funcionalidade.**

**7)** O "Valor Limite" da tela de vínculo do PA com o Pedido é o total do pedido menos o que ja foi atendido. E o no que foi atendido pode-se somar os valores de impostos através do parâmetro MV\_CALIMP.

Documentação parametro MV\_CALIMP:  
<https://tdn.totvs.com.br/display/public/PROT/15546571+DMANMAT02-40492+DT+Valor+Limite+no+relacionamento+de+adiantamentos>

Documentação Adiantamento (Financeiro):  
<https://tdn.totvs.com.br/display/public/PROT/Adiantamento+no+Pedido+de+Compras>

**8)** No caso de título Nota Fiscal de Entrada que possui impostos, como exemplo o PCC (Pis, Cofins e CSLL) e que a geração dos titulos de impostos ocorre na Baixa do título (com ***MV\_BX10925 = 1***), para que sejam gerados os títulos de impostos na baixa pela Compensação Automática com o PA, deve ser habilitado o parâmetro ***MV\_IMPCOM = .T.*** do módulo Financeiro.

Abaixo, seguem links do módulo Financeiro pertinentes ao uso do parâmetro MV\_IMPCOM e sobre a compensação automática, para melhores esclarecimentos.  
\* Parâmetro MV\_IMPCOM: <https://tdn.totvs.com/pages/viewpage.action?pageId=628112424>

\* Compensação Automática: <https://tdn.totvs.com/pages/viewpage.action?pageId=511545788>

**9)** No caso de Pedido que possui processo de alçada envolvido é recomendado o vínculo do PA ser realizado no momento da Inclusão do Pedido, pois na opção de "Alterar", o pedido retornará a alçada, sendo necessário esta alçada ser aprovada novamente caso já havia sido aprovada, conforme o conceito do processo de alçada do sistema reportado no artigo abaixo.

Nesta situação, no padrão atual do sistema, não há uma forma de se vincular um PA através da opção de "Alterar" sem que o bloqueio de alçada retorne ao ínicio, podendo ser analisada a possibilidade de tratamento através customização conforme também reportado no artigo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA121 - É possível alterar um Pedido de compras liberado sem que ele caia em Alçada novamente?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20292164032663-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA121-%C3%89-poss%C3%ADvel-alterar-um-Pedido-de-compras-liberado-sem-que-ele-caia-em-Al%C3%A7ada-novamente)

**10)**O sistema possui algum bloqueio que impeça a inclusão de Títulos no Contas a Pagar quando o Pedido de Compras estiver bloqueado?

**R:**O processo de inclusão de título no Contas a Pagar pela opção **Outras Ações > Adiantamento** do Pedido segue a mesma lógica de uma inclusão manual de título no financeiro.  
Por conceito do sistema, não existe atualmente nenhuma configuração que bloqueie a inclusão de títulos antes da aprovação do Pedido de Compras.

Temos o ponto de entrada que á acionado na Inclusão de títulos pela Opção Adiantamento do Pedido de compras:

[F050ADPC - Valida a inclusão de um título de adiantamento quando este é gerado a partir do Pedido de Compras no módulo SIGACOM](http://tdn.totvs.com/pages/releaseview.action?pageId=6071668)

Segue lista completa dos pontos de entrada da rotina Contas a Pagar.

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Pontos de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031234634-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Pontos-de-Entrada)

**Obs:** Dúvidas em algum ponto de entrada da rotina FINA050, acione por gentileza equipe protheus financeiro.

**11)** No Processo/passo da inclusão do Documento de Entrada, caso seja necessário alterar a condição de pagamento utilizada na NF. A nova Condição de Pagamento utilizada deve também possuir a configuração de **"Adiantamento=Sim"**, para que haja corretamente a compensação automática da funcionalidade.

**12)** Caso seja realizado o Processo de vinculo de PA no Pedido de Compras, para a compensação automática dos titulo de PA e da NF, a funcionalidade padrão não possui uma opção para que não seja realizada esta baixa/compensação dos títulos em alguma determinada situação caso se deseje. Neste caso, não se deve vincular o titulo de PA ao Pedido de Compras e nem usar a Cond. Pagto com configuração de Adiantamento para então se fazer a baixa/compensação de forma manual.

**13)** No caso de NFs de Entrada que tiverem a geração de título(s) financeiro(s) de impostos, estes Títulos de Impostos não serão compensados automaticamente pela funcionalidade, a qual faz a compensação apenas do título da NF com o título de PA.

**14)**Por padrão, é possível executar a compensação automática de PA e Títulos a Pagar em filiais distintas, existe  ponto de entrada para esse processo?

**R:** Atualmente, no padrão do sistema/rotina da funcionalidade de Adiantamento no Pedido de Compras, não há verificação de funcionalidade ou configuração que permita a compensação automática entre filiais distintas.

No comportamento padrão, para garantir o correto processo de compensação no documento de entrada, é necessário que todas as informações estejam vinculadas à mesma filial. Ou seja, o Pedido com Adiantamento, o Pedido de Compras e a Nota Fiscal devem estar associados à mesma filial.

Não foi identificado um ponto de entrada específico para tratamento desse cenário.

***Saiba Mais :***

[Adiantamento no Pedido de Compras](https://tdn.totvs.com/x/bhlaKg)

[PCOM04023 - Adiantamento no Pedido de Compras](https://tdn.totvs.com/display/public/PROT/PCOM04023+-+Adiantamento+no+Pedido+de+Compras)

[MP - SIGACOM - Pedido de Compra com PA em outra Moeda e Compensação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361432-MP-SIGACOM-Pedido-de-Compra-com-PA-em-outra-Moeda-e-Compensa%C3%A7%C3%A3o)

[MP - SIGACOM - Documento de Entrada atrelado a título do tipo PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567072-MP-SIGACOM-Documento-de-Entrada-atrelado-a-t%C3%ADtulo-do-tipo-PA-)

[15546571 DMANMAT02-40492 DT Valor Limite no relacionamento de adiantamentos](https://tdn.totvs.com/x/Y6IcKw)

[PCOM12059 - Parâmetro MV\_VLDADT Validar adiantamentos na inclusão do Documento de Entrada](https://tdn.totvs.com/pages/releaseview.action?pageId=621598855)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001545042)
