---
content_hash: 653d2d4a6013bc5496f610edc5e4393dc803c22e96925db30c87bebf6e6fd488
fetched_at: '2026-06-29T00:11:38.047441+00:00'
page_id: '781205618'
product: rm
source: tdn-rm
title: Abrindo uma nova sessão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781205618
version: 21
---

Cada nova sessão possui suas identificações e também permissões específicas, que podem ser definidas no momento da sua abertura.

Permissões da Sessão

A partir da release 12.1.2402 as permissões específicas também podem ser definidas através dos parâmetros do módulo em *Ambiente | Parâmetros | Gestão Financeira | Contas a Receber | Caixa | Módulo de Caixa | Etapa 1 - Gerais*. Elas estão dispostas em dois grupos:

* **Permissões da abertura da Sessão de Caixa**

Essas definem as configurações da abertura para todas as sessões que serão criadas para a coligada. Veja mais [detalhes aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=744486589#Configura%C3%A7%C3%B5esiniciais-Permiss%C3%B5esdaaberturadaSess%C3%A3odeCaixa).

* **Permissões do operador**

As permissões do operador determina quais opções ele terá ao operar uma sessão de caixa. Veja mais [detalhes aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=744486589#Configura%C3%A7%C3%B5esiniciais-Permiss%C3%B5esdooperador).

## Identificação

**Operador** - Define o usuário que irá operar a sessão de caixa. Este campo é preenchido com o usuário logado no sistema no momento da abertura da tela.

**Conta Caixa** - Define qual conta/caixa será usada para registro dos recebimentos.

**Caixa Nº** - Define o número do caixa que será gerado.

Observações

O número do caixa é controlado por conta/caixa, sempre considerando o número da última sessão.

Se o número da última sessão for numérico, o sistema apresentará automaticamente o próximo sequencial.

Se o número da última sessão for alfanumérico, o sistema apresentará o número da última sessão.

**Código da Filial** - Define qual a filial será considerada durante as ações da sessão de caixa. Durante a abertura da tela, caso o contexto tenha uma filial selecionada, este campo é preenchido com a filial definida, podendo ser alterada pelo usuário responsável pelo cadastro antes de efetivar a abertura da nova sessão.

Campos obrigatórios

Os campos de Identificação da Sessão são obrigatórios.

---

## Permissão

Os parâmetros abaixo definem os recursos e comportamentos permitidos na sessão que está sendo aberta.

Paramêtros de Permissão

A partir da versão 12.1.2402, a tela de abertura da sessão foi reformulada e adota como critério de exibição das permissões para definição, o parâmetro "Permite alterar as permissões na abertura da sessão" que deve estar marcado, no menu *Ambiente | Parâmetros | Gestão Financeira | Contas a Receber | Caixa | Módulo de Caixa | Etapa 1 - Gerais.*Quando esse parâmetro estiver habilitado/marcado os dados a seguir serão exibidos, caso contrário, os campos ficarão ocultos e será utilizado o valor definido no grupo "Permissões da abertura da Sessão de Caixa" dos parâmetros do Módulo de Caixa .

**Recebimentos/Pagamentos** - Define qual a natureza dos lançamentos que o usuário poderá operar, dentre: recebimentos, pagamentos ou ambos.

**Encerramento** - Com esta opção marcada, o usuário operador do caixa poderá encerrar a sua sessão, caso contrário somente o operador supervisor poderá encerrar a sessão.

Observações

Existem três formas de realizar o encerramento da sessão, é importante que os gestores analisem e definam as permissões de acesso corretas a este recurso. [Saiba mais](https://tdn.totvs.com/pages/editpage.action?pageId=781216399)

**Emissão de Relatório de Encerramento de Caixa** - Ao marcar esta opção, ao realizar o encerramento, o relatório de encerramento da sessão de caixa será emitido.

**Estorna Lançamento Baixado em outra Sessão** - Ao marcar esta opção será possível estornar lançamentos baixados em outra sessão de caixa.

Observações

Lançamentos que **não**foram baixados via módulo de caixa, poderão ser estornados independente desta opção estar marcada ou não.

O operador do caixa poderá estornar lançamentos baixados de outra sessão, independente do usuário que realizou a baixa.

**Habilita TEF** - Ao marcar esta opção ficará disponivel na sessão a opção de receber usando os meios de pagamento de cartão, conectado com a máquina TEF.

**Porta PinPad** - Esta informação será preenchida automaticamente baseado no que foi definido nas [configurações iniciais](https://tdn.totvs.com/pages/viewpage.action?pageId=744486589#id-2.Configura%C3%A7%C3%B5esiniciais-Etapas6e7-TEFeTEFFilial).

**Habilita PIX** - Ao marcar esta opção, utilizando um meio de pagamento de PIX, será gerado e exibido o QRCode.

**Consulta aos Saldos** - Para que o operador de caixa tenha acesso aos saldos atuais da sessão de caixa esta opção deverá ser marcada.

**Saldo Inicial** - O saldo inicial corresponde ao valor que compõe o caixa no momento da abertura, poderá ser preenchido ou carregado através do Saldo por Operador ou do Saldo por nº Caixa.

Importante

Ao abrir uma sessão de caixa que está configurada com o TEF habilitado, é realizada a comunicação do SiTef registrando e configurando a integração.

## Processo de abertura da Sessão de Caixa

Se você usa algum dos parâmetros que não estão sendo considerados no Módulo de Caixa 2.0 e serão descontinuados, [compartilhe conosco](https://docs.google.com/forms/d/e/1FAIpQLSfhk_esNFQZK8Za0XbeAK4GjGgbG27nRqazmuoHrPJtXDfWpQ/viewform).

0solid

#### [Voltar para o Menu Principal](https://tdn.totvs.com/pages/viewpage.action?pageId=744486517)
