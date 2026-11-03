---
content_hash: 674ce5f1765bc4a437018e76e1029bab1e3e1996b897ee8b5511ad7c9215a606
fetched_at: '2026-06-29T00:10:46.560060+00:00'
page_id: '554642564'
product: rm
source: tdn-rm
title: Acompanhante
type: documentation
url: https://tdn.totvs.com/display/LRM/Acompanhante
version: 8
---

1. **Visão Geral**
2. **Exemplo de Utilização**

SumárioVisão Geral

## **01. VISÃO GERAL**

Essa funcionalidade serve para vincular o acompanhante ao paciente internado, e nele definir se o acompanhante irá ficar no mesmo leito ou em um leito diferente, onde será cobrado, no caso de diferente, o valor da diária que pode ser entre o acompanhante ou o hospital.   
  
Caso o acompanhante for utilizar o leito diferente do paciente e for responsável pela diária o leito deverá estar configurado para ser lançado na elaboração de contas do paciente como particular.

Exemplo de Utilização.

## **02. EXEMPLO DE UTILIZAÇÃO**

 - A tela de acompanhante só poderá ser exibida caso no atendimento interno o paciente ocupe leito.

* O campo "Nome" pode ser de digitação livre ou ser buscado através de um responsável financeiro do paciente/atendimento em questão (para esse caso serão utilizada as informações dos campos NOMEACOMP, IDENTIDADE, ORGAOEMISSOR e UFIDENTIDADE originados do cadastro de responsável)

* Caso o campo não seja preenchido e o usuário clique no botão para procurar o responsável, o nome do responsável encontrado será exibido. e  os campos de  Identidade, órgão emissor e UF, estes campos serão preenchidos.
* Após clicar para buscar o  responsável financeiro, caso o campo "Nome" não for alterado não seja preenchido  é porque não existe responsável financeiro com os dados pesquisados.
* Caso a  "Acomodação" escolhida seja "Em acomodação diferente do paciente" o botão de escolher o leito será habilitado e o leito deverá ser selecionado através do painel de leitos.
* Após a inserção, a única alteração possível no registro de acompanhante é a data fim

**Validações gerais:**

* O Botão de inserir dados não será exibido:

           - Caso a Data final do atendimento estiver preenchida, o botão de inserir ficará  inabilitado.

           - Caso o Status da Conta do atendimento estiver cancelado

* Caso o botão de selecionar responsável financeiro seja clicado:  
  - O campos: Nome, Identidade, Órgão Emissor e UF serão preenchidos com os dados do responsável financeiro.  
  - Caso o responsável não tenha os dados de Nome, identidade, Órgão Emissor e  UF preenchidos, os campos ficarão editáveis.

**- Serão exibidas mensagens que impedem inserir/alterar/excluir o registro de acompanhante caso um dos itens abaixo seja  encontrado:**

            - Ao tentar Salvar acompanhante em “Acomodação diferente do paciente” e não escolher o leito.

           - Data inicial seja inferior a data de entrada do paciente.

           - Data inicial maior que a data atual.

           - Data final seja menor que a data inicial.

           - Atendimento Cancelado.

           - Atendimento Faturado.

           - Atendimento Liberado.

          - Paciente recebeu alta(data final do atendimento estiver preenchida)

**-Verificar se a diária do paciente foi lançada corretamente:**

* Acessar o RMSaude (MDI Antiga), clicar em 'Tesouraria >> Lançamentos na conta do paciente >> Pesquisar Atendimento' Pesquisar o paciente em questão e selecionar o atendimento também em questão.
* Clicar em 'Diárias' e observar se existe duas diárias lançadas, se a opção "Acomodação diferente do paciente" estiver marcado.
