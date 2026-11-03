---
content_hash: 7ef832110b9055b6e66b110897476db413074828e6a06dea16317d17676fe5b3
fetched_at: '2026-06-29T00:11:43.994104+00:00'
page_id: '808011489'
product: rm
source: tdn-rm
title: Recebimento/Estorno com o TEF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808011489
version: 11
---

Descontinuação do Módulo de Caixa 1.0

A partir da release 12.1.2510, o **Módulo de Caixa 1.0** será descontinuado e deixará de estar disponível no TOTVS Gestão Financeira.

A partir dessa versão, a solução oficial e suportada pela TOTVS para os processos de recebimento via Sessão de Caixa será exclusivamente o **Módulo de Caixa 2.0**, já disponível e que oferece mais recursos, melhor performance e maior aderência às boas práticas de mercado.

Recomendamos que as empresas realizem a migração para o **Módulo de Caixa 2.0** o quanto antes, garantindo continuidade operacional, suporte técnico e acesso às inovações da solução.

Para mais informações sobre a nova funcionalidade, consulte a [documentação nesse link](https://tdn.totvs.com/pages/viewpage.action?pageId=744486517).

Ao ativar a Sessão de caixa, é realizada a comunicação do SiTef integrando com o PinPad, verificando se o PinPad está conectado. Caso não tenha falha na comunicação, a sessão de caixa será ativada normalmente, caso contrário, o sistema retornará uma mensagem para o usuário informando que não há um PinPad conectado.

Na baixa do lançamento informando o meio de pagamento Cartão do tipo Crédito, será habilitado a opção para parcelamento, de acordo com o que foi definido nos parâmetros 'Número máximo de parcelas' e 'Valor mínimo por parcela'. 

**Observação:**

Para correto parcelamento, deve parametrizar o sistema com a quantidade de parcelas contratadas pelo usuário na operadora. Caso exista diferença de centavos entre o total da transação e o somatório das parcelas, o valor será somado na primeira parcela.

Quando selecionado o pagamento do tipo Cartão de Débito durante a baixa de lançamentos, a opção de parcelamento não será habilitada.

As transações de pagamento com cartão Crédito/Débito, será iniciada na tela de 'Conclusão de assistente de baixa' ao clicar sobre o botão "Executar" na tela, iniciando o serviço do SiTef de pagamento com cartão.

Iniciada a transação, são enviadas informações referentes ao pagamento, exibindo as mensagens retornadas pelo SiTef para o operador do caixa, e visualizadas na tela de comunicação com o PinPad.

Na conclusão da transação de cartão, o processo de baixa será finalizado, efetivando os pagamentos realizados com cartão.   
  
  
  
Ao fim da baixa o sistema armazena os seguintes campos referente ao SiTef:

* Identificador de transação (TID);
* Bandeira do cartão;
* Data e hora da transação;
* Status da transação;
* Código do estabelecimento;
* Meio de pagamento;
* Número de parcelas do pagamento;
* Código da coligada;
* Modelo Transação;
* NSU do SiTef;
* NSU adquirente;
* Código da rede autorizada;
* Código autorização emissor de cartão.

Esses dados das transações serão armazenados no sistema para futura conciliação, na tabela FINTEGRACAOCARTAO e FINTEGRACAOXCX.

Caso ocorra algum erro no processo de baixa do lançamento financeiro, o pagamento será efetivado junto a operadora e o lançamento financeiro ficará com o campo BAIXAPENDENTE igual a 'Pendente Sitef' até que a ocorrência exibida no log do histórico da transação seja resolvida - em Movimentações Bancárias > Cartão de Crédito/ Débito - Transações > anexo Histórico de transações. Ao corrigir o problema que impediu a baixa do lançamento, será necessário executar o processo "Ajustar Transação", localizado no menu Movimentações Bancárias > Cartão de Crédito/ Débito - Transações > Processos > Ajustar transação, para que a baixa seja realizada com sucesso e o status da transação relacionada atualize de "Pagamento confirmado" para "Pagamento Concluído". Vale ressaltar que, considerando que o ambiente esteja configurado em N camadas, o processo de ajuste de transação pode ser agendado, evitando a intervenção do usuário para tal.

**Observações:**

* No processo de baixa com transação com SiTef, caso o parâmetro "Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa" estiver marcado, o mesmo deverá ser desconsiderado.
* Os comprovantes da transação serão impressos após o processo, e após a autenticação mecânica caso esteja parametrizado, também poderão ser reimpressos pela visão da Sessão de Caixa no botão '2° Via do Cupom TEF'. Se o parâmetro Saída de Impressão seja "Impressora Windows", no momento da impressão dos comprovantes, o operador deve selecionar a impressora que deseja imprimir. Caso contrário, se o parâmetro Saída de Impressão seja "Impressora Windows" e o parâmetro "Utilizar impressora Padrão" estiver selecionado, os comprovantes serão impressos na impressora padrão configurada no terminal.
* Nos lançamentos bloqueados por "Pendente Sitef", no processo de alteração, serão permitidos modificar os campos Departamento, Centro de Custo, Tabelas Opcionais, Data de Competência, Rateio por centro de custo, Rateio por departamento e Campos complementares.

**Cancelamento de Baixa com Sitef**

O processo de cancelamento é iniciado na etapa "Concluindo o assistente de Cancelamento de Baixa de Lançamentos", clicando no botão "Executar", onde a transação do SiTef para cancelamento será iniciada. Será solicitado pelo SiTef a inserção do cartão no PinPad para o cancelamento. 

No cancelamento da baixa de lançamentos realizadas pelo SiTef, caso o parâmetro "Liberar estorno com senha do supervisor" estiver marcado e a permissão para usuário "Liberar estorno transação SiTef" estiver sem permissão de acesso, será solicitado a senha do usuário supervisor ou usuário com permissão.

O processo de estorno gera três históricos na transação correspondente: Cancelamento Solicitado → Cancelamento Pendente → Pagamento Cancelado. Como o estorno no sistema SiTef é feito de forma desacoplada do módulo de caixa, o processo pode realizar somente parte do todo, ou seja, a transação fica com um dos dois primeiros status. Há dois cenários possíveis:

* Lançamento tem o campo Baixa Pendente como "Sitef" e transação com status "Cancelamento Pendente": nesse caso, é possível sincronizar o status pelo processo de ajuste de transações, onde o sistema efetivará o cancelamento da baixa do(s) lançamento(s);
* Lançamento tem o campo Baixa Pendente como "Livre" e transação com status "Cancelamento Solicitado": para esse cenário, poderá ser realizado uma nova tentativa de estorno através da sessão de caixa.

**Cancelamento de Baixa antes do Estorno de Transação Sitef**

Na tela de cancelamento de baixa, antes da chamada do Sitef ocorre a validação do cancelamento de baixa, onde é verificado se o cancelamento de operação no Sitef e da baixa podem ser executados, de forma a impedir que a operação seja feita em somente um dos lados.

É verificado se os itens de baixa selecionados para cancelar podem ser executados no que diz respeito ao histórico de alteração de lançamentos que, quando habilitado, exige que os itens sejam cancelados do mais recente para o mais antigo. Será apresentada mensagem ao operador caso o cancelamento no sistema não possa ser executado e o cancelamento no SITEF não é chamado.

**Cancelamento de transação Sitef com cancelamento solicitado ou pendente e baixa não realizada**

Caso a transação seja realizada com sucesso pelo SiTef e no processo de baixa ocorreu algum erro, é possível estornar somente a transação no Sitef. Selecione o (s) lançamento (s) envolvido (s) e acione a opção 'Estorno' da tela do módulo de caixa. Será chamado o processo para cancelar a transação no Sitef. **Observação**: Sugerimos que tais transações sejam estornadas separadas de outras onde a baixa ocorreu. Entretanto, caso haja seleção de lançamentos com diferentes cenários, primeiro serão estornadas, de forma independente, as transações com baixa e, em seguida, as outras sem baixa.

**Falha na comunicação com terminal SITEF**

Na baixa integrada com SITEF quando a comunicação com o terminal é interrompida por algum motivo, será apresentada a mensagem de erro informando a falha de comunicação e somente haverá a opção de clicar em [Ok]. Logo, o sistema automaticamente retorna para o operador a visão de forma de pagamento do formulário da baixa, onde caso queira concluir a baixa, deverá tentar novamente ou modificar o meio de pagamento para outro tipo primitivo (diferente de cartão) que não utilize o Sitef para recebimento de pagamento. Caso não queira efetivar a baixa, o operador deverá cancelar o processo através do botão [Cancelar] no formulário de baixa.
