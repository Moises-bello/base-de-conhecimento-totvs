---
content_hash: 208056eb7550d6bb0dbb692c3144a9cb088b6bf80c7560a8f8de615f7cac150c
fetched_at: '2026-06-29T00:11:39.138314+00:00'
page_id: '788600039'
product: rm
source: tdn-rm
title: Aceleração - RM Reports - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=788600039
version: 12
---

Estará disponível em breve

https://tdn.totvs.com/download/attachments/788600039/dashboard.png?version=1&modificationDate=1753800642456&api=v2Ok, entendiApenas para avaliação de clientes pilotosEstamos em versão Alpha

# Aceleração para o Smart View

---

Como parte do esforço de transição do *RM Reports* para o *Smart View*, foi desenvolvido o **Acelerador de Migração para o Smart View**. Essa ferramenta é capaz de analisar o relatório do *RM Reports* e acelerá-lo para uso no *Smart View* em pouco tempo e, caso exista alguma limitação no relatório que impacte na sua versão para o *Smart View*, essa limitação é exibida ao usuário e através do código da limitação, é possível encontrar orientações acerca de como proceder para que a limitação seja corrigida e a transição do relatório seja o mais tranquila possível.

falseÉ necessário reforçar que se trata de um ***Acelerador* de Migração** e não de um Migrador propriamente dito e, por se tratarem de ferramentas de Geração de Relatórios diferentes (*RM Reports* e *Smart View*), alguns elementos não poderão ser migrados em escala 1:1 e deverão ser adaptados.

Relatórios do **Book** (TOTVS Compartilhamento) **não serão acelerados**.

Relatórios que utilizam Filtro do RM, serão acelerados sem levar o filtro para o novo relatório.

No SmartView, adicione o filtro ao novo relatório utilizando os recursos de Filtro,  ou   
Exemplo de construção de filtros:

PermissionamentoÉ recomendado que esteja bem identificada a importância da aceleração de relatórios para o Smart View e portanto, apenas usuários com conhecimento avançado no desenvolvimento de relatórios devem ser responsáveis por analisar e decidir ou não pela aceleração destes relatórios. Por isso, foi determinado o permissionamento deste módulo da seguinte maneira:

Para acesso ao ***Acelerador de Migração***, bem como acompanhar, visualizar possíveis limitações, determinar com "Parece bom" e "Necessita de adaptação", deverá ser concedido o seguinte acesso.

Nos bastidores, a aceleração ocorre em três etapas:

1. É gerado um **Objeto de Negócio Dinâmico** referente à este relatório
2. O layout do relatório é convertido para o padrão que o *Smart View* espera.
3. A comunicação com o *Smart View* é iniciada e o relatório acelerado é enviado para o *Smart View* e disponibilizado dentro do RM.

## Objeto de Negócio Dinâmico

---

O **Objeto de Negócio Dinâmico** é um Objeto de Negócio feito utilizando os recursos do *RM Reports* que são exclusivos ao RM. Este Objeto de Negócio é gerado automaticamente ao acelerar um relatório *RM Reports* e possui informações referentes à todos os controles do relatório. Ele se diferencia dos outros já disponíveis na integração **RM x Smart View** por permitir que ferramentas não disponíveis no Smart View (Como expressão e fórmula) sejam utilizadas para gerar e retornar dados para o relatório.

## O Layout

---

Após a criação do **Objeto de Negócio Dinâmico** com base na estrutura de dados do relatório, o acelerador irá converter o **Layout** do relatório propriamente dito para um formato que o Smart View reconheça. O resultado desta conversão é um arquivo XML que será criptografado e enviado ao Smart View. Caso seja de interesse do usuário, é possível reaproveitar este mesmo Layout no Smart View e utilizar outro Objeto de Negócio que não o Objeto de Negócio acelerado junto do Layout para exibição de dados.

## Disponibilização no Smart View

---

Após a criação do Objeto de Negócio Dinâmico e conversão do Layout RM Reports em Layout Smart View, um arquivo criptografado contendo as informações do relatório é enviado ao Smart View e após a importação do relatório, este é registrado para uso no RM. A partir deste momento o relatório foi completamente acelerado e está disponível para uso como qualquer **Recurso Smart View**.

## Limitações

---

A aceleração possui algumas limitações, pelo fato da arquitetura e funcionamento do Smart View apesar de ser similar, não é idêntica ao RM Reports. Mais informações e auxílios acerca destas podem ser encontrados na página de .

# Índice:

---

Nas páginas seguintes você encontrará informações acerca de como realizar a aceleração de relatórios do **RM Reports** para o **Smart View**, suas limitações e outras relevâncias.

true

Índicefalsefalse

**Produto:** Framework

false

**Versão:** -

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO

GreyRelease Alpha
