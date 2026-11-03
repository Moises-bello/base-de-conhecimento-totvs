---
content_hash: 7663449eb536222b73deaa3d847a5c380333d239ac2db6a2e2f27a24e187abae
fetched_at: '2026-06-29T00:12:01.601065+00:00'
page_id: '896373639'
product: rm
source: tdn-rm
title: PI - Proposta - Condições de Pagamento - Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=896373639
version: 12
---

---

O usuário que possui permissão para acessar esta opção poderá adicionar um novo comissionado de acordo com as regras cadastradas na modalidade de comissão, assegurando que todos os critérios específicos, como **tipo de comissão**, **valores** e **condições**, sejam seguidos.   
Para certificar que o usuário possui suas devidas permissões, clique aqui: ***[Permissões de acesso em Perfil de usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=1001616047)***  
  
Além disso, o usuário poderá alterar os percentuais de comissão nos casos em que a modalidade de comissão for híbrida, permitindo ajustes conforme a performance, metas atingidas ou negociações específicas.

O sistema garantirá que todas as alterações sejam feitas dentro dos parâmetros definidos na configuração do plano de comissão, mantendo a integridade das regras estabelecidas.   
  
É importante que o usuário verifique a consistência das informações antes de realizar qualquer alteração para evitar divergências nos cálculos de comissões.

Na lista de comissionados, ao clicar em '...' e selecionar a opção de **editar**, será exibida a tela com os parâmetros da comissão, onde estarão todas as informações relacionadas àquela linha de comissão gerada na proposta.

#### Editando um Item de Comissão

* **Permitir editar apenas os campos**
  + Percentual quem paga - permite um valor numérico maior que 0 e menor ou igual a 100;
  + Nro de parcelas - permite a edição apenas se ***Quem Paga*** for Empresa. Caso ***Quem Paga*** for Cliente a partir da 12.1.2506 será permitido a edição desde que o perfil do usuário tenha permissão de edição no Acesso a Campos na tabela XCOMISSAOITEM - NROPARCELAS com a permissão Pode Alterar, será possível ainda a alteração do campo Data Vencimento e Valor da parcela desde que a soma das parcelas seja exatamente igual ao Valor Total da comissão;
  + % comissão - permite um valor numérico maior que 0 e menor ou igual a 100.
  + Valor comissão - permite a edição se o Cálculo da Comissão for do Tipo Valor;
  + Demais campos bloqueados;

* **Regras de edição da tela**

* + Possibilidade de Alterar o cliente/fornecedor que receberá as comissões nas propostas, isto eliminará a obrigatoriedade de cadastrar os corretores no PI e definir modalidades de comissão específicas para cada cenário conforme as personas envolvidas. Com essa atualização, os administradores podem ajustar livremente o cli/for que receberá a comissão.
  + Quem Paga comissão (Está bloqueado a alteração pois a definição do híbrido está no percentual de quem paga)
  + % Quem paga -
    - Só pode alterar para um valor numérico maior que 0 e menor ou igual 100;
    - caso seja digitado um valor fora do range estipulado acima, será exibida uma mensagem de exceção ao Usuário e não será possível de se salvar o Registro.

* + - Se deseja zerar o percentual para excluir um dos comissionados quem paga cliente ou empresa deve excluir o registro para o sistema manter apenas um deles e recalcular o percentual de quem paga.
    - se estou alterando o comissionado para 100% quem paga a comissão, exemplo Empresa, e existe o seu par, cliente,  
      então essa ação deve ser feita deletando o cliente comissionado, pois os seus valores não existe mais, ficando zerados
    - Caso o percentual esteja 100 e seja reduzido, então deve-se criar o comissionado parte empresa ou parte cliente com a diferença;
    - Se alterar esse campo, sempre terá prioridade em relação a alteração do valor da comissão ou do percentual, vai depender do tipo de valor da comissão;
    - Serão bloqueados os campos de valores da comissão e liberados após salvar os dados
    - Alterando esse campo, ele interfere diretamente nos valores de %Comissão ou Valor da Comissão, pois mudando o percentual de quem paga vou alterar esses campos campos com  base na nova proporção de de quem paga.
      * Exemplo: Corretor quem paga é 100% empresa e o tipo valor da comissão é PERCENTUAL, que tem o valor de 2%.
        + Vou alterar o percentual de quem paga empresa para 60%, dessa forma o percentual da comissão ficara 60% de 2% = 1,2%;
        + Vou criar o corretor quem paga cliente que ficará com o restante de 40%, dessa forma ficará com o resto do percentual 0,8%;
      * O mesmo raciocínio valerá para o tipo Tipo de valor quando for valor comissão;
  + **Pagar a Imobiliária; (Está bloqueado a alteração)**
    - só pode alterar se não for imobiliária  e for quem paga empresa
      * se passar diferente será ignorado a alteração
  + **Tipo de Cálculo; (Está bloqueado a alteração)**
    - Se quem paga for empresa,  pode alterar conforme o tipo de cálculo para 0 e 1
      * se passar diferente será ignorado a alteração;
    - Se quem paga for cliente, pode alterar para o tipo 0, 1 e 2;
      * se passar diferente será ignorado a alteração
  + **Nro de Parcelas;**
    - Pode alterar se quem paga for empresa ou cliente;
      * se passar diferente será ignorado a alteração
  + **% Comissão**;
    - só pode alterar se o tipo valor for Percentual e não tiver alterado o percentual de quem paga;
      * deve ser informado um valor numérico maior que 0 e menor ou igual 100;
      * caso seja digitado um valor fora do range estipulado acima, será exibida uma mensagem de exceção ao Usuário e não será possível de se salvar o Registro (vide imagem acima).
      * Exemplo:  Corretor quem paga é 50% empresa  e 50% cliente, o tipo valor da comissão é PERCENTUAL, que tem o valor total de 2%, sendo 1% para cliente e 1% para empresa.
        + Vou alterar o percentual da comissão do corretor empresa para 2% e a parte cliente ficará com 1%, dessa forma o percentual de quem paga não é mais 50% para cada, vou recalcular a proporção de ambos que ficará com 66,6667% parte empresa e  33,3332% parte cliente%;
        + Vou criar o corretor quem paga cliente que ficará com o restante de 40%, dessa forma ficará com o resto do percentual 0,8%;
      * o mesmo raciocínio valerá para o tipo Tipo de valor quando for valor comissão;
      * Serão bloqueados os campos de percentual de quem paga a comissão e liberados após salvar os dados
  + **Valor Comissão.**
    - Só pode alterar se o tipo valor for valor comissão e não tiver alterado o percentual de quem paga.
      * se passar diferente será ignorado a alteração
    - Serão bloqueados os campos de percentual de quem paga a comissão e liberados após salvar os dados.

#### **Deletando um item de comissão**

Caso seja deletado um comissionado que tem comissão paga pela empresa e pelo cliente, o valor da comissão/percentual fica para uma das duas situações.

Sendo assim, caso apague o comissionado cliente, então o valor/percentual da comissão vai para comissionado empresa e vice-versa.

Se for um comissionado comum é apagada normalmente o registro

#### **Incluindo um item de comissão**

Caso seja incluindo um comissionado que tem comissão paga pela empresa com percentual menor que 100%, então será criado o comissionado cliente com o a diferença desse percentual e calculando a nova proporção do percentual da comissão em cima dessa proporção de cliente e empresa.

Se for criado um comissionado com regra quem paga 100%, regra padrão, então cria apenas o próprio registro.

* permitir editar/inserir apenas os campos
  + Regra do comissionado avulso;
  + Função;
  + Nome do comissionado;
  + percentual quem paga;
  + Nro de parcelas (liberar a edição se for empresa, cliente sempre bloqueado);
  + % comissão, permitir a edição se o tipo de valor for percentual
  + valor comissão , permitir a edição se o tipo de valor for valor;
  + Demais campos bloqueados;

**Comportamento do Portal de Imóveis ao salvar proposta na comissão com novas funcionalidades**

---

O Portal de Imóveis, quando utilizar a comissão com novas funcionalidades, terá um comportamento de salvar a proposta no backoffice antes da mesma tornar-se uma venda. Isto deve-se ao fato de que, todo o cálculo da comissão será realizado pelo RM. Desta forma, o corretor ao salvar a proposta, irá enviar o registro de venda com status "Proposta" e terá a sua comissão já gerada no RM.

Este registro ainda poderá sofrer alterações e possui somente valores básicos, como a informação da unidade e seu preço de venda no momento em que a proposta foi gerada.

Ao enviar o contrato para o backoffice, através do fluxo normal do Portal, este registro terá seu status alterado de "Proposta" para "Vendido". e todas as informações serão atualizadas neste registro.

**Calculo da comissão de proposta salva**

---

Existem algumas premissas para que a comissão seja salva automaticamente no backoffice quando a proposta for salva no Portal de Imóveis.

Deveremos primeiro criar uma modalidade e essa modalidade deve possuir suas regras, bem como seus imóveis parametrizados. Para entender melhor como cadastrar uma modalidade, verificar nesta mesma página a sessão de modalidades da comissão.

Para quaisquer outros tipos de comissionados, por exemplo, **gerentes**, **diretores**, ou **superiores**, a modalidade deverá possuir uma regra que envolva o tipo "Outro Comissionado" e esta pessoa deverá ser cadastrada diretamente na modalidade em questão.

Estando estes pré requisitos aceitos, o Portal de imóveis irá informar, quando salvarmos a proposta, que a comissão foi gerada automaticamente no RM. Para consultar a comissão, basta utilizar o menu como orientado acima.

Quaisquer mudanças que ocorram no RM, como alteração de usuários, valores, percentuais serão refletidas no Portal de Imóveis.

Quando há a alteração de valores de uma proposta, por exemplo, uma alteração de valor ou um desconto que influencie no cálculo de valores da comissão, o portal de imóveis irá recalcular a comissão quando a proposta for salva com os novos valores.

**Restaurar comissão**

---

A funcionalidade de **Restaurar Comissão** na visão de comissão da Proposta, tem o mesmo princípio do recurso já existente de **Restaurar Tabela** na etapa de **Condições de Pagamento**, permitindo que as regras padrão da modalidade selecionada sejam reaplicadas sem a necessidade de refazer etapas adicionais manualmente.

Comportamento Anterior: Antes desta melhoria, a restauração da regra de comissão só ocorria ao utilizar o botão Restaurar Tabela na etapa de Condições de Pagamento. Esse comportamento acarretava em retrabalho para o usuário, pois ao restaurar a comissão, era necessário também refazer as condições de pagamento, mesmo quando não havia alterações desejadas nessa etapa.  
Comportamento Atual: Com a nova funcionalidade, o usuário pode optar por restaurar apenas a regra de comissão diretamente na visão Comissão da Proposta, sem impactar as informações previamente configuradas nas Condições de Pagamento. O processo restaura os valores padrão da comissão conforme definidos pela modalidade de financiamento, abrangendo todos os componentes, percentuais e critérios aplicáveis.

**Exclusão da comissão**

---

Existem etapas onde, o backoffice irá excluir automaticamente uma comissão gerada

No cenário onde o tempo de reserva da proposta é derrubado, o backoffice irá excluir automaticamente as comissões geradas através desta proposta. Ou seja, quando o status da minha proposta equivale a "Proposta Cancelada" toda comissão será excluída do backoffice.

Há também momentos onde a comissão tem a sua etapa alterada manualmente pelo próprio corretor ou gerente para "Proposta Cancelada". Nestes casos a comissão no backoffice também será excluída.

Se caso esta mesma proposta tenha seu status alterado para algum diferente de "Proposta Cancelada", a comissão será refeita no backoffice, no momento da alteração de etapa.  
  
**Desfazendo venda no backoffice**

---

Tendo em vista a utilização da comissão com novas funcionalidades, o portal de imóveis passa a salvar as propostas também no backoffice após a sua criação no portal, alteramos o processo de Excluir Venda no Backoffice, que passa a se chamar "Desfazer Venda no Backoffice".

A única diferença neste processo é que não iremos mais excluir a venda mas sim, alterar o status da mesma de "Vendida" para "Proposta". Alterando também o status da subunidade que passará de vendida para o status definido no Portal de Imóveis na Etapa ao qual a proposta irá voltar.

**Editando o Parcelamento da Comissão**

---

Para realizar o ajuste no parcelamento de uma negociação "na mesa", o usuário deve acessar a visão de comissão da proposta.

* **Acesso à Edição**: Na lista de comissionados, deve-se clicar no ícone de opções **"..."** e selecionar a opção **"Editar"**.
* **Interface de Edição**: Será exibida a modal **"Comissionado"**, contendo os parâmetros da comissão e a nova visão em grid para detalhamento das parcelas.

---

**1. Alteração do Número de Parcelas**

O campo **"Parcelas"** permite definir a quantidade de divisões da comissão para fins de averiguação da negociação.

* **Regra de Edição**: O campo permite a edição caso o parâmetro de parcelamento de comissão esteja habilitado no RM.
* **Comportamento Dinâmico**: Ao informar um valor numérico (ex: 3), o sistema gera automaticamente a grid **"Parcelas da Comissão"** com o número correspondente de linhas.
* **Distribuição Automática**: Inicialmente, o sistema realiza a divisão igualitária do valor total da comissão entre o número de parcelas informado

---

**2. Edição de Datas de Vencimento**

A grid de parcelas permite o ajuste manual das datas acordadas na negociação.

* **Campo Data Vencimento**: Cada linha da grid possui um campo de data.
* **Flexibilidade Cronológica**: O sistema permite a inserção de datas conforme a negociação, não bloqueando o salvamento caso a **Parcela 1** possua data posterior à **Parcela 2**.
* **Persistência**: Após clicar em **"Enviar Parcelas"**, as datas informadas são registradas como parte da memória da negociação.

---

**3. Edição de Valores das Parcelas**

O usuário pode ajustar individualmente o quanto será pago em cada parcela da grid.

* **Campo Valor Parcela**: Permite a edição manual do valor monetário atribuído a cada vencimento.
* **Saldo a Distribuir**: O campo informativo **"Saldo a Distribuir"** é atualizado em tempo real conforme as alterações na grid.
* **Validação de Consistência**:

  + O sistema apresenta um ícone de alerta (laranja) mostrando que a parcela está em preparação.
  + Se a soma das parcelas for superior ao valor base da comissão, o saldo será exibido como negativo.
* **Regra de Salvamento**: É fundamental que o usuário verifique a consistência das informações antes de salvar para evitar divergências, sendo que o saldo final deve ser zero para a confirmação correta da distribuição.

---

**Regras Gerais de Edição da Tela**

* **Bloqueio de Campos**: Campos como **"Situação"** e **"Valor Total"** permanecem bloqueados para edição direta, sendo derivados do cálculo do RM.
* **Mensagens de Sucesso**: Ao concluir a edição com sucesso, o portal exibirá a notificação: **"Comissionado editado com sucesso!"**.
* **Reset de Valores**: Caso o envio ocorra com valores inconsistentes, o sistema poderá restaurar os valores padrões da modalidade.
