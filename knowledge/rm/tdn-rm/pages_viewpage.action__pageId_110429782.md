---
content_hash: 263e4717e9a427a65f541921bfb6110bd06abe768a4a1d5bc53b6785759a993d
fetched_at: '2026-06-29T00:05:54.860657+00:00'
page_id: '110429782'
product: rm
source: tdn-rm
title: RMPAT00006_Evento Contábil Transferência de Controle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=110429782
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | RM Gestão Patrimonial 11.50 |
| **Processo** | : | Evento Contábil de Transferência de Controle |
| **Subprocesso** |  | Gestão Patrimonial |
| **Data da publicação** | : | 03/08/2012 |

**Introdução**

No Bonum.NET todas as contabilizações são feitas utilizando eventos contábeis. O recurso de eventos contábeis permite maior flexibilidade na definição das contabilizações existentes no sistema. Para cada processo será necessário criar um tipo de evento.   
 Exemplo: Precisaremos criar um evento de aquisição, um evento para baixas, acréscimos, depreciações etc.  
 Cada empresa pode parametrizar os seus eventos para contabilizar as operações de acordo com as contas desejadas, portanto a contabilização ficará bem flexível e permitirá que cada empresa monte seus eventos de acordo com seus processos internos de contabilização.  
 Este documento tem o objetivo de explicar o funcionamento do evento contábil de Transferência Monetária padrão que é disponibilizado a partir da versão 11.50 ou superiores.  
 Antes de citarmos os campos e itens do evento contábil de Transferência de Controle, vamos apresentar o conceito sobre o **processo de Transferência de Controle** dentro do sistema.   
 O processo de Transferência de Controle ocorre quando a empresa necessita transferir um patrimônio entre filiais, centros de custos, Departamentos, Localizações ou Responsáveis.   
 Ex: Em 01/01/2008 a empresa adquiriu uma Máquina e registrou a mesma no centro de custo "Administrativo". Em 01/01/2009 esta máquina foi transferida para o centro de custo "Financeiro". Então a empresa realizará uma transferência de controle em 01/01/2009 e irá contabilizar a mesma.   
 A máquina que será transferida sofre depreciação, então a contabilização da transferência de controle deverá também transferir o valor da depreciação acumulada da máquina.

**Desenvolvimento/Procedimento**

**Explicação sobre a o conceito de depreciação:**   
 Ex: Após adquirir um patrimônio, o mesmo sofre depreciação mensal pelo uso, desgaste, obsolescência, etc.Então, contabilmente o registro desta depreciação é feito em uma conta de resultado chamada **"Despesas com Depreciação**" e sua contrapartida é uma conta redutora do ativo imobilizado chamada **"Depreciação Acumulada**". A **Depreciação Acumulada** vai acumulando os valores de **depreciação mensais** até que o seu saldo chegue ao valor do patrimônio. Quando isto ocorrer o patrimônio estará **totalmente depreciado.**   
   
   
   
   
 Na conversão das tabelas do TOTVS Gestão Patrimonial para a versão 11.50 ou superiores, o sistema já cria o evento contábil de Transferência Monetária e vincula o mesmo aos grupos de Patrimônios existentes na coligada. Com isto, o trabalho do responsável pelo sistema será de revisar os eventos que foram convertidos. Se desejado poderá alterar o evento para contabilizar de acordo com a necessidade da empresa.

 **Desenvolvimento/Procedimento**   
 A seguir vamos apresentar as **pastas/campos** existentes em um evento e a **configuração do evento de Transferência de Controle:**

1. **Pasta - Identificação**:

Na pasta de Identificação de um evento são apresentados os seguintes campos:   
 **Processo:** Neste campo é informado o processo que corresponde o evento, em nosso exemplo o processo é **"Transferência de Controle".**   
 **Inativo** – Quando esta opção estiver marcada o evento contábil estará inativo e não poderá ser utilizado nas contabilizações.   
 **Número:** Corresponde ao número do evento.   
 **Nome:** Corresponde ao nome do evento.   
 **Calcular valor a partir de:**   
 Define como o valor dos itens contábeis será calculado, podendo ser através de fórmula ou percentual. Estes dois itens serão informados posteriormente nos itens do Evento Contábil   
 **Fórmula:** O evento pode possuir uma fórmula para cálculo dos valores**.**   
 **OBS: Na versão 11.50 os eventos não são calculados por fórmula**.   
   
 **Percentual:** O evento pode ser calculado por percentual. Ex: No evento de Baixa, ao incluir um item do evento deve ser definido o valor da Baixa, deste valor o usuário informa qual percentual irá contabilizar. Lembrando que os itens à débito e à crédito devem sempre fechar.   
 **Buscar Filial/Depto em:** Neste campo deve ser informado de onde se deseja buscar os dados de filial e departamento.   
 Se fôr informado a opção **"Evento Contábil"**, ao contabilizar o processo, o sistema irá verificar em cada item do evento dentro da pasta **"Dados Complementares",** a filial e Depto informados.  
 Se fôr informada a opção **"Default Contábil",** na contabilização do processo, o sistema irá verificar a filial e departamento que estão informadas nos default's das tabelas que estão sendo utilizadas nos itens do evento contábil.   
 **Buscar Centro de Custo em:** Da mesma maneira que os dados de filial e departamento, deve ser informado onde os dados de centro de custo serão buscados para que sejam informados na contabilização.   
 **Importante:** O Evento Contábil tentar buscar **Filial/Departamento ou Centro de Custo** conforme a ordem definida (para mudar ordem utilize as setas).   
 Exemplo C. Custo:

* Ordem parametrizada  
   1º Patrimônio - Se não achar no Patrimônio tenta achar no Evento Contábil  
   2º Evento Contábil - Se não achar no Evento Contábil tenta achar no Default Contábil  
   3º Default Contábil - Se não achar no Default fica sem centro de custo   
    
  **Aplicar Centro de Custo em:** Define em qual dos itens (Débito ou Crédito) o centro de custo será preenchido.  
   Algumas empresas não informam centros de custos em determinadas contas, então deve-se informar neste campo em quais contas a informação será gerada.  
  **Agrupa Partida Contábil:** Marcando esta opção, se os itens do evento (contas contábeis) possuírem mesma conta, centro de custo, filial, departamento e histórico padrão, os itens são agrupados gerando somente uma partida contábil.

  |  |
  | --- |
  | O evento contábil sempre irá gerar partidas à débito e partidas à crédito, não existe mais a opção de gerar em uma única partida o débito e crédito nos módulos de origem. Se o usuário desejar agrupar as partidas/Lançamentos em uma única linha, o agrupamento deve ser feito pelo módulo contábil no processo de **"Agrupamento de Lançamentos".**  **Em caso de dúvidas consulte o help do aplicativo ou entre em contato pelo help desk.** |

  **2 – Pasta – Itens do Evento Contábil**  
    
   O item de evento representa a parametrização identificando de onde virão as informações contábeis que irão compor o lançamento contábil. Cada item pode ser responsável em gerar uma ou mais Partidas do lançamento contábil.   
   Nos itens de um evento são apresentados os seguintes campos:   
  **Aplicar:**  
   Define a origem das informações que serão processadas por este item de evento, ou seja, quando o evento for processar este item a informação virá do contexto do item informado no campo **"Aplicar".**  
    
  **Origem da Conta:**  
   Especifica qual é a origem da conta que será preenchida na Partida do Lançamento Contábil.   
  **Tabela Default**: As partidas serão carregas conforme o cadastro do default informado.  
  **Informar Conta:** A partida será gerada com a conta informada pelo usuário no item de evento.   
  **Buscar Default:**  
   Define onde o item de evento vai buscar as informações contábeis que irá compor o lançamento/partida contábil. Cada item listado nesta opção possui em seu cadastro a opção default contábil, é neste default contábil que o evento busca as informações.  
   Opções disponíveis para:  
   -**Filial**  
  **-Centro de Custo**  
  **-Departamento**  
  **-Localização**

    
  + Grupo de Patrimônio\*
  + Cenário Patrimônio\*


  + Conta do Processo de Contabilização\*   
    **Classificação do Centro Custo:**  
     A classificação do Centro de Custo funciona como um filtro aplicado sobre o centro de custo informado nos defaults contábeis a ser carregado (parametrizado no tópico acima).   
     Exemplo:  
     Se você informar no item de evento uma classificação **"02 - Administrativo"**, o evento contábil somente irá carregar do default contábil as partidas que tiverem o centro custo com a classificação **"02 - Administrativo".**  
    **Classificação Conta:**  
     A Classificação da conta funciona igual à Classificação por Centro de Custo, ou seja, como um filtro, pois neste caso somente serão carregados do default contábil as Partidas que tiverem com a mesma classificação informada nos itens do evento contábil.   
    **Valor/Fórmula:**  
     Identifica a origem do valor que ira ser aplicado nas Partidas a ser gerada.   
    **Percentual:**  
     Percentual a ser aplicado no valor identificado no campo **"Valor".**  
    **Itens Gerenciais**  
     Os itens gerenciais correspondem a parametrização para o preenchimento do rateio das Partidas contábeis geradas pelo item de evento, isto quando a conta identificada exigir rateio.   
    **Origem Conta:**  
     Específica à origem da conta gerencial a ser preenchida no rateio da Partida contábil processada pelo evento contábil.   
     Opções disponíveis:   
    **Tabela Default:**  
     Esta opção permite que a conta gerencial venha da tabela default a serem identificados no item gerencial, neste caso os cadastros a ser listado possui um campo chamado "Conta Gerencial" de onde o evento irá pegar.   
    **Informar Conta**  
     O usuário informa a conta a ser gerada no rateio da Partida Contábil.   
    **Contabilidade (Rateio default da conta contábil):**  
     O evento contábil busca o rateio informado no cadastro da conta contábil, lembrando que não obrigatório ter este rateio na contabilidade.   
    ***Default Contábil:***  
     O evento busca a conta gerencial do default contábil informado no item de evento. Lembrando que esta opção somente poderá ser selecionada se a opção informar conta no item de evento for igual a "Tabela Default" de Centro Custo ou Departamento:   
    **Aplicar em:**  
     Identifica de qual contexto o evento contábil deverá identificar a informação para carregar a conta gerencial.   
    **Descrição e Percentual:** Disponível somente para opção "Tabela Default" e "Informar Conta". Pode ser informado uma descrição para o item gerencial e qual percentual será aplicado.   
      
      
      
    **3 – Pasta - Identificação do Evento de Transferência de Controle**  
      
     No evento de Transferência Monetária, a filial/depto e centro de custo estão configurados para buscar as informações no Patrimônio e aplicar o centro de custo nas contas à débito e à crédito.   
      
      
      
    **4 –Pasta - Itens do Evento de Transferência de Controle**  
      
     Conforme citado anteriormente, a transferência de controle pode ocorrer entre Filiais, Centros de Custos, Departamentos, Localizações e Responsáveis.   
     No evento padrão de transferência de Controle que é apresentado pelo sistema após a conversão, existem 4 itens à débito e 4 itens à crédito (tela apresentada no item 4). Este evento está configurado para patrimônios que sofrem depreciação mensal e também para empresas que necessitam fechar os débitos e crédito em uma mesma filial, assim é necessário utilizar uma conta transitória.   
     Se o patrimônio sofre depreciação mensal, consequentemente o mesmo possuirá depreciação acumulada, portanto na transferência Monetária a mesma deverá também ser transferida.   
     Se o patrimônio transferido não sofre depreciação mensal, somente o valor do patrimônio é que será transferido.   
     Ex: Vamos supor que o Patrimônio X pertencente ao grupo "Veículos" possua os seguintes valores:   
     Valor do Patrimônio = R$ 100.000,00  
     Valor da Depreciação Acumulada = R$ 30.000,00  
     Filial = 1  
     Este patrimônio será transferido para a filial2.   
     O evento padrão de "Transferência de Controle" possui os seguintes itens:   
      
    1 item à crédito com o processo Aplicar = "Transferência de Controle – Origem" buscando o default à crédito com a classificação "PATRIMONIO" existente na tabela de Grupo de Patrimônio.  
    1 item à débito com o processo Aplicar = "Transferência de Controle – Origem" buscando a conta à crédito que será informada no momento do processo de contabilização da Transferência de Controle.  
    1 item à débito com o processo Aplicar = "Transferência de Controle – Destino" buscando o default à debito com a classificação "PATRIMONIO" existente na tabela de Grupo de Patrimônio.  
    1 item à crédito com o processo Aplicar = "Transferência de Controle – Destino" buscando a conta à débito que será informada no momento do processo de contabilização da Transferência Monetária.  
    Estes itens irão contabilizar o valor do patrimônio, que em nosso exemplo é de R$ 100.000,00. O valor de R$ 100.000,00 em nosso exemplo está saindo da conta contábil "Veículos" na filial 1 e entrando na conta contábil também de veículos na filial 2.  
    **Atenção: Cada empresa possui sua conta transitória, portanto o evento padrão está configurado para que a conta transitória seja informada no processo de contabilização, mas o usuário pode alterar o evento deixando esta conta contábil fixa no mesmo.**  
      
    A seguir iremos apresentar os itens de eventos para contabilizar a depreciação acumulada.  
      
    1 item à débito com o processo Aplicar = "Depreciação Acumulada (Transf. Origem) buscando o default à débito com a classificação "PATDEPACUM" existente na tabela de Grupo de Patrimônio.  
    1 item à crédito com o processo Aplicar = "Depreciação Acumulada (Transf. Origem) buscando a conta à crédito que será informada no momento do processo de contabilização da Transferência de Controle.  
    1 item à crédito com o processo Aplicar = "Depreciação Acumulada (Transf. Destino) buscando o default à crédito com a classificação "PATDEPACUM" existente na tabela de Grupo de Patrimônio.  
    1 item à débito com o processo Aplicar = "Depreciação Acumulada (Transf. Destino) buscando a conta à débito que será informada no momento do processo de contabilização da Transferência de Controle.  
    Estes itens irão contabilizar o valor da depreciação acumulada do patrimônio, que em nosso exemplo é de R$ 30.000,00.  
    O valor de R$ 30.000,00 de depreciação acumulada em nosso exemplo está saindo da conta contábil "Depreciação Acumulada de Veículos" na filial 1 e entrando na conta contábil também de "Depreciação Acumulada de Veículos na filial 2.  
      
    **Atenção: Cada empresa possui sua conta transitória, portanto o evento padrão está configurado para que a conta transitória seja informada no processo de contabilização, mas o usuário pode alterar o evento deixando esta conta contábil fixa no mesmo.**  
    Na conversão da base de dados o sistema verifica se o parâmetro "Permite Diferença entre filiais" está marcado. Caso esteja marcado, o evento padrão de transferência de Controle será criado sem a utilização de contas transitórias, caso contrário, o evento é criado utilizando as contas transitórias, de acordo com nosso exemplo.  
      
    **Atenção: Se alguma conta contábil configuradas nos itens de eventos possuírem distribuição gerencial, os itens gerenciais devem ser configurados.**  
    Razonetes da contabilização:  
    Ex:

    Repare que a conta transitória foi utilizada apenas para fechar os débitos e créditos por filial, no final a mesma está zerada. A conta de Veículos após o processo possui o saldo de R$ 100.000,00 na filial 2 e a conta de depreciação acumulada de Veículos possui o saldo de R$ 30.000, também na filial 2.

    Este exemplo portanto apresentou uma transferência monetária entre patrimônios do mesmo grupo com filiais diferentes e que possuíam saldo de depreciação acumulada.

    Em nosso exemplo, o Lanc. 1 e Lanc. 2 correspondem aos itens de evento responsáveis pela contabilização da transferência do valor do Patrimônio (R$ 100.000,00).  
     Os Lanc. 3 e 4 correspondem aos itens de evento responsáveis pela contabilização da transferência do valor da depreciação Acumulada do Patrimônio (R$ 30.000,00).

    Este exemplo explicou o funcionamento dos itens do evento de Transferência de Controle padrão.

    Para maiores informações:

    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

    **COMUNIDADE**[**R@Contábil**](https://totvs.byyou.com/?space=rcontbil)

    **Canais** **de Atendimento:**

    **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

    **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 2 – (Ativo Fixo).
