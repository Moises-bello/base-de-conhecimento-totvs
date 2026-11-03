---
content_hash: 832036544e8ff4f50c0ac95df5b981cae9f81ea050888589baddf312edd82aaf
fetched_at: '2026-06-29T00:10:52.408130+00:00'
page_id: '572497578'
product: rm
source: tdn-rm
title: PIX - Integração via arquivo CNAB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572497578
version: 40
---

## **01. VISÃO GERAL**

Pagamentos instantâneos (PIX) são as transferências monetárias eletrônicas na qual a transmissão da ordem de pagamento e a disponibilidade de fundos para o usuário recebedor ocorre em tempo real e cujo serviço está disponível durante 24 horas por dia, sete dias por semana e em todos os dias no ano. É a modalidade de pagamentos e recebimentos mais atual e utilizada, na qual as transferências ocorrem diretamente da conta do usuário pagador para a conta do usuário recebedor, sem a necessidade de intermediários, o que propicia custos de transação menores.

As demais formas de pagamentos já conhecidas, como DOC/TED, Boletos, etc, continuam existindo, porém o PIX trouxe uma grande agilidade na compensação dos valores para o recebedor, visto que ocorre de forma instantânea. Para isso, algumas mudanças no sistema estão sendo necessárias para atender a demanda, e este documento centralizará todas as mudanças e orientações aos usuários do Backoffice Linha RM.

A modalidade de pagamento PIX possibilita que seja utilizada uma chave para identificar os dados bancários. A chave não é obrigatória, mas fará com que os pagamentos sejam mais ágeis.

Neste momento a chave deverá ser criada diretamente no sistema bancário que é utilizado pelos usuários e posteriormente poderá ser vinculada no módulo TOTVS Gestão Financeira.

A chave, que poderá ser usada no lugar do banco/agência e conta, poderá ser identificada de 4 formas diferentes:

* Telefone
* E-mail
* CPF/CNPJ
* Chave aleatória

IMPORTANTE!

###### O PIX está em estudo na TOTVS para que seja aplicado da melhor forma possível. As informações deste documento estão sendo inseridas gradualmente. Além do modelo de layout do gerador de saídas no padrão FEBRABAN CNAB 240 temos, até o momento, os layouts dos bancos Itaú, Bradesco, Banco do Brasil e Santander. Se você possuir um manual atualizado de outro banco, pedimos que entre em contato para nos enviar para incluirmos no estudo.

##### 

****02. LAYOUT DO GERADOR DE SAÍDAS****

Existem alguns modelos de layouts que atendem esta modalidade de recebimentos e pagamentos PIX e estão disponíveis no [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento) para download.   
Observação: Os layouts devem ser importados através do gerados de saídas.

* Banco Itaú

Pagamento: FINLAY0062 - Pag. Itaú SISPAG 85 com PIX.TotvsGen   
**Importante**: Este layout contempla o tratamento de pagamento do FGTS com PIX através das funções de fórmula [CHAVEPAGAMENTOPIX](https://tdn.totvs.com/pages/releaseview.action?pageId=578643071) (extrai a chave de pagamento de um QRCode Pix) e/ou [CHAVETXIDPIX](https://tdn.totvs.com/pages/viewpage.action?pageId=578643071) (extrai o TXID de um QRCode Pix)

Cobrança: FINLAY0072 - Cob. Banco Itau PIX (750).TotvsGen

~~Cobrança: FINLAY0063 - Cob. Padrão PIX (750).TotvsGen~~

* Bradesco

Pagamento: FINLAY0065 - Pag. Bradesco CNAB240 com PIX.TotvsGen

Cobrança: FINLAY0063 - Cob. Padrão PIX (750).TotvsGen

* Brasil

Pagamento: FINLAY0066 - Pag. Banco do Brasil CNAB240 com PIX.TotvsGen

Cobrança: FINLAY0071 - Cob. Banco do Brasil PIX (750).TotvsGen 

~~Cobrança: FINLAY0063 - Cob. Padrão PIX (750).TotvsGen~~

* Santander  
  Pagamento: FINLAY0044 - Pag. SANTANDER (240) (Com Segmento J52, Tributos Com Código de Barras e PIX).TotvsGen   
  **Importante**: Este layout contempla o tratamento de pagamento do FGTS com PIX através das funções de fórmula [CHAVEPAGAMENTOPIX](https://tdn.totvs.com/pages/releaseview.action?pageId=578643071) (extrai a chave de pagamento de um QRCode Pix) e/ou [CHAVETXIDPIX](https://tdn.totvs.com/pages/viewpage.action?pageId=578643071) (extrai o TXID de um QRCode Pix)

**03. CADASTROS**

Contas Corrente x Chave PIX

Foi disponibilizado no cadastro de contas correntes o anexo , onde serão definidos as Chaves PIX das Contas Correntes da Empresa.

Você poderá vincular várias chaves PIX para a mesma conta corrente, mas é necessário que seja definida a chave PIX principal e ativa. Essa chave PIX principal, será utilizada na remessa de cobrança PIX.

Convênio

No cadastro de , foi disponibilizado na aba Remessa bancária o grupo "Cobrança Eletrônica PIX", onde deverá ser vinculado o layout para de remessa de cobrança com PIX.

Para o pagamento o layout utilizado tanto para o meio de pagamento PIX e outros meios é o mesmo.

Clientes/Fornecedores - Dados Bancários

No anexo , foram adicionados duas novas forma de pagamento que serão utilizadas na remessa de pagamento.

PIX Transferência - Será utilizado quando o pagamento for efetuado através de uma transferência PIX para conta do fornecedor.

PIX QR-Code - Será utilizado quando o pagamento for efetuado através de um documento que possui QR-Code

Lançamentos

No cadastro de lançamentos,  , foi disponibilizado o campo "QR-Code PIX". Esse campo será utilizado para lançamentos a pagar no qual o documento possui um QR-Code PIX de pagamento.

A leitura do QR-Code é feita através do botão ao lado do campo "QR-Code PIX", no qual será aberto um aplicativo que fará a leitura de um determinada área da tela. Caso o aplicativo não seja encontrado ao clicar no botão, basta clicar [aqui](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/barcode), baixar e descompactar o aplicativo no caminho onde está instalado a biblioteca RM parte client.

Boletos

Foi disponibilizado no cadastro de boletos os seguintes campos:

- Status Remessa PIX: Esse campo foi criado para armazenar o status da remessa PIX, a princípio não foi utilizado o campo "Status Remessa" permitindo que seja possível enviar uma remessa de cobrança e uma remessa cobrança PIX para o mesmo boleto.

- QR-Code PIX: Campo onde será gravado o EMV do QR-Code que será utilizado na geração de imagem do QR-Code. Ele é preenchido quando é feito o retorno de cobrança PIX e a emissão foi confirmada pelo banco.

- PIX Link: Campo onde será gravado o link gerado para o pagamento do QR Code. Ele é preenchido quando é feito o retorno de cobrança PIX e a emissão foi confirmada pelo banco.

# **04. PROCESSOS**

Geração de Boletos

A remessa de cobrança PIX é feita a partir dos boletos gerados. Esses boleto podem ter três operações:

01 - Geração de QR-Code

02 - Excluir QR-Code já gerado

04 - Alterar dados de um QR-Code já gerado

Essa operação é definida no campo "COMANDO" na geração do boleto. Também é possível definir o valor default CNAB no cadastro de  aba Cobrança bancária.

Remessa de Cobrança Eletrônica

Foi disponibilizado na remessa de cobrança eletrônica a opção PIX. Caso essa opção esteja marcada, então será levado em consideração o layout de cobrança PIX vinculado no cadastro de .

IMPORTANTE!

###### Para que o arquivo seja gerado é necessário que a conta corrente vinculada ao convênio, tenha pelo menos uma  principal e ativa.

Após executar o processo, o status de remessa PIX do boletos passaram a ficar com "Remetidos"

Retorno de Cobrança

Foi disponibilizado no processo de retorno de cobrança e retorno de cobrança em lote a opção "Retorno Cobrança PIX - 750 (layout específico do banco)". Quando o processo é executado com essa opção marcada, será exigido que as linhas do arquivo tenham 750 caracteres.

IMPORTANTE!

###### Não é necessário efetuar configurações de posições no cadastro de layout bancário, pois na opção "Retorno Cobrança PIX - 750 (layout específico do banco)" os campos são preenchidos de acordo com o banco e na "Retorno Cobrança PIX - 750" de acordo com o Layout do Banco Central.

O arquivo de retorno irá fazer as seguintes operações no boleto:

02 - Emissão confirmada - QRCode e o PIX Link foram gerados e serão gravado no boleto. Status de remessa PIX será alterado para "Registrado".

03 - Emissão rejeitada - Por algum motivo a geração do QR-Code do boleto não pode ser gerada. Status de remessa PIX será alterado para "Rejeitado".

06 - Recebimento - O QR-Code foi pago e o boleto/lançamentos serão baixados. Status de remessa PIX será alterado para "Baixado".

Remessa de Pagamento

Na remessa de pagamento as mudanças necessárias foram:

* Novas formas de pagamento 'PIX Transferência' e 'PIX QR-Code'. Mais detalhes em .
* Liberação do [campo "QR-Code PIX" no lançamento financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=445647401) para que seja possível informar o QR-Code de pagamento antes de incluir um borderô de pagamento no lançamento.
* Layout de pagamento (gerador de saídas): Adequação dos layouts citados acima com fórmulas que consistem as formas de pagamento relacionadas ao PIX ('PIX Transferência' e 'PIX QR-Code') e extração dos dados do QRCode Pix (funções de fórmula CHAVEPAGAMENTOPIX e CHAVETXIDPIX), possibilitando tratar os pagamentos do FGTS via CNAB, por exemplo.

IMPORTANTE!

###### Os layouts (gerador de saídas) dos bancos Itaú e Bradesco estão preparados para gerar dois arquivos de remessa de pagamento, um apenas para os pagamentos com PIX e outro para os demais pagamentos. Se na remessa gerada existir pagamentos somente com meio de pagamento PIX, serão gerados dois arquivos sendo o primeiro somente com o Header e Trailer (para os demais pagamentos) e o segundo será gerado com Header, Segmentos e Trailer (com os pagamentos com PIX). Somente deve ser enviado ao banco o arquivo que tiver as informações Header, Segmentos e Trailer.
