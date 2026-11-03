---
article_id: 360049739614
category: SIGAEST - INVENTÁRIO
content_hash: 41a3c43fda6135868292e6bbcb796b4ebfc79cb3e6508d5495e60285c65b5937
fetched_at: '2026-06-28T22:38:50.410693+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo
  padrão para  Inventariar produtos no Estoque
type: support-article
updated_at: '2025-12-11T20:23:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque
---

O processo de inventário no Protheus envolve emissão de etiquetas (MATR270), geração da lista de produtos (MATR280), digitação do inventário (MATA270), conferência de diferenças (MATR285) e acerto de inventário (MATA340).

O sistema permite bloqueio de produtos para inventário, controle de inventário rotativo e gera relatórios para acompanhamento. Ajustes são feitos automaticamente conforme as diferenças encontradas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20027896372375) Tempo aproximado para leitura: **00:15:00 min**  
  
**Dúvida**

Como efetuar o **processo de Inventário no Protheus** desde a Digitação do inventário até o Processamento do Inventário?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

***Sugestão:*** Para se aprofundar no conhecimento das rotinas envolvidas, assista abaixo os ***Webinares que foram apresentados pela equipe de suporte sobre o processo padrão de inventário*** no Protheus:

**- WEBINAR APRESENTADO EM NOVEMBRO 2025**

**- WEBINAR APRESENTADO EM NOVEMBRO 2023**

**- WEBINAR APRESENTADO EM NOVEMBRO 2022**

O Inventário é a forma adequada de corrigir diferenças nos saldos em estoque de uma empresa. O controle é realizado por meio de uma recontagem dos materiais fisicamente e confrontando os resultados com os saldos fornecidos pelo sistema.

O módulo de **Estoque e Custos** permite uma série de controles para os produtos resultantes de alguns procedimentos básicos para o processamento do inventário:

* Emissão das etiquetas com a definição da filial, armazéns, produtos, tipos, grupos e número **(rotina MATR270)**.
* Emissão do Relatório de Inventário que apresenta os itens registrados pelo sistema, além, de um espaço para informação manual das quantidades contadas **(rotina MATR280)**.
* Bloqueio do Inventário que permite impedir, em uma data calculada ou informada, as movimentações do estoque com produtos inventariados.  **(rotina MATA271)**.
* O usuário efetua o inventário e, em seguida, inicia a digitação das quantidades inventariadas **(rotina MATA270)**.
* Emissão do Relatório de Conferência do inventário com informações sobre todas as diferenças detectadas **(rotina MATR285)**.
* Acerto de inventário para situações que resultam de diferenças entre a informação registrada no sistema e o que foi inventariado, gerando automaticamente as requisições ou devoluções necessárias ao ajuste **(rotina MATA340)**.

**Passo a Passo do Processo de Inventário**

Ordenando a tarefa de inventário em passo a passo, ela ficaria da seguinte forma:

**1° Passo** - Emissão da Etiqueta de Inventário através da rotina MATR270 **(verificar a necessidade).**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18016512501271)

**2° Passo** - Geração da Lista de Produtos para contagem física através da rotina MATR280.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18016533959447)

**3° Passo** - Após a conclusão da contagem física, efetuar a Digitação do Inventário no Protheus através da rotina MATA270.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18016533962903)

**4° Passo** - Após digitar, acessar a rotina de Conferência de Inventário através da rotina MATR285 para checagem das diferenças entre o estoque físico e o estoque que apresenta no sistema.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18016533963799)

**5° Passo** - Caso houver diferenças, fazer o Acerto do Inventário através da rotina MATA340 para que o sistema atualize os saldos divergentes para os que foram digitados no Inventário.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18016512517399)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18016533969431)

Abaixo serão listados outros pontos importantes e possibilidades com maior detalhamento que o sistema permite ao usuário com relação ao Inventário:

**Inventário Rotativo**  
Para utilização do inventário rotativo é necessário informar o campo **Per. Inventário (Periodicidade do Inventário)** que define, em dias, a periodicidade em que se deve contar um determinado item do Estoque.  
**Exemplo:** o produto **A** deve ser inventariado de 120 em 120 dias. A partir deste instante, a data do inventário passa a ser de extrema importância, pois, o sistema assumirá como saldo a ser inventariado o saldo do final do dia do Inventário (B7\_DATA). Para corrigir o inventário, é necessário utilizar a rotina de **Acerto de Inventário**. Antes, porém, é preciso assegurar que toda a movimentação anterior ao inventário já esteja digitada. Os registros válidos para o inventário são os que estão digitados no arquivo de Inventário na data efetiva do processamento, ou seja, caso a quantidade inventariada de um produto seja nula, deve ser digitado **0**.

**Informações sobre a Digitação do Inventário (MATA270)**  
A digitação das quantidades inventariadas é informada por almoxarifado para posterior cálculo automático do ajuste a ser efetuado no estoque dos produtos. O inventário dos produtos em processo é tratado no **Armazém 99**.  
Quando o produto utilizar rastreabilidade, devem ser informados os números dos lotes para que o acerto das quantidades seja feito lote a lote. Quando o produto utiliza controle de endereçamento, deve ser informado o endereço e/ou número de série. A rotina de **Inventário** não atualiza os estoques, assim, é apenas um informativo das quantidades inventariadas. Para atualizar os dados, é necessário o processamento da rotina **Acerto de Inventário**.  
  
Para efetuar o lançamento de Inventário:

1. No menu principal, selecione as opções **Atualizações / Internas / Inventário**. O sistema apresenta a tela (*browser*) com o registro das quantidades já inventariadas.
2. Clique na opção **Incluir** e preencha os campos conforme descrição a seguir:

   * **Produto:** informe o código do produto inventariado. A tecla **[F3]** disponibiliza o cadastro de **Produtos** para consulta.
   * **Armazém:** este campo é reservado para informar o armazém respectivo do produto.
   * **Tip. Material:** é preenchido automaticamente pelo sistema e informa o tipo do material sendo inventariado. A tecla **[F3]** disponibiliza o cadastro de **Tipos de Materiais** para consulta.
   * **Documento:** informe o número do documento que registra o inventário do produto.
   * **Quantidade:** informe a quantidade inventariada. A tecla **[F3]** está disponível para ativar a opção **Calculadora** e realizar eventuais cálculos.
   * **Qtde. 2a UM:** informe a quantidade do produto inventariado na segunda unidade de medida, se houver. A tecla **[F3]** está disponível para ativar a opção **Calculadora** e realizar eventuais cálculos.
   * **Invent. Em:** informe a data do inventário do produto. A tecla **[F3]** está disponível para ativar a opção **Calendário**e realizar consultas de datas.
   * **Descrição:** apresenta automaticamente a descrição do produto resultante da digitação do código do produto.
   * **Lote:** se o produto possui rastreabilidade, informe o número do lote que está sendo inventariado.
   * **Sublote:** se o produto possui rastreabilidade tipo **Sim**, informe o número do sublote que está sendo inventariado.
   * **Data de Validade:** este campo informa a data de validade do lote do produto. É preenchido automaticamente quando o número do lote é digitado. A tecla **[F3]** está disponível para ativar a opção**Calendário**e realizar consultas de datas.
   * **Endereço:** informe o endereço d o produto que está sendo inventariado. A tecla **[F3]** disponibiliza o cadastro de **Endereço** para consulta.
   * **Num. de Série:** informe o número de série do produto que está sendo inventariado. Para facilitar a digitação, a tela de inclusão traz o produto na ordem em que foi cadastrado (sequencialmente), de acordo com as confirmações das inclusões.
3. Confira os dados e confirme a inclusão.

**Exclusão de Inventário**  
Para reverter a inclusão de uma digitação de inventário, basta excluí-lo. Visto que, a rotina não atualiza o estoque, o item inventariado pode ser excluído sem causar qualquer dano à posição do estoque. Para realizar este procedimento, é necessário apenas selecionar o item inventariado e clicar na opção Excluir.

**Consultas**  
Para verificar as transferências realizadas, acesse o arquivo **SB7 - Inventários** por meio das opções **Consultas / Cadastros / Genéricos**. Esta consulta pode ser impressa.

**Bloqueio do Inventário**  
Permite bloquear, em uma data calculada ou informada, as movimentações de estoque com produtos que serão inventariados. Para isso, existe o campo **Data Bloq. de Inventário (B2\_DTINV)**, no arquivo de **Saldos Físico e Financeiro (SB2)**, que será preenchido com a data do bloqueio. A função que verifica o bloqueio é **BLQINVENT (ExpC1, ExpC2, ExpD1)** e seu retorno será **.T.** ou **.F.**, dependendo do bloqueio do produto **(ExpC1)**, do local **(ExpC2)** e da data **(ExpD1)**, sendo que, **ExpD1** é a data opcional e, se omitida, será considerada a data base. Esta função pode ser utilizada em RdMakes, validações etc.  
  
Para efetuar o Bloqueio do Inventário:

1. No menu principal, selecione as opções **Atualizações / Processamento / Bloq. Inventário**. O sistema apresenta a tela com os parâmetros da rotina. Preencha-os considerando as seguintes informações:

   * **Quanto ao produto?:** selecione se o processamento a ser realizado terá a função de **Bloqueia** ou **Desbloqueia**os produtos.
   * **Do Armazém? / Até Armazém?:** informe um intervalo de armazéns cadastrados para selecionar os produtos que serão bloqueados ou desbloqueados.
   * **Do Produto? / Até o Produto?:**informe um intervalo de códigos de produtos que serão bloqueados ou desbloqueados.
   * **Do Tipo? / Até o Tipo?:** informe um intervalo de tipos de produtos que serão bloqueados ou desbloqueados.
   * **Do Grupo? / Até o Grupo?:** informe um intervalo de grupos de produtos que serão bloqueados ou desbloqueados.
   * **Máscara:** informe uma máscara para seleção dos códigos dos produtos que serão bloqueados ou desbloqueados. O uso da máscara agiliza o trabalho de seleção, pois, substitui caracteres variáveis com o sinal de asterisco (\*). *Exemplo:*para selecionar códigos de produtos que comecem com **PR** e que variem nos caracteres seguintes, defina a máscara **PR\*\*\*\*\*\*\*\*\*\*\*\*\***.
   * **Da Data? / Até a Data?:** informe um intervalo de datas do último inventário dos produtos que serão selecionados.
   * **Data do Inventário?:** selecione a **Data Informada** para especificar uma data para o bloqueio dos produtos ou **Data Calculada** se desejar que o sistema determine automaticamente a data para bloqueio dos produtos, considerando a data do último inventário mais a periodicidade do Inventário gravada no cadastro de **Produtos**.
   * **Data Informada:** se esta opção for selecionada no parâmetro anterior, é necessário especificar a data em que deve ocorrer o bloqueio dos produtos.
2. Depois de preencher os parâmetros, devem ser selecionados os produtos inventariados que serão bloqueados ou liberados.

Veja também os artigos sobre Bloqueio de Inventário dos links abaixo:

[Bloqueio de produtos para inventário por data calculada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021321072-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-calculada?source=search)

[Bloqueio de produtos para inventário por data informada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021554891-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-informada?source=search)

**Relatórios**  
Para verificar os cadastros de estruturas, estão disponíveis os seguintes relatórios:

* **Relatórios / Inventário / Lista de Produtos (MATR280)**
* **Relatórios / Inventário / Conferência do Inventário**. **(MATR285)**

**Acerto do Inventário**  
O acerto de inventário compara a quantidade em estoque e a quantidade inventariada, resultando em um ajuste, caso não sejam iguais. O sistema gera uma requisição ou devolução automática do produto, dependendo da diferença encontrada.  
Este movimento tem o mesmo tratamento que as requisições/devoluções para consumo, recomendam-se diferenciá-los pelo centro de custo, informando no parâmetro o código do centro responsável pela guarda dos materiais, normalmente o próprio almoxarifado. O saldo considerado no estoque é o saldo na data informada nesta rotina, antes da virada de saldos, quando todos os movimentos do período estiverem conferidos e o saldo final já calculado.  
  
Para efetuar o Acerto de Inventário:

1. No menu principal, selecione as opções **Miscelâneas / Processamentos / Inventário**.
2. Clique na opção **Parâmetros** e preencha-os considerando as seguintes informações:
   * **Data de Seleção?:** informe a data selecionada para efetivar o acerto do inventário. Serão considerados somente os itens digitados com esta data que constam na rotinas MATA270 ao digitar o inventário.
   * **Centro de Custo?:**informe o centro de custo a que se refere o acerto de inventário.
   * **Mostra Lanç. Contab.?:** informe se os lançamentos contábeis devem ser visualizados durante o processo de acerto do inventário. Apresenta as opções **S (Sim)** ou **N (Não)**.
   * **Aglut. Lançamentos?:** informe se os lançamentos contábeis gerados serão aglutinados. Apresenta as opções **S (Sim)** ou **N (Não)**.
   * **Do Produto? / Até o Produto?:** informe o intervalo de códigos de produto considerado para o acerto do inventário.
   * **De Armazém? / Até Armazém?:**informe o intervalo de códigos de localidade considerado para o acerto do inventário.
   * **Do Grupo? / Até o Grupo?:** informe um intervalo de grupos de produtos considerado para o acerto do inventário.
   * **Do Documento? / Até Documento?:** informe um intervalo de número de documento considerado para o acerto do inventário.
3. Confira os dados e confirme.

**Consultas**  
Para verificar as transferências realizadas, acesse o arquivo **SB7 - Inventários** por meio das opções **Consultas / Cadastros / Genéricos**. Esta consulta pode ser impressa.

**Situações em que o sistema não processa o Acerto de Inventário**

**OBS:** Nos casos detalhados abaixo é exibido um **"Relatório de itens não inventariados"**, porém caso não exiba o relatório, revisar se as Stored Procedures estão instaladas.

➢ Saldo em Poder de Terceiro não é possível ser inventariado. Sendo um saldo a parte do saldo físico, as movimentações do saldo de terceiros, somente podem ser ajustadas através de notas fiscais;

➢Produtos que controlam Endereço (B1\_LOCALIZ = S) quando reservados (B2\_RESERVA). O sistema permite o acerto de Inventário para saldos reservados, **desde que**, a quantidade inventariada seja **MAIOR OU IGUAL** à quantidade reservada;

➢Se o saldo no arquivo SB2 estiver negativo (**MV\_ESTNEG = N**), compromete o saldo atual do produto;

➢ B2\_DINVENT maior que a data de digitação do inventário;

➢ Itens com saldo negativo nos Saldos em estoque; **Observações:** É permitido efetuar o processo de inventário quando Saldo esta Negativo incrementando ou mesmo zerando o Saldo para produtos que **não tem** controle de Rastro e Endereço;

➢ Itens com saldo desbalanceado entre o SB2 e o SBF, verificar todos os processos pendentes para a tabela SBF, como por exemplo, endereçamentos pendentes e empenhos para produção com endereços pendentes, também confira se é o caso de saldo desbalanceado entre as tabelas SB2 x SB8 x SBF através do MATR282 ([Ver artigo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-MP-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF?source=search))

➢ Itens sem saldo para o lote / sub-lote verifique todos os processos pendentes para a tabela SB8, como por exemplo: lotes vencidos e/ou bloqueados.

➢ Itens com movimentações de C.Q. pendentes **(Aceita acerto apenas quando incrementar saldo no CQ)**.

➢ Verificar se o parâmetro MV\_CONTINV esta habilitado.

Exemplo de relatório de itens não inventariados ao processar o inventário.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076533933)

**Seleção automática**  
Por conceito, a rotina automática selecionará apenas as contagens em que não haja divergência entre si, desta forma, o sistema busca uma a ser selecionada e, quando houver contagens diferentes entre si, a seleção deverá ser procedida manualmente.  
É necessário existir mais de uma contagem e nenhuma selecionada para ser considerada múltipla contagem. Portanto, para haver seleção, todas as contagens deverão obrigatoriamente serem equivalentes entre si.

**Help BLQINVENT**

O help estava sendo apresentado, pois, o produto estava com o campo **Data Invent (BE\_DTINV)** preenchido. Após alteração, a movimentação foi efetuada com sucesso. Produtos bloqueados para inventário (**B2\_DTINV** e **B2\_DINVFIM** diferentes de branco)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar o estorno (exclusão) de movimento de Inventário?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402384407063)

[*SIGAEST - MILE importação de arquivo da tabela SB7 (Digitação do inventário)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10573324218007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SB7-Digita%C3%A7%C3%A3o-do-invent%C3%A1rio-)

[*MP - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data calculada*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021321072-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-calculada?source=search)

[*MP - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data informada*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021554891-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-informada?source=search)

[*MP - SIGAEST - MATA340 - Inventário rotativo ou cíclico no Protheus*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058014194)

[*Clique aqui e veja mais artigos sobre Inventário no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)
