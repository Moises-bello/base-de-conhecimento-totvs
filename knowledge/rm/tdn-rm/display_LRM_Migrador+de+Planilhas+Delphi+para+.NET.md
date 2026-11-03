---
content_hash: d17455e037ae85b3fa20d8eda8f3294230dceb956b922b78b1a825757222616a
fetched_at: '2026-06-29T00:08:50.812720+00:00'
page_id: '334340321'
product: rm
source: tdn-rm
title: Migrador de Planilhas Delphi para .NET
type: documentation
url: https://tdn.totvs.com/display/LRM/Migrador+de+Planilhas+Delphi+para+.NET
version: 25
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      Especificação sobre a ferramenta para conversão de Planilhas Delphi para Planilhas RM.

# Introdução

---

      O Migrador de Planilhas Delphi x Planilha RM está em versão beta. Sendo assim, algumas conversões podem não ser bem sucedidas e, desta forma, é altamente recomendável que, ***antes de qualquer execução, sejam realizados backups das planilhas ou até mesmo de sua base de dados***.

false

As planilhas Win32 selecionadas através do aplicativo serão migradas para a **Planilha RM** e não para as planilhas do tipo **Excel**.

# Utilização

---

false

**Instruções para o uso do aplicativo**

1) o aplicativo  deverá ser inserido na pasta de instalação da BibliotecaRM, que por padrão cria o seguinte diretório c:\Totvs\CorporeRM\RM.Net.

2) Deverá ser criado o arquivo de configuração deste aplicativo, com o seguinte nome, “MigradorPlan.exe.config” (este pode ser gerado a partir de uma aplicação Client do RM, por exemplo, o arquivo de configuração “RM.exe.config”. Pode-se criar uma cópia do RM.exe.config e renomear para MigradorPlan.exe.config.

3) O Host RM deverá estar iniciado e em funcionamento (poderá estar como serviço “RM.Host.Service” ou pelo executável “RM.Host.exe”.

4) Ao final do processo de migração das planilhas selecionadas será gerado um log (arquivo txt) será criado na pasta “RM.Net”, contendo informações da migração processada. Exemplo: MigradorPlanLog220217180335.txt

false

*A partir da versão **12.1.21** o MigradorPlan estará disponível no instalador. Nesta versão não será necessário estes passos de forma manual*

**Segue passo a passo e alguns prints demonstrando o processo de migração**

Planilha Delphi X Planilha RMPasso 01

Acesse o MigradorPlan.exe na pasta padrão de instalação do RM ("RM.Net").

Passo 02

Na tela de login do MigradorPlan, informe o Alias, Usuário e Senha do banco de dados. O Alias deve ser criado no BDE (Borland DataBase Engine).

Passo 03

Depois do login, a tela do MigradorPlan será exibida. Somente as planilhas Delphi serão mostradas na listagem e poderão ser marcadas para migração.

Passo 04

Serão selecionados todos os registros através do botão   ou através da seleção manual, conforme exemplo:

false

*Caso queira selecionar uma quantidade “X” de registros, pressione e segure a tecla “Ctrl” do teclado e selecione as planilhas desejadas.*

Passo 05

Depois de selecionado as planilhas clique no botão “Executar migração”. Será exibida uma caixa de dialogo solicitando confirmação:

Clicando em “***SIM***” o processo será executado, em “***NÃO***” o processo será cancelado.

Passo 06

Durante a execução do processo será exibido o andamento da conversão. A duração do processo se dará de acordo com a quantidade de planilhas selecionadas.

Passo 07

Depois da execução, o resultado da migração será mostrado através da aba “Resultado”.

Planilha RM

Depois de todo o processo acima, acesse a aplicação através da nova MDI, selecione o segmento a qual foi convertida as planilhas e vá em "Gestão | Ferramentas de Analise | Planilhas .Net".

false

O alias na nova MDI deverá apontar para a mesma base configurado no BDE para realizar a conversão.

Restauração

Depois do processo de conversão a planilha não será mais utilizada na aplicação Delphi. Caso queira retornar com a planilha, ou seja, reverter o processo será necessário selecionar a “aba” de Restaurar, selecionar a(s) planilha(s) convertidas e clicar em “Restaurar Planilha”.

false

Caso realize o processo de restauração de planilha, a mesma será retornada para a aplicação em Delphi da mesma forma que se encontrava. Ou seja, caso feita alguma alteração na planilha depois da conversão estas alterações não serão salvas na planilha.

A restauração da planilha para a plataforma WIN32 implicará na EXCLUSÃO da planilha já migrada para a plataforma .NET em sua próxima migração!

Caso a planilha migrada já tenha sido alterada, sugerimos exportá-la para que não haja retrabalho por parte de sua empresa.

Depois do processo de restauração será apresentada uma tela informando o log de conversão. Verifique se todas as planilhas foram restauradas com sucesso.

false

Verifique com o suporte do aplicativo se o mesmo possui o aplicativo em Delphi, caso sim, abra o mesmo, acesse o menu de Relatórios > Planilha.

false

*A partir da versão **12.1.23 não será mais possível o uso da Planilha.Net como RMPart nos Cenários**. Permanecendo a inclusão de [Planilhas RM](http://tdn.totvs.com/x/MceFDg) somente.*

falsefalse

**Produto:** Planilha RM

false

**Versão:** 12.1.18 ou Superiores

false

**Processo:** Conversão de Planilha RM para .NET

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
