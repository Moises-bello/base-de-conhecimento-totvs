---
content_hash: 568a77325e461aa4a07e02c5e899005810ab728adac54970d38a6d05f1f3acb4
fetched_at: '2026-06-29T00:11:03.487550+00:00'
page_id: '623893573'
product: rm
source: tdn-rm
title: Parâmetros - Proposta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=623893573
version: 12
---

| Parâmetro |
| --- |
| **Criar interesse no instante que cria a proposta** Defina se ao criar uma proposta o sistema deverá também criar automaticamente interesse vinculado ao CPF/CNPJ contido na proposta |
| **E-mail de notificação de reserva estendida** Ao atribuir valor a este parâmetro, todas as vezes que uma reserva for estendida, os e-mail(s) atribuídos a este receberão uma notificação via e-mail informando que a reserva foi estendida. Para informar mais de um endereço de e-mail separe-os por ponto vírgula. Exemplo: [email1@email.com](mailto:email1@email.com);email2@[email.com](http://email.com);email3@[email.com](http://email.com) ... |
| **ID's de situações de propostas não contabilizada na contagem total de propostas realizadas nos gráficos padrões** Informe o(s) ID's das propostas delimitas por vírgula, caso informe mais de um ID. Exemplo: 1,3,5,7, ... Para saber quais ID's informar acesse o cadastro de situações da proposta. **Atenção:** Os valores informados devem ser do tipo inteiro positivo |
| **Situação da Proposta ao Expirar ou Derrubar Reserva** **ATENÇÃO:** Para que uma proposta caia automaticamente e a unidade volte para a situação disponível, ou reservada (caso tenha uma reserva na fila), a situação da unidade na qual a proposta se encontra necessita ter marcado o parâmetro PERMITIR PROPOSTAS, caso contrário a proposta irá para a situação de cancelada mas a unidade continuará na mesma situação. |
| **Acompanhamento Proposta - Assunto do e-mail acompanhamento da proposta** Tags disponíveis:  *${nome\_empresa}, ${numero\_proposta}, ${situacao\_proposta}*  *${nome\_empresa} - Proposta #${numero\_proposta} - ${situacao\_proposta}*  As tags então serão substituídas antes de enviar o email:  Exemplo: **TOTVS - Proposta #233 - Em Análise** |
| **Acompanhamento Proposta - Mensagem do e-mail acompanhamento da proposta** Tags disponíveis:  *${nome\_empresa}, ${numero\_proposta}, ${situacao\_proposta}, ${nome\_corretor} ${email\_corretor}, ${celular\_corretor}, ${link\_acompanhamento} e ${nome\_cliente}*  **Importante:** O e-mail é confeccionado em html, você pode usar tags html para formatar sua mensagem conforme desejar. |
| **Alterar todas as propostas para esta situação caso a unidade seja vendida** Se uma proposta é transformada em venda, todas as outras propostas (com exceção da proposta que gerou a venda) terão a situação alterada para outra. |
| **Comissão (adicional): Marcado como existente por padrão** No momento da simulação da proposta, deseja a comissão adicional esteja sempre marcada? |
| **Comissão (adicional): Paga pelo Cliente ou Empresa** Escolha quem paga a comissão adicional no momento da proposta. |
| **Comissão (adicional): Paga por RPA/NF** No momento da simulação da proposta, é perguntado ao corretor se a comissão adicional é por RPA ou NF. Este parâmetro define qual comissão deverá ser marcada como padrão. |
| **Comissão: Gerente recebe sempre pela empresa** O gerente sempre recebe pela empresa. |
| **Comissão: Gravar comissão no backoffice quando cliente faz pagamento da comissão** Defina se no momento do envio da venda é gravado a comissão no backoffice quando o cliente tem a responsabilidade de efetivar o pagamento da comissão. Nota: Para backoffice RM, está funcionalidade está disponível para versão maior igual a 12.1.17.176 |
| **Comissão: Gravar valor da comissão no backoffice** No momento que o Portal de Imóveis gravar a venda no backoffice, deseja que seja gravado a comissão? Nota: Para backoffice RM, está funcionalidade está disponível para versão maior igual a 12.1.17.176, então marque SIM se e somente se a versão do seu backoffice RM for maior igual 12.1.17.176 |
| **Comissão: Mostrar Painel na Proposta** Mostrar o painel de comissão e permitir o usuário a alterar se desejado. **Caso o painel não seja mostrado, é necessário selecionar quem paga a comissão abaixo**. |
| **Comissão: Paga pelo Cliente ou Empresa** Escolha quem paga a comissão no momento da proposta. |
| **Comissão: Paga por RPA/NF** No momento da simulação da proposta, é perguntado ao corretor se a comissão é por RPA ou NF. Este parâmetro define qual comissão deverá ser marcada como padrão. |
| **Criar plano de financiamento no backoffice** Define se ao enviar venda para o backoffice será criado plano de financiamento |
| **Data de corte para visualização de propostas no menu de comissão e corretores** Informe uma data de corte de exibição/listagem de propostas nos menus / submenus de comissão e corretores. **Atenção: Informe a data no padrão americano. Exemplo 2000-01-01 (ano-mes-dia).** |
| **Dia de vencimento das parcelas por padrão** Deixe em branco para usar a data do dia. **Nota:**No lançamento da proposta, caso o dia definido aqui seja menor que o dia atual, o dia atual será usado como dia de vencimento. Componentes configurados pra usar a data de entrega, não são afetados por este parâmetro, sendo assim, será sempre usado a data de entrega. |
| **Dias para o combo da modalidade** Separe cada dia por vírgula, ex: 1,5,10,15 |
| **Grava comissão diretamente** Ao salvar a proposta, gravar a comissão automaticamente baseado na porcentagem de comissão do corretor da proposta. |
| **Gravar mensagem ao mudar situação da proposta** Quando for modificado a situação de uma proposta será gravado uma breve mensagem com descrição da situação a proposta estava definida e a nova situação atribuída. |
| **Identificação do vendedor enviado para backoffice no instante do envio da venda** Selecione um valor para identificação de qual o vendedor que será gravado no backoffice no momento de fazer o envio da venda  Quando temos distribuições de comissão numa proposta teremos o seguinte comportamento:   * Caso a comissão possua distribuição para o Diretor de acordo com os parâmetros do Empreendimento e este Diretor possua CPF / CNPJ cadastrado no RM, ao enviar a venda o Diretor será enviado como Vendedor, independente do parâmetro. * Caso a comissão possua distribuição para o Gerente de acordo com os parâmetros do Empreendimento e este Gerente possua CPF / CNPJ cadastrado no RM, ao enviar a venda o Gerente será enviado como Vendedor, independente do parâmetro. * Caso o Corretor não tenha CPF / CNPJ cadastrado no RM, não será enviado o Vendedor para o RM.   Caso o parâmetro "**Identificação do vendedor enviado..."**seja:   * **Imobiliária:** Somente será levado como Vendedor caso o Corretor possua em seu cadastro uma Imobiliária. A Imobiliária deve possuir CPF / CNPJ cadastrado no banco RM. * **Corretor / imobiliária:** Caso o Corretor possua em seu cadastro uma Imobiliária, serão enviados como vendedores tanto o Corretor quanto a Imobiliária. Para que sejam enviados ao RM, eles devem possuir CPF / CNPJ cadastrado no banco RM. |
| **Local para mostrar na proposta** Digite aqui o local que deverá ser mostrado no rodapé da impressão da proposta. Para que esta localidade seja mostrada, escolha "Parâmetro" na configuração abaixo. |
| **Local para mostrar na proposta (qual mostrar)** Escolha qual localidade mostrar na impressão da proposta ou desativar a impressão do local. Caso escolha a opção "Parâmetro", digite acima qual localidade usar. |
| **Mensagem exibida quando às condições de pagamento da proposta for aprovada** Essa mensagem será apresentada quando às condições de pagamento for aprovada. |
| **Mensagem exibida quando às condições de pagamento da proposta for reprovada** Essa mensagem será apresentada quando às condições de pagamento for reprovada. |
| **Motivo do interesse ao derrubar proposta automaticamente** Selecione motivo para ser atribuído automaticamente quando uma proposta for derrubada e houver interesse(s) cadastrado(s) para o empreendimento e pessoa da proposta |
| **Nome do documento de impressão de proposta** Define o nome que será impresso no cabeçalho do documento de impressão da proposta |
| **O valor da proposta pode ser menor que o valor à vista** Permitir que o valor da proposta seja menor que o valor à vista. |
| **Ordenar as condições de pagamento por data na impressão do contrato/proposta** Escolha ***Sim*** para ordenar as condições de pagamento por data. Escolha ***Não*** para ordenar as condições de pagamento pela ordem que elas foram definidas no momento da simulação da proposta. |
| **Permite mais de uma proposta para o mesmo usuário** Alterando para **Não** fará com que seja feita uma verificação onde o usuário da proposta não possa ter uma proposta para a mesma unidade e esta esteja com situação diferente de cancelada. |
| **Permitir edição de proposta com data do mês anterior** Permitir editar as propostas que foram feitas com data do mês anterior ou posterior. |
| **Permitir editar propostas com a tabela de preços expirada** |
| **Permitir efetivar propostas sem comissão** Este parâmetro define se o sistema irá permitir que uma proposta vire contrato apenas se a comissão tiver sido lançada. |
| **Permitir propostas mesmo que o usuário tenha atingido o limite de reservas** Caso o usuário tenha atingido o limite de reservas, essa opção irá controlar se ele pode salvar uma proposta mesmo após o limite de reservas dele. |
| **Permitir prospect acompanhar proposta** Permitir envio de e-mail ao cliente com link para acompanhamento da proposta e envio de documentos |
| **Permitir que o valor da proposta seja maior que valor da tabela de preços** Caso este parâmetro esteja marcado como Sim e o valor da proposta seja maior que o valor da tabela de preços, a proposta será reprovada, mas poderá ser salva.  Importante: Este parâmetro não será aplicado quando a modalidade possuir cálculo do tipo price. |
| **Permitir que sejam pagas parcelas após a data de entrega** Permitir que as datas dos componentes ultrapassem a data de entrega. |
| **Permitir salvar proposta se não for o corretor da reserva ativa** |
| **Permitir venda se não houver cliente cadastrado no backoffice** Sim irá criar ou atualizar o cliente no backoffice. Não, o cliente deverá existir no backoffice antes que a venda possa ser enviada. |
| **Qual a data da proposta, data efetiva de cadastro ou data de algum componente** No momento da impressão da proposta, a data que deverá ser mostrada como data da proposta é a data configurada aqui. |
| **Qual a data da venda, data efetiva de cadastro, do dia ou data de impressão do contrato** No momento da impressão do contrato ou envio desta para o backoffice, a data que deverá ser mostrada como data da venda é a data configurada aqui. |
| **Qual valor do item da venda quando enviado para o backoffice** Este parâmetro define se o sistema deverá enviar o valor da proposta menos o valor de comissão ou o valor da unidade. |
| **Quando a comissão for NF, imprimir na proposta** Caso a comissão e/ou a comissão adicional sejam por NF, este parâmetro controla se estas devem aparecer na impressão da proposta ou não. |
| **Situação da Proposta com Venda Distratada** Quando uma venda é distratada no Backoffice, a proposta que teve a venda distratada será alterada para a situação selecionada aqui. Importante: Quando existe mais de uma proposta para a mesma subunidade, por exemplo, em casos onde determinada situação não consta como proposta ativa, o sistema irá emitir uma mensagem que informará ao usuário quais propostas impedem que a proposta seja avançada para o status definido neste parâmetro. Somente após a exclusão das propostas é que o Portal conseguirá realizar o avanço de etapa. |
| **Taxa Mínima de Atratividade (TMA)** TMA (taxa mínima de atratividade ou taxa de oportunidade) Global. **Nota:** A nova taxa afetará apenas as propostas futuras ou editadas.  **Importante: Quando a modalidade possui cálculo price, não deverá ser utilizado o TMA Global, visto que os dois cálculos (PRICE e TMA) não podem ser usados ao mesmo tempo.** **Recomendamos que, caso necessite utilizar TMA, defina o mesmo no empreendimento e utilize uma modalidade que não possua cálculo price.** |
| **Título para a linha de assinatura 1 da proposta/plano de pagamento.** No rodapé da proposta/plano de pagamento, é possível definir com este parâmetro qual o título dos dois campos pra assinatura. |
| **Título para a linha de assinatura 2 da proposta/plano de pagamento.** No rodapé da proposta/plano de pagamento, é possível definir com este parâmetro qual o título dos dois campos pra assinatura. |
| **Título para a linha de assinatura 3 da proposta/plano de pagamento.** No rodapé da proposta/plano de pagamento, é possível definir com este parâmetro qual o título dos dois campos pra assinatura. |
| **Usar valor da parcela price nos relatórios** **Sim:** Usa o valor da parcela nos relatórios. **Não:** Usa o valor total da parcela sem cálculo do price. |
| **Validar o valor do VPL acumulado** Validar se o valor do VPL acumulado do cliente é superior ao valor do VPL acumulado da tabela. |
| **Validar o valor do VPL até a entrega** Validar ou não o valor do VPL até a data de entrega comparando com o valor da tabela de preço. |
| **Validar o VPL de modo linear** Escolha ***Sim***, para validar o VPL período à período comparando as condições de pagamento do cliente x tabela ou ***Não*** para validar o VPL acumulado. **Nota:** O parâmetro de percentual de aprovação de VPL não terá efeito quando a validação for linear. |
