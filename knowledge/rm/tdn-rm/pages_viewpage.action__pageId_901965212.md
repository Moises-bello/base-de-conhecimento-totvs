---
content_hash: f327192d1f8549d7b051d2c11584f594c7ee826822ba33ddb2ec81b2f51f87ca
fetched_at: '2026-06-29T00:12:02.639516+00:00'
page_id: '901965212'
product: rm
source: tdn-rm
title: 1- Parametrização  TOTVS Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901965212
version: 19
---

Parametrização do TOTVS Gestão Financeira para utilização do TOTVS Pagamento com Cartão, no Portal do Aluno, Meu EduCONNECT, Taxa de Inscrição do Processo Seletivo, baixa automática dos lançamentos e criação do extrato de caixa.

Neste passo vamos informar os dados de acesso ao TOTVS Pagamento com Cartão, para isso acessar:

**Ambiente | Parâmetros | TOTVS Gestão Financeira**

Após avançar o processo selecionar:

****Contas a Receber | Baixas | Cartão de Credito/Débito****

Avance o processo e informe o usuário que será responsável pela baixa do lançamento financeiro

O usuário precisa ter permissão para realizar baixas lançamentos.

Após inserir o usuário responsável pela baixa, avance o processo e em **Configurações de E-commerce** selecione os parâmetros abaixo e avance o processo.

Modelo de E-commerce: **CyberSource**  
Ambiente Ativo: **Produção**  
Merchant Id: **Informe a chave enviada por e-mail**

Nº máximo de parcelas: O campo define o numero máximo de parcelas independente do serviço vinculado ao contrato do aluno. Caso seja necessário o controle pode ser definido no cadastro dos serviços no Educacional.  
Key Id: Informe a chave enviada por e-mail

Shared Secret Key: **Informe a chave enviada por e-mail**

Tipo de adquirente: Selecione a opção contratada podendo ser REDE, GETNET ou CIELO  
Modulo de Antifraude: **TOTVS Gestão Educacional**

Na **Baixa** informe a conta caixa transitória e o meio de pagamento.

Para criação da conta caixa transitória clique em ...

Clique no +

Informe os dados para a criação da conta caixa transitória, o campo código é obrigatório e pode seguir a sequencia das contas caixas já criadas na instituição.

Após a criação selecione a conta e clique em Ok

Após a seleção da conta caixa será necessário selecionar o meio de pagamento, para criação siga os passos abaixo.

Clique em ...

Informe o Código, Descrição, Tipo Primitivo Credito

Na guia Outros Dados, marque o parâmetro Credito no Tipo de Transação e clique em Ok.

Podemos criar um meio de pagamento Genérico "Cartão de credito" ou criar um para cada bandeira a decisão é de responsabilidade da instituição.

Após criar o meio de pagamento ou os meios de pagamento informar os dados para cada bandeira, em nosso exemplo informamos somente para a bandeira visa, o mesmo procedimento precisa ser realizado para todas as bandeiras.

Em Conciliação marque o parâmetro Novo modelo de previsão de recebimento com cartão

Como a baixa ocorre primeiro na conta caixa transitória, criada nos passos anteriores, será necessário informar a conta caixa recebimento, que pode ser uma conta padrão para todas as bandeiras, ou uma conta individual por bandeira.

Ou podemos informar contas individuais para cada bandeira, neste exemplo vamos demonstrar para a bandeira visa, e o procedimento precisa ser replicado para todas as outras bandeiras.

O Evento Contábil é obrigatório, para instituições com o Modulo contábil implementado e que o extrato de caixa seja do tipo contábil.

O link abaixo contem a documentação para auxiliar na criação do evento contábil do tipo extrato de caixa, lembrando que é uma base para criação e que precisa ser adaptado para a regra contábil definida pela instituição, a criação é de responsabilidade da instituição e caso seja necessário a TOTVS disponibiliza o time de consultoria tarifada para a criação do evento.

[TOTVS Pagamento Cartão - Base para criar evento contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=662420204)

Informe o diretório de leitura do arquivo, o diretório precisa estar compartilhado na rede interna com permissão de leitura e escrita para o usuário de execução do host.

Na Guia Cyber Source - Skyline informe o usuário e senha enviado por e-mail, o campo URL é padrão <https://secure1.nexxera.com/nexxeraws/v2/SkylineWSv2>

No exemplo acima, realizamos a configuração por coligada, que também pode ser realizada por filial, caso a seja a necessidade da instituição

Para configuração por Filial, clique em **Configuração por Filial** e em **+**

Selecione a filial a ser parametrizada e informe os dados e chaves enviados por e-mail.

O Preenchimento dos dados são os mesmos dos passos por coligada, alterando somente as chaves enviadas por e-mail que precisam ser geradas por filial, procedimento de geração de chaves de integração para credenciamento informados no KickOff.

Cadastre as taxas para geração do extrato de caixa  para isso acesse:

**Movimentações bancarias | Cartão de Credito/Débito | Mais | Taxa de cartão**

Para criar um filtro clique em **Novo**

Selecione a opção **Indentificador**e operador **IS NOT NULL**

Clique em adicionar depois salvar.

Clique em executar

Para o cadastro das taxas clique na opção **+**

As taxas podem ser cadastradas por filial caso existam diferença de valores de tarifas acordadas com a adquirente, para isso selecione a filial desejada.

Não existindo o campo filial pode ficar vazio.

Selecione a adquirente, em nosso exemplo vamos selecionar a Rede.

Selecione o Tipo de venda, em nosso exemplo vamos selecionar Credito à vista

Selecione a Bandeira, em nosso exemplo vamos selecionar a Visa

Informe a Taxa para a opção de credito a vista (Rotativo)

Clique em Salvar

Vamos cadastrar uma Taxa para o credito parcelado, vamos manter o exemplo com a bandeira VISA e os parâmetros até a adquirente são os mesmos, alterando somente na opção Tipo de Venda.

Selecione a opção Tipo de venda, Credito parcelado

Vamos manter a bandeira visa

Informe o valor da Taxa para o credito parcelado

Marque o parâmetro Faixa de parcelas e em nosso exemplo vamos definir a taxa para o parcelamento de 2 a 6 parcelas

Clique em Salvar

Todas as taxas passadas pela adquirente precisam ser cadastradas para todas as bandeiras.

Finalizamos a Parametrização no TOTVS Gestão Financeira e o cadastro de taxas.
