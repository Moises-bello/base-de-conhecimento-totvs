---
content_hash: 3d1b24ac47a18cb56108140560888ecfebf312a91ae4374639724e701453219c
fetched_at: '2026-06-29T00:09:15.530785+00:00'
page_id: '421385402'
product: rm
source: tdn-rm
title: Cálculo do Projeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385402
version: 39
---

---

**Cálculo**

Esse menu permite calcular o projeto corrente naquele momento, ou seja, recalcula tudo que está sendo utilizado pelo projeto e grava na base de dados os valores e a data/hora do cálculo.

Após a efetuação do cálculo do projeto, as alterações podem ser feitas normalmente, mas o projeto não é recalculado automaticamente.

No momento da execução do cálculo, caso haja   ativos, é possível escolher qual(ais) Cenário(s) serão calculados, assim como as Planilhas de Atividades e Serviço.

Ao final da execução do cálculo, os valores referente à cada planilha calculada assim como dos Cenários poderão ser visualizados no Resumo do Projeto no menu Projeto | Resumo do Projeto.

Importante

Os valores lançados na barra superior da visão principal sempre corresponderá a valores da Planilha de Atividades.

Mesmo que alguma Planilha (Atividade ou Serviço), assim como algum Cenário esteja aplicando o filtro de Obras, o cálculo será aplicado por completo, ou seja, para todas as Obras das planilhas ou cenários selecionados no momento da Obra.

O cálculo não considera Cenários inativos ou Cenários ativos que não tenham sido selecionados.

Esta opção não estará ativa caso não haja nenhum projeto aberto.

**Como é feito o cálculo do cronograma:**

* O cronograma considera os valores dos insumos conforme preço ativo, inativo ou vigente:
  + O cronograma pode ser Realizado, Previsto ou Medido;
* Para os Cenários não há disponibilidade dos Cronogramas Realizado ou Medido, apenas Previsto:
  + O cálculo verifica se o parâmetro "Todo o Projeto" ou "Somente Cronograma" está marcado, caso esteja marcado "todo o projeto" o sistema usa o cálculo no cronograma e no projeto, caso esteja marcado "somente cronograma" o sistema usa apenas para o cronograma;
  + O sistema verifica se existe preço vigente cadastrado no sistema, caso tenha, ele utiliza o mesmo para o cálculo de acordo com o período usado pela vigência, se não existir o sistema usa o preço ativo do insumo;
  + Caso esteja marcado o parâmetro "Não Utiliza" , o sistema utilizara o valor ativo do insumo e não o vigente;

**Como é feito o cálculo do projeto:**

+ Identificação das tarefas a serem calculadas:
  - **Filtro de obras:** O filtro de obras não interfere no cálculo do projeto;
  - **Aplicar filtro de serviços ativos:** Serão consideradas no cálculo do projeto somente tarefas, etapas e obras ativas;
+ Cálculo dos Insumos utilizados no projeto:
  - Identificar o preço ativo a ser considerado:

    **Insumo local:** Considera o preço ativo ou vigente;

    **Insumo global:** Considera o preço ativo local ou vigente. Se não existir, considera o preço ativo global;

    Caso exista preço vigente e o parâmetro esteja habilitado para "todo o projeto", o sistema ira considerar o preço vigente para realizar o cálculo;

    Se nenhum preço estiver ativo ou o parâmetro "todo o projeto" não estiver marcado, o preço do insumo será igual a zero;
  - Aplicar indexação / conversão de moeda:

**Indexação:** Acontece quando o insumo possui uma moeda indexadora;

**Converter:** Acontece quando a moeda do sistema difere da moeda do preço;

O preço é indexado / convertido para moeda do preço do insumo conforme a cotação da moeda na data do parâmetro [Data Base para indexação] e [Data Base para conversão];

**Fórmula de conversão:**

**Preço do insumo**

1- Valor da Cotação baseado na moeda do preço Fórmula de indexação: Preço do insumo / Valor da Cotação baseado na moeda indexadora na data de atualização do preço;

2- Valor da Cotação baseado na moeda do preço na data atual;

Se o preço do insumo não tem moeda indexadora e a moeda do preço for diferente da moeda do projeto, é feita a conversão do valor somente para o cálculo do projeto e o valor do preço do insumo não é alterado. Se o preço do insumo está numa moeda diferente da moeda do projeto e tem uma moeda indexadora, é feita a indexação e depois a conversão para o cálculo do projeto e o valor do preço do insumo não é alterado. Se o preço do insumo está na moeda do projeto e tem uma moeda indexado, é feita somente a indexação para o cálculo do projeto e o valor do preço do insumo não é alterado. Para insumos globais vale a mesma regra dos insumos locais. 

* + **Aplicar conversão de unidade:** Somente acontece quando a unidade do insumo difere da unidade do preço. 
    - Fórmula: (Produto de 2.2) / Fator Conversão Unidade Preço \* Fator Conversão Unidade Insumo;

Exemplo

* Temos um insumo que tem a unidade M (metro) e que seu preço esteja em CM (centímetro).

* No cadastro de unidade, o CM tem como unidade base o M com fator de conversão igual a 0,01.

* O M tem como unidade base o próprio M com fator de conversão igual a 1.

Primeiro o sistema verifica se as unidades bases são iguais.

* Para se chegar ao fator de conversão, divide-se o fator da unidade de origem pelo da unidade de destino:

**Fator de Conversão = Fator do CM (Unidade Origem) / Fator do M (Unidade de Destino) = 0,01 / 1 = 0,01**

A partir deste fator, chegamos ao cálculo:

* Caso a conversão seja de quantidade (por exemplo no Pedido) seja preciso requisitar 500 cm de um determinado produto e a unidade de compra no Suprimentos/Faturamento seja M, logo será pedido 500 \* 0,01 = 5 M
* Caso a conversão seja de preço (por exemplo no cálculo do insumo) e o preço do insumo seja R$ 5,00 o CM e o insumo esteja em M, logo o preço deste insumo será 5 / 0,01 = R$ 500,00.

* **Aplicar lei social:**

Acontece quando o grupo de custo do insumo especifica o uso de um fator de lei social.

O valor do fator é definido através dos parâmetros do projeto [Lei Social - Fator 1] ou [Lei Social - Fator 2].

**Fórmula:** **(Produto de 2.3) \* Fator da Lei Social** Se o insumo for global, a lei a ser aplicada (1 ou 2) será aquela definida no grupo de custo global do insumo. Mas, será considerada a taxa de lei definida no projeto onde o insumo foi inserido.

Isso significa que o insumo global do grupo de custo global que indica que, deve ser aplicada a taxa de lei social 1, sofrerá aplicação da lei com a taxa 1 do projeto onde o insumo for inserido.

O preço improdutivo do insumo não sofre incidência de leis sociais.

* + **Aplicar BDI do grupo de custo:** Quando existe BDI definido para o grupo de custo do insumo e o parâmetro para sua utilização está habilitado [BDI - Utilização - Grupo de Custo] este é aplicado:

**Fórmula: (Produto de 2.4) \* BDI do Grupo de Custo** O preço improdutivo do insumo não sofre incidência do BDI do grupo de custo.

* **Cálculo de tarefa que possui Valor Cotado**
  + O valor cotado da tarefa é obtido selecionando o campo VALOR da tabela MTRF (desde que a tarefa não possua tarefas percentuais associadas).

* **Cálculo de Composições utilizadas no projeto**
  + **Filtrar recursos a serem utilizados:** Selecionar todos os recursos que não são percentuais e que estejam ativados.
  + Calcula composição por preço unitário
    - **Buscar preço do insumo:** Calcular o preço do insumo através do processo 2 (Cálculo do Insumo).
    - **Aplicar fator K do insumo:** Caso o parâmetro de utilização de fator do insumo esteja marcado como [Como Fator Multiplicador aos Coeficientes dos Insumos nas Composições], o fator definido no insumo deve ser aplicado ao seu preço. **Fórmula: Preço do Insumo \* Fator K do insumo**
    - **Buscar preço da composição auxiliar:** Calcular o preço da composição auxiliar através do processo 4.
    - **Aplicar a quantidade do recurso:** Fórmula: **Quantidade \* 1**
    - **Aplicar fator K da composição:** Se o parâmetro [Fator K da Composição - Utiliza] estiver marcado, aplica este fator ao preço do recurso. **Fórmula: Fator K da Composição \* (Produto de 4.2.4).**
    - **Calcular valor do recurso:**Para recurso composição: Fórmula: **(Produto de 4.2.5) \* (Produto de 4.2.3)**
    - **Aplicar lei social sobre o custo total do grupo na composição:** Acontece quando o parâmetro [Aplicar Lei Social sobre - Valor Total do Grupo na Composição] está selecionado. Neste caso, os recursos de um mesmo grupo de custo devem ser agrupados (exceto as composições auxiliares e os recursos percentuais) e em cada grupo deve ser aplicado sua respectiva lei social. O valor de leis sociais da composição será o somatório dos valores de leis destes grupos de custo. **Fórmula: Somatório do custo parcial dos recursos do grupo de custo \* Fator de Lei Social para o grupo de custo.**
    - **Calcular insumos percentuais:** Devem ser selecionados todos os recursos ativos da composição (exceto percentuais e composições auxiliares) que pertençam aos grupos de custo unitário do grupo de custo do insumo percentual que está sendo calculado. Após esta seleção, é feito o somatório do custo parcial destes recursos e multiplicado pela quantidade do recurso. Se a lei está sendo aplicada sobre o custo unitário, o insumo percentual será calculado considerando as leis dos grupos de custo que afetam seu valor. Se a lei está sendo aplicada sobre o total do grupo na composição, o insumo percentual será calculado desconsiderando as leis dos grupos de custo que afetam seu valor.
    - **Calcular Composição:** O valor da composição por preço unitário é obtido somando-se o custo parcial de todos os seus recursos.

**Após esse cálculo, já temos:**

1. Valor da composição com BDI do projeto;
2. Valor da composição sem BDI do projeto;
3. Valor de leis sociais;
4. Valor com leis sociais sem BDI do projeto;
5. Valor sem leis sociais;
6. Valor de cada grupo DNIT;
7. Valor do BDI do projeto;

* Calcula composição por produção
  + **Buscar preço do insumo:** Calcular o preço do insumo através do processo 2 (Cálculo do Insumo);
  + **Aplicar fator K do insumo:** Caso o parâmetro de utilização de fator do insumo esteja marcado como [Como Fator Multiplicador aos Coeficientes dos Insumos nas Composições], o fator definido no insumo deve ser aplicado ao seu preço. **Fórmula: Preço do Insumo (produtivo e improdutivo no caso de grupo DNIT A - equipamentos) \* Fator K do insumo;**
  + Caso o parâmetro de utilização de fator do insumo esteja marcado como [Somente insumos mão de obra de composições por produção] e o insumo pertença ao grupo DNIT B (mão-de-obra), o fator k do insumo deve ser aplicado ao seu preço. **Fórmula: Preço do Insumo (produtivo e improdutivo no caso de grupo DNIT A - equipamentos) \* Fator K do insumo;**
  + **Buscar preço da composição auxiliar:** Calcular o preço da composição auxiliar através do processo 4.
  + **Aplicar a quantidade do recurso:** Fórmula: **Quantidade \* 1**
  + **Aplicar fator K da composição:** Se o parâmetro [Fator K da Composição - Utiliza] estiver marcado, aplicar este fator ao preço do recurso. **Fórmula: Fator K da Composição \* (Produto de 4.3.4).**
  + **Calcular coeficiente produtivo (somente para insumos do grupo DNIT A - equipamentos):** Fórmula: **Conteúdo do campo COEFICIENTEPRODUTIVO do recurso**
  + **Calcular coeficiente improdutivo (somente para insumos do grupo DNIT A - equipamentos):**
    - Parâmetro [Aceita coef. Improdutivo igual a ZERO] habilitado:
      * Fórmula: **Conteúdo do campo COEFICIENTEIMPRODUTIVO do recurso**
    - Parâmetro [Aceita coef. Improdutivo igual a ZERO] desabilitado:
      * Fórmula: **1 - (Produto de 4.3.6)**
  + **Calcular custo produtivo (somente para insumos do grupo DNIT A - equipamentos):** Fórmula: **((Produto de 4.3.5) \* (Produto de 4.3.2 - produtivo) \* (Produto de 4.3.6));**
  + **Calcular custo improdutivo (somente para insumos do grupo DNIT A - equipamentos):** Fórmula: **((Produto de 4.3.5) \* (Produto de 4.3.2 - improdutivo) \* (Produto de 4.3.7));**
  + **Aplicar DMT (somente para insumos do grupo DNIT F - momento de transporte):** Fórmula: **(Produto de 4.3.5) \* DMT**
  + **Calcular valor do recurso:**
    - Para recurso insumo do grupo DNIT A:
      * Fórmula: **(Produto de 4.3.8) + (Produto de 4.3.9)**
    - Para recurso insumo do grupo DNIT F:
      * Fórmula: **(Produto de 4.3.10) \* (Produto de 4.3.2 - produtivo)**
    - Demais recursos:
      * Fórmula: **(Produto de 4.3.5) \* (Produto de 4.3.2 - produtivo)**
  + **Aplicar lei social sobre o custo total do grupo na composição:** Acontece quando o parâmetro [Aplicar Lei Social sobre - Valor Total do Grupo na Composição] está selecionado. Neste caso, os recursos de um mesmo grupo de custo devem ser agrupados (exceto as composições auxiliares e os recursos percentuais) e em cada grupo deve ser aplicado sua respectiva lei social. O valor de leis sociais da composição será o somatório dos valores de leis destes grupos de custo. Fórmula: Somatório do custo parcial dos recursos do grupo de custo \* Fator de Lei Social para o grupo de custo;
  + **Calcular insumos percentuais:** Devem ser selecionados todos os recursos ativos da composição (exceto percentuais) que pertençam aos grupos DNIT percentuais do grupo de custo do insumo percentual que está sendo calculado. Após esta seleção, é feito o somatório do custo parcial destes recursos e multiplicado pela quantidade do recurso. Se a lei está sendo aplicada sobre o custo unitário, o insumo percentual será calculado considerando as leis dos grupos de custo que afetam seu valor. Se a lei está sendo aplicada sobre o total do grupo na composição, o insumo percentual será calculado desconsiderando as leis dos grupos de custo que afetam seu valor;
  + **Calcular Composição:** Fórmula**:** **((Somatório do custo dos recursos de grupo DNIT A) + (Somatório do custo dos recursos de grupo DNIT B)) / Produção por hora + (Somatório do custo dos recursos de grupo DNIT C) + (Somatório do custo dos recursos de grupo DNIT F);**

* **Calcula tarefa**
  + **Aplicar quantidade da tarefa:** Fórmula: **(Produto de 2 ou Produto de 3 ou Produto de 4) \* Quantidade da tarefa Se tiver um insumo associado à tarefa**, o valor da tarefa não considera o fator k do mesmo.
  + **Aplicar quantidade de obras:** Somente acontece caso o parâmetro [Considerar quantidade de obras] está habilitado. Neste caso, deve ser aplicado o conteúdo do campo Quantidade da obra a qual a tarefa que está sendo calculada pertence. O valor default é 1. Fórmula: **(Produto de 5.2) \* Quantidade da obra**
  + **Aplicar BDI do projeto:** Somente acontece quando os parâmetros [BDI - Utilização - Projeto] e [Aplicar BDI do projeto sobre - Custo Unitário dos serviços] estão habilitados e o BDI do projeto não é calculado. Fórmula: **(Produto de 5.2) \* BDI do projeto**
  + **Aplicar BDI diferenciado:** Somente acontece quando o parâmetro [BDI - Utilização - Diferenciado] está habilitado. Fórmula: **(Produto de 5.3) \* BDI diferenciado**
* **Calcula o valor do Projeto**
  + **Calcular BDI do projeto:** Acontece quando o parâmetro [BDI - Calculado] está habilitado
    - **Cálculo das taxas:** Fórmula: (**somatório das taxas do projeto) / 100**
    - **Cálculo do BDI em função das taxas:**  Fórmula: **(1 / (1 - (Produto de 6.1.1)))**
    - **Cálculo do custo direto:** somatório dos serviços diretos do projeto
    - **Cálculo do custo indireto:** somatório dos serviços indiretos do projeto
    - **Cálculo do preço de venda:**
      * Fórmula: **((Produto de 6.1.3) + (Produto de 6.1.4)) \* (Produto de 6.1.2)**
      * Fórmula do BDI: **((Produto de 6.1.3) + (Produto de 6.1.4)) + ((Produto de 6.1.1) \* (Produto de 6.1.5) / (Produto de 6.1.3)) + 1**
  + **Aplicar BDI do projeto:** Caso os parâmetros [BDI - Utilização - Projeto], [Aplicar BDI do projeto sobre - Custo Unitário dos Serviços] e [BDI - Calculado] estejam habilitados, aplico o BDI calculado do projeto em todos os serviços ativos e que não possuem associação percentual.
  + **Calcular tarefas percentuais:** Para cada tarefa com associação percentual encontrada, deverá ser selecionado todos os serviços que estão vinculados a ela e seus respectivos percentuais. Fórmula: **(Somatório da multiplicação de cada percentual das tarefas associadas pelo seu respectivo ValorTotal) \* BDI diferenciado (caso o parâmetro [BDI - Utilização - Diferenciado] esteja habilitado) \* Quantidade**
  + **Calcular etapas e obras:** todos os valores superiores dos serviços (etapas e obras) devem ser calculados de acordo com os seus serviços filhos. Fórmula **(para cada obra ou etapa): (somatório de todos os serviços filho)**
  + **Calcular projeto:** O valor do projeto é obtido através do somatório do custo de todos os serviços ativos e de custo direto da planilha de tarefas (de acordo com o filtro aplicado no processo 1).  
    Caso os parâmetros [BDI - Utilização - Projeto] e [Aplicar BDI do projeto sobre - Valor Total do Projeto] estejam habilitados, o BDI do projeto deve ser aplicado sobre o valor total.

**Pós cálculo do projeto**

Após executar o cálculo do projeto, caso as Planilhas de Atividades e Serviços estejam abertas, as mesmas serão atualizadas com os valores que o processo calculou. Se alguma alteração tiver sido feita em ambas as planilhas e não tiver sido salva, antes de atualizar, uma mensagem será exibida informando que as alterações serão perdidas e se deseja continuar.

---

 Veja Também

---
