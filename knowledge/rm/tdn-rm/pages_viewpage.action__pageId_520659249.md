---
content_hash: 7c28d9e715e0736f00ba21dec214e96cc5dd5ed6d4a6fb3e906682110609337c
fetched_at: '2026-06-29T00:10:31.003047+00:00'
page_id: '520659249'
product: rm
source: tdn-rm
title: Contrato de Locação - Dados Gerais - Rateio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659249
version: 8
---

O contrato de Locação permite que o valor seja dividido entre os diversos Centros de Custos dos imóveis inclusos. Caso o contrato possua imóvel com áreas fracionadas e as mesmas possuam centro de custo informado, estes serão utilizados no rateio. Caso contrário o sistema buscará o centro de custo informado no imóvel, se ainda assim não for encontrado, o centro de custo será buscado no Parâmetro de integração financeira do contrato.  
   
**Pré-Condições** 

1. Ter incluído pelo menos um imóvel no contrato de locação.
2. Ter informado no cadastro do Imóvel (Anexos > Centro de Custo), ou no cadastro da área do Imóvel, quando locado por área, ou no cadastro  de Parâmetros da Integração o campo [Centro de Custo]
3. Ter configurado o Parâmetro  Rateio Automático em : Ambiente/ Parâmetros/ TOTVS Incorporação/aluguel / Contrato de Locação.

**Gerando o Rateio Por Centro de Custo** 

* **Rateio por Centro de Custo Automático**  
  + Se o parâmetro "Utiliza Rateio Manual no Contrato de Locação" estiver desmarcado, o sistema preencherá automaticamente a aba Rateio ao adicionar um imóvel. Não será permitido que os dados desta aba sejam alterados.
  + É  de suma importância verificar os rateios do contrato e os centro de custos dos imóveis associados. O sistema somente irá permitir a efetivação do contrato caso os centro de custo do contrato de locação sejam os mesmos cadastrados no imóvel.

* **Rateio por Centro de Custo Manual**

* + Duplo clique no contrato de locação desejado.
  + Clique sobre o botão Gerar Rateio. O sistema adicionará os centros de custo à lista.
  + Os registros adicionados permitem que as seguintes colunas sejam alteradas:
    - **Centro de custo:** Permite manter, alterar ou excluir o centro de custo do rateio. Ao clicar nos "..." para edição, serão apresentados os centros de custo cadastrados na coligada corrente, possibilitando uma flexibilidade maior na distribuição do rateio.
    - **Percentual:** Se atribuído a apenas 1 Centro de Custos, deve possuir o valor 100.
    - **Valor Rateado:** Preenchido com o valor referente ao percentual informado. O valor total rateado é retirado do campo [Valor Total do Contrato]

É importante frisar que, quando o rateio é definido de forma manual e os percentuais são definidos como 0%, esses centro de custo com percentuais zerados não irão participar do rateio de centro de custo dos lançamentos financeiros.

---

Veja Também:
