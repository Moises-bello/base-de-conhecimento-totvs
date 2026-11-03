---
content_hash: 700e5cedd5450adc8cb456e9d2cfd05eccb14f7fcb92540147c2ac4e980b669f
fetched_at: '2026-06-29T00:12:08.156367+00:00'
page_id: '928960392'
product: rm
source: tdn-rm
title: 02. Contratos 2.0 | Cadastros
type: documentation
url: https://tdn.totvs.com/display/LRM/02.+Contratos+2.0+%7C+Cadastros
version: 73
---

A inclusão de novos contratos é realizada por meio do menu: **"Contratos | Gestão de Contratos 2.0 | Manutenção de Contratos"**, onde são solicitadas informações obrigatórias para o registro, tais como: número do contrato, data do contrato, data de início da vigência, tipo de contrato, natureza do contrato (Compra, Venda ou Arrendamento Mercantil), status do contrato e cliente/fornecedor associado.

Embora os demais campos não sejam essenciais para a inclusão de um contrato, dependendo da parametrização realizada, eles podem se tornar obrigatórios, uma vez que fazem parte de controles internos da empresa.

---

ContratoPaginasDoContratotrueIdentificação

Na etapa de identificação do contrato, devem ser preenchidos os campos que definem o contrato, seu tipo, status, natureza, duração e as partes envolvidas.

Além disso, nesta mesma etapa, são exibidos o valor total e o saldo do contrato, conforme os itens que o compõem.

Campos - Identificação

### Grupo - Dados do Contrato

**1. Código**

* O código do contrato é a forma usual de identificação dos contratos, a entrada de dados para esse campo pode ser configurada através de máscara permitindo que o cliente customize o código de forma aderente ao seu negocio.
* O tamanho deste campo e sua forma de preenchimento está de acordo com o parâmetro **Máscara do código do contrato** que pode ser acessado em [Parâmetros | Gestão de Estoque, Compras e Faturamento | Contratos | Definições Gerais](https://tdn.totvs.com/x/ochEGQ)
* Para mais informações de preenchimento acesse

**2. Nome**

* O nome do contrato permite um descritivo detalhado e livre sobre o mesmo, pode ter até 100 caracteres.

**3. Status**

* O status do contrato pode ter qualquer valor que tenha sido configurado pelo cliente em sua tabela "Status de Contratos".
* O status além da informação descritiva também direciona se o contrato pode ou não:  Faturar e Cancelamento.

Caminho: Cadastro do Status de Contrato

Gestão de Compras e Faturamento > Contratos > Tabelas de Contrato > Status de Contrato

**4. Tipo**

O tipo de contrato pode ser de qualquer valor que tenha sido configurado pelo cliente em "Tipos de Contrato".

Caminho: Cadastro dos Tipos de Contrato

Gestão de Compras e Faturamento > Contratos > Tabelas de Contrato > Tipos de Contrato 

****5. Natureza****

As naturezas disponíveis para o contrato são:  
✔️Compra  
✔️Arrendamento Mercantil  
✔️Venda

**6. Contratante / Arrendatário**

| Natureza | Contratado |
| --- | --- |
| Compra | O contratante é uma das "filiais cadastradas para a coligada" onde o contrato está sendo feito. |
| Arrendamento Mercantil | O arrendador é uma das "filiais cadastradas para a coligada" onde o contrato está sendo feito. |
| Venda | O contratante é um Cliente/Fornecedor cadastrado no sistema (global ou da coligada do contrato). |

**7. Contratado / Arrendador**

| Natureza | Contratado |
| --- | --- |
| Compra | O contratado é um Cliente/Fornecedor cadastrado no sistema (global ou da coligada do contrato). |
| Arrendamento Mercantil | O arrendador é um "Cliente/Fornecedor" cadastrado no sistema (global ou da coligada do contrato). |
| Saldo Contrato | O saldo do contrato é o ("Valor total do contrato" subtraído do "Valor Faturado do Contrato"). |

### Grupo - Datas do Contrato

| Tipo de Data | Descrição |
| --- | --- |
| Data do Contrato | Data em que o contrato foi firmado. |
| Data Início Vigência | Início da vigência do contrato. |
| Data Fim Vigência | Término da vigência do contrato. |
| Data Fim Vigência (aditivo) | Data final após alteração por aditivo (preenchido automaticamente). |
| Data Auxiliar | Data Auxiliar do contrato, será apresentada após marcar o parâmetro Usar Campos: Data Auxiliar do Contrato, acessando os parâmetros > **| 04.05 | Contratos > Definições Gerais |** . |

### Grupo - Valores do Contrato

| Tipo de Valor | Descrição |
| --- | --- |
| Valor Contrato | Valor total do contrato considerando todos os itens do contrato, este campo será preenchido automaticamente. |
| Valor Faturado | Valor já faturado do contrato considerando faturamento de todos os itens do contrato, este campo será preenchido automaticamente Saldo Contrato. |
| Saldo Contrato | O saldo do contrato é o ("Valor total do contrato" subtraído do "Valor Faturado do Contrato"). |

Grupo - Valores Extras

| Tipo de Valor | Descrição |
| --- | --- |
| Valor Abatimento | Valor total de abatimento realizados e todos os itens do contrato. |
| Valor Acréscimo | Valor total de acréscimo realizados em todos os itens do contrato. |

Tabelas

A página Tabelas do contrato trás vários grupos de dados, são eles:

* Tabelas de Classificação
* Tabelas de Faturamento
* Funcionários
* Representante

Campos - Tabelas

### Grupo - Tabelas de Classificação As Tabelas de Classificação são configuráveis acessando: [Parâmetros | Gestão de Estoque, Compras e Faturamento | Contratos | Definições Gerais](https://tdn.totvs.com/x/ochEGQ)

### **Parâmetros > 04.01.04.01 | Parâmetros Gerais > Tabelas > Classificação.** Campos:

* Tabela 1
* Tabela 2
* Tabela 3
* Tabela 4
* Tabela 5

Os campos relacionados às Tabelas de Classificação são exibidos conforme parametrização.  
Para que essas tabelas sejam apresentadas no Contrato/Item do Contrato, deve-se configurar acessando: *Parâmetros > 04.05.04 | Contratos > Faturamento > Tabelas 2/4*.

### Grupo - Tabelas de Faturamento

As Tabelas de Faturamento são configuráveis no módulo Gestão Financeira, acessando: *Parâmetros > Contas a Pagar > Tabelas Opcionais*.

Campos:

* Tabela 1
* Tabela 2
* Tabela 3
* Tabela 4
* Tabela 5

Os campos relacionados às Tabelas de Faturamento são exibidos conforme parametrização.  
Para que essas tabelas sejam apresentadas no Contrato/Item do Contrato, deve-se configurar acessando: *Parâmetros > 04.05.04 | Contratos > Faturamento > Tabelas 1/4.*

### Grupo - Funcionários

### É possível parametrizar até quatro funcionários por Natureza do Contrato, nomeando-os conforme a necessidade do processo.

* Nos contratos de Compras/Arrendamento Mercantil, é possível definir quatro nomes.
* Nos contratos de Vendas, outros quatro nomes diferentes podem ser atribuídos.

Para configurar, acesse: *Parâmetros > 04.05.04 | Contratos > Faturamento > Tabelas 3/4 e Tabelas 4/4.*  
Isso possibilita uma melhor adequação dos cadastros às regras de negócio.

Observação

Caso não haja nenhuma parametrização, serão exibidos apenas dois campos de funcionários e comissões para preenchimento.

Grupo - Representante

* A Tabela de Representante é configurável acessando: *Parâmetros > 04.01.04.08 | Parâmetros Gerais > Tabelas > Representante.*
* É possível definir o nome visível desse campo.
* Também é possível configurar a informação retornada ao pesquisar representantes.
* Para que o Representante seja apresentado no Contrato, deve-se configurar acessando: *Parâmetros > 04.05.04 | Contratos > Definições Gerais > Usar Campos > Flag Representante.*
Contábil/Fiscal

Informações contábeis e fiscais atrelada ao contrato.

Campos - Contábil/Fiscal

### Grupo - Fiscal

Natureza de Operação → Indica a natureza da operação que será definida para os faturamentos do contrato. A natureza de operação é cadastrada no Módulo Gestão Fiscal, sendo apresentadas todas as naturezas ativas da coligada atual.  
  
  
Grupo - Contábil

Centro de Custo **→** Indica o centro de custo associado ao contrato, o centro de custo é cadastrado no Módulo Contábil, serão apresentados todos os centros de custos ativos.

Departamento → Indica o departamento associado ao contrato, o departamento é cadastrado no Módulo Contábil, serão apresentados todos os departamentos ativos.

Adicionais

Os campos adicionais do contrato trazem informações não obrigatórias, mas que podem ser importantes conforme o tipo do contrato e a necessidade da empresa.

Campos - Adicionais

### Grupo - Adicionais

### Observação → Observação sobre o contrato realizado.

### Campo Livre 1 → Campo livre configurável pelo cliente.

### Campo Livre 2 → Campo livre configurável pelo cliente.

### Campo Livre 3 → Campo livre configurável pelo cliente.

### Os campos livres poderão ser renomeados conforme a necessidade da empresa acessando: *Parâmetros > 04.05 | Contratos > Campos Opcionais 1/2.*

### Grupo - Endereço/Contato

**Contato do Cliente/Fornecedor para Entrega**  
Qual é a pessoa de contato no cliente/fornecedor que pode ser acionada, se necessário, no ato da entrega. 

**Contato do Cliente/Fornecedor para Pagamento**  
Qual é a pessoa de contato no cliente/fornecedor que pode ser acionada para assuntos relacionados a pagamento.

Grupo - Histórico

Histórico associado ao contrato, podendo ser Curto ou Longo:

* Histórico Curto: permite a inclusão de até 255 caracteres.
* Histórico Longo: não possui um limite determinado.

Para habilitar o histórico no contrato, acesse: *Parâmetros > 04.05 | Contratos > Campos Opcionais 2/2*.

### Grupo - Reajustes

**Mês de Aniversário**

Mês de aniversário do contrato.

Campos Complementares

Os campos complementares do contrato 2.0 permitem a personalização de informações específicas e individuais necessárias para cada contrato do cliente.  
É possível criar diversos campos com nomes e tipos diferentes. Esses campos estarão disponíveis ao acessar: [Cadastros | Campos Complementares | Contratos](https://tdn.totvs.com/x/ushEGQ)

Atenção

Os campos complementares do contrato 2.0 são os mesmos utilizados no contrato 1.0. Dessa forma, todos os campos complementares já cadastrados no contrato estarão disponíveis no contrato 2.0 e em seus respectivos itens de contrato.  
O acesso ao cadastro dos campos complementares está vinculado à configuração de segurança do perfil do usuário.

ItensFilhosContratotrueItens do Contrato

O contrato é composto de itens que identificam o que está sendo negociado no contrato e as características dessa negociação, o item de contrato tem muitas informações e uma página dedicada a ele, acesse a página "Item do Contrato" 

Histórico de Processos

No histórico de processos, é possível acompanhar os dados de todos os processos executados no contrato. As informações disponíveis são:

* Tipo de Processo: Nome e código do processo que foi executado.
* Descrição: Informações sobre os parâmetros do processo executado, além de dados adicionais relevantes.
* Executado em: Data em que o processo foi efetivamente executado.
* Executado por: Usuário que solicitou a execução do processo.
* Contrato: Identificador do contrato.
* Item: Número sequencial do item do contrato. (VALIDAR)
* ID: Identificador do processo.
* Código da Coligada: Código da coligada.
* Tipo Processo: Tipo de processo
* ID Ocorrência Prazo: Identificador da ocorrência de Revisão Vida Útil gerada no módulo patrimonial.
* ID Ocorrência Valor: Identificador da ocorrência de Acréscimo gerada no módulo patrimonial.

Atenção

* Não é possível editar um histórico, mas é possível visualizar no formato detalhe.
* Ao regerar as parcelas, todo o histórico vinculado as parcelas anteriores serão excluídos.
* A exclusão de um item, excluirá  todo o histórico vinculado ao item excluído.
* A exclusão do contrato, excluirá todo o histórico do contrato.
Dicas

* É possível agrupar colunas para facilitar a localização dos dados.
* Ao realizar pesquisa utilizando "Ctrl+F" procura-se o termo pesquisado em todos os campos visíveis, em todos os pontos que o mesmo é localizado o texto fica destacado.
Histórico de Contabilidade

Nesta página, é apresentada a lista de todos os históricos de contabilidade registrados pelos processos que modificam valores no contrato.

| **Campo** | **Descrição** |
| --- | --- |
| Id Lançamento | Identificador do lançamento contábil (Número atribuído a cada lançamento contábil individual). |
| Id Operação | Identificador da operação (identificador que agrupa um conjunto de lançamentos contábeis que fazem parte de uma mesma operação). |
| Lote | Lote contábil (conjunto de lançamentos contábeis que são processados em grupo). |
| Data | Data da partida (data em que o lançamento contábil foi efetivado, ou seja, a data em que a transação ocorreu ou foi registrada no sistema). |
| Processo | Descrição ou nome do processo que gerou o histórico da contabilidade. |

**➡️ Grid do Contrato:**

Grid de exibição dos campos do contrato, exibindo alguns dos campos das abas acima em conjunto com  os relatados abaixo:

Grid - Contrato

**Identificador**

Identificador único do contrato por coligada.

**Status Faturamento**

* Á Faturar: Parcelas ainda não geraram movimento;
* Parcialmente Faturado: Ao menos uma parcela gerou movimento;
* Faturado: Todas as parcelas geraram movimentos.

**Status Previsão Financeira:**

* Não Previsionado: Todos os itens do contrato estão com status Previsão Financeira = Não Previsionado;
* Previsionado: Todos os itens do contrato estão com status Previsão Financeira = Previsionado;
* Parcialmente Previsionado: possuem itens com status Previsão Financeira = Não Previsionado e Previsionado.

**Integrado ao Patrimônio**

* Sim: O contrato está integrado ao módulo patrimonial
* Não: O contrato não está integrado ao módulo patrimonial.
Item do ContratotrueItem do Contrato 

As informações definidas no contrato serão carregadas automaticamente para os respectivos campos dos itens do contrato, isso porque funcionam como um default, que será utilizado durante a inclusão dos seus itens.

Arrendamento Mercantil

Em contratos com natureza do tipo Arrendamento Mercantil só é possível cadastrar um único item.

PaginasDoItemDeContratotrueIdentificação Campos - Identificação

### Grupo - Dados do Item

**Número Sequencial**

Na grid de exibição de itens do contratos, cada item é atribuído com um "Número Sequencial" que reflete sua ordem de criação. Este número é gerado automaticamente para fornecer uma sequência crescente que facilita a visualização e o gerenciamento dos itens listados. Por exemplo:

* + Item 1: Número Sequencial 1
  + Item 2: Número Sequencial 2
  + Item 3: Número Sequencial 3

**Remoção e Reordenação Automática**

É importante destacar que, ao excluir um dos itens da lista, o sistema automaticamente reordena o número sequencial dos itens restantes para preencher qualquer lacuna criada pela remoção. Isso garante que a sequência permaneça consecutiva e os números sequenciais reflitam corretamente a ordem atual dos itens, sem interrupções. Por exemplo, caso o Item 2 seja excluído, a sequência será ajustada da seguinte maneira:

* + - Antes da remoção:

      * Item 1: Número Sequencial 1
      * Item 2: Número Sequencial 2
      * Item 3: Número Sequencial 3
    - Após a remoção do Item 2:

      * Item 1: Número Sequencial 1
      * Item 3: Número Sequencial 2

Essa funcionalidade de reordenação automática contribui para manter a organização e a clareza visual na grid de itens do contratos, facilitando a compreensão da ordem dos itens para os usuários.

**Tipo Faturamento**

Indica o tipo de faturamento desse item do contrato, o tipo de faturamento pode ser:

* + Periódico - Um contrato que ocorre de forma recorrente durante um período com valores fixos, ou seja, é conhecido o valor que será faturado periodicamente.
  + Medição por valor - Um contrato que ocorre de forma recorrente durante um período sem valores fixos, ou seja, não é conhecido o valor que será faturado periodicamente, ocorre medição para indicar o valor a faturar no período. Neste tipo de contrato será controlado por valor, sendo possível realizar medições de qualquer valor até o valor total do item do contrato.
  + Medição por quantidade - Um contrato que ocorre de forma recorrente durante um período sem quantidades fixas, ou seja, não é conhecido a quantidade que será faturada periodicamente, ocorre medição para indicar a quantidade a faturar no período. Neste tipo de contrato será controlado por quantidade, sendo possível realizar medições de qualquer quantidade até a quantidade total do item do contrato.

**Produto/Serviço**

Indica o produto ou serviço contratado.  
A descrição do produto apresentada no filtro será a definida no parâmetro > *| 04.01 | Parâmetros Gerais > Tabelas > Produto > Definições Gerais > Descrição do Produto| .*

**Unidade**Qual a unidade de medida utilizada para o produto contratado.

### Grupo - Datas do Item

| Data | Descrição |
| --- | --- |
| Data Inicio Vigência | Indica o inicio da vigência do item do contratado. |
| Data Fim Vigência | Indica o fim de vigência do item do contrato. |
| Data Fim Vigência (Aditivo) | Indica o fim da vigência do item contratado alterado por aditivo. |
| Data Fim Curto Prazo | Indica a data de corte do que é considerado "curto prazo" para efeito contábil. (Campo especifico e obrigatório quando o contrato tiver natureza  Arrendamento Mercantil) |
| Data Cancelamento | Caso o item tenha sido cancelado, aqui vamos ter indicativo da data em que ocorreu o cancelamento. |

**Grupo - Valores do Item**

**Quantidade**

| Tipo de Contrato | Descrição |
| --- | --- |
| Contrato periódico | Indica a quantidade do produto/serviço contratada por período. |
| Contrato de medição por quantidade | Indica a quantidade total do contrato de medição. |
| Contrato de medição por valor | Neste tipo de contrato serão realizadas medições de valores, desta forma a quantidade é fixa em 1. |
| Arrendamento Mercantil | A quantidade é fixa em 1. |

**Valor / Valor Arrendamento**

| Tipo de Contrato | Descrição |
| --- | --- |
| Contrato periódico | Indica o valor do produto/serviço por unidade. |
| Contrato de medição por quantidade | Indica o valor do produto/serviço por quantidade contratada. |
| Contrato de medição por valor | Indica o valor total do item contratado. |
| Arrendamento Mercantil | Indica o valor do arrendamento. |

**Taxa Juros**Taxa de juros mensal aplicada ao Arrendamento Mercantil. (Apresentado somente quando o contrato for natureza  Arrendamento Mercantil).

**Custos Iniciais**Quaisquer custos diretos iniciais incorridos pelo arrendatário, utilizado na integração com o modulo Patrimonial. (Apresentado somente quando o contrato for natureza  Arrendamento Mercantil).

**Custos Futuros**Estimativa de custos a serem incorridos pelo arrendatário na desmontagem e remoção do ativo subjacente, restaurando o local em que está localizado ou restaurando o ativo subjacente à condição requerida, utilizado na integração com o modulo Patrimonial. (Apresentado somente quando o contrato for natureza  Arrendamento Mercantil).

**Desconto**Desconto aplicado ao item do contrato.  
  
**Despesa**Despesa aplicado ao item do contrato.  
  
**Aditivo Quantidade**Indica a quantidade do produto/serviço contratada por período após a efetivação de aditivo.  
  
**Aditivo Valor**Indica o valor do produto/serviço por unidade de medida  após a efetivação de aditivo.  
  
**Valor Parcela**Caso o Número de Parcelas informado na aba de Faturamento do item do contrato não houver sido informado ele será considerado como 1 para o cálculo descrito abaixo.

* + Contrato periódico: É composto por "*Quantidade x Valor*" subtraído do Desconto e  acrescido da Despesa.
  + Contrato de medição (quantidade e valor): É composto pelo *{ "Quantidade x Valor" subtraído do Desconto e  acrescido da Despesa } / Número de Parcelas*

Após o preenchimento da Aba Faturamento este campo informará o valor da úlitma parcela.

**Valor Total**Caso o Número de Parcelas informado na aba de Faturamento do item do contrato não houver sido informado ele será considerado como 1 para o cálculo descrito abaixo.

* + Contrato periódico: É composto por *{ "Quantidade x Valor" subtraído do Desconto e  acrescido da Despesa } x Número de Parcelas*
  + Contrato de medição (quantidade e valor): É composto por *{ "Quantidade x Valor" subtraído do Desconto e  acrescido da Despesa }*
TabelasCampos - Tabelas 

### Grupo – Tabelas de Classificação

```
As Tabelas de Classificação são configuráveis por meio do seguinte caminho:  
Parâmetros > 04.01.04.01 | Parâmetros Gerais > Tabelas > Classificação
```

* Campos disponíveis: Tabela 1, Tabela 2, Tabela 3, Tabela 4, Tabela 5
* Os campos relacionados às tabelas de classificação são exibidos conforme parametrizados.

```
Para que as tabelas de classificação sejam apresentadas no Contrato / Item do Contrato, é necessário configurar em:  
Parâmetros > 04.05.04 | Contratos > Faturamento > Tabelas 2/4
```

### Grupo – Tabelas de Faturamento

As Tabelas de Faturamento são configuráveis no módulo Gestão Financeira, acessando:  
Parâmetros > Contas a Pagar > Tabelas Opcionais

* Campos disponíveis: Tabela 1, Tabela 2, Tabela 3, Tabela 4, Tabela 5
* Os campos relacionados às tabelas de faturamento são exibidos conforme parametrizados.

Para que as tabelas de faturamento sejam apresentadas no Contrato / Item do Contrato, é necessário configurar em:  
Parâmetros > 04.05.04 | Contratos > Faturamento > Tabelas 1/4

### Grupo – Natureza

**Natureza Orçamentária / Financeira**       Indicador na natureza orçamentária do item do contrato. Serão apresentadas todas as naturezas ativas da coligada global e atual.

Faturamento

Na página Faturamento do Item do Contrato temos as informações necessárias ao faturamento do contrato a geração dos movimentos  e a indicação do frente do emitente e do destinatário.

Campos - Faturamento

### Grupo - Condições Gerais

**Periodicidade**  
Indica a periodicidade em que ocorrem os faturamentos do contrato. A periodicidade também representa uma carência de igual período antes do primeiro vencimento.  
As opções de periodicidade são:

| **Semanal** | **Quinzenal** | **Mensal, Bimestral, Trimestral, Semestral e Anual** |
| --- | --- | --- |
| Deve-se escolher umdia da semana como vencimento:   * + - Domingo     - Segunda-feira     - Terça-feira     - Quarta-feira     - Quinta-feira     - Sexta-feira     - Sábado | Deve-se escolher dois dias de vencimento por mês, com as regras:   * + - Os vencimentos devem estar entre os dias 1 e 31     - O primeiro vencimento deve ser inferior ao segundo | Escolher um dia do mês entre 1 e 31 |

**Dia do Vencimento**

Indica o dia em que ocorre o vencimento do contrato. Neste dia, será realizado o faturamento da parcela correspondente. O dia de vencimento varia de acordo com a periodicidade escolhida, conforme descrito a seguir:

**1.Definições por Periodicidade:**

* + - Semanal: deve-se escolher um dos dias da semana como vencimento (ex.: segunda-feira, quarta-feira etc.).
    - Quinzenal: deve-se escolher dois dias de vencimento por mês.
    - Mensal: deve-se escolher um dia de vencimento por mês, podendo ser o último dia.
    - Semestral e Anual: deve-se escolher um dia do mês como vencimento.

**2. Carência para o Primeiro Vencimento**

Antes do primeiro vencimento, deve-se respeitar uma carência mínima, conforme a periodicidade definida:

| Periodicidade | Carência Mínima |
| --- | --- |
| Semanal | 7 dias |
| Quinzenal | 15 dias |
| Mensal | 1 mês |
| Bimestral | 2 meses |
| Trimestral | 3 meses |
| Semestral | 182 dias |
| Anual | 1 ano |

**Observação:**  
No cálculo da carência, considera-se o dia de início da vigência do contrato.

**Exemplos de Cálculo da Carência**

* + - Início de vigência: 01/01  
      Periodicidade: Quinzenal  
      Vencimentos definidos: 15 e 25  
      ➝ Primeiro vencimento será em 15/01
    - Início de vigência: 02/01  
      Periodicidade: Quinzenal  
      Vencimentos definidos: 15 e 25  
      ➝ Primeiro vencimento será em 25/01

> **📌 Importante:** Sempre que o Dia do Vencimento for definido como "31", nos meses que não possuem 31 dias, será considerado automaticamente o último dia do mês.

**Vencimento Imediato**

 Indica que o vencimento da primeira parcela será imediato, não havendo a carência  descrita no tópico acima. Desta forma, quando o Vencimento Imediato estiver = Sim, seguirá a seguinte regra:

* + Caso a Data de vigência do contrato seja maior que a data do primeiro vencimento, a data da primeira parcela será no dia da data de vigência.
  + Caso a Data de vigência do contrato seja menor que a data do primeiro vencimento, a data da primeira parcela será no dia da data do primeiro vencimento.

**💡Explicando o Vencimento Imediato**, observe que no cálculo para o primeiro dia de vencimento não será considerado a carência do período desejado, levando em consideração apenas da data de vigência do contrato e data do primeiro vencimento.   
     Sendo assim segue exemplos:

| **Periodicidade** | **Início de Vigência** | **Vencimento(s) Definido(s)** | **Primeiro Vencimento** |
| --- | --- | --- | --- |
| **Semanal** | 05/01/2024 (sexta-feira) 10/01/2024 (quarta-feira) | 08/01/2024 (segunda-feira) 08/01/2024 (segunda-feira) | 08/01/2024 (segunda-feira) 10/01/2024 (quarta-feira) |
| **Quinzenal** | 01/01 20/01 26/01 | 15 e 25 15 e 25 15 e 25 | 15/01 25/01 26/01 |
| **Mensal / Bimestral / Trimestral / Semestral / Anual** | 10/01/2024 | 15 | Mensal: 15/01/2024 Bimestral: 15/02/2024  Trimestral: 15/03/2024  Semestral: 15/06/2024  Anual: 15/01/2025 |
|  | 20/01/2024 | 15 | Mensal: 20/01/2024 Bimestral: 20/02/2024  Trimestral: 20/03/2024   Semestral: 20/06/2024  Anual: 20/01/2025 |

> **📌 Importante:** O Vencimento Imediato se aplica apenas à primeira parcela, eliminando a carência inicial. Todas as demais parcelas seguirão o período e as datas de vencimento definidas.

**Número de Parcelas**Define o número de parcelas ou medições previstas para o item do contrato.  
Ao salvar o item, será gerada automaticamente uma quantidade equivalente de parcelas, considerando todos os parâmetros definidos na página de faturamento.  
  
**Condição de Pagamento**Especifica a condição de pagamento que será copiada para o movimento gerado no processo de faturamento do contrato.

**Tipo de Movimento**

Determina o tipo de movimento que será utilizado no faturamento das parcelas.  
⚠️ **Atenção:** Se este campo não estiver preenchido, o processo de faturamento do contrato **não será executado**.

Para definir um tipo de movimento padrão (default) para contratos de compra e/ou venda, acesse:  
Parâmetros > `04.05.04 | Contratos` > `Definições Fat. de Contrato 2/3`.  
  
  
**Tipo de Produto para Faturamento**Os Tipos de Produto para Faturamento são cadastrados em:  
Cadastro > `Contratos` > `Tabelas de Contrato` > `Tipo de Produto para Faturamento`.

Para que os tipos de produto apareçam nos itens do contrato, é necessário ativar a flag correspondente em:  
Parâmetros > `04.05.04 | Contratos` > `Definições Gerais` > Flag "Tipo prod. p/faturamento".

**Faturar item separadamente**

          Quando a opção **"Faturar item separadamente"** está marcada, um movimento de faturamento individual é gerado para aquele item específico.

          O campo  **não  é visível** **para itens em contratos de arrendamento mercantil**.

Grupo - Frete  
No contrato, é possível selecionar uma entre quatro opções de frete para a entrega do item contratado:

* + **Terceiros** → Um terceiro é responsável pelo pagamento do frete.
  + **CIF** → O vendedor assume todos os custos e riscos relacionados ao transporte da mercadoria até o destinatário.
  + **FOB** → A responsabilidade do vendedor termina no momento em que a mercadoria é despachada.
  + **Nenhum Frete** → Não há cobrança ou controle de frete.

A opção selecionada será automaticamente enviada para o movimento gerado durante o faturamento do contrato.

### Grupo - Emitente

**Filial**

Indica a filial do emitente.

**Local de Estoque**

Exibe os locais de estoque disponíveis para a filial selecionada.

**Município**

Ao selecionar um município, o estado (UF) é preenchido automaticamente.  
Ao selecionar um estado, serão exibidos apenas os municípios pertencentes àquele estado.  
Para visualizar novamente todos os municípios, é necessário apagar o valor do campo de estado (lookup de UF).

**UF (Unidade Federativa)**Ao selecionar o estado, são listados apenas os municípios correspondentes.

> **📌 Importante:** A pesquisa de UF é realizada somente pelo **código** do estado.

**Serviço**Código do serviço prestado ou adquirido. Este campo deve ser preenchido caso deseje enviar a informação para o movimento gerado no faturamento do contrato.

### Grupo - Destinatário

**Destinatário**Indica um cliente/fornecedor como destinatário do item do contrato.

Contábil/Fiscal

Informações para contabilização do contrato e dados fiscais do mesmo.

Campos - Contábil/Fiscal 

### Grupo - Fiscal

**Natureza de Operação**

Define a natureza da operação que será aplicada aos faturamentos do contrato.  
As naturezas de operação são cadastradas no **Módulo de Gestão Fiscal** e serão exibidas todas as naturezas **ativas** disponíveis.

### Grupo - Contábil

**Centro de Custo**Especifica o centro de custo associado ao contrato.  
Os centros de custo são cadastrados no Módulo Contábil e serão listados todos os centros de custo ativos.

**🔗Vide regra:**  [Rateio de Centro de Custo](https://tdn.totvs.com/display/LRM/01.+Contratos+2.0+%7C+Cadastros#PaginasDoItemDeContrato--382646637)

**Departamento**Indica o departamento vinculado ao contrato.  
Os departamentos são cadastrados no Módulo Contábil e serão exibidos todos os departamentos ativos.

Adicionais

Informações adicionais do item de contrato

As informações  do grupo  "Reajustes" fornece dados para o processo de reajuste de contratos "Reajuste de Preço" localizado em "Manutenção de contrato | Processos → Reajuste de Preço".

Campos - Adicionais

### Grupo - Reajustes

**Índice**  
Índice base utilizado para o reajuste do contrato.

> ⚠️ *Obrigatório que seja utilizado um índice.*

**Dia da Cotação**  
Define o dia de referência da cotação do índice base.

**Meses de Defasagem**  
Informa o número de meses de defasagem aplicados ao índice.

### Grupo - Financeiro

**Conta/Caixa**  
Conta ou caixa utilizada para a geração da previsão financeira.

**Moeda**  
Moeda considerada para a geração da previsão financeira.

### Grupo - Adicionais

**Campo Livre 1**  
Campo livre configurável pelo cliente.

**Campo Livre 2**  
Campo livre configurável pelo cliente.

> 💡 Os **campos livres** podem ser renomeados conforme a necessidade da empresa, acessando:  
> `Parâmetros > 04.05 | Contratos > Campos Opcionais 1/2`.

### Grupo - Histórico

**Histórico**  
Texto associado ao contrato, podendo ser:

* + **Histórico Curto**: permite até 255 caracteres.
  + **Histórico Longo**: não possui limite de caracteres.

> 🔧 Para habilitar o histórico no contrato, acesse:  
> `Parâmetros > 04.05 | Contratos > Campos Opcionais 2/2`.

Campos Complementares

Os campos complementares permitem a personalização de informações específicas e individuais para cada item do contrato, de acordo com as necessidades do cliente.

É possível criar diversos campos com nomes e tipos diferentes, tornando o contrato mais flexível e adaptado às particularidades de cada operação.

📍 Os campos ficam disponíveis na tela de Itens do Contrato, acessando: `Mais > Campos Complementares`.

Atenção

Os campos complementares do Contrato 2.0 são específicos e exigem cadastro independente em relação ao Contrato 1.0.  
Além disso, a segurança referente ao gerenciamento desses campos também é exclusiva para o Contrato 2.0, garantindo controle individualizado.

Rateio de centro de custo

Permite indicar o **rateio de centro de custo** a ser utilizado na geração do faturamento das parcelas. Como o rateio é vinculado apenas no momento da geração das parcelas, ele pode ser atualizado durante a vigência do contrato, impactando os próximos faturamentos.

> ⚠️ **Importante:**  
> Caso esteja utilizando o rateio por centro de custo, só será possível faturar o item do contrato se o rateio estiver com 100% distribuído.

Preenchimento Automático:

1. Inclusão de Item: Se o Centro de Custo estiver preenchido, será criado um rateio de 100% para o centro informado.
2. Alteração de Item:

* + Se o Centro de Custo for alterado e existir apenas um rateio, ele será atualizado automaticamente.
  + Se houver mais de um rateio, os valores existentes serão mantidos.
  + Caso o Centro de Custo seja excluído, todos os rateios vinculados serão removidos.

Campos - Rateio de centro de custo

#### Centro de Custo Centro de custo que compõe o rateio do item do contrato.

#### Percentual Percentual atribuído ao centro de custo no rateio.

#### Valor de Referência Valor utilizado apenas para o cálculo proporcional do percentual de rateio do centro de custo.

> 🔎 Observação:  
> Caso a conversão de algum valor de referência para percentual gere dízima periódica, poderá ser necessário editar manualmente um dos rateios, ajustando o percentual restante para fechar os 100%.

#### Histórico Campo destinado à descrição de observações relevantes relacionadas à linha de rateio.

Atenção

Não é permitido editar o Centro de Custo de um rateio já existente.  
Caso seja necessário realizar a alteração, o procedimento correto é excluir o rateio atual e incluir um novo com o Centro de Custo desejado.

Parcelas

Nesta página do item de contrato, são exibidas as parcelas geradas automaticamente com base nas informações de faturamento preenchidas no item.

As parcelas são criadas e atualizadas automaticamente ao salvar o item, desde que todos os dados necessários para sua geração estejam corretamente informados: quantidade, valor, periodicidade, vencimento e número de parcelas.

Caso haja alteração em qualquer um desses dados de faturamento, as parcelas existentes serão excluídas (incluindo todo o histórico associado), e novas parcelas serão geradas de acordo com as novas informações.

Campos - Parcelas

| **Campo** | **Descrição** |
| --- | --- |
| Código da Coligada | Código da Coligada do contrato. |
| Identificador do Contrato | Identificador do contrato. |
| Identificador do Item do Contrato | Identificador do item do contrato. |
| Número da Parcela | Número da parcela inserida para o item do contrato. Esta numeração é gerada sequencialmente. |
| Status | Os status das parcelas são atualizados conforme a execução dos processos do contrato:  • **A Faturar** – Status inicial, sem execução de processos. • **Previsionada** – Quando gerada uma previsão financeira via processo *Gerar Previsão*. • **Faturada** – Quando o movimento é gerado pelo processo *Faturar Contrato*. • **Inativa** – Quando uma medição zera o valor da parcela. |
| Data de Vencimento | Data de vencimento da parcela, que pode ser editada. Caso a parcela tenha previsão, esta será atualizada com a nova data. |
| Valor da Parcela | Valor calculado conforme o tipo de faturamento do item do contrato. |
| Valor de Abatimento | Valor registrado no processo *Gerar Abatimento ou Acréscimo do Item do Contrato*. |
| Valor de Acréscimo | Valor registrado no processo *Gerar Abatimento ou Acréscimo do Item do Contrato*. |
| Justificativa | Justificativa registrada no processo *Gerar Abatimento ou Acréscimo do Item do Contrato*. |
| Classificação de Prazo | Preenchido como "C" Curto quando a data da parcela for menor ou igual à *Data Fim Curto Prazo*, e "L" Longo para as demais parcelas. Preenchido apenas para contratos de Arrendamento Mercantil. Quando o contrato é diferente de Arrendamento será apresentado "N" Nenhum. |
| Valor Presente | Fórmula: `Valor Parcela / (1 + Taxa de Juros) * Número de Parcelas`. Preenchido apenas para contratos de Arrendamento Mercantil. |
| Taxa Juros | Informada no cadastro do item e alterada no processo de aditivo. Preenchida apenas para contratos de Arrendamento Mercantil. |
| Amortização de Juros | Fórmula: `Saldo Devedor * (Taxa de Juros / 100)`. Preenchido apenas para contratos de Arrendamento Mercantil. |
| Amortização da Parcela | Fórmula: `Valor Parcela - Amortização de Juros`. Preenchido apenas para contratos de Arrendamento Mercantil. |
| Saldo Devedor | Fórmula: `(Primeira Parcela = Valor Presente Total) + Amortização de Juros - Valor Parcela`. Preenchido apenas para contratos de Arrendamento Mercantil. |

Importante

Durante o processo de arredondamento ou truncamento dos valores das parcelas, podem ocorrer pequenas diferenças em relação ao valor total do item do contrato.

Para garantir a consistência dos valores:

👉 O sistema aplica automaticamente essa diferença à última parcela.

Assim, o valor total do item permanece correto, mesmo com ajustes mínimos nas demais parcelas.

Históricos Histórico de Reajuste

Nesta seção, são exibidos todos os reajustes aplicados ao item de contrato, com base nas configurações preenchidas na aba Adicionais | Reajustes.

| **Campo** | **Descrição** |
| --- | --- |
| Data de Reajuste | Data de início da aplicação do reajuste. |
| Valor Anterior do Item | Valor original do item do contrato, antes do reajuste. |
| Valor Atual do Item | Valor do item após a aplicação do reajuste. |
| Executado em | Data em que o reajuste foi efetivamente executado no sistema. |
| Executado por | Usuário que executou o reajuste no sistema (caso diferente do usuário que cadastrou). |
| Memória de Cálculo | Detalhamento completo do processo de reajuste: valores considerados, índices aplicados, fórmulas utilizadas, entre outros. Facilita o entendimento do que foi aplicado em cada reajuste. |
| ID Ocorrência Valor | Identificador da ocorrência de Acréscimo gerada no módulo patrimonial. |

Histórico de Aditivos

Nesta página, é apresentada a lista de todos os aditivos aplicados ao item de contrato.

| **Campo** | **Descrição** |
| --- | --- |
| Número Sequencial | Número sequencial do aditivo dentro do item do contrato. |
| Número | Identificação numérica do aditivo. |
| Tipo de Aditivo | Tipo do aditivo realizado: Valor, Quantidade ou Prazo. |
| Efeito do Aditivo | Indica se o aditivo representa um acréscimo ou uma redução. Aplicável apenas aos tipos: Valor e Quantidade. |
| Valor | Valor aditivado ao item. Preenchido quando o aditivo for do tipo Valor e informado o campo de valor. |
| Percentual | Percentual aditivado ao item. Preenchido quando o aditivo for do tipo Valor e informado o campo de percentual. |
| Quantidade | Quantidade aditivada ao item. Preenchido quando o aditivo for do tipo Quantidade. |
| Quantidade de Parcelas | Quantidade de parcelas adicionadas ao item. Preenchido quando o aditivo for do tipo Prazo. |
| Taxa Juros | Esse campo é preenchido em contratos de arrendamento mercantil. Fica vazio quando a taxa não foi informada no processo. |
| Data de Vigência | Data de início da vigência do aditivo. |
| Data de Assinatura | Data de assinatura oficial do aditivo. |
| Justificativa | Justificativa registrada para realização do aditivo. |
| Memória de Cálculo | Detalhes do processo de aditivo, incluindo os dados utilizados e valores considerados. Facilita a compreensão do que foi aplicado em cada caso. |
| Executado em | Data em que o aditivo foi registrado no sistema. |
| Executado por | Usuário responsável por executar o processo no sistema. |
| Novo Valor Parcela | Novo valor da parcela informado no aditivo de prazo. |
| ID Ocorrência Prazo | Identificador da ocorrência de Revisão Vida Útil gerada no módulo patrimonial. |
| ID Ocorrência Valor | Identificador da ocorrência de Acréscimo gerada no módulo patrimonial. |

Histórico de Medição

Nesta página, é apresentada a **lista de todas as medições executadas** para o item de contrato.

| **Campo** | **Descrição** |
| --- | --- |
| Número da Medição | Número sequencial da medição. |
| Status | Indica o status de faturamento: Faturado ou Não Faturado. |
| Número da Parcela | Refere-se à parcela do contrato vinculada à medição. |
| Data da Medição | Data em que a medição foi realizada. |
| Executado em | Data em que a medição foi registrada no sistema. |
| Quantidade | Quantidade medida. |
| Valor | Valor unitário aplicado na medição. |
| Valor Total | Resultado da multiplicação: Quantidade × Valor. |
| Município | Código do município referente à medição. |
| UF | Código do estado (Unidade Federativa). |
| Serviço | Código do serviço conforme cadastro no município. |
| Justificativa | Justificativa registrada para a medição realizada. |

> **Observação:**  
> Quando a medição for por **quantidade**, ao medir a **quantidade restante**, poderão ocorrer **ajustes de valor** devido a **arredondamento de dízimas**.  
> Ao medir a **quantidade total**, a somatória das medições deverá ser **igual ao valor total do item** medido.

Histórico de Reclassificação

Nesta página, é apresentada a lista de todos as reclassificações contábeis aplicadas ao item de contrato (apenas para contratos de arrendamento mercantil).

| **Campo** | **Descrição** |
| --- | --- |
| Número Sequencial | Número sequencial da reclassificação dentro do item do contrato. |
| Meses a Incrementar | Número de meses em que a data fim curto prazo vai avançar. |
| Data da contabilização | Data utilizada na contabilização. |
| Utiliza último dia do mês ? | Marcada quando a data fim curto prazo é alterada para o último dia do mês. |
| Memória de Cálculo | Detalhes do processo de reclassificação, incluindo os dados utilizados e valores considerados. Facilita a compreensão do que foi aplicado em cada caso. |

**➡️ Grid itens do Contrato:**O grid de itens do contrato apresenta uma visualização consolidada de informações do item, reunindo campos exibidos nas abas superiores, além dos listados abaixo:

Grid - Itens do Contrato

**Grid itens do Contrato:**

Grid de exibição dos campos do item de contrato.

A posição de cada coluna pode ser alterada, clicando no ícone de Engrenagem.

**Identificador**

Identificador único do item de contrato por coligada.

**Número Sequencial**

Na grid de exibição de itens do contratos, cada item é atribuído com um "Número Sequencial" que reflete sua ordem de criação. Este número é gerado automaticamente para fornecer uma sequência crescente que facilita a visualização e o gerenciamento dos itens listados. Por exemplo:

* + - Item 1: Número Sequencial 1
    - Item 2: Número Sequencial 2
    - Item 3: Número Sequencial 3

**Remoção e Reordenação Automática**

É importante destacar que, ao excluir um dos itens da lista, o sistema automaticamente reordena o número sequencial dos itens restantes para preencher qualquer lacuna criada pela remoção. Isso garante que a sequência permaneça consecutiva e os números sequenciais reflitam corretamente a ordem atual dos itens, sem interrupções. Por exemplo, caso o Item 2 seja excluído, a sequência será ajustada da seguinte maneira:

* + - * Antes da remoção:

        + Item 1: Número Sequencial 1
        + Item 2: Número Sequencial 2
        + Item 3: Número Sequencial 3
      * Após a remoção do Item 2:

        + Item 1: Número Sequencial 1
        + Item 3: Número Sequencial 2

Essa funcionalidade de reordenação automática contribui para manter a organização e a clareza visual na grid de itens do contratos, facilitando a compreensão da ordem dos itens para os usuários.

**Status Faturamento**

Status do item de contrato.

* + Á Faturar: Parcelas ainda não geraram movimento
  + Parcialmente Faturado: Ao menos uma parcela gerou movimento
  + Faturado: Todas as parcelas geraram movimentos
> ⚠️ **Importante:**  
> A posição de cada coluna pode ser alterada, clicando no ícone de Engrenagem.

Restrições de edição de campos

Quando houver previsão financeira, integração com o patrimônio, contabilização ou movimentos com status Faturado ou Parcialmente Faturado, os seguintes campos do contrato terão a edição bloqueada:

* Status
* Natureza
* Data do Contrato
* Data de Início da Vigência
* Data de Fim da Vigência

Quando houver previsão financeira, integração com o patrimônio, contabilização ou movimentos com status Faturado ou Parcialmente Faturado, os seguintes campos do item do contrato terão a edição bloqueada:

* Tipo de Faturamento
* Produto
* Unidade
* Data de Início da Vigência
* Data de Fim da Vigência
* Quantidade
* Valor
* Desconto
* Despesa
* Vencimento Imediato
* Periodicidade
* Dia de Vencimento / Dia da Semana
* Dia do Primeiro Vencimento / Dia do Segundo Vencimento (para periodicidade quinzenal)
* Nº de Parcelas

Quando houver item no contrato, a natureza não poderá ser alterada de *Compra/Venda* para *Arrendamento Mercantil* (ou vice-versa).
