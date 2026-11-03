---
content_hash: 93d1cf0f4c5bd6353616b16fc17da94e57339d495556d1a33e95b75c6ad351ad
fetched_at: '2026-06-29T00:08:56.916719+00:00'
page_id: '351385703'
product: rm
source: tdn-rm
title: DT Emissão de NFS-e para campus em outra filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351385703
version: 10
---

# GERAÇÃO DE MOVIMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional*. |
| **Módulo:** | *TOTVS Educacional.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Geração de movimento. | Geração de movimento. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Geração de movimento em regime de caixa.* | *Geração de movimento em regime de caixa.* | | *Geração de movimento em regime de competência* | *Geração de movimento em regime de competência* | |
| **Cadastros Iniciais:** | *N/A.* |
| **Parâmetro(s):** | *N/A.* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *[DEDUINTEGRACOES-1006](http://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-1006 "Emissão de NF-e para o Campus Porto Alegre")* |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *SHABILITACAOFILIALCAMPUS* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

Alunos em Campus distintos, localizados em municípios diferentes, podem pertencer a uma mesma filial, mesmo que a prestação dos serviços ocorra em outra filial. Porém, devido exigências dos municípios, a NFS-e precisa ser emitida para o município (Filial), na qual o serviço foi prestado.

Para tanto, foi realizada otimização do processo de geração de movimento, permitindo ao sistema, gerar movimentos para uma filial diferente do contexto logado, conforme parametrização do cadastro de Campus da matriz aplicada, como será mostrado abaixo.

Geração de movimentoGeração de movimento em regime de competência

Para parametrizar o sistema para gerar movimento para uma filial diferente da filial do contexto logado, é necessário acessar o cadastro da matriz aplicada e em seguida, acessar o anexo de Campus/Polo da matriz aplicada, conforme ilustram as imagens abaixo:

Figura 1 - Cadastro da matriz aplicada

Figura 2 - Anexo de Campus/Polo da matriz aplicada

Uma vez acessado o cadastro de Campus/Polo da matriz aplicada é possível criar/editar um novo Campus/Polo, definindo para ele a filial para qual serão gerados movimentos, conforme a figura abaixo. Não existindo uma configuração específica para o Campus/Polo da matriz aplicada, o movimento será gerado para a filial do contexto logado.

Figura 3 - Parametrização da filial considerada para a geração de movimento.

Após a parametrização da filial para qual o movimento será gerado, é necessário que o aluno, cujo o contrato esteja associado a matriz aplicada,  esteja também matriculado no Campus/Polo parametrizado anteriormente, conforme mostra a imagem abaixo:

Figura 4 - Aluno matriculado no Campus/Polo 1 da matriz aplicada

Após seguir esses passos, a geração de movimento poderá ser gerada. O exemplo abaixo mostra a geração de movimento para a filial 2 para um contrato da filial 1.

Figura 5 - Usuário logado na filial 1

Figura 6 - Geração de movimento para a 1ª competência do contrato

Figura 7 - Movimento gerado com sucesso

Figura 8 - Movimento gerado para a filial 2

Geração de movimento em regime de caixa

Para parametrizar o sistema para gerar movimento para uma filial diferente da filial do contexto logado, é necessário acessar o cadastro da matriz aplicada e em seguida, acessar o anexo de Campus/Polo da matriz aplicada, conforme ilustram as imagens abaixo:

Figura 1 - Cadastro da matriz aplicada

Figura 2 - Anexo de Campus/Polo da matriz aplicada

Uma vez acessado o cadastro de Campus/Polo da matriz aplicada é possível criar/editar um novo Campus/Polo, definindo para ele a filial para qual serão gerados movimentos, conforme a figura abaixo. Não existindo uma configuração específica para o Campus/Polo da matriz aplicada, o movimento será gerado para a filial do contexto logado.

Figura 3 - Parametrização da filial considerada para a geração de movimento.

Após a parametrização da filial para qual o movimento será gerado, é necessário que o aluno, cujo o contrato esteja associado a matriz aplicada,  esteja também matriculado no Campus/Polo parametrizado anteriormente, conforme mostra a imagem abaixo:

Figura 4 - Aluno matriculado no Campus/Polo 1 da matriz aplicada

Após seguir esses passos, a geração de movimento poderá ser gerada. O exemplo abaixo mostra a geração de movimento para a filial 2 para um boleto da filial 1.

Figura 5 - Usuário logado na filial 1

Figura 6 - Geração de movimento para um determinado boleto

Figura 7 - Movimento gerado com sucesso

Figura 8 - Movimento gerado para a filial 2
