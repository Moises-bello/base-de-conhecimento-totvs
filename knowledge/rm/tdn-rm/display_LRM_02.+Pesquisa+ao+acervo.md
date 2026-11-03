---
content_hash: 48c425244c9814a7ae95fb61febad754f86acd72c10e1aeae9b313ada290abf0
fetched_at: '2026-06-29T00:10:58.942722+00:00'
page_id: '607856695'
product: rm
source: tdn-rm
title: 02. Pesquisa ao acervo
type: documentation
url: https://tdn.totvs.com/display/LRM/02.+Pesquisa+ao+acervo
version: 66
---

Versão disponível

Esta funcionalidade está disponível a partir da versão 12.1.2205

Atualização

A partir das versões 12.1.2402.228 e 12.1.2406.156, a informação referente à quantidade de exemplares existente em cada unidade bibliotecária foi alterada. Agora serão exibidos os campos:

**Disponíveis no acervo**: mostra a quantidade de exemplares existentes no acervo para cada unidade.

**Disponíveis para empréstimo**: mostra a quantidade de exemplares disponíveis para serem emprestados. **Os exemplares que não possuem o campo "Situação do exemplar" preenchido no [cadastro do exemplar](https://tdn.totvs.com/display/LRM/Exemplar), também podem entrar na contagem dos exemplares disponíveis.**

Estes campos podem ter variação em seus valores, dependendo da configuração dos parâmetros do TOTVS Gestão Bibliotecária.

Consiste no retorno de informações das publicações e exemplares disponíveis no acervo da biblioteca.

Usuario/Unidade

Quando o usuário logado no sistema possui dependentes, o sistema não utiliza o contexto global do portal educacional.  
Nesses casos, a biblioteca adota seu próprio contexto, definido individualmente na tela, conforme ilustrado na imagem abaixo.

Permissão

Para habilitar a funcionalidade de Pesquisa ao Acervo no Portal Educacional faz-se necessário habilitar as permissões de Perfil do usuário para que o menu seja exibido no caminho: 

**Serviços Globais | Segurança | Acesso | Perfil | Sistema: Gestão Bibliotecária | [13] Gestão Bibliotecária (Portal) | [13.02] Biblioteca (Novo Portal do Aluno) | [13.02.01] Pesquisa ao acervo**

Para habilitar a funcionalidade de "Reserva de publicação" no Portal Educacional, faz-se necessário habilitar a permissão de Perfil do usuário para que o botão de reservar esteja disponível nos detalhes do exemplar da publicação.  
**Serviços Globais | Segurança | Acesso | Perfil | Sistema: Gestão Bibliotecária | [13] Gestão Bibliotecária (Portal) | [13.02] Biblioteca (Novo Portal do Aluno) | [13.02.01] Pesquisa ao acervo | [13.02.01.01] Fazer reserva**

No Portal Educacional, será disponibilizado o botão "Reservar" nos detalhes do exemplar da publicação, conforme mostra a figura abaixo:

Personalizando a opção “Buscar por”

As configurações do parâmetro "[14.03.01 - Pesquisa ao Acervo](https://tdn.totvs.com/display/LRM/14.03+-+Pesquisa)" definem os campos que serão disponibilizados em "**Buscar por:**"

Pesquisa

Ao preencher a informação no campo "**Pesquisa**", selecionar a opção "**Buscar por**" e clicar em "**Buscar**" será aplicada a pesquisa.

É obrigatório informar no campo "**Pesquisa**" uma palavra com no mínimo 3 caracteres

* Ao clicar no ícone   será copiado a referência da publicação para a área de transferência.
* Ao clicar no ícone  será acionada a impressão da referência da publicação.
Detalhes da publicação

Ao clicar sobre os itens em destaque conforme a imagem abaixo, você será redirecionado para a pagina de exibição dos detalhes da publicação.

**Página de detalhes da publicação**

Download

A opção de download de anexo somente vai estar disponível caso:

1. Existir um anexo associado a esta publicação
2. A opção de "**Disponibilizar para o download na pesquisa ao acervo"** estiver habilitada ().

Ao clicar no botão de download o arquivo será baixado (Download).

Opção "Exibir detalhes"

Ao clicar no botão "**Exibir****detalhes**" serão exibidos todos os campos preenchidos da publicação.

Somente as informações preenchidas serão exibidas, ou seja, caso o campo esteja em branco no cadastro ele não será exibido.

Pode-se utilizar o campo de "**Pesquisa**" para localizar um detalhe especifico da publicação, conforme o exemplo abaixo:

Exemplares

Ao clicar na aba "**Exemplares**" serão exibidos por filial/unidade bibliotecária os exemplares cadastrados para a publicação.

Serão exibidos na "**Informações do exemplar**":

* Somente os campos que possuem informação preenchida no cadastro
* Os campos respeitarão as parametrizações definida em "**Biblioteca| Parâmetros/Configurações| Pesquisa| Pesquisa ao acervo| Visualização dos detalhes| campos exemplar**"

Outro ponto importante que destacamos, é que a exibição dos exemplares levara em consideração a regra do parâmetro "**Liberar circulação de exemplares bloqueados"** ou do parâmetro **"Permitir reserva e empréstimo de exemplares de circulação interna quando não existir mais nenhum outro exemplar disponível"**  disponíveis em**"Biblioteca| Parâmetros/Configurações| Movimentações| Empréstimo 2/2**". 

Portanto se o exemplar não estiver sendo apresentado é importante conferir o parâmetro citado acima e a opção "**Bloquear este exemplar para empréstimo consulta interna**"  no cadastro do exemplar.

A numeração apresentada representa o "**Exemplar**" da publicação.

Para visualizar informações do exemplar basta clicar no numero correspondente.

A informação destacada abaixo representa a quantidade de exemplares disponíveis no acervo e a quantidade de exemplares disponíveis para empréstimo.

Reservar - Publicação do acervo

Para realizar o processo de reserva de publicação de acervo (botão Reservar), deve-se conceder a permissão para o perfil do usuário, conforme mostra no tópico "Permissão" descrito acima.

Para realizar a reserva de um exemplar em uma unidade bibliotecária, a quantidade de exemplares disponível para empréstimo precisa ser igual a 0 (zero), pois o portal permite a reserva apenas quando não possui nenhum exemplar disponível para empréstimo.

A informação destacada (em laranja) representa que não será possível reservar devido a disponibilidade de um exemplar na filial/unidade "Matriz - CAMPUS".

Exemplares de consulta interna 1/2

Caso a publicação, possua um exemplar de consulta interna, este exemplar não irá constar como disponível para empréstimo  e o botão de reservar irá aparecer, porém, se o parâmetro **"Liberar circulação de exemplares bloqueados"** disponível no caminho TOTVS Gestão Bibliotecária → Parâmetros / Configurações →  Movimentação → Empréstimo → Empréstimo 2/2, estiver **marcado** então esse exemplar de consulta interna passará a constar como disponível para empréstimo e o botão de reservar não estará disponível.

Para consultar os parâmetros de movimentação onde contém o parâmetro informado acima, [clique aqui](https://tdn.totvs.com/x/7P1bGQ).

Exemplares de consulta interna - 2/2

Caso a publicação, possua um exemplar de consulta interna, este exemplar não irá constar como disponível para empréstimo  e o botão de reservar irá aparecer, porém, se o parâmetro **"Permitir reserva e empréstimo de exemplares de circulação interna quando não existir mais nenhum outro exemplar disponível"** disponível no caminho TOTVS Gestão Bibliotecária → Parâmetros / Configurações →  Movimentação → Empréstimo → Empréstimo 2/2, estiver **marcado** então esse exemplar de consulta interna passará a estar disponível para realizar empréstimo e o botão de reservar ficará visível quando não existir mais exemplar disponível. **Importante:**Ao marcar o parâmetro "**Liberar circulação de exemplares bloqueados**" o parâmetro "**Permitir reserva e empréstimo de exemplares de circulação interna quando não existir mais nenhum outro exemplar disponível**" ficará bloqueado. O mesmo acontecerá de modo inverso. Sendo assim, não é possível marcar os dois parâmetros ao mesmo tempo.

Para consultar os parâmetros de movimentação onde contém o parâmetro informado acima, [clique aqui](https://tdn.totvs.com/x/7P1bGQ).

Ao acionar o botão "**Reservar**" em uma unidade bibliotecária, será exibido uma nova janela com as informações:

* **Código da publicação**: *Código da publicação a ser reservada.*
* **Título da publicação**: *Título da publicação a ser reservada.*
* **Filial / Unidade**: *Filial e Unidade Bibliotecária da reserva a ser realizada.*
* **Reservar e listar reservas**: *Botão para realizar a reserva e direcionar para a funcionalidade de listagem de reservas.*
* **Reservar**: *Botão para realizar a reserva e continuar na funcionalidade de exemplares.*
* **Cancelar**: *Botão para cancelar a ação de reservar e retornar para a listagem de exemplares.*

Para disponibilizar os campos "**Volume, Edição e Ano**" na funcionalidade de reserva, a unidade bibliotecária necessita estar parametrizada no sistema, disponível em "**Educacional | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | 14 - Biblioteca | 14.04 - Movimentação | 14.04.04 - Reserva**":

Ao marcar os parâmetros acima, a funcionalidade de reserva passa a exibir/obrigar os campos no momento da reserva para a unidade bibliotecária parametrizada:

Ao acionar a opção de "Reservar", o usuário precisa ter acesso a unidade bibliotecária (**Educacional | Gestão Bibliotecária | Cadastros | Usuários | Aba Acesso por Unidades**), pois caso contrário será exibido uma nova janela sem as opções de efetivar a reserva, conforme mostra a figura abaixo:

Ficha CatalográficaMarc
