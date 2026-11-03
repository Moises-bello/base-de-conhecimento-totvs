---
content_hash: f4325e20c2cf42caf844eab94c8770ae35a18b726d14450a2f849e16ffde1c7b
fetched_at: '2026-06-29T00:11:43.085252+00:00'
page_id: '801997247'
product: rm
source: tdn-rm
title: Totvs Incorporação - Parâmetros - Portal de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=801997247
version: 25
---

### **Proposta Venda 1/3**

---

Para saber mais sobre a parametrização das opções desta etapa acesse a documentação abaixo:

* **[Alçada de Aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=759938600)**

### **Proposta de Venda 2/3**

---

* **Proposta:** Parametrize as mensagens exibidas quando as condições de pagamento da proposta for:
  + **Aprovado;**
  + **Reprovado.**
* **Usuário default para criar o usuário de acesso do Cli/For copiando as permissões para o corretor AUTOMATICAMENTE no PI (somente para a nova tela de usuário):** Para facilitar e padronizar o acesso dos Corretores ao PI, crie um perfil no TCGI com todas as permissões de acesso básicas que o corretor deve ter, associe um usuário padrão a este perfil e utilize-o como base para atribuir estas permissões de acesso aos demais corretores, quando for utilizar a ferramenta [Utilitários - Portal - Manutenção de Usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=435105178). Para isto informe:  
  + **Usuário de Origem:** informe o código do usuário que tem o perfil básico de corretor;
  + **Código de Acesso:** Informe o código de acesso ao sistema que será atribuído a estes corretores.

* **Envio da Proposta Aprovada para o TCGI:** No *Portal de Imóveis*, ao executar o processo para *Enviar Venda para o BackOffice*, é possível de se definir as opções abaixo:
  + **Gerar Plano de Financiamento:** Marque esta opção para definir se o *Plano de Financiamento* da venda será gerado automaticamente ou se o usuário do TCGI deverá gerá-lo manualmente. Esta opção é muito útil, caso seja necessária a conferência das *Condições de Financiamento* da venda gerada no PI. Reforçando que todas as Propostas neste portal sempre passam pela validação da *VPL* para serem aprovadas.
  + **Efetivar o Contrato de Venda:** Marque esta opção para definir se a venda, quando oriunda do PI, será *Efetivada* automaticamente ou se a mesma permanecerá *Em Preparação*, para realização de qualquer conferência e posteriormente efetivada manualmente.

    Importante!
    - **Configuração da Data da Venda / Proposta**

      Sempre que optar por definir a **“Data da Venda” como “Proposta”**, é importante seguir as orientações abaixo para garantir que as demais datas do contrato fiquem corretamente alinhadas no sistema.

      Ao realizar o envio da venda para o backoffice, o campo **“Data da Proposta/Venda”** será exibido na tela de confirmação. A data informada nesse momento passará a ser considerada como a nova **data oficial da venda**.

      Caso deseje que outras datas contratuais acompanhem essa mesma referência, configure também os campos **“Data da Assinatura”** e **“Data Base da Venda”** como **“Proposta”**. Dessa forma, todas as datas relacionadas serão ajustadas automaticamente, garantindo maior consistência e alinhamento das informações no contrato.

      Quando o parâmetro **“Data da Venda”** estiver configurado corretamente, ele será o responsável por alinhar automaticamente as seguintes informações:

      * Data de início de vencimento da regra que compõe a parcela que não seja o principal (Juros Contratual e/ou Correção Monetária)
      * Data de entrada do comprador na proposta
      * Data de emissão das parcelas no financeiro

      Essa configuração garante maior padronização e evita divergências no cronograma financeiro do contrato.

      ---

      **⚠️ Atenção Importante**

      Os **cálculos de valores não serão refeitos automaticamente pelo sistema** após a alteração da data da venda.

      Se o contrato possuir cálculos que utilizam a data de entrada como base (por exemplo, correções, encargos ou prazos financeiros), poderá haver diferenças entre os valores originalmente apresentados e a nova linha do tempo do contrato.

      Isso ocorre porque a alteração da data é realizada **ao final do processo de venda**, momento em que a proposta normalmente já foi analisada, aprovada pelas partes e, em muitos casos, assinada. Para preservar a integridade das condições previamente acordadas, o sistema não executa recálculos automáticos.

      **Recomendação:**  
      Antes de confirmar a alteração, verifique se será necessário revisar manualmente os valores ou condições financeiras para garantir que permaneçam corretos.Imagem Envio - Possibilidade de alterar data venda
  + **Data da Venda:** Utilize as opções abaixo para definir qual data será utilizada como [*Data da Venda*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105242):
    - **Proposta:** A data da venda será a mesma data em que a Proposta foi cadastrada no PI. Esta é a data padrão utilizada pelo sistema; Ao realizar a etapa de *Atualizar a venda no Backoffice*, há a possibilidade de alterar a data da proposta neste momento.
    - **Hoje:** A data da venda será a data da execução do processo *Enviar Venda para o BackOffice*; ou
    - **Impressão do Contrato:** A data da venda será a data de impressão do contrato gravado da tabela da proposta do PI. Caso a proposta da venda não sido impressa para o cliente, o sistema utilizará a Data da Proposta. O sistema não considera a data do *envio da proposta por e-mail*.
  + **Data da Assinatura:** Utilize as opções abaixo para definir qual data será utilizada como [*Data da Assinatura*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105242) da venda:
    - **Proposta:** A data da assinatura da venda será a mesma data em que a Proposta foi cadastrada no PI. Esta é a data padrão utilizada pelo sistema;
    - **Hoje:** A data da assinatura será a data da execução do processo *Enviar Venda para o BackOffice*; ou
    - **Impressão do Contrato:** A data da assinatura será a data de impressão do contrato gravado da tabela da proposta do PI. Caso a proposta da venda não tenha sido impressa para o cliente, o sistema utilizará a Data da Proposta. O sistema não considera a data do *envio da proposta por e-mail*.
    - **Em Branco:** Utilize esta opção caso não queira que a data da assinatura seja preenchida na venda enviada pelo PI;
    - **1o. Dia Próximo Mês:** Utilize esta opção para que a data da assinatura seja o primeiro dia do próximo mês em relação à data de cadastro da proposta no portal.
  + **Data Base da Venda:** Utilize as opções abaixo para definir qual data será utilizada como [*Data Base da Venda*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105242):
    - **Proposta:** A data base da venda será a mesma data em que a Proposta foi cadastrada no PI. Esta é a data padrão utilizada pelo sistema;
    - **Hoje:** A data base será a data da execução do processo *Enviar Venda para o BackOffice*; ou
    - **Impressão do Contrato:** A data base será a data de impressão do contrato gravado da tabela da proposta do PI. Caso a proposta da venda não tenha sido impressa para o cliente, o sistema utilizará a Data da Proposta. O sistema não considera a data do *envio da proposta por e-mail*.
    - **Em Branco:** Utilize esta opção caso não queira que a data base da venda seja preenchida na venda enviada pelo PI;
    - **1o. Dia Próximo Mês:** Utilize esta opção para que a data base seja o primeiro dia do próximo mês em relação à data de cadastro da proposta no portal.
  + **Tipo da Situação da Proposta com Venda Distratada**
    - Define a situação da proposta no PI caso a venda no **RM** seja distratada

Importante!

As ações acima só serão refletidas na venda do TCGI, no momento em que o processo ***Enviar Venda para o BackOffice*** for executado Portal de Imóveis. Antes desta ação, nenhuma das parametrizações acima serão aplicadas.

* **Comissão - TCGI**
  + **Alinhar data inicial parcela comissão paga na mesa:** Ao marcar o parâmetro o sistema passa utilizar a menor data do primeiro componente gerador de parcela do plano de financiamento da proposta que esteja marcado como "desconta comissão"

### **Proposta de Venda 3/3**

---

* **Validar o valor do VPL acumulado:** Validar o valor final, acumulado, da VPL onde o valor da tabela é maior que o valor do cliente;
* **Validar o valor do VPL até a entrega:** Validar o valor final, acumulado até a entrega, da VPL onde o valor da tabela é maior que o valor do cliente;
* **Validar o VPL de modo linear:** Validar o valor, mês a mês, da VPL onde o valor da tabela é maior que o valor do cliente;
* **Permitir que o valor da proposta seja menor que valor da tabela de preços****:** Permite o valor do plano do cliente seja menor que a tabela.
* **Permitir que o valor da proposta seja maior que valor da tabela de preços****:** Permite o valor do plano do cliente seja Maior que a tabela.
* **Permitir que sejam pagas parcelas após a data de entrega:** Permite que tenha parcelas depois da entrega.
* **Usar Alçada de Aprovação como Desconto ao Invés de VPL:** Permite que a alçada seja validada como desconto ao invés de validar como VPL. Sendo assim, a prioridade no desconto ficaria assim,  Desconto na Alçada e depois por Modalidade.
* **Meios de Pagamento:** Define quais formas de pagamento estarão disponíveis para a geração do [*adiantamento de sinal*](https://tdn.totvs.com/pages/viewpage.action?pageId=865405461) no Portal de Imóveis. As opções são:

  + **Boleto Híbrido:** Gera um *[Boleto Híbrido](https://tdn.totvs.com/pages/releaseview.action?pageId=908344227#0-1)* que oferece ao cliente flexibilidade na escolha da forma de pagamento. Ao selecionar esta opção, as opções de PIX e Boleto Online são automaticamente desabilitadas; **ou**
  + **PIX:** Gera uma cobrança via *[PIX](https://tdn.totvs.com/pages/viewpage.action?pageId=727916895)* para o cliente. Ao selecionar esta opção, também é possível ativar a opção Boleto Online. No entanto, a opção Boleto Híbrido será desabilitada devido à regra de exclusão entre as modalidades; **e**
  + **Boleto Online:** Gera um boleto bancário tradicional para o adiantamento de sinal. Pode ser combinada com a opção PIX, mas é incompatível com o Boleto Híbrido, que será desabilitado automaticamente.

### **Parâmetros**

---

Quando a base é unificada, estes parâmetros de conexão serão adicionados / atualizados quando realizada a primeira instalação do portal de imóveis. É de suma importância verificar a conectividade da URL do webservice, visto que o Portal de Imóveis depende desta para seu correto funcionamento.

* **Webservice**
  + **URL**: URL de acesso aos webservices TOTVS
  + **Usuário**: Usuário de acesso aos webservices. Normalmente é um usuário administrador, com permissões totais de acesso.
  + **Senha**: Senha do usuário.
* **API Rest**
  + **URL**: URL da API Rest do sistema.

### **Notificações Whatsapp**

---

Com a parceria Worknow, essa parametrização permite definir os templates para notificações de corretores. Após a sincronia, associe os perfis correspondentes às seguintes etapas:

* Atribuição de Leads;
* Roleta de Leads;
* Reserva de Unidade

Para saber mais sobre essa integração acesse:   
Para saber mais sobre a worknow, acesse: <https://worknow.com.br/wikihelp/>

### **Integração OQDigital**

---

Com a parceria OQDigital, essa parametrização permite integrar o sistema para o recebimento de novos Leads. Após a ativação e configuração, o sistema gerará uma URL exclusiva responsável por:

* Autenticação segura com a plataforma parceira;
* Recebimento de novos *leads* em tempo real;

Para saber mais sobre a OQDigital, acesse: <https://oqdigital.com/oq-detalhes/>
