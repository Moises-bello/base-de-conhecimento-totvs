---
content_hash: 175fddc127d38848ed06eff5c5971ff188c25304884c01aaa3ac3ad1bcd0c4dc
fetched_at: '2026-06-29T00:09:47.230203+00:00'
page_id: '435104998'
product: rm
source: tdn-rm
title: Imóvel - Processo - Alterar situação do imóvel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104998
version: 8
---

Este processo permite alterar o valor do campo "Situação do imóvel" no cadastro de imóveis. As opções para alterar a situação são: Ativar, Inativar, Vender.

* **Inativar Imóvel**: Acessar a funcionalidade de Aluguel, acessar o cadastro do imóvel, executar o processo "Alterar situação do imóvel", selecionar a opção Inativar e informar o motivo da alteração. Ao executar o processo o sistema irá alterar a situação do imóvel para "Inativo".
* **Ativar Imóvel**: Acessar a funcionalidade de Aluguel, acessar o cadastro do imóvel e executar o processo "Alterar a situação do imóvel". Selecionar a opção Ativar e informar o motivo da alteração. Ao ativar um imóvel o processo irá alterar a situação do imóvel para a situação mais adequada seguindo a seguinte regra:
  + Se existir contrato de locação em elaboração a situação do imóvel será "Reservado";
  + Se o imóvel for de propriedade da administradora, a situação será "Disponível para locação";
  + Se o imóvel não for de propriedade da administração a situação será "Disponível para administração".

OBSERVAÇÃO:

A partir da **versão 12.1.2209**, ao realizar o processo de alteração de situação do imóvel será apresentada uma opção ***(imagem 1)*** para "Alterar o status do imóvel mesmo quando estiver **vinculado ao módulo de Vendas\Contratos" *(imagem 2)*.**   
  
***Imagem 1:***  
  
  
***Imagem 2:***

* **Vender Imóvel**: Esta opção poderá ser utilizada quando a administradora desejar vender um imóvel, seja ele próprio ou de terceiros. Acessar a funcionalidade de Aluguel, acessar o cadastro do imóvel, executar o processo "Alterar situação do imóvel", selecionar a opção Vender. Ao executar o processo o sistema irá alterar a situação do imóvel para "Vendido". Caso esta opção seja selecionada e o imóvel em questão possua alguma despesa vinculada, serão seguidas as seguintes regras:
  + A despesa associada e suas respectivas parcelas e parcelas de reembolso ficarão indisponíveis para alteração.
  + Os lançamentos em aberto das parcelas de reembolso serão cancelados.
  + As parcelas de reembolso que possuírem lançamento baixado ficarão com o campo "Tipo integração financeiro" igual a "Cancelado", porém os lançamentos baixados não serão alterados.
  + Após a alteração de status para "Vendido", não será possível executar o processo "Gerar movimento de despesa".
  + **Restrições:**
    - Se a despesa associada ao imóvel possuir alguma parcela ou parcela de reembolso vencida, não será possível alterar o status.
    - Se o imóvel em questão possuir contrato de locação ativo, não será possível alterar o status.
    - Se o imóvel estiver associado com um seguro, não será possível alterar o status.
    - Se o imóvel estiver vinculado à uma subunidade, não será possível alterar o status.

[Voltar](http://tdn.totvs.com/pages/viewpage.action?pageId=435105278)
