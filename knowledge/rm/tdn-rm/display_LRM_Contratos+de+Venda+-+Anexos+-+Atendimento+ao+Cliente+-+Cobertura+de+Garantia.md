---
content_hash: 9c9c0aab0fac0a0a98677c872edf975a9e941003966b18b5abd32bc971e81795
fetched_at: '2026-06-29T00:09:47.605849+00:00'
page_id: '435105025'
product: rm
source: tdn-rm
title: Contratos de Venda - Anexos - Atendimento ao Cliente - Cobertura de Garantia
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Anexos+-+Atendimento+ao+Cliente+-+Cobertura+de+Garantia
version: 6
---

Neste anexo é possível visualizar as Coberturas de Garantia vinculadas a subunidade da venda, tendo os seguintes detalhes:

* **Status da Cobertura;**
* **Tipo de Cobertura;**
* **Data Inicial vigência**
* **Data final vigência;**
* **Mensagem;**
* **Tipo de inicio da vigência;**
* **Período de Vigência (meses);**
* **Venda/Aluguel.**

- Gestão de Imóveis possui dois tipos de atendimento que podem ser utilizados somente com fluxo do TIN ou com o Agilis (CRM).  
- Atendimento Garantia  
- Para que seja utilizado o atendimento de Garantia os pré requisitos são:   
Cadastro de Coberturas, Modelos e Etapas que se encontra respectivamente dentro do menu   
"Atendimento >> Coberturas", "Atendimento >> Modelos", "Atendimento >> Etapas"  
  
Associando a Garantia para Venda:  
Após os cadastros básicos deverá sempre que criar uma venda associar as garantias que a venda terá:  
- Action: ImbVendGarantiaCoberturaAction  
- DataServer: ImbVendGarantiaCoberturaData  
  
No Menu "Venda >> Contratos de Venda" com a visão de vendas aberta e com as Venda na situação "Em Preparação"   
vá na opção "Anexos >> Atendimento ao Cliente >> Cobertura de Garantia" adicione as garantias que serão cobertas para a Venda.  
  
Criando a Solicitação de Atendimento para Garantia:  
- Tem duas formas que poderá  ser utilizada para gerar os atendimentos:   
1 - Com a visão de Vendas aberta, selecione a venda desejada   
e no canto superior da visão vá em "Anexos >> Atendimento ao Cliente >> Solicitação de Atendimento".  
2 - No menu "Atendimento >> Solicitação de Atendimento".  
  
- Atendimento Entrega Chaves

Observação

Informação Importante sobre Cobertura de Garantia.

Cliente pode cadastrar um Atendimento de Garantia com ou sem nenhuma Cobertura de Garantia.

Para que possa cadastrar um novo Atendimento sem utilizar nenhuma cobertura de garantia , é preciso marcar o seguinte parâmetro abaixo.

Parametros do TCGI - Atendimento

Marcar o Parâmetro : Permitir cadastrar atendimento de garantia sem cobertura de Garantia vinculado a venda.

Esse parametro marcado , permite ao usuário cadastrar um atendimento sem nenhuma cobertura , ( Sem cobertura ou com alguma cadastrada já fora do período de vigência ).

**Solicitação de Atendimento de Garantia**

Neste anexo é possível visualizar a tela de Solicitação de Atendimento associada a venda. Para maiores informações sobre Solicitação de Atendimento, .

Veja Também

---
