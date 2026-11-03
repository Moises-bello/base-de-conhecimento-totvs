---
article_id: 360021352991
category: Financeiro - Contas a Pagar
content_hash: a9c7d67334bc7b623406e070a26d574974cb2b9fa715542372dde05aad292767
fetched_at: '2026-06-28T22:38:09.657401+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - HELP: NOTITSEL'
type: support-article
updated_at: '2026-03-24T16:36:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021352991-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-HELP-NOTITSEL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39262137052695)**Tempo aproximado para leitura: **00:05:00 min**  
  
  
**Dúvida**  
Ao realizar a compensação na rotina FINA340, apresenta o mensagem de HELP: **NOTITSEL**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001879441)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Temos alguns processos que ao serem executados na rotina de **Compensação** o sistema retornará o **help NOTITSEL.**

Neste artigo, mencionaremos alguns cenários, para que sejam validados buscando agilizar a solução ao tema.

**1º Cenário :**

Para compensação entre adiantamentos e títulos de diferentes filiais, deve ser utilizado o botão **Filiais** para definir quais filiais serão consideradas para a seleção dos títulos a compensar.  
Caso não seja utilizado o botão **Filiais**, apenas títulos da filial corrente serão considerados para a compensação.

![image2021-5-7_9-9-26.png](https://tdn.totvs.com/download/attachments/504794483/image2021-5-7_9-9-26.png?version=1&modificationDate=1620389366557&api=v2)

**Observação:**

Caso as tabelas do módulo financeiro sejam **totalmente compartilhadas** e não for utilizado o botão **Filiais**, serão considerados para o processo os registros de todas as filiais. Se for utilizado o botão **Filiais**, os registros serão filtrados por **filial de****origem (E2\_FILORIG)**.

Caso as tabelas do módulo financeiro sejam **compartilhadas a nível de filial**, e não for utilizado o botão **Filiais**, serão considerados para o processo os registros cuja **filial de origem (E2\_FILORIG)**seja a filial corrente. Se for utilizado o botão **Filiais**, os registros serão filtrados por **filial de origem (E2\_FILORIG)**.

**Filial do processo de compensação:**

Quando o processo de compensação for feito com títulos de filiais diferentes, a rotina irá considerar a filial do título de origem (de partida) da compensação para gravar as movimentações (tabela SE5) e contabilização (tabela CT2).

*Obs: Comportamento vigente na rotina FINA340 com data igual ou superior a 27/06/2022 , para deixar a rotina com o mesmo comportamento da rotina FINA330 (Compensação a Receber). Até então a rotina FINA340 exibia uma tela para a selecionar a filial do processo após clicar no botão "Compensar".*

**2º Cenário :**

No processo de compensação da NDF/NF, deve-se gerar na movimentação tipos de títulos PA, DIC, PA e NF. Nesse cenário foi apresentado novamente o tipo DIC.

**Solução**

Alguns ambientes migrados da versão 11, possuem a tabela SES com registros que não devem ser utilizados, por tratar-se de um fluxo desenvolvimento somente para o ambiente do Mercado Internacional.

Acessar rotina Tipos de Títulos (FINA015), avaliar a existência de registro na tabela SES para o PA, NDF (NCC ou RA em caso do erro acontecer no FINA330 compensação contas a receber), caso possua, excluí-lo.

**Saiba Mais:** [Utilização da rotina Tipos de títulos](https://tdn.totvs.com/display/public/PROT/FIN0004_Utilizacao_rotina_tipos_de_titulos_FINA015)

**3º Cenário :**

O sistema não localiza NDF para realizar Compensação, apresentando o HELP NOTITSEL na tentativa de compensar com o tipo NDF ou PA.

**Análise**

Caso no ambiente esteja configurado o parâmetro com o conteúdo MV\_CTLIPAG=.T. verificar se os títulos a serem compensados foram liberados.

**Solução:** Acessar a rotina "FINA580 - Liberação de títulos" e efetuar as liberações dos títulos a serem compensados exemplo: NF, PA, NDF, verificar após a liberação, se os campos foram atualizados para status Liberado. Segue exemplo modelo abaixo E2\_STATLIB=03, (status que o título está liberado) E2\_USUALIB=Administrador (usuário que liberou) E2\_DATALIB=20210125 (data da liberação)

**Saiba mais:** [Como utilizar a rotina liberação para baixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016596851-MP-SIGAFIN-FINA580-Como-utilizar-a-rotina-libera%C3%A7%C3%A3o-para-baixa-)

**4º Cenário :**  
Para correção do **HELP**, é necessário realizar o ajuste na **parametrização** para o seu correto funcionamento, porém, é importante avaliar, antes de tudo, o conteúdo do parâmetro **MV\_BX10925,** pois, para a configuração = 1 (Baixa), seguir a opção A e para o configuração = 2 (Emissão), seguir a opção B. Abaixo, segue as duas opções:

**OPÇÃO A.**  
O parâmetro **MV\_PABRUTO** caso esteja com o valor **2** (**Líquido**), ao gerar títulos do tipo **PA**é mantida a geração com o valor líquido, em que são descontados os valores de impostos que podem ser retidos na inclusão.  
Ao realizar a compensação de um título, por exemplo, do tipo **NF** com uma **PA**, sendo que ambas retêm impostos na baixa, é aconselhável os parâmetros abaixo sejam configurados da seguinte maneira, para que haja coerência de valores:  
**MV\_COMPCP** = **.T.** - Indica se na compensação de uma **NF** com um **PA** os impostos serão proporcionalizados.  
**MV\_BP10925** = **2** - Considera valor Líquido na baixa Parcial descontados os impostos.  
**MV\_PAPRIME** = **1** - Considera provisionamento de impostos para **PA** Líquido.

**OPÇÃO B.**  
O parâmetro **MV\_PABRUTO** estiver igual a **1** (**Bruto**) ao gerar títulos do tipo **PA**(Pagamentos Antecipados), é gerado com o valor **bruto**, não descontando os valores de impostos que podem ser retidos na inclusão. Então a compensação de uma **NF** com uma **PA**, deveria ser pelo valor bruto configurando os parâmetros conforme abaixo:  
**MV\_PABRUTO** = **1** - **Bruto** e **MV\_BX10925** = **1** Imposto na baixa ou **MV\_BX10925**=**2**Imposto na emissão  
**MV\_BP10925** = **1** - Considera valor Bruto na baixa Parcial sem descontar os impostos.  
**MV\_PAPRIME** = **2** - Não considera provisionamento de impostos para PA Líquido.  
Observação:  
O parâmetro **MV\_COMPCP** não influencia caso o parâmetro **MV\_PABRUTO** esteja com o valor em **1**. Independente dos títulos terem impostos, ou não, é necessário a parametrização.  
A compensação entre **NF** x **PA**, partindo tanto da **NF** como do **PA**, não é permitida caso o parâmetro **MV\_PABRUTO** esteja com o valor **2** (**Líquido**) e as naturezas estiverem diferentes.

**Importante**  
O parâmetro **MV\_BX10925**não pode ser alterado, pois no momento da implantação do ***Protheus***, é definido como a empresa irá tratar o imposto.

**5º Cenário :**  
Observar o campo **Contabilização** na tela de consulta de títulos pelo seguinte caminho:  
**Financeiro** > **Atualizações** > **Contas a Pagar** > **Contas a Pagar** > **Visualizar** > **Outras Ações** > **Posição**.  
Se o registro contido no campo **Contabilização** (data que o usuário estava logado momento da inserção do título), for maior que a data base no momento da compensação, o sistema apresentará o Help pois validará a data que o título foi inserido no sistema e consequentemente não localizará o título para a compensação.

![contabiliza__o.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360017923091)

**6º Cenário :**  
  
**Ocorrência:** Cliente lança uma NF e uma PA, na hora de compensar, da erro NOTITSEL, com uma PA  
  
**Solução:**Verifique se o Grupo de perguntas no F12 da FINA050 não está ajustada para o PA não gerar movimentação bancária e gerar cheque para pagamento conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053219193)

Sendo assim para o NOTITSEL não ocorrer, basta configurar conforme abaixo:

\*Gera cheque para adiantamento = NÃO

\*Gera Movimentação sem cheque = SIM

**7º Cenário**

**Ocorrência**: Cliente lança uma NF e uma PA , na hora de compensar, da erro NOTITSEL, com uma PA.  
  
**Solução**: Verificar os campos “Parcela” das tabelas SE2 e SE5 se estão com o mesmo tamanho no dicionário e banco de dados. Assim como o conteúdo do parâmetro MV\_1DUP se está coerente ao tamanho destes campos.

1 - Valide se os campos abaixo possuem os mesmos tamanhos na SE2 e SE5, além disso valide a quantidade de "caracteres" que tem nos campos abaixo dos registro com problema. Por exemplo.  
Tamanho e conteúdos dos Campos:  
E2\_FILIAL = E5\_FILIAL  
E2\_PREFIXO = E5\_PREFIXO  
E2\_NUM = E5\_NUMERO  
E2\_PARCELA = E5\_PARCELA  
E2\_TIPO = E5\_TIPO                                                                                                                                                                                                            
  
**Exemplo**: Quantidade de "caracteres":  
Veja que o registro possui o campo E2\_NUM com '5555     ', ou seja nesse registro o campo E2\_NUM possui quantidade de "caracteres" 9 contando o 5555 e os espaços em branco.  
  
OBS: O campo E5\_DOCUMEN contém uma chave, onde a mesma deve respeitar os espaços dos campos.  
  
![](https://totvssuporte.zendesk.com/attachments/token/yj9dpBZmJrYAzM0eMfZmdB3kG/?name=inline-1638113119.png)​  
  
3 - Valide se o campo MV\_1DUP está de acordo com a documentação abaixo.  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021873891-MP-SIGAFIN-Desdobramento-acima-de-35-parcelas>

**8º Cenário**

**Ocorrência**: Cliente lança uma NF e uma PA , na hora de compensar, da erro NOTITSEL, com uma PA.  
  
**Solução**: Verificar se a ocorrência acontece para registros novos ou apenas antigos. Pois em algumas ocorrências identificamos a ausência do preenchimento do campo **E5\_FILORIG** para os registros de compensação. A consequência do não preenchimento deste campo, também resulta na no assistente **NOTITSEL**.  
  
Ao detectar um caso semelhante ao mencionado, uma verificação na base de dados quanto ao campo **E5\_FILORIG** será necessária.  
Para manutenção na base de dados, para esta ação sugerimos a alocação de um analista Totvs.  
  
**IMPORTANTE**: Ao apresentar o assistente NOTITSEL no **ESTORNO**de compensação, valide o campo **E5\_FILORIG** nos registros da compensação e também verifique os campos da chave **(Prefixo+número+parcela+tipo+fornecedor+loja)** das tabelas SE2 e SE5. Os campos devem possuir tamanhos correspondentes nas duas tabelas.

**9º Cenário**

**Ocorrência**  
No módulo **Financeiro**, ao tentar realizar **baixa ou compensação de um pagamento antecipado** é apresentada a mensagem **NOTITSEL - Não é possível realizar a baixa de pagamento antecipado sem movimentação bancária.**  
  
**Causa**  
Esse incidente ocorre, pois o pagamento antecipado foi gerado sem cheque ou movimentação bancária.  
  
**Solução**  
Para solucionar essa ocorrência, será necessário incluir um cheque e vinculá-lo ao pagamento antecipado ou então, excluí-lo e incluir novamente seguindo as regras de inclusão de pagamento antecipado.

**Para geração do cheque:**  
1. Acessar a rotina **Cheque sobre títulos (FINA390)**;  
2. Selecione a opção **Cheque sobre títulos**e preencha os parâmetros exibidos na tela;  
3. Clique em **OK**;  
4. Será exibida uma tela para seleção do título no qual quer vincular o cheque criado. **Selecione e confirme**.  
5. Após a confirmação, o cheque será criado e será possível realizar a baixa ou compensação do pagamento antecipado.

**10º Cenário**

**Ocorrencia**  
No módulo Financeiro, ao tentar realizar baixa ou compensação de um pagamento antecipado é apresentada a mensagem **NOTITSEL** - **Não são permitidas movimentações financeiras com data menores que a data limite de movimentações no Financeiro**  
  
**Causa**  
Esse incidente ocorre, pois a data de emissão **(E2\_EMISSAO)** é menor que a data do **E2\_EMIS1 ( Data Logado no sistema)**

**Solução**  
Para solucionar essa ocorrência, será necessário logar no sistema com a mesma data-base que foi inserido o título e não da emissão e realizar novamente a compensação.

**Saiba mais**  
Para maiores informações sobre os modos de inclusão de pagamento antecipado, consulte o documento: [Modos de inclusão de PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726827-MP-SIGAFIN-Quais-os-modos-de-inclus%C3%A3o-de-PA)
