---
content_hash: a631d34a69a1b454600881b29d2d04f437e3f793715bdff98e0b14b593487f99
fetched_at: '2026-07-02T19:24:26.084749+00:00'
page_id: '520666465'
product: protheus
source: tdn-tec
title: Ofuscamento de dados nos componentes do SmartClient
type: documentation
url: https://tdn.totvs.com/display/tec/Ofuscamento+de+dados+nos+componentes+do+SmartClient
version: 5
---

Ofuscamento de dados nos componentes do SmartClient

|  |  |
| --- | --- |
| Situação | Necessário ocultar ou exibir a qualquer momento os dados de certos componentes do SmartClient. |
| Ocorrência | Decorre da necessidade de adequação a Lei Geral de Proteção de Dados Pessoais (LGPDP). |
| Implementação | O ofuscamento foi implementado nos seguintes componentes:  TGet:   * Para ofuscar/desofuscar os dados basta, a qualquer momento, atribuir um valor lógico na propriedade lObfuscate (ex.: oTGet:lObfuscate := .T.) * Campos do tipo caractere assumirão o mesmo comportamento de campos com TGet:lPassword ativado * Outros tipos de campo (numérico, data...) ofuscarão o conteúdo digitado e manterão o comportamento de máscara, permitindo a entrada/edição normalmente   TMultiGet, TSimpleEditor e TComboBox   * Para ofuscar/desofuscar os dados basta, a qualquer momento, atribuir um valor lógico na propriedade lObfuscate (ex.: oMulti:lObfuscate := .T.) * Independentemente da quantidade de dados, o componente exibirá uma quantidade fixa de asteriscos e assumirá o estado "ReadOnly" * Nenhuma ação de edição por parte do usuário é permitida * O componente ainda pode ser atualizado internamente pelo Advpl via TMultiGet:AppendText() / TSimpleEditor:Load()   TGrid e TCBrowse:   * O ofuscamento é feito por coluna, então para ofuscar/desofuscar os dados basta, a qualquer momento, atribuir um array de valores lógicos na propriedade aObfuscatedCols (ex.: oBrowse:aObfuscatedCols := {.T., .F., .F., .F.}) onde cada posição do array representa a posição da coluna * Independentemente da quantidade de dados, o componente exibirá uma quantidade fixa de asteriscos * Colunas com imagens também ocultam esse tipo de conteúdo * TCBrowse/TGetDados não permitirá que o usuário edite os dados em células de colunas ofuscadas |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-399 * Disponível em builds iguais ou superiores a **19.3.0.1** do TOTVS SmartClient e a **19.3.0.1** do TOTVS Application Server Lobo-Guará 19. * Disponível em builds iguais ou superiores a **17.3.0.18** do TOTVS SmartClient e a **17.3.0.21** do TOTVS Application Server Lobo-Guará. * Disponível em builds iguais ou superiores a **13.2.3.43** do TOTVS SmartClient e a **13.2.3.50** do TOTVS Application Server NG. |
