---
content_hash: 16fe8aa3614219f6152871f7673d46e54b05d152d850e8fa1db31126da6e4dee
fetched_at: '2026-06-29T00:08:24.639596+00:00'
page_id: '270899168'
product: rm
source: tdn-rm
title: GED - Gerenciamento Eletrônica de Documentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270899168
version: 38
---

# Índice:

---

.\*ndice:

# Objetivo:

---

     O objetivo deste documento é trazer uma visão do que é e como funciona a funcionalidade GED - Gerenciamento Eletrônica de Documentos, e como é feita a sua configuração.

# Introdução:

---

     O RM permite a integração com o Fluig para a sua utilização como servidor GED – Gerenciamento eletrônico de documentos. Está integração é realiza de uma base do RM para um servidor GED, ou seja, não permite múltiplos servidores GED. Após sua configuração, qualquer cadastro do RM passa a ter possibilidade de realizar o seu gerenciamento de arquivos, bastando apenas realizar os passos de mapeamento da pasta destino.

# Configuração:

---

     Processo de Configuração da Linha RM x GED - Gerenciamento eletrônico de documentos:

falseInstalação em N camadas (App Server)1º Passo:

Para configurar a integração GED, acesse o módulo Integração, e os menus "Ferramentas | Parâmetros | 50.07 - Linha RM x GED (Gerenciamento Eletrônico de Documentos)".

Clique para ver o Menu2º Passo:

Em seguida preencha as informações do servidor Fluig com as informações abaixo, para que o RM faça a comunicação com o Fluig.

* Servidor: Endereço do servidor (Nome ou IP)
* Porta: Porta a qual o Fluig está configurado
* Porta FTP: Porta FTP a qual o Fluig está configurado (Padrão: 21)

  Clique aqui
* Usuário: Nome do usuário administrador do Fluig
* Senha: Senha do usuário administrador do Fluig
* Empresa: Empresa cadastrada no Fluig
* Integração Fluig: Marcar o flag caso seja o servidor Fluig
* Matrícula: Preencher com o Usuário de Integração. (Obrigatório se a integração foi com o Fluig)
* Protocolo: Protocolo a qual o Fluig está configurado
* Grupo de Usuário: Nome do Grupo ao qual usuários do RM serão associados no Fluig após o Sincronismo
* Senha Padrão: Senha padrão para o usuário sincronizado com o GED acessar o Fluig
* Tipo Log: Quais eventos serão inseridos no Log

  

**Observação:**

O ambiente físico de intra-estrutura dos sistemas ECM e Fluig precisam estar configurados para permitir o tráfego de informações do RM pelas portas configuradas pelo FTP. Quando não são feitas alterações nas portas utilizadas pelo FTP, as portas padrões 20 e 21 são utilizadas pelo RM para fazer o upload dos arquivos.  
Na estrutura dos sistemas ECM e Fluig existe um diretório utilizado para fazer o upload dos arquivos do RM através do FTP. É necessário dar permissão de escrita nesta pasta (no ambiente ECM ou Fluig) para o Usuário de Integração utilizado na parametrização da integração conseguir fazer o upload pelo FTP:

Ao publicar um documento do RM para o ECM, a matrícula utilizada para registrar quem fez a publicação é àquela correspondente ao Usuário de Integração:

3º Passo:

Após a configuração, clique em Testar conexão para garantir que os dados estão corretos e em seguida clique em avançar até a finalização do processo.

|  |
| --- |

# Sincronismo do Usuário:

---

     Após realizarmos a configuração da Linha RM x GED precisamos enviar para o Fluig os usuários que terão acesso a está funcionalidade. No módulo Serviços Globais, acesse o menu "Segurança | Usuários".

     Em nosso exemplo, iremos integrar apenas o usuário corrente (mestre).

falseInstalação em N camadas (App Server)1º Passo:

Selecione os usuários e execute o processo “Sincronizar usuários do Corpore com o GED”.

Atenção

Caso o **Usuário** possua uma associação com **Funcionário** os dados Nome e E-mail que serão sincronizados serão o do **Funcionário**.

Obs.: Na tela de sincronização, a coluna "Integrado" irá mostrar um ícone caso aquele usuário ja tenha sido sincronizado.

Obs:2: Caso o usuário selecionado para executar a sincronização **NÃO** exista no Fluig, ele será criado de acordo com as informações do usuário em questão no RM:   
E-mail: mesmo do RM   
Login: mesmo do RM   
Matrícula: HASH de Segurança   
Nome: mesmo do RM   
Sobrenonme: mesmo do RM"

Cache com informação do UserID.

Após finalizado o processo de sincronização será apresentado um aviso informando o tempo de renovação do cache, que deverá ser respeitado para utilizar qualquer outro processo seguinte.

2º Passo:

Após a execução do processo, o usuário será criado no Fluig.

Caso o campo 'Senha padrão' esteja em branco na configuração da integração, a senha desse novo usuário no FLUIG é "123456789".

|  |
| --- |

|  |
| --- |

# Realizando Mapeamento:

---

    Após os parâmetros estarem configurados e o usuário sincronizado com o Fluig, é necessário realizar o mapeamento da pasta para a integração com o Fluig.

    Em nosso exemplo, utilizaremos o cadastro de Alunos do RM.

falseInstalação em N camadas (App Server)1º Passo:

No Fluig, crie a pasta “Documentos Alunos”

|  |
| --- |

2º Passo:

No módulo Educacional, acesse o menu Currículo e Oferta -> Alunos

|  |
| --- |

3º Passo:

Acesse Anexos -> GED -> Gerenciar

|  |
| --- |

   Depois de executar o passo 3 descrito acima e após clicar em avançar, teremos 6 (seis) opções de mapeamentos distintos:

**1.Utilizar pasta mapeada**:

* Todos os arquivos de todos os registros serão enviados para a mesma pasta mapeada no GED.

Clique para ver imagem

Neste exemplo, todos os arquivos serão salvos na pasta "Teste\_Pasta Mapeada".

**2. Permitir o usuário escolher uma das sub-pastas de pasta mapeada**:

* O usuário pode selecionar uma Sub-Pasta dentro da pasta configurada, no momento do envio do arquivo.

Clique para ver imagem

Neste exemplo, o usuário poderá salvar os arquivos nas pastas filhas da "Teste\_Sub Pasta Mapeada", sendo "Pasta1" ou "Pasta2".

Essas opções serão exibidas para o usuário na hora de enviar o arquivo.

**3.** **Utilizar o retorno de uma coluna do dataServer como nome da pasta:**

* A estrutura de dados da tabela do cadastro é exibida, e o usuário pode selecionar uma coluna para que o RM crie no GED uma pasta com o nome referente a coluna selecionada.  
  Ex.: Caso selecionado o RA do aluno, dentro da pasta selecionada como mapeamento será criada uma pasta para cada registro, sendo seu nome o RA do registro selecionado na hora de envio do arquivo.   
  **Obs**: Caso a coluna selecionada não seja única por registro, os arquivos de registro que contém o mesmo conteúdo para a coluna selecionada ficaram na mesma pasta no servidor GED. Ex.: Selecionar a coluna CODCOLIGADA, todos os registros que estiverem na mesma coligada terão o seus arquivos enviados para a mesma pasta no servidor GED.
* Ao selecionar mais de uma coluna do DataServer, é possível criar estruturas de pastas.

Clique para ver imagem

Neste exemplo, os arquivos serão organizados no GED por diretórios criados automaticamente por: Estado > Nome Fantasia.

Por exemplo:

...Teste\_Coluna DataServer/MG/Coligada1

...Teste\_Coluna DataServer/MG/Coligada2

...Teste\_Coluna DataServer/SP/Coligada3

**4.** **Utilizar o retorno de uma coluna do dataServer como nome da pasta com o CheckBox “Permitir sincronismo automático dos arquivos postados através GED” marcado:**

* Idem ao item 3, mas acrescentando o sincronismo da pasta do servidor GED com os registros no RM. Ou seja, caso um arquivo seja postado diretamente no GED, na pasta do registro especifico, o RM também exibirá este registro. Da mesma forma, se o arquivo for removido diretamente no GED, ele não será mais listado no RM.  
  Cuidado: a marcação deste parâmetro pode ocasionar a exibição de arquivos de outros registros caso o mapeamento seja igual o exemplo do CODCOLIGADA citado acima.

Clique para ver imagem

Neste exemplo, os arquivos serão organizados no GED por diretórios criados automaticamente por: Estado > Nome Fantasia.

Por exemplo:

...Teste\_Coluna DataServer/MG/Coligada1

...Teste\_Coluna DataServer/MG/Coligada2

...Teste\_Coluna DataServer/SP/Coligada3

Os arquivos adicionados/removidos diretamente no GED, também serão listados/ou não no RM.

**5.** **Utilizar uma pasta para cada registro de acordo com a chave primária:**

* Dentro da pasta selecionada para o mapeamento, quando o usuário incluir um arquivo novo, será criada automaticamente uma pasta tendo seu nome como a combinação da chave primaria da tabela referente ao cadastro.

Clique para ver imagem

Neste exemplo, os arquivos serão organizados no GED por diretórios criados automaticamente por: Chave primária

Por exemplo:

...Teste\_ChavePrimária/{PK\_Tabela}

**6.** **Utilizar uma pasta para cada registro de acordo com a chave primária pasta com o CheckBox “Permitir sincronismo automático dos arquivos postados através GED” marcado:**

* Idem ao item 5, mas acrescentando o sincronismo da pasta do servidor GED com os registros no RM. Ou seja, caso um arquivo seja postado no GED na pasta do registro especifico, o RM também exibirá este registro. Da mesma forma, se o arquivo for removido diretamente no GED, ele não será mais listado no RM.

Clique para ver imagem

Neste exemplo, os arquivos serão organizados no GED por diretórios criados automaticamente por: Chave primária

Por exemplo:

...Teste\_ChavePrimária/{PK\_Tabela}

Os arquivos adicionados/removidos diretamente no GED, também serão listados/ou não no RM.

Importante!

Apenas mapeamentos com a opção "Permitir sincronismo automático dos arquivos postados através GED" marcada terão as inclusões/remoções de arquivos feitas diretamente no GED refletidas no RM.

Caso essa configuração não esteja disponível para algum tipo mapeamento ou esteja desmarcada, ao incluir um arquivo diretamente no GED ele não será listado no RM. E se algum arquivo for excluído diretamente no GED, ele continuará a ser listado no RM até que seja excluído pelo RM.exe.

falseInstalação em N camadas (App Server)1º Passo:

Vamos selecionar a opção número 1 – Utilizar pasta mapeada e selecionar a pasta “Documentos Alunos”

2º Passo:

Avançar e finalizar o processo:

# Envio de Arquivos:

---

    Passo a passo de envio de arquivos para o GED

falseInstalação em N camadas (App Server)1º Passo:

Para enviar arquivos para o GED, clique em Anexo -> GED -> Integração GED

2º Passo:

Uma aba será apresentada. Para enviar um arquivo, clique em novo. Teremos a opção de alterar o nome do arquivo ou Utilizar o próprio nome do arquivo. No exemplo a seguir vamos selecionar Utilizar o próprio nome do arquivo.

3º Passo:

Após clique em Localizar e Enviar. Uma caixa de seleção de arquivo será exibida. Selecione o arquivo e clique em Abrir

4º Passo:

 Ao clicar em Abrir, o arquivo é enviado para o servidor GED e listado na aba Integração GED

5º Passo:

Como no tipo de mapeamento selecionamos “Utilizar pasta mapeada” o arquivo foi postado na pasta “Documentos Alunos” no Fluig

Mais informações sobre erros

Caso algum erro seja apresentado ao enviar um arquivo, consulte 

# Visualização do Arquivo:

---

falseInstalação em N camadas (App Server)1º Passo:

Após realizar a importação do arquivo, é possível visualiza-lo. Para isso, edite o registro inserido e clique em Visualizar

2º Passo:

Caso o usuário não esteja logado no Fluig, será solicitado o usuário e senha para acessar o sistema

3º Passo:

Após acessar o sistema o arquivo é aberto e exibido para o usuário

Serão aceitos os seguintes caracteres especiais no nome do arquivo enviado, mais espaços em branco.

* ´`' !@#$%& -\_+=()[]{}[] ªº^~, . ; ¨§¢¬£ ³²¹

Exemplo: Nome do arquivo **"teste!@#$%¨& - 123.txt",** tudo será mantido, nada será alterado.

**Os seguintes caracteres não serão aceitos e o envio do arquivo será recusado:**

* **\ / ? : \* <>"**Estes caracteres por padrão não são aceitos pelo sistema operacional, portanto não é permitido definir um nome de arquivo que os contenha.

# Visualização de Logs:

---

Ao marcar a configuração de Tipo de Log's ao configurar a integração os Log's podem ser vistos em

Menu Integrações | Integração | Monitor da Fila de Integração, onde todos os tipos de requisições serão logadas nesta visão. A coluna Status informa se a mensagem foi processada com sucesso ou não.

# Envio de Relatórios

---

Ao enviar um relatório para o GED, é necessário que o mapeamento na visão de relatórios (Anexo → GED → Gerenciar) tenha sido executado. Sem esta execução, será apresentando um erro informando para verificar o mapeamento da pasta.

Para envio de relatórios do RMReports para o GED, estão disponíveis as opções de mapeamento "*Utilizar pasta mapeada*" e "*Utilizar uma pasta para cada registro de acordo com a chave primária*".

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** GED - Gerenciamento Eletrônico de Documentos

falsefalse

**Status:** Finalizado

false

**Data:** 20/08/2021

false

**Autores:**

---
