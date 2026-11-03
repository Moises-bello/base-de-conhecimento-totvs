---
content_hash: 59fda4b863ff23e383a86b8c134fa8ccb95b13f3321e95e664f1ed206b297626
fetched_at: '2026-06-29T00:09:12.975223+00:00'
page_id: '419535619'
product: rm
source: tdn-rm
title: Como gerar diferenças de desligamento que não são retificações?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419535619
version: 6
---

# Objetivo:

---

       O objetivo deste documento é trazer informações de como é o processo de diferenças de desligamento que não devem ser tratadas como retificações.

---

Quando há necessidade de pagamento de Remuneração referente a períodos anteriores que deverá ser lançada na competência em que ocorrer quaisquer dos fatos descritos na tabela a seguir (com exceção da situação em que o campo {compAcConv} é informado):

|  |  |  |
| --- | --- | --- |
| **Tipo** | **Descrição** | **Característica** |
| A | Acordo Coletivo de Trabalho | Acordo feito entre sindicato de uma categoria e empresa |
| B | Legislação Federal, Estadual, Municipal ou Distrital | Verbas devidas em decorrência de alguma legislação |
| C | Convenção Coletiva de Trabalho | Acordo feito entre os sindicatos de empregados e o sindicato patronal |
| D | Sentença Normativa (dissídio) | Decisão do TRT ou TST no julgamento de dissidio coletivo |
| E | Conversão de Licença Saúde em Acidente de Trabalho | Processo que converte licença saúde em acidente de trabalho onde será devido o FGTS |
| F | Verbas de natureza salarial ou não salarial devidas após o desligamento | Verbas que legalmente não poderiam ser apuradas na competê[ncia.do](http://ncia.do) pagamento. |

Nos itens A, B, C e D dos casos acima a data de ocorrência dos fatos e a competência em que é devida a obrigação de pagar seus efeitos remuneratórios de Lei, Acordo, Convenção ou Sentença Normativa devem ser informados e a informação está no cadastro de Dados do dissídio.

As datas do cadastro de Dados do dissidio sâo:

* **Data Assinatura (Acordo ou Reajuste por Lei) =** A data de ocorrência do fato conforme tabela acima deve ser informada no campo {dtAcConv}.
* **Data do efeito =** Caso o instrumento normativo tenha efeito remuneratório retroativo, deve ser também preenchido o {dtEfAcConv}, informando a data de início desse efeito.
* **Competência acordada para pagamento =** Se a obrigação de pagar ocorrer em competência posterior à {dtAcConv}, deve ser preenchido o campo {compAcConv}.

Para o tipo E – “Conversão de Licença Saúde em Acidente de Trabalho”, a empresa deverá utilizar uma rubrica informativa correlacionada com o código 9932 da Tabela de Natureza de Rubricas. Então deve ser criado um evento no cadastro de eventos com esta rubrica.

**Observação:** Para o FGTS, a data de vencimento dos tipos A, B, C, D e F é a mesma da competência do evento S-1200, ou seja a data informada no campo período de apuração {perApur}. Já para o tipo E, a data de vencimento é o da competência informada no período anterior, ou seja a data informada no campo período de referência {perRef}.

Só poderão ser informados no tipo “F - Verbas de natureza salarial ou não salarial devidas após o desligamento” parcelas que legalmente não poderiam ser apuradas em competência igual ou anterior ao período de apuração {perApur} informado neste evento. Para os demais casos, deve ser feita a retificação do evento remuneratório correspondente: S-1200, S-1202, S-2299 ou S-2399.

**Exemplo de geração de eventos para Acordo coletivo**

Inserir Dados do dissídio

Alteração do salário foi retroativa a 01/05/2017 estando a competência atual em 09/2017

Funcionário foi demitido em 06/2017

Cálculo da diferença de salário por dissidio referente a 05/2017 – marcado o parâmetro Dissidio Sim

Valores são inseridos em Verbas geradas por diferença no mês de referência do cálculo que é 05/2017

Cálculo da rescisão complementar por dissidio para o cálculo das diferenças referentes a rescisão de 06/2017 – marcado o parâmetro Dissidio Sim

Valores são inseridos em Verbas geradas por diferença no mês de referência do cálculo que é 06/2017

Gerar XML para o período de apuração atual 09/2017, gerando o evento S-1200

Gerar XML para o período de apuração atual 10/2017, gerando o evento S-1210

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |
| 12.1.19 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
