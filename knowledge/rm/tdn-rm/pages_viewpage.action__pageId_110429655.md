---
content_hash: 1fc3d8a69bcd136c9915dc7710a73b8f0b667128afc3c23691ebe5c869f769ec
fetched_at: '2026-06-29T00:05:54.830987+00:00'
page_id: '110429655'
product: rm
source: tdn-rm
title: RMPAT00003_Evento Contábil de Aquisição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=110429655
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Gestão Patrimonial 11.50 |
| **Processo** | : | Evento Contábil de Aquisição |
| **Subprocesso** |  | Gestão Patrimonial |
| **Data da publicação** | : | 02/08/2012 |

**Introdução**

No Bonum.Net todas as contabilizações são feitas utilizando eventos contábeis. O recurso de eventos contábeis permite maior flexibilidade na definição das contabilizações existentes no sistema. Para cada processo será necessário criar um tipo de evento.   
 Exemplo: Precisaremos criar um evento de aquisição, um evento para baixas, acréscimos, depreciações etc.  
 Cada empresa pode parametrizar os seus eventos para contabilizar de acordo com as contas desejadas, portanto a contabilização ficará bem flexível e permitirá que cada empresa monte seus eventos de acordo com seus processos internos de contabilização.  
 Este documento tem o objetivo de explicar o funcionamento **do evento contábil de Aquisição padrão** que é disponibilizado a partir da versão 11.50 ou superiores

|  |
| --- |
| Na conversão das tabelas do TOTVS Gestão Patrimonial para a versão 11.50 ou superiores, o sistema já cria o evento contábil de Aquisição e vincula o mesmo aos grupos de Patrimônios existentes na coligada. Com isto, o trabalho do responsável pelo sistema será de revisar os eventos que foram convertidos, e se desejado poderá alterar o evento para contabilizar de acordo com a necessidade da empresa.   **Em caso de dúvidas consulte o help do aplicativo ou entre em contato pelo help desk.** |

**Desenvolvimento/Procedimento**

No TOTVS Gestão Patrimonial a aquisição de um patrimônio pode ser feita manualmente ou via integração com o módulo de compras (RM Nucleus). No caso dos patrimônios originados do Nucleus a contabilização da aquisição é feita na inclusão do Movimento, portanto somente as aquisições de Patrimônio manuais pelo TOTVS Gestão Patrimonial é que serão contabilizadas.   
 Antes de citarmos os campos e itens do evento contábil de Aquisição, vamos apresentar o conceito sobre o processo de Aquisição de Patrimônios.  
 Ex: Vamos supor que a empresa adquiriu um veículo para realizar a entrega de mercadorias . Esta operação significa que houve uma entrada no ativo imobilizado da empresa, e uma saída de recursos para a aquisição do veículo, a saída de dinheiro do caixa da empresa pode ser considerado a saída do recurso.   
 Assim a contabilização ficaria da seguinte maneira:   
 **Débito – Conta de Veículos**  
 **Crédito – Conta Caixa**   
 Na contabilidade os débitos são considerados **"aplicações"** e os créditos **"Origens de Recursos".** Devemos sempre lembrar que as contas contábeis pertencem à empresa, ou seja, os débitos (aplicações) registrados no ativo são devedores porque pertencem aos sócios da empresa e os créditos registrados no Passivo e Patrimônio Líquido são credores porque os mesmos possuem créditos com os sócios da empresa, por este motivo as contas do Ativo são devedoras (com algumas exceções) e as contas do passivo são credoras (com algumas exceções).  
 A seguir vamos apresentar as pastas/campos existentes em um evento e a configuração do evento de aquisição:

1. **Pasta - Identificação:**

**Processo:** Neste campo é informado o processo que corresponde o evento, em nosso exemplo o processo é **"Aquisição".**   
 **Inativo** – Quando esta opção estiver marcada o evento contábil estará inativo e não poderá ser utilizado nas contabilizações..   
   
 **Número: Corresponde ao número do evento**  
 **Nome: Corresponde ao nome do evento**   
 **Calcular valor a partir de:**   
 Define como o valor dos itens contábeis será calculado, podendo ser através de fórmula ou percentual. Estes dois itens serão informados posteriormente nos itens do Evento Contábil   
 **Fórmula:** O evento pode possuir uma fórmula para cálculo do valor da contabilização**.**   
 Vamos supor que seja criado uma fórmula no RM Bonum para buscar o valor de Aquisição menos o valor de determinado imposto x. Ao criar o evento de aquisição e utilizar esta fórmula o valor a ser contabilizado para os itens do evento serão calculados pela fórmula vinculada ao mesmo.   
 OBS: Na versão 11.50 os eventos não são calculados por fórmula.   
   
 **Percentual:** O evento pode ser calculado por percentual. Ex: No evento de aquisição, ao incluir um item do evento deve ser definido o valor de aquisição, deste valor o usuário informa qual percentual irá contabilizar. Lembrando que os itens à débito e à crédito devem sempre fechar em  
 **Buscar Filial/Depto em:** Neste campo deve ser informado de onde deseja-se buscar os dados de filial e departamento.   
 Se fôr informado a opção **"Evento Contábil"**, ao contabilizar o processo, o sistema irá verificar em cada item do evento dentro da pasta **"Dados Complementares",** a filial e Depto informados.  
 Se fôr informada a opção **"Default Contábil",** na contabilização do processo, o sistema irá verificar a filial e depto que estão informadas nos default's das tabelas que estão sendo utilizadas nos itens do evento contábil.   
 **Buscar Centro de Custo em:** Da mesma maneira que os dados de filial e departamento, deve ser informado onde os dados de centro de custo serão buscados para que sejam informados na contabilização.   
 **Importante:** O Evento Contábil tentar buscar Filial/Departamento ou Centro de Custo conforme a ordem definida (para mudar ordem utilize as setas).   
 Exemplo C. Custo:

* Ordem parametrizada  
   1º Patrimônio - Se não achar no Patrimônio tenta achar no Evento Contábil  
   2º Evento Contábil - Se não achar no Evento Contábil tenta achar no Default Contábil  
   3º Default Contábil - Se não achar no Default fica sem centro de custo   
    
  **Aplicar Centro de Custo em:** Define em qual dos itens (Débito ou Crédito) o centro de custo será preenchido.  
   Algumas empresas não informam centros de custos em determinadas contas, então deve-se informar neste campo em quais contas a informação será gerada.  
  **Agrupa Partida Contábil:** Marcando esta opção, se os itens do evento (contas contábeis) possuírem mesma conta, centro de custo, filial, departamento e histórico padrão, os itens são agrupados gerando somente uma partida contábil  
    
    
  **2 – Pasta – Itens do Evento Contábil**  
   O item de evento representa a parametrização identificando de onde virão as informações contábeis que irão compor o lançamento contábil. Cada item pode ser responsável em gerar uma ou mais Partidas do lançamento contábil.   
  **Aplicar:**  
   Define a origem das informações que serão processadas por este item de evento, ou seja, quando o evento for processar este item a informação virá do contexto do item informado no campo "Aplicar".   
  **Origem da Conta:**  
   Especifica qual é a origem da conta que será preenchida na Partida do Lançamento Contábil.  
  **Tabela Default**: As partidas serão carregas conforme o cadastro do default informado.  
  **Informar Conta:** A partida será gerada com a conta informada pelo usuário no item de evento.   
  **Buscar Default:**  
   Define onde o item de evento vai buscar as informações contábeis que irá compor o lançamento contábil. Cada item listado nesta opção possui em seu cadastro a opção default contábil, é neste default contábil que o evento busca as informações.   
   Opções disponíveis para:   
   -Filial  
   -Centro de Custo  
   -Departamento  
   -Localização
* Grupo de Patrimônio
* Cenário Patrimônio
* Conta do Processo de Contabilização   
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
  ***Tabela Default:***  
   Esta opção permite que a conta gerencial venha da tabela default a serem identificados no item gerencial, neste caso os cadastros a ser listado possui um campo chamado "Conta Gerencial" de onde o evento irá pegar.   
  ***Informar Conta***  
   O usuário informa a conta a ser gerada no rateio da Partida Contábil.   
  ***Contabilidade (Rateio default da conta contábil):***  
   O evento contábil busca o rateio informado no cadastro da conta contábil, lembrando que não obrigatório ter este rateio na contabilidade.   
  ***Default Contábil:***  
   O evento busca a conta gerencial do default contábil informado no item de evento. Lembrando que esta opção somente poderá ser selecionada se a opção informar conta no item de evento for igual a "Tabela Default"  
   Rateio Centro Custo:  
   Rateio Departamento:   
  **Aplicar em:**  
   Identifica de qual contexto o evento contábil deverá identificar a informação para carregar a conta gerencial.   
  **Descrição e Percentual:** Disponível somente para opção "Tabela Default" e "Informar Conta". Pode ser informado uma descrição para o item gerencial e qual percentual será aplicado   
    
    
  **3 – Pasta Identificação do Evento de Aquisição**  
    
    
    
   No evento de Aquisição, a filial/depto e centro de custo estão configurados para buscar as informações no Patrimônio**.**  
  **4 – Itens do Evento de Aquisição - Débito**  
    
   O item à débito irá buscar o default de débito existente no grupo de Patrimônio.  
   Seguindo nosso exemplo, na aquisição do patrimônio seria informado no campo "Grupo de Patrimônio" o grupo corresponde à Veículos. Assim, ao contabilizar a aquisição o sistema irá buscar a conta à debito deste grupo classificada como "Patrimônio".   
  Atenção: Os defaults contábeis também são criados automaticamente na conversão da base para todos os grupos de contas existentes antes da conversão. Portanto, somente para os novos grupos de patrimônios é que o usuário precisará cadastrar seus defaults contábeis.   
    
    
  **5 – Itens do Evento de Aquisição – Crédito**  
    
    
   O item à crédito será informado no processo de contabilização da aquisição. No momento que o usuário estiver contabilizando a aquisição deverá informar a conta à crédito.  
   Seguindo nosso exemplo, no momento da contabilização da aquisição do patrimônio seria informado a conta Caixa.   
    
   Estes são os itens do evento de aquisição padrão, lembrando que o mesmo poderá ser alterado a qualquer momento.   
  **Atenção:** Se alguma conta contábil configuradas nos itens de eventos possuírem distribuição gerencial, os itens gerenciais devem ser configurados.

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE**[**R@Contábil**](https://totvs.byyou.com/?space=rcontbil)

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 2 – (Ativo Fixo).
