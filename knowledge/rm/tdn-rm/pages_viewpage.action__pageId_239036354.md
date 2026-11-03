---
content_hash: c70ad233dfa6ed25d16003d3ad66ef27bb1e1181b845f954134e70139e706686
fetched_at: '2026-06-29T00:08:09.391493+00:00'
page_id: '239036354'
product: rm
source: tdn-rm
title: ER_Geração_Grupo_Pagamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239036354
version: 112
---

# Geração do grupo de pagamentos para o município de Jambeiro - SP

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Fiscal* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Envio de Nota Fiscal Eletrônica de Serviço* | *Envio de Nota Fiscal Eletrônica de Serviço* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Envio de Nota Fiscal Eletrônica de Serviço* | *Envio de Nota Fiscal Eletrônica de Serviço* | |  |  | |
| **Chamados Relacionados** | TTSIN1, TVBFM0 |
| **País(es):** | *Brasil* |

## Descrição

Implementação para geração do grupo de informações de pagamento da Nota Fiscal Eletrônica de Serviço para o município de Jambeiro - SP.

## Procedimento para Configuração do Processo

**CONFIGURAÇÃO DE PARÂMETROS**

             Para que as informações de pagamento sejam geradas é necessário marcar a flag "Utiliza edição de Meios de Pagamento" na etapa Fin - Condições de Pagamento na parametrização do tipo de movimento.

## Procedimento para Utilização

Após marcar o parâmetro citado na etapa anterior, será mostrado a seguinte tela no momento da criação do movimento, em Integrações -> Financeira:

Primeiramente iremos criar os meios de pagamentos "À Vista". "À Prazo", "Cartão de Débito" e "Cartão de Crédito", irei citar separadamente como criar cada um dos meios de pagamento, cadastro disponível em: Cadastros -> Estoque, Compras e Faturamento -> botão "Mais" -> Tabelas Auxiliares -> Meio Pagamento.

1. **À Vista:**  
      Para criar uma meio de pagamento do tipo à vista, este meio de pagamento não pode ter como tipo primitivo Cartão, Cartão de Débito ou Parcelado. As outras formas de pagamento serão consideradas a vista. Irei exemplificar com o tipo de pagamento Dinheiro:

            2. **À Prazo:**  
                  Para criar uma meio de pagamento do tipo à prazo, marque o tipo primitivo "Parcelado". Para que seja do tipo a prazo é necessário que a data de vencimento do pagamento seja maior que da data de emissão do movimento.

 

3. **Cartão de Débito:**

O cartão de debito pode ser parametrizado de 2 formas:

1ª Forma: Marque o tipo primitivo como Cartão. na aba Cartão de credito/debito marque a opção debito no tipo de transação.

2ª Forma: A outra forma de gerar o cartão de debito é simplesmente marcar o tipo primitivo como Cartão de debito.

4. **Cartão de Crédito**

Marque o tipo primitivo como Cartão. Na aba Cartão de credito/debito marque a opção credito no tipo de transação.

 

Terminado este Cadastro, voltamos para o movimento para a aba Integrações -> Financeira:

Utilize o meio de pagamento que deseja, informe o valor e a data de vencimento.

Exemplo de como deve ser feito o parcelamento. No meu exemplo estou parcelando em 3x no Cartão de Crédito, seus valores totalizados é equivalente ao valor do movimento:

O sistema também permitirá pagamentos mistos, por exemplo pagar um parte no Cartão de Débito e o restante no Cartão de Crédito.

Foi inserido uma linha para cada tipo de meio de pagamento, seus valores totalizados é equivalente ao valor do movimento.

Mostrarei como ficará o grupo novo no XML:

Primeiramente o exemplo do parcelado no cartão de crédito em 3x:

Foi criado um grupo apenas de condição de pagamento do tipo cartao de credito contendo 3 parcelas, informando o numero da parcela, valor e data de vencimento.

<CondicaoPagamento>  
      <Condicao>CARTAO\_CREDITO</Condicao>  
      <QtdParcela>3</QtdParcela>  
      <Parcelas>  
            <Parcela>1</Parcela>  
            <DataVencimento>15/06/2016</DataVencimento>  
             <Valor>10.00</Valor>  
      </Parcelas>  
      <Parcelas>  
             <Parcela>2</Parcela>  
             <DataVencimento>15/07/2016</DataVencimento>  
             <Valor>10.00</Valor>  
      </Parcelas>  
      <Parcelas>  
             <Parcela>3</Parcela>  
             <DataVencimento>15/08/2016</DataVencimento>  
             <Valor>10.00</Valor>  
      </Parcelas>  
 </CondicaoPagamento>

No exemplo do pagamento Misto o XML será montado da seguinte forma:

Foram criados 2 grupos de condição de pagamento, um para o pagamento com cartão de débito e outro para o pagamento com o cartão de crédito.

<CondicaoPagamento>  
      <Condicao>CARTAO\_DEBITO</Condicao>  
      <QtdParcela>1</QtdParcela>  
      <Parcelas>  
             <Parcela>1</Parcela>  
             <DataVencimento>15/06/2016</DataVencimento>  
             <Valor>15.00</Valor>  
      </Parcelas>  
 </CondicaoPagamento>  
 <CondicaoPagamento>  
      <Condicao>CARTAO\_CREDITO</Condicao>  
      <QtdParcela>1</QtdParcela>  
      <Parcelas>  
             <Parcela>1</Parcela>  
             <DataVencimento>15/06/2016</DataVencimento>  
             <Valor>15.00</Valor>  
      </Parcelas>  
 </CondicaoPagamento>

divs
