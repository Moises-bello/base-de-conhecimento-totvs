---
content_hash: de897ecd631aefbfb0b4d20d319aacef1905e0f1621695a7941f6e33cf493f7e
fetched_at: '2026-06-28T21:35:18.096995+00:00'
page_id: '146969092'
product: fluig
source: tdn-fluig
title: Conversão de Templates anteriores a versão 1.3.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146969092
version: 25
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é informar impactos, soluções e mudanças realizadas nos *templates* padrões de e-mail na versão 1.3.0. 

# Introdução

Os códigos de templates de emails tiveram seus nomes alterados para facilitar a manutenção e para a padronização de nomenclatura.

**Exemplo:** Um evento que se chamava APPROVE\_TASK e tinha seu código de template TPL105, agora tem o código TPLAPPROVE\_TASK. Repare que o padrão de nomenclatura é o prefixo TPL + (Código do evento).

Um arquivo que se chamava TPL105-pt.html foi renomeado para TPLAPPROVE\_TASK-pt.html Esse novo padrão facilitou a manutenção do template. Antes era necessário acessar o arquivo HTML para mapear qual o template que estava sendo alterado.

# Impactos gerais

Foram alterados os códigos e os nomes dos arquivos físicos dos *templates* para o padrão do TOTVS Fluig Plataforma. Os códigos HTML dos *templates* foram alterados para seguir um padrão. Estas mudanças podem afetar clientes e aplicativos de terceiros que utilizam *templates* personalizados.

Nota

Esta mudança afeta apenas os eventos padrão do Fluig Plataforma, ou seja, aqueles disponibilizados nativamente na plataforma. Eventos criados ou personalizados pelo cliente não são considerados padrão.

# Impactos nos códigos Java

As funções que especificavam algum código de evento precisam ser alterados para o novo padrão.

**Exemplo:** Um evento que se chamava APPROVE\_TASK e tinha seu código de *template*TPL105, agora tem o código TPLAPPROVE\_TASK. Repare que o padrão de nomenclatura é o prefixo TPL + (Código do evento).

Nota

Quando não especificado o código ou ele não for encontrado a plataforma Fluig utiliza o *template* *default* de e-mail.

Exemplo de chamada Java para o evento APPROVE\_TASK:

javaImportante

O envio de dados de formulario na primeira atividade, somente irá funcionar se utilizado os scripts beforeStateEntry e afterStateEntry.

Exemplo do novo padrão:

javaImportante

O envio de dados de formulario na primeira atividade, somente irá funcionar se utilizado os scripts beforeStateEntry e afterStateEntry.

Em caso de dúvidas sobre qual o novo código do *template*,  que mapeia os novos códigos com os antigos.

Observação

Os *templates* criados e personalizados pelo cliente, e que portanto não são eventos padrão do Fluig Plataforma, não foram afetados.

# Impactos nos arquivos físicos de template

Os arquivos de *template* padrão também tiveram seus nomes alterados. Os que usavam o *default* agora tem seu próprio *template* e com o seguinte padrão:

Um arquivo que se chamava TPL105-pt.html do evento APPROVE\_TASK foi renomeado para TPLAPPROVE\_TASK-pt.html

O evento APPROVE\_TASK\_RESPONSABLE, que não possuía nenhum *template* agora possui o TPLAPPROVE\_TASK\_RESPONSABLE-pt.html.

Observação

Os *templates* criados e personalizados pelo cliente, e que portanto não são eventos padrão do Fluig Plataforma, não foram afetados.

# Impactos na atualização 1.3.0

Ao atualizar a instalação do Fluig Plataforma para a versão 1.3.0, os *templates* padrão são movidos da pasta tempaltes\tpl (pasta padrão de *templates*) para a pasta templates\tplmail\_backup e os novos *templates* padrão da versão com novo padrão de nomenclatura são adicionados novamente. Portanto, se o cliente alterou algum arquivo físico de algum evento padrão, esse arquivo estará na pasta de *backup* e será necessário o cliente refazer a atualização do *template* do evento.

**Exemplo:**

Se o cliente, na versão anterior, alterou o para o evento CREATE\_DOCUMENT o arquivo *default* de *template* para template\_create\_document-pt.html. O processo de atualização removerá este arquivo e no lugar colocará o novo arquivo padrão TPLCREATE\_DOCUMENT-pt.html e moverá o arquivo template\_create\_document-pt.html para a pasta de *backup*.

Para o usuário voltar a sua versão, é necessário apenas fazer atualizar o arquivo template\_create\_document-pt.html novamente.

Observação

Os *templates* criados e personalizados pelo cliente, e que portanto não são eventos padrão do Fluig Plataforma, não foram afetados.
