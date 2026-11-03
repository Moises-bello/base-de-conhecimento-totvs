---
content_hash: 085e6352aa6f820334c3a5ff8793aa6b415988d3a9db9072ea6816318157f84d
fetched_at: '2026-06-29T00:09:00.121625+00:00'
page_id: '364919031'
product: rm
source: tdn-rm
title: Novo SICRO - Alterações em Cadastros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364919031
version: 37
---

**Informações Gerais**

O SICRO (Sistema de Custos Referenciais de Obras) é uma ferramenta criada e aperfeiçoada pelo DNIT para manter atualizada a definição de custos (natureza do insumo), apta para estabelecer os melhores parâmetros para referenciar a elaboração dos orçamentos de Projetos Rodoviários e Licitação de Obras. Sendo assim alguns cadastros foram adequados à necessidade das definições da terceira versão do SICRO:

Essas alterações terão impactos diretamente no cadastro de Grupo de Custo, Insumos, Composições e Recursos de Composições.:

| Classificações Antigas DNIT | Novas Classificações |
| --- | --- |
| A - Equipamento | A - Equipamento |
| B - Mão de Obra | B - Mão de Obra |
| E - Material | C - Material |
| F - Transporte | D - Atividades Auxiliares |
|  | E - Tempo Fixo |
| F - Momento de Transporte |
| C - Produção por Hora | P - Produção por Hora |
| D - Custo Unitário de Execução **((A+B)/C)** | U - Custo Unitário de Execução **((A+B)/P)** |

* **Grupo de Custo:**

* **Composição:**

* **Backup / Restore:**Visando tornar compatíveis os Backups que foram realizados em versões do TOTVS Obras e Projetos que não contemplam a implementação do novo SICRO 3, onde a partir dessa versão, sempre que for criado um novo Backup de Projeto, o mesmo será definido com uma versão de controle interno do sistema. Nesse caso do SICRO a versão inicial será a **"1.0.0"**e é possível verificar no arquivo  **MPRJ.xml.**

Todo backup anterior à esta versão sofrerá alterações nas tabelas de Grupos de Custo (MGIS), Insumos (MISM), Composições (MCMP) e Recursos de Composição (MRECCMP), onde os registros que tiverem os respectivos campos definidos como **"Material"**, isto é o código **"E"**, serão alterados para o novo código **"C".**

* **Insumo:** O cadastro de Insumos foi adequado à necessidade de novas definições do SICRO que permite que Fatores de Eficiência tenham incidência na execução de alguns serviços que impactam diretamente no custo de um projeto. **Na tela de edição de insumos existe o "Fator de Eficiência" que somente pode ser definido caso a unidade seja do tipo "Percentual (%)"**. Os Fatores são os seguintes:  
    
  + **FIC - Fator de Influência de Chuvas:**Em face de sua natureza essencialmente linear, o conhecimento das condições climáticas regionais constitui fator fundamental para o planejamento de uma obra de infraestrutura de transportes. Por meio do tratamento da série histórica de centenas de estações pluviométricas do país, o SICRO propõe a utilização de um Fator de Influência de Chuvas, o FIC, a ser aplicado sobre o custo unitário de execução dos serviços que sofram influência das chuvas em sua produção. FIC incidirá sobre o custo unitário de execução de mão de obra e equipamentos, das composições de custos principais, dos serviços auxiliares e momento de transporte. Importante destacar que as atividades relacionadas à usinagem de materiais não fazem jus à aplicação do FIC;
  + **FIT - Fator de Interferência do Tráfego:**Durante a execução de obras em rodovias novas ou existentes, o volume de tráfego local é fator real de redução de produção dos serviços, principalmente nas proximidades dos grandes centros. Por essa razão, o SICRO apresenta o conceito de Fator de Interferência de Tráfego, o FIT, a ser aplicado sobre o custo unitário de alguns serviços nas obras de melhoramentos, de adequação de capacidade, de restauração, de conservação e de transporte, em função do volume médio diário de tráfego. No SICRO, a aplicação do FIT incidirá sobre todos os serviços que estejam sujeitos efetivamente à interferência do tráfego, cabendo ao orçamentista sua classificação e definição em função do volume médio diário e da proximidade de centros urbanos. No caso da elaboração de projetos que envolvam segmentos com comportamento heterogêneo em termos de volume médio diário de tráfego, recomenda-se definir um fator de interferência de tráfego médio em função da ponderação dos fatores de interferência obtidos nas diferentes seções em relação à extensão total do trecho. O FIT incidirá sobre o custo unitário de execução de mão de obra, equipamentos, atividades auxiliares e momento de transporte.

Ao cadastrar o insumo que tenha o fator de eficiência, é necessário que a unidade do mesmo seja "Percentual (%)", pois o cálculo envolvendo o FIC e FIT deve considerar os insumos que pertencem aos grupos DNIT específicos. O Grupo de Custo no qual o insumo estará associado deve ter o Grupo DNIT definido como "Nenhum" essa consistência será realizada no momento de salvar o cadastro do insumo, no cálculo da composição no qual o insumo está associado como recurso e no cálculo do projeto. Uma mensagem de alerta será exibida, tanto no cadastro quanto no log do cálculo:

Os valores dos Fatores de Eficiência, na composição, podem ser vistos de forma distinta no painel de valores, onde os mesmos são atualizados após o cálculo da composição. O cálculo do FIC e FIT pode ou não considerar o Custo Unitário de Execução que é representado pela letra "U" na tela de edição de composições e considera também, os grupos DNIT que estão associados ao Grupo de Custo do Insumo e que serão utilizados para o cálculo do insumo percentual. São três principais possibilidades de como o cálculo pode ser realizado:

* Com nenhum grupo de custo selecionado para percentual: O cálculo será realizado considerando o Custo Unitário, isto é, (Equipamento + Mão de Obra) / Produção;
* Com no mínimo um grupo de custo selecionado para percentual desde que não tenha Equipamento e Mão de Obra: O cálculo será realizado considerando apenas o impacto no grupo de custo selecionado;
* Com Equipamento e Mão de Obra entre os grupos de custo selecionados para percentual: O cálculo será realizado considerando o Custo Unitário e o impacto nos demais grupos de custo selecionados.

Abaixo um exemplo de como o cálculo é realizado:

* **FIC:**
* **FIT:**

* + **Relatórios:**

| Classificações Antigas | Novas Classificações |
| --- | --- |
| C - Produção por Hora | P - Produção por Hora |
| D - Custo Unitário de Execução **((A+B)/C)** | U - Custo Unitário de Execução **((A+B)/P)** |
| Custo Direto Total **D+E+F** | Custo Direto Total **U+C+D+E+F** |

* **Recursos Vinculados:**  
  No cadastro de Recursos de Composição, existe o anexo de "Recursos Vinculados" que permite que recursos da mesma composição "mãe" insumo possam ser vinculados à um recurso do tipo composição auxiliar que esteja presente na mesma composição principal. Essa necessidade se deu a partir de informações e regras do DNIT que define que uma composição auxiliar pode representar um custo do tempo ou do transporte de um determinado material, como pode ser visto na imagem abaixo:  

  No exemplo acima, é possível notar que o Material **"M0082** **Areia média lavada"** está presente na composição como **MATERIAL**, **TEMPO FIXO** e **MOMENTO DE TRANSPORTE,**porém trata-se somente de um material. No caso dos outros grupos, o que representa o custo com o material, seriam as composições 5914647 para tempo fixo e 5914359, 5914374 e 5914389 para momento de transporte.

  Sendo assim, para que essa representação possa ser considerada e que um relatório possa exibir essa "amarração" existe o cadastro de Recursos Vinculados:

    
  Para composições auxiliares do tipo "Momento de Transporte", se faz necessário que no momento do cadastro do Recurso Vinculado, sejam definidos os valores dos DMT's que são específicos para cada recurso relacionado ao transporte, onde o cálculo realizado afim de definir o Valor Parcial da composição auxiliar considera essas grandezas, como no exemplo a seguir:
* **BDI da composição e Fator FIT e FIC**
* Algumas considerações são importantes, tais como:

  + Somente recursos da mesma composição principal podem ser vinculados;
  + Somente em Recursos do tipo Composição que é possível realizar o vínculo;
  + A soma das quantidades dos recursos vinculados atualiza a quantidade do recurso pai;
  + Tanto o cálculo da composição pai quanto o cálculo do projeto atualizam a quantidade do recurso que tem vinculo;
  + O campo quantidade da visão de recursos e da tela são somente leitura para recursos que possui vinculados;
  + O mesmo recurso só pode ser vinculado uma única vez em outro recurso;
  + Os DMT's somente podem ser definidos para Tipos de Associação LN, RP ou P sendo que é possível apenas um dos tipos.
  + O Tempo Fixo e Momento de Transporte não interfere no cálculo, só é visível no relatório.

**Vídeos sobre a funcionalidade:**
