---
content_hash: 0e1665c7dbbac46a6ed5bda649ba026cfde8310be8dc124317d58cdc60abad98
fetched_at: '2026-06-29T00:12:00.695783+00:00'
page_id: '886036783'
product: rm
source: tdn-rm
title: Contrato com Aluguel Complementar em dobro
type: documentation
url: https://tdn.totvs.com/display/LRM/Contrato+com+Aluguel+Complementar+em+dobro
version: 1
---

---

### **Objetivo:**

A funcionalidade de "Criação de Fundo em Dobro Separado para Aluguel Complementar" foi implementada com o objetivo de oferecer mais controle sobre a forma como o fundo promocional em dobro é gerado no sistema de aluguel complementar. A inovação está na forma como o sistema lida com o "fundo em dobro", permitindo que ele seja lançado de maneira agregada ao aluguel ou de forma separada, conforme definido por um parâmetro de integração financeira.

O sistema agora pode verificar se um fundo promocional em dobro deve ser gerado de forma agregada ao aluguel ou separada, conforme definido no cadastro de Fundo Promocional \ Cobrança em Dobro \ Forma de cobrança do aluguel em dobro.  
  
Anteriormente, o fundo em dobro era gerado e somado automaticamente ao valor do aluguel, mas agora, com a implementação desse parâmetro, o sistema permite que esse fundo seja tratado como uma transação financeira separada, ao invés de ser apenas integrado ao valor do aluguel como um desconto ou acréscimo.

### Aplicação e funcionamento:

1. **Verificação do Fundo Promocional em Dobro**: O sistema realiza uma verificação para identificar se há um fundo promocional em dobro aplicável no processo de geração do aluguel complementar.
2. **Definição de Agregação ou Separação**: Com base no cadastro de Fundo em dobro \ Cobrança em dobro, o usuário pode deixar desmarcada a opção (Geração não agregada) para se o fundo promocional em dobro seja agregado ao valor do aluguel (como parte do aluguel complementar) ou gerado como um lançamento separado (marcando a opção Geração não agregada.

   * **Agregado ao Aluguel**: Se o parâmetro de integração não indicar a necessidade de separação, o fundo em dobro será somado ao valor do aluguel.
   * **Gerado Separadamente**: Se o parâmetro de integração financeira for ativado, o fundo será lançado como uma transação financeira separada, não impactando diretamente o valor do aluguel, mas sim gerando um lançamento financeiro distinto.
