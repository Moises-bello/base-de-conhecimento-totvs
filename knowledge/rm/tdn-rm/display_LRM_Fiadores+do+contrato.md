---
content_hash: dd7d9ab795bbc7fa245874471d4e4c9520d2f49aefa3739d3cc785dd018bec14
fetched_at: '2026-06-29T00:11:17.959801+00:00'
page_id: '682442514'
product: rm
source: tdn-rm
title: Fiadores do contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Fiadores+do+contrato
version: 7
---

Essa tela é responsável por incluir ou editar os fiadores de um contrato.

Essa funcionalidade foi liberada à partir das versões: ***12.1.33.245***, ***12.1.34.149***, ***12.1.2205.108***.

No ato **finalização** da [matrícula por período letivo](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=425458883) ou [rematrícula online](https://tdn.totvs.com.br/pages/viewpage.action?pageId=354471683), os [fiadores](https://tdn.totvs.com.br/display/LRM/Fiadores) previamente associados ao aluno são vinculados, automaticamente, ao contrato, na tabela SCONTRATOFIADOR, desde que esses fiadores estejam ativos e com status diferente de rejeitados.

Nessa tela é possível fazer a inclusão de um fiador adicionado, posteriormente, à matrícula do aluno ou alterar algum status de algum fiador associado. Para isso, devem ser observadas as seguintes regras:

* Somente fiadores que estão vinculados ao aluno com **status aprovado** e que estejam **ativos** poderão ser ativados no contrato;
* O status "substituído" será utilizado apenas para identificar os fiadores que foram substituídos durante o processo de troca;
* Não poderão ser associados ao contrato do aluno (SCONTRATOFIADOR), os fiadores que não estejam previamente associados ao aluno (SFIADOR);
* Fiadores em processo de [troca](https://tdn.totvs.com/x/xCnFK) não poderão ter seu status modificado nessa tela, esse controle será feito na aprovação ou rejeição da troca.

Mais informações: [Processo de troca de fiadores](https://tdn.totvs.com/x/xCnFK)

Para a liberação de acesso ao anexo, é necessária a definição de uma permissão no perfil do usuário.

Caminho: *Educacional | Financeiro / Contábil | Contratos | Contratos | Fiadores do contrato*
