---
content_hash: 5af23caeeba1ebe66562029967cd0acfdff350e7b7570ccc5218108fbff57567
fetched_at: '2026-06-29T00:11:26.816290+00:00'
page_id: '720357997'
product: rm
source: tdn-rm
title: TPI - Base para criar conta caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/TPI+-+Base+para+criar+conta+caixa
version: 17
---

**CONTA CAIXA TRANSITÓRIA**

A parametrização do recebimento via TOTVS Pagamento Instantâneo utiliza uma conta caixa para simular a conta transitória que é responsável pelo recebimento e repasse dos valores referente as transações aprovadas.

No processo de recebimento com PIX, os valores são depositados na conta transitória são repassados em janelas horarias durante o dia para a conta banco da instituição, por este motivo é necessário a criação de uma conta caixa sem integração bancaria no TOTVS Gestão Financeira.

**IMPORTANTE**

Caso utilize a contabilização na baixa do lançamento, recomendamos que a baixa seja efetuada na conta contábil vinculada à conta caixa transitória, assim ao realizar a conciliação do extrato, a transferência do valor referente ao pagamento será contabilizada para a conta banco da instituição finalizando o processo da contabilização..

Uma boa prática seria a criação de contas contábeis específicas para a conta caixa transitória que será utilizada na contabilização da taxa e no repasse para a conta banco da instituição ao concluir do processo de conciliação.

**IMPORTANT**E

Ressaltamos que este exemplo não contempla as particularidades de cada instituição e por isso, não recomendamos a cópia fiel para o sistema. Se necessário, solicite auxilio de sua consultoria contábil para adicionar as necessidades legais de sua instituição.

**Inclusão da Conta caixa**

***BackOffice > Gestão Financeira > Movimentações bancarias > Contas/Caixa***

Clique no botão novo para criação da Conta Caixa transitória

Após inserir o código e descrição, salvar o cadastro da conta caixa e acesse a aba Integração Bancária.

Por se tratar de uma conta transitória e não existir dados de banco, agencia e conta, não é necessário inserir as os dados, podem manter os campos em branco.

Existindo integração Educacional X Protheus os campos precisam ser informados com dados fictícios, pois são informações obrigatórias para a funcionamento da integração.

Acesse a Aba Contabilidade e clicar no botão de Defaults.

No botão Defaults informar a conta contábil default de Débito e Crédito.

Após inserir as contas contábeis de Crédito e Débito salvar o cadastro, efetivar a criação da conta caixa utilizada na parametrização.
