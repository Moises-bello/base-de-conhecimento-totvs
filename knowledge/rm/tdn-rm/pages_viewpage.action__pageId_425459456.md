---
content_hash: d2ff7c7e1792809e8d8536825a09f0dda927afb96268a7507093d3d9a363c83e
fetched_at: '2026-06-29T00:09:36.008272+00:00'
page_id: '425459456'
product: rm
source: tdn-rm
title: Regras - Regeração de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459456
version: 7
---

---

Para que a regeração de lançamentos realizada diretamente no TOTVS Educacional seja possível, o parâmetro do *sistema* **Permite regerar lançamentos** deve estar marcado e se o lançamento estiver com status 'Cancelado' o parâmetro **Regerar Lançamentos Cancelados**, também deve estar marcado.

Ambos parâmetros estão disponíveis no menu **Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional,** o parâmetro **Permite regerar lançamentos** também está disponível no processo de

**− Regerar Lançamentos Cancelados:**

Na regeração do lançamento cancelado os valores conta/caixa, data de emissão, data de vencimento, data de previsão de baixa, centro de custo, valor do desconto, juros, multa, opcionais, convênio, tabelas opcionais, campos alfas, datas opcionais **serão preenchidos com os valores padrões definidos nos parâmetros do sistema**. Vale ressaltar que tais configurações dos parâmetros podem ser realizadas no TOTVS Educacional ou no TOTVS Backoffice - Gestão Financeira (Linha RM).

**− Regeração de Lançamentos que possuem boletos Remetidos ou Registrados:**  
Se os lançamentos regerados tiverem mudança em seus *valores* o sistema irá verificar o status de remessa dos seus boletos e, se já tiverem sido remetidos aos bancos estas remessas precisam ser canceladas:

**- Cancelamento automático da remessa**  
Parâmetro , disponível no menu *Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 1/4.*

Com este parâmetro *marcado* ao regerar um lançamento pelo TOTVS Educacional em que o valor deste lançamento seja alterado e que o status do seu boleto seja igual a 'Remetido' ou 'Registrado' o sistema automaticamente executará o cancelamento desta remessa, modificando o status de remessa deste boleto para *'Pendente Remessa'* e prosseguirá com a regeração do lançamento.

Quando este cenário ocorrer, o processo que realizou a alteração do lançamento finalizará com o status de atenção (warning) e será apresentado no LOG os boletos que tiveram a remessa cancelada. Ressaltamos que, posteriormente, no módulo *TOTVS Gestão Financeira*, será necessário enviar para o banco uma nova remessa destes boletos.

Alguns bancos, porém, não aceitam remessa para *alteração* de valores do boleto. Neste caso, quando houver alterações de valores em lançamento cujo boleto já tenha sido remetido ou registrado no banco, será necessário *cancelar* o boleto original e consequentemente sua remessa, incluir um novo boleto contemplando o novo valor e, posteriormente, remeter este novo boleto ao banco:

**- Inclusão de novo boleto na regeração de lançamento**

No cadastro de *Convênio* do sistema financeiro existe a opção ***'Cancelar boletos pendentes de remessa ao alterar valores dos lançamentos'***. Esta opção *marcada* possibilita a execução automática do cancelamento do boleto que teve sua remessa cancelada e imediata inclusão de um novo boleto, com os valores atualizados.

**Atenção:**  
Aliando o parâmetro do sistema que cancela automaticamente a remessa à esta opção do cadastro de Convênio, havendo mudança de valores na regeração de lançamentos, o boleto original terá o seu status alterado para 'Pendente Remessa' e será *cancelado* automaticamente e imediatamente após será *incluído* um novo boleto contemplando as alterações.

Ressaltamos que, posteriormente, no módulo *TOTVS Gestão Financeira*, será necessário enviar para o banco uma remessa de *cancelamento* do boleto original e também uma *nova* remessa de envio para o novo boleto.

**− Processos executados no TOTVS Educacional que automaticamente realizam a regeração de lançamentos:**

****-**Processo de Inclusão/Exclusão de Bolsa Retroativa**Ao realizar a inclusão ou exclusão de uma bolsa retroativa o sistema altera o lançamento financeiro no qual a bolsa está sendo incluída ou excluída, e para os casos em que o status do boleto deste lançamento seja igual a 'Remetido' ou 'Registrado', serão aplicadas as mesmas regras da regeração de lançamento descritas nos tópicos acima.

Ao término do processo o sistema apresentará no LOG informações com os lançamentos/boletos que tiveram a sua remessa cancelada automaticamente.

**− Atualização das informações bancários:**

*****-****Geração* de lançamentos: na geração (*inclusão*) de lançamentos, as informações bancárias utilizadas para os lançamentos serão aquelas informadas na Conta Caixa definida nos parâmetros do sistema (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional*), ou conforme parametrização da base, na Conta Caixa definida no cadastro do próprio .

-*Regeração* de lançamentos '*em aberto'*: Na regeração de lançamentos em aberto, o sistema *não* fará a atualização das informações bancárias, ou seja, o sistema não fará novamente a leitura da Conta Caixa parametrizada no sistema, mantendo a mesma Conta Caixa utilizada no lançamento que está sendo regerado. Isto é necessário, pois após a geração (inclusão) do lançamento as informações bancárias do lançamento podem ter sido alteradas, e assim, na regeração de lançamentos em aberto, o sistema manterá a mesma Conta Caixa já utilizada no lançamento.  
**Observação:**Após o lançamento ter sido gerado, se necessitar alterar as informações bancárias do lançamento e boleto, acesse diretamente no *TOTVS Gestão Financeira*, dentro do Anexo de Boleto, o processo *Manutenção de Boletos | Alterar Conta Caixa e Convênio*.

- *Regeração* de lançamento '*cancelados'*: Na regeração de lançamentos *cancelados* o sistema incluirá um novo lançamento, então as informações bancárias serão aquelas informadas na Conta Caixa definida nos parâmetros do sistema (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional*), ou conforme parametrização da base, na Conta Caixa definida no cadastro do próprio *serviço*.

A *Forma de Pagamento*, indicada como Default dos Dados Bancários no cadastro do cliente, será atualizada nos lançamentos regerados seguindo a mesma lógica para atualização dos dados da Conta Caixa citados acima.

**Importante:**

**− Lançamentos agrupados:**

Na regeração de lançamentos, realizada diretamente no TOTVS Educacional, como regra do sistema, se os lançamentos não tiverem boletos ou os seus boletos estiverem todos cancelados, o sistema incluirá automaticamente novos boletos para os lançamentos que estiverem sendo regerados, porém, na regeração de lançamentos as regras de *agrupamento* de lançamentos *não* serão aplicadas em lançamentos já agrupados, sendo, neste caso, incluído um boleto para cada lançamento gerado. Se desejar que as regras de agrupamento de lançamentos sejam aplicadas, os lançamentos envolvidos deverão ser *cancelados e incluídos novamente*.

**− Valores Opcionais/Valores de Integração:**  
Os valores de Bolsa Condicional, Bolsa Incondicional, Pagamento a Maior, Pagamento a Menor e os valores aproveitados da Conta Corrente dos alunos são controlados nos lançamentos financeiros em campos específicos, denominados *Valores Opcionais* ou *Valores de Integração*, que são parametrizados no sistema (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional*). Eventualmente estes valores podem possuir tanto uma parametrização de Valor Opcional quanto de Valor de Integração, uma vez que inicialmente só era possível utilizar Valores Opcionais sendo liberada a utilização dos Valores de Integração posteriormente. Ao parametrizar um campo de Valor de Integração para assumir o controle dos valores acima, o sistema contudo, grava a data em que cada Valor de Integração foi parametrizado na base, e assim:

- Os lançamentos **gerados (incluídos)** após realização da parametrização dos Valores de Integração utilizarão esta parametrização para os novos lançamentos, validando sempre a data em que os campos de Valores de Integração foram parametrizados no sistema.  
**Exemplo**:  
• Criado o Valor de Integração como nome de *'Bolsa'* para registrar os valores de Bolsa Incondicional. Indicação deste campo *'Bolsa'* nos parâmetros do sistema educacional realizada em *01/12/2017*. Todos os lançamentos gerados (incluídos) a *partir desta data* utilizarão este campo de Valor de integração, denominado *'Bolsa'*, para registrar os valores de Bolsa Incondicional.

- Na **regeração** dos lançamentos serão considerados os mesmos campos utilizados quando o lançamento foi incluído, ou seja, campos de Valores Opcionais ou de Valores de Integração, mantendo os dados legados.  
**Exemplo**:  
• Lançamento 'X' gerado originalmente em **15/11/2017** utilizando o Valor Opcional com o nome de *'Bolsa Aluno'* para registrar o valor de Bolsa Incondicional.  
Criado o Valor de Integração como nome de 'Bolsa' para passar a registrar os valores de Bolsa Incondicional e indicação deste campo 'Bolsa' nos parâmetros do sistema educacional realizada em *01/12/2017*.   
Lançamento 'X' foi **regerado** em **10/12/2017**: neste caso, apesar da nova parametrização, o sistema continuará utilizando o Valor Opcional com o nome de *'Bolsa Aluno'* para controlar neste lançamento o valor de Bolsa Incondicional.

Bolsa de Crédito

Não é permitido regerar lançamentos quando existem lançamentos de bolsa de crédito e os lançamentos associados a parcela não estão todos cancelados.

**Lançamentos enviados para cobrança terceirizada:**

Lançamentos que foram classificados como enviados para cobrança terceirizada, pelo financeiro, não poderão ter seus valores alterados.

Documentação: <https://tdn.totvs.com/x/cfADIQ>

  Veja Também

---
