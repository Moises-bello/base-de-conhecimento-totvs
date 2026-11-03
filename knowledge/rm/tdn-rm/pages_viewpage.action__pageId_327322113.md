---
content_hash: a8e63ffdc45731147c44d4e666561b595830cb91767b868661c876c16933e25a
fetched_at: '2026-06-29T00:08:48.590959+00:00'
page_id: '327322113'
product: rm
source: tdn-rm
title: Eliminação de Resíduos - Integração Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327322113
version: 12
---

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Pedido de Material** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Pedido de Material* | *PrjPedidoMaterialAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **PrjVerificaEliminacaoResiduosAction** | *Verificar Eliminação de Resíduos* | | *PrjVerificaEliminacaoResiduosAgendadoAction* | *Verificar Eliminação de Resíduos - Agendamento* | |
| **Cadastros Iniciais:** | *Projeto, Produtos, Insumos, Tarefas, Cronograma e Pedido de Material.* |
| **Parâmetro(s):** |  |
| **Tickets relacionados** | *Não se aplica - Versão Stored: <http://tdn.totvs.com.br/pages/releaseview.action?pageId=271847998>* |
| **Issue:** |  |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *SQL Server e Oracle.* |
| **Tabelas Utilizadas:** | * *RM: MITEMPEDIDOMATERIAL.* * *PROTHEUS: SC1 e SC7* |
| **Sistema Operacional:** | *Windows* |

**Procedimento para utilização:**

**Na Visão de Pedidos de Materiais**

1. Execute os processos necessários para eliminação de resíduos no Protheus;
2. Acesse a visão de pedidos de materiais  e selecione o pedido integrado com o Protheus;
3. Execute o processo "Verificar Eliminação de Resíduos". A execução dessa rotina não bloqueia o usuário, podendo o mesmo utilizar simultaneamente outras rotinas do sistema;
4. Analise a quantidade estornada dos itens do pedido.

Quando executada pela visão de pedidos, o sistema permite a escolha de um ou vários pedidos na Eliminação de Resíduos, sendo que todos os pedidos selecionados serão processados mesmo que já tenham sido processados anteriormente. Este comportamento visa possibilitar a atualização da quantidade estornada quando uma nota fiscal é excluída após o processo de Eliminação de Resíduos já ter sido executado no Protheus.

##### Agendamento (Somente Ambiente 3 Camadas)

1. Utilize o menu "Executar" à direita da aplicação RM;
2. Pesquise por "Verificar Eliminação de Resíduos - Agendamento" e execute;
3. Informe os dados necessários para o agendamento. Este processo necessita que sejam informadas a coligada e o projeto, porém, caso o usuário esteja logado no TOTVS Obras e Projetos em algum projeto, os sistema automaticamente terá essa informação;
4. Após a execução, analise a quantidade estornada dos itens do pedido.

Na execução por agendamento são verificados todos os pedidos do projeto que não tenham sido analisados em processamentos anteriores, o que significa que a execução por agendamento controla os pedidos verificados, ou seja, caso tenham sido finalizados ou já tenha ocorrido a sua eliminação de resíduos no Protheus o pedido não será reprocessado.

Quando processados via agendamento, os itens dos pedidos são marcados para não serem reprocessados de acordo com as seguintes regras:

* Considera que o pedido foi totalmente atendido, caso a totalidade da quantidade solicitada tenha sido contemplada na emissão da nota fiscal;
* Considera que houve eliminação de resíduos de acordo com a marcação nas tabelas do Protheus.

Após identificada a quantidade atendida, será automaticamente atualizado o campo quantidade estornada dos itens do pedido de material. Desta forma esta quantidade fica disponível para ser novamente utilizada em um novo pedido.

Informações exemplificadas do Processo:

Informações exemplificadas do Processo:

**1.****Pedido enviado para o PROTHEUS**

**2. Solicitação de Compras no PROTHES**

**3. Pedido com quantidade a menor**

**4. Solicitação após eliminação de resíduos na SC**

**5.** **Nota Fiscal com quantidade a menor**

**6. Pedido com eliminação de resíduos**

**7. Resumo a Deduzir no TOP**

**8.** **Execução do Processo com sucesso**

**9. Exemplo da estrutura** **Json de retorno:**

{"pageSize":1,

    "data":{"movAssignments":[

                               {"itemNumber":"99|01|000019|0001",

                               "companyInternalId":"99|01",

                               "documentNumberSC":"99|01|000019",

                               "unitofMeasureInternalId":"99||UN",

                               "qujeSC":150000,

                               "quantitySC":200000,

                               "documentNumberPC":"99|01|000020|1",

                               "qujePC":100000,

                               "quantityPC":150000,

                               "residuoPC":"S",

                               "cotacaoSC":"99|01|XXXXXX",

                               "itemInternalId":"99||0003",

                               "residuoSC":"S"},

                               {"itemNumber":"99|01|000019|0002",

                               "companyInternalId":"99|01",

                               "documentNumberSC":"99|01|000019",

                               "unitofMeasureInternalId":"99||UN",

                               "qujeSC":50000,

                               "quantitySC":100000,

                               "documentNumberPC":"99|01|000020|1",

                               "qujePC":40000,

                               "quantityPC":50000,

                               "residuoPC":"S",

                               "cotacaoSC":"99|01|XXXXXX",

                               "itemInternalId":"99||0003",

                               "residuoSC":"S"},

                               {"itemNumber":"99|01|000019|0003",

                               "companyInternalId":"99|01",

                               "documentNumberSC":"99|01|000019",

                               "unitofMeasureInternalId":"99||UN",

                               "qujeSC":50000,

                               "quantitySC":100000,

                               "documentNumberPC":"99|01|000020|1",

                               "qujePC":40000,

                               "quantityPC":50000,

                               "residuoPC":"S",

                               "cotacaoSC":"99|01|XXXXXX",

                               "itemInternalId":"99||0003",

                               "residuoSC":"S"}]}

                               ,"page":1}

Também é possível, através do navegador, "chamar" o serviço REST passando seus parâmetros para obter o retorno do Protheus:

A exclusão da nota fiscal ou pedido do Protheus, interfere no saldo do pedido no TOTVS Obras e Projetos e neste caso, deve ser utilizada a sua visão de pedidos para filtrar aqueles que foram afetados pela exclusão e acionar o processo “Verificar Eliminação de Resíduos” para que o seu saldo seja atualizado.
