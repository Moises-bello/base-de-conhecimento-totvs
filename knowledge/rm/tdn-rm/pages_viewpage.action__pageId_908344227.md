---
content_hash: 78573346166e855f77038b4ccf97891c5b14ac69e0e1d2244a86fc284f2971cd
fetched_at: '2026-06-29T00:12:03.414371+00:00'
page_id: '908344227'
product: rm
source: tdn-rm
title: Boleto Híbrido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=908344227
version: 43
---

## O que é o Boleto Híbrido?

O boleto híbrido é uma solução de pagamento moderna e prática que combina o melhor de dois mundos: a confiabilidade do boleto registrado e a agilidade do Pix. Com ele, o cliente pode escolher como prefere pagar: utilizando o boleto bancário tradicional ou realizando o pagamento instantâneo via Pix, tudo em um único documento e processo integrado.

Essa flexibilidade oferece uma experiência simples e eficiente, garantindo que o cliente tenha controle sobre sua escolha de pagamento, sem abrir mão da segurança. O boleto registrado segue todas as normas bancárias e oferece a opção de pagamento em prazo mais longo, enquanto o Pix possibilita a confirmação instantânea, ideal para quem precisa de agilidade.

## Por que adotar o Boleto Híbrido?

Além de beneficiar o cliente, o boleto híbrido traz diversas vantagens para empresas. Uma delas é a integração direta com o banco, eliminando a necessidade de enviar ou processar arquivos de remessa e retorno. Todas as informações, como pagamentos realizados e atualizações, são automaticamente sincronizadas com o sistema por meio de processos agendados. Isso reduz erros, simplifica a gestão financeira e economiza tempo.

### Vantagens do Boleto Híbrido:

* **Flexibilidade**: O usuário pode optar entre pagar com boleto ou Pix, de acordo com sua preferência.
* **Segurança**: Tanto o boleto registrado quanto o Pix oferecem níveis elevados de proteção contra fraudes.
* **Agilidade**: O Pix permite a confirmação de pagamento imediata, enquanto o boleto oferece a opção de um prazo maior para quitação.
* **Praticidade**: Todas as opções de pagamento estão reunidas em uma única interface, facilitando a experiência do usuário.

### Contratação:

Esta solução deve ser contratada, para mais informações acessar a página: <https://totvstechfin.com.br/pagamentos/>

0Permissão

No cadastro do Perfil do usuário, é necessário conceder as permissões relacionadas ao Boleto Híbrido conforme a necessidade de cada operador. Na imagem a seguir demonstramos as permissões disponíveis:

1Parâmetros de Configuração do Boleto Híbrido

Para configurar o boleto híbrido, siga as etapas abaixo:

#### 1. Acessando os Parâmetros

No TOTVS Gestão Financeira, acesse o menu **Ambiente > Parâmetros > TOTVS Gestão Financeira > Contas a Receber > Boleto Híbrido**.

#### 2. Configuração dos Campos

* **Credenciais**: Insira as credenciais de acesso ao RAC.
* **Baixa**: Informe os meios de pagamento que serão utilizados para realizar a baixa do boleto híbrido.

> **Observação**:  
> A parametrização pode ser feita no nível **Coligada** ou **Filial**. Caso seja configurado para a **Filial**, essa configuração terá prioridade sobre a da Coligada.  
> Preencha todos os campos obrigatórios (*Credenciais* e *Baixa*) para garantir o correto funcionamento.

---

### [Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845)

#### 1. Ativar o Boleto Híbrido

* Acesse a aba **Boleto Híbrido** e habilite a opção **"Permite registro de boleto híbrido"**.
* Informe a **chave PIX** fornecida pelo banco.
  + Cada chave PIX pode estar vinculada a apenas um convênio.
* Informe o **Prazo de liquidação em dias úteis (Cod. barras)**.
  + Alguns bancos não retornam a data de liquidação/crédito quando o pagamento é realizado por código de barras. Para que a data de compensação no extrato de baixa seja calculada corretamente, é necessário definir o prazo de liquidação em dias úteis após o pagamento.
  + Para pagamentos realizados via QR Code Pix, a data de liquidação/crédito ocorre no mesmo dia quando efetuados em dias úteis. Caso o pagamento seja realizado em dias não úteis, a liquidação ocorrerá no próximo dia útil.
  + Sábado e Domigo são considerados dias não úteis
  + O calendário utilizado para definição de feriados é o configurado na filial. Quando não houver calendário definido na filial, será utilizado o calendário oficial configurado nos parâmetros do TOTVS Gestão Financeira.

#### 2. Configurar Dados Adicionais

* Vá até a aba **Dados Adicionais** e, no campo **"Valor código de barras"**, selecione a opção **Original**.

Atenção!

Em relação à configuração "valor código de barras" acima, para uso com o **TCGI** deve-se obrigatoriamente, marcar a opção de valor **líquido**, para que o boleto seja gerado com os valores de correção monetária e juros associados ao contrato de venda do cliente.

Já em relação à configuração "valor código de barras" acima, para uso com o **Educacional,** é necessário que seja marcada a opção de parcial, para que o boleto seja gerado considerando o valor do desconto incondicional. Para maiores informações de como definir o valor que será considerado na geração do código de barras do boleto, acesse a página: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041183453-RM-FIN-Como-definir-o-valor-que-ser%C3%A1-considerado-na-gera%C3%A7%C3%A3o-do-c%C3%B3digo-de-barras-do-Boleto>

Ao marcar esta opção, o sistema executará o reajuste online das parcelas associadas ao boleto, garantindo que não haja divergência entre esses valores no momento da baixa.

Caso seja mantido a parametrização com o valor original, o boleto será gerado apenas com o componente do componente principal da parcela, sem os valores de correção monetária, juros e demais componentes originados no TCGI.

#### 3. Configurações para Baixa

Permita que a baixa seja efetuada mesmo com valores calculados através das configurações descritas no passo 3.

3Funcionalidades Disponíveis

##### 1. **Transações**

A visão de transações exibe as transações existentes para os boletos híbridos. Para acessá-la:

* Navegue até **Contas a Pagar/Receber** e clique no menu **Boleto Híbrido**.
* Selecione a opção **Transações**.

Na visão de transações, você encontrará:

* **Anexos**:  Utilizar o menu **Anexos** para executar opções como:  
    
  + **Histórico de Transações**
  + **Boleto**
* **Processos**: Utilize o menu **Processos** para executar ações, como:  
    
  + **Ajuste de Transação**
  + **Cancelar Registro de Boleto Híbrido**

**Importante:**A visão de transações do boleto híbrido podem ser visualizadas em todas as coligadas visto que as transações são globais. Logo, é possível que uma transação tenha sido gerada através do processo de registro do boleto híbrido na coligada '1' mas o ajuste/cancelamento da transação pode ser executado na coligada '2'.

---

##### 2. **Registro Online do Boleto Híbrido**

Registre o boleto híbrido diretamente na instituição bancária. É necessário que o boleto já esteja cadastrado no sistema, podendo ser visualizado através do menu **Contas a Pagar/Receber | Boleto.** Selecione um boleto em aberto que ainda não esteja registrado. Em seguida, clique em **Processos > Boleto Híbrido > Registrar Boleto Híbrido**.

**Observações:**

* Os campos Nosso Número, Linha Digital, Código de Barras e QRCode Pix, são gerados pelo banco e atualizados automaticamente no boleto após a confirmação do registro.
* Os campos de valores (Desconto, Multa e Juros) e modalidade são recuperados do cadastro do convênio, caso não estejam preenchidos, são utilizados o do próprio boleto.
* Quando o registro é realizado, o sistema cria uma transação para o boleto híbrido, garantindo que todas as atualizações sejam refletidas corretamente.

**Status de Registro:**

* **Falha no Pagamento:** Ocorreu um problema no registro.
* **Pagamento Solicitado:** Registro executado com sucesso; o boleto foi atualizado.

> **Observação**:  
> Se o boleto estiver com o status "Remessa Registrado Boleto Híbrido", um novo registro não será permitido.  
> Para registrar novamente, primeiro é necessário cancelar o registro atual.

---

##### 3. **Atualização Online do Boleto Híbrido**

O status das transações de boletos híbridos é atualizado pelo processo **Ajuste de Transação.** Este processo visa realizar atualizações nas transações geradas através do registro do boleto híbrido com base nas informações fornecidas pela instituição bancária. As atualizações podem ser realizadas de três formas:

Cards2Ajuste individual de Transação

O sistema possibilita a atualização de uma ou mais transações. O requisito para que essa atualização ocorra é o status atual da transação, considerando apenas registros com os seguintes status: **Pagamento Confirmado.** Através da visão de transações do boleto híbrido, basta selecionar as transações desejadas, clicar em **Processos > Ajuste de Transação** e executar o processo.

3Atualizar Transação

Ao clicar na opção 'Atualizar Transação' será iniciado o processo:

Este processo possui as seguintes características:

* Possibilidade de fracionar a execução em vários jobs (caso o ambiente esteja [configurado em N camadas](https://tdn.totvs.com/pages/viewpage.action?pageId=236432384)) para obtenção de ganho de performance.

Além de utilizar esta arquitetura na instalação do sistema, é necessário acessar o menu 'Ambiente - Segurança de Jobs Fracionáveis' e inserir um novo registro com a classe "**FinBoletoHibridoAtualizacaoFracionadoProcess**", definindo o número mínimo e máximo de frações e ativando as opções 'Departamento Ativo' e 'Agendável'.

A Atualização de Transação possui dois tipos de atualização:

* **Diário**: Recomendado para ser executado com recorrência, onde o processo irá procurar todas as atualizações que ocorreram no dia corrente e no anterior.
* **Período**: Recomendado para ser executado caso algum período não tenha sido executado. Logo, o usuário poderá definir o período que deseja consistir. Ressaltamos que o tipo de atualização por período não permite recorrência, pois não faz sentido executar o processo recorrente para o mesmo período.

**Observações**:

1. Não será permitido efetuar mais de um processo com recorrência, pois como é um processo global só faz sentido ter apenas uma recorrência e assim preservar os recursos de jobs. Ao tentar criar outra recorrência, será apresentada uma mensagem mencionando os demais jobs já programados para serem executados com recorrência.
2. Também não será permitido ter recorrência do processo de "Ajuste de Transação" e "Atualizar Transação" ao mesmo tempo, para evitar concorrência entre os processos.

**Status possíveis após a atualização:**

* **Pagamento Confirmado:** O pagamento foi confirmado junto à instituição bancária, porém o boleto não foi baixado no ERP automaticamente (ocorreu um problema na contabilização da baixa do lançamento financeiro, por exemplo).
* **Pagamento Concluído:** O pagamento foi confirmado junto à instituição bancária e a baixa do boleto foi concluída com sucesso no ERP.
* **Pagamento Expirado:** O registro expirou junto à instituição bancária.
* **Pagamento Cancelado:** O registro foi cancelado pela instituição bancária.

---

##### 4. **Alterar Data de Vencimento**

A funcionalidade "Alterar Data de Vencimento", localizada no menu 'Processos - Manutenção de Boletos', visa definir uma nova data de vencimento para o boleto e os lançamentos vinculados a ele.

Existem algumas regras no sistema que não permite o usuário alterar a data de vencimento do boleto. São elas:

* Boletos com status diferente de "Em aberto" e "Parcialmente Baixado";
* Boletos baixado parcialmente e com código de barras gerado;
* Boletos com status de remessa diferente de "Registrado Boleto Híbrido".

**Observações**:

* Ao alterar a data de vencimento de um boleto registrado, o código de barras e o QRCode não são alterados.
* Opção disponibilizada a partir dos patch 12.1.2506.277, 12.1.2510.196 e 12.1.2602.118

---

##### 5. **Cancelamento de Registro**

O cancelamento de registro tenta desfazer transações com o status **Pagamento Solicitado** diretamente na instituição bancária. **Atenção:** As regras de cancelamento podem variar de acordo com a instituição.

Formas de realizar o cancelamento:

* **Na visão de boletos:**

  + Selecione o boleto desejado.
  + Acesse o menu **Processos > Boleto Híbrido > Cancelar Registro de Boleto Híbrido**.
* **Na visão de transações:**

  + Selecione a transação desejada.
  + Acesse o menu **Processos > Cancelar Registro de Boleto Híbrido**.
8Bancos Habilitados

Bancos habilitados: Itaú, Banco do Brasil, Santander, Sicoob, Bradesco, Caixa Econômica Federal e Sicredi. Cada banco possui suas próprias exigências e particularidades para parâmetros como Multa, Juros, Desconto e Protesto.

As regras descritas não são uma definição do nosso sistema, mas sim os padrões determinados pelas instituições financeiras. É fundamental seguir essas diretrizes para garantir o sucesso no registro de boletos híbridos.

Para facilitar a consulta, as informações estão organizadas por modalidade, destacando quais opções são suportadas por cada banco.

### **Regras para Multa**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Descrição** | **Itaú (341)** | **BB (001)** | **Santander (033)** | **Sicoob (756)** | **Bradesco (237)** | **Sicredi (748)** | **Caixa (104)** |
| Valor Fixo | Sim | Sim | Não | Sim | Sim | Não | Sim |
| Percentual | Sim | Sim | Sim | Sim | Sim | Sim | Sim |

---

### **Regras para Juros**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Descrição** | **Itaú (341)** | **BB (001)** | **Santander (033)** | **Sicoob (756)** | **Bradesco (237)** | **Sicredi (748)** | **Caixa (104)** |
| Valor por Dia Corrido | Sim | Sim | Não | Sim | Sim | Sim | Sim |
| Percentual por Dia Corrido | Sim | Sim | Não | Não | Sim | Sim | Não |
| Percentual por Mês Corrido | Sim | Sim | Sim | Sim | Não | Não | Sim |
| Percentual por Ano Corrido | Não | Não | Não | Não | Não | Não | Não |
| Valor por Dia Útil | Sim | Não | Não | Não | Não | Não | Não |
| Percentual por Dia Útil | Sim | Não | Não | Não | Não | Não | Não |

---

### **Regras para Desconto**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Descrição** | **Itaú (341)** | **BB (001)** | **Santander (033)** | **Sicoob (756)** | **Bradesco (237)** | **Sicredi (748)** | **Caixa (104)** |
| Valor Fixo até o Vencimento | Sim | Sim | Sim | Sim | Sim | Sim | Sim |
| Percentual até o Vencimento | Sim | Sim | Não | Sim | Sim | Sim | Sim |
| Valor por Dia Corrido Antecipado | Não | Não | Não | Não | Não | Não | Sim |
| Valor por Dia Útil Antecipado | Não | Não | Não | Não | Não | Não | Não |
| Percentual por Dia Corrido Antecipado | Não | Não | Não | Não | Não | Não | Sim |
| Percentual por Dia Útil Antecipado | Não | Não | Não | Não | Não | Não | Não |

---

### **Regras para Protesto**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Descrição** | **Itaú (341)** | **BB (001)** | **Santander (033)** | **Sicoob (756)** | **Bradesco (237)** | **Sicredi (748)** | **Caixa (104)** |
| Dias para Protesto | Não | Sim | Sim | Sim | Sim | Sim | Sim |

---

API de Registro de Boleto Híbrido

## Autenticação

Sim (Basic, Bearer Token)

## Estrutura da Url

| **POST** | http://{ambiente}/api/financial/v1/hybrid-bank-slip |
| --- | --- |

## Requisição

| Campo | Descrição |
| --- | --- |
| PaymentChannel | Deve ser enviado Fixo "Web" |
| companyId | Código da Coligada do boleto |
| BankSlipId | Id do Boleto. |

RDark

## Resposta

### 200 - Success

### 400 - Bad Request

Dúvidas Frequentes

 Veja também

---

[Boleto Híbrido - TOTVS Educacional](https://tdn.totvs.com/pages/viewpage.action?pageId=1074618418)
