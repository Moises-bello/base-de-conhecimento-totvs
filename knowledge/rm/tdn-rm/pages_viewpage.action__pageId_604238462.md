---
content_hash: a61a33aa2952b4f8bf9af5e2d2860b6ec4a853c4bff07815a14b587e323e09ca
fetched_at: '2026-06-29T00:10:58.170941+00:00'
page_id: '604238462'
product: rm
source: tdn-rm
title: Movimentos para Geração de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604238462
version: 34
---

Geração de Contrato pelo TOTVS Gestão de Estoque, Compras e FaturamentoParametrização - TOTVS Gestão de Estoque, Compras e Faturamento

Os movimentos do TOTVS Gestão de Estoque, Compras e Faturamento devem ser parametrizados para que sejam capazes de gerar contrato. A parametrização do movimento para geração de contrato no TCOP é realizada na etapa de Contratos e na etapa de Projetos.

Para que seja possível geração de contrato, o checkbox "Gerar Contrato" deve estar marcado nas duas etapas.

Etapa 52 - Contratos:

Etapa 71 - Projeto:

No cadastro de usuário, o usuário deve possuir permissão para geração do contrato. No cadastro de usuário, deve-se selecionar o usuário desejado no sistema Gestão de Estoque, Compras e Faturamento e abrir o anexo Permissões por Tipo de Movimento para que seja possível conceder a permissão para Gerar Contrato.

Selecionar o tipo de movimento e conceder permissão para Gerar contrato.

Essa parametrização deverá ocorrer para cada coligada que o usuário acessar.

Movimentos para Geração de Contrato

A visualização dos movimentos para geração de contrato é controlada nos perfis de usuário. Para que o usuário possa visualizar os movimentos, o perfil do usuário deve ter permissão de acesso em cada coligada que ele utilizar.

São duas opções, de gerar  contrato a partir do movimento e gerar aditivo a partir de movimento:

Os movimentos serão visualizados em **Controle | Contrato | Movimentos para geração de contrato**

**Importante: Serão exibidos somente movimentos capazes de gerar contrato no TCOP conforme a parametrização do tipo de movimento no TOTVS Gestão de Estoque, Compras e Faturamento; e conforme as permissões de usuário, perfil e movimento por coligada.**

Para facilitar a visualização dos movimentos será possível utilizar os filtros, de coluna por coligada:

e filtro da visão:

Geração de Contrato

A geração de contrato poderá ser executada a partir da tela dos Movimentos para geração de Contrato. É possível que sejam selecionados mais de um movimento para geração porém não será possível gerar contrato caso o Tipo de Movimento seja diferente.

Os Movimentos do TOTVS Gestão de Estoque, Compras e Faturamento contém itens associados. Ao Gerar Contrato a partir do movimento, os produtos/serviços serão associados ao contrato.

Ao Gerar Contrato a partir do movimento, serão validados para Geração do Contrato no TCOP os parâmetros de Associação de Itens/Objetos do Contrato (Parâmetros de Projeto(F6)|Contratos|Associação de itens e Objetos)

Ao executar o processo, o projeto deve estar calculado e devem ser informados a Finalidade do Contrato, "Num. Contrato", as datas do contrato e o Cliente/Fornecedor do Contrato

* **Prestação de Serviço:**
  + O item associado ao movimento deve ser um produto do tipo Serviço.
* **Fornecimento de Material:**
  + O item associado ao movimento deve ser um produto do tipo Produto.
  + Apenas insumos ligados ao grupo DNIT "Materiais" e com unidade diferente de Percentual poderão ser vinculados ao contrato de fornecimento de material.
* **Contrato de Insumo:**  
  + A associação de insumos para contratação somente será utilizada em contratos do tipo "Fornecimento de material" e "Contratos de insumo" em projetos que utilizam insumo para contratação.
* **Extra-Histograma:**
  + Para a utilização do Contrato com a finalidade Extra Histograma ou Extra é necessário definir nos parâmetros do projeto a finalidade desejada.
  + O Contrato Extra Histograma possibilita que sejam criados contratos onde podem ser consumidos apenas insumos que não façam parte do Histograma do Projeto, ou seja, os insumos que não constam na Curva ABC de Insumos do Projeto.
* **Contrato Extra**
  + O contrato Extra tem as mesmas funcionalidades do contrato de Extra Histograma, diferenciando apenas na associação de insumos ao contrato, isso porquê o contrato Extra permite a associação de insumos planejados e não planejados ao contrato.

**Validações do Processo:**

* **Clientes Protheus podem usar essa funcionalidade desde que utilizem o Módulo de Compras do RM. [Saiba mais](https://tdn.totvs.com/pages/releaseview.action?pageId=309396414)**
* **Contratos do tipo Prestação de Serviços só serão exibidos no processo caso o item vinculado ao movimento seja do tipo Serviço.**
* **Somente movimentos pendentes podem gerar contrato a partir do movimento, pois ao gerar contrato a partir do movimento, o movimento terá seu status alterado para recebido.**
* **As mesmas consistências da associação de itens de contrato serão validadas ao gerar o contrato para o TCOP.**
* **Não será possível gerar contrato se forem selecionados movimentos de tipos diferentes.**
* **Não será possível gerar contrato no TCOP sem informar o Cliente/Fornecedor.**
  + **Caso o Cliente/Fornecedor estiver preenchido no movimento, ao executar o processo o lookup de Cliente/Fornecedor do contrato virá preenchido conforme o Movimento.**
  + **Caso o Cliente/Fornecedor não estiver preenchido no movimento, é obrigatório informá-lo no processo de Geração de Contrato.**
* **Quando o parâmetro Consiste saldo do pedido e contrato está habilitado, caso o movimento de contrato impacte o saldo do projeto, o sistema realiza o estorno do pedido antes da geração do contrato, evitando que o saldo seja consumido duas vezes.**

No próximo passo serão exibidas as tarefas que estão no rateio do movimento e suas respectivas: Quantidade contratada, Valor unitário contratado e o % que a quantidade contratada representa no planejamento.

Ou insumo, dependendo da finalidade informada na tela anterior:

Caso os itens do movimento sejam produtos que não estão vinculados a nenhum insumo do projeto no TCOP será exibida uma nova etapa para que o insumo seja associado ao produto/serviço:

A geração de contrato também pode ser feita utilizando insumos para contratação, caso o projeto esteja configurado para utilizar.

Ao final do processo o contrato é criado conforme o movimento:

Após o contrato ser gerado, o movimento terá seu status alterado para "Recebido":

Geração de Aditivos

A geração de **Aditivo** a partir de movimentos recebidos do TCOP, incluindo o comportamento automático de **estorno dos itens do pedido**.o gerar contrato a partir de um movimento, o movimento tem seu status alterado para recebido e o mesmo não é capaz de gerar contrato novamente.

**Ao acessar a tela Movimentos para Geração de Contrato você verá:**

* Lista de movimentos vindos do TCOP

### O que fazer:

✔ Localize o movimento desejado  
✔ Selecione o registro

Após selecionar o movimento, inicie o processo de geração.

### Na tela “Gerar contrato a partir do movimento marque a opção gerar Aditivo, nesta parte é apresentado os seguintes campos para preenchimento.

* **Contrato:** Selecione o contrato desejado para realizar o aditivo

* **Número do Aditivo:** Campo automático, números de aditivos gerados apartir da quantidades de aditivos ja gerados para o contrato selecionado.
* **Data de Utilização**
* **Data de Prorrogação** (se aplicável)
* **Descrição**

Nesta próxima tela é listado os itens disponíveis para seleção:

# ✅ **Após finalizar, o sistema automaticamente**:

### ✔ Gera o Aditivo

* Vinculado ao contrato informado e cria um Movimento com status: **A Pagar**

---

# 🔄**Na tela do Pedido**

* O campo **Quantidade Estorno** será atualizado com a quantidade estornada
* Os itens utilizados no aditivo serão **estornados automaticamente**

Cancelamento/Estorno

Ao gerar contrato/aditivo a partir de um movimento, o movimento tem seu status alterado para recebido e o mesmo não é capaz de gerar contrato novamente. O cancelamento de um contrato/aditivo gerado a partir de um movimento, realiza o estorno, ou seja, ao cancelar ou excluir o contrato/aditivo gerado pelo movimento, automaticamente o movimento volta ao seu status de Pendente. E caso este movimento tenha sido gerado por um pedido, a quantidade de estorno; preenchida com a geração do contrato será zerada com o cancelamento ou exclusão do contrato/aditivo.

Movimento que gerou contrato:

Contrato cancelado:

Movimento após cancelamento do contrato:
