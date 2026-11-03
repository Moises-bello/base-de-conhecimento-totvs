---
content_hash: 725dcb490b01625ec79f5098c96379532c19d5cb3b61aa92a2cefad7cd4accab
fetched_at: '2026-06-29T00:09:36.159640+00:00'
page_id: '425459475'
product: rm
source: tdn-rm
title: Valores de Integração Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459475
version: 29
---

---

*Valores de Integração* são campos especiais, criados para auxiliar uma ação ou determinado processo que envolve *valores* entre o sistema de origem e o sistema financeiro (TOTVS Gestão Financeira).  Estes campos são totalmente parametrizáveis pelo usuário que definirá o comportamento dos mesmos em relação ao lançamento financeiro. No momento da baixa dos lançamentos, estes campos serão interpretados pelo TOTVS Gestão Financeira conforme a ação indicada em seus cadastros, podendo acrescentar, descontar ou não afetar o valor líquido dos lançamentos.

O cadastro dos campos de Valores de Integração está disponível no TOTVS Educacional através do menu *Financeiro/Contábil | Geração | Financeiro | Valores de Integração Financeira*, mas atenção, é necessário que o usuário tenha permissão para manutenção neste cadastro. Confira, primeiramente, as permissões no perfil do usuário (*Perfil Educacional-tags: Financeiro/Contábil | Geração | Financeiro | Valores de Integração Financeira | Incluir|Excluir|Editar* devem estar habilitadas).

Para incluir os campos de 'Valores de Integração' acione o botão 'Novo': informe uma *'Descrição'* para o campo e defina a *'Ação'* que será interpretada no momento da *baixa* do lançamento financeiro podendo ser *Nada, Acrescenta* ou *Desconta*. Informe também a *'Ordem'* numérica em que valor atribuído ao campo deverá ser aplicado no momento da baixa do lançamento.  
   
**Exemplo:**

|  |  |  |
| --- | --- | --- |
| **Valores de Integração** | **Ação** | **Ordem** |
| Bolsa Especial | Descontar | 1 |
| Bolsa Familiar | Descontar | 2 |
| Pagamento a Maior | Acrescentar | 3 |
| Perda Desconto | Nada | 4 |

No momento da baixa dos lançamentos financeiros, o TOTVS Gestão Financeira irá efetuar o cálculo do valor líquido dos lançamentos provenientes do TOTVS Educacional na seguinte ordem:

Valor Líquido = Valor Original - Valores a descontar (Desconto, Imposto IRRF) - Valores de Integração Financeira (Bolsa Especial, Bolsa Familiar) + Valores a acrescentar (Multa, Juros) + Valores de Integração Financeira (Pagamento a Maior)

**Até o Vencimento** Essa opção estará disponível se a *'Ação'* do campo for 'Desconta'.  
Com essa opção marcada, o Valor de Integração somente será considerado até a data de vencimento. Quando a opção estiver desmarcada, o Valor de Integração sempre será considerado.

**Dias de Atraso** Esse campo ficará disponível se a *'Ação'* do valor de integração for 'Acrescenta'.  
Nesse campo pode-se informar o número mínimo de dias de atraso para que a ação seja executada.   
   
**Atenção:**  
1- Os Valores de Integração são utilizados pelo Educacional para registrar separadamente nos lançamentos financeiros os valores de Bolsa condicional, Bolsa incondicional, Pagamento a maior, Pagamento a menor, Valor de acréscimo de cobrança retroativa para débito (conta corrente), Valor de desconto de cobrança retroativa para crédito (conta corrente) e Repasse de bolsa a menor.   
 Para isto, após cadastrar os campos de Valores de Integração, associe-os um a um, nos parâmetros do sistema, aos respectivos campos (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Vlrs. Opcionais/Integração 1 a 3*). Assim, os lançamentos financeiros gerados terão cada um destes valores lançados e controlados separadamente nos respectivos campos de Valores de Integração, sendo interpretados, conforme a *'Ação'* de cada campo, na composição dos valores e baixas dos lançamentos.

 2- Para auxiliar exclusivamente no cálculo dos valores de *Bolsa condicional*, é possível utilizar uma ***fórmula***. Para isto, tanto o campo de Valores de Integração que será associado nos parâmetros do sistema para registrar estes valores de *Bolsa condicional* assim como a respectiva *fórmula* deverão ser criados diretamente no TOTVS Gestão Financeira pelo menu *Cadastros | Específicos | Valores de Integração*, pois somente *fórmulas* do sistema financeiro são aceitas para estes cálculos. Após o cadastro do campo com a indicação da *fórmula* desejada no sistema Financeiro, volte ao TOTVS Educacional e associe este campo, conforme necessitar, nas configurações para Bolsa condicional nos parâmetros do sistema Educacional.

O processo *'Cópia de Valores de Integração entre Coligada'* permite realizar a cópia de campos específicos de valor de integração financeira para outra coligada. Caso o valor de integração financeira a ser copiado contenha uma fórmula cadastrada, a fórmula não será copiada para a coligada de destino. Isso porque a fórmula é vinculada à coligada que pertence o valor de integração financeira.

O processo *'Ordenar Valores de Integrações'* permite redefinir, de maneira otimizada, a ordem, indicada em cada campo de valor de integração financeira, em que os valores de integração deverão ser aplicados no momento da baixa dos lançamentos financeiros.  
   
**Importante:**  
Os valores de Bolsa Condicional, Bolsa Incondicional, Pagamento a Maior, Pagamento a Menor e os valores aproveitados da Conta Corrente dos alunos inicialmente eram registrados nos lançamentos financeiros em campos de *Valores Opcionais* disponibilizados e controlados exclusivamente pelo sistema *TOTVS Gestão Financeira*, ficando com isto muito limitada a sua utilização.

Hoje é possível controlar estes mesmos valores através de campos de ***Valores de Integração***. Estes campos, depois de criados, devem ser corretamente associados na parametrização do TOTVS Educacional nas suas devidas funcionalidades (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Vlrs. Opcionais/Integração 1 a 3*).

Eventualmente, nos parâmetros do sistema, estes valores podem possuir então tanto uma parametrização de Valor Opcional quanto de Valor de Integração, uma vez que inicialmente só era possível utilizar Valores Opcionais sendo liberada a utilização dos Valores de Integração posteriormente. Ao parametrizar um campo de Valor de Integração para assumir o controle dos valores acima, o sistema contudo, grava a data em que cada Valor de Integração foi parametrizado na base, e assim:

- Na **Regeração** de um lançamento que originalmente utilizou os campos de *Valores Opcionais* para registrar tais valores, os mesmos campos de *Valores Opcionais* continuarão sendo utilizados no lançamento regerado, mantendo as informações legadas.

- Na **Geração** (*inclusão de novos lançamentos*), sempre serão utilizados os campos de *Valores de Integração* que estiverem parametrizados na base, levando sempre em consideração a data em que foram parametrizados, então, se a data de inclusão dos lançamentos for superior à data de parametrização dos campos de *Valores de Integração*, estes serão sempre utilizados, tanto na *geração* como na *regeração.*

**- Clientes que já utilizavam campos de *Valores Opcionais*:\***  
   Para estes clientes será possível parametrizar qualquer um dos valores acima para passar a utilizar um campo de *Valor de Integração*, seguindo a seguinte regra:  
         - Depois de associado nos parâmetros do sistema Educacional um campo de *Valor de Integração*, todo o lançamento incluído pelo Educacional a partir da data da sua parametrização, passa a controlar este valor no                             respectivo campo de *Valor de Integração* parametrizado.   
         - Para lançamentos que já foram gerados e necessitam ser regerados o sistema vai considerar a data em que o campo de *Valor de Integração* foi parametrização para saber ser utilizará o campo de *Valor Opcional* ou de *Valor                   de Integração*, por exemplo:  
               • Lançamento 1 gerado com data de criação no dia **10/11/2017** utilizando *Valor Opcional*.  
               • Dia **01/12/2017** o sistema foi parametrizado para passar a utilizar no campo "Bolsa incondicional" o campo de *Valor de Integração* denominado 'Bolsa'.  
               • Se for preciso regerar o lançamento 1 o sistema vai continuar utilizando o campo de *Valor Opcional* utilizado inicialmente antes da mudança da parametrização.  
         - Não é obrigatório que todos os valores acima passem a utilizar campos de *Valores de Integração*, contudo a sua utilização é indicada, pois possibilita uma maior flexibilidade nas escolhas, porém, uma vez que tenha sido                   utilizada em algum lançamento alguma parametrização de *Valor de Integração*, esta ficará desabilitada, não sendo mais possível modificar a parametrização.

**- Clientes que irão implantar o sistema:\***  
Para estes clientes, o controle dos valores acima somente será possível através da utilização de campos de *Valores de Integração* criados e parametrizados no Educacional. Lembrando que após a geração de lançamentos utilizando os *Valores de Integração* não será mais possível modificar a parametrização.  
  
**Atenção**:  
Clientes que já utilizavam campos de *Valores Opcionais* é importante que após a parametrização para utilização de *Valores de Integração*, altere os relatórios, consultas e etc. para considerar a nova parametrização conforme as regras descritas.

Valores de Integração do TOTVS Financeira

O TOTVS Financeira possibilita a inclusão de valores de integração default para lançamentos gerados a partir de outros módulos, ou seja todo lançamento gerado para Educacional poderá ser criado possuindo um valor de integração  
com regra especifica determinada pelo cliente, que pode ser definidas manualmente ou por fórmula.

Observação:  
Este recurso foi disponibilizado para as versões 12.1.25 e superiores ou igual a 12.1.28, para habilitar a opção entre em contato com o Suporte.  
Para saber mais detalhes consulte [FIN - Valores de Integração Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=532041706).

**Importante destacar as observações abaixo para os valores de integração default do TOTVS Financeiro:**

* Para parcelas que já existe lançamento gerado se incluímos no TOTVS Financeiro um novo valor de integração nas parametrizações, mesmo que o lançamento seja regerado o valor de integração não será considerado.  
  Para isso será necessário que o lançamento seja excluído e um nova geração seja executada para parcela.
* Se o TOTVS Financeiro utilizar o mesmo valor de integração parametrizado no TOTVS Educacional, (ex: Bolsa Condicional) se o lançamento não tiver bolsa condicional o valor de integração não fará parte do lançamento.
* Em lançamentos de Bolsa de Crédito não deve processar o valor de integração default parametrizados no TOTVS Financeiro.

Vr.Integração-TOTVSFinanceiroVr.Integração-TOTVSFinanceiroAcordoAcordoAcordo

**Lançamentos de Acordo:**

* Na geração de acordo financeiro os valores de integração afetam o valor do acordo financeiro, porém esses valores de integração não são replicados para os lançamentos gerado pelo acordo.  
  Os valores de integração já foram utilizados para agregarem o valor do acordo e se fossem replicados para os lançamentos gerados pelo acordo fariam uma nova alteração nos valores que já haviam sido fechados pelo acordo financeiro.
Conta CorrenteConta CorrenteConta Corrente

**Lançamentos com aproveitamento de conta corrente:**

* Aproveitamento manual da conta corrente os valores de integração cadastrados no TOTVS Financeira não serão disponibilizados, no lançamento a receber (conta corrente a menor) e no lançamento a pagar (conta corrente a maior)
* Quando o aproveitamento da conta corrente é pela geração de lançamentos serão considerados os valores de integração já cadastrados no TOTVS Financeira, o valor aproveitando pela conta corrente deve sempre aproveitar o valor liquido já descontando os descontos e acrescimentos do lançamento.
Bolsa RetroativaBolsa RetroativaBolsa Retroativa

**Lançamentos gerados de bolsa retroativa:**

* Lançamentos gerados através do processamento de inclusão/exclusão de bolsa retroativa não serão apresentando os valores de integração default parametrizados no no TOTVS Financeira.
FaturaFaturaFatura

**Lançamento gerado pela fatura**

Quando um lançamento do Educacional é submetido ao procedimento de fatura, o lançamento gerado é sempre um lançamento Financeiro, não estando assim submetido a regra de negócio do Educacional.

Neste sentido, os valores de integração compõem o lançamento apenas para a composição do valor líquido. Tratamentos como pagamento a maior, ou a menor, com reflexo ao conta corrente do aluno não serão executados.

A forma mais adequada para agrupar, desdobrar, ajustar valores e prazos é o processo de acordo.

Veja Também

---

[Cadastro de Valores de Integração Financeira](http://tdn.totvs.com/pages/viewpage.action?pageId=320376755)  
[Parametrização de Valores de Integração](http://tdn.totvs.com/pages/viewpage.action?pageId=320375713)  
[Inclusão de Faturas](http://tdn.totvs.com/pages/viewpage.action?pageId=334335462)
