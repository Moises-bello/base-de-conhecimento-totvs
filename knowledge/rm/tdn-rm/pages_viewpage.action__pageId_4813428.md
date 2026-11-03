---
content_hash: b161447eb41f4321a2b55908d63d2b73f6d82523ca416f9d707ded6a1102bf47
fetched_at: '2026-06-29T00:10:19.336460+00:00'
page_id: '4813428'
product: rm
source: tdn-rm
title: RSS – NF de remessa com prazo de retorno próximo ao vencimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813428
version: 5
---

BLOCK

RSS – NF de remessa com prazo de retorno próximo ao vencimento

FAQ: **RSS – NF de remessa com prazo de retorno próximo ao vencimento**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

***Como Fazer***

Como parametrizar o sistema para utilizar Canais RSS para verificar quais notas fiscais de remessa ainda não foram retornadas e o prazo para regularização.

**Obs.:** Por lei, as saídas de mercadorias a títulos de remessas possuem suspensão de ICMS quando as mesmas retornam em até 180 dias.

Solução

***Descrição do Processo***

Tem por finalidade envio de email ao usuário vinculado a um Feed do Outloolk automaticamente sempre que a rotina de Canal RSS retornar alguma informação, ou seja, quando a execução da consulta SQL, informada na inclusão do Canal RSS, apresentar algum resultado.

É necessário que haja um critério para configuração do Canal RSS, visto que, ao utilizar uma consulta SQL mais complexa o desempenho do sistema pode ficar comprometido.

O RSS será disparado automaticamente obedecendo à configuração do tempo de atualização definido no sistema, sempre que a consulta SQL retornar alguma informação.

Importante:

- Para utilização do RSS é necessário que o cliente possua o “RM PORTAL” instalado e que a versão do “Outlook” seja 2007 ou posterior.

- Todo processo de assinatura, inclusão e publicação de RSS será feito considerando perfil parametrizado para este fim. Neste caso específico será considerado perfil “mestre” para fazer parametrização do processo.

***Parametrizações Necessárias***

Acessar diretório **| CORPORERM\RM.NET |** e clicar no ícone |[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI8QqN-BYI/AAAAAAAAEoU/vHu-zc8T-n8/image_thumb.png?imgmax=800 "image")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI8P5PK5aI/AAAAAAAAEoQ/_arluPnZ-KQ/s1600-h/image%5B2%5D.png) | para acessar pela MDI. A seguir clicar no ícone |[![image](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI8SY1JlDI/AAAAAAAAEoc/KC_9Tj2D7fA/image_thumb%5B1%5D.png?imgmax=800 "image")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI8RbQb7xI/AAAAAAAAEoY/YfsHn4_v1ZU/s1600-h/image%5B5%5D.png) | e escolher opção **| Serviços Globais |**

Na seqüência acessar menu **| Ambiente | Parâmetros Gerais | Globais |** onde deve acessar aba | **Gerais |** e informar:

- Porta para envio de mensagens: definido pelo cliente

- URL de acesso ao Portal RM: colocar endereço de acesso ao portal

\*\*Neste exemplo específico será considerado endereço | [http://RM0004068/CORPORE1120](http://rm0004068/CORPORE1120)|

Acessar o menu **| Gestão | Visões de Dados |** **Inserir |** e cadastrar Consulta SQL que será considerada para geração deste RSS com o conteúdo:

SELECT DISTINCT(TMOV.NUMEROMOV), CONVERT(VARCHAR, TMOV.DATAEMISSAO, 103) AS DATAEMISSAO, CONVERT(VARCHAR, (TMOV.DATAEMISSAO + 180),103) AS DATA\_LIMITE\_DE\_RETORNO,

DATEDIFF(DAY, GETDATE(),(TMOV.DATAEMISSAO + 180)) AS PRAZO\_PARA\_REGULARIZAÇÃO

FROM TITMMOV (NOLOCK),

(SELECT TITMMOV.IDMOV, TITMMOV.NSEQITMMOV, TITMMOV.CODCOLIGADA, TITMMOV.IDPRD FROM TITMMOV

LEFT JOIN TITMMOVRELAC

ON TITMMOV.IDMOV = TITMMOVRELAC.IDMOVORIGEM

AND TITMMOV.CODCOLIGADA = TITMMOVRELAC.CODCOLORIGEM

AND TITMMOV.NSEQITMMOV = TITMMOVRELAC.NSEQITMMOVORIGEM

WHERE TITMMOV.CODCOLIGADA IS NOT NULL

AND TITMMOV.IDMOV IS NOT NULL

AND TITMMOVRELAC.CODCOLORIGEM IS NULL

AND TITMMOVRELAC.IDMOVORIGEM IS NULL ) R

INNER JOIN TMOV

ON R.CODCOLIGADA = TMOV.CODCOLIGADA

AND R.IDMOV = TMOV.IDMOV

AND TMOV.STATUS <> 'C'

INNER JOIN TPRD

ON R.IDPRD = TPRD.IDPRD

AND R.CODCOLIGADA = TPRD.CODCOLIGADA

INNER JOIN TTMVEXT

ON TTMVEXT.CODTMV = TMOV.CODTMV

AND TTMVEXT.CODCOLIGADA = TMOV.CODCOLIGADA

AND (TTMVEXT.CONTROLETERCEIROS = 1

OR TTMVEXT.CONTROLETERCEIROS = 2

OR TTMVEXT.CONTROLETERCEIROS = 6)

AND TTMVEXT.CODTMV LIKE '2.%'

GROUP BY TMOV.NUMEROMOV,TMOV.DATAEMISSAO

HAVING DATEDIFF(DAY, GETDATE() , (TMOV.DATAEMISSAO + 180)) < 30

AND DATEDIFF(DAY, GETDATE() , (TMOV.DATAEMISSAO + 180)) > 0

ORDER BY TMOV.PRAZO\_PARA\_REGULARIZAÇÃO

**Importante:**

- A consulta em questão retorna os movimentos de remessa que estão próximos (30 dias) do vencimento da data de suspensão de ICMS.

- Foram considerados na consulta como movimentos de Remessas, tipos de movimentos 2.2.XX parametrizados na etapa | **Estoque – Estoque** |, parâmetro | **Tipo Controle Estoque Terceiros** | como: Remessa/Entrada de Mercadoria, Remessa/Entrada para Industrialização, Remessa/Entrada para Consignação, que no banco de dados correspondem respectivamente a 1, 2 e 6.

- Na inclusão da consulta deve ser marcada opção **| ( x ) Disponível para o RM Portal |**, caso contrário a consulta não será apresentada para seleção.

Acessar menu **| Gestão |** e clicar no ícone |[![image](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI8UmP9UQI/AAAAAAAAEok/LeMwikDZPS0/image_thumb%5B2%5D.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI8TuYYZFI/AAAAAAAAEog/QBDv57JLs1U/s1600-h/image%5B8%5D.png) **|** para configurar o tempo de atualização dos dados onde deve informar:

- Tempo de Atualização(min): tempo em minutos para atualização dos dados

- Tempo de exibição do aviso (seg): tempo em segundos para exibição de avisos Proxy

- Endereço: endereço do servidor de email

- Porta: porta de acesso ao servidor

Ainda neste menu, acessar o ícone |[![image](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI8Wi4HDWI/AAAAAAAAEos/HpZ_dI44z1M/image_thumb%5B3%5D.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI8WD2KvoI/AAAAAAAAEoo/rr3_e_2xpfE/s1600-h/image%5B11%5D.png) | e escolher opção **| Incluir |** para cadastrar e configurar o RSS.

Ao escolher opção “Incluir RSS” serão apresentadas abas com parametrizações específicas para geração do RSS, onde deve ser informado:

**Aba – Identificação**

Preencher Título, Descrição e caminho URL a ser utilizado. Ao salvar esta informação o campo **| Copie a URL abaixo para assinar o Canal |** será preenchido e este caminho será considerado para gerar os convites e emails de RSS.

**Aba – PermissÕes**

Clicar no ícone **| Incluir |** e selecionar o perfil a ser utilizado para receber as mensagens de RSS. Todos os usuários vinculados a este perfil receberão convite para participar do RSS e ao aceitar, o mesmo receberá emails com conteúdo parametrizado para este RSS.

**ABA – FONTES**

Clicar no ícone **| Incluir |** e preencher todos os campos apresentados. A informação em questão será considerada para composição e geração dos dados do RSS.

**- Consulta SQL do Alerta:** campo de preenchimento obrigatório, onde o usuário tem que referenciar a consulta SQL inclusa anteriormente, onde o resultado apresentado vai determinar o disparo do RSS.

[![image](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI8YQg0EFI/AAAAAAAAFMY/qZMXD_l-ae0/image12_thumb.png?imgmax=800 "image")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI8Xu_2aiI/AAAAAAAAFMU/jRPaVZQ2I1M/s1600-h/image12%5B1%5D.png)

|  |
| --- |
| O usuário deve clicar em [image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI8YvqeBUI/AAAAAAAAEo4/1_CuZjR2mEA/s1600-h/image%5B17%5D.png) e escolher a sentença SQL inclusa anteriormente no aplicativo para este fim. Esta consulta vai selecionar os movimentos que se adéquam ao resultado da consulta para geração do RSS.  Se a consulta em questão utilizar parâmetros o usuário deverá clicar na opção **| Parâmetros |** para definição dos mesmos |

**- Identificador Único**: Este campo será apresentado para manutenção depois que as outras informações forem preenchidas, visto que, através do mesmo o usuário vai determinar quais campos chaves da base devem ser considerados para disparar o RSS. Para isto deverá clicar na opção **| Selecionar |** onde serão apresentados campos referenciados na Consulta SQL.

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI8Z95xh7I/AAAAAAAAFMk/ODh8DGkNuyc/image18_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI8ZY6iCeI/AAAAAAAAFMc/NQaEffs8ThY/s1600-h/image18%5B1%5D.png)

Neste exemplo especifico serão selecionados campos **| NUMEROMOV – DATAEMISSAO – DATA\_LIMITE\_DE\_RETORNO – PRAZO\_PARA\_REGULARIZAÇÃO |** que serão referenciados na “Descrição” para compor o conteúdo do RSS a ser enviado ao usuário.

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI8bJMMQ4I/AAAAAAAAFM8/e3krrPkuvv0/image21_thumb%5B1%5D.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI8alS4TyI/AAAAAAAAFMw/s-pPXdTPdf8/s1600-h/image21%5B2%5D.png)

**- Título:** Campo de preenchimento obrigatório onde deve ser informada identificação do RSS para o Feed a ser enviado. Será definido título a ser apresentado no RSS onde o usuário tem opção de vincular o mesmo a um parâmetro que será preenchido ao clicar no ícone | **Parâmetros |**

[![image](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI8cL1rHfI/AAAAAAAAFNM/AiSy_A8Uog4/image24_thumb.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI8bgcknOI/AAAAAAAAFNA/b_ZidfrA1YM/s1600-h/image24%5B1%5D.png)

**- Descrição:** Campo de preenchimento obrigatório onde deve ser informada descrição do processo a ser enviado para o usuário através do RSS. No campo em questão poderá buscar os dados que retornam na consulta SQL através de { }.

O vínculo entre este campo e o resultado da consulta será feito ao clicar no ícone **| Parâmetros |**. Ao informar **<b>** o conteúdo preenchido a partir do mesmo será apresentado em “negrito”, já a opção **</b>** determina que o texto deixará de ser apresentado em “negrito” e voltará a ser apresentado normal.

Estes dados se referem a linha de programação **HTML** não sendo de responsabilidade da TOTVS a definição ou utilização dos mesmos.

[![image](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI8dDoXbPI/AAAAAAAAFNU/yZQd43uHlTw/image27_thumb.png?imgmax=800 "image")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI8cs2nTaI/AAAAAAAAFNQ/tAqV6VOCQvA/s1600-h/image27%5B1%5D.png)

Descrição Completa:

*Prezado Responsável Fiscal, <br>*

*Informamos que as notas fiscais de remessas abaixo relacionadas, ainda não tiveram retorno de todas as mercadorias. O prazo de 180 dias para o benefício de suspensão do ICMS está próximo. Favor verificar. <br>*

*Nota Fiscal - Data Emissão – Data Limite para Retorno - Prazo para Regularização (em dias)’*

*{0} {1} {2} {3}*

Cada informação apresentada em **| {} |** se refere ao conteúdo referenciado na Consulta SQL. Para vincular os dados deverá clicar no ícone |[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI8eam_8wI/AAAAAAAAEpk/eFdmjeB053w/image_thumb%5B10%5D.png?imgmax=800 "image")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI8drm3NCI/AAAAAAAAEpg/heyuLbfpt20/s1600-h/image%5B32%5D.png) | onde será apresentada coluna **| PARAM |** com os campos referenciados na descrição, a partir daí, o usuário deverá preencher na coluna **| ORIGEM |** para vincular ao parâmetro utilizado.

Neste exemplo específico os dados são:

0 – Número do Movimento

1 – Data de Emissão do Movimento

2 – Data Limite para Retorno da NF de Remessa

3 – Prazo restante para regularização (retorno da NF)

**- Fonte de Leitura**

**Tipo de Leitura (SQL\URL):** Este campo define o tipo de retorno do RSS podendo ser através de consulta SQL ou através de uma URL que fará o direcionamento á tela do Corpore.NET.

O endereço da URL é gravado na aba **| Identificação |** no campo **| Copie a URL abaixo para assinar o canal |**

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI8fnJqeVI/AAAAAAAAFNo/Dw9xRAxd9kE/image33_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI8evQR47I/AAAAAAAAFNk/QM5UvTNaB4o/s1600-h/image33%5B1%5D.png)

Nos campos em questão também podem ser passados parâmetros para obter resultado esperado.

Tela Configurada

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI8jF0YB2I/AAAAAAAAFN4/kGsZs2mRsjU/image36_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI8hwZASQI/AAAAAAAAFNs/miO_42uVcKc/s1600-h/image36%5B1%5D.png)

***Publicação de Convite de Canal RSS***

Depois de feitas parametrizações anteriores, o Canal RSS estará pronto para ser assinado e enviado convite para o funcionário fazer as configurações do Feeds.

Para isto é necessário selecionar o canal e clicar em **| Processo | Publicar Canal RSS |** onde será enviado convite para todos os usuários vinculados ao perfil parametrizado. Nessa tela é permitido alterar o assunto e o corpo do e-mail.

[![image](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI8mtUEY1I/AAAAAAAAFOM/EzqotO53sMo/image42_thumb.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI8kjgojpI/AAAAAAAAFOA/O9oHcRHLAa0/s1600-h/image42%5B1%5D.png)

***Criação de RSS Feeds no Outook***

Ao publicar o Canal RSS será enviado email para o usuário com convite, onde o mesmo deverá copiar o caminho referenciado no RSS e fazer a criação do mesmo.

De posse desta informação, deve acessar o Outlook em **| RSS |** clicar com botão direito do mouse e escolher opção **| Adicionar Novo RSS Feed |**. A seguir colar caminho informado no email que recebeu com “convite” para assinatura do canal e clicar no ícone **| Adicionar |**.

Depois de feito isto clicar no ícone **| Avançado |** e informar:

- Aba Geral: preencher descrição desejada para o Canal RSS

- Aba Downloads: habilitar campos | Baixar Automaticamente os Anexos neste feed - Baixar o artigo inteiro como um anexo .html para cada um |

A seguir clicar em | OK | para confirmar o processo.

Para assinar o RSS no Outlook 2007 deve-se inserir o usuário e senha do RM Portal se for pedido. Sempre que a consulta SQL referenciada na inclusão do Canal RSS retornar alguma informação será transformada em um *Feed* que é enviado para o Outlook. Para cada *Feed* será enviado email para o usuário que aceitou o convite.

Observações

Link para o TOTVS Connect: http://totvsconnect.blogspot.com/2010/12/como-fazer-rss-nf-de-remessa-com-prazo.html
