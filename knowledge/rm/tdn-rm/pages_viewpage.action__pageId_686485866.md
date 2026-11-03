---
content_hash: 1bf59e93e5a47ff1cc4b9f9180e15afc53bb1c32e6ea909d102adaaf9af38ba5
fetched_at: '2026-06-29T00:11:20.540263+00:00'
page_id: '686485866'
product: rm
source: tdn-rm
title: Conciliação Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=686485866
version: 92
---

**Conteúdo**

truesquare

## **01. Sobre**

A conciliação contábil é um processo, imprescindível para a **boa gestão empresarial**, que verifica e ajusta possíveis diferenças entre as informações registradas na contabilidade e aquelas apresentadas por outras fontes, como extratos bancários, faturas de fornecedores e clientes, folhas de pagamento, entre outros.

Esse processo é essencial para as empresas porque garante a **precisão** e a **confiabilidade** das informações contábeis, uma vez que permite identificar e corrigir eventuais erros ou omissões que possam afetar a precisão dos registros contábeis, fornecendo **informações de qualidade** que auxiliam a **tomada de decisão** por parte dos gestores.

A **Conciliação Contábil** que o módulo de Gestão Contábil oferece vem trazer automatismo ao processo, facilitando a atividade do setor contábil.

Todas as funcionalidades para as Contas Sintéticas, estão disponíveis a partir da versão **12.1.2302**

## **02. Configuração**

Deve ser observado a configuração abaixo para a utilização do recurso.

1. Habilitação do menu aos usuários responsáveis pelo processo através da configuração do Perfil.

## **03. Filtros para acessar a Visão**

Os Lançamentos Contábeis são carregados após o preenchimento dos filtros a seguir:

60%VídeosleftfadeConta ContábilConta Contábil \*Conta Contábil

**(FILTRO OBRIGATÓRIO)**

Conta Contábil que será feita a conciliação dos lançamentos.

Data InicialData InicialData Inicial

Data de Início em que devem ser buscados os lançamentos.

Caso não seja preenchida, será utilizada a Data do Início do período contábil informada nos parâmetros.

Importante!

*Para que a pesquisa de lançamentos/partidas considere também aqueles de exercícios anteriores ao atual (dados da tabela de histórico) basta informar como data inicial uma data menor que a data de inicio do período contábil.*

Data FinalData Final \*Data Final

**(FILTRO OBRIGATÓRIO)**

Data Final em que devem ser buscados os lançamentos

Seleção de ColigadaSeleção de ColigadaSeleção de Coligada

Será possível selecionar outras Coligadas para Conciliação desde que a conta selecionada para conciliação exista.

Serão apresentadas apenas as Coligadas nas quais o usuário possui permissão de acesso!

Lançamentos em LotesLançamentos em LotesLançamentos em Lotes

Quando marcado, filtra também os lançamentos de Lotes não integrados

Lançamentos conciliadosLançamentos conciliadosLançamentos conciliados

Quando marcado, filtra também os lançamentos já conciliados.

40%

## **04. Visão da Conciliação**

Nessa visão são exibidas as partidas a Crédito e a Débito por lançamento para a conta utilizada no filtro. Caso seja selecionada uma conta contábil sintética, serão exibidas todas as contas analíticas filhas.

Informações Importantes

* Lançamentos estornados ou de estorno não serão exibidas na visão;
* Lançamentos agrupados:  
         -Serão exibidos os valores das partidas que **foram agrupadas** de forma separada sem totalizar o crédito e débito, as outras partidas não agrupadas, irão ser exibidos os totais normalmente.  
         -Não serão contemplados no processo de Pré Conciliação, por tanto, a conciliação para estes casos deverá ser feita de forma manual.  
         -Lançamentos que tiveram apenas suas **partidas agrupadas** não se aplicam as regras citadas acima.
* Nessa visão é possível visualizar o lançamento e suas partidas, porém, não é possível editá-lo. Para isso, acesse o menu de Lançamentos;
* As visões do TOTVS RM, como esta apresentada na conciliação, por padrão tem um limite de 500 registros. Caso seja necessário apresentar mais registros será necessário aumentar tal limite seguindo os passos descritos na documentação de [Criação de servidores de aplicação](https://tdn.totvs.com/pages/viewpage.action?pageId=244417247) ou [Servidores de aplicação](https://tdn.totvs.com/pages/viewpage.action?pageId=102924324) (utilize "CtbConciliacaoLancamentosData" como **ID do Server**);
* O campo **Documento**também é utilizado como agrupador na tela, portanto partidas com o mesmo documento e a mesma conta terão seus valores agrupados. Assim como os campos Filial e Complemento;
* **Não** serão carregados na tela de Conciliação, lançamentos de **Reajuste de Multimoedas**, ou seja, com valor **igual a zero;**
* A tela de Seleção para Conciliação Contábil, possui salvamento de preferências automático, sempre a última execução será salva, a fim de facilitar as próximas;
* Lançamentos financeiros decorrentes de acordo, assim como suas respectivas baixas, não conterão preenchido o campo/coluna **Id. Movimento** com seu movimento originário para que a pré-conciliação, caso ocorra, seja realizada pelo **Id. Financeiro**.
* Complemento do Histórico - Se o Complemento estiver preenchido na Partida, consideramos este campo. Caso contrário consideramos a Descrição do Histórico associado à Partida.
40%

**Complementos da visão:**

1. No topo é exibido a informação de qual a conta e data final selecionados no filtro da visão.
2. No rodapé são exibidos os valores **Total de Débito** / **Total de Crédito** / Diferença entre **Débito X Crédito.**
3. E no canto inferior direito, os processos **Conciliar** e**Desconciliar (**dependendo do status dos lançamentos**), Conciliar com a Origem** e **Concluir Conciliação.**

50%

## **05. Processos**

Além dos processos conciliar/desconciliar, contamos ainda com outras funcionalidades que estão disponíveis no rodapé da tela, canto direito. Basta acessar o ícone "Mais" e um sub-menu será exibido.

Acesse as documentações abaixo para mais informações:

## **06. Materiais de Apoio**

VídeosleftfadeWebinarWebinarWebinarnoneVideo Webinar

648432

648432

How ToHow ToHow TononeVideo How To

648432
