---
content_hash: 4c00aaf0f3ad6e75659097bfbf36dcc34a4e37e39d7cf11ecb75e9108b36fb62
fetched_at: '2026-06-29T00:10:43.699448+00:00'
page_id: '550325873'
product: rm
source: tdn-rm
title: 2.5 Registro de Cobrança Online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550325873
version: 24
---

A funcionalidade de Registro Online de Boletos efetua o registro online junto ao Banco para os boletos incluídos no sistema, sem a necessidade de enviar arquivo remessa para o Banco. Para que o Registro Online possa ser executado com sucesso, o convênio deve estar parametrizado corretamente, na aba 'Registro Online' selecionando a opção 'Permite registro de boleto online', informando os dados do Sistema de Cobrança e URL de Registro do banco. Caso alguma informação esteja incorreta para o processo de Registro Online, irá ser exibido o log de divergência informando o ponto a ser ajustado, que é retornado pelo serviço de Registro do banco.

O detalhamento das parametrizações não estarão descritos por se tratar de atividades de implantação do sistema.

Somente os boletos com status de remessa "*Não remetido*" e com status de boleto "*Em aberto*" ou "*Baixado Parcialmente*" poderão ser registrados online.

Existem algumas maneiras para o registro online acontecer no SGE:

* [Portal do Aluno:](https://tdn.totvs.com/display/LRM/2.5.1+Portal+do+Aluno) Quando o aluno visualizar/imprimir o boleto através do "Portal do Aluno", o mesmo será registrado automaticamente de forma online;
* [TOTVS Gestão Financeira (inclusão de boleto em lançamento gerado pelo Contrato Corporativo):](https://tdn.totvs.com/pages/viewpage.action?pageId=550326011) Ao incluir um boleto em um lançamento gerado pelo contrato corporativo, poderá marcar a opção para registrar o boleto online;
* [TOTVS Educacional | Processo Seletivo](https://tdn.totvs.com/display/LRM/Boleto+Registrado): Quando o aluno visualizar/imprimir o boleto através do "Portal do Processo Seletivo", o mesmo será registrado automaticamente de forma online, vale ressaltar que isso ocorrerá para a primeira parcela/boleto, os demais quando houver deverá ser registrado acessando o extrato financeiro no Portal do Aluno;
* [Processos em Lote - Agendamento de Job](https://tdn.totvs.com/display/LRM/2.5.4+Processos+em+Lote+-+Agendamento+de+Job)[:](https://tdn.totvs.com/display/LRM/Processos+em+Lote+-+Agendamento+de+Job) Através do menu Processos em Lote disponível no TOTVS Gestão Financeira;
* [TOTVS Gestão Financeira (boletos gerados pelo Educacional e/ou Contrato Corporativo):](https://tdn.totvs.com/pages/viewpage.action?pageId=550326376) Os boletos poderão ser registrados através da execução do processo na tela de lançamentos, de forma manual.

Os bancos não disponibilizam serviços para alteração de informações dos boletos já registrados.

falseBancos homologados - Registro Online de Boletos

* [Registro Online Santander](http://tdn.totvs.com/pages/releaseview.action?pageId=272147537)
* [Registro Online Bradesco](http://tdn.totvs.com/display/public/LRM/DT+Registro+Boleto+Online+Bradesco)
* [Registro Online Itaú](http://tdn.totvs.com/pages/viewpage.action?pageId=273993534)
* [Registro Online Banco do Brasil](http://tdn.totvs.com/display/LRM/DT+Registro+Boleto+Online+Banco+do+Brasil)
* [Registro Online Caixa Econômica Federal](http://tdn.totvs.com/pages/viewpage.action?pageId=315890985)
* [Registro Online Sicredi](http://tdn.totvs.com/pages/viewpage.action?pageId=315901508)
* [Registro Online Banrisul](http://tdn.totvs.com/pages/viewpage.action?pageId=351384062)
Veja também

* [Layout Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online)
* [Visualizar XML/JSON do Registro Online no boleto](http://tdn.totvs.com/pages/viewpage.action?pageId=286499982)
* [Cadastro de Certificado Digital](http://tdn.totvs.com/x/WoovGQ)
* [Associação do Layout do Registro Online](http://tdn.totvs.com/x/1_EdGQ)
* [Inclusão de Boleto Registrado Online](http://tdn.totvs.com/pages/viewpage.action?pageId=273997002)
* [Registro Online para boletos inclusos](http://tdn.totvs.com/display/public/LRM/DT+Registro+Online+de+Boletos)
* [Motivo da Recusa do Registro Online de Boleto](http://tdn.totvs.com/x/meAfGg)
