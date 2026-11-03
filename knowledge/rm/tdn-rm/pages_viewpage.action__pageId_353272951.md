---
content_hash: f8070be0f202663752822e00b087fd02ac90f05054694adb422ab600235c90ab
fetched_at: '2026-06-29T00:08:57.078101+00:00'
page_id: '353272951'
product: rm
source: tdn-rm
title: Gestão de Seguro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353272951
version: 9
---

Afim de atender com maior abrangência ao mercado imobiliário este recurso será destinado a todos os módulo do TIN, permitindo a associação do Seguro a um imóvel, a um contrato de locação ou a um condomínio/ empreendimento, exceto os seguros do contrato de venda que já possuem recurso especifico.

*Desde 1964, todos os condomínios verticais ou horizontais, de qualquer tipo, isto é, formados por prédios residenciais, comerciais, mistos, consultórios, escritórios, flats, apart-hotéis e shopping centers são obrigados, por lei, a ter seguro contra riscos de incêndio, queda de raio e explosões de qualquer natureza que provoquem sua destruição total ou parcial. A cobertura obrigatória é para todas as unidades e para as partes comuns do condomínio. O valor segurado total deve corresponder à soma do valor segurado de cada uma das unidades autônomas e das partes comuns. A quantia encontrada deverá representar o total dos recursos necessários para a reconstrução do prédio, no caso de um sinistro coberto. A exigência do seguro condomínio consta do Decreto-Lei 73/1966 (artigo 20), da Lei 4.591/1964 (artigo 13) e do Código Civil (Lei 10.406/2002, artigos 1.346 e 1.348, inciso IX).  
  
Leia mais em: <http://www.tudosobreseguros.org.br/portal/pagina.php?l=422>  
Copyright : Todos direitos reservados a Escola Nacional de Seguros. Este material não pode ser publicado, transmitido por broadcast, reescrito ou redistribuído sem autorização.   
Veja nossa política de permissão para utilização de conteúdo de nosso site em: <http://www.tudosobreseguros.org.br/sws/tools/reproducao/reproducaoedt.html>*

O Seguro do imóvel pode ocorrer nas seguinte situações:

* **Cobertura durante a Locação**: Ocorre sempre que um imóvel é locado e pode ser feito pelo Administrador do Imóvel ou pelo locatário. O período de cobertura pode variar, mas na maioria das vezes é anual. Quando o imóvel é locado por M2 a responsabilidade de fazer o seguro é sempre do Administrador do imóvel, podendo fazer o rateio do custo a ser cobrado do locatário conforme tempo e metragem locada. Neste tipo de apólice o beneficiário é o Administrador do Imóvel, também pode haver mais de um beneficiário que não o administrador ou proprietário do imóvel. Referente aos seguros de locação podem ser feitos dois tipos seguros, um Predial e o de Responsabilidade Civil.
* **Para Lastro de Operação Financeira**: ocorre quando um imóvel é dado como garantia para uma operação financeira como, por exemplo, empréstimos, e neste caso o beneficiário é a instituição financeira responsável pela operação, logo não há necessidade do imóvel estar locado.
* **Cobertura de Condomínio**: por exigência de lei é necessário que todo condomínio tenha o seguro para a estrutura física do prédio. A obrigação de fazer o seguro é sempre do Sindico e o beneficiário em caso de sinistro é o próprio condomínio, estando sujeito a sanções legais como multas, senão realizado.

 Não há limite de seguros vigentes simultaneamente por imóvel ou por contrato de locação.

No módulo de aluguel a gestão do seguro terá as seguintes opções de acesso:

* No menu Geral: onde serão apresentados todos os seguros de todos os imóveis.
* Anexo ao Contrato de Locação: onde serão apresentados apenas os seguros associados ao imóvel do contrato de locação especifico.
* Anexo ao Imóvel: onde serão apresentados todos os seguros associados ao imóvel, seja ele de cobertura de contrato ou para lastro de operação financeira.

No módulo de condomínio a gestão do seguro terá as seguintes opções de acesso:

* No menu Geral: onde serão apresentados todos os seguros de todos os condomínios.
* Anexo ao Empreendimento: onde serão apresentados apenas os seguros associados ao Empreendimento.

**A Gestão de Seguros terá as seguintes informações em seu cadastro:**

* **Data do cadastro**: data informada pelo usuário, mas o sistema deve trazer por default a data atual do sistema*. (Obrigatório somente na efetivação)*
* **Data da Emissão****:** inicial e data final de vigência do seguro.
* **Objetivo do seguro**: o usuário deverá informar enter as seguintes opções:
  + **Cobertura de Contrato de Locação**:  realizado sempre que o imóvel for locado. Duração de um ano e renovável pelo mesmo período consecutivamente até o fim do contrato. Caso o contrato seja encerrado antes do previsto (rescisão) o seguro deve ser cancelado automaticamente mas deve ser analisada a possibilidade de gerar um aviso pois neste caso há devolução do valor pago pelo seguro. *Opção visível apenas no módulo de aluguel.*
  + **Lastro para Operação Financeiro**: realizado a qualquer tempo com duração variável. *Opção visível apenas no módulo de aluguel.*
  + **Cobertura de Condomínio**: realizado periodicamente desde a constituição do Condomínio. *Opção visível apenas no módulo de Condomínio.*
* **Modalidade de Seguro ou Finalidade de Cobertura** (*dois termos usados no mercado)* (Tabela estruturada): cadastro aberto com campo de código e descrição para informar,  por exemplo, Seguro Predial, Seguro de Responsabilidade Civil, Seguro de Condomínio, etc. Não haverá tratamento sistêmico sobre este campo.
* **Responsável pela Seguro**: Locador (*Somente Aluguel)* ou Locatário (*Somente Aluguel)* ou Sindico (*somente condomínio)*.
  + Quando for informado "Locador" significa que o proprietário/ administrador do Imóvel *(Exemplo: Grupo CB* -*Capital Brasileiro)*, será o contratante do seguro e será necessário controlar o Vencimento dos Seguros via Objeto Gerencial  além de permitir a parametrização de avisos (definir se por formula visual, agendamento ou dashboard de avisos ao usuário contanto que possam ser automatizados);
  + Quando informado *"*Locatário*"* indica que o inquilino deve contratar o seguro e manter o proprietário/ administrador informado. Este responsável só poderá ser atribuído a imóveis que **não** são locados fracionados. Nestes casos a Administradora do Imóvel deve:  
    - Acompanhar o vencimento via relatório do sistema;
    - Verificará se a apólice feita está com as coberturas necessárias (processo fora do sistema) mas com workflow de aprovação e documentos anexados.
    - Associar Apólice digitalizada ligada ao imóvel, no cadastro do seguro;

Alem dos controles acima devem ser disponibilizados os seguintes artefatos:

* + - Relatório geral por vigência de apólice (de todos os imóveis) com vencimento entre dia 1 e 30 dias. O layout deve ser definido em tempo de projeto.
    - Relatório com informações gerais referentes a seguros. O layout deve ser definido em tempo de projeto.

* **Situação do Seguro**: Em Preparação, Vigente, Vencido. Estes status serão pré definido e alterados pelo sistema ou via processo ou pelo usuário.
  + Em preparação: quando o registro foi incluindo mas ainda não está totalmente preenchido e por isso não pode sofrer impacto de processos.
  + Vigente: indica que o seguro foi aprovado e todas as condições foram atendidas, portanto ponde entrar em vigência  e por isso deve ter seu controle de validade ativado.
  + Vencido: indica que a apólice já não cobre sua finalidade.

* **Corretora**: empresa que fez as cotações dos seguros e negocia os valores, intermediando a relação entre a Seguradora e o Segurado. Poderá ser associado um Fornecedor RM.  Esta informação não é obrigatória.
* **Seguradora**: entidade responsável pela emissão e registro da apólice junto a SUSEP.
* **Seguradora Anterior**: campo que será preenchido somente no caso de renovação de seguro.
* **Número da Apólice**:  Campo destinado a indicar o número da apólice gerada pela empresa seguradora, portanto trata-se de um campo informado pelo usuário.
* **Número da Apólice Anterior:**campo que será preenchido somente no caso de renovação de seguro.
* **Processo SUSEP:** número de registrodo processo na Superintendência de Seguros Privados.
* **Beneficiário(s)** (tabela): podem ser associados 1 ou vários beneficiários, neste cadastro será associado um cliente/ fornecedor.
* **Condição de Pagamento**: a condição de pagamento informada será usada na geração do movimento de entrada da cobrança (pedido de compra)

* **Prêmios Contratados**(Tabela): podem ser associados vários prêmios
  + Descrição
  + Valor

* **Coberturas Contratada**s (tabela)
  + Cobertura: campo descritivo obrigatório ou tabela com código e descrição para que seja possível aproveitar em mais de um seguro. Se for uma tabela deve ser criado também um campo para Descrição onde o usuário poderá complementar a informação.
  + Data Inicial e Data Final: campo informado pelo usuário. As coberturas podem ter vigências diferentes.
  + LMI - Limite Máximo de Indenização (R$)
  + LMGA- Limite Máximo de Garantia da Apólice
  + Franquias: descritivo pois ser o valor ou um percentual especifico. (exemplo> 10% dos prejuízos indenizáveis com minimo de R$ 750,00 a franquia pos ...)
  + Premio: campo de valor que o usuário poderá ou não preencher;
* **Premio TOTAL**: somatório do prêmios das coberturas, mas que o usuário poderá informar manualmente já que o usuário pode não informar o valor no cadastro das coberturas e observamos que nem sempre a soma das coberturas representam o valor Premio Total, outra situação que pode gerar diferença de valor é a existência da cobrança do IOF, pois não criaremos este campo a principio; (confirmar com Monica)
* **Valor da Cobertura:** campo de valor informado pelo usuário.
* **Gera Reembolso (Sim ou Não)**: o Locador / Adm, tem o direito de ser reembolsado pelo valor pago pelo seguro, mas não é obrigatório por isso o usuário deve informar quando pode ser gerado o repasse/ reembolso deste valor. O Default deve ser "Sim" quando o responsável for Locador ou Sindico, mas o campo não deve ser apresentado se o responsável for o Locatário.

Conforme "*Objetivo do Seguro*" o sistema permitirá associar um Contrato de Locação, ou Imóvel ou o empreendimento. Quando se tratar de um imóvel podem ser informados mais de um, portanto será necessária a criação de um anexo para indicar o "Objeto" ou Item de Cobertura, onde pode ser indicado um contrato de locação, ou vários imóveis ou um empreendimento.

**PROCESSOS da Gestão de Seguro**

* **"Gerar Pagamento" ou "Integrar com Backoffice"**: esta opção será a responsável pela geração da cobrança e por consequência o título a pagar do seguro e só estará disponível para os seguros que forem de responsabilidade do Locador ou do Sindico. (*Não é o repasse para o inquilino)*
  + Se Protheus: gera Pedido de Compra
  + Se RM: gera Movimento parametrizado

Em ambos os casos será necessária a criação de um parâmetro de integração  para informar os seguintes dados: Tipo de Movimento, Coligada, Filial, Produto, centro de custo e Natureza Financeira Orçamentária. Pode ser utilizado o cadastro já existente de "Parâmetros Movimento" *(cadastros →Parâmetros Movimento)* , mas com um Novo "Tipo de Geração"  especifico e com mnemônicos para Histórico que atendam ao Aluguel, como por exemplo, número e descrição do Imóvel, número e descrição do Contrato de Locação, etc. Este Parâmetro de Geração de Movimento deve ser associado a um parâmetro da coligada afim de dar melhor usabilidade, trazendo sempre o default mas permitindo alteração dos dados. Ainda neste cadastro devem ser ajustadas as opções de Buscar Filial, Buscar Centro de Custo, Buscar Natureza e Buscar Rateio de Centro de Custo para que se informado o  "Tipo de Geração"  = "Movimento de Seguro" adicionar a opção de Contrato de Locação (apenas para aqueles que fizerem sentido).  
  
Na tela do processo de "Gerar Pagamento" ou "Integrar com Backoffice", além do parâmetro acima descrito será necessário apresentar as seguintes informações:

* + - Valor: o sistema deve trazer o valor total do prêmio que o Locador/ Administrador terá que pagar;
    - Condição de Pagamento: número de parcelas que o pagamento será dividido. A Administradora pode  repassar o valor sem desconto quando paga a vista e repassa a prazo, por isso deve ser avaliada a necessidade da criação do campo para informar o valor do Premio a Prazo.
    - Data da Emissão: trazer por default a data atual, mas permitir que o usuário altere afim de informar a data da emissão da Apólice.
    - Observação: campo para que o usuário possa acrescentar alguma informação pertinente e que deve ser levada para a Observação do Movimento.

Dentro do Movimento:

* + O fornecedor do Movimento será a Seguradora.
  + A data de Entrega será a mesma da Emissão

Permitir enviar para o Backoffice a apólice digitalizada associada ao Seguro.

Por se tratar de um processo periódico e repetitivo (anualmente) o sistema deve permitir um acelerador para este cadastro como por exemplo uma cópia de seguro e/ou renovação.

* **Gerar Reembolso (repasse)**  
  Quando o seguro é de responsabilidade do Locador/ Administrador ou do sindico e se tratar de um seguro com Objetivo de fazer a Cobertura do Contrato de Locação,  Imóveis Fracionados ou Empreendimentos é feita a cobrança contra o Locatário chamado de repasse.  
    
  O Seguro pode ser pago a vista  e repassado parcelado ou pago a vista e repassado a vista, condições estas que facilitam o pagamento por parte do locatário conforme já mencionado.  
    
    
  Cenário 1- Cobertura do contrato de locação com Imóvel Integral  
    
  O valor de prêmio pago deve ser cobrado do locatário conforme parcelamento ocorrido na apólice, este valor pode ser cobrado junto com o valor de Aluguel e sendo levado como valor de integração.  
    
    
  Cenário 2- Cobertura de Imóvel Fracionado

  O valor de prêmio pago deve ser cobrado do locatário conforme parcelamento ocorrido na apólice ou determinado nesta geração, este valor pode ser cobrado junto com o valor de Aluguel como valor de Integração.

  Por se tratar de uma locação por área fracionada, deve ser feito o **rateio** para os contratos ativos que tenham parte da área do imóvel.

*Fórmula de Calculo do Rateio*

**Seguro Predial**

Premio Total do Imóvel: R$ 346.704,40

Vigência da Apólice (01/01/2018 a 31/12/2018) Quantidade de Dias Cobertos pela Apólice: 365 dias

Vigência do Contrato de Locação (17/06/2018 a 16/06/2020)

**1º Ratear o Valor total do Seguro pelo prazo em que o contrato de locação fizer intersecção.**

Valor do Seguro no período de Locação = (Dias de Intersecção com Ct Loc)\*(Valor total do Seguro)/ Total de dias da Vigência do Seguro= (197\*R$ 346.704,40) / 365 =**R$ 187.125,38**

**2º Ratear o valor do Período pela metragem locada**

Valor do Seguro por período de Locação E Metragem= (M2 \*Valor Rateado Por período)/ M2Total= (2.648,86\*187.125,38)/102.698,14= R$ 4.826,60

Como áreas totais considera-se a área comum + área privada

Uma Contrato de Locação com X Metros pode começar depois do inicio da Apólice, por isso o cálculo deve ser proporcional.

Um mesmo contrato de locação pode ter mais de um Seguro (1 do inquilino e outro do grupo CB) um por contrato e outro por lastro.

Se forem cobrados vários seguros ao mesmo tempo todos devem constar no título como valores de integração, afim de possibilitar a demonstração da cobrança via boleto.

Se o Administrador do Imóvel pagar o seguro a vista o valor pago terá desconto, mas se o repasse for parcelado será cobrado o valor sem o desconto, ou seja, o beneficio do desconto não será repassado ao locatário se este pagar parcelado.

**ENDOSSO (Anexo do Seguro)**

O endosso é o instrumento que permite alterar a apólice aumentando ou diminuindo as coberturas e seus respectivos valores,  para isso as seguintes informações serão necessárias:

* Prêmios Contratados: trazer por default os prêmios da apólice original permitindo que o usuário altere (incluindo ou excluindo ou alterando);
* Coberturas Contratadas: trazer por default as coberturas da apólice original permitindo que o usuário altere (incluindo ou excluindo ou alterando);
* Premio TOTAL: trazer por default o Prêmio da apólice original permitindo que o usuário altere;
* Beneficiários: permitir alterar, excluir ou incluir novo beneficário.

Além das informação referentes a alteração do seguro, o Endosso deve ter as seguintes informação:

* Número do Endosso: campo informado pelo usuário;
* Descrição (Campo Longo): campo informado pelo usuário;
* Data do Endosso: campo informado pelo usuário;
* Motivo (tabela estruturada): campo informado pelo usuário;
* Data inicial de vigência: campo informado pelo usuário;
* Data Final de Vigência:campo informado pelo usuário;
* Situação: Em Preparação, Vigente e Vencido com o mesmo tratamento do Seguro

**Processos do Endosso**

* + Efetivar
  + Alterar Situação:
    - Se a situação for Vigente: permite alterar para "Em Preparação" ou "Vencido";
    - Se a situação for "Vencido":permite alterar para "Vigente" ou "Em Preparação";
    - Não será possível alterar por este processo a situação "Em Preparação
    - Não permitir alterar a situação para "Em Preparação se ja houver cobrança ou repasse referente ao endosso.
  + Atualizar Cobrança: se o endosso alterar o valor do premio para mais, uma diferença pode ser cobrada e se for para menos um valor deve ser devolvido a Administradora, portanto em ambos os casos pode gerar impacto no Movimento já gerado
  + Atualizar Repasse: da mesma forma que a cobrança pode ser impactada pela alteração de valor do Seguro, o repasse também pode, desta forma os lançamentos financeiros que foram gerados com o repasse do seguro em sua composição devem ser refeitos. Este processo deve localizar tais lançamentos e atualizá-los.

**Considerações do Endosso**

* + Todo endosso pode ser excluído desde que esteja na situação de "Em Preparação";
  + O Endosso só poderá ser editado com a situação "Em Preparação";
  + Permitir anexar o documento de Endosso;

**Considerações Gerais**

* Permitir associar Apólice digitalizada;
* Criar processo para gerar **renovação**, ou seja, que permitirá o acompanhamento de status das cotações que serão realizadas no backoffice.
* Permitir disparar e-mail para responsável pré- definido por renovar apólices com anexo o relatório de seguros a vencer;
* Permitir Aprovação dos Seguros;
* Permitir a criação de campo complementar na tabela de Seguro, Coberturas, Prêmios, Endosso
* **Quando um contrato de locação for Rescindido as apólices relativas a cobertura contratual devem ser encerradas e o valor do premio pago deve ser devolvido ao Administrador, já o locatário, se tiver pago a vista tb deverá ter o valor restituído;**
* **Não será controlado neste recurso se um Seguro for acionado em caso de Sinistro;**
* Criar Cubo que apresenta seguros que estão para vencer nos próximos x dias. Este relatório deve permitir o filtro de multi coligadas. O layout deve ser definido em tempo de projeto.
* Criar Cubo que apresente relação de imóveis com e sem seguro. Este objeto deve permitir o filtro de multi coligadas. O layout deve ser definido em tempo de projeto.
