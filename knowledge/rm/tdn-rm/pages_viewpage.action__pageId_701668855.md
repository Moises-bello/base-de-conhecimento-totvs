---
content_hash: 4134981403ea52cb25b794e2ae283c66b894429d6c9b770259c3a4651841065e
fetched_at: '2026-06-29T00:11:22.273061+00:00'
page_id: '701668855'
product: rm
source: tdn-rm
title: Pré-Venda - Pessoas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=701668855
version: 69
---

A visão de pessoas do Portal de Imóveis tem por fim modernizar e agilizar o cadastro de pessoas, tornando o processo mais simples, intuitivo e rápido.

Abaixo seguem os menus deste cadastro. Todas as opções e campos seguem os mesmos [padrões da tela de pessoas descontinuada.](https://tdn.totvs.com/pages/viewpage.action?pageId=622513802)

MãoC\_1Prospect

## **Objetivo:**

---

O cadastro de pessoas refere à inclusão de potenciais clientes, conhecidos como "prospects", em um banco de dados ou sistema de gestão de clientes.   
O termo "prospect" é utilizado para descrever indivíduos ou empresas que ainda não se tornaram clientes, mas que demonstraram algum interesse nos produtos ou serviços da empresa.

**Algumas particularidades de campos devem ser especificadas:**

* **Opções de Seleção Física ou jurídica**: Ao selecionar a opção **Pessoa Jurídica** no cadastro de pessoas, são exibidos dois novos campos: **Inscrição Estadual e** **Inscrição Municipal.** Estes campos exibidos apenas quando o tipo de pessoa for **"Pessoa Jurídica"**. Estes mesmos campos também são apresentados no cadastro de clientes e pessoas adicionais da proposta. Seguem o mesmo tipo e tamanho definidos no backoffice.
* **Cadastro de CPF ou CNPJ**: O sistema permite que o campo de CPF/CNPJ seja deixado em branco ou configurado como obrigatório. Para definir essa configuração, acesse **Backend > Parâmetros > Pessoas**, onde há a opção "CPF/CNPJ obrigatório no cadastro de pessoas?" que pode ser ajustada conforme a necessidade.
* **E-mail**: Não é permitido cadastrar e-mails duplicados, ou seja, o sistema não aceitará o registro de um e-mail que já exista na base de dados. No entanto, será possível incluir e-mails duplicados se o campo CPF estiver preenchido, uma validação interna do sistema. Os campos de e-mail deste cadastro respeitam a **[RFC 6530](https://www.rfc-editor.org/info/rfc6530)**, para tratativa de caracteres especiais em e-mails, porém não recomendamos o uso destes caracteres, pois alguns servidores de e-mails podem não estar preparados para tratá-los.

Importante!

Embora o uso de caracteres acentuados em endereço de e-mail sejam tecnicamente possíveis com o suporte adequado (configuração do servidor de e-mail), eles ainda não são amplamente aceitos ou recomendados para uso cotidiano. Para evitar problemas de compatibilidade, muitos recomendam o uso de e-mails sem acentos, cedilhas ou outros caracteres especiais complexos.

Alguns exemplos de e-mails com formatos inválidos: jo*ã*o@teste.com.br, joao*#*@teste.com.br, joao@teste*!*.com.br. 

* **Celular**: Não é possível cadastrar um número de celular que já esteja registrado no cadastro de outra pessoa. Entretanto, assim como no caso do e-mail, o sistema permitirá a duplicidade do número de celular apenas se o campo CPF estiver preenchido.
* **Corretor:** Refere-se ao corretor responsável por este lead, podendo ser atribuído no momento do cadastro ou definido pelo usuário SDR (Administrador).  
  Para clientes que utilizam integração com o RD Station, ao alterar o corretor no cadastro de pessoas, essa informação será automaticamente atualizada no registro correspondente no **[RD Station (campo: dono do Lead) (Marketing)](https://tdn.totvs.com/pages/releaseview.action?pageId=687737814)**, e no **[Funil de Leads (CRM).](https://tdn.totvs.com/pages/viewpage.action?pageId=699798333)**

Importante!

Para que o campo corretor esteja habilitado para edição é preciso marcar o parâmetro "***[Vincular prospect ao corretor (ao editar)](https://tdn.totvs.com/pages/viewpage.action?pageId=622513802)"***, no Grupo vinculado a este usuário.

* **Correspondente**: É uma pessoa jurídica contratada por instituições financeiras para fazer intermediação do Lead com rotinas financeiras;
* Ao final os dados serão listados na visão:
* SDR: Representante de vendas que atende a este lead.

* **Whatsapp, Telefone, Email:** Abaixo do Avatar de Lead há três botões, (Canto Superior Esquerdo) cada um com uma funcionalidade específica:

* + O ícone de Whatsapp irá abrir em nova aba no browser uma conversa direta via WhatsApp Web. É importante ressaltar que este link só funcionará se o corretor estiver logado no browser em seu Whatsapp Web;
  + O ícone de telefone irá usar o programa padrão de chamadas telefônicas do sistema;
  + O ícone de e-mail irá acionar o programa de e-mail padrão para envio de e-mails do sistema.

**Importar Cadastro:** Ao incluir um Lead, você pode importar um cadastro existente no Backoffice. Para isso, basta informar um CPF válido no campo correspondente e selecionar a opção "Importar cadastro". Além disso, também é possível atualizar um cadastro já existente. Nesse caso, ao selecionar a opção "Importar cadastro", se o registro já estiver no Backoffice, os dados serão atualizados no cadastro do Lead.

**Extrair Dados de Doc:** A partir do **Release 12.1.2410** o sistema permite o uso da ferramenta de IA, ***[DTA Vision Document](https://tdn.totvs.com/pages/viewpage.action?pageId=877136137)***, para executar a a extração de dados a partir da imagem de documentos

1. **Dados Básicos:** Nesta seção, os usuários têm a oportunidade de registrar informações fundamentais sobre o prospect. Isso inclui nome, cargo, informações de contato e outros detalhes pessoais relevantes.   

   Algumas observações referentes a este cadastro:

   * **Telefone**: O sistema permite cadastrar um número de telefone, mesmo que já exista outro registro com o mesmo número na base de dados. Isso ocorre porque pessoas da mesma família podem compartilhar o mesmo número de telefone fixo.
   * **Estado Civil**: Quando a opção "Casado" for selecionada, o sistema habilitará automaticamente os campos para preencher os **Dados Profissionais** e **Dados do Cônjuge**.

     + Se o estado civil da pessoa for diferente de **Casado** e houver **dados de cônjuge preenchidos**, será exibido um botão **"Excluir dados do cônjuge"**.
     + Ao clicar nesse botão, todos os dados do cônjuge serão apagados do banco de dados **de forma permanente**.
     + Se não desejar excluir os dados, **basta não clicar no botão**.

     ---

     **Cadastro com CPF/CNPJ já vinculado a um cônjuge**

     + Ao tentar cadastrar uma nova pessoa usando um **CPF/CNPJ que já está vinculado a um cônjuge cadastrado com um corretor associado**, o sistema exibirá uma mensagem informando que o CPF/CNPJ já está registrado.
     + Ainda assim, **o cadastro será permitido**, **desde que o corretor que está realizando a inclusão seja o mesmo vinculado ao cônjuge já existente**.
     + **Se o cônjuge cadastrado não estiver vinculado a nenhum corretor**, **qualquer usuário poderá incluí-lo** no sistema normalmente.
2. **Informações Financeiras:** Ao preencher os dados financeiros, a tela de prospect permite que os usuários capturem detalhes, como orçamento disponível, histórico de compras e qualquer outra informação financeira relevante.
3. **Endereço da Empresa:** Com a seção dedicada ao endereço da empresa, os usuários podem registrar o local físico onde o prospect opera. Isso não apenas facilita a logística, mas também fornece insights valiosos sobre a localização e a escala das operações do prospect.
4. **Perfil e Características:** Dados referente a Midia, e empreendimento de interesse.

**Versões a partir da 12.1.2506:** Quando a opção "União Estável" for selecionada, o sistema habilitará automaticamente os campos para preencher os Dados Profissionais e Dados do Cônjuge.

Ao importar o cadastro de pessoas de outras fontes, é importante prestar atenção em dois campos específicos do layout:  **pessoa\_naturalidade\_id** e **id\_conjuge\_naturalidade**.

Quando preencher esses campos com o ID correspondente à naturalidade já existente no banco de dados, o sistema utilizará esses IDs para buscar e retornar o nome do município associado. Em seguida, o campo **NATURALIDADE** nos cadastros da pessoa e do cônjuge será preenchido automaticamente com o nome do município correto.

**Exemplo:** Se você importar um registro onde o **pessoa\_naturalidade\_id** é 123, e esse ID está associado ao município de "São Paulo" no banco de dados, o sistema preencherá o campo NATURALIDADE com "São Paulo".

Campos Obrigatórios 

Quando houver campos definidos como obrigatórios no cadastro de Cliente/Fornecedor na integração com o PI, será necessário definir valores padrão (default) para esses campos.

Exemplos de campos que podem exigir valores padrão incluem: Tipo de Rua, Bairro, entre outros.

Essa configuração deve ser aplicada tanto nas informações da aba **Principal** quanto na aba **Pagamento**, garantindo a consistência dos dados e o correto processamento da integração.

C\_2Documentos

## **Objetivo:**

---

A opção de "documentos da pessoa" se refere à capacidade de armazenar e gerenciar documentos relacionados a uma pessoa específica. Esses documentos podem incluir uma variedade de informações, dependendo do contexto da plataforma ou sistema em que você está trabalhando. Aqui estão alguns exemplos de documentos que podem ser associados a uma pessoa em um contexto de leads:

1. **Documentos de identificação:** Pode incluir cópias digitalizadas de documentos como carteira de identidade, passaporte, carteira de motorista, etc.
2. **Comprovantes de endereço:** Faturas de serviços públicos, contratos de aluguel ou outros documentos que confirmem a residência da pessoa.
3. **Documentos financeiros:** Extratos bancários, comprovantes de renda, declarações de imposto de renda, entre outros.
4. **Contratos e acordos:** Contratos assinados, acordos legais ou qualquer documento relacionado a transações específicas com a pessoa.
5. **Notas e comunicações:** Qualquer comunicação escrita relevante, como e-mails, mensagens, ou notas internas sobre interações com a pessoa.

O objetivo é ter um local centralizado para armazenar informações importantes e relevantes sobre a pessoa associada ao lead. Isso pode facilitar a gestão de relacionamento com o cliente (CRM), permitindo uma visão mais completa e organizada das interações e transações.  Além de serem apresentados no cadastro da Pessoa, estes documentos também estarão disponíveis no Menu de Propostas (Documentos da Pessoa)

## **Como configurar:**

---

Primeiramente, será necessário configurar os tipos de documentos que deverão ser incluídos no cadastro da Pessoa. Esses documentos são essenciais para a validação de dados necessários para a aquisição ou locação de um imóvel, como: documentos de identificação, comprovantes de endereço, documentos financeiros, entre outros.

Para realizar essa configuração, acesse: **Backend > Globais > Documentos da Proposta**. Na tela, clique em "Adicionar" e preencha os campos:

* **Título**: Informe o nome dos documentos que serão solicitados no cadastro da Pessoa (ex.: Comprovante de Residência Atualizado, Cópia da CNH).
* **Tipo de Pessoa**: Indica o tipo de pessoa que deverá apresentar essas informações no cadastro.
* **Vinculado a**: Defina se a documentação estará vinculada à Proposta ou à Pessoa.
* **Tipo**: Defina a quem a solicitação de documentos se aplica (ex.: Prospect, Procurador, Procurador do Cônjuge, Fiador).
* **Estado Civil**: Especifica para qual estado civil informado no cadastro da Pessoa a documentação será solicitada.

Opções:

* **Obrigatório**: Indica se a documentação é obrigatória.
* **Ativo**: Define se a opção está ativa.
* **Exigir Upload**: Indica se é necessário o envio do documento.
* **Instruções de Envio e Instruções de Verificação**: Campos onde podem ser fornecidas instruções específicas sobre o envio e verificação do documento.

## **No cadastro de pessoas:**

---

Ao acessar o cadastro de Pessoas, no menu **Documentos**, será possível incluir documentos com base no registro de cada documentação solicitada na visão.

Além disso, nesta tela, o corretor pode realizar algumas ações relacionadas aos documentos. As opções disponíveis são:

* **Visualizar**: Baixa o documento anexado.
* **Excluir**: Exclui o documento.
* **Aprovar**: Permite ao corretor aprovar o documento inserido, atualizando o status.
* **Reprovar**: Permite ao corretor reprovar o documento inserido, também atualizando o status.
* **Enviar**: Inclui o documento no cadastro de documentos. É **preferível** que o nome/descrição do arquivo para upload seja informado **sem espaços**.

C\_3Interesses

## **Objetivo:**

---

O cadastro de interesse em imóveis permite que os usuários registrem suas preferências, como localização, tipo de imóvel e faixa de preço.   
Por exemplo, um usuário pode especificar que está buscando um apartamento de 2 quartos na zona sul da cidade, com valor entre R$ 300.000 e R$ 500.000 além de outras preferências.

**Cadastro de interesses:**

* **Termômetro:** Define o nível de interesse do prospect (Frio, Morno, Quente).
* **Tipo de Imóvel:** Define se o imóvel é Residencial, Comercial, etc.
* **Sol:** Indica a posição solar desejada (ex.: Manhã, Tarde).
* **Banheiros:** Quantidade mínima de banheiros desejada.
* **Suítes:** Quantidade mínima de suítes desejada.
* **Área:** Área mínima do imóvel, em metros quadrados.
* **Quartos:** Quantidade mínima de quartos desejada.
* **Vagas:** Número mínimo de vagas de garagem.
* **Valor Máximo:** Valor máximo do imóvel desejado.
* **Empreendimento:** Lista os empreendimentos disponíveis. Ao selecionar um, os campos Bairro e Cidade são preenchidos automaticamente e ficam não editáveis.
* **Bairro:** Preenchido automaticamente com base no empreendimento selecionado. Não editável.
* **Cidade:** Preenchida automaticamente com base no empreendimento selecionado. Não editável.
* **Empreendimento em lançamento:** Checkbox para demonstrar interesse nos empreendimentos em fase de lançamento.
* **Unidade:** Lista as unidades do empreendimento selecionado.
* **Situação:** Define o status do interesse (Aberto, Ganho, Perdido).
  + **Aberto:** Campos Proposta e Motivo permanecem desabilitados.
  + **Ganho:** Habilita o campo Proposta para seleção da proposta que resultou no ganho.
  + **Perdido:** Desabilita o campo Proposta e habilita o campo Motivo, para registrar o motivo da perda.
* **Proposta:** Habilitado apenas quando a situação for Ganho. Permite selecionar a proposta associada.
* **Motivo:** Habilitado apenas quando a situação for Perdido. Permite informar o motivo da perda.

**Importante:** Se o parâmetro do sistema *“Clientes com interesses perdidos ou ganhos vão para o banco de clientes”* estiver habilitado, ao alterar a **Situação** de um interesse para **Perdido** (ou Ganho) e salvar, a tela de edição do cadastro da pessoa será fechada automaticamente .

Caso queira editar ou excluir, basta navegar no campo e selecionar a opção para as opções serem apresentadas;

C\_4Propostas

Ao acessar o menu de Propostas, serão exibidas as propostas existentes para este Lead. Esses mesmos registros também podem ser visualizados na visão de propostas.

C\_5Contratos

Ao acessar o menu de Contratos, serão exibidos os contratos existentes para este Lead. Esses mesmos registros também podem ser visualizados na visão de contratos.

C\_5Time Line

## **Objetivo**

---

A Timeline, ou linha do tempo, no cadastro de um Lead, tem como objetivo registrar e exibir de forma cronológica todas as interações e atividades relacionadas a esse contato. Sempre que um corretor realiza uma ação — como entrar em contato com o lead para discutir uma oferta de imóvel — essa interação é registrada na TimeLine, acompanhada de data e hora.

Além disso, é possível anexar arquivos, como propostas comerciais ou documentos relevantes, diretamente na linha do tempo. Dessa forma, todas as informações ficam centralizadas e acessíveis no mesmo registro.

A TimeLine oferece uma visão sequencial e completa do histórico de relacionamento com o lead, facilitando o acompanhamento das ações e decisões tomadas ao longo do tempo. Essa funcionalidade é especialmente útil para equipes de vendas e marketing, pois proporciona uma compreensão mais clara sobre a evolução do relacionamento e apoia estratégias de atendimento e conversão mais eficazes.

Algumas informações que podem ser registradas na Timeline incluem:

1. **Atividades de Contato:** Registra quando e como a equipe entrou em contato com o lead, seja por e-mail, telefone, reuniões ou outros meios.
2. **Interesses Demonstrados:** Registra os interesses específicos que o lead manifestou durante as interações.
3. **Eventos Relevantes:** Registra eventos importantes, como webinars, seminários ou outras atividades relevantes para o lead.
4. **Mudanças de Status:** Registra alterações no status do lead, como mudanças de fase no processo de vendas.
5. **Histórico de Compras ou Atividades no Site:** Se aplicável, pode incluir informações sobre compras anteriores ou atividades específicas no site.
6. **Notas e Comentários:** Permite que os membros da equipe adicionem notas e comentários sobre as interações, para compartilhar informações importantes.
7. **Propostas Cadastradas**: Ao registrar uma proposta para o lead, as informações da subunidade, bloco, empreendimento e número da proposta são adicionadas automaticamente à TimeLine, garantindo o histórico completo da negociação.

## **Procedimentos para Utilização**

---

Na edição de Pessoas, navegue até o menu Timeline e clique em Incluir. Em seguida, na tela aberta, inclua as anotações pertinentes.

* Mensagem: Este é um campo obrigatório e serve para registrar **Notas ou Comentários**, como informações a respeito dos Leads, seus contatos realizados e outros assuntos.
* Situação: Permite alterar a **situação** do lead, facilitando a identificação de seus interesses e seu termômetro dentro do fluxo de vendas.
* Forma de Contato: As **formas de contato** que foram utilizadas na comunicação com o lead.
* Agendar Tarefa: Ao agendar uma **tarefa**, a mesma será inserida como compromisso ao corretor, facilitando a organização de sua agenda.
* Horas: A hora do agendamento definido.
* O Botão "**Anexar**" permite ao usuário anexar documentos diretamente na Timeline. Lembrando que o limite de tamanho de documento é definido via parâmetro do sistema.

Após inclusão da Timeline, poderemos visualizar esse registro diretamente no menu Timeline do Lead. Nesta visualização, os corretores poderão acessar informações cruciais de forma organizada e cronológica.

Algumas das informações que estarão disponíveis incluem:

1. **Data e Hora de Inclusão:** Cada evento na Timeline será registrado com precisão de data e horário, permitindo uma compreensão detalhada do histórico de interações.
2. **Assunto**: Cada entrada na Timeline exibirá a mensagem registrada no momento de sua criação, oferecendo uma visualização rápida e clara dos eventos ocorridos.
3. **Tarefa / Anotação:** Caso a inclusão possua um agendamento com data e hora definidos, a entrada na Timeline será exibida como **Tarefa**, apresentando essas informações. Se não houver agendamento, a entrada será exibida como **Anotação**.
4. **Enviar Anexo:** Permite ao corretor vincular um documento ao registro da Timeline. Cada registro pode conter apenas um anexo. Caso seja necessário removê-lo, basta clicar no ícone de lixeira.

O recurso **Filtros** na Timeline permite que o usuário localize e visualize entradas de forma organizada e eficiente. Os filtros disponíveis são:

* **Tipo:** Permite selecionar o tipo de entrada a ser exibida.

  + **Anotação:** Exibe apenas entradas do tipo Anotação.
  + **Tarefa:** Exibe apenas entradas que foram agendadas como Tarefa.
* **Status:** Permite filtrar as **Tarefas** pelo seu estado atual.

  + **Aguardando:** Exibe Tarefas pendentes.
  + **Concluída:** Exibe Tarefas que já foram finalizadas.
* **De** e **Até:** Permite selecionar um **intervalo de datas** para exibir as entradas criadas ou agendadas dentro desse período.
* **Pesquisar:** Campo de texto livre para buscar informações específicas dentro das entradas da Timeline.

Após definir os critérios de busca, clique no botão **Pesquisar** (representado por uma lupa) para aplicar o filtro e exibir os resultados.

C\_6Situação

## **Situação:**

---

O campo **Situação** no cadastro de leads existe para indicar em qual **etapa do processo de vendas** o lead se encontra. Ele serve como um **marcador do progresso comercial**, permitindo que a equipe saiba, rapidamente, se o lead está em prospecção, negociação, aguardando resposta, fechado (ganho ou perdido), entre outras fases definidas pela empresa.
