---
content_hash: c11d834c4d1583a357ec3e2c0c2b47f1bf9c8ae98241b7bf1e81082b76686093
fetched_at: '2026-06-29T00:05:55.207421+00:00'
page_id: '126718269'
product: rm
source: tdn-rm
title: SMS - Envio de mensagens através de gráfico medidor - Produtos RM - 11.52 (cópia)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=126718269
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.52 |
| **Processo** | **:** | SMS |
| **Subprocesso** | **:** | Envio de SMS através de gráfico medidor |
| **Data da publicação** | **:** | 04/10/2013 |

**Enviando SMS via sistema**

O envio de SMS via aplicativo poderá ser configurado para utilização em um gráfico medidor que possua 1 campo retornado por consulta SQL.

Este recurso possibilitará o usuário receber mensagens em seu aparelho Celular, e Smartphones.

**Pre-Requisitos:**

Para utilizar o recurso será necessário possuir **pacote de serviços de SMS** podendo ser adquiridos pela prestadora de serviços TEKENET <http://www.take.net/pt/solucoes/>.

**\*\*\*\*\*\*\*\*\*\*\* NO EXEMPLO ABAIXO IREMOS PARAMETRIZAR UM USUÁRIO, ONDE AO SER REALIZADO ALTERAÇÃO EM SEU SALÁRIO O MESMO RECEBERÁ UMA MENSAGEM (SMS) INFORMANDO QUE O VALOR FOI REAJUSTADO PARA R$ XXX \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

* **Parametrizando o Ambiente** **(Gerenciamento de Alias)**

Acesse o diretório: **C:\totvs\CorporeRM\RM.Net** e edite o aplicativo  RM.AliasManagem.exe realizando a parametrização conforme o exemplo disponibilizado.

1. Acesse a guia de SERVIÇOS.
2. Habilite tais itens:  
   1. Habilitar Alertas de Gráfico;
   2. Habilitar Histórico de Gráficos;
   3. Habilitar envio de email de RSS;
3. Clique em Aplicar.

* **Parametrizando o aplicativo**

Ao acessar o aplicativo o primeiro procedimento será realizar a configuração do Mashups.  
Este recurso será necessário ser parametrizado para utilização do envio de SMS. O mesmo deverá ser configurado da seguinte forma:

1. Acesse o cadastro de Coligadas.
2. Selecione: Processos | Mashups | Gerenciar.
3. Realize a configuração selecionando a Opção: Criar conta do TOTVS Mashups.
4. Preencha os dados e ao confirmar será enviado um e-mail de confirmação da conta.
5. Após confirmação, informe o usuário e a senha para conexão da conta.
6. Clique em OK

Será apresentada a tela com a conexão estabelecida.

Acesse os parâmetros do sistema realizando a parametrização abaixo:

1. Acesse Sistema | Ambiente | Parâmetros | Globais.
2. Selecione a guia de CONFIGURAÇÕES DE SMS.
3. Informe o USUÁRIO e SENHA disponibilizado pela empresa pela prestadora de serviços TEKENET.
4. Clique em OK para finalizar a parametrização.

Em nosso exemplo a seguir realizaremos a inclusão de um gráfico medidor. Este gráfico possuirá uma consulta SQL parametrizada que enviará um SMS para um determinado usuário **(Cadastro de Pessoas)** sempre que o salário do mesmo for reajustado **(dentro da faixa do Gráfico).**

**Acesse o módulo RH e configure a máscara do DDD e telefone conforme exemplo abaixo.****Para isto acesse o Menu CONFIGURAÇÕES -> Selecione o ÍCONE (Parâmetros RH) -> Menu: MÁSCARAS**

**Deverá ser utilizado o # e ponto (.)**

* **1º Passo** – **Definindo o usuário que receberá a mensagem**

1. Acesse módulo Gestão de Pessoas.
2. Menu Acompanhamento | Pessoas | Edite o cadastro do participante que irá receber as mensagens | Dados Pessoais | Endereço Principal.
3. Informe os telefones.
4. Clique em Salvar em seguida em OK.

**OBS: Na guia IDENTIFICAÇÃO: Parametrize um código de usuário para este cadastro.**

* **2º Passo – Criando o gráfico medidor**

- Deverá ser incluído uma consulta SQL que retorne o valor do salário do funcionário. Exemplo:

**SELECT SALARIO FROM PFUNC WHERE CHAPA = '12345'**

- Acesse o Menu -> GESTÃO -> Selecione o ícone gráficos incluindo um novo, seguindo o exemplo abaixo:

Ao clicar em OK será apresentado o **Assistente de Configuração de Gráfico.**

Informe:

1. Tipos disponíveis: Medidor 1.
2. Tamanho do gráfico (pixels)  
   Largura: 400  
   Altura: 300

Clique em **Avançar**.

Informe:

1. Selecione a coluna cujo valor será exibido: SALARIO.
2. Escala
   1. Valor inicial: 0
   2. Valor final: 1000
3. Frequência
   1. Labels: 100
   2. Marcador maior: 100
   3. Marcador menor: 100
4. Faixas de valor:

1. Inclua as faixas de valor conforme imagem abaixo:

*obs.: Neste exemplo quando o salário estiver maior que R$ 500 será enviado uma mensagem para o usuário.*

       b. Ainda na mesma tela, deverá ser selecionado a Ação para a faixa que possibilitará o envio da mensagem informando o salário que foi reajustado.  
           Selecione a faixa e clique em **Configurar Ação**.

* Inclua um título;
* Insira a mensagem que será enviada para o usuário (observe que existe uma regra onde ao utilizar o {0} o valor do resultado será apresentado entre estas chaves;
* Selecione a opção da periodicidade;
* Marque o tipo de ação e clique em OK;

Sugestão de Dados:

Título: Alerta de Mensagem  
Mensagem: Seu salário foi reajustado para R{0}   
Periodicidade: Sempre ao entrar na faixa.  
Tipos de Ação: SMS

5. Será apresentado a mensagem informando que o processo foi executado com sucesso.

Neste momento será possível visualizar o Gráfico Medidor constando o valor do salário.

A mensagem será disparada quando o valor do salário deste funcionário (No cadastro do Funcionários) for alterado.

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
