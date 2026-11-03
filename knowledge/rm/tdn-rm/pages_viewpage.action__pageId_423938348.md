---
content_hash: a2551e7fecf15629c5a5c8b5d4a4e740f5618acfb61f4d4b36d0fbe9c75bd0bc
fetched_at: '2026-06-29T00:09:26.643621+00:00'
page_id: '423938348'
product: rm
source: tdn-rm
title: Depreciação/Correção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938348
version: 19
---

Responsável pela contabilização dos valores da depreciação e correção monetária dos patrimônios, este processo cria lançamentos contábeis de acordo com a parametrização definida no (s) evento (s) contábil (eis) de forma que, posteriormente, sejam enviados para o sistema contábil a partir do processo "Integrar Contabilização".  
A contabilização será efetuada apenas para o período corrente. Ou seja, caso nos parâmetros do sistema o mês de cálculo esteja igual a Janeiro e o ano a 2024 todos os valores de depreciação e correção referentes a Janeiro de 2024 serão contabilizados.

**Observações**

Não é permitido que um grupo de patrimônio tenha mais de 1 evento classificado como de depreciação e 1 classificado como de correção monetária associado a ele (em Anexos/Default Cenário);   
- É importante que os eventos contábeis de depreciação e correção monetária estejam devidamente cadastrados de forma a garantir que o processo possa criar os lançamentos que serão, posteriormente, enviados os sistema contábil;   
- Após a realização da contabilização da depreciação e/ou correção não é permitida a execução dos seguintes processos:   
Cálculo de Depreciação;   
Ocorrências: Baixa (Total ou Parcial), Acréscimo  
Transferência Monetária;   
Nova contabilização da depreciação/correção monetária sem que antes seja executado o processo de Exclusão de Contabilização da Depreciação/Correção Monetária.

**Parametrização do Totvs Gestão Contábil**

Antes da realização da Contabilização de Depreciação/Correção Monetária é importante verificar as seguintes opções nos parâmetros do sistema contábil:

- **Tamanho do  Documento**: o número do documento (que será armazenado no lançamento contábil) informado no processo de contabilização tem que respeitar o tamanho máximo permitido no sistema contábil;   
- **Usa Centro de Custo**: Caso esta opção esteja marcada nos parâmetros do sistema contábil fica obrigatório selecionar a opção "Contabilizar por centro de Custo" na tela do processo de Contabilização de Depreciação/Correção Monetária;   
- **Usa Departamento:** Após marcar esta opção nos parâmetros do sistema contábil será exibida uma mensagem de alerta, no processo de Contabilização de Depreciação/Correção Monetária, caso a tela seja avançada sem marcar a opção "Contabilizar por Departamento".

**Procedimentos para Contabilização da Depreciação/Correção Monetária**

Antes de contabilizar a Depreciação e/ou Correção Monetária deve-se verificar a existência de evento contábil, devidamente parametrizado.   
Este evento deverá ser classificado em "Classificação de Evento Contábil"  como de Depreciação ou Correção.   
Após a classificação do evento deve-se associá-lo ao grupo de patrimônio, grupo este que será, posteriormente, associado ao patrimônio durante sua inclusão.  
Os lançamentos contábeis serão criados respeitando as informações definidas no evento contábil associado ao cenário informado no grupo de patrimônio. Desta forma é fundamental que todos os passos citados até o momento sejam respeitados a fim de que a contabilização seja realizada corretamente.  
   
Na tela de Contabilização de Depreciação/Correção Monetária deve-se selecionar, obrigatoriamente, qual o tipo de informação será contabilizado (Contabilizar Correção ou Depreciação) e quais patrimônios serão considerados (Ativos ou Inativos).  
   
Ao marca a opção **"Selecionar Filiais"** serão exibidas todas as filiais existentes para coligada em questão. Esta opção permite que sejam filtrados os valores dos patrimônios por filial contabilizando apenas as filiais informadas. Para que os valores (de depreciação e/ou correção) de todos os patrimônios existentes para a coligada sejam contabilizados deve-se manter a opção "Selecionar Filiais" desmarcada.  
   
Para que os lançamentos contábeis gerados sejam quebrados por **centro de custo,** permitindo assim uma visualização mais detalhada da contabilização, deve-se selecionar a opção **"Contabilizar por centro de custo"**.  
A opção **"Contabilizar por departamento"**, seguindo a mesma ideia citada anteriormente para o centro de custo, também criará lançamentos contábeis quebrados, porém por departamento.  
   
Para que as duas opções (Contabilizar por Centro de Custo e Departamento) citadas anteriormente tenham efeito satisfatório é necessário que os campos Centro de Custo e Departamento estejam preenchidos de acordo com a parametrização do Evento Contábil.   
Por exemplo:  
Se no campo "Buscar centro de custo em" estiver marcado o Default contábil como primeiro na ordem de prioridade, é neste local que o sistema irá buscar o centro de custo para gerar a contabilização.  
O mesmo se aplica para a opção Patrimônio - Desta forma o sistema considerará os centros de custos associados aos patrimônios.  
O mesmo se aplica para a opção Evento contábil - Desta forma o sistema considerará os centros de custos informados no Evento.  
   
Após definir quais informações serão contabilizadas e a forma como os lançamentos serão criados (separados por centro de custo e/ou departamento) deve-se informar qual Cenário de cálculo será utilizado (item obrigatório). Todos os patrimônios associados ao Cenário informado no processo serão considerados para a realização da contabilização, ou seja, o processo será executado por cenário.  
   
Além do cenário devem ser informados a descrição do lançamento contábil, o número do documento, o histórico padrão e complemento do histórico.  
Por default, a descrição do lançamento e o complemento do histórico serão preenchidos, respectivamente, pelo nome do processo (Depreciação ou Correção) e o mês/ano que esta sendo realizada a contabilização ficando estes campos livres para serem alterados.  
   
Estando todos os dados corretos o processo deverá ser executado sendo que, ao seu final será exibido um Log contendo todas as informações referentes a contabilização.

Fórmulas

A partir da versão 12.1.2410 foi disponibilizado o uso de fórmulas na contabilizações do patrimônio para permitir aos clientes a customização na geração dos valores dos lançamentos/partidas e seus respectivos rateios.

* Se o evento contábil não envolver fórmula, for por percentual, então o comportamento se manterá inalterado, será utilizado o valor do cálculo e aplicado o percentual do item do evento contábil e este será o valor da partida;

* Se o evento contábil envolver fórmula o sistema percorrerá a lista de patrimônios envolvidos no cálculo da depreciação/correção e, para cada um, chamará a fórmula acumulando/somando o resultado a cada chamada. Ao final, o valor da partida/rateio será o valor acumulado/somado.

ATENÇÃO: O valor acumulado/somado gerado pela aplicação da fórmula aos patrimônios, dependendo de como a fórmula for elaborada, pode não ser exatamente o valor da depreciação/correção calculada pelo sistema mas que isto não impedirá a geração da contabilização apenas o processo emitirá um alerta sobre tal diferença.

Maiores detalhes em particularidades de  e também consultar [Itens Evento](http://tdn.totvs.com/pages/viewpage.action?pageId=423938464) do cadastro de Eventos contábeis do módulo Contábil.

 **Calculo de Rateio Gerencial**Quando os parâmetros do evento possuem conta contábil que exigem rateio gerencial, os valores são distribuídos entre diferentes itens de acordo com as regras definidas no sistema. Este processo é feito respeitando as seguintes regras:

* **Truncamento de Valores**:

  + Todos os valores resultantes do cálculo de rateio que excedem duas casas decimais serão truncados.
  + Isso significa que, após o cálculo, apenas as duas primeiras casas decimais serão mantidas, descartando qualquer fração adicional.
* **Ajuste de Diferenças**:

  + Em casos onde a soma dos valores rateados não coincide exatamente com o valor original devido ao truncamento, será realizada uma correção automática.
  + A diferença entre o valor original e a soma dos valores rateados será adicionada ao último item de rateio.
  + Essa diferença de ajuste é pequena e não ultrapassa alguns centavos, garantindo que os valores finais sejam precisos e consistentes.
* **Exemplo Prático**:

  Clique para verificar o exemplo

  Suponha que o valor total a ser rateado seja **R$ 100,05** e ele deva ser dividido em **3** partes proporcionais com os seguintes percentuais:

  + Item 1: 33,33%
  + Item 2: 33,33%
  + Item 3: 33,34%

  **Cálculo antes do truncamento:**

  + Item 1: R$ 100,05 \* 33,33% = R$ 33,349665
  + Item 2: R$ 100,05 \* 33,33% = R$ 33,349665
  + Item 3: R$ 100,05 \* 33,34% = R$ 33,35067

  **Cálculo após o truncamento (mantendo duas casas decimais):**

  + Item 1: R$ 33,34
  + Item 2: R$ 33,34
  + Item 3: R$ 33,35

  **Soma dos valores rateados após truncamento:**

  + R$ 33,34 + R$ 33,34 + R$ 33,35 = **R$ 100,03**

  **Ajuste da diferença:**

  + A diferença entre o valor original (R$ 100,05) e a soma dos valores rateados (R$ 100,03) é de **R$ 0,02**.
  + O sistema ajusta essa diferença, adicionando os **R$ 0,02** ao último item de rateio, resultando em:

    - Item 1: R$ 33,34
    - Item 2: R$ 33,34
    - Item 3: R$ 33,37

    Total: **R$ 100,05** (valor original ajustado).

**Visualizar Contabilização de Depreciação/Correção**

Após realizar a contabilização da depreciação e/ou Correção com sucesso os lançamentos contábeis poderão ser visualizados a partir da opção Visualizar Contabilização da Depreciação/Correção. Por medida de segurança estes lançamentos não poderão ser alterados. Caso alguma informação não esteja correta deve-se excluir a contabilização utilizando o processo de Desfazer Contabilização da Depreciação/Correção Monetária.  
   
**Integração com o Totvs Gestão Contábil**

Após a verificação das informações dos lançamentos contábeis gerados pela contabilização da depreciação/correção monetária pode-se executar o processo "Integrar Contabilização". Este processo permite que os lançamentos sejam enviados para o sistema contábil em um determinado lote. Para maiores informações referentes a este processo clique aqui.

Veja Também

* Integrar Contabilização
* Exclusão de Contabilização da Depreciação/Correção Monetária
