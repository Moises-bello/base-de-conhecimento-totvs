---
content_hash: ec5188b33d026a6f12e47c4156c82e45f88fdc178b0d5b51066588848686a55a
fetched_at: '2026-06-28T21:35:25.625622+00:00'
page_id: '286511885'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Eventos de auditoria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286511885
version: 44
---

.\*ndice

# Falando de eventos de auditoria...

---

Este recurso é responsável por registrar eventos ocorridos na plataforma com foco em auditoria. Basicamente são registros de criação, edição e remoção de itens de negócio.

Importante!

Para uso desse recurso é necessário obter uma licença especial de **Eventos de Auditoria**. Para saber mais sobre o funcionamento desse recurso, consulte a documentação técnica de .

**buscar**

## Buscar os eventos de auditoria

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Aplicativos**.

**03**. Clique em  **Eventos de auditoria**.

**04**. Na seção **Busca de eventos**, preencha as informações solicitadas:

#f2f2f2#f2f2f2

**Nome do usuário**Nome do usuário que efetuou a ação que foi auditada.

**Recurso**Item referente à ação auditada (Usuário, Papel, Grupo, Processo, Documento, ...).

**Chave**Chave de acordo com o recurso selecionado anteriormente. Por exemplo: a chave do recurso "Usuário" será o login; do recurso "Grupo" será o código do grupo; de "Processo" será o código do processo, e assim por diante.

**Período**Intervalo de datas que se deseja visualizar.

**05**. Clique em **Buscar**.

#f2f2f2#f2f2f2

Na seção **Resultado de Busca** será exibida a listagem com as informações filtradas pelo usuário solicitante referente aos eventos auditados. A coluna **Saiba Mais** proporciona acesso ao detalhamento da atividade, basta acionar o ícone **Saiba mais**.

trueimageVeja a imagem#0897E9INLINE

## Exportar os dados encontrados

---

**01.** Realizar a busca dos eventos desejados conforme o item .

**02.** Clique em **Exportar dados**.

**03.** Aguarde até receber uma notificação com o *link* para *download*.

#f2f2f2#f2f2f2

A exportação gera uma listagem detalhada com todos os dados de auditoria no formato CSV (compatível com softwares de planilha eletrônica como o Microsoft₢ Excel), respeitando os filtros utilizados na busca dos eventos. O tempo de geração do arquivo de dados depende da quantidade de registros gerados na busca e, por esse motivo, a tarefa é executada em segundo plano. Quando finalizada a execução da tarefa, uma notificação é apresentada em tela informando a conclusão da geração do documento. Esta notificação contém o *link* para *download* do arquivo de forma simples e rápida. Caso deseje baixar o arquivo em outro momento, ele ficará salvo na pasta "Meus Documentos" do usuário que solicitou a exportação.

trueimageVeja a imagem#0897E9INLINE

## Excluir os dados de auditoria

---

Não é possível excluir manualmente os dados registrados na auditoria. A exclusão ocorre de forma automática conforme as configurações de histórico realizadas de acordo com o help [Configuração de eventos de auditoria](https://tdn.totvs.com/x/UvBvI).

## Ativar a geração de eventos de auditoria

---

Caso a geração dos eventos de auditoria esteja desabilitada para a empresa em questão, essa tela não será apresentada, somente um aviso sobre como habilitar este recurso.

trueimageVeja a imagem#0897E9INLINE

Para saber como fazer a configuração, acesse [Configuração de eventos de auditoria](https://tdn.totvs.com/x/UvBvI).

oculto
$("b:contains('oculto')").parent().parent().hide();
]]>Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
