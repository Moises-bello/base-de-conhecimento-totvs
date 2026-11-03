---
content_hash: ad8b3d69745707206f05ecece8ef8535268b07e19f857b804d66122cf291c755
fetched_at: '2026-06-29T00:11:44.958721+00:00'
page_id: '81789313'
product: rm
source: tdn-rm
title: SMS - Envio de mensagens através de gráfico medidor-  Produtos RM - 11.52
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=81789313
version: 13
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

**Parametrizando o Ambiente** **(Gerenciamento de Alias)**

Acesse o diretório: **C:\totvs\CorporeRM\RM.Net** e edite o aplicativo  RM.AliasManagem.exe realizando a parametrização conforme o exemplo disponibilizado.

**Parametrizando o aplicativo**

Ao acessar o aplicativo o primeiro procedimento será realizar a configuração do Mashups. Este recurso será necessário ser parametrizado para utilização do envio de SMS. O mesmo deverá ser configurado da seguinte forma:

Será apresentada a tela com a conexão estabelecida.

Acesse os parâmetros do sistema realizando a parametrização abaixo:

Em nosso exemplo a seguir realizaremos a inclusão de um gráfico medidor. Este gráfico possuirá uma consulta SQL parametrizada que enviará um SMS para um determinado usuário **(Cadastro de Pessoas)** sempre que o salário do mesmo for reajustado **(dentro da faixa do Gráfico).**

**Acesse o módulo RH e configure a máscara do DDD e telefone conforme exemplo abaixo.**

**Para isto acesse o Menu CONFIGURAÇÕES -> Selecione o ÍCONE (Parâmetros RH) -> Menu: MÁSCARAS**

**Deverá ser utilizado o # e ponto (.)**

**1º PASSO – Definindo o usuário que receberá a mensagem**

**OBS: Na guia IDENTIFICAÇÃO: Parametrize um código de usuário para este cadastro.**

**2º PASSO – Criando o gráfico medidor**

- Deverá ser incluído uma consulta SQL que retorne o valor do salário do funcionário. Exemplo:

**SELECT SALARIO FROM PFUNC WHERE CHAPA = '12345'**

- Acesse o Menu -> GESTÃO -> Selecione o ícone gráficos incluindo um novo, seguindo o exemplo abaixo:

Ao clicar em OK será apresentado o **Assistente de Configuração de Gráfico.**

**Selecione o Tipo Medidor 1 -> Avançar**

Neste momento será possível visualizar o Gráfico Medidor constando o valor do salário.

A mensagem será disparada quando o valor do salário deste funcionário (No cadastro do Funcionários) for alterado.

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
