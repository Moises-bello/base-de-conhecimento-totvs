---
content_hash: d0cf47a34fe741dc9b6ae45d166f1b67dc19cbcc23ca9ff5f42b326dfe3228af
fetched_at: '2026-06-29T00:09:49.704496+00:00'
page_id: '435105347'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Controle de Despesas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105347
version: 33
---

Ter um controle nas Despesas de uma empresa , para que serve ? O planejamento econômico-financeiro das operações de uma empresa, e de fiscalização da execução do programa preestabelecido. Nos tempos atuais não há lugar para empresas que não saibam planejar o progresso. Em face da viva e agressiva concorrência e das frequentes e violentas variações nas estruturas econômicas do mundo, qualquer organização que deseje progredir, ou, pelo menos, sobreviver, tem de planejar suas atividades e cuidar para que prossigam no sentido previsto pelo plano. Acima de tudo a empresa precisa se empenhar ao máximo para que os resultados de seus esforços sejam efetivos, o que se demonstra pela obtenção do lucro projetado. Com o Controle de Despesas do TCGI , é possível repassar despesas de uma forma prática e segura.Abaixo mais sobre o Controle de Despesas do TCGI.

Parcela de Despesas

Sobre processo de : Geração de Parcelas de Despesas.

Sobre Parcela de Despesa |

A parcela de Despesa é gerada quando a Despesa é salva pelo usuário. Os seus valores são preenchidos de acordo com a Despesa que a gerou. A partir da Parcela de Despesa que se pode gerar os Movimentos, para que seja realizado os pagamentos das despesas. Segue abaixo mais detalhes sobre a tela e seus campos:

**Figura 1 - Tela de edição da Parcela de Despesa**

**Campos:**

* **Origem:** Esse campo é preenchido conforme o campo origem da Despesa que gera a Parcela de Despesa. Esse campo possui as seguintes opções "Aluguel" ou "Venda";
* **Responsável:**Campo é preenchido de acordo com o Responsável pelo pagamento do ITPU conforme os Defaults informando no Empreendimento ou Subunidade.
* **Identificador:** Esse campo possui um valor numérico, onde o sistema auto incrementa o valor. Ele é único entre as parcelas de despesa, dessa forma pode servir com um identificador de parcela de despesa.
* **N° da Parcela:**  Esse campo exibe o valor numérico sequencial das parcelas, onde é ordenado de acordo com a data de vencimento.
* **Vencimento:** Esse campo exibe a Data de Vencimento da Parcela de Despesa. A data de vencimento é definida pela Despesa no qual foi gerada. Através dos campos "Primeiro Vencimento" , que será a Data de Vencimento da primeira parcela, e o "Intervalo em dias", no qual define o vencimento das demais parcelas, acrescentando o seu valor em relação ao Primeiro Vencimento.
* **Valor:** Esse campo exibe o valor da Parcela de Despesa. Esse valor é definido pela Despesa no qual foi gerada, através dos seguintes campos:

* + **Tipo valor de despesa:** Esse campo define qual o valor será utilizado no cálculo das parcelas de despesa. Possui 2 opções, "Valor à Vista" e "Valor à Prazo";
  + **Valor à prazo:** Nesse campo o usuário define qual será o valor à prazo daquela despesa. Ele será utilizado no cálculo das Parcelas de Despesa, somente se no campo "Tipo valor de despesa" estiver selecionado a opção "Valor à Prazo";
  + **Valor à vista:** Nesse campo o usuário define qual será o valor à vista daquela despesa. Ele será utilizado no cálculo das Parcelas de Despesa, somente se no campo "Tipo valor de despesa" estiver selecionado a opção "Valor à Vista";
  + **N° de Parcela(s):** Esse campo irá definir quantas Parcelas de Despesa serão geradas. Dessa forma o valor da Parcela de Despesa, será resultado do Valor definidos nos campos citados anteriormente dividido pela o número de parcelas informado;
  + **Código Fornecedor:** Esse campo exibe para qual Cliente/Fornecedor será realizado o pagamento da despesa;

* **Movimento:**

* + **Identificador:** Esse campo exibe o identificador do Movimento gerado pela Parcela de Despesa. Através desse campo é possível acessar o movimento criado.
  + **Situação:** Esse campo exibe a situação do Movimento gerado pela Parcela de Despesa.
  + **Tipo de Movimento:** Esse campo exibe o código do Tipo de Movimento utilizado para a geração do Movimento da Parcela de Despesa;
  + **Nome:** Esse campo exibe o nome do Tipo de Movimento utilizado para a geração do Movimento da Parcela de Despesa;

* **Data Criação:** Exibe a data de criação da Parcela de Despesa;
* **Usuário Criação:** Exibe qual o usuário que foi o responsável pela criação da parcela de despesa. Nesse caso será o mesmo usuário que salvou a despesa, que assim gerou a parcela de despesa;
* **Data Alteração:** Exibe a data de alteração da Parcela de Despesa;
* **Usuário Alteração:** Exibe qual o usuário que foi o responsável pela alteração da parcela de despesa.

Anexo de Documentos

Ao editar uma parcela da despesa através do menu Anexos>>Documentos da Parcela será possível realizar a inserção de um arquivo PDF.

**Alteração do valor e vencimento da Parcela de Despesa**

Foi disponibilizado a possibilidade de alterar os campos "Vencimento" e "Valor" quando a parcela de despesa ainda não foi integrada a um movimento.   
Importante.: Para Aluguel existe controle de segurança no perfil associado ao usuário, para saber clique no link .  
Para que o sistema permita essa alteração, é necessário permitir acesso ao perfil do usuário. Essa permissão se encontra no seguinte Caminho: Serviços Globais >> Segurança >> Perfis. Na visão de perfis, altere o Sistema para "Incorporação" e edite o perfil desejado. Na aba Acesso a Menus, permita o acesso para a opção "Alterar vencimento e valor da parcela de despesa".

Segue abaixo um print:

**Figura 2 - Permitindo que possa ser alterado o Valor e Vencimento das parcelas de despesas não integradas.**

**Figura 3 - Tela de Parcela de Despesa permitindo que o vencimento e valor sejam alterados**

**Figura 4 - Tela da Parcela de Despesa integrada, assim não permitindo a alteração do Vencimento e Valor.**

**Parcela de Despesa : Responsável ( CLIENTE ).**

Nas parcelas de despesas com responsabilidade do cliente, fica habilitado o Status Pagamento (se o cliente pagou ou não a despesa). [ Pendente ou Pago ].

Esse Status Pagamento só fica visível, quando a responsabilidade da parcela for do cliente, sendo a Empresa , este campo não é visualizado.

O campo é editável , o  default fica pendente e a informação não será preenchida automaticamente.

Alteração de Status em lote.

Alteração do status de pagamento em lote

Processo para alterar o status do pagamento para as despesas de responsabilidade do cliente com a finalidade de facilitar o controle das incorporadoras e imobiliárias sobre o que é pago diretamente pelos clientes.

Selecionar as Parcelas desejadas e em seguida : Processos | Alterar Status da Parcela

Ai seleciona o Status desejado que será vinculado nas parcelas.

**Visão da tela de Parcela de Despesa:**

Para facilitar a visualização das parcelas e de processos em lote a serem realizados, está disponível no menu Despesas para Venda e Aluguel uma visão geral das parcelas de despesa (venda e aluguel).

Além de mostrar a visão diretamente, foram acrescentadas as informações de código e descrição da despesa e do tipo de despesa.

**Figura 5 - Tela da Parcela de Despesa para Venda**

**Figura 6 - Tela da Parcela de Despesa para Aluguel**

Pagamento de Despesa para Cliente |Importante

Gerando pagamento de despesa.

Quando o responsável pela parcela for o cliente, ao executar o processo de Gerar pagamento de despesa (para gerar movimento ou lançamento a pagar) e gerar lançamento de reembolso, não serão gerados movimentos ou lançamentos financeiros. Isso porque, quando o responsável for o cliente, a parcela será utilizada apenas para o controle de pagamentos realizados pelos compradores ou locatários dos imóveis.

Ao regrar parcela de despesas do tipo reembolso, parcela de responsabilidade do cliente, mas quem paga primeiro é a empresa e é cobrado do cliente com parcela de reembolso. Agora é possível incluir essas parcelas no plano de financiamento da venda, para que possa ser exibido dentro do contrato, na ficha financeira, no Informe rendimento, módulo de cobrança e apuração de competência.

 Acesse o parâmetros gerais => Integração Financeira => Financeiro e seleciona o Componente principal que representa a Despesas, com isso, a partir de qualquer geração será incluído e excluído despesas de reembolso. Para Incluir o legado nas vendas, vá na visão de venda => processo => Atualizar Despesas. Ao clicar nesse processo, o sistema via buscar todas as despesas de todas as coligada e associar ao contrato de venda, com isso todos os módulos citados irão ver as parcelas de despesas. Caso não queira visualizar nos relatórios pode colocar o filtro somente dos componentes desejados.

Gerando Parcelas de Despesas - Responsável parametrizado na Definição de Despesa. |

No momento da geração das parcelas das despesas, durante a execução do processo de gerar despesas ou ao salvar uma nova despesa avulsa, será preenchido o responsável por cada parcela da despesa.

O responsável será definido através da parametrização da **definição da despesa**. As informações buscadas na **definição da despesa** serão gravadas na própria despesa. Caso seja incluída uma despesa avulsa, o usuário poderá informar as parametrizações no momento da inclusão.

A parcela será de responsabilidade do cliente caso o parâmetro de responsável default for o cliente e a partir da data definida nos parâmetros.

A informação do fica bloqueada nas parcelas, pois ela será preenchida apenas pelo processo.

Exemplo:

Selecionada a Definição de despesa - Neste exemplo uma definição de Despesa com Responsável ( EMPRESA )

Apenas 1 Parcela.

Informando os valores ( Vista e Prazo ) - Selecionar as unidades ( Imóveis ) e aplicar.

Gerada uma Parcela corretamente para Responsável ( Empresa ).

Editando a **Despesa de Venda** - Agora troco para **CLIENTE** e definir data para inicio de cobrança para

E troco para **10 Parcelas** e SALVO.

As Parcelas são atualizadas.

**Ficam as parcelas com responsabilidade da Empresa até OUTUBRO .**

**Cliente fica Responsável com as Parcelas de Novembro em diante conforme alteração na Despesa de Venda.**

Parcela de Despesa - Informação do Movimento ou Ref do Lançamento. |

Quando se gerar Pagamento de Despesa e o mesmo for para ( Empresa ) será apresentada na parcela as Informações do Movimento ou as informações do lançamento (Identificador - link para o lançamento e status do lançamento, conforme parametrizado.

Além disso, os valores dos lançamentos são gerados automaticamente, ficam bloqueados para alterações manuais para os campos data e valor da parcela de despesa. Esses campos serão preenchidos apenas pelos processos (que já existem).

Exemplo de parcela de Despesa ( **CLIENTE** ) Não tem informção de Movimento ou Lançamento.

* Gerando parcela de Despesa para ( **Empresa** ) - Tipo de Pagamento ( **Gerar Movimento de Faturamento** ).

Parcela passa a ser gerada com os dados do Movimento.

* Gerando parcela de Despesa para ( **Empresa** ) - Tipo de Pagamento ( **Gerar Lançamento Financeiro.)**

Parcela de Despesa gerada com os dados da Ref do Lançamento.

Cubo de Despesas |

No TCGI tem o cubo que apresenta as despesas da venda e as informações relevantes para o cliente.

Este Cubo pode ser Customizado.

## **Exemplo do CUBO gerado com Despesa para Cliente e para Empresa.**

Despesa de Venda ( Cliente Responsável )

Parcelas foram geradas da Despesa.

Empresa ficando Responsável pelas Parcelas com Vencimento de Agosto e Setembro ( 2021 )

Cliente ficando Responsável pelas parcelas de Outubro de 2021 em diante conforme Parametrização.

Ao gerar o CUBO sendo levada as divisões dos valores para Empresa e Cliente e todos os dados da Despesa de Venda.

## **Exemplo do CUBO gerado com Despesa para Empresa.**

Contrato de Despesa gerado para emprsea Responsável com Primeiro Vencimento para Agosto de 2021.

Parcelas geradas.

Cubo sendo gerado com as Informações da Despesa de Venda ( Empresa ).

Layout do CUBO 

O Cubo de Despesa exite 4 Layout para sua geração.

1. Padrão
2. Responsável
3. Sintético
4. Coligada

Exemplo com CUBO **( Responsável ).**

Processo de Regeração de Despesa |

**Regeração de pagamento de Despesa.**

Existem situações em que as datas relacionadas ao início da responsabilidade do cliente pela despesa são alteradas.  
Um exemplo em que responsabilidade passa para o Cliente, o imóvel é vendido ou alugado, a data de entrega do empreendimento ou do próprio imóvel é alterada.  
O processo deverá ser efetuado manualmente pelo usuário, após alterar qualquer uma datas possíveis.  
Nesses casos, se a despesa já tiver sido gerada, a responsabilidade ainda pelo pagamento precisará ser também alterada.  
Por este motivo tem o Processo de Regeração de Pagamento de Despesa, para  possibilitar essa alteração de uma forma mais simples.  
Esse processo irá  alterar o responsável pela despesa das despesas selecionadas.  
Se a responsabilidade definida na geração da despesa for o cliente, e a data de inicio definida for alterada a responsabilidade dos pagamentos serão regerados.   
Somente será aceito a regeração dos titulos anteriores a data definida a data de inicio da responsabilidade do cliente.  
Se a responsabilidade mudar da empresa para o cliente, o processo deverá cancelar os movimentos, lançamentos a pagar, caso tenham sido gerados. Se não for possível o cancelamento (lançamentos baixados, boletos gerados, etc.), o processo irá retornar uma mensagem informando que não foi possível alterar a responsabilidade das parcelas.

Exemplo de Regeração de Despesa ( Com data da **Venda alterada** - Responsabilidade do **CLIENTE** )

Neste exemplo , um contrato de Venda com data de

Foi cadastrada uma Despesa de Venda com responsabilidade da **EMPRESA**,

Editando a Despesa de VENDA ( Alterando para **CLIENTE** como responsável pelas parcelas ) Responsável a partir da Data da Venda do contrato.

Parcelas foram repassadas para o Cliente conforme data da VENDA.

Empresa ficando responsável pelas parcelas até Julho de 2021.

A data ta venda ocorreu uma **alteração** , passando para 01 de Janeiro de 2021 e assim o cliente teria que passar a assuimr as parcelas de **Janeiro 2021 em diante.**

Data da Venda alterada para Janeiro de 2021.

As parcelas de **01/01/2021** ainda estão com a **Empresa como responsável**, para que as mesmas passem para o CLIENTE , basta executar o processo: **Regerar Pagamento de Despesa.**

Selecionando a Despesa de Venda.

Processos > Regerar Pagamento Despesa

Cliente passou a assumer as Parcelas de Janeiro de 2021 em Diante conforme processo.

Mnemônicos Para Histórico Lançamento |

É possível na tela de parâmetros de integração Financeira, configurar um texto com mnemônicos que irá aparece no Histórico do lançamento. Esses mnemônicos são substituídos por informações da venda.

Os mnemônicos são:

[NOM] - Será substituído pelo nome do empreendimento da venda;

[VND] - Será substituído pelo código da venda;

[UNI] - Será substituído pelo código da unidade da venda;

[SUB] - Será substituído pelo código da subunidade da venda;

[EMP] - Será substituído pelo código do empreendimento.

Mnemônicos Para Histórico Movimento Venda |

É possível na tela de parâmetros para geração de movimento venda, configurar um texto com mnemônicos que irá aparece no Histórico da parcela da despesa. Esses mnemônicos são substituídos por informações da venda.

Os mnemônicos são:

Veja Também

---

* Mais sobre Despesa !! [CLIQUE AQUI!](https://tdn.totvs.com/pages/releaseview.action?pageId=599367719)
