---
content_hash: 564cf70dd94e6e050e57f3433032376af1b33957fe824cb4033e8e565066c2ad
fetched_at: '2026-06-29T00:05:55.105646+00:00'
page_id: '126190638'
product: rm
source: tdn-rm
title: Tutorial TOTVS Restore 2.0
type: documentation
url: https://tdn.totvs.com/display/LRM/Tutorial+TOTVS+Restore+2.0
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                         **Versão:** 11.50, 11.80, 12.1 |
| **Processo** | **:** | Instalação |
| **Subprocesso** | **:** | *Tutorial Totvs Restore Versão 2.0* |
| **Data da publicação** | **:** | 19/02/2014 |

**01 – Tela Inicial**

* Execute o TOTVS Restore e em sua tela inicial, clique no botão "adicionar" cujo ícone é representado por um símbolo "+ " (vide ilustração abaixo)

**02- Criação do Ambiente**

* Na nova janela, digite o nome do ambiente na caixa de texto correspondente. Esse nome deve ser descritivo o suficiente para que você possa identifica-lo posteriormente na grade da tela inicial. Em seguida, digite um nome de usuário e senha conforme ilustração abaixo. Esse nome de usuário deverá obrigatoriamente ser uma conta do Windows com privilégios de administrador em todas os servidores que serão gerenciados pelo TOTVS Restore.

**03 – Adicionar Máquinas**  
 Na tela seguinte, será possível filtrar todos os servidores do domínio através dos controles de tela:  
 Caixa de texto "Domínio": digite o domínio que contém todos os servidores a serem gerenciados. Apenas um único domínio poderá ser utilizado por projeto/ambiente, até mesmo por que um usuário estará a princípio vinculado a um único domínio.  
 Caixa de texto "Iniciar com": Se desejar filtrar os servidores pelo seu nome exato, nome parcial ou se até mesmo desejar listar todos os servidores do domínio, poderá então realizar essa tarefa através do texto digitado nessa opção. Se não digitar nada, todos os servidores serão listados no listbox; se digitar o nome completo de um servidor e o mesmo existir, será listado apenas esse servidor no listbox; se digitar apenas o início do nome do servidor, todos os servidores cujo nome começar com as mesmas iniciais serão listados no listbox.(vide ilustração abaixo).  
   
 **04 – Desinstalação de Programas**

* Nesse passo, será possível selecionar quais os programas se deseja desinstalar antes que o processo de instalação se inicie (vide ilustração abaixo)

**05 – Gerenciar Serviços do Windows**

* Nessa tela, serão listados por servidor todos os serviços que contém as substrings "RM" ou "TOTVS" e que estão registrados ( em execução ou não). Logo, será possível definir uma ação para cada um deles caso necessário. As ações são Parar, Iniciar ou Remover. Sempre utilize essa opção para remover os serviços que foram replicados pelo TOTVS Restore em instalações anteriores. Os nomes desses serviços seguem o padrão RM.Host.Service#### onde as cerquilhas representam o número da porta para o qual o serviço de host foi replicado.

**06 –** **Instalação dos Produtos**

* Agora, será necessário definir quais os softwares serão instalados por servidor. Utilize os botões "..." para localizar e selecionar os arquivos de instalação dos produtos da linha RM (ou não), assim como os botões  e  para poder adicionar ou remover um arquivo de instalação. As instalações serão executadas na ordem de sua inserção, conforme destaque em vermelho na imagem abaixo:

**07- Replicar Diretórios**

* A opção de "Replicar Diretórios de Instalação" deverá ser utilizada exclusivamente para as instalações dos produtos (Folha de pagamento, automação de ponto, Recursos Humanos, etc...) A finalidade dessa opção é a de se permitir que os diretórios dos aplicativos sejam replicados e devidamente configurados, permitindo que cada executável de uma pasta diferente possa utilizar o RM.Host em uma porta distinta.

**08 – Configurar arquivos de Config**

* Agora, será possível copiar arquivos de configuração para as pastas distintas nessa opção. Observe que essa opção pode ser utilizada tanto para cópia dos arquivos de configuração dos aplicativos (RMLabore, RMChronus, etc...) quanto para se copiar os arquivos de config dos serviços de host.

**09 – Copiar arquivos ao final da instalação**

* Através dessa opção, será possível copiar arquivos ao fim da instalação. Observe que após a cópia, os serviços de host serão reiniciados. Utilize essa opção para copiar o arquivo Alias.Dat nas instalações dos servidores que irão atuar como AppServers.

**10 – Replicar Serviços de Host**

* Através dessa tela, será possível definir o número de serviços de host a serem instalados em um servidor. Para os AppServers, não será necessário replicar o diretório de host, uma vez que todos os serviços podem utilizar de forma compartilhada o mesmo Alias.dat, já que nenhum deles poderá conter a tag JobServerEnabled = true.

* Já para os servidores que serão JobServers, será obrigatório se marcar o checkbox de réplica de diretório de host, já que cada jobserver deverá ter seu próprio alias.dat e evitando a concorrência na tabela GJOBSERVER.
* Selecione então a quantidade de hosts que deseja instalar no servidor específico e digite o número da porta inicial. Recomendado iniciar pela porta 8090, sempre.

**11 – Parâmetros do Ambiente**

* Na tela de parâmetros do ambiente, SEMPRE deixar marcada a opção "Local" para todas as instalações. Em seguida, clique no botão "Salvar".

**12 – Atualização**

* Finalizados todos os passos anteiories, basta selecionar o Ambiente na grade inicial do TOTVS Restore e clicar no botão "Atualizar Ambiente". Uma nova janela será exibida ilustrando uma seção com barra de progresso para cada instalação de servidor em execução. As instalações são todas executadas em paralelo.

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha);
