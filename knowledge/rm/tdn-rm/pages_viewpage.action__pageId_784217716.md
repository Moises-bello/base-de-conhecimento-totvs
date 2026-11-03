---
content_hash: fabc7294e2b5ba675e3206f9909a09ce2acf5bffb12397526889ae76d2c348eb
fetched_at: '2026-06-29T00:11:38.304305+00:00'
page_id: '784217716'
product: rm
source: tdn-rm
title: Cópia de Checklist para retirada do RDP - Visão do Desenvolvedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784217716
version: 1
---

# Objetivo

---

Este documento contém uma lista de instruções a serem seguidas pelos produtos, com o objetivo de não utilizarmos mais o GoGlobal ou TS.

# Checklist

---

Abaixo estão listadas as instruções à serem seguidas:

* OBS.: Trataremos o client como RM.exe (MDI) e servidor de aplicação RM.Host.

1. As telas do produto não podem depender de um volume alto de dados na parte client, ou seja, o processamento de dados e cálculos de negócio devem ser feitos do lado do servidor de aplicação.
2. As visões de dados devem trazer somente as colunas essenciais para tal finalidade, o restante das colunas deverão aparecer somente na edição.
3. As visões de dados não podem obrigar o usuário, de alguma forma, a trazer um volume alto de registros para realizar algum cálculo, por exemplo:

1. Se existir um processo que geralmente é executado para um volume alto de registros, este não deve depender da marcação destes registros na visão, senão o usuário será obrigado a trazer todos os registros para o client e então executar o processo.
2. Um cálculo em cima dos dados de vários registros não pode ser feito no client a partir do binding source da visão, este deve ser realizado do lado do servidor de aplicação.

4. Caso haja um cadastro em que seja necessário anexar arquivos de imagem, é necessário limitar o tamanho do arquivo a ser inserido no cadastro. O componente de imagem da Lib já tem este recurso.
5. Chamadas ao servidor que trazem volumes de dados muito pequenos, mas que são feitas em todas as telas devem ser “cacheadas” no client utilizando o CacheService  da Lib. Por exemplo:

1. Checagem de segurança extra.
2. Verificação de integração habilitada.
3. Preferência de usuário.

6. NUNCA deve-se fazer chamadas do client para o servidor dentro de loop/laço. Se for necessário, uma única chamada deve trazer todos os dados necessários do servidor e dentro do loop tratar este conjunto de dados.
7. NUNCA devemos fazer cache ou reutilização de objeto proxy para chamadas ao servidor. Isso significa que quando for necessário fazer chamadas ao servidor, deve-se criar um novo objeto RMSServer através do RMSBroker e não armazenar este objeto dentro de uma propriedade do escopo da classe e muito menos em uma propriedade ou variável estática.
8. Deve ser evitado o carregamento e armazenamento de grande volumes de dados do lado servidor de aplicação, pois o elevado gasto de memória implica em custo.
9. As execuções paralelas (Parallel, Parallel.ForEach, etc) devem ser utilizados com cautela no servidor de aplicação, pois isso implica no altgo consumo de CPU, consequentemente em custo.
10. A manipulação de arquivos em disco devem ser feitas exclusivamente utilizando as classes RMSFileServer no servidor de aplicação e FileServerClient na parte client. Isso é necessário, pois em ambientes cloud não temos controle sobre em quais servidores cada rotina é executada, logo temos que ter um repositório centralizado de arquivos e essas classes já fazem todo o trabalho de forma transparente.
11. Nenhuma rotina deve exigir do usuário informações sobre o servidor de banco de dados.
12. Nenhuma rotina deve exigir que a estação tenha instalado o Office da Microsoft.
13. Nenhum rotina que faça login via serviço (GSERVICO) ou anônimo deve utilizar o parâmetro DEFAULTDB mais. Fizemos uma implementação para a aplicação rodar no formato MultiTenancy, desta forma para que não tenhamos problemas futuros o alias deve ser recuperado pelo método *RMSUtils.GetCurrentAliasWithoutPrincipal().*
14. A aplicação deve rodar com performance satisfatório com uma largura de banda de no máximo 128 Kbps (Kbits, não KBytes). Para os testes temos disponíveis licenças do software Net Limiter que faz o trabalho de reduzir a banda utilizada por uma aplicação.
15. Sugerimos ligar o parâmetro LOGWCFCALLS no config do RM.exe na execução dos testes. Este parâmetro habilita um log que registra cada chamada ao servidor de aplicação e seus respectivos tempos. Para visualizar o log basta pressionar CTRL + SHIFT + F9 após abertura de qualquer tela.
16. Todas as integrações devem ser realizadas via WebService do Host, não podemos realizar acesso direto ao banco de dados.
falsefalse

**Produto:** Framework

false

**Versão:** 12.1.19

false

**Processo:** Check List para retirada do RDP

falsefalse

**Status:** Em desenvolvimento

false

**Data:**

false

**Autores:**
