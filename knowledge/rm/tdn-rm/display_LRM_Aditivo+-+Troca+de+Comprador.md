---
content_hash: 0033c90fa7a229594d462d9518bbdae2afac34bf6d32e0b2d23c0b8e7711c430
fetched_at: '2026-06-29T00:09:48.429428+00:00'
page_id: '435105151'
product: rm
source: tdn-rm
title: Aditivo - Troca de Comprador
type: documentation
url: https://tdn.totvs.com/display/LRM/Aditivo+-+Troca+de+Comprador
version: 14
---

Esta funcionalidade não só permite alterar o(s) cliente(s) da venda para o(s) novo(s) cliente(s) escolhido(s), como também permite editar o seu percentual de participação e o seu papel como comprador Principal ou secundário, conforme a necessidade da incorporadora.

Melhoria no Histórico de Compradores!

Não é possível desfazer aditivo de troca de comprador em duas situações:

1. Aditivos que estejam na **versão 4.0;**
2. Quando existir uma parcela com baixa parcial que foi finalizada na **versão 5.0** e o sistema não consegue desfazer essa situação, pois não temos a rastreabilidade e nem a foto das parcelas afetadas. Favor refazer a troca para o comprador antigo.
3. A partir da **versão 2602**, não será possível desfazer aditivo que estejam **na versão anterior 6.0**, pois foi feito o tratamento de aditivos com a baixa parcial nessa versão e a troca de compradores agora você seleciona as parcelas que irão ser trocadas, não mais a regra (série de pagamento). Com isso teremos a foto das parcelas antes da troca, melhorando a usabilidade do sistema e da ficha financeira.

A partir da **versão 5.0** do Aditivo de Troca de Compradores, o sistema grava uma nova linha para as inclusões e alterações realizadas na Troca de Compradores, garantindo assim, um histórico fidedigno dos compradores, seus papéis e sua participação ao longo da existência da venda.

Ao selecionar este tipo de Aditivo, será apresentado todos os compradores ativos cadastrados da Venda, para manipulação. Nessa tela podemos Incluir , Editar e Excluir os compradores.

Importante!

Não cancele o Processo ***Sincronizar parcelas do aditivo com a venda***, pois o mesmo é essencial para a correta parametrização do Aditivo.

Caso esta ação seja executada, o sistema retornará à tela inicial do Aditivo e será necessário refazer toda a parametrização, até que o processo acima seja executado em sua completude.

Caso a Integração com a [Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=729222653) esteja parametrizada, verifique as **[Premissas](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora)** em relação à este tipo de Aditivo, para se executar o Processo [Integrar com Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora).

**Observação:**

Ao realizar o Aditivo de Troca de Compradores, se na venda existir parcelas baixadas parcialmente, o sistema gera um novo grupo de aditivo no financiamento com o saldo restante destas parcelas para o novo comprador, atualizando a data do reajuste nas novas parcelas.

Ao incluir ou editar um comprador será exibida uma tela, contendo os seguintes campos:

**Comprador principal:** Esse campo quando marcado, determina que o comprador é o principal do Contrato. Dessa forma as parcelas serão geradas em seu nome.   
**Situação operacional**: Esse campo exibe a situação do comprador, que pode ser:

* **Inclusão:** Ao incluir um novo comprador, esse campo é exibido automaticamente;
* **Corrente:** Ao editar um comprador já existente na venda, esse campo é exibido automaticamente;
* **Exclusão:** Ao excluir um comprador já existente na venda, esse campos é exibido automaticamente;

**Versão 5 e anteriores até a release 2510**

**Comprador:** Nesse campo é possível definir qual o Cliente/Fornecedor será o comprador;    
**Transferir comprador**: Esse campo permite definir como será a transferência das parcelas para o novo comprador, possui as seguintes opções:

* **Para todas as parcelas em aberto da(s) série(s) selecionadas(s):** Ao selecionar essa opção, será realizado a transferência de comprador para todas as parcelas em aberto das séries de pagamento selecionadas no aditivo;
* **Para a(s) parcela(s) da(s) série(s) selecionadas(s) com vencimento igual ou maior a data de transferência:** Ao selecionar essa opção, será realizado a transferência de comprador para todas as parcelas com vencimento igual ou maior a data de transferência informada pelo usuário, nas séries de pagamentos selecionadas;

**Data de transferência:** Determina de qual data a transferência de comprador será realizada, caso selecionada essa opção no campo anterior;    
**Aplicar:** Esse botão tem como função aplicar a transferência de comprador parametrizada pelo usuário;   
**Limpar:** Esse botão tem como função limpar as alterações de transferência de comprador realizadas pelo usuário;   
**Série de pagamentos:** Nessa tela é possível visualizar as séries de pagamento da venda, assim como o compradores responsáveis;

**Observação:** O sistema permite a efetivação de Aditivo de Troca de Comprador para contrato de venda em situação Quitada, sem que seja necessário alterar a situação do mesmo. Esta ação é permitida, caso a incorporadora necessite manter algum histórico em relação aos compradores. Seja para fins de cobrança de impostos ou serviços, seja para fins de atendimento, ou qualquer outro tipo de controle, que se fizer necessário.

**Versão 6 e superior a release 2510**

**Comprador:** Nesse campo é possível definir qual o Cliente/Fornecedor será o comprador;    
**Transferir comprador**: Esse campo permite definir como será a transferência das parcelas para o novo comprador, possui as seguintes opções:

* **Para todas as parcelas em aberto selecionadas(s):** Ao selecionar essa opção, será realizado a transferência de comprador para todas as parcelas em aberto das séries de pagamento selecionadas no aditivo;
* **Para a(s) parcela(s) da(s) série(s) selecionadas(s) com vencimento igual ou maior a data do aditivo:** Ao selecionar essa opção, será realizado a transferência de comprador para todas as parcelas com vencimento igual ou maior a data de transferência informada pelo usuário, nas séries de pagamentos selecionadas;

**Transferir:** Esse botão tem como função aplicar a transferência de comprador parametrizada pelo usuário;   
**Limpar:** Esse botão tem como função limpar as alterações de transferência de comprador realizadas pelo usuário;   
**Parcelas de pagamentos:** Nessa tela é possível visualizar todas as parcelas em aberto da venda, assim como o compradores responsáveis;

Veja Também

---
