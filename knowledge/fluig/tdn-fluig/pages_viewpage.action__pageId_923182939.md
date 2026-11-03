---
content_hash: 8a51875a59a7136e37e1b03bf10a33b378f71bc3637d099019e8ae63c137ef3c
fetched_at: '2026-06-28T21:35:31.437805+00:00'
page_id: '923182939'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Subprocesso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=923182939
version: 38
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse .

75%

3.\*ndice

25%

trueIdioma

# Falando de componente Subprocesso...

---

O componente **Subprocesso** representa um ponto do processo onde será iniciado outro processo completo, que é o subprocesso. Ou seja, esse componente representa um conjunto de atividades agrupadas – que formam um processo – dentro de um processo principal ou maior, permitindo encapsular esse conjunto de atividades dentro de um único componente para facilitar a leitura e a manutenção do diagrama do processo principal.

Com o componente Subprocesso, é possível dividir processos grandes e complexos em partes menores – subprocessos – melhorando o entendimento das etapas, pois evita que os diagramas fiquem confusos, simplificando a modelagem e o gerenciamento do processo como um todo.

Também é possível reutilizar um fluxo de trabalho em vários processos ou em vários pontos de um mesmo processo, o que garante a consistência das etapas, minimiza erros, proporciona economia de tempo de modelagem do processo e reduz o esforço de configuração de componentes.

#ebecf0

trueExemplo  
Se na sua empresa existem algumas etapas de aprovação de valores que são comuns em vários processos, você pode agrupar essas etapas em um processo de **Aprovação financeira** e reutilizá-lo a partir do componente **Subprocesso** em todos os outros processos que, em algum momento, precisam passar por essas mesmas etapas de aprovação.

Quando uma solicitação do processo principal chega na etapa do subprocesso, ela é pausada e uma nova solicitação do subprocesso é criada. Quando a solicitação do subprocesso é finalizada, a solicitação do processo principal pode ser retomada para que continue no fluxo principal até sua finalização.

Se o fluxo do processo principal permite retorno, quando a solicitação chega na etapa do subprocesso, uma nova solicitação será aberta no subprocesso e a solicitação do processo principal fica bloqueada até que a solicitação do subprocesso seja finalizada. Assim que a solicitação do subprocesso for finalizada, a solicitação do processo principal é enviada para a etapa anterior à do subprocesso, para que continue no fluxo principal até sua finalização.

Ao utilizar o componente Subprocesso, também é possível compartilhar informações entre os formulários do processo principal e do subprocesso. Mais detalhes são descritos no tópico [Envio de dados entre o processo e o subprocesso](https://tdn.totvs.com/pages/viewpage.action?pageId=923182939#Plataforma%E2%9D%99Subprocesso-Enviodedadosentreoprocessoeosubprocesso).

#ebecf0

trueExemplo de uso  
Em um processo de **Cadastro de funcionário**, quem faz o primeiro cadastro é a área de RH no sistema de gerenciamento de pessoas da empresa. Depois disso, é necessário liberar o acesso nas ferramentas internas que o funcionário vai utilizar no seu dia a dia. Porém, essa é uma atribuição da área de TI, que precisa, inclusive, da aprovação de quem será o gestor do novo funcionário para liberar os acessos. Neste caso, as etapas de execução da área de TI podem ser um subprocesso dentro do processo principal de cadastro do funcionário. O processo principal vai enviar alguns dados do funcionário – como nome, área de atuação, ferramentas que vai utilizar – para o subprocesso e o subprocesso vai devolver um *e-mail*. Depois de finalizadas as etapas de TI, o RH precisa complementar o cadastro com o *e-mail* enviado pela TI.

## Envio de dados entre o processo e o subprocesso

---

O componente Subprocesso permite que informações sejam compartilhadas entre o processo principal e o subprocesso, reduzindo a necessidade de informar os dados manualmente novamente. Para isso, é necessário que os dois processos – o principal e o subprocesso – possuam um formulário vinculado, possibilitando assim, o tráfego de informações entre os processos de forma simples e transparente.

O envio e o recebimento de informações entre os processos são definidos a partir da configuração dos campos existentes nos dois formulários, sendo possível definir quais valores devem ser compartilhados e a direção de cada um:

* **processo principal  subprocesso**: os valores serão enviados do processo principal para o subprocesso;

* **processo principal  subprocesso**: os valores serão enviados do subprocesso para o processo principal.

#ebecf0

trueExemplos de direção de valores

* Enviar valor do campo do formulário do **processo principal** (**origem**) para o campo do formulário do **subprocesso** (**destino**): **Nome**  **Nome do usuário**;

* Enviar valor do campo do formulário do **subprocesso** (**origem**) para o campo do formulário do **processo principal** (**destino**): **Nome** **Nome do usuário**;

* Enviar e receber o valor do campo do formulário do processo principal e do formulário do subprocesso (ambos **enviam** e **recebem** o valor um do outro): **Nome** **Nome do usuário**.
Importante!

Cada campo pode receber o valor de apenas um campo, ou seja, não é permitido configurar o mesmo campo para receber valor de mais de um campo.

#ebecf0

trueExemplo  
Essa configuração não é permitida:

* **Nome**  **Nome do usuário**
* **Sobrenome**  **Nome do usuário**

O campo **Nome do usuário** de um **subprocesso** não pode ser configurado para receber o valor dos campos **Nome** e **Sobrenome** do **processo**, visto que, se isso fosse permitido, o primeiro valor recebido seria sobreposto pelo segundo.

## Ver *tour* guiado do componente Subprocesso

---

**100%true5%**

**01.** No  do processo, clique no componente **Subprocesso** .

**02.** Na lateral direita, onde foram exibidas as configurações do componente, clique em  **Guia de uso** – localizado na parte inferior.

**03.** Veja a apresentação do recurso destacado.

**04.** Clique em **Próximo** para seguir para a apresentação do próximo recurso.

#f2f2f2#f2f2f2

Quando há recursos anteriores, é possível clicar em **Voltar** para revê-los.

**05.** Ao finalizar o *tour* guiado, clique em **Concluir**.

#f2f2f2#f2f2f2

Se desejar, é possível clicar em **Voltar** para rever os recursos anteriores antes de concluir.

## Configurar componente Subprocesso

---

**100%true5%**

**01.** No  do processo, clique no componente **Subprocesso**  que deseja configurar.

#f2f2f2#f2f2f2

As configurações disponíveis são exibidas na lateral direita.

**02.** Na aba **Geral**, defina as informações gerais para o componente que representa outro processo dentro do processo principal.

#f2f2f2#f2f2f2

**Título**  
Nome da etapa que representa o início de outro processo dentro do processo principal. O nome também pode ser alterado diretamente no componente, clicando sobre seu nome atual e depois em **Editar**– localizado no lado direito.

#ebecf0

trueExemplo de uso  
Em um processo de **Compra de ativos** para uma empresa, o componente poderia receber o nome **Aprovação financeira**, que são etapas de aprovação específicas da área financeira.

**Instruções para atividade**  
Instruções que visam facilitar o entendimento sobre o que acontece nessa etapa que é um subprocesso, tais como dados que serão enviados para o subprocesso ou dados que serão recebidos do subprocesso. As instruções são exibidas na aba **Informações** da solicitação.

Dica!

Ao preparar as instruções de uma etapa, é comum precisar buscar informações de outros documentos ou *sites*. A plataforma possui o conceito de *hiperlink*, que permite incluir um documento de instruções armazenado no recurso , evitando a replicação de informações e facilitando a navegação. Para isso, basta utilizar o formato **[WD:codigodoc]**, substituindo **codigodoc** pelo código numérico do documento.

**Processo**  
Processo que será incluído dentro do processo principal como um subprocesso. Qualquer processo existente na plataforma pode ser utilizado como um subprocesso dentro de outro processo. Porém, é necessário que ele possua, pelo menos, uma versão publicada.

**Transferir anexos**  
Quando ativada, determina que todos os anexos adicionados na solicitação do processo principal serão copiados para a solicitação criada no subprocesso em questão. Porém, o contrário não ocorre, ou seja, anexos adicionados na solicitação do subprocesso não são copiados para a solicitação do processo principal. Essa opção somente é habilitada quando o processo principal já possui um formulário vinculado e já foi selecionado um processo que tenha, pelo menos, uma versão publicada, no campo **Processo**.

**Cancelamento conjunto**  
Quando ativada, determina que, se a solicitação do processo principal for cancelada, a solicitação do subprocesso também será. Porém, o contrário não ocorre, ou seja, se a solicitação do subprocesso for cancelada, a solicitação do processo principal não será. Essa opção somente é habilitada quando o processo principal já possui um formulário vinculado e já foi selecionado um processo que tenha, pelo menos, uma versão publicada, no campo **Processo**.

**Movimentar atividade**  
Quando ativada, determina que assim que a solicitação chegar na etapa que é o subprocesso, ele será iniciado imediatamente, sem a necessidade de acessar a Central de tarefas para isso. Ou seja, ao enviar a solicitação principal para o subprocesso, a primeira etapa do subprocesso – ou as primeiras, caso o fluxo do subprocesso seja alternativo – será exibida para seleção e definição do responsável por ela quando o tipo de atribuição permitir. Essa opção somente é habilitada quando o processo principal já possui um formulário vinculado e já foi selecionado um processo que tenha, pelo menos, uma versão publicada, no campo **Processo**.

**03.** Clique em **Configurar campos** para definir o compartilhamento de dados entre os formulários do processo principal e do subprocesso.

#f2f2f2#f2f2f2

Essa opção somente é habilitada quando o processo principal já possui um formulário vinculado e já foi selecionado um processo que tenha, pelo menos, uma versão publicada, no campo **Processo**.

A configuração de campos permite definir quais valores devem ser compartilhados entre os formulários dos dois processos e qual a direção de cada um. É possível enviar dados do formulário do processo principal para o formulário do subprocesso e vice-versa. Mais detalhes podem ser obtidos em [Envio de dados entre o processo e o subprocesso](https://tdn.totvs.com/pages/viewpage.action?pageId=923182939#Plataforma%E2%9D%99Subprocesso-Enviodedadosentreoprocessoeosubprocesso).

**04.** Clique em **Adicionar** .

**05.** Na coluna **Campos do processo**, selecione o campo do formulário do processo principal que enviará ou receberá o valor do formulário do subprocesso – de acordo com o que for definido na coluna **Direção**.

**06.** Na coluna **Direção**, defina qual a direção do compartilhamento do valor desse campo, ou seja, se o valor do campo deve ser enviado para o subprocesso ou recebido do subprocesso.

#f2f2f2#f2f2f2

Para alterar a direção, basta clicar sobre a flecha até que a direção desejada seja exibida.

As opções de direção são:

* **Enviar o valor**: o valor contido no campo selecionado do processo principal será enviado para o campo do subprocesso selecionado na coluna **Campos do subprocesso**.

* **Receber o valor**: o campo selecionado do processo principal receberá o valor do campo do subprocesso selecionado na coluna **Campos do subprocesso**.

* **Enviar e receber o valor**: o valor contido no campo selecionado do processo principal será enviado para o campo do subprocesso selecionado na coluna **Campos do subprocesso** e, posteriormente, o campo selecionado do processo principal receberá de volta o valor contido no campo do subprocesso selecionado na coluna **Campos do subprocesso**.

**07.** Na coluna **Campos do subprocesso**, selecione o campo do formulário do subprocesso que enviará ou receberá – de acordo com o que foi definido na coluna **Direção** – o valor do campo do formulário do processo principal que foi selecionado na coluna **Campos do processo**.

**08.** Clique em **Salvar**  – localizado no lado direito.

#f2f2f2#f2f2f2

Para desistir de adicionar o envio do valor entre os campos, basta clicar em **Cancelar** – localizado no lado direito – ao invés de **Salvar** .

Na coluna ***Status*** é exibida a situação da relação de compartilhamento de valor entre os campos do formulário do processo principal e do subprocesso. Os indicativos são:

* → indica que o compartilhamento entre os campos está correto e funcional;
* → indica que há alguma inconsistência no compartilhamento entre os campos, como por exemplo, um campo foi alterado ou deixou de existir em um dos formulários.

É possível editar a relação entre os campos clicando em **Editar** – localizado no lado direito – e alterando os itens desejados. Para remover a relação entre os campos adicionada, basta clicar em **Remover**  – também localizado no lado direito.

**09.** Ao concluir a configuração de todas as relações de compartilhamento entre os campos desejadas, clique em **Salvar**.

**10.** Clique na aba **Atribuição** para ver quem será o responsável pela solicitação que será criada no subprocesso.

#f2f2f2#f2f2f2

A atribuição exibida é a que foi configurada na primeira etapa do subprocesso, ou seja, a solicitação que será aberta no subprocesso será enviada para o responsável de acordo com o tipo de atribuição definido no subprocesso.

**11.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Subprocesso**.

**12.** Na mensagem exibida, clique em **Ok, entendi**.

## Configurar envio de dados entre os processos

---

**100%true5%**

**01.** No  do processo, clique no componente **Subprocesso**  para o qual deseja configurar o compartilhamento de dados entre os formulários do processo principal e do subprocesso.

**02.** Na aba **Geral**, clique em **Configurar campos**.

#f2f2f2#f2f2f2

Essa opção somente é habilitada quando o processo principal já possui um formulário vinculado e já foi selecionado um processo que tenha, pelo menos, uma versão publicada, no campo **Processo**.

A configuração de campos permite definir quais valores devem ser compartilhados entre os formulários dos dois processos e qual a direção de cada um. É possível enviar dados do formulário do processo principal para o formulário do subprocesso e vice-versa. Mais detalhes podem ser obtidos em [Envio de dados entre o processo e o subprocesso](https://tdn.totvs.com/pages/viewpage.action?pageId=923182939#Plataforma%E2%9D%99Subprocesso-Enviodedadosentreoprocessoeosubprocesso).

**03.** Clique em **Adicionar** .

**04.** Na coluna **Campos do processo**, selecione o campo do formulário do processo principal que enviará ou receberá o valor do formulário do subprocesso – de acordo com o que for definido na coluna **Direção**.

**05.** Na coluna **Direção**, defina qual a direção do compartilhamento do valor desse campo, ou seja, se o valor do campo deve ser enviado para o subprocesso ou recebido do subprocesso.

#f2f2f2#f2f2f2

Para alterar a direção, basta clicar sobre a flecha até que a direção desejada seja exibida.

As opções de direção são:

* **Enviar o valor**: o valor contido no campo selecionado do processo principal será enviado para o campo do subprocesso selecionado na coluna **Campos do subprocesso**.

* **Receber o valor**: o campo selecionado do processo principal receberá o valor do campo do subprocesso selecionado na coluna **Campos do subprocesso**.

* **Enviar e receber o valor**: o valor contido no campo selecionado do processo principal será enviado para o campo do subprocesso selecionado na coluna **Campos do subprocesso** e, posteriormente, o campo selecionado do processo principal receberá de volta o valor contido no campo do subprocesso selecionado na coluna **Campos do subprocesso**.

**06.** Na coluna **Campos do subprocesso**, selecione o campo do formulário do subprocesso que enviará ou receberá – de acordo com o que foi definido na coluna **Direção** – o valor do campo do formulário do processo principal que foi selecionado na coluna **Campos do processo**.

**07.** Clique em **Salvar**  – localizado no lado direito.

#f2f2f2#f2f2f2

Para desistir de adicionar a relação entre os campos, basta clicar em **Cancelar** – localizado no lado direito – ao invés de **Salvar** .

Na coluna ***Status*** é exibida a situação da relação de compartilhamento de valor entre os campos do formulário do processo principal e do subprocesso. Os indicativos são:

* → indica que o compartilhamento entre os campos está correto e funcional;
* → indica que há alguma inconsistência no compartilhamento entre os campos, como por exemplo, um campo foi alterado ou deixou de existir em um dos formulários.

É possível editar a relação entre os campos clicando em **Editar** – localizado no lado direito – e alterando os itens desejados. Para remover a relação entre os campos adicionada, basta clicar em **Remover**  – também localizado no lado direito.

**08.** Ao concluir a configuração de todas as relações de compartilhamento entre os campos desejadas, clique em **Salvar**.

**09.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Subprocesso**.

**10.** Na mensagem exibida, clique em **Ok, entendi**.

### Editar envio de dados entre os processos

---

**100%true5%**

**01.** No  do processo, clique no componente **Subprocesso**  do qual deseja editar o compartilhamento de dados entre os formulários do processo principal e do subprocesso.

**02.** Na aba **Geral**, clique em **Configurar campos**.

**03.** Localize a relação de campos que deseja editar.

**04.** Clique em **Editar** – localizado no lado direito.

**05.** Altere os itens desejados.

**06.** Clique em **Salvar**  – localizado no lado direito.

**07.** Ao concluir todas as alterações desejadas, clique em **Salvar** – localizado no canto inferior direito.

**08.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Subprocesso**.

**09.** Na mensagem exibida, clique em **Ok, entendi**.

### Remover envio de dados entre os processos

---

**100%true5%**

**01.** No  do processo, clique no componente **Subprocesso**  do qual deseja remover o compartilhamento de dados entre os formulários do processo principal e do subprocesso.

**02.** Na aba **Geral**, clique em **Configurar campos**.

**03.** Localize a relação de campos que deseja remover.

**04.** Clique em **Remover** – localizado no lado direito.

**05.** Na mensagem de confirmação exibida, clique em **Confirmar** para confirmar a remoção da relação de compartilhamento entre os campos.

**06.** Ao concluir todas as remoções desejadas, clique em **Salvar** – localizado no canto inferior direito.

**07.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Subprocesso**.

**08.** Na mensagem exibida, clique em **Ok, entendi**.

## Dúvidas frequentes

---

Confira aqui algumas dúvidas frequentes sobre o componente Subprocesso.

(function() {
function toggleAreas(isExpand, $parent) {
var $items = $parent.find('.panel');
$.each($items, function(idx, el) {
var $arrow = $(el).find('span.cloakToggle').find('span');
var $content = $(el).find('span.cloak');
if (isExpand) {
$arrow.removeClass('cloakDefaultOpen').addClass('cloakDefaultClose');
$content.show();
} else {
$arrow.addClass('cloakDefaultOpen').removeClass('cloakDefaultClose');
$content.hide();
}
});
}
$(document).on('click', '#toggleAll-3', function(ev) {
ev.preventDefault();
var isExpand = $(this).data('expand');
var $parent = $(this).nextAll('.sectionColumnWrapper').first();
toggleAreas(isExpand, $parent);
$(this).data('expand', !isExpand);
});
})();
[Abrir/fechar todas as dúvidas](#)]]>#ebecf0

#### @saiba-mais-1 O componente Subprocesso pode impactar o desempenho do processo?

@saiba-mais-1

---

Em termos gerais, o uso do componente Subprocesso não impacta significativamente o desempenho ou a execução de um processo.

O que pode impactar é o uso de muitos subprocessos em um único processo, subprocessos muito complexos e com muitas atividades automáticas ou interações externas – como chamadas de API.

Portanto, o ideal é garantir que os subprocessos não sejam excessivamente sobrecarregados com atividades complexas.

#ebecf0

#### @saiba-mais-2 É possível reutilizar um subprocesso em diferentes partes do mesmo processo ou em outros processos?

@saiba-mais-2

---

Sim. O objetivo do componente Subprocesso é justamente esse: permitir que processos sejam reutilizados em vários pontos de um mesmo processo ou em vários processos diferentes, tornando a modelagem mais eficiente e evitando a duplicação de atividades que sejam comuns em diversos processos.

#ebecf0

#### @saiba-mais-3 O que acontece se um subprocesso falhar ou retornar uma reprovação?

@saiba-mais-3

---

Se nenhum caminho alternativo foi configurado, é possível que o processo principal fique travado se o subprocesso apresentar uma falha ou uma reprovação.

Por isso, é extremamente importante configurar **eventos de captura de erros** para tratar exceções dentro do subprocesso – que redirecionarão o processo para uma etapa de correção ou notificação – e **fluxos de exceção** com decisões condicionais – que redirecionarão o processo por um outro caminho ou finalizam a solicitação com uma notificação sobre a falha.

Certificar-se de que o subprocesso tenha fluxos de exceção bem definidos evitará com que o processo principal seja impactado por uma falha ou recusa.

#ebecf0

#### @saiba-mais-4 O subprocesso pode ter atribuições e responsáveis diferentes do processo principal?

@saiba-mais-4

---

Sim. O subprocesso nada mais é do que um processo que foi incluído dentro do processo principal e que possui o seu próprio conjunto de participantes – como usuários, grupos e papéis – que podem ser diferentes – ou os mesmos – do processo principal.

Isso permite que as responsabilidades sejam delegadas de acordo com o que faz sentido para o subprocesso, facilitando a distribuição de tarefas e o acompanhamento dentro de um processo mais amplo que é o processo principal.

#ebecf0

#### @saiba-mais-5 O que acontece se um campo de um dos formulários configurado para compartilhar dados for alterado ou excluído?

@saiba-mais-5

---

Um alerta informando que há inconsistência no relacionamento dos campos será exibido na coluna ***Status*** da **Configuração de campos**. Neste caso, basta ajustar o campo em questão no formulário para que o compartilhamento de dados volte a funcionar corretamente.

Fique atento!

Esta documentação é válida a partir da atualização**Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
