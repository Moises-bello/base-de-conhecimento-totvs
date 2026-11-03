---
content_hash: d14039d40ea65760823f0c0308c1c249f01630b69ec97ea0267562a8c7a212fd
fetched_at: '2026-06-29T00:10:51.660323+00:00'
page_id: '569502422'
product: rm
source: tdn-rm
title: Portal de Imóveis - Frontend - Propostas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=569502422
version: 31
---

### **Filtros por tipo de comissão, situação da proposta e CPF / CNPJ**

---

Da versão **12.1.33** em diante, foram adicionados dois novos filtros na visão de propostas:

* **Filtros por comissão:** Permitirá filtrar as propostas por tipo de pagamento da comissão: Cliente, Empresa ou Ambos (Cliente / Empresa);
* **Filtros por situação da proposta:** Será apresentada apenas a situação escolhida no filtro proposto.
* **Filtros por CPF ou CNPJ:** Será apresentado na visão, apenas o CPF ou CNPJ informado pelo usuário.
  + Importante: Ao pesquisar pelo CPF ou CNPJ o usuário não deverá digitar traços ou números.

### **Informações Importantes**

---

Importante: Quando o RM possui um componente e o mesmo tem o seu cálculo realizado através de uma fórmula, o Portal de Imóveis irá realizar este cálculo no momento em que a proposta é exibida. Esta funcionalidade será disparada no momento em que a proposta é exibida, bem como no momento da escolha da modalidade dentro da proposta.

### **Percentual de renda Comprometida**

---

Há um consenso no mercado de que o comprometimento de renda ideal para qualquer financiamento é de, no máximo 30%. Isso significa que, se a renda for no valor de R$1.000,00 por mês, a parcela não poderá ultrapassar os R$300,00 mensais que representa 30% da renda.

A partir da versão **12.1.33** ao selecionarmos a opção de mostrar dados adicionais durante a criação da proposta, será exibido também o percentual da renda comprometida que será calculado de acordo com os valores de renda mensal. Este campo é apenas informativo e pode ser verificado na imagem abaixo:

**Impressão da proposta:**Dentro da aba proposta estará disponível a opção "*Proposta: imprimir*", onde poderá ser realizado a impressão da proposta que será impresso com as seguintes informações:

* Do empreendimento, bloco, unidades, proposta e corretor;
* Dados do comprador;
* E os dados financeiro do comprador como :  Renda, Renda comprometida, Tipo de Renda, Credito FGTS, Credito de Financiamento e Validade da Avaliação, assim como as condições de pagamento.

Para a correta exibição do card na impressão da proposta, observar se os campos abaixo estão preenchidos:

**Correspondente:**Na opção Simular a proposta será possível selecionar o correspondente bancário da pessoa, esse corresponde poder informado no cadastra do usuário, ou estar vinculado diretamente no empreendimento.

**Componentes**

---

Quando a modalidade de venda for do tipo "Restringe no PVI", será exibido um botão de componentes disponíveis. Nesta visão serão apresentados todos os componentes que não possuem valores. Desta forma, será possível adicionar os componentes apresentados na proposta então inserir seus respectivos valores caso necessário.

Observação

* Para as modalidades do tipo restringe, os componentes removidos da proposta serão enviados ao backoffice com seus valores zerados

 

Importante

* Caso seja removido algum componente da proposta, ele continuará sendo exibido nesta tela de componentes disponíveis para que possa ser adicionado novamente caso necessário.
