---
content_hash: d386f485c771267da2da6383633b2253df5903b92fc9f40958dc5aa7bca3f7c4
fetched_at: '2026-06-28T21:35:22.919758+00:00'
page_id: '242391931'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Lista mestra da pasta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242391931
version: 56
---

# Falando de lista mestra da pasta...

---

A  lista mestra é uma lista ou relatório gerado de acordo com os filtros que você seleciona. Ou seja, a lista mestra de uma pasta é uma lista contendo todos os seus documentos, podendo listar também os documentos presentes em suas subpastas, se assim for definido.

É possível determinar quais características dos documentos devem ser consideradas na geração da lista mestra, como por exemplo, solicitar que sejam exibidos os documentos que possuem data de expiração com o intuito de saber quais já estão expirados e quais estão prestes a expirar.

Este recurso pode ser usado ainda como um relatório a ser apresentado como requisito para obtenção do certificado da norma ISO. Os campos da lista gerada são selecionados pelo usuário, desde que o mesmo tenha a permissão necessária sobre as pastas, e posteriormente são apresentados na lista mestra. Caso determinado campo não esteja presente nas opções de geração de lista mestra, é possível ainda gerar um relatório personalizado que poderá ser exportado para o formato Excel.

Para mais informações sobre desenvolvimento de relatório confira a documentação [Desenvolvimento de Relatórios](http://tdn.totvs.com/x/KAJzB).

## Obter a lista mestra da pasta

---

Importante

Por padrão, a lista mestra irá retornar todos os dados. Podendo mostrar também dados definidos de acordo com a seleção de dados, descritos no item 03.

Se for marcada alguma destas opções, além dos dados já mostrados por padrão na lista, também serão adicionados os dados referentes a cada opção selecionada.

**01.** Selecione as pastas que devem ser apresentadas na lista mestra.

**02**. Clique em **Mais** localizado na barra de ações da parte superior esquerda da janela e em seguida clique em **Lista mestra**.

**03**. Defina os dados que devem ser considerados ao gerar a lista mestra da pasta.

#f2f2f2#f2f2f2

**Documentos em sub-pastas**  
Quando assinalado, exibirá documentos que estão em subpastas da pasta selecionada.

**Documentos expirados**  
Quando assinalado, exibirá documentos que possuem data de validade e estão expirados

**Documentos não liberados**  
Quando assinalado, exibirá documentos que possuem data de validade posterior à data atual.

**Status de aprovação**  
Quando assinalado, exibirá o histórico de aprovação de documentos que exigem aprovação. O usuário deverá selecionar os tipos de documentos a serem exibidos:

* Reprovados
* Em aprovação
* Aprovados

**Documentos com histórico de aprovação**Quando assinalado, exibirá o histórico de aprovação de documentos que exigem aprovação. Ao assinalar esta opção, deverá ser definido se serão mostrados ou não os documentos aprovados no histórico, através da opção **Não mostrar os aprovados no histórico**.

***Log* de cópia controlada**  
Quando assinalado, exibirá o log de cópia controlada de documentos.

**Cota consumida**  
Quando assinalado, exibirá a cota consumida da pasta.

**Tipo de documento**Exibirá o tipo ou extensão do documento ao qual a pasta pertence, podendo ser definido entre: **Todos**, **Contrato**, **Financeiro** ou **Genérico**

**Publicador**Permite filtrar pelo usuário publicador dos documentos.

**Autor**Permite filtrar pelo usuário autor dos documentos.

**Data de atualização**  
Permite selecionar a data de atualização do documento.

**04.** Clique em **Criar lista**.

#f2f2f2#f2f2f2

Uma nova tela será aberta, contendo os dados solicitados.

É possível imprimir a lista mestra da pasta acionando **Imprimir**.

**05.** Clique em **Exportar para o Excel.**

#f2f2f2#f2f2f2

O download da lista será feito automaticamente.

oculto

[Get the folder's main list](https://tdn.totvs.com/display/HFE/Get+the+folder%27s+main+list)

[Obtener lista principal de la carpeta](https://tdn.totvs.com/display/HOE/Obtener+lista+principal+de+la+carpeta)

$("b:contains('oculto')").parent().parent().hide();
]]>Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
