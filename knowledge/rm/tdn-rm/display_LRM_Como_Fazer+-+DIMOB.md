---
content_hash: eb4813b24c2e735d49d40e2a2c317e5075c86517009a45d69c9d746e51b14477
fetched_at: '2026-06-29T00:08:27.182204+00:00'
page_id: '271396180'
product: rm
source: tdn-rm
title: Como_Fazer - DIMOB
type: documentation
url: https://tdn.totvs.com/display/LRM/Como_Fazer+-+DIMOB
version: 3
---

| Produto: TOTVS Incorporação | Versão: 12.1.13 e 12.1.14 |
| --- | --- |
| **Processo de Negócio:** | **DIMOB** |

**Introdução:**

Esse Documento irá auxiliar o usuário a realizar o processo da Geração da DIMOB.

A DIMOB (Declaração de Informações sobre Atividades Imobiliárias) é uma Instrução Normativa da Receita Federal que obriga as empresas imobiliárias, construtoras e incorporadores a informar à Receita detalhes de todas as transações imobiliárias, inclusive locação. Na declaração, deve constar a identificação dos contratantes e do imóvel, data, valor da operação e comissão cobrada.

**Como Fazer:**

Para gerarmos a DIMOB, devemos acessar o Menu/Relatórios/DIMOB, e abrirmos a visão, conforme abaixo:

Na visão da DIMOB, o sistema irá trará a seguinte tela, no qual o usuário poderá escolher a coligada na qual deseja gerar o arquivo:

**Na tela seguinte, o usuário irá parametrizar as informações que deseja enviar para a DIMOB.**

**Caminho:**O Diretório onde o sistema irá SALVAR o arquivo gerado.

**Opções de Agrupamento**: Sem nenhuma opção marcada, será gerado somente um arquivo, contendo os dados de todos os empreendimentos no mesmo arquivo.

**Gerar um arquivo por empreendimento****-** Se marcado será criado um arquivo para cada empreendimento.

**Gerar um arquivo por parceiro de acordo com o repasse**– Se marcado será criado um arquivo para cada repasse de cada empreendimento.  
 (Definimos como parceira(o) a empresa que tem algum percentual de participação no recebimento dos valores do empreendimento.   
Para cadastrar um repasse em um empreendimento o processo é o seguinte: Aba Cadastros | Manutenção de Empreendimentos | Empreendimento | Anexos | Dados de Repasse do Empreendimento | [Incluir], aonde pode ser informado o Cliente/Fornecedor e o Percentual de Participação.).

**O comportamento da DIMOB depende do modelo de repasse definido no contrato de administração:**

* Para contratos que tenha o repasse do tipo “Garantido” será considerado que encargos moratórios (juros e multa) e desconto são da administradora não sendo repassados ao(s) proprietário(s).
* Para contratos do tipo “Condicional”, será sempre considerado o valor dos respectivos campos para o cálculo dos encargos moratórios (juros e multa) e desconto na DIMOB.

**Ano Calendário:** Informe o ano de qual serão extraídas as Atividades Imobiliárias.

**CPF Responsável:** O Usuário irá informar o CPF do responsável pela geração**.**

**Declaração Retificadora:** Caso seja necessário retificar o usuário deverá informar o número do recibo da declaração enviada anteriormente.

**Valor Total da Operação:**É definido qual valor será considerado na geração do arquivo (Valor da Venda ou Valor do Financiamento).

**Situação Especial**:Nos casos de extinção, fusão, incorporação e cisão total da pessoa jurídica, a declaração de Situação Especial deve ser apresentada até o último dia útil do mês subsequente à ocorrência do evento.

**Tabela de Classificação do Município:**Neste campo deverá ser informado o identificador da classificação informada no cadastro de municípios.

**Após parametrizar as informações a serem enviadas clique em Avançar> Executar:**

No final da geração do arquivo será gerado um log informando se ocorreu algum erro no processo.

Fonte:
