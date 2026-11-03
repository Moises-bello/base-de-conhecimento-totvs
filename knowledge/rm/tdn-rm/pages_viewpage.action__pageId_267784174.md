---
content_hash: ed03f463a2ac0ce862090aa8f9e5959057a1dde5f7eada40d80ba40b71f512e3
fetched_at: '2026-06-29T00:08:19.393310+00:00'
page_id: '267784174'
product: rm
source: tdn-rm
title: Instalação versão 12.1.2209 ou superiores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267784174
version: 10
---

# Orientações para instalar a versão 12.1.2209 ou superiores

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.2209 ou superiores |
| **Ocorrência:** | Novas opções que aparecem no momento da instalação da versão 12.1.13 ou superiores |
| **Ambiente:** | Ambiente de Produção / Ambiente de Teste / |
| **Passo a passo:** | Passo a passo para realizar a instalação da versão:  Desative o Firewal do Windows, Antivirus e UAC;  Verifique se está instalado o .Net Framework versão 4.8 ou superior.  Ao iniciar a instalação, a primeira validação é do License Server    Clicando em Sim, o cliente é direcionado a documentação referente ao License Sever <https://tdn.totvs.com/x/lPKRDg>  Em Seguida é apresentada mensagem sobre descontinuidade das versões do Oracle  Clicando em " Sim",    Clicando em " Sim", o cliente é redirecionado para a página de portabilidade do RM  <https://tdn.totvs.com/x/XDVNDQ>  Em seguida iniciaremos a instalação      Aceite dos temos    Informações do Cliente - Defina os parâmetros destcados    Informe o caminho de Instalação, por default é sugerido a pasta C:\totvs mas o usuário pode alterar de acordo com sua preferência      Prossiga com a instalação    Na próxima tela informe se a instalação é local ou N camadas    Nessa opção é definida o tipo de ambiente de instalação:  **Ambiente Local** : A máquina client acessa diretamente a camada de banco de dados.  **Ambiente 3 camadas** : Nesse ambiente ocorre uma melhor divisão das atividades do sistema. O servidor de aplicação fica responsável por executados processos específicos(Regra de Negócio, relatórios cálculos, etc) além de realizar a comunicação com o Banco de Dados.  Opção: Client    Servidor de Aplicação    Servidor de Jobs    **Obs.** Quando selecionado a opção de Ambiente N camadas deve ser informado o caminho para FileServerPath, esse caminho deve ser compartilhado na rede.  Avance para a próxima etapa    Nessa opção o RM oferece para o usuário:  Fazer Download e instalar TAF em Paralelo - Mais informações, acesse: <https://tdn.totvs.com/x/Lv4GEQ>  Utilização do Oracle RAC - Mais informações, acesse: <https://tdn.totvs.com/x/uS1ZEg>  E se a opção de Instalação 03 camadas for escolhida na instalação é possível Configurar o TOTVS Update, mais informações, acesse: <https://tdn.totvs.com/x/zAHYD>  Avance para a próxima tela    Escolha quantos serviços deseja utilizar, sendo 9 o máximo de serviços suportados. Essa parametrização ficará a cargo do usuário para fazer o balanceamento nativo, conforme a sua configuração de Hardware.  Maiores informações sobre balanceamento nativo acesse : <https://tdn.totvs.com/x/AKwXDg> O número de serviços de Host sugeridos durante a instalação é um número default com base em ambientes de clientes Totvs. Já, o dimensionamento de usuários por serviços, temos validado pela equipe de Performance de Banco de Dados o valor de 25 usuários simultâneos por host.  Avance para a próxima tela    Nessa opção o RM oferece para o usuário se deseja utilizar o TOTVS Gateway Manager, mais informações, acesse: <https://tdn.totvs.com/x/lw37Gw>  Progresso de instalação em andamento    Escolha o idioma que deseja trabalhar nos sistemas RM    Informe os dados de Conexão da Base    Caso não deseje informar, basta clicar em "Cancelar".  Neste momento o serviço do RM.Host.Service está sendo criado  Na próxima tela, informe se deseja Instalar e Configurar o Rm.Host.Cleanner    Caso positivo, configure as telas a seguir.      Finalize a instalação do RM |
| **Observações:** |  |
