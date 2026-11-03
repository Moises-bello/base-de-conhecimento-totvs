---
content_hash: 2b6b2126b7ea1befc874afc010d9fd82cb0f9f1feb7647ff1fe0cd224c3becb8
fetched_at: '2026-06-29T00:09:48.512411+00:00'
page_id: '435105178'
product: rm
source: tdn-rm
title: Utilitários - Portal/App - Manutenção de Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105178
version: 23
---

### Introdução

---

O processo de **manutenção de usuários** possibilita a criação automatizada de usuários de acesso ao Portal de Imóveis, ao PDC e ao app Meu Imóvel.

Após a execução desta funcionalidade, os usuários listados no log deste processo terão o campo *código usuário de acesso* preenchidos no seu cadastro de cliente/fornecedor.

Para acessar esta ferramenta acesse o menu utilitários | portal/app | manutenção de usuários:

### Procedimentos para Utilização

---

Ao acessar esta funcionalidade o sistema apresenta ao usuário encontrará os seguintes campos:

* **Desativar Usuários dos Compradores/Locatários/Corretores:** Ao marcar esta opção, o campo "Usuário de Origem" ficará desabilitado e, ao executar o processo, os usuários  serão desativados, bloqueando o acesso ao portal.
* **Inserir um Usuário sem Vínculo na Locação/Lojista:** Este campo é habilitado ao selecionar a opção para conceder acesso aos contratos para *locação/lojista*, detalhado mais abaixo. Ao marcar esta opção o sistema irá criar um usuário, sem vínculo a nenhum contrato de locação ou lojista, para que se possa testar o acesso às funcionalidades destes portais no PDC. Dessa forma é possível de se tentar simular algum problema reportado pelos clientes sem a necessidade de solicitar a senha de acesso deles;
* **Usuário de Origem:** Usuário que será utilizado com o "modelo" para que os usuários criados sigam as mesmas configurações de perfis e permissões de acesso.
* **Usuários dos Compradores / Locatários / Corretores:**
  + **Código de Acesso:** Código de acesso a ser considerado para o banco de dados;
  + **Somente Cli/For sem Usuário:** Ao marcar esta opção, o processo criará códigos de acesso apenas para os usuários que ainda não possuem essa informação preenchida. Essa opção vem selecionada por padrão para evitar que Cli/For já parametrizados sejam processados novamente, prevenindo alterações indesejadas nos seus acessos. Além disso, essa configuração melhora significativamente a performance da execução, pois o sistema processa apenas os usuários nessas condições específicas. Na primeira execução, é comum que todos os Cli/For não possuam usuários cadastrados, mas nas execuções seguintes, haverá um ganho substancial de desempenho.  
    Por outro lado, ao desmarcar essa opção, o sistema processará todos os cadastros, independentemente da situação, o que pode comprometer a performance.
  + **Coligada:** Será considerado para filtrar uma coligada específica. Caso não seja preenchido, irá considerar as vendas de todas as coligadas;
  + **Compradores/Locatários Principal**: Com o parâmetro marcado será criado o usuário apenas para o Comprador/Locatário Principal. Caso esteja desmarcado é criado um usuário considerando os demais compradores/Locatários.

* **Contratos/Corretores:** Selecione em qual entidade este processo irá atuar. as opções disponíveis são:
  + **Venda:** Permite selecionar se deseja gerar os usuários de acesso para contratos de vendas. Ao selecionar esta opção, o sistema habilitará os campos abaixo:
    - **Venda:** Permitirá executar o processo para uma venda específica. Caso não seja preenchido, irá considerar todas as vendas conforme seleção ou não da Coligada.
    - **Situação da venda/aluguel:** Permite selecionar para qual situação de venda irá executar o processo e gerar os usuários. Por padrão, vem selecionada a situação "Efetivada".
    - **Empreendimento:**Permitirá executar o processo para um empreendimento especifico. Desta forma o sistema irá criar um usuário para todas as vedas que ainda não possuam.
  + **Locação/Lojista:** Permite selecionar se deseja gerar os usuários de acesso para contratos de locação, com papel de locatário e lojista, conforme cadastro realizado na aba *Controle de Acesso* do contrato de locação. Ao selecionar esta opção o sistema apresenta os campos abaixo e habilita a opção **Inserir um Usuário sem Vínculo na Locação/Lojista** descrita no início deste documento;
    - **Contrato Locação:** Informe o contrato de locação, caso necessite tratar o acesso para um contrato específico;
    - **Código da Função:** Selecione a função para filtrar para quais grupos de locatários/lojistas serão criados os usuários de acesso. Este campo não é obrigatório e ao deixá-lo em branco, o sistema irá criar e atribuir o usuário de acesso ao cadastro deste cliente/fornecedor;
  + **Ambos Anteriores:** Permite que sejam gerados os usuários para ambos os tipos de contratos acima simultaneamente. São habilitados os seguintes campos: Venda, Contrato de Locação e Código da Função, já descritos acima;
  + **Corretores (PI):** Esta opção permite que seja gerados os códigos de usuário de acesso para os usuários que são corretores no PI. Para que esta opção seja concluída com sucesso, devem ser observados os seguintes aspectos:
    - Este corretor esteja cadastrado previamente como cli/for no rm, com o mesmo cpf ou cnpj que está cadastrado no Portal de Imóveis. Em outras palavras o campo id\_erp deve estar preenchido na tabela de usuários e o cpf/cnpj deve ser o mesmo no rm;
    - Este usuário deve exercer o papel de corretor no grupo ao qual ele está associado no Portal de Imóveis.

Observação:

Caso os campos de **coligada**, **venda** e **empreendimento** não sejam preenchidos, o sistema realizará a busca considerando todos os registros de forma global.

* **Enviar e-mail para usuários criados:** Se marcada esta opção, irá enviar um e-mail para cada usuário gerado pelo processo, informando a criação do usuário, seu código de acesso e sua senha.
  + **Endereço de acesso ao portal**: Este campo deverá ser preenchido e será considerado no e-mail enviado. Ele deve conter o caminho do portal a ser acessado, para que os compradores saibam qual o link de acesso. Este campo, após o primeiro preenchimento, virá preenchido nas próximas vezes em que o usuário executar o processo.
  + **Assunto do E-mail**: Ao informar será enviado o assunto preenchido no processo, caso o campo fique sem preenchimento o irá enviar no assunto o texto '**Acesso ao portal do cliente**'.

### Efeitos após o processamento

---

Após a execução deste processo e de acordo com as opções selecionadas, os compradores/locatários/corretores terão usuários criados desde que não exista um usuário de acesso cujo código seja o seu CPF/CNPJ, mesmo que um usuário de acesso qualquer já esteja associado e cujo código não seja o CPF/CNPJ. Uma vez que o usuário é criado, ele é associado ao respectivo comprador/locatário.

Os novos usuários serão criados, com seu código de acesso e senha iguais ao número de CPF ou CNPJ (apenas números, sem máscaras) de seu cadastro.

Ao cancelar ou distratar  uma venda o usuário do comprador (usuário do PDC) poderá ser inativado, bastando executar o processo com a opção "Desativar usuários dos compradores" marcada.

**Ao término de execução deste processo, o sistema apresenta um log detalhando os registros tratados.**

Em relação ao Portal do Cliente, para que os usuários dos compradores sejam criados, o "administrador" ou "gestor" do sistema pode faze-lo através do produto TOTVS da linha RM, no cadastro de usuários do sistema, porém, para facilitar para os clientes que já possuem vendas ativas, devido ao grande volume, foi criado o processo Manutenção de Usuário.

Este processo também poderá ser utilizado para criação de novos usuários em novas vendas, uma vez que a criação do usuário para o portal poderá ser feita em outro momento, em lote evitando assim que o atendente crie usuário e senha na criação do contrato de venda.

A partir do Release 12.1.2205, a senha criada através desta ferramenta, para esses Usuários, irá respeitar as parametrizações de complexidade de Senha definidas na aba de *Segurança*, dos [Parâmetros Globais](https://tdn.totvs.com/pages/viewpage.action?pageId=496800805) do RM:

* **Tamanho Mínimo** da Senha;
* Senha deve conter caracteres **maiúsculos**;
* Senha deve conter caracteres **minúsculos**;
* Senha deve conter **símbolos**; e
* Senha deve conter caracteres **números.**

Como Fazer

---

**Observação:** Utilizando o ambiente N camadas, é possível realizar o agendamento do processo de *Manutenção de Usuários*, para que a criação dos Usuários de Acesso ao Portal seja realizada automaticamente, em datas e horários previamente determinados, evitando a necessidade de se executar manualmente este processo após o cadastro de cada venda.

Veja Também

---

* **[Cadastro de Usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=244425754)**
