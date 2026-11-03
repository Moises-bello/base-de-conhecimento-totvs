---
content_hash: c380a54201d031ec937c5d615a04d2bfd107bdb79f09e725376fe05c0a35f91f
fetched_at: '2026-06-28T21:35:29.248363+00:00'
page_id: '744485418'
product: fluig
source: tdn-fluig
title: Flows - Materiais
type: documentation
url: https://tdn.totvs.com/display/fluig/Flows+-+Materiais
version: 14
---

# **Flows Essentials**

## Tecnologia da Informação

### Abertura de Chamado

**O que esse Flow faz:** Permite que o colaborador abra um chamado junto ao departamento de T.I, informando qual suporte necessita, direcionando para a  tratativa da equipe correta.

**O que esse Flow não faz:** Não está integrado ao ERP ou outro tipo de sistema de abertura de chamados.

**Parametrizações:**

* Cadastro de Tipos de Ocorrência;
* Parametrização de atribuição de responsável por atividade;
* Personalização de SLA por atividade;
* Definição de gestor do processo.

**Requisitos:**

* Fluig instalado e parametrizado a partir da versão 1.7.1;
* Utilização de processo padrão.

**Restrições:**

* Não permite integrações com outros sistemas;
* Não é customizável.

**Processo:**

 

**Descrição do Processo:**

1. Atividade **Início:** Solicitante abre o processo, preenche as informações necessárias e envia;
2. Atividade **Analisar a Solicitação:**
   1. Atribuição:
      1. Se estiver configurada, será enviada para o responsável;
      2. Se não estiver configurada, o usuário precisará escolher um responsável dentre os usuários cadastrados na plataforma.
   2. Prazo de Expiração - tempo em horas para execução da atividade até que seja considerada em atraso:
      1. Se estiver configurado, o tempo será calculado levando em conta o expediente padrão cadastrado na plataforma e o momento em que o responsável recebeu ou assumiu a atividade;
      2. Se não estiver configurado, a tarefa ficará com status "sem prazo definido".
   3. Prazo de Aviso - tempo em horas para o responsável ser avisado antes do prazo de expiração.
      1. Se estiver configurado, no tempo determinado o responsável será notificado sobre a expiração da atividade;
      2. Se não estiver configurado, não acontecerá nenhum tipo de notificação.
3. Atividade **Analisar a Solicitação**: Responsável entende a demanda e pode tomar as seguintes ações:
   1. Consegue resolver?

      1. **Sim** - envia para **4. Analisar Serviço**, de forma que o requisitante possa validar a solução dada;
      2. **Não** - Abrem duas opções:

         1. **A atual solicitação possui inconsistências que impedem sua movimentação**: nesse caso, a solicitação será **finalizada;**
         2. **A atual solicitação carece de informações, o que limita o entendimento da real necessidade do usuário**: nesse caso a solicitação será enviada para a atividade **"Solicitar informações ao usuário"** em que a atribuição deve ser automática e devolvida a quem requisitou o serviço pedindo mais informações;
4. Atividade **Analisar Serviço**
   1. O responsável deverá preencher com a informação se a situação foi resolvida, suas opções são **sim** ou **não.** Caso **tenha sido resolvida**, o processo **finaliza**.Caso contrário, retorna ao técnico responsável para ajuste da solução;
5. Atividade **Solicitar informações ao usuário**
   1. O solicitante precisará colocar informações adicionais para poder complementar o entendimento acerca de sua demanda. Esse complemento poderá ser com informações adicionais em texto ou anexo de documentos e imagens, conforme o que for mais interessante para ilustrar a situação enfrentada;
   2. Após terminar de complementar as informações, o responsável envia a atividade que deverá passar por uma nova análise (atividade 4), reiniciando o fluxo.
6. Atividade **Fim do processo**.

**Formulário:**

**Detalhamento dos Campos:**

Dados Gerais

**Usuário de abertura:** usuário que estiver identificado na plataforma ao abrir a solicitação. *Carregado automaticamente.*

**Data:** data de abertura da solicitação. *Carregado automaticamente.*

**Usuário Solicitante:**usuário que solicitou o atendimento, mas por qualquer motivo precisa que outra pessoa abra a solicitação. Permite a escolha entre todos os usuários ativos cadastrados na plataforma. Mesmo que esteja definido nesse campo, todas as interações e notificações do processo acontecerão diretamente para o usuário de abertura.

**E-mail Solicitante:** carregado automaticamente a partir do cadastro do usuário solicitante.

**Gestor:** O gestor do usuário ou do solicitante pode ser informado nesse campo. A consulta abre todos os usuários ativos cadastrados na plataforma.

**E-mail do gestor:** carregado automaticamente a partir do cadastro do usuário solicitante.

**Estabelecimento/Filial:** Campo descritivo e não obrigatório. Permite informar o estabelecimento ou a filial a que o usuário pertence, se houver.

**Complemento:** Campo descritivo e não obrigatório. Permite dar informações adicionais sobre como encontrar o solicitante, no caso de atendimento presencial.

Dados Técnicos

**Tipo da Ocorrência:** Campo obrigatório. Permite consultar a tabela de tipos de ocorrência, cadastradas no momento da instalação/edição do Flow. Pode auxiliar na classificação da solicitação no time de suporte e na transferência para as pessoas competentes.

**Título da Ocorrência:** Campo obrigatório e descritivo. Deve ser utilizado para descrever de forma sintética a ocorrência.

**Descreva detalhadamente a situação:** Campo obrigatório e descritivo. Deve ser utilizado para colocar os detalhes da ocorrência, de forma a auxiliar o time de suporte a resolver o problema reportado.

Análise da TI

**Analista Técnico:** usuário que estiver identificado na plataforma ao assumir a atividade ou ao recebê-la. *Carregado automaticamente.*

**Data:** data de análise da solicitação. *Carregado automaticamente.*

**Consegue resolver? Sim/Não:**

* Sim, analista técnico deve escrever as considerações e a solicitação será enviada para a avaliação do serviço.
* Não - Escolher entre duas opções adicionais:
  + A atual solicitação possui inconsistência que impedem a sua movimentação: escolhendo essa opção a solicitação será **finalizada**.
  + A atual solicitação carece de informações, o que limita o entendimento da real necessidade do usuário: escolhendo essa opção a solicitação será devolvida ao usuário requisitante para complementar as informações que faltam.

**Considerações Técnicas:**

Validação da Solução

**Usuário Validador:**usuário requisitante que abriu a solicitação. *Carregado automaticamente.*

**Data:** data de abertura da solicitação. *Carregado automaticamente.*

**Situação Resolvida? Sim / Não:** Se resolvida, a solicitação será finalizada. Se não resolvida, será devolvida ao analista técnico que atuou em sua solução.

**Nível Satisfação (Estrelas):** Satisfação com a solução, de 1 a 5 estrelas.

**Considerações:** Campo obrigatório e descritivo para informar o que achou do serviço prestado.

## Suprimentos

### Solicitação de Compras

**O que esse Flow faz:**Permite abertura de solicitação de compras automatizada, informando qual item será comprado e direcionando para as aprovações corretas.

**O que esse Flow não faz:** Não está integrado ao ERP ou qualquer outro tipo de sistema de compras.

**Parametrizações:**

* Cadastro de Itens (Produtos e Serviços);
* Cadastro de Centros de Custos;
* Parametrização de atribuição de responsável por atividade;
* Personalização de SLA por atividade;
* Definição de gestor do processo.

**Instalador:**

O instalador é responsável pela parametrização e edição do flow de solicitação de compras. As suas telas permitem que sejam escolhidas as formas de atribuição das atividades, o tempo padrão de atendimento e sejam feitos os cadastros necessários para funcionamento do processo. O instalador é feito em 4 etapas: Geral, Responsáveis, Itens e Revisão.

**Etapa Geral**

**Código Identificador do Processo:** Campo vem preenchido com o código do processo e não pode ser alterado.

**Título do Processo:** Título para o processo, será exibido na tela de processos para abertura de solicitações.

**Instruções:** Instruções para uso desse flow.

**Categoria:** Categoria é utilizada para facilitar o a aglutinação de processos com objetivos semelhantes ou dentro de uma mesma área de atuação.

**Quem será o gestor do processo:** O gestor do processo tem o poder de representar qualquer um dos demais usuários envolvidos no fluxo. Ele pode ser escolhido definido escolhendo um usuário específico cadastrado na plataforma, através de um papel ou de um grupo. Maiores detalhamentos sobre atribuições para gestor de processo podem ser consultadas [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=263784090).

**Responsáveis**

**Solicitante**

**Quem poderá abrir uma solicitação:**Define quem serão os usuários da plataforma que poderão abrir solicitações para esse processo. As opções são:

* Qualquer pessoa;
* Um usuário específico - sendo mandatório especificar quem seria esse usuário;
* Um papel específico - sendo mandatório escolher um papel e todos os usuários que possuírem esse papel poderão abrir uma solicitação;
* Um grupo específico - sendo mandatório escolher um grupo e todos os usuários associados a esse grupo poderão abrir uma solicitação.

**Prazo de Expiração (em horas):**Definição do prazo que a atividade de aprovação por centro de custos tem para ser executada. Não se trata de um campo obrigatório, mas se for configurado o responsável terá essa atividade em atraso se não finalizá-la dentro do prazo determinado. Essa informação irá constar no processo e nos indicadores da plataforma (detalhes sobre [fluig analytics aqui](https://tdn.totvs.com/display/public/fluig/Analytics)).

**Prazo de Aviso (em horas):** Definição do prazo para notificar ao responsável antes que a demanda atrase.

**Compras**

**Quem será o responsável pela atividade "Compras - Analisar a solicitação"? -**Atribuição de responsável pela atividade de "Analisar a solicitação", pode ser feita dentro das seguintes opções:

* **Qualquer pessoa:** qualquer usuário cadastrado na plataforma poderá ser escolhido para analisar a solicitação;
* **Um usuário específico:** o usuário escolhido receberá essa atividade como responsável;
* **Todos de um papel específico:** todos os usuários de um papel específico poderão assumir a atividade e serão notificados quando o fluxo for movimentado;
* **Todos de um grupo específico:** todos os usuários de um grupo específico poderão assumir a atividade e serão notificados quando o fluxo for movimentado;
* **Um usuário de um papel específico:** todos os usuários associados a um papel serão apresentados no momento da movimentação da atividade para que um seja escolhido para assumir a próxima tarefa;
* **Um usuário de um grupo específico:** todos os usuários associados de um grupo serão apresentados no momento da movimentação da atividade para que um seja escolhido para assumir a próxima tarefa.

**Prazo de Expiração (em horas):**Definição do prazo que a atividade de análise da solicitação tem para ser executada. Não se trata de um campo obrigatório, mas se for configurado o responsável terá essa atividade em atraso se não finalizá-la dentro do prazo determinado. Essa informação irá constar no processo e nos indicadores da plataforma (detalhes sobre [fluig analytics aqui](https://tdn.totvs.com/display/public/fluig/Analytics)).

**Prazo de Aviso (em horas):** Definição do prazo para notificar ao responsável antes que a demanda atrase.

**Quem será o responsável pela atividade "Compras - Realizar compra"? -**Atribuição de responsável pela atividade de "Realizar compra", pode ser feita dentro das seguintes opções:

* **Qualquer pessoa:** qualquer usuário cadastrado na plataforma poderá ser escolhido para analisar a solicitação;
* **Um usuário específico:** o usuário escolhido receberá essa atividade como responsável;
* **Todos de um papel específico:** todos os usuários de um papel específico poderão assumir a atividade e serão notificados quando o fluxo for movimentado;
* **Todos de um grupo específico:** todos os usuários de um grupo específico poderão assumir a atividade e serão notificados quando o fluxo for movimentado;
* **Um usuário de um papel específico:** todos os usuários associados a um papel serão apresentados no momento da movimentação da atividade para que um seja escolhido para assumir a próxima tarefa;
* **Um usuário de um grupo específico:** todos os usuários associados de um grupo serão apresentados no momento da movimentação da atividade para que um seja escolhido para assumir a próxima tarefa.

**Prazo de Expiração (em horas):**Definição do prazo que a atividade de realização da compra tem para ser executada. Não se trata de um campo obrigatório, mas se for configurado o responsável terá essa atividade em atraso se não finalizá-la dentro do prazo determinado. Essa informação irá constar no processo e nos indicadores da plataforma (detalhes sobre [fluig analytics aqui](https://tdn.totvs.com/display/public/fluig/Analytics)).

**Prazo de Aviso (em horas):** Definição do prazo para notificar ao responsável antes que a demanda atrase.

**Itens**

Cadastro de centros de custo disponíveis para que os funcionários escolham durante a inclusão da solicitação de compras, contemplando os seguintes campos:

**Código:**código do centro de custo.

**Nome do centro de custo:** descrição do centro de custo.

**Gestor do centro de custo:** nome do gestor responsável pelo centro de custo escolhido.

Cadastro de centros de custo disponíveis para que os funcionários escolham durante a inclusão da solicitação de compras, contemplando os seguintes campos:

**Item:** descrição do produto ou serviço disponível para ser comprado.

**Unidade de Medida:** referente a como esse item poderá ser medido para compra, contagem, cálculo e verificação na entrega. Exemplo: unidade, peças, quilo, caixa, litro, etc.

**Requisitos de Uso:**

* Fluig instalado e parametrizado a partir da versão 1.7.1;
* Utilização de processo padrão.

**Restrições:**

* Não permite integrações com outros sistemas;
* Não é customizável.

**Processo:**

**Descrição do Processo:**

1. Atividade **Início:** Solicitante abre o processo, preenche as informações necessárias e envia;
2. Atividade **Possui Centro de Custos:**
   1. Se sim, encaminha para aprovação do gestor cadastrado no centro de custos;
   2. Se não, encaminha para a atividade **3. Compras - Analisar a solicitação.**
3. Atividade **Compras - Analisar a Solicitação**:
   1. Responsável deverá verificar se os itens escolhidos, centro de custos e demais informações estão corretas e de acordo com a política da empresa;
   2. Caso todas as informações estejam corretas, aprova e envia para a tarefa de **4. Realizar compra;**
   3. Caso as informações não estejam corretas, o responsável coloca uma observação e finaliza a solicitação.
4. Atividade: **Realizar compra**:
   1. Responsável realiza a compra e coloca informações que considera relevante. Essa atividade não visa informar detalhes da compra executada, mas permitir aos solicitantes e gestores o acompanhamento referente ao atendimento da solicitação aberta.
   2. Após finalizar a atividade, o responsável envia para a próxima fase **5. Receber e Validar Produto/Serviço.**
5. Atividade: **Receber e Validar Produto/Serviço:**
   1. O solicitante é responsável por validar o produto ou serviço que foi comprado, verificando se as necessidades iniciais foram atendidas e se o que foi entregue tem boa qualidade;
   2. Caso considere que a solicitação foi bem atendida, o processo finaliza;
   3. Se entender que a entrega não está acordo, movimenta para a tarefa de **6. Verificar problema.**
6. Atividade: **Verificar Problema:**
   1. Responsável pela compra recebe o retorno do Solicitante e verifica qual é o problema, informando as providências tomadas;
   2. Ao concluir, envia a **5. Receber e Validar Produto/Serviço.**
7. Atividade: **Fim.**

**Formulário:**

**Detalhamento dos Campos:**

Dados Gerais

**Usuário de abertura:** usuário que estiver identificado na plataforma ao abrir a solicitação. *Carregado automaticamente.*

**Data:** data de abertura da solicitação. *Carregado automaticamente.*

**Usuário Solicitante:**usuário que solicitou o atendimento, mas por qualquer motivo precisa que outra pessoa abra a solicitação. Permite a escolha entre todos os usuários ativos cadastrados na plataforma. Mesmo que esteja definido nesse campo, todas as interações e notificações do processo acontecerão diretamente para o usuário de abertura.

**E-mail Solicitante:** carregado automaticamente a partir do cadastro do usuário solicitante.

**Estabelecimento/Filial:** Campo descritivo e não obrigatório. Permite informar o estabelecimento ou a filial a que o usuário pertence, se houver.

**Centro de Custo:** descrição de item para compra e/ou contratação.

**Gestor:** O gestor do usuário ou do solicitante pode ser informado nesse campo. A consulta abre todos os usuários ativos cadastrados na plataforma.

**E-mail do gestor:** carregado automaticamente a partir do cadastro do usuário solicitante.

**Endereço do Solicitante:** Endereço do solicitante. Campo livre para digitação.

**Complemento:** Campo descritivo e não obrigatório. Permite dar informações adicionais sobre como encontrar o solicitante, no caso da entrega dos itens ou prestação de serviços.

Itens

**Item de Compra:**descrição de item para compra e/ou contratação.

**Quantidade:**quantidade necessária, referente ao item da compra.

**Unidade de Medida:** referente a como esse item poderá ser medido para contagem, cálculo e verificação na entrega. Exemplo: unidade, peças, quilo, caixa, litro, etc.

Justificativa

**Qual o motivo da compra:**definir quais motivações aconteceram para que esse item seja solicitado, de forma a conseguir mais facilmente uma autorização superior.

Validação do centro de custo

**Gestor aprovador do centro de custo:**gestor definido que deverá aprovar ou reprovar a solicitação de compras.

**Data:**data em que a aprovação de solicitação de compras aconteceu.

**Aprovar / Reprovar solicitação de compra:** definição do gestor se a solicitação será aprovada ou reprovada.

**Justificativa:** texto explicativo sobre aprovação ou reprovação.

Analisar solicitação

**Usuário responsável pela compra:** usuário responsável por analisar a compra.

**Data:** data da análise da compra.

**Considerações:** observações feitas pelo responsável.

Considerações de compras

**Usuário responsável pela compra:** usuário responsável por comprar.

**Data:** data da execução da atividade da compra.

**Considerações:** observações feitas pelo responsável.

Validação de itens

**Solicitante:** usuário que abriu a solicitação.

**Data:** data da execução da atividade da validação.

**Avaliação da compra:** Não houve problema / Pedido não entregue / Entregue com inconsistência (qualidade, quantidade, embalagem, etc.)

**Justificativa:** observações a validação feita.

Validar problema: considerações de compras

**Quais as suas considerações:** observações feitas sobre providências ou explicações a respeito do ocorrido.

### Solicitação de Cotação

### Solicitação de Equipamentos

### Inclusão de Contratos

### Lançamento de Documento

**O que esse Flow faz:** Este fluxo permite o lançamento dos dados referentes a um documento, seja uma nota, recibo, boleto ou outro que a empresa possua, com a obrigatoriedade de anexar o documento citado.

**O que esse Flow não faz:**

* Não envia o documento ou as informações do documento para o ERP;
* Não efetua controle ou geração de pagamentos.

**Parametrizações:**

* Criação de tipos de documentos;
* Define se o documento anexado foi enviado por clientes, fornecedores ou outros;
* Definição se documento anexado será publicado no  GED;
* Escolher a pasta no GED para armazenamento dos documentos anexados (se publicado);
* Parametrização de atribuição de responsável por atividade;
* Personalização de SLA por atividade;
* Definição de gestor do processo.

**Processo:**

**Descrição do Processo:**

1. Atividade **Início:** 
   1. Solicitante abre o processo, preenche as informações necessárias e envia.
2. Atividade **Analisar o Documento:**
   1. Analisa se solicitação e o documento estão corretos e decide encaminhamento;
   2. Se necessitar de mais informações, encaminha para **3. Solicitar informações;**
   3. Se aprovado, encaminha para **4. Aprovado**;
   4. Se reprovado, encaminha para a atividade **5****. Reprovado - Solicitação finalizada;**
3. Atividade: **Solicitar informações:**
   1. A solicitação é recebida por quem a abriu para verificar as informações enviadas;
   2. O solicitante pode corrigir ou complementar a solicitação e encaminhar para a atividade **2. Analisar o documento**;
4. Atividade **Aprovado**:
   1. Verifica se o documento deve ser publicado no GED;
   2. Se sim, verifica em qual pasta no GED e publica o documento na pasta indicada gravando os campos e mantendo todas as permissões necessárias;
   3. Após publicação ou caso não precise publicar, a solicitação é finalizada com sucesso;
5. Atividade: **Reprovado - Solicitação finalizada:**
   1. Solicitação encerrada.
6. **Processo encerrado.**

**Formulário:**

**Detalhamento dos Campos:**

Dados Gerais

**Usuário de abertura:** usuário que estiver identificado na plataforma ao abrir a solicitação. *Carregado automaticamente.*

**Data:** data de abertura da solicitação. *Carregado automaticamente.*

**Id Centro de Custo:** código de centro de custo.

**Nome Centro de Custo:** descrição do centro de custo escolhido. *Carregado automaticamente.*

**\*Entidade Documento:** entidade responsável pela emissão do documento. Pode ser cliente, fornecedor, colaborador, interno ou outros.

**\*Id Entidade:** Entidade geradora do documento anexado.

**CNPJ/CPF:** documento da entidade geradora do documento. Preenchido automaticamente.

**\*Tipo do Documento:**tipo de documento que será anexado na solicitação. Pode ser um contrato, boleto, nota fiscal, recibo, etc. Deve ser apresentadas os tipos padrões do GED.

**\*Número de Documento:** número do documento anexado a solicitação.

**Valor:** Valor do documento anexado, se houver.

**\*Documento será publicado no GED:** Sim ou Não. Se sim, o campo "Pasta de Publicação" deverá ser habilitado.

**Pasta de Publicação:** abrir para escolha as pastas que tem acesso e permissão para publicar no GED.

**\*Documento expira?** Sim ou Não. Se sim, os campos referentes a expiração e revisão devem ser habilitados e obrigatórios, caso contrário ficam vazios e somente para leitura.

**Data de Expiração do documento:** Definir a data de expiração do documento, se houver.

**No dias para revisão do documento:** Número de dias para notificação antes que o documento expire.

Justificativa

**\*Justificativa:** Campo descritivo e obrigatório. Permite dar informações adicionais sobre como encontrar o solicitante, no caso da entrega dos itens ou prestação de serviços.

Validação

**Pessoa Validadora -** Responsável por validar se documento está correto e de acordo com as normas e diretrizes da empresa. *Campo carregado automaticamente.*

**Data -** Data em que aconteceu a validação. *Campo carregado automaticamente.*

**\*Justificativa -** Texto explicando a decisão tomada, seja para validar, pedir mais informações ou reprovar solicitação.

## Financeiro

### Solicitação de Adiantamento

### Solicitação de Reembolso

### Solicitação de Pagamento

**O que esse Flow faz:** Este flow registra a necessidade de um pagamento avulso para fornecedor / funcionário / prestador de serviço. Envia para os aprovadores de acordo com as regras definidas e encaminha a notificação para o responsável liberar o pagamento.

**O que esse Flow não faz:**

* Não envia a solicitação para o ERP;
* Não recebe os títulos automaticamente de um ERP;
* Não filtra os títulos que devem ser analisados.

**Parametrizações:**

* Cadastro de Fornecedores
* Cadastro de Colaboradores
* Cadastro de Prestadores de Serviços
* Cadastro de Centros de Custos
* Cadastro de Formas de Pagamento

**Processo:**

**Descrição do Processo:**

1. Atividade **Início:** 
   1. Solicitante abre o processo, preenche as informações necessárias e envia.
2. Atividade **Analisar e Validar:**
   1. Analisa se solicitação está correta e decide encaminhamento;
   2. Se aprovado, encaminha para **3. Realizar o pagamento**;
   3. Se necessitar de mais informações, encaminha para **4. Solicitar mais informações;**
   4. Se não, encaminha para a atividade **5****. Reprovado - Solicitação finalizada;**
3. Atividade **Realizar o pagamento**:
   1. Verifica se todos os dados estão corretos para realizar o pagamento;
   2. Se considerar que os dados não estão corretos, pode encaminhar para  **4. Solicitar mais informações;**
   3. Não encontrando nenhum problema, efetua o pagamento, preenche as informações e envia o processo a atividade **6. Processo encerrado.**
4. Atividade: **Solicitar mais informações:**
   1. Devolve a solicitação para quem a abriu pedindo mais informações ou correções nos dados;
   2. Solicitante pode corrigir ou complementar a solicitação e encaminhar para uma análise da área responsável;
   3. Usuário responsável pode cancelar a solicitação e finalizar o processo.
5. Atividade: **Reprovado - Solicitação finalizada:**
   1. Solicitação encerrada.
6. Atividade: **Processo encerrado.**

**Formulário (vou melhorar esse formulário):**

**Detalhamento dos Campos:**

Dados Gerais (padrão do Flow)

**Usuário de abertura:** usuário que estiver identificado na plataforma ao abrir a solicitação. *Carregado automaticamente.*

**Data:** data de abertura da solicitação. *Carregado automaticamente.*

**Usuário Solicitante:**usuário que solicitou o atendimento, mas por qualquer motivo precisa que outra pessoa abra a solicitação. Permite a escolha entre todos os usuários ativos cadastrados na plataforma. Mesmo que esteja definido nesse campo, todas as interações e notificações do processo acontecerão diretamente para o usuário de abertura.

**E-mail Solicitante:** carregado automaticamente a partir do cadastro do usuário solicitante.

**Estabelecimento/Filial:** Campo descritivo e não obrigatório. Permite informar o estabelecimento ou a filial a que o usuário pertence, se houver.

**Centro de Custo:** descrição do centro de custo que irá arcar com o valor relacionado a essa solicitação.

**Gestor:** O gestor do usuário ou do solicitante pode ser informado nesse campo. A consulta abre todos os usuários ativos cadastrados na plataforma.

**E-mail do gestor:** carregado automaticamente a partir do cadastro do usuário solicitante.

**Endereço do Solicitante:** Endereço do solicitante/unidade da empresa. Campo livre para digitação.

**Complemento:** Campo descritivo e não obrigatório. Permite dar informações adicionais sobre como encontrar o solicitante ou a unidade a que ele pertence.

Dados do Favorecido

**Tipo de favorecido:** O favorecido pode ser um colaborador, fornecedor ou prestador de serviço. Esse campo abre essas opções. Campo obrigatório.

**CPF/CNPJ:** documento que sai na nota fiscal emitida e que deve ser informado aqui. Campo obrigatório.

**Nome do favorecido:** Quando escolher o tipo do favorecido, deve abrir apenas os itens pertencentes a esse tipo. Campo obrigatório.

**Telefone do favorecido:** telefone do favorecido. Deverá ser carregado do cadastro de favorecidos, se houver.

**E-mail do favorecido:** e-mail do favorecido. Deverá ser carregado do cadastro de favorecidos, se houver.

**Justificativa:** Explicar o motivo para solicitar o pagamento. Campo obrigatório.

Dados do Pagamento

**Data vencimento:** data do 1o vencimento do pagamento solicitado. Campo obrigatório.

**Quantidade de parcelas:** número de parcelas desse pagamento. Campo obrigatório..

**Valor unitário:** valor unitário do pagamento solicitado. Campo obrigatório.

**Valor total do pagamento:** valor unitário multiplicado pelo total de parcelas. Campo obrigatório.

**Forma de pagamento:** quaisquer formas cadastradas. Por exemplo, podem ser pagamento em boleto, contra apresentação, nota fiscal, nota fiscal consumidor, etc. ou cartão de crédito, débito, PIX.

**Banco:** Banco no qual o pagamento deverá ser efetuado.

**Agência:** agência no qual o pagamento deverá ser efetuado.

**Conta:** conta na qual o pagamento deverá ser efetuado.

**Tipo de chave:** se houver, informar o tipo de chave.

**Chave:** chave recebida.

Aprovação do Gestor

**Aprovador:**nome do gestor.

**Data da análise:** data da análise, será preenchida automaticamente conforme validação do usuário responsável.

**Justificativa:** Explicar o motivo para aprovar ou recusar o pagamento.

Aprovação do Pagamento

**Aprovador:**nome do responsável pelo pagamento.

**Data do Pagamento/Recusa:** data do pagamento ou recusa, será preenchida automaticamente conforme validação do usuário responsável.

**Justificativa:** Explicar o motivo para efetuar ou recusar o pagamento.

## Recursos Humanos

### Solicitação de Férias

### Solicitação de Benefícios

### Lançamento de Atestado Médico

### Admissão

### Demissão

# **Flows Advanced**

## Compras Digital

### Solicitação de Compras

### Cotação

### Aprovação de Pedido de Compras

### Recebimento de Nota Fiscal
