---
content_hash: 78358d49a3afb1723b697d304c89dee572b865f1415d3bf8b87791c1269399aa
fetched_at: '2026-06-29T00:11:37.986237+00:00'
page_id: '780787770'
product: rm
source: tdn-rm
title: TCGI - Gerar Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=780787770
version: 10
---

**Cobrança Gerar Cobrança**

O processo de cobrança percorre a base de dados em busca de lançamentos vencidos, que não estejam bloqueados por distrato ou aditivos e que não sejam parcelas da MVMC (Minhas Casa Minha Vida). As parcelas com Status diferente de baixado ou parcialmente quitado e com status de bloqueio diferente de livre, não serão consideradas para a geração de cobrança.

Ao identificar os registros em atraso será feito a criação de uma nova cobrança para o cliente/fornecedor, essa cobrança é criada por contrato e origem(Venda ou Aluguel), caso já exista uma cobrança para o contrato e for identificado um novo lançamento em atraso essa cobrança é atualizada. O cliente/fornecedor pode possuir mais de uma cobrança, caso ele possua lançamentos em contratos distintos.

Quando todos os lançamentos da cobrança são quitados ou renegociados caso exista um atendimento em aberto para essa cobrança o mesmo é encerrado automaticamente quando o processo de Gerar Cobrança for executado. Neste momento o Status da cobrança é alterado para concluída e mesma é desassociada na carteira, em caso de futuros atraso o processo de Gerar Cobrança irá reabrir a cobrança inserindo a mesma em uma carteira respeitando os filtros estabelecidos no cadastro de Carteira de Cobrança.

Importante!

Feriado em Vencimento de Parcela.

Para realizar as Ações de Cobrança, o sistema utiliza o Calendário associado à [Filial](https://tdn.totvs.com/pages/viewpage.action?pageId=422545738#1--401241980) para validar se o vencimento das parcelas é um dia útil ou não.

Caso não haja nenhum calendário associado à Filial, o sistema buscará o calendário associado ao [Parâmetro do Financeiro](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar).

Se a Data do Vencimento de um lançamento ocorrer em um feriado, ou um dia não útil (sábado ou domingo, por exemplo), este lançamento somente será considerado em atraso para fins de cobrança, após o primeiro dia útil posterior à esta data.

Exemplo:  
Caso a parcela ou o boleto tenha o vencimento no sábado ou domingo, o sistema de Cobrança considera que esse dia do vencimento foi deslocado para a segunda-feira, assim, caso o cliente não pague esta parcela, a Ação de Cobrança para a mesma será executada apenas na terça-feira, que é quando ela estará em atraso, em relação ao calendário utilizado.

Exemplo Prático:

Uma parcela tem o seu vencimento no dia 05/08/2023, sábado;

Dessa forma, o vencimento desta parcela será deslocado para o próximo dia útil, dia 07/08/2023, segunda-feira;

Caso o cliente não quite esta parcela nesta data, no dia subsequente à data acima, terça-feira, dia 08/08/2023, esta parcela estará com 3 dias de atraso.

Com a Régua de Cobrança configurada com as duas  Ações de Régua de Cobrança abaixo:

* + Ação 1: 1 Dia de Atraso, enviar email; e
  + Ação 2:  3 Dias de Atraso, enviar email.

Considerando o cenário acima, no dia 08/08/2023 o sistema executará estas duas ações no processo de Gerar Cobrança. Ou seja disparará 2 emails para o Cliente desta parcela:

* + Um com 1 dia de atraso; e
  + Outro com 3 dias de atraso.

Salientando que, em nosso exemplo, utilizamos o envio de emails, mas as Ações da Régua de Cobrança pode ser:

* + **[Envio de E-mail](https://tdn.totvs.com/display/LRM/TCGI+-+Envio+de+E-mail)**
  + **[WhatsApp](https://tdn.totvs.com/display/LRM/TCGI+-+WhatsApp)**
  + **[Envio de SMS](https://tdn.totvs.com/display/LRM/TCGI+-+Envio+de+SMS)**
  + **[Abertura de Atendimento de Cobrança para contato com Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=780781177)**
Novidades!

A partir do Patch Específico Patch12.1.2310.203, ao término da execução do processo Gerar Cobrança, o TCGI exibe no Job desta execução, a aba Log\_Detalhe, com as vendas e suas respectivas parcelas que foram incluídas nas novas cobranças.

Mais sobre Gerar Cobrança!

**Gerar cobrança é o coração do processo de Cobrança - Faz tudo!**

* Cria as cobranças em atraso
* Finalizar cobrança
* Abrir atendimento
* Enviar E-mail
* Enviar SMS
* Associa a Carteira

## **Quando é o momento de Rodar o Gerar Cobrança** ? Sempre após o Retorno Bancário.

Exemplo , se um retorno bancário todo dia é executado todo dia 8 horas da manhã , por poder ocorrer um atraso , Agenda  para rodar em 3 camadas todos os dias o processo de Gerar cobrança automaticamente , caso o cliente não tenha efetuado o pagamento , a cobrança seria realizada para o mesmo , ou via Atendimento , SMS ou E-mail.

**Como configurar ambiente 3 camadas** : [Clique aqui !](https://tdn.totvs.com/pages/viewpage.action?pageId=273982231#:~:text=Configura%C3%A7%C3%A3o%20Ambiente%203%20Camadas&text=xx%20basta%20selecionar%20o%20tipo,Exemplo%3A%20ou%20a%20mais%20recente.)

Observação sobre campo: IDCARTEIRA

**Observação importante sobre o campo IDCARTEIRA, uma vez que esse campo  foi preenchido, o sistema não irá alterá-lo em relação aos Filtros da Visão da Carteira, mesmo que o processo de Gerar Cobrança seja executado novamente, o campo IDCARTEIRA irá se manter inalterado. Esse processo de Geração de Cobrança não altera as informações do Campo IDCARTEIRA, da Tabela XCOBRANCA dinamicamente a cada execução do Processo.**
