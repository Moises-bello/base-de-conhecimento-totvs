---
content_hash: 47fd73b0548bf674ea34a347fcae62004fbc37f51710751a6f6945c996ceb65a
fetched_at: '2026-06-29T00:09:18.549035+00:00'
page_id: '421388722'
product: rm
source: tdn-rm
title: FIN - Cobrança Eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388722
version: 10
---

O processo Cobrança Eletrônica visa automatizar os recebimentos de títulos através de integração com a Rede Bancária. Consiste na geração de arquivos de remessa dos lançamentos a receber e envio à rede bancária, que oferece serviços diversificados de processamento, tais como: cobrança registrada, sem registro, entre outros.  Neste contexto, a empresa estabelece um convênio com o Banco, que tem uma importante atuação garantindo agilidade e praticidade ao processo.

**Etapas do processo**

Convênio firmado entre a Empresa e o Banco para definir as regras da Cobrança. No Gestão Financeira foi unificado no cadastro do Convênio toda a regra da Integração Bancária, ou seja, o tipo de Carteira e de Cobrança, o tipo de geração do nosso numero e código de barras etc. Outro fator relevante é que um Banco poderá ser associado a diversos Convênios, garantido maior flexibilidade à Cobrança Eletrônica.

Atualização dos Cadastros (Bancos, Agência, Conta Corrente, Convênio e Conta Caixa).

Geração dos boletos de Cobrança. O Boleto como uma Entidade bem definida proporciona o agrupamento de Lançamentos Financeiros provenientes de qualquer segmento da linha RM. É possível incluir um Boleto agrupando Lançamentos gerados pelo Gestão Educacional e do Incorporação, por exemplo, sem distinção por segmento. Os dados da remessa, como por exemplo, Nosso Numero, Código de Barras e IPTE, ficarão armazenados no Boleto. Dessa forma, se houver uma baixa parcial, é possível gerar novo(s) boleto(s) para o(s) Lançamento(s).

Geração do arquivo de remessa pela opção "Boletos", localizada no menu Contas a Pagar / Receber, e envio ao Banco através da opção "Remessa Cobrança Eletrônica".

Processamento pelo Banco e envio de arquivo de retorno confirmando o processamento. Este primeiro arquivo, se importado na base de dados, não produzirá baixas automáticas, apenas resultará na atualização do Status CNAB dos Lançamentos. Havendo alguma rejeição, o Banco informará o motivo e a empresa então poderá gerar novas remessas para estes títulos.

Quitação dos títulos pelos Clientes. O Banco envia à empresa um arquivo de retorno contendo informações de data de quitação,  valor pago e outras informações afins que caracterizam a ocorrência. A importação deste arquivo produzirá a baixa automática dos respectivos Lançamentos Financeiros.

**Cancelamento de Remessa**

Ao realizar processo de cancelamento da remessa, o sistema irá limpar automaticamente o código de barras do boleto. Dessa forma, quando o boleto for remetido novamente ao banco, o Código de Barras poderá ser gerado novamente.

**Envio de Remessa**

O processo de envio de remessa tem como objetivo realizar a comunicação eletrônica com o banco.  
É possível gerar a remessa de cobrança para os boletos que estejam com os status Em Aberto, Cancelado, Baixado, Baixado Parcialmente ou Inativo e o status de remessa igual a "Não remetidos", "Remetidos", "Registrados" (esta opção vale tanto para o status 'Registrado' e 'Registrado Online'), "Recusados" e "Pendentes remessa".  
No processo de geração de remessa para boletos a serem cancelados junto ao banco, verifique antes se o campo COMANDO do boleto está preenchido de acordo com as regras de cancelamento do registro no banco.

**Observação:**

Para lançamentos que "serão" baixados por acordo, será preciso antes de realizar o envio da Remessa de Cancelamento ao banco, cancelar manualmente a Remessa, cancelar o boleto e realizar o processo de Remessa para o banco.

Para geração de remessa de lançamentos faturados, o sistema permite que o boleto faturado com status 'Pendente Remessa' seja remetido ao banco, para que ocorra a baixa do mesmo no banco.

 Veja Também
