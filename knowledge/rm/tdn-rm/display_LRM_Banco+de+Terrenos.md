---
content_hash: 93a1342e32f187292c7a0dd9f35cbf2ada40af511d427460da587cb59555466d
fetched_at: '2026-06-29T00:09:14.854601+00:00'
page_id: '421385283'
product: rm
source: tdn-rm
title: Banco de Terrenos
type: documentation
url: https://tdn.totvs.com/display/LRM/Banco+de+Terrenos
version: 8
---

---

O Banco de Terrenos é um repositório onde são registrados os terrenos que uma incorporadora ou construtora tem a disposição para construir.

O terreno pode ou não ser de propriedade da Empresa (incorporadora) ou pode ser prospectado no mercado, assim podem ser identificados dados do proprietário entre outros.

Este repositório pode ou não ser associado a um Estudo de Viabilidade.

De forma geral sua intenção é registrar terrenos disponíveis para investimento.

Ao acessar este cadastro temos as seguintes informações:

**ABA EMPREENDIMENTOS**

* **Prioridade:** : Identifica a prioridade de utilização do terreno. A informação deste campo é retornada pelo lookup do cadastro de *Prioridades*, que por sua vez tem as seguintes informações:
  + **Código:** Informe o código identificador desta prioridade;
  + **Descrição:** Informe a descrição desta prioridade.

Este campo anteriormente era chamado de *ID do Gap*;

* **Nicho:** Cada terreno é classificado segundo uma tabela de nichos de mercado (econômico, upgrade, etc.) e cada nicho possui uma tabela de pontos para a realização do questionário de análise de terrenos.

Cada pergunta do questionário possui 3 (três) faixas de valores que indicam a pontuação para a resposta.

Exemplo: No nicho Econômico, para a Inclinação do terreno, caso seja de 0 a 8%, 10 (dez) pontos, 8 a 11%, 5 (cinco) pontos e > 11% 0 (zero) pontos. A tabela abaixo demonstra um exemplo do questionário de análise de terrenos.

|  |  |  |  |
| --- | --- | --- | --- |
| Nicho: Econômico |  |  |  |
| **Terreno** | **10** | **5** | **0** |
| Inclinação x Implantação | 0 a 8 % | 8 a 11% | > 11% |
| Existência de vegetação de Porte | Inexistente | Existência com facilidade de corte | Existência com dificuldade para corte |
| Solo | 10 | 5 | 0 |
| Resistência à Compressão | Alta | Média | Baixa |
| Resistência dos taludes | Alta | Média | Baixa |

A manutenção do questionário de análise de terrenos é feita em um anexo do cadastro de nichos.

* **Descrição:** A descrição que identifica o terreno como, por exemplo, Lote 10 da Av Brasil.
* **Corretor:** Apresenta um ou mais corretores envolvidos na negociação de compra do terreno.
* **Telefone do Corretor:** É o telefone do corretor.
* **Data da Visita:** Informa a em que foi realizada a visita ao terreno. Este campo é apenas informativo e não terá processos associados a ele.
* **Data da Entrada:** Informa a data em que este terreno foi cadastrada no sistema.
* **Valor Total Pedido:** É o valor do terreno. Este campo está em formato de valor, porém não indica a moeda deste valor, portanto recomenda-se que em caso de valor em moeda estrangeira seja adicionada uma observação sobre este detalhamento no campo destinado a este fim.
* **Representante:** É o contato do representante responsável por este terreno:
  + **Proprietário:** Podem ser informados um ou mais proprietários Telefone: telefone do (s) Proprietário (s)
* **Observação:** Campo para informações diversas que pode ser utilizado, por exemplo, para identificar qual é o proprietário é o responsável pela negociação, entre outras informações gerais.
* **Opção:**
  + **Solicitada a Opção:** Identifica se foi solicitada a opção de compra do terreno.
  + **Data de Vencimento:** Indica até quando a opção de compra é válida.

**ABA LOCALIZAÇÃO**

* **Logradouro:** Nome da rua ou avenida ou outro logradouro onde o terreno está localizado.
* **Número:** Número do endereço onde o terreno está localizado.
* **Bairro:** Bairro do terreno.
* **Cidade:** Cidade do terreno.
* **UF:** Estado da federação onde o terreno está localizado.
* **País:** País, no qual o terreno está localizado.
* **CEP:** Informe o CEP do endereço do terreno.
* **Link Google Earth:** Link do Google Earth.
* **Tipo de Área:** Identifica se o terreno se encontra em Área Urbana ou em Área Rural.
* **Visualizar:** Botão quer permite localizar o terreno no Google Earth.

**ABA DOCUMENTOS**  
Controle de entrega dos documentos pertinentes ao terreno, possuindo um checkbox que deve ser marcada na entrega dos documentos.

Exemplo de documentos que podem ser controlados: autorização do proprietário, certidão de ônus atual, registro, guia de IPTU.

Deve(m) ser informado(s) o(s) código(s) dos documentos de controle e se estes já foram entregues.

**ABA FORMA DE PAGAMENTO**  
Nesta aba será informado como o terreno será pago.

Além de um pagamento padrão em moeda corrente é comum o pagamento de terrenos com outras contrapartidas financeiras como, por exemplo, aluguel do empreendimento durante um período determinado ou permuta física ou financeira.

Ao acessar esta aba temos as seguintes informações:

**Aluguel:** Nesta modalidade de pagamento de terreno, o dono receberá a receita de aluguel do empreendimento construído em seu terreno durante um período determinado.

* **Validade:** É a data o aluguel deste terreno será pago ao dono do terreno.
* **Valor do Aluguel:** É o valor de aluguel que será repassado ao dono do terreno como forma de pagamento.

**Tipo de Permuta:** Nesta modalidade de pagamento de terreno, o dono realiza a troca do mesmo ou por subunidades do empreendimento ou por um percentual do valor da receita da venda do mesmo.

* **Permuta Física:** Ocorre quando o terreno será pago com subunidades (aptos por exemplo) que forem construídas ou no terreno que está sendo comprado ou mesmo em outro empreendimento de outro terreno.
* **Permuta Financeira:** Ocorre quando o terreno será pago através de um percentual da receita obtida com a venda de subunidades do empreendimento.
* **Permuta (%):** É é o percentual (financeiro) da receita que será dado como permuta.
* **Valor Total:** valor total da permuta que geralmente equivale ao valor do terreno.

**Venda:**

* **Histórico de Negociação:** Neste campo livre podem ser registradas todas as informações da negociação, como por exemplo, as datas que a empresa entrou em contato, com quem falou, qual foi a proposta, se foi aceita, ou se houve contraproposta, assim por diante. Trata-se de campo livre para registro de informações gerais da negociação do terreno.
* **Condição de Pagamento:** Neste campo é informado a Forma de Pagamento do terreno. Esta forma de pagamento é um lookup para o cadastro de mesmo nome do sistema. Exemplo: a vista, 12 vezes, etc.

**ABA COMPOSIÇÃO**

Um terreno pode ser composto por vários lotes ou glebas com áreas definidas, sendo que nesta área é possível existir situações de redução da área utilizável.

**Lotes:** Lista de lotes que formam o terreno. Possuí as seguintes colunas:

* **Descrição:** nome do lote ou da gleba. Exemplo: "Lote 01".
* **Área (m2):** área do lote ou gleba.
* **Valor (m2):** valor em metros quadrados do lote ou gleba.
* **Área Total (m2):** soma de todas as áreas de todos os lotes.
* **Valor médio / m2:**  (Σ Valor (m2)) /  (Σ (Área (m2)).
* **Valor Total do Pedido:** Soma do valor de todos os lotes; Valor / m2 (viabilidade): valor do metro quadrado calculado no estudo de viabilidade levando em consideração outras variáveis não tratadas o cadastro do terreno.
* **Valor Total do Pedido (Viabilidade):** valor total pedido pelo terreno levando em consideração outras variáveis não tratadas o cadastro do terreno.

**Possíveis Reduções na Área do Terreno:** É uma lista de situações que diminuem a área útil do terreno. Entre elas estão: Área de Preservação Permanente  Área de Doação.

* **Descrição:** descrição da possível redução na área do terreno. Exemplo: Área de Preservação Permanente.
* **%:** Quanto em percentual da área informada terá redução.
* **Área Líquida:** Área Total (m2)\* (% de possíveis reduções/100).
* **Produção Líquida:** Área líquida \* Coeficiente de Aproveitamento.
* **Varandas:** Quantidade em m2 ocupadas por varandas que representará um ganho final da edificação,
* **Produção de Varanda:** Produção líquida + Varandas.
* **Coeficiente de Aproveitamento:** Nenhum lote pode ter sua área total construída, além dos fatores de reduções existem os coeficientes de aproveitamento que são limites de construção estabelecidos por planos diretores de municípios bem como de ocupação e uso do solo. Assim ao informar um coeficiente de aproveitamento teremos uma redução da área de edificação permitida.
* **Cota de Utilização do Terreno:** Informa qual é a área de cada unidade construída em m2. Exemplo: 10 varandas de 1m2 corresponde a 10 m2 a mais que serão incorporados no campo de " produção de varadas";
* **Unidades Possíveis:** Área líquida / Cota de Utilização do Terreno.
* **Aproveitamento Efetivo:** Área Privativa / Área Remanescente, onde Área Privativa é calculada pela seguinte regra: Área Privativa = Valor Área (Área Total) \* Valor Quantidade e a  Área Remanescente é: Área Remanescente = Área Total Lote - (Área Total Lote \* SOMA (Reduções %)/100) Valor Quantidade corresponde  ao campo de quantidade da unidade selecionada (foco).

**ABA ESTUDO DE PRODUTO**

É possível que uma análise simplificada ou previa seja feita no cadastro do terreno antes mesmo do estudo mais completo. Para isso estão disponíveis os campos:

**Cadastro das unidades**

* **Descrição:** descrição da unidade que será edificada. Ex: apto 1 qto.
* **Qtd:** quantidade de unidades desta característica.
* **R$/ m2. AP:** Valor do metro quadrado da Área privativa. Considera-se neste caso área privativa do espaço em metros quadrados da unidade incluído áreas de depósito que sejam exclusivas para cada unidade.
* **Vagas/ Unidade:** quantidade de vagas de estacionamento por unidade.
* **Área da Unidade:** quantidade de metros quadrados da unidade.
* **Área da Varanda:** quantidade de metros quadrados da varanda da unidade, caso tenha.
* **Área do Terraço:** quantidade de metros quadrados do terraço da unidade, caso tenha.
* **Área total:** Área da Unidade + Área da Varanda + Área do Terraço
* **Área Privativa Total (m2):**
* **Total de vagas:** Total de vagas disponíveis de todos os apartamentos.
* **R$ (m2):** media dos preços do metro quadrado das unidades informadas.
* **VGV Total:** soma do Valor Geral de Vendas das unidades   (Σ (Área total\* Qtd)\* R$/ m2. AP).
* **Total de Unidades:** soma de todas as unidades informadas.
* **Unidades/ Andar:** quantidade de unidades edificadas por andar.
* **Área Média da Unidade:** Área total de cada unidade / quantidade de tipos de unidades.
* **Número de Pavimentos:** número de andares.
* **Número de Torres:** número de torres ou blocos.
* **Área / vagas (m2):** campo informado pelo usuário para informar o tamanho em metros2 de cada garagem.
* **Área Projeção Vagas (m2):** Área / vagas (m2) multiplicado pela quantidade de unidades que tem garagem.
* **Área de projeção (m2):** área média do andar  (Área Média da Unidade\* Unidades/ Andar).
* **Acréscimo (%):** percentual de acréscimo de área no andar/ pavimento.
* **Área com Acréscimo:** Área de projeção (m2)+ área calculada de acréscimo;

**ABA ANÁLISE PRELIMINAR**

* **Valor do Terreno / VGV**
  + **VGV Viabilidade:** Total Ofertado / VGV Total
  + **Valor/ m2 (Viabilidade):** Total Pedido / VGV Total
* **Fração do Terreno / m2 A.P.**
  + **AP Viabilidade:** Total Ofertado / Produção com Varandas
  + **AP Pedido:** Total Pedido / Produção com Varandas
* **Fração do Terreno na Unidade**
  + **Unidade Viabilidade:** Área média das unidades x Valor Viabilidade da Fração do Terreno A.P.
  + **Unidade Pedido:** Área média das unidades x Valor Pedido da Fração do Terreno A.P.

*AP= área privativa*

**ABA FOTOS**

Área destinada a cadastrar fotos do terreno ou demais arquivos de imagens associados ao terreno.

**ABA VIABILIDADE**

Permite associar uma versão de estudo de viabilidade ao terreno para posterior análise trazendo os indicadores de viabilidade.

### Anexos

### Documentações Complementares
