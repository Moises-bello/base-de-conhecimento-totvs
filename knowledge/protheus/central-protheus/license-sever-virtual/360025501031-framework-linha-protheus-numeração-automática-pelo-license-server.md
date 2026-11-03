---
article_id: 360025501031
category: License Sever Virtual
content_hash: fce323d90461b63648d6e63c5b714fea443c5efc68a4ea3ea426529111995e8d
fetched_at: '2026-06-28T22:42:20.071681+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - Numeração automática pelo License Server
type: support-article
updated_at: '2026-01-27T17:25:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025501031-Framework-Linha-Protheus-Numera%C3%A7%C3%A3o-autom%C3%A1tica-pelo-License-Server
---

**Dúvida**  
Como configurar o tipo de numeração automática que meu ambiente irá utilizar?  
  
**Ambiente**  
Protheus - AppServer - A partir da versão 11  
  
**Solução**  
Para a utilização de numeração automática, é recomendável que se utilize o modo de controle via License Server (Enablenumber=1).

|  |
| --- |
| Informação: O desempenho da numeração automática pelo License Server é muito superior ao utilizado nas tabelas SXE/SXF, há um grande ganho de performance. |

A numeração das tabelas em License Server é armazenada em memória, enquanto o License Server está ativo. Quando o serviço do License Server é parado, é criado um arquivo chamado LSNumber.val na pasta do Application Server. Neste arquivo são gravadas as últimas sequências das chaves em uso no License, das tabelas que possuem numeração automática. Quando o License é reiniciado, esses dados são lidos desse arquivo e carregados em memória novamente, para dar continuidade na sequência da numeração automática.  
  
Caso o License Server seja parado de forma inesperada, como uma queda de energia ou fechamento inadequado, o arquivo não é gerado, e não reinicialização do License, as informações da última numeração são lidas diretamente das tabelas no banco e carregadas em memória.  
  
Nota:  
Caso necessário, a geração do arquivo pode ser desligada, adicionando a linha Numberval=0 na seção [LicenseServer] do arquivo appserver.ini do License.  
  
Caso ocorra algum problema na numeração automática, de sequência incorreta por exemplo, é necessário tomar as medidas abaixo:  
- Executar a rotina APCFG110 pelo Configurador, para fazer o **Acerto de Numeração Automática** (mais detalhes sobre a rotina, abaixo)  
- Se houver uma numeração discrepante na sequência da tabela, como por exemplo, alguma numeração iniciada com uma letra, em meio a uma sequência de números (no banco de dados, as letras vem depois dos números, então o código iniciado com letra vai ser considerado o último número da sequência, depois de qualquer número), toda vez que o servidor for reiniciado, esse código virá incorreto. Desta forma, recomendamos abrir a tabela manualmente e efetuar a correção, caso seja possível. Caso tenha dúvidas nesse processo, favor entrar em contato com a equipe responsável pelo respectivo módulo responsável por esta tabela.  
  
  
**Rotina APCFG110**  
  
Esta rotina precisa ser inserida manualmente no menu do Configurador. Ao executá-la, são exibidas a numeração atual e a próxima numeração das tabelas, podendo ser editada essa informação para corrigir a sequência.  
  
Para criar a chamada de menu:  
1. Acesse o Configurador > Ambiente > Cadastros > **Menu**  
2. Selecione somente o menu no Configurador clicar em **OK**  
3. Adicione o menu para a coluna **Novo Menu**  
4. Selecione onde deverá ser **salva** a rotina   
5. Clique em **Novo Item**  
6. Preencha o **nome**  
7. Em **Programa** digite **APCFG110**  
8. Selecione o módulo **Configurador** e clique em **OK**  
9. Gere o menu como **SIGACFG**  
10. Saia do Configurador e entre novamente para visualizar a **nova rotina**  
  
  
**CRIASXE**  
  
Para ambientes que possuam lacunas na numeração automática, é possível utilizar o ponto de entrada CRIASXE, que consegue varrer a tabela e setar a numeração.  
Maiores informações sobre a CRIASXE: <http://tdn.totvs.com/pages/releaseview.action?pageId=6815179>  
  
  
**Múltiplos Ambientes utilizando o mesmo License Server**  
  
Quando sua estrutura possui mais de um ambiente (mais de um Appserver) apontando para o mesmo License Server, a numeração de uma base pode influenciar na outra. Por isso, é necessário configurar a chave SpecialKey no arquivo appserver.ini de cada base, para que cada ambiente possua uma chave diferente no License Server.  
Maiores informações de como configurar a chave SpecialKey:  
<http://tdn.totvs.com/display/tec/SpecialKey>  
  
  
**Alteração de modo: SXE/SXF para License Server**  
  
Ao alterar o modo de numeração para o modo License Server (Enablenumber=0 para Enablenumber=1) as tabelas SXE e SXF serão deletadas no momento em que acessar a primeira rotina que utilize numeração automática, e nesse momento, o License Server irá buscar a última numeração de cada tabela com numeração automática, e carregar em memória. Desta forma, recomendamos que faça um *backup* das tabelas SXE e SXF antes de alterar o modo de numeração, e após a alteração, caso a numeração esteja na ordem incorreta, utilizar a rotina APCFG110 para acertar.  
  
  
**Como alterar o modo de numeração automática**  
  
A alteração do modo de numeração automática é feita no arquivo appserver.ini do License Server, na seção [LicenseServer]. Enablenumber=0 é pelas tabelas SXE/SXF. Enablenumber=1 é no License Server (padrão).  
  
Exemplo:  
  
Numeração nas tabelas SXE/SXF:  
[LicenseServer]  
Enable=1  
Enablenumber=0  
  
Numeração no License Server:  
[LicenseServer]  
Enable=1  
Enablenumber=1  
  
Obs.: se não existir a linha Enablenumber na seção [LicenseServer], assume-se o padrão, que é numeração no License Server.
