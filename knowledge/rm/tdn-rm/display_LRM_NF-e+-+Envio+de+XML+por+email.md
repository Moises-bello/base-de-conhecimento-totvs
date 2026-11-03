---
content_hash: 14bc20cc6508b9c19b73e4561ed611c0384725d8e1e0229ebf3d41974368b469
fetched_at: '2026-06-29T00:11:11.230580+00:00'
page_id: '64651819'
product: rm
source: tdn-rm
title: NF-e - Envio de XML por email
type: documentation
url: https://tdn.totvs.com/display/LRM/NF-e+-+Envio+de+XML+por+email
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | Envio de XML por email |
| **Subprocesso** | **:** | Envio de XML por email |
| **Data da publicação** | **:** | 02/07/2013 |

**Introdução**

A partir da 11.40 é possível realizar algumas alterações no processo de envio do XML por e-mail, neste “*Como Fazer”* iremos explicar como parametrizar o sistema para a utilizar estas novas funcionalidades: Alterar o Texto padrão do e-mail, Enviar e-mails com Cópia oculta, Enviar o XML por e-mail automaticamente no envio da NF-e e Enviar o XML para vários e-mails ao mesmo tempo.

****1- Texto padrão do e-mail**Abaixo as parametrizações que deverão ser realizadas para cada funcionalidade.**

Para se utilizar a funcionalidade do envio de e-mail mantendo um texto padrão na mensagem do e-mail que será enviado para o cliente/fornecedor é necessário seguir alguns passos, segue abaixo:

* + Acesse o Menu Cadastros / Tabelas Auxiliares / Mensagens, crie uma mensagem com a Classificação “Outras”, conforme imagem abaixo:

Na mensagem poderá ser utilizado algumas variaveis conforme a necessidade da empresa, são elas:

            @Usuario - usuário logado no sistema

            @NomeFilial - Razão Social da Filial do movimento

            @TelFilial - Telefone da Filial do movimento

            @Nome - Nome do Cliente/Fornecedor

            @ChaveAcesso - Chave de Acesso da NF-e

            @DataAutorizacao - Data de Autorização da NF-e

            @Contato -  Contato do Cliente/Fornecedor

            @NumeroNota - Número do Movimento

* + Acesse o Menu Opções | Parâmetros | RM Nucleus | Tipo de Movimento, na Etapa Fis - NF-e para escolher o texto padrão do e-mail que foi cadastrado anteriormente, caso nenhum seja selecionado o sistema continuará carregando a mensagem default.

**2- Opção de envio de e-mail para BCC**

Para se utilizar a funcionalidade do envio de e-mail com cópia oculta, segue abaixo a parametrização a ser feita.

* + Ao acessar a visão de envio de e-mail, em Processos | Enviar XML por e-mail , foi criado um campo CCo ( Cópia Oculta), onde ao preenche-lo será disparado o e-mail com o XML em anexo como cópia oculta.

**3- Envio automático do e-mail**

Esta funcionalidade foi criada para automatizar o processo de envio de XML por e-mail, ao realizar o envio da NF-e e receber a autorização da mesma, o sistema irá automaticamente enviar um e-mail para o cliente fornecedor com o XML da nota enviada. Para que o sistema faça este processo automático, é necessário acessar os parâmetros:

* + Opções | Parâmetros | RM Nucleus | Tipo de Movimento, na Etapa Fis - NF-e**,** existem três opções para se escolher, abaixo segue a explicação de cada uma:

**Não enviar e-mail automaticamente**: Ao escolher esta opção o XML deverá ser enviado manualmente em Processos | Envio do XML por e-mail.

**Enviar XML da NF-e por E-mail:** Ao escolher esta opção o XML da nota será enviado automaticamente, juntamente com a autorização da NF-e.

**Enviar XML da NF-e por E-mail com cópia para a transportadora:** Ao escolher esta opção o sistema irá realizar automaticamente o envio do XML com cópia para a transportadora, caso o email da transportadora não esteja preenchido no cadastro da mesma o email será enviado normalmente para o email do cliente/fornecedor.

**Observação: O campo Menssagem deve ser preenchido Obrigatoriamente.**

**4- Selecionar contatos do cliente Fornecedor**

Ao enviar o XML por e-mail é possível escolher uma lista de e-mails no qual se deseja enviar o XML, para que seja possível o envio para vários e-mails é necessário parametrizar o sistema da seguinte forma:

Cadastrar os contatos no cadastro do Cliente\Fornecedor, conforme imagem abaixo:

* + Acesse os parâmetros em Opções | Parâmetros | Rm Nucleus | Tipo Movimento – Etapa Mov – Impressão 2/2 – marque o parâmetro “Usar contato de fornecedor no envio de e-mail”.

Ao executar o processo de envio de e-mail, será exibida uma tela, avance ate a etapa que ira selecionar o contato do cliente. Será exibida a lista de Contatos do Cli/For do movimento para que seja selecionado todos os que receberam copias do e-mail com o XML.

**Para possíveis falhas no processo de envio de email, verifique os seguintes dados:**

**Possíveis causas:**

**1.** Cadastro de e-mail da filial não está preenchido;

**2.** Cadastro de e-mail do Usuário no sistemas não está preenchido;

**3.** Cadastro de e-mail do cliente não está preenchido;

**4.** Proxy, Firewall ou antivírus bloqueando portas de saída de e-mail;

**5.** Configurações de autenticação do servidor preenchidas erroneamente;

**6.** Nos paramentos globais (Opções | Parâmetros | Globais), o campo domínio estar preenchido.

**Possíveis soluções:**

**1.** Preencher todos os e-mails nos cadastros citados acima;

**2.** Liberar todas as portas;

**3.** Configurar corretamente a autenticação do servidor (exige autenticação ou não exige autenticação).

**4.** Limpar o campo Domínio nos parâmetros globais;

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica);
