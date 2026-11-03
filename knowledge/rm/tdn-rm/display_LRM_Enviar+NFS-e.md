---
content_hash: 7f61189ffbd9db951a13cf6fef56e5df94fb23e3ee4b1e956df11883769a38b9
fetched_at: '2026-06-29T00:09:20.620588+00:00'
page_id: '422545721'
product: rm
source: tdn-rm
title: Enviar NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Enviar+NFS-e
version: 12
---

## **Conteúdo**

**Conteúdo**

## **01 Sobre**

O processo "Enviar NFS-e" é responsável por localizar os Movimentos de RPS, montar um XML com os dados e transmiti-los para autorização da prefeitura.  
Na tela do processo, informe a Filial, o Tipo de Movimento, Data de Emissão e Faixa de Numeração. Serão selecionados todos os Movimentos de RPS que ainda não tenham sido enviados ou que estejam com status "Inconsistente" ou "Rejeitado".

## **02 Integração RM x TSS ou TPF**

Ao executar o processo, o RM não transmite a NFS-e diretamente para a prefeitura, mas realiza a integração com um dos aplicativos auxiliares: TSS ou TPF. Esses aplicativos, por sua vez, irão assinar e transmitir o XML para o ambiente da prefeitura.  
Esta integração é realizada através do modelo único de XML que disponibiliza todos os campos de todas as prefeituras. Não é necessário preencher todos os campos, apenas aqueles que são requeridos para a prefeitura em questão.

## **03 Quantidade de RPS por Lote**

O processo pode ser configurado para definir a quantidade de RPS que serão enviados no lote para a prefeitura, mas esta quantidade pode mudar de acordo com as regras de cada prefeitura. A quantidade informada para o lote não tem relação com a capacidade de transmissão do processo, ou seja: o usuário pode definir o parâmetro de lote como "10" e executar o processo selecionando uma quantia de 10.000 movimentos. Neste exemplo, o processo irá identificar a parametrização e montar 10 lotes com 1.000 RPS automaticamente.

## **04 Performance**

Algumas empresas transmitem uma grande quantidade de RPS de forma simultânea. Para que não ocorram problemas de performance, o processo "Enviar NFS-e" foi habilitado com o Fracionamento de Jobs, tornando o processo significativamente mais rápido.   
Para saber mais, consulte a documentação:

## **05 Outras informações**

* [Envio de NFS-e por arquivo texto](http://tdn.totvs.com/pages/viewpage.action?pageId=422546002)
