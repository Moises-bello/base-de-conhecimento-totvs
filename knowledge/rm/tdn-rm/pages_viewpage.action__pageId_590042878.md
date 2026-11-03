---
content_hash: 644b69a85dcf08f7f2f253ce5054b1f76fa9006f0bcc535a1bcd605c6493123a
fetched_at: '2026-06-29T00:10:53.955430+00:00'
page_id: '590042878'
product: rm
source: tdn-rm
title: Transmitir NF-e de Devolução por Recusa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590042878
version: 7
---

No ato do recebimento de uma compra em seu destino o cliente pode recusar-se a receber a mercadoria por vários motivos. Este processo é conhecido como Devolução por Recusa, ocorre através de um Movimento de Entrada.

No RM a emissão de NF-e de entrada ocorre através de um Movimento de Entrada do tipo *Empresa-Empresa* e com o preenchimento do campo *Cliente Fornecedor Origem Destino*.

Para atender a legislação é necessário que durante a emissão da *NF-e de Devolução por Recusa* o *Remetente/Destinatário* da NF-e e do SPED Fiscal sejam preenchidos com dados da Filial e não com os dados do cliente.

Ao enviar uma NF-e de um movimento parametrizado através processo de *Cópia por Referência(30 - Devolução por Recusa)* em conjunto com o *Tipo de Natureza(Rotinas Legais)* igual a *Devolução por Recusa*, resultará em um XML da qual a tag destinatário (**dest** Grupo E, Linha 62) será referente a empresa, e não ao cliente/fornecedor de origem/destino.

false0lefttrue1Parametrização Geral1true1Passo 1

* Nos parâmetros gerais do módulo do Nucleus em Tipo de Movimento de Entrada(1.1.XX), parametrizar o Motivo de Referência com o tipo **Devolução por Recusa** na base e parametrizar o movimento desejado. [[1]](http://tdn.totvs.com#_ftn1)
* Parametrizar movimento para ser Empresa-Empresa;

Imagem2Passo 2

* Parametrizar Movimento para editar Cliente/Fornecedor de Origem/Destino na etapa 60 dos parâmetros gerais do Movimento.

Imagem3Passo 3

* A CFOP a ser utilizada como devolução por recusa deve esta devidamente parametrizada no campo Tipo da Natureza(Rotinas Legais);

Imagem2Criando Movimento

* Criar um movimento de Saída Interestadual ou Interno;
* Criar um movimento de Entrada por Cópia por Referência. Se deve utilizar o Tipo de Movimento parametrizado como Cópia po Referência (Devolução por Recusa) em um movimento de Entrada através do processo "Assistente de Cópia por Referência";
* No Cabeçalho o Emitente e Destinatário devem ser a mesma Empresa.
* Em Integrações Fiscais:
  + Utilizar a CFOP parametrizada como Devolução por Recusa;
  + Preencher o Código do Cliente
3Enviar NF-e

* Note que a tag **dest** foi preenchida com o comportamento descrito anteriormente (dados referentes a empresa).

ImagemNota

Disponível a partir da versão **12.1.28**

Informações

 Documento explicando parametrização [Motivo de Referência para Devolução por Recusa](https://tdn.totvs.com/pages/viewpage.action?pageId=274839397);
