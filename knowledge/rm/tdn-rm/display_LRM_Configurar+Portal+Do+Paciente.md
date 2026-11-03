---
content_hash: c11816ddd3c10af4d554b0e9ff80aa31b8ced8c5c73b56c8515822a089599c52
fetched_at: '2026-06-29T00:11:43.116960+00:00'
page_id: '802020572'
product: rm
source: tdn-rm
title: Configurar Portal Do Paciente
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurar+Portal+Do+Paciente
version: 22
---

Olá, você está na página de configuração do Portal do Paciente.

Basta seguir o passo a passo.

### 1) Passo 1: Realize a instalação do portal.

Através do Instalador, execute a instalação do Portal do Paciente.

Confira se os arquivos do portal se encontram dentro do diretório no qual o portal foi instalado, geralmente dentro do diretório: C:\totvs\CorporeRM\FrameHTML\web\app\Sau\portalpaciente\

### 2) Passo 2: Configure o arquivo Config.Staging.Json

Vá na pasta do diretório onde o portal está instalado, geralmente dentro do diretório: C:\totvs\CorporeRM\FrameHTML\web\app\Sau\portalpaciente\assets

Encontre o arquivo: **config.staging.json**, e faça uma copia com o nome "**config.json**" sem aspas (OBS: Se o arquivo já for do tipo json, não e necessário incluir o .json ao nome do arquivo)

Edite o arquivo config.json que acabou de duplicar:

* Modifique o usuário e senha de acordo com um usuário já cadastrado no RM e que tenha todas as permissões necessárias, tais como visualização de agendas, horários e outras permissões necessárias para o portal funcionar. Para verificar os usuário, acesse "Serviços Globais" > "Usuários" > Verifique um usuário com as permissões necessárias (nome de usuário na coluna "Usuário")

* Modifique o url, trocando o localhost, pelo url de acesso ao servidor que o portal irá fazer a conexão.
* Caso o portal apresente erro ao tentar se cadastrar/ logar. Verifique se a url se encontra igual a da imagem , dentro arquivo de configuração config.json que acabamos de duplicar.
  + **A partir da versão 12.1.2510 retire o /api/hcg/ ao final do url, dentro arquivo de configuração config.json que acabamos de duplicar.**

* Defina qual coligada para acesso de acordo com seu código. Acesse as coligadas em "Serviços Globais" > "Administração" > "Coligadas" (Verificar o código da coligada desejada de acordo com a coluna "Código")

* Pronto seu portal já deverá estar funcionando. Seu arquivo terá o seguinte formato de exemplo a seguir:  
    
  + **Versões anteriores á 12.1.2510:**
  + **Versão 12.1.2510 e posteriores:**

### 3) Passo 3: Portal Configurado com sucesso!

Pronto agora seu portal deve estar configurado corretamente.

Para acessá-lo basta acessar pelo url abaixo, trocando o "minha\_url\_aqui", pelo que informou nas configurações do portal.

[https://minha\_url\_qui/FrameHTML/web/app/Sau/portalpaciente/#/login.](https://SeuUrlAqui/FrameHTML/web/app/Sau/portalpaciente/#/login.)

OBS: Para funcionamento do portal para mais de 1 coligada, deve-se fazer a instalação de 1 portal para cada coligada, alterando os diretórios e também o arquivo de configuração do portal, alterando a informação do campo de CODColigada, para o número da coligada que deseja disponibilizar o portal.

### 4) Versões

As versões 12.1.2402 e 12.1.2406 do portal do paciente são compatíveis com a linha RM.

Funcionalidades da versão 12.1.2402: Agendamentos de consultas e exames via portal do paciente;

Funcionalidades da versão 12.1.2406: Agendamentos de consultas e exames via portal do paciente, verificação de elegibilidade da carteirinha do paciente, configurações de parâmetros gerais do portal do paciente;
