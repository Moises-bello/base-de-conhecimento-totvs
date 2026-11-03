---
article_id: 360021322032
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: f41e1078058520c59d333757617001622fa1590d1848263d69e1fe3e4ccb39f6
fetched_at: '2026-06-28T22:37:21.496014+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como Excluir ou Zerar
  o Saldo de um Produto / Item do contrato ?
type: support-article
updated_at: '2026-06-01T14:50:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021322032-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-Excluir-ou-Zerar-o-Saldo-de-um-Produto-Item-do-contrato
---

**Dúvida**

Como Zerar o Saldo do produto do contrato ?

**Ambiente**

Microsiga Protheus – Gestão de Contratos – A partir da versão 12

**Solução**

No padrão do módulo de Gestão de Contratos não existe uma Funcionalidade ou Tipo de Revisão para realizar a exclusão, "troca" ou alteração de produtos dos itens de uma planilha do contrato.

No caso da situação de um item que não será mais utilizado, a possibilidade é "zerando" o saldo deste item da planilha.

Pode-se realizar os seguintes passos:

**1.** Pode-se utilizar o tipo de revisão **Aditivo de decréscimo**, cadastrado conforme abaixo:

Cadastre um tipo de revisão de ativo em cadastros >tipos>revisões. O Campo Tipo selecione Aditivo, Modo = Ambos ou Decréscimo e Espécie = Quantidade ou Quantidade/Prazo. Ao utilizar este tipo de revisão, o campo de quantidade será habilitado durante o processo (*campo não habilitado para contrato/planilha de Serviço - vide Observações ao final do artigo*).

Podem também ser utilizados os Tipos de revisão de *"Renovação"* ou *"Aberta"* para estas alterações.

**2.** Para zerar o item da planilha, basta alterar sua **quantidade**, igualando-a com a **quantidade medida** (esta informação estará disponível na linha do item no momento da revisão), assim o saldo será zerado automaticamente.

**3.** Clique em Outras Ações: Atualizar o cronograma financeiro e atualize o cronograma financeiro conforme os parâmetros definidos na Aba "Parâmetros/Revisão", ou alterando manualmente os valores das parcelas de modo a zerar seus saldos assim como do item do contrato, onde por premissa o montante do cronograma financeiro e o Valor Total da Planilha contrato devem ser iguais.

**4.** Posteriormente realizar a aprovação da revisão realizada para a mesma ficar "Vigente".

***Obs1:***

Caso exista um título tipo=PR no módulo financeiro, com saldo restante de parcela do cronograma e esta parcela for zerada, o mesmo será excluído.

***Obs2:***

Após Realizar os procedimentos acima, se o saldo da planilha ficar com um valor negativo. Será necessário verificar as casas decimais dos campos de quantidade.

Para esse ajuste utilizar a documentação:

<https://tdn.totvs.com/display/public/PROT/GCT0016_Quantidade_Casas+Decimais_Contrato_GCT>

***Obs3:***

Esta alternativa acima existente de se zerar saldo de produto ou de parcela de Cronograma Financeiro, não tem funcionalidade para contratos/Planilha do Tipo Servico, que são configurados conforme o artigo abaixo onde o campo de "Quantidade" do item da planilha não é habilitado para alteração conforme o seu conceito :

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais as configurações para utilização de Contrato / Planilha de Serviço no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053570234-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-as-configura%C3%A7%C3%B5es-para-utiliza%C3%A7%C3%A3o-de-Contrato-Planilha-de-Servi%C3%A7o-no-Gest%C3%A3o-de-Contratos-?source=search)

***Saiba Mais:***

[Como zerar o saldo de um produto do contrato?](http://tdn.totvs.com/pages/viewpage.action?pageId=235588459)

[Tipos de Revisões de Contrato](https://tdn.totvs.com/pages/releaseview.action?pageId=224447795)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os tipos de Revisão disponíveis no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-tipos-de-Revis%C3%A3o-dispon%C3%ADveis-no-Gest%C3%A3o-de-Contratos)

[MP - SIGAGCT - Como Alterar Produto em um Contrato Vigente ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059003154)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
