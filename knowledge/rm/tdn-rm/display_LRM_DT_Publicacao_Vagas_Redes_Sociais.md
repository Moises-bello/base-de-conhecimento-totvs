---
content_hash: 8c45faf4903e9c06e4f0fd4a1a06b974e8efdc1652211c0b53926bf72bb9f10e
fetched_at: '2026-06-29T00:06:06.119028+00:00'
page_id: '201728549'
product: rm
source: tdn-rm
title: DT_Publicacao_Vagas_Redes_Sociais
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Publicacao_Vagas_Redes_Sociais
version: 13
---

# PUBLICAÇÃO DE VAGAS NAS REDES SOCIAIS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Planejamento e Captação* | *Publicação de vagas nas redes sociais* | |
| **Versões/Release:** | *12.1.7* |

## Descrição

O processo para publicação das vagas nas Redes Sociais visa auxiliar o usuário a tornar público as vagas nas maiores redes sociais, obtendo assim uma maior divulgação e consequentemente um maior número de candidatos.

## Procedimento para Utilização

Pelo TOTVS Gestão de pessoas vamos em **Mensagem Customizada / Configurações / Mensagens / Customizadas** para ser realizado a criação de mensagens customizadas para publicação em redes sociais.

Dê duplo clique em **novo filtro 1 / Clique em Mensagem Facebook.**

Também será possível incluir parâmetros que serão executados no momento do envio das mensagens.  
Os parâmetros na mensagem deverão estar entre colchetes [ ].  
Nele informaremos os seguintes parâmetros, todos relacionados ao perfil de vaga:

 Código do Perfil de Vaga [CODPERFILVAGA]  
  Nome do perfil de vaga [NOME]  
  Localidade [LOCALIDADE]  
  Descrição do Perfil de Vaga [COMPLEMENTO]  
  Data de Abertura [DATAABERTURA]  
  Data de Fechamento [DATAFECHAMENTO]  
  Grau de Instrução [CODGRAUINSTRUCAO]  
  Descrição da Instrução [DESCRICAOGRAUINSTRUCAO]  
  Experiência Exigida [EXPERIENCIASEXIGIDAS]  
  Experiência Desejada [EXPERIENCIASDESEJADAS]  
  Salário do perfil de vaga [REMUNERACAO]  
   
 Além disso, deverá ser gerado um link que permita ao candidato o acesso as vagas publicadas. Para tanto, através da função *ENCURTARLINK*, será possível passar um link como parâmetro, e no momento do envio da mensagem o link será transformado em um link curto. O link a ser encurtado deverá estar entre parênteses, conforme exemplo:  
   
 ENCURTARLINK ([http://www.testes.com.br](http://www.testes.com.br/))

Segue exemplo da utilização dos parâmetros na mensagem customizada de publicação em redes sociais.  
   
 Descrição completa da vaga:  
Vaga: Analista  
Descrição da Vaga: Analista de Suporte Pleno para atuação em Help Desk  
Salário (Pretensão) + Benefícios: A combinar  
Local: Belo Horizonte  
Formação Exigida: Formação Superior Completo em TI  
Experiência Exigida: Suporte intermediário a usuários de informática, instalação e configuração de hardware, impressoras, smartphones, desktops, notebooks, dispositivos móveis e softwares como MS Office e MS Windows XP, 7, 8.  
Experiência Desejada: Conhecimentos básicos de administração de redes, Exchange, VPN, FTP e Telefonia IP.  
Data da Abertura da Vaga: 01/11/2014  
Data de Encerramento: 30/11/2014  
Para candidatar-se a vaga acesse o link abaixo:

<http://fluig.contax.com.br/curriculum?vaga=000120&desc=analista&rede=f>

Descrição da Vaga utilizando parâmetros:  
Vaga: [CODPERFILVAGA]  
Descrição da Vaga: [NOME]  
Salário (Pretensão) + Benefícios : [REMUNERACAO]  
Local: [LOCALIDADE]  
Formação Exigida : [DESCRICAOGRAUINSTRUCAO]  
Experiência Exigida : [EXPERIENCIASEXIGIDAS]  
Experiência Desejada : [EXPERIENCIASDESEJADAS]  
Data da Abertura da Vaga : [DATAABERTURA]  
Data de Encerramento : [DATAFECHAMENTO]  
Para candidatar-se a vaga acesse o link abaixo :

ENCURTARLIK *http://fluig.contax.com.br/curriculum?vaga=[CODPERFILVAGA]]&desc=[NOMEPERFILVAGA]&rede=f*  
  
Antes de executar o processo de publicação de vagas em redes sociais, o usuário deverá realizar algumas parametrizações no sistema.

Caso o usuário esteja em uma rede protegida por proxy, a configuração deverá ser feita na primeira aba: "Redes Sociais", do cadastro de "Parâmetros Globais".

Após realizar a configuração de contas das redes sociais, o usuário deverá parametrizar quais contas serão utilizadas pelo processo de publicação de vagas nas redes sociais.  
 OBS: Cada rede social somente poderá ter uma conta por rede social parametrizada.

Esse processo poderá ser executado por qualquer usuário logado no sistema e com permissão de acesso na funcionalidade, entretanto, a vaga será publicada no perfil do usuário informado no parâmetro de publicação.

O processo Publicação de Vagas em Redes Sociais está disponível em **Painel de Seleção / Vagas da Seleção / Processo / Publicação da Vaga nas Redes Sociais.**   
O processo de publicação será executado por perfil de vaga e o usuário do RM poderá escolher em qual rede social Deseja publicar a vaga.   
O usuário do RM deverá selecionar o perfil de vagas desejado, executar o processo de publicação e selecionar as redes sociais no qual deseja publicar a vaga.

Será obrigatório informar uma mensagem, caso contrário o usuário não conseguirá avançar até a próxima etapa.

Após selecionar as redes sociais e informar as mensagens de publicação o usuário deverá avançar e executar o processo para realizar a publicação nas redes sociais selecionadas.  
Após a publicação nas redes sociais, o candidato ao acessar essa vaga, será ser direcionado ao formulário de captação de currículos do Fluig, onde através do link criado será capaz de reconhecer o perfil do candidato, origem da rede social e a vaga desejada.

No momento da execução do processo será verificado se a mensagem processada da rede social Twitter possui mais de 140 caracteres. Caso tenha mais de 140 caracteres, a mensagem não será publicada no Twitter, e será exibida mensagem ao usuário informando sobre a restrição.

No histórico das publicações tem como o usuário saber quem foi o responsável pela publicação de acordo com o log in de acesso ao sistema, mostrando quando e em qual rede social cada vaga foi divulgada. Através do histórico será possível publicar novamente a vaga na rede social. As vagas serão publicadas somente nas redes sociais nas quais foram publicadas originalmente.
