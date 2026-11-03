---
content_hash: 26647d4c06159f26d19b4cfd76756d827efb5cef231ea41b9a70ca7283e1b68a
fetched_at: '2026-06-29T00:11:11.432534+00:00'
page_id: '64652506'
product: rm
source: tdn-rm
title: NF-e - Instalação e Configuração do TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=64652506
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***P11* |
| **Processo** | **:** | Instalação e Configuração do TSS |
| **Subprocesso** | **:** | Instalação e Configuração do TSS |
| **Data da publicação** | **:** | 03/07/2013 |

**Introdução:**

Este passo a passo tem como finalidade auxiliar na instalação/atualização do TSS (totvs service sped).

**Importante:**

É altamente recomendado a criação de uma base própria para armazenar as tabelas do TSS, bastando apenas criar uma base vazia, onde assim que o processo de instalação do TSS for concluído e o mesmo for iniciado as tabelas serão criadas de forma automática.

Não é necessário instalar o TSS em todas as maquinas que iram enviar NF-e, o TSS e o TOPCONNECT devem ser instalados somente em uma maquina onde as demais devem apontar para a maquina que os aplicativos foram instalados. **Não se deve ter mais de um TSS e TOPCONNECT na rede.**

**Remover a instalação antiga do TSS:**     

Acesse: Iniciar | Configurações | Painel de Controle | “Adicionar ou Remover Programas” | remova a instalação de todos os programas com nome de TSS (normalmente existem dois, onde um é referente ao executável e outro referente ao update). Após desinstalar o TSS será necessário apagar os diretórios da versão antiga, para isso realize o seguinte procedimento: Vá em C: | e apague a pasta totvssped.

 

**Instalação e configuração do TSS:**

Execute o arquivo TSS 11.exe e selecione o idioma em seguida clique em OK, na tela de **bem vindo** clique em avançar, na tela de **contrato** clique em sim, na tela de **escolha de local de destino** clique em avançar e na tela de **tipo de instalação** clique em avançar.

Na tela de **Editar dados** no campo servidor deverá ser informado o **IP da maquina** onde o TSS está sendo instalado (varias maquinas poderão enviar NF-e) ou **localhost** (somente a maquina local irá enviar NF-e), no campo porta de ser informado uma porta **HTTP**, normalmente a **8080**:

\* Para saber a porta **HTTP** procure o setor de TI da empresa e informe a eles que o TSS utilizará a porta HTTP e 443 para transações com a internet e devem liberar QUALQUER TIPO DE BLOQUEIO que possa impedir esta transação (Proxy, Firewall, Antivírus, etc.)

Na próxima tela são solicitadas as informações para o TSS conectar-se no **TopConnect**

No campo **“Database”,** para banco **SQL** será sempre “**MSSQL”** e para e banco **Oracle** será sempre “**ORACLE”**

No campo **Alias** para banco **SQL** deve ser informado **TOTVSSPED (**nome da fonte de dados ODBC criada na instalação do topconnect). Para banco Oracle deve ser informado o nome da Instancia do banco criado para o TSS.

No campo **Servidor** informe o mesmo que estiver informado na tela inicial do topconnect monitor. (Iniciar | todos os programas | topconnect | topconnect monitor).

Duvidas sobre o este passo procure a equipe de Ti da empresa.

**Seleção de processos que serão utilizados:**

Na Tela seguinte selecione os tipos de notas que a empresa irá emitir:

Nota Fiscal Eletrônica: Estadual - produto – tributada pelo ICMS;

Nota Fiscal Eletrônica: Não deve ser marcado;

Nota Fiscal de Serviço: Municipal – serviço – tributada pelo ISS;

Conhecimento Transporte Eletrônico: Emitir CT-e, MDF-e e MD-e.

**OBS:** Para NFS-e BH, Cuiabá e Aparecida de Goiânia também é necessário selecionar a opção de **“Nota Fiscal Eletrônica”**.

Após clicar em avançar aparecera uma tela semelhante a anterior, porem a mesma é referente ao TOTVS Colaboração, **somente deverá ser marcada** alguma opção se o cliente possuir o pacote de Colaboração. Caso não possua gentileza não marcar.

Na tela seguinte clique em **“Sim”** para executar o TSS como um serviço, esta opção cria um serviço no Windows para executar o envio das notas.

Agora execute o arquivo **“TSS 11 - Update.exe”,** selecione o idioma e avance as etapas até concluir.

**DICAS DE POSSÍVEIS ERROS:**

Ao abrir o TSS SERVER, apresenta o seguinte erro:

- Connection failed – DataBase: **XXXX** Server: **XXXX** Port:**XXXX**

**Causas possíveis:**

1. 1. Configuração incorreta do TOPCONNECT;
   2. Configuração dos dados do TOPCONNECT incorretos no TSS;
   3. Porta de conexão bloqueada ou informada incorretamente.

**Solução:**

1. Se ao validar a conexão do TopConnect com o banco de dados apresentar erro, favor rever as dicas do [TOPCONNECT](http://totvsconnect.blogspot.com/2010/12/dica-topconnect-erros-de-conexao.html).

2. Acesse o diretório “**C:\totvssped\bin\appserver**” e edite o arquivo “**Totvsappserver.ini**” (ou appserver.ini) e realize as seguintes verificações:

a. Localize dentro do arquivo a linha “[**TopConnect**]” e verifique se no campo “**Database**” está preenchido com o ambiente criado no “TopConnect”, o campo “**Server**” está preenchido como o IP ou Host da máquina onde o TopConnect foi instalado e o campo “**ALIAS**” preenchido com a “Fonte de dados ODBC” em caso de SQL, e em caso de Oracle o nome da instância.

**(Imagem exemplo para banco SQL)**

3. Verifique com a equipe de TI se a porta de conexão utilizada está disponível.

**Informações Adicionais:**

Verifique as configurações dos parâmetros do RMNucleus em Opções| Parâmetros | RMNucleus | Integrações | Fiscal | Parâmetros por Filial | Conexão NF-e .Este parâmetro deve ser configurado conforme o TSS.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
