---
content_hash: e42e12da12259831f23c426aa27526a709649e0a2c7fb41afc3fa67fdd6ea8d9
fetched_at: '2026-06-29T00:11:33.424540+00:00'
page_id: '759938709'
product: rm
source: tdn-rm
title: 11 - Processo de Conciliação Pontual - Considerando a data da Liquidação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=759938709
version: 9
---

O Processo Importação do Arquivo de Conciliação é responsável por realizar a transferência da conta caixa transitória para a conta caixa banco da instituição. Os arquivos de conciliação são disponibilizados de segunda a sexta-feira.

As transações realizadas e aprovadas são disponibilizadas na API de conciliação no próximo dia útil, assim todas as transações realizadas hoje estarão disponíveis no arquivo de conciliação no próximo dia util.

Eventualmente podem ocorrer inconsistências nos dados da API e alguma transação pode não ser conciliada no extrato de caixa. Então precisaremos localizar no **Payment Core** - **RaaS** a transação que não foi conciliada e verificar a data da liquidação.

Acessar o **Payment Core** - **RAAS**,

Para ajudar na busca, recomendamos clicar na engrenagem apontada na seta e marcar a exibição da coluna Data de Liquidação, que corresponde efetivamente a data que ocorreu a transferência dos valores da conta transitória para a conta banco da instituição.

Importante observar que somente transações com status do pagamento **Aprovado** e status de liquidação **Liquidada** tem o campo data de liquidação informado.

Após identificar a data da liquidação acessar: **BackOffice | Gestão Financeira**

**Contas a Pagar/Receber | Transações**

Localizar a transação que não foi conciliada, neste exemplo criamos um filtro buscando o campo TID

O Status da transação precisa ser **Pagamento Concluído**e em anexos Histórico de Transações deve estar como Baixa do boleto/Lançamento efetuada

Após a baixa do lançamento, através do Processo **Ajuste de Transações**, no extrato de caixa serão criadas duas movimentações, Deposito na Baixa e Saque manual.

Acessar **Movimentações Bancarias | Extrato de Caixa**

Criamos um filtro buscando o campo TID para listar os extratos de caixa da transação não conciliada

No exemplo abaixo, mesmo após o processo de conciliação ter sido executado, não criou as outras duas movimentações de **Saque Transferência** e **Deposito Transferência**

Neste caso recomendamos que seja executado o Processo de Importação do Arquivo de Conciliação pontualmente considerando a data de Liquidação da transação.

Acessar: **Movimentações Bancarias | Conciliação** fechar a janela do filtro exibida

Acessar: **Processos | Importação do Arquivo de Conciliação**

Na próxima tela Informar a data inicial e final (Recomendamos a data inicial 90 dias a antes da data final hoje) o parâmetro **Considerar data de liquidação** precisa estar marcado,  informar a data de liquidação listada no **Payment Core**

O processo foi concluído com ressalvas, pois já existiam transações conciliadas anteriormente. Não se preocupe.

Acessar o extrato de caixa e verificar se as movimentações **Saque Transferência** e **Deposito Transferência** foram criadas após o reprocessamento da importação do arquivo de conciliação.
