---
content_hash: c72253d4595ec82cd8e146cfa480cdc8cde3a18ec525fafd7a06de03d72c81ad
fetched_at: '2026-06-29T00:11:33.441217+00:00'
page_id: '759941886'
product: rm
source: tdn-rm
title: Altera LS
type: documentation
url: https://tdn.totvs.com/display/LRM/Altera+LS
version: 1
---

|  |  |
| --- | --- |
| **Funcionalidade** | Responsável por efetuar alterações no banco de dados do produto RM sendo (SQL Server ou Oracle).  Calcula o CRC e efetua alterações na tabela GPARAMS alterando os campos LICENCESERVERADDRESS, LICENCESERVERPORT, CONTROLELIC, URLPORTAL, e CONTROLE. |
| **Código** | Power Shell / C# / .NET Framework 4.8 / Visual Studio 2022 |
| **Respositório** | AlteraLS - <https://github.com/cloud104/tcloud-rm-alterals.git> Power Shell (Commons) - [https://github.com/cloud104/tcloud-devops-rm/](https://github.com/cloud104/tcloud-devops-rm/blob/main/management/commons/modules/security.psm1) |
| **Executado em** | A ferramenta é chamada através de AÇÃO "Altera LS" no TCLOUD manualmente pelo usuário. |
| **Descrição** | Ao executar a ação na TCLOUD, o formulário é preenchido com os dados pelo usuário, e ao clicar em ENVIAR o TCM é acionado enviando a chamada para o método Power Shell do nosso repositório **/commons/security.ps1** > **EncryptString($TextToExcrypt))**. Este método, pega as informações do formulário, cria a string de conexão no padrão do banco selecionado, busca da google GCP os secrets necessários para a criptografia (**AES** / algoritmo **IV**) e executa a chamada do programa RM.AlteraLS.exe, passando estes parâmetros criptografados.  Dentro do método é realizada a descriptografia, utilizando as mesmas chaves no método em powe shell, sendo executado as ações diretas no banco de dados. |
| **Dependências** | * Obrigatório existir a variável de ambiente chamada **GOOGLE\_APPLICATION\_CREDENTIALS** apontando para o valor que faz o login na GPC: **C:\toolsinstall\gcloud-bucket-secret.json**   + Caso não exista uma nova exceção (**New-TCloudException**) informando que esta variável de ambiente é obrigatória, será enviada a TCLOUD. * Garantir que o .NET Framework é o 4.8 * DLLs do Google e de Criptografia são obrigatórias |
| **Em caso de alterações** | * É preciso compilar o projeto, executar os testes unitários localmente (dentro do mesmo projeto), e garantir que não estão quebrando, caso esteja, é necessário realizar as alterações necessárias de acordo com a nova demanda * Ao compilar, o .exe e as novas DLLs de dependência, devem ser inseridas no nosso repositório do commons na pasta **tcloud-devops-rm\management\files\RM.AlteraLS\  -** é através dele que a atualização do código será realizada nas imagens |
