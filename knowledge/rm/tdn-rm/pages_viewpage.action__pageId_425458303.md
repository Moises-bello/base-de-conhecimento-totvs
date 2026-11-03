---
content_hash: 99273dd1f59283fd69fecdafddd1d96a5af4facdcbcfcaef033b824d904e8bd3
fetched_at: '2026-06-29T00:09:29.834475+00:00'
page_id: '425458303'
product: rm
source: tdn-rm
title: Documentação do candidato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458303
version: 5
---

Esse serviço que também se apresenta na forma de anexo da tela "Inscrição de Candidato" torna possível gerenciar a entrega de documentos por um candidato. A visão apresentará entradas para todos os candidatos inscritos em áreas ofertadas por processos seletivos que exijam entrega de um ou mais documentos. Para cada candidato e cada documento exigido para ele haverá uma entrada na lista.

Quando o usuário editar o registro ele terá acesso a duas guias: "Identificação" e "Status do Documento". - Na "Identificação" que é "somente leitura" ele visualizará em detalhe as configurações definidas para o documento dentro do processo seletivo. O campo "Obrigatório" informa sobre a obrigatoriedade de entrega do documento.

Na guia "Status do Documento" o usuário poderá indicar se a instituição considera que o documento foi entregue pelo candidato. O usuário terá, ainda, a opção de inserir um texto informando o motivo pelo qual o documento entregue pelo candidato tenha sido recusado.

Agora o serviço de Matrícula do Processo Seletivo RM do TOTVS Educacional, utilizará informações de documentos do candidato do processo seletivo para integrar aos documentos exigidos do curso do aluno. São estes:

* Código do documento, Quantidade - definidos em documentos exigidos da Área ofertada do Processo Seletivo.
* Status (Entregue / Não entregue), Motivo - informados em Inscrições, anexo Documentos do candidato.

No momento de realizar a matrícula, o TOTVS Educacional utilizará estes dados para obter os documentos entregues do candidato e importará para o TOTVS Educacional os documentos que são iguais aos documentos parametrizados por curso.

À partir da versão 12.1.24 será possível vincular um arquivo do candidato a um documento:

* Botão 1 ("..."):  o sistema irá listar todos os arquivos que o candidato possuir (Candidato → Anexos → Arquivos do candidato) que ainda não possuem vínculos com um documento. Para evitar que um arquivo seja vinculado a mais de um documento, ao vincular um arquivo a um documento, este não será mais exibido na lista de arquivos para vincular, somente arquivos que não possuem vínculos que serão exibidos.
* Botão 2 ("Anexar arquivo"): este botão permite anexar um arquivo diretamente no documento, o arquivo será salvo nos "arquivos do candidato" e já é feito o vínculo com o documento, este botão também permite alterar um arquivo de documento.
* Botão 3 ("Visualizar arquivo"): este botão permite visualizar o arquivo.
