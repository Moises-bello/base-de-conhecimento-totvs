---
content_hash: 71fe5236dd9e7a4032d178c7cf00673485a069be52ebb6b3d40290203e8c32c6
fetched_at: '2026-06-29T00:11:27.423935+00:00'
page_id: '725272863'
product: rm
source: tdn-rm
title: Processo Trabalhista - Funcionamento dos eventos eSocial
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+Trabalhista+-+Funcionamento+dos+eventos+eSocial
version: 106
---

**EVENTOS**

* **S-2500**
* **S-2501**
* **S-2555**
* **S-3500**

[eSocial - Leiaute 1.2](https://tdn.totvs.com/display/LRM/eSocial+-+Leiaute+1.2)

[eSocial - Leiaute 1.3](https://tdn.totvs.com/display/LRM/eSocial+-+Leiaute+1.3)

Importante!

* Processo desvinculado do produto, ou seja, não serão exibidas informações cadastradas no produto. Foram criadas novas tabelas.
* Não haverá validação com outros eventos do eSocial, por exemplo: Folha e SST.
* Não possui integração com Folha, SST e Financeiro.
* Foi disponibilizado no TAF o cadastro desses eventos também, disponível para clientes TAF FULL.

**Objetivo**

Permitir o cadastro das informações do Processo Trabalhista.

**Regra de envio**

Devem ser prestadas, independentemente do período abrangido pelas decisões/acordos, as informações relativas a:

a) processos trabalhistas cujas decisões transitaram em julgado do dia 1º de outubro de 2023 em diante;

b) acordos judiciais homologados a partir desta mesma data;

c) processos com trânsito em julgado da decisão homologatória dos cálculos de liquidação a partir dessa mesma data, mesmo que o trânsito em julgado da sentença condenatória tenha ocorrido em data anterior;

d) acordos no âmbito de CCP ou Ninter celebrados também dessa data em diante; ou

e) determinações judiciais para cumprimento antecipado de decisão, ainda que parcial, proferidas a partir dessa mesma data.

**Prazo de envio**

Até o dia 15 (quinze) do mês subsequente à data:

a) do trânsito em julgado da decisão líquida proferida no processo trabalhista;

b) da homologação de acordo judicial;

c) do trânsito em julgado da decisão homologatória dos cálculos de liquidação da sentença;

d) da celebração do acordo celebrado perante CCP ou Ninter; ou

e) da determinação judicial para cumprimento antecipado da decisão, ainda que parcial. Esse prazo pode ser antecipado para fins de cumprimento de obrigações decorrentes de decisão judicial.

Espaço Legislação

A área [espaço legislação](https://espacolegislacao.totvs.com/) da TOTVS é destinada a apresentar todas as novidades e atualizações da legislação fiscal e tributária brasileira. Temos também um espaço no [YouTube](https://www.youtube.com/playlist?list=PLXa8l0dq5zRkxpHqPKL7ZVYHt3urJ9VeM) com os eventos realizados.

Aproveite e se [inscreva](https://rhinforma.totvs.com/) para receber os comunicados.

**Como Funciona**

Como FuncionafadeParametrizaçãoParametrização

Acessar o módulo **Folha de Pagamento**, ir até o menu **Configurações | Parametrizador:**

Abrir o **Parametrizador** e acessar o item **eSocial | Configurações Gerais**:

Clicar em **Avançar**, acessar **Configurações Gerais 1/7**, preencher o campo **Versão do Leiaute**:

Clicar em **Avançar**, acessar **Integração TAF | Outros Parâmetros**, preencher os campos da tela:

No campo **Porta** do **Servidor API** informar a mesma porta definida nos arquivos **RM.Host.exe.config** e **RM.Host.Service.exe.config** tag **APIPORT**.

No campo **Porta** do **Servidor APP** informar a mesma porta definida nos arquivos **RM.Host.exe.confi**g e **RM.Host.Service.exe.config** tag **HTTPPORT**.

Para mais informações referente aos campos **Servidor**, em **Servidor API** e **Servidor APP**, acessar o link .

**Atenção:**

A persistência do Processo Trabalhista é realizada segundo o campo **Servidor** em **Servidor API** e não segundo o Alias logado (O Processo Trabalhista utiliza API para leitura e Persistência dos dados no RM, e a url da API é montada utilizando o endereço informado neste campo). Portanto, ao realizar um backup da base de Produção e restaura-la como Homologação, é importante que o valor do campo seja alterado para o endereço do RM de Homologação.

Exemplo elucidado considerando arquitetura com RM e Banco de Dados na mesma máquina:  
Máquina A (de Produção);  
Máquina B (de Validação ou Testes);  
   
- O ambiente da Máquina A está com sua parametrização do campo **Servidor** em **Servidor API** com o endereço da Máquina A na rede. Ao realizar um backup e restaurar na Máquina B, a Leitura e Persistência dos dados será feita na Máquina A, visto que o campo continua com o endereço da Máquina A. Portanto é necessário que o campo tenha o valor alterado para o endereço da Máquina B na rede para que o Processo Trabalhista tenha a Leitura e Persistência no RM da Máquina B.

Por envolver arquitetura, é recomendado consultar a TI para correta parametrização.  
 

**Importante:** Essa configuração é referente as parametrizações de instalação do RM e não do TAF.

PermissãoPermissão

Com a Parametrização concluída, o próximo passo é liberar o acesso dos usuários, através do perfil.

Acessar o módulo **Serviços Globais**, ir até o menu **Segurança | Perfis**:

Abrir a tela e selecionar o sistema **Gestão de Pessoas**:

Criar ou Editar o perfil que deseja **Permitir Acesso** ao menu **Processo Trabalhista** e salvar:

CadastroAcesso ao Cadastro

Após a conclusão da Parametrização e Permissão, o próximo passo é acessar a tela de cadastro que fica no módulo **Gestão de Pessoas** , ir até o menu **Gestão Organização | Processos Trabalhistas**:

EventoS25001.2Leiaute 1.2

Para detalhar a regra do evento S-2500 , favor acessar o link: [Cadastro do eventos S-2500](https://tdn.totvs.com/display/LRM/Cadastro+do+eventos+S-2500+-+Leiaute+1.2)

Para detalhar a regra do evento S-2501 , favor acessar o link: [Cadastro do eventos S-2501](https://tdn.totvs.com/display/LRM/Cadastro+do+eventos+S-2501+-+Leiaute+1.2)

Para detalhar a regra do evento S-3500 , favor acessar o link: [Evento de exclusão - S-3500](https://tdn.totvs.com/pages/viewpage.action?pageId=887737582)

Importante!

Para que o botão SALVAR fique habilitado, é necessário que todos os campos obrigatórios sejam preenchidos em todas as telas exibidas.

Após salvar,  será executado o gatilho para geração do XML na [fila de evento existente no Folha de Pagamento](https://tdn.totvs.com/display/LRM/Fila+de+Eventos).

Evento1.3Leiaute 1.3

Para detalhar a regra do evento S-2500 , favor acessar o link: [Cadastro do eventos S-2500](https://tdn.totvs.com/display/LRM/Cadastro+do+eventos+S-2500+-+Leiaute+1.3)

Para detalhar a regra do evento S-2501 , favor acessar o link: [Cadastro do eventos S-2501](https://tdn.totvs.com/display/LRM/Cadastro+do+eventos+S-2501+-+Leiaute+1.3)

Para detalhar a regra do evento S-2555 , favor acessar o link: [Evento de consolidação - S-2555](https://tdn.totvs.com/pages/viewpage.action?pageId=887737413)

Para detalhar a regra do evento S-3500 , favor acessar o link: [Evento de exclusão - S-3500](https://tdn.totvs.com/pages/viewpage.action?pageId=887737497)

Para detalhar a regra dos eventos alterados pela nota técnica, favor acessar o link:

Importante!

Para que o botão SALVAR fique habilitado, é necessário que todos os campos obrigatórios sejam preenchidos em todas as telas exibidas.

Após salvar,  será executado o gatilho para geração do XML na [fila de evento existente no Folha de Pagamento](https://tdn.totvs.com/display/LRM/Fila+de+Eventos).

AssistenteAssistente de Vinculação de Processos Jurídicos a Processos Trabalhistas

O [Assistente de Vinculação de Processos Jurídicos a Processos Trabalhistas](https://tdn.totvs.com/pages/viewpage.action?pageId=799270888) tem como finalidade facilitar a migração das informações entre os cadastros "Processo Jurídico" e "Cadastro do evento S-2500" do Processo Trabalhista.

Importante!

* Somente as informações que existem nos dois cadastros serão enviados, desde que no evento S-2500 não tenha regra atrelada de validação do campo.
* O assistente não envia o evento S-2500 para o eSocial pelo fato de ter campos específicos e obrigatórios, conforme definição do eSocial.
