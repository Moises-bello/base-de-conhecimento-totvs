---
content_hash: a89f5ff3a1675a3babbfc6b0de3dc522e52fe278769923852b34e15c0abc47ca
fetched_at: '2026-06-29T00:09:49.230340+00:00'
page_id: '435105257'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Alteração dos Imóveis do Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105257
version: 14
---

**Pré-condições**

* Ter habilitado a permissão [02.03.01.21 e 22] para Efetivar / Desfazer aditivo de Alteração dos Imóveis do Contrato, do perfil do TOTVS Gestão de Imóveis, localizada em *Serviços Globais / Segurança / Perfis.*
* Ter efetivado o Contrato de Locação
* Ter incluído um Motivo do Aditivo

**Campos da tela:**

* **Código do aditivo:** Código do aditivo realizado, campo preenchido automaticamente  pelo sistema;
* **Data do aditivo:** Data da criação do aditivo. A partir dessa data será aplicado no Contrato de Locação as alterações do aditivo. No caso do Aditivo de Alteração dos Imóveis do Contrato, a inclusão ou alteração dos Imóveis do Contrato serão realizadas a partir da data do aditivo;
* **Tipo de aditivo:** Exibe o Tipo de Aditivo no qual está sendo cadastrado. Esse campo é preenchido automaticamente pelo sistema, onde o é preenchido pelo Tipo de Aditivo selecionado no Anexo do Contrato de Locação >> Aditivo;
* **Situação do aditivo:** Exibe a situação do aditivo, que pode ser:
  + **Preparação:** O aditivo tem essa situação quando está sendo cadastrado e ainda não foi executado o processo "Efetivar Aditivo" ou quando é executado o processo "Desfazer Aditivo" em um aditivo com a situação "Efetivado". Nessa situação é permitido alterar o aditivo e as modificações cadastradas não são aplicadas ao Contrato de Locação associado;
  + **Efetivado:**O aditivo tem essa situação quando é executado o processo "Efetivar Aditivo". Nessa situação não é possível alterar o aditivo. As modificações cadastradas já foram aplicadas ao Contrato de Locação, quando foi executado o processo "Efetivar Aditivo";
* **Motivo do aditivo:** Motivo do aditivo a ser executado. Novos motivos de aditivos podem ser criados através do Cadastro de Motivo do aditivo, que se encontra no seguinte caminho Aluguel >> Cadastros >> Motivo de aditivo.
* **Número do Aditivo no Cliente:** Campo onde o cliente informar o número do Aditivo no Contrato físico. Podendo assim realizar o agrupamento de vários aditivos do sistema a um aditivo físico.
* **Seleção do Imóveis:** Nesta área o usuário seleciona os imóveis que já existem no contrato de locação para serem alterados ou então seleciona novos imóveis para serem incluídos. Esta ação depende da utilização do campo **Incluir um novo imóvel.**
* Ao editar/incluir um imóvel selecionado, caso o mesmo tenha áreas cadastradas, é possível também editar as áreas do imóvel. Com isso serão exibidos os campos abaixo:
* **Valor do Imóvel anterior:** Campo mostra o último valor informado para o imóvel.
* **Novo valor do imóvel:** Neste campo é possível informar o novo valor para o imóvel.
* **Valor total do aditivo (Sem Desconto):** Disponível a partir da versão 12.1.28, o valor apresentado neste campo é o somatório dos novos valores dos imóveis alterados através do aditivo.

Na grid de **Ocupação de áreas**, são mostrados detalhes das áreas. Ao editar uma área serão exibidos os seguintes campos:

* Cód. Área, Ocupação da área, Disponível (m²), Reservado (m²), Ocupação da área anterior, Valor do m² anterior, Nova ocupação da área, Novo valor do m² ;
* Presente a partir da versão 12.1.22, a opção "Compõe saldo de área para locação é apenas informativa, pois se trata de uma característica da área que não pode ser alterada para cada contrato.

Importante!

* Para as áreas que não compõem saldo, somente será permitido alterar o m² locado para zero. Caso necessite excluir uma ocupação de área, basta definir como zero o campo "Nova ocupação da área".
* Não será permitido zerar todas as ocupações do imóvel.

**Área do Desconto original:**

**Tipo desconto anterior:** Exibe o tipo de desconto aplicado no Contrato de Locação antes da alteração do Aditivo. O Tipo de Desconto pode ser: Valor Final do Contrato, Percentual e Valor m². O valor do campo não pode ser alterado;

**Valor Fim do conteúdo adicionado desconto anterior:** Exibe o valor do desconto aplicado no Contrato de Locação antes da alteração do Aditivo. O valor do campo não pode ser alterado;

**Percentual desconto anterior:** Exibe o percentual do desconto aplicado no Contrato de Locação antes da alteração do Aditivo. O valor do campo não pode ser alterado;

**Aplica reajuste anterior:** Exibe se desconto aplicado antes da alteração do Aditivo, é reajustado conforme a variação do reajuste do Contrato Fim do conteúdo adicionado de Locação. O valor do campo não pode ser alterado;

**Área de Alteração de desconto:**

**Novo Tipo desconto:** Este campo permite definir qual o tipo de desconto será aplicado ao  Contrato de Locação. Possui as seguintes opções:

**Valor Final do Contrato:** Ao escolher essa opção, o valor inserido pelo usuário será descontado do valor final do Contrato de Locação;

**Percentual:** Ao escolher essa opção, o valor inserido pelo usuário será descontado em percentual ao valor final do Contrato de Locação;

\*Valor do M²:\* Ao escolher essa opção, o valor inserido pelo usuário será descontado no valor médio do m². O valor final do contrato será impactado, pois é resultado do (Valor médio do m² \* Área Locada);

* **Observações:** Só poderá ser aplicado Desconto por m² em Contrato de Locação que possuam somente Imóveis do tipo Áreas Fracionadas ou Unificadas. Imóveis do Tipo Imóvel não podem ser aplicado o desconto por m². Assim como não poderá inserir Imóvel do tipo "Imóvel" em Contrato de Locação com o desconto por m²;

**Novo Valor Fim do conteúdo adicionado desconto:** permite o usuário inserir o valor de desconto desejado em aplicar ao Contrato de Locação. Esse campo somente é habilitado quando é selecionado no "Novo Tipo de Desconto" as opções "Valor final do Contrato" ou "Valor do m² ";

**Novo Percentual desconto:** permite o usuário inserir o valor em percentual do desconto no valor final do contrato. Esse campo somente é habilitado quando é selecionado no "Novo Tipo de Desconto" a opção "Percentual";

**Novo Aplica reajuste:** define se o valor do desconto será reajustado conforme a variação do reajuste do Contrato de Locação. Este campo só é habilitado quando é selecionado no "Tipo de Desconto" as opções "Valor final do Contrato" ou "Desconto no valor do m² ";

**Incluindo um Aditivo de Renegociação do Valor de Locação**

**Passo 1 -** Selecione o Contrato de Locação e acesse: Anexo / Aditivo / Alteração de Dados do Imóvel.

**Passo 2 -** Clique em Incluir Aditivo de Renegociação do Valor de Locação.

**Passo 3 -** Preencha os campos:

Código do Aditivo: Campo de preenchimento automático

Data do Aditivo: A data do aditivo deve estar dentro do período de vigência do Contrato de Locação;

Tipo do Aditivo: Preenchido automaticamente

Situação do Aditivo: Preparação

Motivo do Aditivo: Informar um Motivo do Aditivo

**Passo 4 -** Clique em Adicionar o imóvel no qual se deseja alterar o valor da locação.

**Passo 5 -** Foi exibida a tela para preenchimento dos dados do Imóvel. Preencha os campos:

Imóvel

Valor do imóvel anterior: Campo de preenchimento automático.

Novo valor do imóvel

**Observações:**

* Caso queira inserir um novo imóvel no Contrato de Locação, deve ser marcado a opção "Incluir um novo Imóvel", onde será exibido os imóveis que estão disponíveis para Locação.
* Só podem ser incluídos Imóveis de um mesmo Contrato de Administração em um Contrato de Locação;

**Passo 6 -** Salvar

**Passo 7** - 

**Passo 8 -** Verifique que o status do Aditivo foi alterado para Efetivado.

**Passo 9 -** Selecione o Aditivo e clique em Editar Aditivo de Renegociação do Valor de Locação.

**Passo 10 -** Acesse a aba Histórico. Será exibida a informação do campo Observação preenchido ao efetivar o Aditivo.

**Observação:** O aditivo de Alteração dos Imóveis do Contrato não poderá incluir Imóveis do Tipo "Imóvel" no Contrato de Locação com data do aditivo anterior a data final de Escalonamento por M² nas situações "Em preparação" ou "Efetivado".

Importante!

* Se o contrato possui uma garantia associada com vinculo ao valor do contrato, (opção "Vínculo com o valor do contrato" no cadastro de garantias), o sistema exigirá, na efetivação do aditivos de alteração de imóveis, um aditivo de garantia em preparação para ser aplicado. Este aditivo será automaticamente efetivado ao se efetivar o aditivo de alteração de imóvel;
* O aditivo de alteração de imóvel deverá possuir o mesmo número do aditivo de garantia "Em Preparação" para que sejam efetivados corretamente;
* Da mesma forma, ao desfazer o aditivo de alteração de imóvel, o sistema automaticamente deverá desfazer o aditivo de garantia e voltar sua situação para "Em Preparação".

Como Fazer

---
