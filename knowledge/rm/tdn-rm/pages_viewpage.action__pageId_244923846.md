---
content_hash: 7275820aee47a7cd4235ba0a71ba733916906116f9225a4219df5e575718082a
fetched_at: '2026-06-29T00:08:15.749215+00:00'
page_id: '244923846'
product: rm
source: tdn-rm
title: RMPAT00005_Cenários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244923846
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.16. ou superior. |
| **Ocorrência:** | Cenários |
| **Ambiente:** |  |
| **Passo a passo:** | Este recurso permite que sejam criados Cenários com [Moedas e Índices](https://tdn.totvs.com/pages/viewpage.action?pageId=421388563) diferentes, permitindo que os valores dos patrimônios sejam calculados para mais de uma moeda.  Disponível através do **menu Cadastros | Cenários.** Durante o cadastro do cenário deve-se informar a Descrição (campo livre), o [Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=423938333), a Moeda e o Índice, sendo este último não obrigatório.        O cenário cadastrado deve ser associado ao [Grupo de Patrimônio](https://tdn.totvs.com/pages/viewpage.action?pageId=423938277)  para que os valores a serem calculados para o patrimônio respeitem a moeda e o índice (e suas respectivas cotações), bem como o tipo de depreciação (integral ou proporcional).  No cadastro do Cenário pode-se também definir as informações relacionadas ao Default Contábil. Estas informações serão utilizadas, posteriormente, no [Evento Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=423938693) para que seja realizada a contabilização a ser enviada ao sistema contábil.  **Classificação do cenário :**  Contábil ou Fiscal.  O processo de cálculo de Depreciação poderá ser executado a partir da tela de Cenários. Para isto deve-se selecionar o **Cenário desejado | Processos | Calcular Cenário.**    **Observação:** Somente os patrimônios associados a um Grupo de Patrimônio que possui o Cenário em questão terão o cálculo de depreciação gerado. |
| **Observações:** | A criação de um novo cenário de cálculo nos patrimônios possibilita ao usuário a utilização de taxas de depreciação diferentes dos cenários já existentes e, também, a caracterização dos novos cenários como fiscais, para que tenham informações diferentes do(s) cenário(s) que seja(m) contábil(eis). Ou seja, o sistema possibilitará ao usuário ter mais de uma visão sobre o controle do imobilizado de suas empresas, sendo esta visão contábil ou fiscal, como taxas de depreciação diferentes ou não das ditas pela legislação de imposto de renda, dando assim um horizonte diferenciado sobre a vida de seu imobilizado. |
