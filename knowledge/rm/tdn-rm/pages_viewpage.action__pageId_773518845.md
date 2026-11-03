---
content_hash: 5def9683120bedda28543042202fde518dadb33545d87882f20e9725c7af3c1c
fetched_at: '2026-06-29T00:11:36.884549+00:00'
page_id: '773518845'
product: rm
source: tdn-rm
title: TCGI - Comissão - Portal Imóveis - Visão da Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773518845
version: 21
---

### Parametrizações de ambiente para a comissão com novas funcionalidades do TCGI

#FF9000Primeiro Passo - Configurações de CORS

**[Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=804620024)** **e veja como parametrizar o Perfil de Acesso para manipular a Comissão do PI**

O arquivo **web.config** dentro da instalação do Portal de Imóveis normalmente localizado em *FrameHTML\web\app\Imb\PVI\api* deve possuir as seguintes *tags* relacionadas as operações **CORS** dentro da tag custom headers. Abaixo um exemplo deste arquivo:

php1true



























]]>#FF9000Segundo Passo - Configurações da porta ApiPort 

A porta API deve ser definida para que a comunicação entre o host e o portal de imóveis aconteça de forma transparente. Abaixo os locais onde esta porta deve estar parametrizada:

1) Arquivos *.config* do *rm.host.exe* e *rm.host.service.exe*

Para entender e configurar a tag de apiPort nos arquivos do host, [siga o procedimento clicando neste link (clique aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-)

2) Arquivo *config.json* dentro da pasta *config* em *wwwroot*:

Normalmente localizado em *C:\TOTVS\CorporeRM\RM.Net\wwwroot\config.*O parâmetro apiServer deve estar configurado com a URL do Portal de Imóveis + porta da API. Abaixo um exemplo deste arquivo:

php1true

*Onde [http://127.0.0.](http://127.0.0.1:8051)1 é a URL do portal de Imóveis e 8051 é a porta da API (ApiPort)*

3) Dentro do Portal de Imóveis deveremos definir em */backend/parametros,* aba TOTVSo parâmetro ***API REST TOTVS: URL***

Esta é a mesma URL definida no arquivo *.config* da pasta *wwwroot* como exemplificado acima.

#FF9000Terceiro Passo - Sincronização do Portal de Imóveis

Após as configurações acima, o ambiente do Portal de Imóveis deve ser sincronizado em  /backend/sincronizar, opção de Parâmetros.  
Estando a sincronização realizada, o Portal de Imóveis estará pronto para gerar as comissões.

### Nova visão de comissão no Portal de Imóveis

A nova visão da comissão no Portal de Imóveis será acessada através do menu *Corretores / Comissão ou Propostas / Comissão.*

Esta visão somente estará disponível se o parâmetro que utiliza a comissão com novas funcionalidades estiver marcado no backoffice e a sincronia tiver sido feita.

Para dar acesso ao menu, verifique o cadastro de grupo de usuário, no meu *Corretores / Comissão.*

Esta visão será uma visão agrupadora, ou seja, irá agrupar as comissões dos usuários de acordo com os parâmetros de filtro ou situação da comissão e papel do usuário no sistema.

Papeis de usuários acessando a comissão do portal de imóveis:

* Quando o usuário é um usuário que possui subordinados, este usuário terá acesso as suas comissões, bem como as comissões de seus usuários subordinados.
* Quando o usuário é um corretor, ele somente terá acesso as suas comissões, sem visualizar as comissões dos outros usuários.
* Quando o usuário é um administrador, ou seja, um analista de TI que acessa o portal de imóveis, ele terá acesso a todas as comissões cadastradas.

Campos da tela de comissão:

* Filtro de data: Possibilita uma filtragem pela data de inclusão da comissão no sistema;
* Filtro de situação: Filtra somente as situações definidas. Integradas, calculadas, em preparação e concluídas;
* Dados da comissão: Os dados da comissão no RM;
* Corretor: O corretor que participa da comissão no sistema;
* Empreendimento: O empreendimento associado a comissão;
* Data da venda: Data da venda no RM;
* Valor: Valor da comissão.
* Opções:  
  + Ver: Visualiza a comissão e sua distribuição de valores. O item da comissão do RM será exibido nesta tela;
  + Aprovar: Para fluxos de aprovação de gestores;
  + Excluir: Exclui a comissão.

**Visualização de comissionados avulsos**

---

Na comissão com novas funcionalidades, o portal de imóveis permitirá a visualização de comissionados avulsos de acordo com os comissionados avulsos informados na respectiva modalidade de comissão.

Para realizar esta ação acesse a tela de Proposta, selecione uma Proposta Em Preparação e acesse o menu de Comissão:

Na tela de *Dados de Comissão da Proposta*, para ter acesso às opções de *Visualizar* conforme as permissões aplicadas no **Perfil** do *TCGI*, para este *Usuário*;

Importante!

O botão para Adicionar Comissionado somente será habilitado na interface de Comissões da Proposta do PI, se a Modalidade de Comissão tiver uma Regra de Comissão com o Tipo Pessoa Quem Recebe configurado para **Comissionado Avulso Portal de Imóveis**.

#### **Alterando um Item de Comissão - Recurso Comissão presente na etapa Condições de Pagamento**

* Permitir editar apenas os campos
  + Percentual quem paga - permite um valor numérico maior que 0 e menor ou igual a 100;
  + Nro de parcelas - permite a edição se o usuário tiver permissão de edição;
  + % comissão - permite um valor numérico maior que 0 e menor ou igual a 100.
  + Valor comissão - permite a edição se o Cálculo da Comissão for do Tipo Valor;
  + Demais campos bloqueados;
* Restaurar Comissão

  A funcionalidade de **Restaurar Comissão** na visão de comissão da Proposta, tem o mesmo princípio do recurso já existente de **Restaurar Tabela** na etapa de **Condições de Pagamento**, permitindo que as regras padrão da modalidade selecionada sejam reaplicadas sem a necessidade de refazer etapas adicionais manualmente.

  Comportamento Anterior: Antes desta melhoria, a restauração da regra de comissão só ocorria ao utilizar o botão Restaurar Tabela na etapa de Condições de Pagamento. Esse comportamento acarretava em retrabalho para o usuário, pois ao restaurar a comissão, era necessário também refazer as condições de pagamento, mesmo quando não havia alterações desejadas nessa etapa.  
  Comportamento Atual: Com a nova funcionalidade, o usuário pode optar por restaurar apenas a regra de comissão diretamente na visão Comissão da Proposta, sem impactar as informações previamente configuradas nas Condições de Pagamento. O processo restaura os valores padrão da comissão conforme definidos pela modalidade de financiamento, abrangendo todos os componentes, percentuais e critérios aplicáveis.

* Regras de edição da tela

* + Quem Paga comissão (Está bloqueado a alteração pois a definição do híbrido está no percentual de quem paga)
  + % Quem paga -  Este campo define a proporção da comissão paga por cada parte envolvida (Cliente ou Empresa) aos comissionados definidos na [Regra](https://tdn.totvs.com/pages/viewpage.action?pageId=773517977) da comissão. A seguir, estão as regras e orientações para preenchimento e edição deste campo:
    - **Intervalo permitido:** O campo "% Quem Paga" só aceita valores numéricos **maiores que 0** e **menores ou iguais a 100**.
      * Se for digitado um valor fora desse intervalo, o sistema exibirá uma mensagem de erro e **não permitirá salvar o registro**.
    - **Edição e exclusão de registros:** A comissão paga ao corretor padrão **sempre soma 100%**, podendo ser dividida entre dois pagadores: **Empresa** e **Cliente**.
      * Caso deseje que **apenas uma parte arque com 100% da comissão** do corretor, é necessário **excluir o outro comissionado**.
      * Exemplo: se a comissão deve ser paga apenas pela empresa, exclua o registro do cliente comissionado.
      * Em cenários em que o botão de excluir a comissão do corretor não está habilitado, pode-se informar o valor de  0% no campo "% Quem Paga", da comissão paga pela empresa ou da comissão paga pelo cliente, para que o sistema (PI) recalcule automaticamente a comissão e atribua 100% da responsabilidade para a empresa, ou para o cliente.
    - **Distribuição parcial entre Empresa e Cliente nas comissões pagas ao corretor:**Ao alterar o percentual de um dos pagadores, o sistema **recalcula automaticamente** o percentual do outro, de forma que a **soma sempre permaneça em 100%**.
      * **Exemplo**: Se atualmente a empresa paga 50% e o cliente os outros 50%, e o usuário altera o percentual da empresa para 15%, o sistema ajustará automaticamente o percentual do cliente para 85%, após o salvamento desta edição.
    - **Prioridade de cálculo:**Alterações neste campo têm **prioridade sobre o valor ou percentual da comissão**.
      * Ao alterar "% Quem Paga", os campos **% Comissão** e **Valor da Comissão** serão **recalculados automaticamente** com base na nova proporção.
    - **Bloqueio temporário de campos:**Durante a edição deste campo, os campos relacionados ao valor da comissão ficam **temporariamente bloqueados**. Eles são reabilitados somente após o salvamento da alteração.

* + Pagar a Imobiliária; (Está bloqueado a alteração)
    - só pode alterar se não for imobiliária  e for quem paga empresa
      * se passar diferente será ignorado a alteração
  + Tipo de Cálculo; (Está bloqueado a alteração)
    - Se quem paga for empresa,  pode alterar conforme o tipo de cálculo para 0 e 1
      * se passar diferente será ignorado a alteração;
    - Se quem paga for cliente, pode alterar para o tipo 0, 1 e 2;
      * se passar diferente será ignorado a alteração
  + Nro de Parcelas;
  + % Comissão;
    - só pode alterar se o tipo valor for Percentual e não tiver alterado o percentual de quem paga;
      * deve ser informado um valor numérico maior que 0 e menor ou igual 100;
      * caso seja digitado um valor fora do range estipulado acima, será exibida uma mensagem de exceção ao Usuário e não será possível de se salvar o Registro (vide imagem acima).
      * Exemplo:  Corretor quem paga é 50% empresa  e 50% cliente, o tipo valor da comissão é PERCENTUAL, que tem o valor total de 2%, sendo 1% para cliente e 1% para empresa.
        + Vou alterar o percentual da comissão do corretor empresa para 2% e a parte cliente ficará com 1%, dessa forma o percentual de quem paga não é mais 50% para cada, vou recalcular a proporção de ambos que ficará com 66,6667% parte empresa e  33,3332% parte cliente%;
        + Vou criar o corretor quem paga cliente que ficará com o restante de 40%, dessa forma ficará com o resto do percentual 0,8%;
      * o mesmo raciocínio valerá para o tipo Tipo de valor quando for valor comissão;
      * Serão bloqueados os campos de percentual de quem paga a comissão e liberados após salvar os dados
        + - * **Exemplo de cálculo proporcional**
              + Tipo de comissão: **Percentual**
              + Comissão total definida: **2%**
              + Se a empresa passa de 100% para 60% como pagadora da comissão:
              + Empresa: **60% de 2% = 1,2%**
              + Cliente: **40% de 2% = 0,8%**
              + Esse mesmo raciocínio se aplica ao tipo de comissão do tipo **valor fixo**.
* + Valor Comissão.
    - Só pode alterar se o tipo valor for valor comissão e não tiver alterado o percentual de quem paga.
      * se passar diferente será ignorado a alteração
    - Serão bloqueados os campos de percentual de quem paga a comissão e liberados após salvar os dados.

* **Comissão paga na mesa:** É permitido ao ao usuário que tiver permissão a quantidade de parcela e até mesmo data vencimento e valor da parcela.

  Importante!

  Parâmetro ajuda a definir que a data inicial acompanha componente do plano de financiamento para comissões paga na mesa: **Comissão - TCGI**

#### Deletando um item de comissão

Caso seja deletado um comissionado que tem comissão paga pela empresa e pelo cliente, o valor da comissão/percentual fica para uma das duas situações.

Sendo assim, caso apague o comissionado cliente, então o valor/percentual da comissão vai para comissionado empresa e vice-versa.

Se for um comissionado comum é apagada normalmente o registro

#### Incluindo um item de comissão

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

**Segurança dos campos da edição da comissão com novas funcionalidades**

---

Para usar esse recurso, os usuários, como por exemplo o corretor, deverão ter seu cadastro sincronizado com o backoffice. Pois a segurança de edição/inserção/deleção dos registros da comissão e de seus campos serão feitos no **[perfil](https://tdn.totvs.com/pages/viewpage.action?pageId=804620024)**de segurança de Globais.

IMPORTANTE!

O CPF desse Usuário de Acesso (FCFO.CODUSUARIOACESSO) deve ser igual, no cadastro de *Usuários (USUARIO.CPFCNPJ) d*o *Portal de Imóveis (PI)* e no cadastro de *Clientes/Fornecedor* (FCFO.CGCCFO) do RM.

Com o uso da nova Comissão, a ferramenta de **[Manutenção de Usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=435105178)** permite que os usuários de acesso ao RM para os Corretores do Portal de Imóveis sejam criados automaticamente com base em um perfil de acesso predefinido.

Os corretores poderão ter um perfil que não permita editar a comissão, já os supervisores poderão ter um perfil que permita a edição. Nessa controle será possível tirar a permissão dos corretores de editar o número de parcelas a serem pagas ou até mesmo o valor.  Através da aba acesso a campos, procurando a tabela XCOMISSCOESITEM, retirando a permissão de alterar esses campos ou até mesmo de visualizar.

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
