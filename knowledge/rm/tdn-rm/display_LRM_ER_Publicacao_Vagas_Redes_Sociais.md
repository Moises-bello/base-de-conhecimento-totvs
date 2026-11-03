---
content_hash: 2b2708e1deb18b4794215defe8e8dac703e0d4315fb79b20349c01799df3ed6a
fetched_at: '2026-06-29T00:05:59.789039+00:00'
page_id: '192093455'
product: rm
source: tdn-rm
title: ER_Publicacao_Vagas_Redes_Sociais
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Publicacao_Vagas_Redes_Sociais
version: 15
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | RHU – DESENVOLVIMENTO RHU006 | **IRM1** | PCREQ-1960 |
| **Requisito1** | PCREQ-1961 | **Subtarefa1** | PDR\_RHU\_RHU006-32 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 O processo para publicação das vagas nas Redes Sociais visa auxiliar o usuário a tornar público as vagas nas maiores redes sociais, obtendo assim uma maior divulgação e consequentemente um maior número de candidatos.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Planejamento e Captação | Alteração | Desenvolvimento > Planejamento e Captação > Painel de Seleção > Vagas > Publicação de Vagas em Redes Sociais | - |
|  |  |  |  |
|  |  |  |  |

**1. Mensagem Customizada para publicação em Redes Sociais**

Será criado no TOTVS Gestão de Pessoas o recurso "Mensagem Customizada" (Configurações>Mensagens Customizadas). Este recurso permitirá a criação de mensagens customizadas para publicações em redes sociais. Para utilização da "Mensagem Customizada" para publicação de vagas nas redes sociais, deverá ser configurado o tipo da mensagem como: "Redes Sociais".

Também será possível incluir parâmetros que serão executados no momento do envio das mensagens.

Os parâmetros na mensagem deverão estar entre colchetes [ ].  
   
 Será possível informar os seguintes parâmetros, todos relacionados ao perfil de vaga:

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

Além disso, deverá ser gerado um link que permita ao candidato o acesso as vagas publicadas. Para tanto, através da função ENCURTARLINK, será possível passar um link como parâmetro, e no momento do envio da mensagem o link será transformado em um link curto. O link a ser encurtado deverá estar entre parenteses, conforme exemplo :  
   
 ENCURTARLINK (<http://www.testes.com.br>)

Abaixo segue exemplo da utilização dos parâmetros na mensagem customizada de publicação em redes sociais.

Descrição completa da vaga:

Vaga: Analista

Descrição da Vaga: Analista de Suporte Pleno para atuação em Help Desk

Salário (Pretensão) + Benefícios : A combinar

Local: Belo Horizonte

Formação Exigida : Formação Superior Completo em TI

Experiência Exigida : Suporte intermediário a usuários de informática, instalação e configuração de hardware, impressoras, smartphones, desktops, notebooks, dispositivos móveis e softwares como MS Office e MS Windows XP, 7, 8.

Experiência Desejada : Conhecimentos básicos de administração de redes, Exchange, VPN, FTP e Telefonia IP.

Data da Abertura da Vaga : 01/11/2014

Data de Encerramento : 30/11/2014

Para candidatar-se a vaga acesse o link abaixo :

http://fluig.contax.com.br/curriculum?vaga=000120&desc=analista&rede=f

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

ENCURTARLIK (http://fluig.contax.com.br/curriculum?vaga=[Codigo do Perfil de Vaga]&desc=[Nome do Perfil de Vaga]&rede=f)

Ao executar o processo de publicação de vagas em redes sociais(conforme prototipos 3,4,5) os parâmetros serão buscados do perfil de vagas selecionado, conforme definido no item 4, a seguir.

**2. Configuração para o processo de Publicação de Vagas em Redes Sociais**  
  
Antes de executar o processo de publicação de vagas em redes sociais, o usuário deverá realizar algumas parametrizações no sistema.

* Para configurar uma conta do facebook favor consultar o anexo : Config RM Facebook.pdf
* Para configurar uma conta do linkedin favor consultar o anexo : Config RM Linkedin.pdf
* Para configurar uma conta do twitter favor consultar o anexo : Config RM Twitter.pdf

Caso o usuário esteja em uma rede protegida por proxy, a configuração deverá ser feita na primeira aba: "Redes Sociais", do cadastro de "Parâmetros Globais".

Após realizar a configuração de contas das redes sociais, o usuário deverá parametrizar quais contas serão utilizadas pelo processo de publicação de vagas nas redes sociais (protótipo 6).  
OBS: Cada rede social somente poderá ter uma conta por rede social parametrizada.

Esse processo poderá ser executado por qualquer usuário logado no sistema e com permissão de acesso na funcionalidade, entretanto, a vaga será publicada no perfil do usuário informado no parâmetro de publicação (protótipo 6).

**3. Publicação de Vagas em Redes Sociais**

Será criado no TOTVS Gestão de Pessoas o processo “Publicação de Vagas em Redes Sociais”. Este processo estará disponível em Painel de Seleção > Vagas da Seleção > Processo > Publicação da Vaga nas Redes Sociais. Este processo tem como objetivo realizar a publicação das vagas do TOTVS Gestão de Pessoas nas redes sociais Facebook,Twitter e Linked in.

O processo de publicação será executado por perfil de vaga e o usuário do RM poderá escolher em qual rede social Deseja publicar a vaga.   
   
O usuário do RM deverá selecionar o perfil de vagas desejado, executar o processo de publicação (conforme protótipo 3) e selecionar as redes sociais no qual deseja publicar a vaga (conforme protótipo 4). Na tela de seleção das redes sociais o usuário deverá selecionar uma mensagem de publicação, que foi criada no recurso "Mensagem Customizada para Redes Sociais" (conforme protótipos 1 e 2). Será obrigatório informar uma mensagem, caso contrário o usuário não conseguirá avançar até a próxima etapa.

Após selecionar as redes sociais e informar as mensagens de publicação o usuário deverá avançar e executar o processo para realizar a publicação nas redes sociais selecionadas.

Após a publicação nas redes sociais, o candidato ao acessar essa vaga, será ser direcionado ao formulário de captação de currículos do Fluig, onde através do link criado será capaz de reconhecer o perfil do candidato, origem da rede social e a vaga desejada.

**4. Controles para o processo de Publicação de Vagas em Redes Sociais**

No momento da execução do processo será verificado se a mensagem processada da rede social Twitter possui mais de 140 caracteres. Caso a mensagem tenha mais de 140 caracteres a mensagem não será publicada no Twitter, e será exibida mensagem ao usuário informando sobre a restrição. Esta verificação será realizada já considerando o retorno dos parâmetros e o link curto, caso seja utilizado. Esta consistência não será realizada para as redes sociais Facebook e Linkedin.  
   
Será criado também um histórico das publicações (conforme protótipos 7 e 8 disponibilizado em Painel de Seleção > Vagas da Seleção > Anexos > Histórico de Publicação de Vagas), para que o usuário saiba quem foi o responsável pela publicação de acordo com o log in de acesso ao sistema, quando e em qual rede social cada vaga foi divulgada. Através do histórico será possível publicar novamente a vaga na rede social. As vagas serão publicadas somente nas redes sociais nas quais foram publicadas originalmente.

## Protótipos de Tela

**Protótipo 01**

****Protótipo 02****

********Protótipo 03********

**********Protótipo 04**********

************Protótipo 05************

**************Protótipo 06**************

****************************Protótipo 07****************************

******************************************Protótipo 08******************************************

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
