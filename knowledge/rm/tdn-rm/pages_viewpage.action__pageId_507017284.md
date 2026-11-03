---
content_hash: c3cf3233359e89d160741c40124ba9cdb8a05762db2e0c35cb48ae12ca04f8dc
fetched_at: '2026-06-29T00:10:25.966106+00:00'
page_id: '507017284'
product: rm
source: tdn-rm
title: Impressão de Requisição ao Concluir Prescrição do PEPRM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=507017284
version: 18
---

## 

## **ÍNDICE**

1. **Visão Geral**
2. **Habilitando a Impressão**

sumarioVisão Geral

## **01. VISÃO GERAL**

Esse recurso permite que ao liberar uma prescrição no PEPRM seja possível realizar a impressão automática de um relatório na farmácia que atende a unidade de atendimento na qual paciente está alocado.

Habilitando a Impressão

## **02. HABILITANDO A IMPRESSÃO**

Para que seja impressa a requisição ao concluir uma prescrição é necessário que sejam realizadas algumas configurações que estão listadas abaixo.

1. Primeiramente é necessário que esse recurso seja habilitado para a Unidade de Atendimento (Cadastros / Uso Geral) desejada através do parâmetro **Imprime requisição direto na farmácia ao concluir a prescrição** presente na aba Farmácia.

1. É necessário configurar uma impressora para a unidade de atendimento na aba Estoques dos Parâmetros Gerais.
2. Em Relatórios / Gerador.NET é preciso criar um relatório que contenham os parâmetros CODCOLIGADA e NUMEROREQ.
3. Por fim em Utilitários / Utilitários do RM Saúde / Configuração de relatórios é necessário configurar o relatório que deseja imprimir para o Parâmetro 99 (Requisição). O relatório precisa ser do novo gerador.
4. O processo de impressão ocorre após a conclusão da prescrição médica. Quando a unidade optar pela utilização da checagem o processo de impressão não ocorrerá de maneira automática.

Se o Host estiver rodando como serviço do Windows, o dispositivo de impressão deve realizar a impressão sem exigir interação gráfica, como abrir uma janela para salvar o arquivo.

Impressão a partir da versão 12.1.2402

## **03. Impressão a partir da versão 12.1.2402**

A partir da versão 12.1.2402 teremos duas possibilidades de realizar a impressão da prescrição, são elas:

1. O cliente pode optar por realizar a impressão diretamente na impressora do local de estoque configurado, para isso, será necessário no host.config incluir a tag rmsaude\_ImprimeRequisicaoImpressoraFarmacia com o valor true, da seguinte forma:
2. Para esse cenário, só será necessário configurar impressora no servidor onde está hospedado o host.
3. O cliente pode optar por não utilizar a tag citada acima, com isso, o relatório será exibido diretamente no Prontuário eletrônico, o usuário poderá imprimir em qualquer impressora da instituição.

   Os clientes que estão hospedados no cloud da TOTVS não será possível realizar a impressão diretamente na impressora do local de estoque.

   ]]>
