---
content_hash: a715834c5f24eaa2148cc30dccbfc91d0651fb6c44f4e2a23fd8c325534249a9
fetched_at: '2026-06-29T00:09:48.441030+00:00'
page_id: '435105155'
product: rm
source: tdn-rm
title: Totvs Incorporação - Parâmetros - Cadastros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105155
version: 10
---

Nesta opção temos os parâmetros dos cadastros associados ao Empreendimento e ao Fiador, a saber:

### 22.01.02 - Empreendimento

* **Nome para o empreendimento, unidade e sub-unidade:** O sistema permite a personalização das labels descritivas para o Empreendimento, Unidade e Subunidade, de forma que estes cadastros sejam exibidos da forma mais adequada ao ramo de atividade da incorporadora. Estas descrições são apresentadas em vários pontos da interface do TCGI, como menus de acesso, relatórios, portais, aps, etc..
  + **Nome do empreendimento:** é possível de se definir nomes como: empreendimento, torre, condomínio, etc.;
  + **Nome da unidade:** é possível de se definir nomes como: bloco, quadra, etc.;
  + **Nome da subunidade:** é possível de se definir nomes como apto, lote, loja, etc.
* **Usar custo diferido:** Ao marcar este parâmetro, será habilitado o campo "valor opcional do custo diferido" na aba Custos do cadastro de Empreendimento. Neste campo será informado o percentual do custo diferido sobre o valor das parcelas. O custo diferido será calculado através do percentual cadastrado no empreendimento sobre o valor das parcelas de uma venda e será gravado no valor opcional escolhido do Financeiro e no campo "vr\_custo\_dif" da tabela "xparcelapagamento". Esta informação poderá ser utilizada em relatórios e a sua finalidade é informacional.

* + **Valor Opcional para Custo Deferido:** se o parâmetro custo diferido for marcado, o usuário deverá informar qual valor opcional do TOTVS Gestão Financeira que tenha ação = "nada", para gravar o valor do custo diferido.

* **Usar controle de vaga:** Se ativado, será habilitado no cadastro de sub-unidade, o cadastro de vagas de garagem.
* **Empreendimento outros imóveis:** Informe o código do empreendimento utilizado para controlar e vender os bens móveis ou imóveis recebidos de terceiros como parte de pagamento em uma venda.
* **Tipo característica subunidade:** Ao escolher o tipo de característica, será apresentado no cadastro de Unidade/Subunidade, na aba Manutenção da Subunidade, o campo do Tipo de Característica escolhido e o campo para escolher o Índice da Característica. Ao selecionar o índice da característica, será gravado automaticamente esta característica para a Subunidade.
* **Considerar empreendimento já entregue:** Informe como o sistema deverá preencher a data de próximo reajuste do componente de CM e Juros Após a Entrega do Empreendimento na efetivação da venda. As opções são:
  + **Um mês após a data da Entrega:** Se o empreendimento ainda não foi entregue, da data do próximo reajuste de juros será a data de entrega do empreendimento mais um mês;
  + **Mesmo mês da data da Entrega:** A data do próximo reajuste de juros será a própria  data de entrega do empreendimento;
* **Precisão Fração Ideal:** Informe o número de casas decimais que terá a Fração Ideal das Sub-Unidades;

* **Máscara do Código do Empreendimento:** Informe qual a máscara do código do Empreendimento;

* **Usar data opcional empreendimento:** São tabelas definidas de acordo com a necessidade do cliente. Estas tabelas podem ser de uso obrigatório ou não, podendo ter até 5 tabelas opcionais de datas para o empreendimento. Com as seguintes opções:
  + **Nome data opcional empreendimento:** informe o nome que será exibido na label descritiva desta data, na interface de cadastro para o usuário. Exemplo: Data Averbação, Data Liberação Fiscalização, etc.;
  + **Obrigar usar data opcional:** informe se o uso destas datas pelos usuários será obrigatório ou não.

Em versões mais antigas, estas etapas também apresentam a opção:

* **Não associar modalidades à empreendimentos:** Se marcado, o sistema não irá fazer a consistência das modalidades associadas aos empreendimentos. Sendo assim, qualquer empreendimento poderá utilizar qualquer modalidade.

### 22.01.03 - Fiador

* **CGC/CPF único para fiadores:** Se este parâmetro for ativado, o sistema irá barrar a inclusão de clientes com CGC/CPF em duplicidade.
* **Associar fiador a sub-unidade:** Se este parâmetro for ativado, ao cadastrar uma venda, só poderá informar os Fiadores que estão associados à sub-unidade da venda.
