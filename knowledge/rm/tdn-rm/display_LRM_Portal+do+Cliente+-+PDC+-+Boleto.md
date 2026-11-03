---
content_hash: dd9ac5f28b7c8b1673c5f1933f492d2518b4637e2faa6ea1a80ba81e52c8b970
fetched_at: '2026-06-29T00:10:25.909921+00:00'
page_id: '506392927'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Boleto
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Boleto
version: 40
---

PDC - Segunda via BoletoSegunda Via Boleto

Nesta tela, será possível acessar a **segunda via dos boletos em aberto**, referentes às parcelas de financiamento da(s) venda(s) do usuário.

Importante!

Para que os boletos gerados sejam listados nesta visão os mesmos devem estar com [Status da Remessa](https://tdn.totvs.com/display/LRM/Status+CNAB+do+Boleto) igual a *Registrado* ou *Registrado Online*.

**Utilização**

Para habilitar esta funcionalidade no PDC é necessário conceder permissão para o perfil de usuários em questão, no caminho **TOTVS Serviços Globais>Segurança>Perfis>duplo clique no perfil desejado>Acesso a Menus>Incorporação>Incorporação (Portal)>Cliente>Boleto (2ª via).**

                                              Tela de permissão de acesso a menus do RM

Ao acessar o menu “**2ª Via de Boleto**” no PDC, será exibida a tela abaixo com os respectivos boletos, que estejam com cnabstatus Registrado e Registrado Online, agrupados por subunidade.

O usuário poderá também, acessar os seus boletos de contratos de aluguel, caso possua boletos emitidos, no status de Registrado e Registrado Online.

Para isso basta selecionar o contrato de aluguel em questão, utilizando o botão Alterar empreendimento/contrato.

A visão de boletos de aluguel não possui diferenças da visão de boletos de contratos de venda e possibilitará ao usuário gerar uma segunda via dos boletos, bem como copiar o código de barras para a área de transferência, como explicado com maiores detalhes abaixo.

Importante!

* Caso o usuário possua um **boleto agrupado**, cujos lançamentos pertençam a um contrato de aluguel e um contrato de venda, o mesmo boleto irá aparecer tanto na visão de boletos de aluguel, quanto na visão de boletos de venda e seu valor sempre será o valor total de todos os lançamentos que compõem o boleto, independente do contexto selecionado.
* Os Boletos de Reembolso das despesas que pertencem ao Imóvel do Locador ou Subunidade do Comprador, também deverá aparecer na visão da 2ª Via de Boleto para emissão.

                                                                           Tela de 2ª via de boletos do PDC

Clicar em Baixar o Boleto ou Gerar código de Barras.

Ao clicar no ícone de código de barras abaixo do título “**Cód. de Barras**”, o código de barras do boleto será copiado para a área de transferência do sistema operacional.

                                                                           Cópia do código de barras

[Fórmula que calculará o código de barras / IPTE num ambiente integrado com o Protheus](https://tdn.totvs.com/x/BsSQHQ)               

Download de Boletos

"Para realizar o download de boletos no portal do cliente, é necessário que o boleto esteja registrado ou com registro online. Caso contrário, o download não estará disponível."

O botão de ocultar as informações do **BOLETO** , oculta também o valor das parcelas.

E o Boleto tem a informação da **Compensação do BOLETO**.

Despesas no Boleto

**Obs: Descrição da Despesa de Venda é informado em 2ºvia de Boleto como é mostrado abaixo:**

**Descrição de Despesa de Venda sendo visualizado no Boleto do PDC.**

Registro de PIX no Boleto

Agora será possível realizar o pagamento de 2ª via de boleto por PIX para boletos que possuam remessa PIX registrada com o respectiva instituição financeira.

O pagamento por PIX agora encontra-se disponível no PDC (Portal do Cliente), que pode visualizar o QR code PIX e copiar o QR code PIX

* (QR code PIX)
* (Copiar QR code PIX)

Na visão de 2ª via de boletos , foram incluídas as colunas “QR code PIX” e outra para a cópia “Copiar QR code PIX”.

O botão de QR code PIX, irá mostrar a imagem com o QR code PIX para ser lido.

O botão de Copiar QR code PIX irá copiar para a memória do dispositivo o QR code PIX para ser colado em um aplicativo ou site de instituição financeira para pagamento.

Em versões anteriores apenas os boletos registrados com o banco eram apresentados no portal no menu de 2ª via de boleto. Agora com o PIX, além de todos os boletos registrados, agora serão apresentados também os boletos que tiverem a remessa PIX registrada.

**Diferença entre PIX - Remessa CNAB e PIX TOTVS Pagamento Instantâneo**

É importante ressaltar que existem diferenças entre as duas opções de pagamento de boleto por PIX.

O TOTVS Pagamento Instantâneo (TPI) é um produto exclusivo TOTVS, onde o pagamento dispensa negociações com Instituições Financeiras, reduz custos com tarifas de outros meios de pagamento e conta com a facilidade da conciliação de venda automática e oferece uma experiência mais fácil e segura aos seus clientes, que realizam pagamento via PIX, de forma presencial ou online.

Já para o PIX de remessa, o pagamento é negociado diretamente com a instituição financeira. Esta modalidade de pagamento PIX possibilita que seja utilizada uma chave para identificar os dados bancários. A chave não é obrigatória, mas fará com que os pagamentos sejam mais ágeis.

Neste momento a chave deverá ser criada diretamente no sistema bancário que é utilizado pelos usuários e posteriormente poderá ser vinculada no RM.

A chave, que poderá ser usada no lugar do banco/agência e conta, poderá ser identificada de 4 formas diferentes:

* Telefone
* E-mail
* CPF/CNPJ
* Chave aleatória

Para mais informações segue abaixo as documentações mais detalhadas sobre as modalidades descritas.

Importante:

Documentação do Totvs Gestão Financeira sobre a configuração e o processo do PIX - Remessa CNAB: [PIX (Pagamento instantâneo) - Remessa CNAB](https://tdn.totvs.com/pages/viewpage.action?pageId=572497578)

Documentação do PIX - TOTVS Pagamento Instantâneo: [PIX - TOTVS Pagamento Instantâneo](https://tdn.totvs.com/pages/viewpage.action?pageId=577622236)

Observação importante:

Não existe a segunda modalidade de PIX no aluguel (Via TPI), pois esse módulo não gera pagamento instantâneo pelo PDC nem pelo APP.

**Processo PIX**

Selecionar o Boleto e em seguida : Remessa Cobrança Eletrônica

Agora no processo de Remessa tem a opção de ( PIX )

Neste exemplo : 3 Boletos Registrados.

Boleto 9095 – Registrado Remessa PIX

Boletos 9096 e 9097 – Registrados Remessa Boleto

Portal PDC | Segunda Via de Boleto

Visualização dos Boletos no Portal PDC

Boleto 9095 – Registrado Remessa PIX

Boletos 9096 e 9097 – Registrados Remessa Boleto

**Observação: O boleto pode estar Registrado por PIX e Registrado por Boleto.**

Boleto no PDC com as Duas opções.

Cliente pode optar por :

* Imprimir segunda via de boleto
* Cód. de Barras
* QR code PIX
* Copiar QR code Pix

APP - Meu imóvel.

APP meu imóvel informa quando o Boleto é Registrado por PIX.

PIX - Lançamento Aluguel.

PIX no Aluguel.

Lançamentos gerados no contrato de Locação.

**No APP meu Imóvel também é informado o PIX para o usuário.**

Data Limite para Geração de Boleto

Antes o TCGI poderia colocar a quantidade de dias que o cliente poderia gerar o vencimento do boleto. No caso se o parâmetro estiver como 30 dias, o cliente pode gerar um boleto para o mês que vem e durante esse tempo a parcela sofrerá uma correção monetária.

Agora o cliente TCGI poder gerar o boleto com vencimento até o ultimo dia útil do mês.

**Melhoria para o novo parãmetro:**

* Maior liberdade para o cliente.
* Redução de mão de obra interna.
* Transparência para o cliente.

Parâmetros do Portal do Cliente | Relatórios

Limitar vencimento do Boleto até o ultimo dia do mês atual  ( Marcado ).

PDC mostrando a data limite para Gerar Boleto último dia do mês.

App Meu ímóvel.

Parâmetro Desmarcado e agora com limíte de dias = 0

Agora o limite é o dia presente.

App meu imóvel mostrando o dia Presente apenas.

Boleto Híbrido

### Implementação do Boleto Híbrido no PDC

### Melhoria que será liberada a partir da versão 12.1.2506

Foi implementado o **boleto híbrido** no Portal do Cliente (PDC).

Com essa implementação, ao configurar nos parâmetros do portal do cliente no TCGI para utilizar o boleto híbrido, o PDC passará a gerar o boleto híbrido na tela de **Situação Financeira**. Além disso, na tela de **2ª via**, serão apresentadas, em uma única interface, duas formas integradas de pagamento:

* **Código de barras** para pagamento via boleto bancário tradicional.
* **QR code PIX** para pagamento instantâneo.

Dessa forma, o cliente tem a flexibilidade de escolher sua forma preferida de pagamento, seja pela agilidade do PIX ou pela praticidade e prazo mais longo do boleto tradicional, sem comprometer a segurança e integridade da transação.

* Para configurar o uso do **boleto híbrido** no portal, acesse: [Totvs Incorporação - Parâmetros - Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047).
* Para saber mais sobre o funcionamento e vantagens do **boleto híbrido**, acesse: [Boleto Híbrido](https://tdn.totvs.com/pages/releaseview.action?pageId=908344227#0-1).

**É importante que o relatório associado à impressão deste tipo de boleto esteja parametrizado para apresentar tanto a imagem do código de barras, quanto a imagem do qr code pix.**
