---
content_hash: fd17fd2470d700c852aebfce280f8efc404655f989823f9c9b3b0c9693ef0b9e
fetched_at: '2026-06-29T00:10:19.206685+00:00'
page_id: '4813120'
product: rm
source: tdn-rm
title: RSS - Movimentos que necessitam de aprovação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813120
version: 6
---

BLOCK

RSS - Movimentos que necessitam de aprovação

FAQ: **RSS - Movimentos que necessitam de aprovação**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para utilizar Canais RSS para validar os movimentos que necessitam de aprovação?

* ***Descrição do Processo***

Tem por finalidade envio de email ao usuário vinculado a um Feed do Outloolk automaticamente sempre que a rotina de Canal RSS retornar alguma informação, ou seja, quando a execução da consulta SQL, informada na inclusão do Canal RSS, apresentar algum resultado.

É necessário que haja um critério para configuração do Canal RSS, visto que, ao utilizar uma consulta SQL mais complexa a performance do sistema pode ficar comprometida.

O RSS será disparado automaticamente obedecendo configuração do tempo de atualização definido o sistema, sempre que a consulta SQL retornar alguma informação.

Importante:

- Para utilização do RSS é necessário que o cliente possua o “RM PORTAL” instalado e que a versão do “Outlook” seja 2007.

- Para configurar o RSS o usuário deverá acessar o aplicativo através da **Nova MDI**.

- Todo processo de assinatura, inclusão e publicação de RSS será feito considerando perfil parametrizado para este fim. Neste caso específico será considerado perfil “mestre” para fazer parametrização do processo.

Solução

* ***Parametrizações Necessárias***

Acessar diretório **| CORPORERM\RM.NET |** e clicar no ícone [![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmMZEAqSI/AAAAAAAABt4/WrFT0oGP388/clip_image002_thumb.jpg?imgmax=800 "clip_image002")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmLo1_9RI/AAAAAAAABt0/aEX6U6olafQ/s1600-h/clip_image002%5B3%5D.jpg) | para acessar Nova MDI. A seguir clicar no ícone | [![clip_image004](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmNgDcM7I/AAAAAAAABuA/7WR8LNhn4TA/clip_image004_thumb.jpg?imgmax=800 "clip_image004")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmM9RsG3I/AAAAAAAABt8/-ako9DV4m2k/s1600-h/clip_image004%5B3%5D.jpg) | e escolher opção **| Serviços Globais |**

Na sequência acessar menu **| Administração | Parâmetros Gerais |** na aba | **Gerais |** e informar:

- Porta para envio de mensagens: definido pelo cliente

- URL de acesso ao Portal RM: colocar endereço de acesso ao portal

\*\*Neste exemplo específico será considerado endereço | [http://RM0005369/CORPORE1080](http://rm0005369/CORPORE1080) |

Acessar o menu **| Gestão | Visões de Dados |** **Inserir |** e cadastrar Consulta SQL que será considerada para geração deste RSS com o conteúdo:

SELECT T.CODTMV,T.NUMEROMOV, T.DATAEMISSAO, T.CODUSUARIO, T.VALORLIQUIDO, T.CODUSUARIO, T.IDMOV FROM TMOV T, TITMTMV TT

WHERE T.CODCOLIGADA=TT.CODCOLIGADA

AND T.CODTMV=TT.CODTMV

AND TT.USARAPROVACAO='1'

AND TT.CODTMV LIKE ('1.1%')

AND T.IDMOV NOT IN (SELECT IDMOV FROM TMOVAPROVA)

AND T.CODCOLIGADA = '1'

AND T.DATAEMISSAO >= '2010-01-01'

Importante:

- A consulta em questão retorna os itens de contrato com vencimento nos próximos 30 dias considerando a data do sistema.

- Na inclusão da consulta deve ser marcada opção **| ( x ) Disponível para o RM Portal |**, caso contrário a consulta não será apresentada para seleção.

Acessar menu **| Gestão |** e clicar no ícone |**[![clip_image006](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtmO-mhIGI/AAAAAAAABuI/yR6nFpIYwy4/clip_image006_thumb.jpg?imgmax=800 "clip_image006")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmOMLPI6I/AAAAAAAABuE/tHa_owJsVf0/s1600-h/clip_image006%5B3%5D.jpg)** **|** para configurar o tempo de atualização dos dados onde deve informar:

- Tempo de Atualização(min): tempo em minutos para atualização dos dados

- Tempo de exibição do aviso (seg): tempo em segundos para exibição de avisos

Proxy

- Endereço: endereço do servidor de email

- Porta: porta de acesso ao servidor

Ainda neste menu, acessar o ícone | [![clip_image008](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmQYHGqUI/AAAAAAAABuQ/QLDdeVqHyPI/clip_image008_thumb.jpg?imgmax=800 "clip_image008")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmPgugVMI/AAAAAAAABuM/uZHeIyKsJMI/s1600-h/clip_image008%5B3%5D.jpg) | e escolher opção **| Incluir |** para cadastrar e configurar o RSS.

Ao escolher opção “Incluir RSS” serão apresentadas abas com parametrizações específicas para geração do RSS, onde deve ser informado:

**Aba – Identificação**

Preencher Título, Descrição e caminho URL a ser utilizado. Ao salvar esta informação o campo **| Copie a URL abaixo para assinar o Canal |** será preenchido e este caminho será considerado para gerar os convites e emails de RSS.

**Aba – Permissões**

Clicar no ícone **| Incluir |** e selecionar o perfil a ser utilizado para receber as mensagens de RSS. Todos os usuários vinculados a este perfil receberão convite para participar do RSS e ao aceitar, o mesmo receberá emails com conteúdo parametrizado para este RSS.

**Aba – Fontes**

Clicar no ícone **| Incluir |** e preencher todos os campos apresentados. A informação em questão será considerada para composição e geração dos dados do RSS.

**- Consulta SQL do Alerta:** campo de preenchimento obrigatório, onde o usuário tem que referenciar a consulta SQL inclusa anteriormente, onde o resultado apresentado vai determinar o disparo do RSS.

[![clip_image012](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmSKWjWYI/AAAAAAAABuY/KeFG42O03nI/clip_image012_thumb%5B1%5D.jpg?imgmax=800 "clip_image012")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtmRZXDXXI/AAAAAAAABuU/xxw0_At_35Y/s1600-h/clip_image012%5B4%5D.jpg)

O usuário deve clicar em [![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmTY0YAyI/AAAAAAAABug/NSvNjTBFrSg/clip_image002_thumb.gif?imgmax=800 "clip_image002")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmSv-oOQI/AAAAAAAABuc/TW0kZsx7D6E/s1600-h/clip_image002%5B3%5D.gif) e escolher a sentença SQL inclusa anteriormente no aplicativo para este fim. Esta consulta vai selecionar os movimentos que se adequam ao resultado da consulta para geração do RSS.

Se a consulta em questão utilizar parâmetros o usuário deverá clicar na opção **| Parâmetros |** para definição dos mesmos

**- Identificador Único**: Este campo será apresentado para manutenção depois que as outras informações forem preenchidas, visto que, através do mesmo o usuário vai determinar quais campos chaves da base devem ser considerados para disparar o RSS. Para isto deverá clicar na opção **| Selecionar |** onde serão apresentados campos referenciados na Consulta SQL.

[![clip_image014](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmU5QozyI/AAAAAAAABuo/8piB2GP1GLc/clip_image014_thumb%5B1%5D.jpg?imgmax=800 "clip_image014")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmUKYjqtI/AAAAAAAABuk/sJA_d8w856M/s1600-h/clip_image014%5B4%5D.jpg)

Neste exemplo especifico serão selecionados campos **| CODTMV – NUMEROMOV – DATAEMISSAO – CODUSUARIO- IDMOV |** que serão referenciados na “Descrição” para compor o conteúdo do RSS a ser enviado ao usuário.

[![clip_image016](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmWSYsjJI/AAAAAAAABuw/jUxiYWsXf4k/clip_image016_thumb.jpg?imgmax=800 "clip_image016")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmVurNGQI/AAAAAAAABus/GSJGNkbBorw/s1600-h/clip_image016%5B3%5D.jpg)

[![clip_image018](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmXguIMzI/AAAAAAAABu4/EwDPHqXlF1s/clip_image018_thumb.jpg?imgmax=800 "clip_image018")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmW16Y7eI/AAAAAAAABu0/3R2JLSr5BDI/s1600-h/clip_image018%5B3%5D.jpg)

**- Título:** Campo de preenchimento obrigatório onde deve ser informada identificação do RSS para o Feed a ser enviado. Será definido título a ser apresentado no RSS onde o usuário tem opção de vincular o mesmo a um parâmetro que será preenchido ao clicar no ícone | **Parâmetros |**

[![clip_image020](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtmY1zhegI/AAAAAAAABvA/u3y3_W7ldes/clip_image020_thumb.jpg?imgmax=800 "clip_image020")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtmYlGSvXI/AAAAAAAABu8/b9qaJw4dF4s/s1600-h/clip_image020%5B3%5D.jpg)

**- Descrição:** Campo de preenchimento obrigatório onde deve ser informada descrição do processo a ser enviado para o usuário através do RSS. No campo em questão poderá buscar os dados que retornam na consulta SQL através de { }.

O vínculo entre este campo e o resultado da consulta será feito ao clicar no ícone **| Parâmetros |**. Ao informar **<b>** o conteúdo preenchido a partir do mesmo será apresentado em “negrito”, já a opção **</b>** determina que o texto deixará de ser apresentado em “negrito” e voltará a ser apresentado normal.

Estes dados se referem a linha de programação **HTML** não sendo de responsabilidade da TOTVS a definição ou utilização dos mesmos.

*[![clip_image022](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmab2JdbI/AAAAAAAABvI/Lx_idjPaCaQ/clip_image022_thumb%5B1%5D.jpg?imgmax=800 "clip_image022")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmZuE1y2I/AAAAAAAABvE/0kccGPCqapA/s1600-h/clip_image022%5B4%5D.jpg)*

Cada informação apresentada em **| {} |** se refere ao conteúdo referenciado na Consulta SQL. Para vincular os dados deverá clicar no ícone | [![clip_image024](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmbkPv6_I/AAAAAAAABvQ/c6pGHpyUEhQ/clip_image024_thumb.jpg?imgmax=800 "clip_image024")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmbO0a7NI/AAAAAAAABvM/0566UG7yV70/s1600-h/clip_image024%5B3%5D.jpg) | onde será apresentada coluna **| PARAM |** com os campos referenciados na descrição, a partir daí, o usuário deverá preencher na coluna **| ORIGEM |** para vincular ao parâmetro utilizado.

**[![clip_image026](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmdQysrxI/AAAAAAAABvY/farrQ_rzAKA/clip_image026_thumb.jpg?imgmax=800 "clip_image026")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtmcteWK9I/AAAAAAAABvU/mEMTPU3dMcw/s1600-h/clip_image026%5B3%5D.jpg)**

Neste exemplo específico os dados são:

0 – Código do usuário

1 – Número do movimento

2 – Código do tipo de movimento

3 – Identificador do movimento

4 – Data de emissão do movimento

**- Fonte de Leitura**

**Tipo de Leitura (SQL\URL):** Este campo define o tipo de retorno do RSS podendo ser através de consulta SQL ou através de uma URL que fará o direcionamento á tela do Corpore.NET.

O endereço da URL é gravado na aba **| Identificação |** no campo **| Copie a URL abaixo para assinar o canal |**

[![clip_image028](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtmegcWbWI/AAAAAAAABvg/hBTnNbEwptg/clip_image028_thumb%5B1%5D.jpg?imgmax=800 "clip_image028")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmdxdjLkI/AAAAAAAABvc/fegW347SJU8/s1600-h/clip_image028%5B4%5D.jpg)

Nos campos em questão também podem ser passados parâmetros para obter resultado esperado.

Tela Configurada

[![clip_image030](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmiKJRG7I/AAAAAAAABvo/X-fYpaIoliw/clip_image030_thumb%5B1%5D.jpg?imgmax=800 "clip_image030")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmg9fOY4I/AAAAAAAABvk/Cocg3LZ4JYI/s1600-h/clip_image030%5B4%5D.jpg)

* ***Publicação de Convite de Canal RSS***

Depois de feitas parametrizações anteriores, o Canal RSS estará pronto para ser assinado e enviado convite para o funcionário fazer as configurações do Feeds.

Para isto é necessário selecionar o canal e clicar em **| Processo | Publicar Canal RSS |** onde será enviado convite para todos usuários vinculados ao perfil parametrizado. Nessa tela é permitido alterar o assunto e o corpo do e-mail.

[![clip_image032](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmjga_RXI/AAAAAAAABvw/KtUDOEyZtZc/clip_image032_thumb%5B1%5D.jpg?imgmax=800 "clip_image032")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmi3n-kNI/AAAAAAAABvs/tPspKEihWnU/s1600-h/clip_image032%5B4%5D.jpg)

[![clip_image034](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmlTsW6wI/AAAAAAAABv4/UV_CifQ-OLI/clip_image034_thumb%5B1%5D.jpg?imgmax=800 "clip_image034")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmkfjltpI/AAAAAAAABv0/BloRA0g8MOM/s1600-h/clip_image034%5B4%5D.jpg)

* ***Criação de RSS Feeds no Outook***

Ao publicar o Canal RSS será enviado email para o usuário com convite, onde o mesmo deverá copiar o caminho referenciado no RSS e fazer a criação do mesmo.

[![clip_image036](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmm0An18I/AAAAAAAABwA/ffXQ1lQtLfI/clip_image036_thumb.jpg?imgmax=800 "clip_image036")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmmCVRDsI/AAAAAAAABv8/JRo3DJEu5Zk/s1600-h/clip_image036%5B3%5D.jpg)

De posse desta informação, deve acessar o Outlook em **| RSS |** clicar com botão direito do mouse e escolher opção **| Adicionar Novo RSS Feed |**. A seguir colar caminho informado no email que recebeu com “convite” para assinatura do canal e clicar no ícone **| Adicionar |**.

[![clip_image038](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtmons-l3I/AAAAAAAABwI/oUB6Fewl1N4/clip_image038_thumb%5B1%5D.jpg?imgmax=800 "clip_image038")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtmn89c6rI/AAAAAAAABwE/TCpkPvmFlsQ/s1600-h/clip_image038%5B4%5D.jpg)

Depois de feito isto clicar no ícone **| Avançado |** e infomar:

[![clip_image040](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtmq5_zQQI/AAAAAAAABwQ/iUf9L256uAA/clip_image040_thumb%5B1%5D.jpg?imgmax=800 "clip_image040")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtmqEUN8yI/AAAAAAAABwM/8msjffBhjkU/s1600-h/clip_image040%5B4%5D.jpg)

- Aba Geral: preencher descrição desejada para o Canal RSS

- Aba Downloads: habilitar campos | Baixar Automaticamente os Anexos neste feed - Baixar o artigo inteiro como um anexo .html para cada um |

A seguir clicar em | OK | para confirmar o processo.

Para assinar o RSS no Outlook 2007 deve-se inserir o usuário e senha do RM Portal se for pedido. Sempre que a consulta SQL referenciada na inclusão do Canal RSS retornar alguma informação será transformada em um *Feed* que é enviado para o Outlook. Para cada *Feed* será enviado email para o usuário que aceitou o convite.

[![clip_image042](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtmtCH8zyI/AAAAAAAABwY/IxljFURr6bI/clip_image042_thumb%5B1%5D.jpg?imgmax=800 "clip_image042")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtmr801o0I/AAAAAAAABwU/e2boNtgqP5g/s1600-h/clip_image042%5B4%5D.jpg)

Para maiores informações:

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
