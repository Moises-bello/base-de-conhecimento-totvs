---
content_hash: 1fe064579b6f5588cab53d04acce2ee94371ddbd904ddeca5484f42fcb0c6fe9
fetched_at: '2026-06-29T00:11:13.111794+00:00'
page_id: '656324920'
product: rm
source: tdn-rm
title: Opções da proposta salva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656324920
version: 9
---

---

#FF9000Introdução

Após termos uma proposta salva temos outras opções além da edição da própria proposta. Para acessar estas opções basta clicar no ícone com “…” (três pontos) ao lado do ícone de edição da proposta.

Este menu tem diversas opões possíveis que serão descritas a seguir.

#FF9000Validar

Esta opção no menu da proposta só aparece quando a proposta está reprovada. Ela deve ser usada para tentar aprovar uma proposta usando as alçadas do usuário logado no portal. Ao selecionar esta opção o Portal de Imóveis validará a alçada do grupo do usuário logado e se possivel aprovará a proposta.

#FF9000Proposta: imprimir

Imprimir os modelos de proposta. O Portal de Imóveis tem um modelo padrão de proposta de compra, mas o usuário poderá criar um novo modelo usando um documento WORD com tags pré-definidas (idem ao processo de criação de minutas de contrato). Estes modelos devem ser inseridos em *Backend > Empreendimentos > Modelos de Propostas.*

#FF9000Relatório comparativo

Relatório padrão que demonstra a análise financeira da condição de pagamento padrão da unidade comparando com a proposta ofertada pelo cliente.

#FF9000Proposta: Enviar por e-mail

Envia por e-mail o modelo de proposta impresso pelo Portal de Imóveis. Esta opção sempre enviará esta proposta para o e-mail do prospect da proposta e também podemos acrescentar outros e-mails para receberem uma cópia do documento

#FF9000Plano de pagamento: imprimir

Imprime a relação de pagamentos mensalmente de acordo com a proposta formalizada e salva.

#FF9000Plano de pagamento: XLS

Extrai para EXCEL o mesmo plano de pagamento impresso na opção 15.6.5

#FF9000Contrato: imprimir

Imprime o modelo de contrato selecionado. Lembrando que os modelos de contratos podem ser inseridos através da opção *Backend > Empreendimentos > Minutas.*

#FF9000Contrato: salvar Word

Faz download do modelo de contrato desejado no formato WORD pra alteração posterior. Somente grupos de usuários que possuem a opção “Salvar Contrato em WORD” visualizam esta opção.

#FF9000Avançar etapa da proposta

Uma das principais opções do menu da proposta. Ela é responsável por movimentar a proposta dentre as diversas situações possíveis cadastradas em *Backend > Globais > Situação da proposta*. Existe um completo ciclo de parametrização das situações de proposta que formarão o fluxo por onde uma proposta pode passar.

Durante o avançar a etapa da proposta são feitas diversas analises e somente será permitido o avançar a etapa se todas forem atendidas.

Em Avançar para são listadas todas as situações possíveis para uma proposta avançar. Dependendo desta situação, pode ou não ser obrigatório uma justificativa e um motivo para avançar a situação da proposta:

#FF9000Trocar corretor da proposta

Esta opção possibilitará realizar a troca do corretor da proposta.

**Observação:** A alteração do corretor só será possível quando n*ão houver uma reserva ativa para a unidade*. Recomendamos verificar a disponibilidade e status de reservas antes de solicitar qualquer modificação.  
  
Há duas maneiras de efetuar essa troca. Você pode fazer isso através do Menu, escolhendo a opção "Trocar corretor da proposta". Ao selecionar essa opção, você terá acesso aos dados da proposta e poderá indicar o novo corretor responsável, conforme mostrado na tela abaixo:  
  
  
  
A outra opção será através da edição da proposta no campo corretor:

#FF9000Autorizar proposta reprovada

Esta opção somente aparece para usuários cujo grupo ao qual ele pertence tenha permissão em “Autorizar Proposta Reprovada’. Esta opção você encontra em *Backend > Usuários > Aba Grupos.*

Os usuários que possuem esta opção, podem aprovar uma proposta REPROVADA, sem nenhuma validação de alçada, ou seja, mesmo que as condições financeiras da proposta estejam muito abaixo das condições aceitas, esta opção aprovaria a proposta. Podemos dizer que é a opção de mais alto poder na aprovação de propostas reprovadas.

#FF9000Solicitar aprovação

Esta opção aparece para todos os demais usuários que não possuem a permissão de autorizar proposta e que façam uma proposta REPROVADA e possuam usuários SUPERIORES na hierarquia do cadastro de usuários do Portal de Imóveis. Ao clicar nela, será aberta uma janela para podermos enviar uma mensagem ao superior na hierarquia de cadastro de usuários, solicitando que este valide a proposta com a alçada que ele possui, na tentativa de aprovar a  proposta.

O superior receberá um email com o link para acessar o Portal de Imóveis e validar a proposta promovendo-a para uma aprovação, caso ele tenha autonomia.

#FF9000Documentos da proposta

No Portal de Imóveis é possível definir, por empreendimento, quais são os tipos de documentos necessários após a criação de uma proposta. Para criar estes documentos devemos acessar *Backend > Globais > Documentos da Proposta.*

Os documentos de proposta podem ser associados a PROPOSTA ou a PESSOA. Um documento associado a PESSOA deverá ser associado no cadastro de pessoas e seria válido somente para casos em que necessito ter a documentação do cliente antes de realizar a proposta.

Os documentos, depois de criados deverão ser associados aos empreendimentos em *Backend > Empreendimentos > Documentos da Proposta.*

Após os documentos associados, eles serão visíveis no menu da proposta “Documentos da proposta” e ao abrir esta opção aparecerá uma janela onde serão solicitados o upload dos documentos obrigatórios.

#FF9000Documentos da pessoa

Documentação de pessoa seguem os mesmos processos do item de documentos da proposta, a principal diferença é que os documentos que são associados a pessoa podem ser inseridos diretamente no cadastro de pessoas no menu *Pré-Venda > Pessoas,* na aba *Documentos*.

#FF9000Comissão

O Portal de Imóveis pode atribuir automaticamente a comissão do corretor que gerou a venda, mas para isto é necessário ter o percentual de comissão definido. O Portal possibilita que a comissão seja calculada pelo Empreendimento, Usuário, Imobiliária ou grupo de usuário, nesta ordem de precedência, ou seja, se definida uma comissão no cadastro do empreendimento esta irá sobrepor todas as demais.

Uma comissão pode ter seu valor lançado manualmente após proposta feita e entrando no menu de ações da proposta opção COMISSÃO (esta opção só aparece para propostas aprovadas). Ou calculada automaticamente pelo Portal de Imóveis baseado nos percentuais definidos no parágrafo acima. Para isto o parâmetro "Grava Comissão Diretamente" deve estar marcado como SIM.

Se marcado como SIM ao salvar uma proposta o sistema criará automaticamente um valor de comissão. O Portal de Imóveis trata o percentual de comissão definido como sendo o teto de comissão a pagar, não permitido lançar um valor maior que o definido pelo percentual aplicado aos componentes que estão com o FLAG de descontar comissão habilitados.

A comissão é calculada sobre o valor total da proposta multiplicando sobre o percentual da comissão do empreendimento, ou do usuário, ou da imobiliária ou do grupo do usuário, se todos estes campos estiverem zeramos o valor base de comissão e o valor da comissão serão zero.

Caso a soma das parcelas que permitem descontar comissão (demonstrado na imagem) não seja suficiente para pagar toda a comissão calculada, o valor da comissão será limitado no valor do componente que está marcado com Desconta Comissão.

É possível distribuir a comissão entre mais de um usuário, desde que esta não ultrapasse o teto permitido. Para lançar outras pessoas participantes da comissão basta inserir novos usuários clicando em ADICIONAR LINHA DE COMISSÃO.

OBS: No Portal de Imóveis existem parâmetros que permitem que o sistema calcule ou não o valor da comissão automaticamente e parâmetros que definem se uma proposta poderá avançar para próxima etapa sem comissão lançada. Para modificar estes parâmetros acesse Backend e em pesquisa de parâmetros a palavra COMISSÃO. Os parâmetros são:

* Grava comissão diretamente - para que o sistema já gere um valor de comissão para as propostas salvas
* Permitir efetivar propostas sem comissão - permite ou não que uma proposta avance para próxima etapa sem comissão gerada.

A partir da versão 12.1.31 o Portal de Imóveis possui o campo de gerente do empreendimento e a este podemos associar uma comissão que será sempre gerada quando a comissão da venda for calculada. A comissão do gerente abate sobre o percentual de comissão total definido no empreendimento, exemplo:

* Percentual de comissão total: 5%
* Comissão do gerente: 1%

Neste exemplo acima se uma venda for realizada o corretor terá 4% de comissão e o gerente 1%.

O gerente do empreendimento é cadastrado em backend > empreendimentos > comissão .

Sempre quando um gerente de empreendimento estiver associado em um empreendimento, todas as solicitações de aprovação de propostas reprovadas serão enviadas para este gerente e não mais para o superior do corretor que fez a venda.

#FF9000Reservas da unidade

Esta opção demonstra todas as reservas existentes da unidade

#FF9000Mensagens

Neste menu é possível registrar mensagens que ficarão armazenadas na proposta e poderão ser acessadas a qualquer momento. Estas mensagens poderão ser enviadas por e-mail para pessoas específicas.

#FF9000Anexos

Em anexos podemos incluir qualquer documento em uma proposta. Estes anexos não são controlados e não necessitam ser validados. Aqui podemos colocar uma cópia do contrato assinado, documentos recebidos na proposta e qualquer outro arquivo que julgar importante no processo da venda.

#FF9000Log

Na opção LOG podemos acompanhar todas as ações realizadas na proposta. É o melhor local para analisar tudo que aconteceu deste a criação da proposta.

#FF9000Excluir proposta

Para esta opção aparecer ela deve ser habilitada em *Backend > Globais > Situação da proposta*, selecionando a opção “Excluir Proposta’. Uma vez habilitada ela permite que a proposta seja excluída da base de dados do Portal de Imóveis.

#FF9000Excluir proposta no backoffice

Da mesma forma que o item anterior, esta opção somente aparecerá quando habilitada em *Backend > Globais > Situação da proposta.*

A funcionalidade desta opção é excluir uma venda enviada ao TOTVS TCGI, ou seja, finalizamos o processo de vendas e enviamos a proposta para o TOTVS para esta se transformar em venda. Só que identificamos algum erro no processo e precisamos excluir a venda em preparação que foi criada com o processo de exportação da proposta do Portal de Imóveis.  Então quando a situação VENDIDA permite excluir venda no backoffice, o Portal de Imóveis irá apagar a venda que foi criada no TCGI e voltará a situação da proposta para a primeira condição desta (Aprovada ou Reprovada).

Importante: Esta opção só faz sentido ser liberada na situação de proposta VENDIDA, pois ela só funciona para propostas que já foram integradas com o TCGI.

Mais informações

---

* [Propostas - Anexos da Proposta](https://tdn.totvs.com/display/LRM/Propostas+-+Anexos+da+Proposta)
* [Propostas - Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=570059863)
* [Propostas - Contrato: Assinatura Eletrônica](https://tdn.totvs.com/pages/viewpage.action?pageId=572197716)
* [Propostas - Documentos da Proposta](https://tdn.totvs.com/display/LRM/Propostas+-+Documentos+da+Proposta)
* [Propostas - Solicitar Aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=569502880)
