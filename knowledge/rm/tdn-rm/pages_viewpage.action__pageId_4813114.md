---
content_hash: bdbe3077b444a9a2762b66869b6d2199db3376a92e25703af4e1ccc0fb281951
fetched_at: '2026-06-29T00:10:19.194707+00:00'
page_id: '4813114'
product: rm
source: tdn-rm
title: RSS - Contratos a vencer nos próximos 30 dias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813114
version: 6
---

BLOCK

RSS - Contratos a vencer nos próximos 30 dias

FAQ: **RSS - Contratos a vencer nos próximos 30 dias**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para utilizar Canais RSS para validar os contratos a vencer nos próximos 30 dias?

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

Acessar diretório **| CORPORERM\RM.NET |** e clicar no ícone [![clip_image002](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgVn829uI/AAAAAAAABrQ/JD7-_DifQEc/clip_image002_thumb.jpg?imgmax=800 "clip_image002")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgVOUQ8mI/AAAAAAAABrM/f9KFZgCSoUA/s1600-h/clip_image002%5B3%5D.jpg) | para acessar Nova MDI. A seguir clicar no ícone | [![clip_image004](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtgXQoJKbI/AAAAAAAABrY/XPTEM86U5v0/clip_image004_thumb.jpg?imgmax=800 "clip_image004")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgWuT2yfI/AAAAAAAABrU/82C0B-FLacE/s1600-h/clip_image004%5B3%5D.jpg) | e escolher opção **| Serviços Globais |**

Na sequência acessar menu **| Administração | Parâmetros Gerais |** na aba | **Gerais |** e informar:

- Porta para envio de mensagens: definido pelo cliente

- URL de acesso ao Portal RM: colocar endereço de acesso ao portal

\*\*Neste exemplo específico será considerado endereço | [http://RM0005369/CORPORE1080](http://rm0005369/CORPORE1080) |

Acessar o menu **| Gestão | Visões de Dados |** **Inserir |** e cadastrar Consulta SQL que será considerada para geração deste RSS com o conteúdo:

SELECT T.CODIGOCONTRATO, T.CODFILIAL, T.CODCFO, I.NUMEROSEQUENCIAL, I.EPERIODICO, I.DATAINICIO, I.DATAFIM, I.VALORTOTAL, I.CODFILIALFAT, I.CODTMV, I.CODVEN1 FROM TCNT T,TITMCNT I

WHERE T.CODCOLIGADA = I.CODCOLIGADA

AND T.IDCNT = I.IDCNT

AND DATEADD(DAY,-30,I.DATAFIM)<GETDATE()

AND I.DATAFIM>GETDATE()

ORDER BY I.DATAFIM DESC

Importante:

- A consulta em questão retorna os itens de contrato com vencimento nos próximos 30 dias considerando a data do sistema.

- Na inclusão da consulta deve ser marcada opção **| ( x ) Disponível para o RM Portal |**, caso contrário a consulta não será apresentada para seleção.

Acessar menu **| Gestão |** e clicar no ícone |**[![clip_image006](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtgZRYSKnI/AAAAAAAABrg/K1kEI84jxJc/clip_image006_thumb.jpg?imgmax=800 "clip_image006")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgYqsuZ4I/AAAAAAAABrc/U1lRkuJvH6M/s1600-h/clip_image006%5B3%5D.jpg)** **|** para configurar o tempo de atualização dos dados onde deve informar:

- Tempo de Atualização(min): tempo em minutos para atualização dos dados

- Tempo de exibição do aviso (seg): tempo em segundos para exibição de avisos

Proxy

- Endereço: endereço do servidor de email

- Porta: porta de acesso ao servidor

Ainda neste menu, acessar o ícone | [![clip_image008](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtga1LCACI/AAAAAAAABro/1HJtBTn1dEw/clip_image008_thumb.jpg?imgmax=800 "clip_image008")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtgaBXV33I/AAAAAAAABrk/vijIH-VrFyM/s1600-h/clip_image008%5B3%5D.jpg) | e escolher opção **| Incluir |** para cadastrar e configurar o RSS.

Ao escolher opção “Incluir RSS” serão apresentadas abas com parametrizações específicas para geração do RSS, onde deve ser informado:

**Aba – Identificação**

Preencher Título, Descrição e caminho URL a ser utilizado. Ao salvar esta informação o campo **| Copie a URL abaixo para assinar o Canal |** será preenchido e este caminho será considerado para gerar os convites e emails de RSS.

**Aba – PermissÕes**

Clicar no ícone **| Incluir |** e selecionar o perfil a ser utilizado para receber as mensagens de RSS. Todos os usuários vinculados a este perfil receberão convite para participar do RSS e ao aceitar, o mesmo receberá emails com conteúdo parametrizado para este RSS.

**ABA – FONTES**

Clicar no ícone **| Incluir |** e preencher todos os campos apresentados. A informação em questão será considerada para composição e geração dos dados do RSS.

**- Consulta SQL do Alerta:** campo de preenchimento obrigatório, onde o usuário tem que referenciar a consulta SQL inclusa anteriormente, onde o resultado apresentado vai determinar o disparo do RSS.

[![clip_image012](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtgedmWLoI/AAAAAAAABrw/VzPjirFJfv8/clip_image012_thumb%5B2%5D.jpg?imgmax=800 "clip_image012")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtgdz-_a9I/AAAAAAAABrs/NUdkBfrFiyo/s1600-h/clip_image012%5B5%5D.jpg)

O usuário deve clicar em [![clip_image002](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtggPbm2fI/AAAAAAAABr4/aNM3DgJYgHI/clip_image002_thumb.gif?imgmax=800 "clip_image002")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgfalH8II/AAAAAAAABr0/8QwRFybTAkI/s1600-h/clip_image002%5B3%5D.gif) e escolher a sentença SQL inclusa anteriormente no aplicativo para este fim. Esta consulta vai selecionar os movimentos que se adequam ao resultado da consulta para geração do RSS.

Se a consulta em questão utilizar parâmetros o usuário deverá clicar na opção **| Parâmetros |** para definição dos mesmos

**- Identificador Único**: Este campo será apresentado para manutenção depois que as outras informações forem preenchidas, visto que, através do mesmo o usuário vai determinar quais campos chaves da base devem ser considerados para disparar o RSS. Para isto deverá clicar na opção **| Selecionar |** onde serão apresentados campos referenciados na Consulta SQL.

[![clip_image014](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgiLaU-NI/AAAAAAAABsA/BhkkTzzMxjk/clip_image014_thumb%5B1%5D.jpg?imgmax=800 "clip_image014")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtggwXq2II/AAAAAAAABr8/NfZdhYe8eZ4/s1600-h/clip_image014%5B4%5D.jpg)

Neste exemplo especifico serão selecionados campos **| CODIGOCONTRATO – CODFILIAL – NUMEROSEQUENCIAL – DATAFIM – VALORTOTAL |** que serão referenciados na “Descrição” para compor o conteúdo do RSS a ser enviado ao usuário.

[![clip_image016](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgjsWKBaI/AAAAAAAABsI/nuTVAmxdEUE/clip_image016_thumb%5B2%5D.jpg?imgmax=800 "clip_image016")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgi3D9T7I/AAAAAAAABsE/SjNYjULB08w/s1600-h/clip_image016%5B5%5D.jpg)

[![clip_image018](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtgk-w29XI/AAAAAAAABsQ/pwlx59dLSsc/clip_image018_thumb%5B1%5D.jpg?imgmax=800 "clip_image018")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtgkC3JhtI/AAAAAAAABsM/JiEBINdl3jI/s1600-h/clip_image018%5B4%5D.jpg)

**- Título:** Campo de preenchimento obrigatório onde deve ser informada identificação do RSS para o Feed a ser enviado. Será definido título a ser apresentado no RSS onde o usuário tem opção de vincular o mesmo a um parâmetro que será preenchido ao clicar no ícone | **Parâmetros |**

[![clip_image020](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgmPMIfSI/AAAAAAAABsY/3j8H-cNpbPU/clip_image020_thumb%5B1%5D.jpg?imgmax=800 "clip_image020")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtglclGbCI/AAAAAAAABsU/0JKnyH_kinE/s1600-h/clip_image020%5B4%5D.jpg)

**- Descrição:** Campo de preenchimento obrigatório onde deve ser informada descrição do processo a ser enviado para o usuário através do RSS. No campo em questão poderá buscar os dados que retornam na consulta SQL através de { }.

O vínculo entre este campo e o resultado da consulta será feito ao clicar no ícone **| Parâmetros |**. Ao informar **<b>** o conteúdo preenchido a partir do mesmo será apresentado em “negrito”, já a opção **</b>** determina que o texto deixará de ser apresentado em “negrito” e voltará a ser apresentado normal.

Estes dados se referem a linha de programação **HTML** não sendo de responsabilidade da TOTVS a definição ou utilização dos mesmos.

*[![clip_image022](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtgpNqPFZI/AAAAAAAABsg/2Y9jmMhxq70/clip_image022_thumb%5B1%5D.jpg?imgmax=800 "clip_image022")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtgoL3T94I/AAAAAAAABsc/CdP6rNiBPmw/s1600-h/clip_image022%5B4%5D.jpg)*

Cada informação apresentada em **| {} |** se refere ao conteúdo referenciado na Consulta SQL. Para vincular os dados deverá clicar no ícone | [![clip_image024](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtgqW39oXI/AAAAAAAABso/9V-0l7c7fEI/clip_image024_thumb.jpg?imgmax=800 "clip_image024")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtgp3CNIpI/AAAAAAAABsk/KWQ6e0fX9IE/s1600-h/clip_image024%5B3%5D.jpg) | onde será apresentada coluna **| PARAM |** com os campos referenciados na descrição, a partir daí, o usuário deverá preencher na coluna **| ORIGEM |** para vincular ao parâmetro utilizado.

**[![clip_image026](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtgtNAt_MI/AAAAAAAABsw/Dki_TFXy3KA/clip_image026_thumb%5B2%5D.jpg?imgmax=800 "clip_image026")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtgsO8PPEI/AAAAAAAABss/WoVshXit_HU/s1600-h/clip_image026%5B5%5D.jpg)**

Neste exemplo específico os dados são:

0 – Número sequencial do item

1 – Código do contrato

2 – Valor do item de Contrato

3 – Filial do contrato

4 – Data fim do contrato

**- Fonte de Leitura**

**Tipo de Leitura (SQL\URL):** Este campo define o tipo de retorno do RSS podendo ser através de consulta SQL ou através de uma URL que fará o direcionamento á tela do Corpore.NET.

O endereço da URL é gravado na aba **| Identificação |** no campo **| Copie a URL abaixo para assinar o canal |**

[![clip_image028](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtgvvCRaoI/AAAAAAAABs4/j-qJJljMwDw/clip_image028_thumb%5B1%5D.jpg?imgmax=800 "clip_image028")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtguzWQcNI/AAAAAAAABs0/0ubIvgTIyH4/s1600-h/clip_image028%5B4%5D.jpg)

Nos campos em questão também podem ser passados parâmetros para obter resultado esperado.

Tela Configurada:

[![clip_image030](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtgzUeuieI/AAAAAAAABtA/FEMupThv_Es/clip_image030_thumb%5B1%5D.jpg?imgmax=800 "clip_image030")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtgx1vTDMI/AAAAAAAABs8/xLhIym73NUI/s1600-h/clip_image030%5B4%5D.jpg)

* ***Publicação de Convite de Canal RSS***

Depois de feitas parametrizações anteriores, o Canal RSS estará pronto para ser assinado e enviado convite para o funcionário fazer as configurações do Feeds.

Para isto é necessário selecionar o canal e clicar em **| Processo | Publicar Canal RSS |** onde será enviado convite aos usuários vinculados ao perfil parametrizado. Nessa tela é permitido alterar o assunto e o corpo do e-mail.

[![clip_image032](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtg1-hqj5I/AAAAAAAABtI/viv44vhKTFM/clip_image032_thumb%5B1%5D.jpg?imgmax=800 "clip_image032")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtg08R57VI/AAAAAAAABtE/dpQclFiNTFs/s1600-h/clip_image032%5B4%5D.jpg)

[![clip_image034](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtg54LrWuI/AAAAAAAABtQ/skr4EX89mWk/clip_image034_thumb%5B1%5D.jpg?imgmax=800 "clip_image034")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtg4kDWKdI/AAAAAAAABtM/rqacpYXQ0o4/s1600-h/clip_image034%5B4%5D.jpg)

* ***Criação de RSS Feeds no Outook***

Ao publicar o Canal RSS será enviado email ao usuário com convite de assinatura do RSS, onde o mesmo deverá copiar o caminho referenciado.

[![clip_image036](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtg8KS3JQI/AAAAAAAABtY/it7ljXQEFOc/clip_image036_thumb%5B2%5D.jpg?imgmax=800 "clip_image036")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtg7TabziI/AAAAAAAABtU/zyp7pA3LFcY/s1600-h/clip_image036%5B5%5D.jpg)

De posse desta informação, deve acessar o Outlook em **| RSS |** clicar com botão direito do mouse e escolher opção **| Adicionar Novo RSS Feed |**. A seguir colar caminho informado no email que recebeu com “convite” para assinatura do canal e clicar no ícone **| Adicionar |**.

[![clip_image038](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtg9syTANI/AAAAAAAABtg/nKQ0m5zXlck/clip_image038_thumb%5B1%5D.jpg?imgmax=800 "clip_image038")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtg8-Qa93I/AAAAAAAABtc/VpZh-TtH5rE/s1600-h/clip_image038%5B4%5D.jpg)

Depois de feito isto clicar no ícone **| Avançado |** e infomar:

[![clip_image040](http://lh4.ggpht.com/_G7KXZLoZDsY/TKthAG60PFI/AAAAAAAABto/mt2rMN8Sssg/clip_image040_thumb.jpg?imgmax=800 "clip_image040")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtg-4uIPMI/AAAAAAAABtk/X98vEEpUjmo/s1600-h/clip_image040%5B3%5D.jpg)

- Aba Geral: preencher descrição desejada para o Canal RSS

- Aba Downloads: habilitar campos | Baixar Automaticamente os Anexos neste feed - Baixar o artigo inteiro como um anexo .html para cada um |

A seguir clicar em | OK | para confirmar o processo.

Para assinar o RSS no Outlook 2007 deve-se inserir o usuário e senha do RM Portal se for pedido. Sempre que a consulta SQL referenciada na inclusão do Canal RSS retornar alguma informação será transformada em um *Feed* que é enviado para o Outlook. Para cada *Feed* será enviado email para o usuário que aceitou o convite.

[![clip_image042](http://lh4.ggpht.com/_G7KXZLoZDsY/TKthGinOFhI/AAAAAAAABtw/SntGrfsydq0/clip_image042_thumb%5B1%5D.jpg?imgmax=800 "clip_image042")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKthEMwZLPI/AAAAAAAABts/eUbEWItlUQI/s1600-h/clip_image042%5B4%5D.jpg)

Para maiores informações:

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
