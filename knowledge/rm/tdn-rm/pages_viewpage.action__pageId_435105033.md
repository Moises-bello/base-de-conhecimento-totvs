---
content_hash: 5a13aac3e4e9f1e240d0b5986e502df8e1a7ce5580ebce62552df7357b0c258e
fetched_at: '2026-06-29T00:09:47.632402+00:00'
page_id: '435105033'
product: rm
source: tdn-rm
title: Empreendimento - Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105033
version: 9
---

**Empreendimento - Gestão Financeira**

---

**Filial:** Informe a filial do Empreendimento, o sistema apresentará na lista de opções todas as filiais já cadastradas no RM. Esta informação é obrigatória, pois os lançamentos a receber no RM Fluxus serão classificados com a filial do Empreendimento da venda (Obrigatório);  
   
**Departamento:** Informe qual departamento irá constar nos lançamentos do RM Fluxus, o sistema apresentará na lista de opções todos os Departamentos já cadastrados;  
   
**Centro de Custo:** Informe qual centro de custo irá constar nos lançamentos do RM Fluxus, o sistema apresentará na lista de opções todos os Centros de Custos já cadastrados;  
   
**Natureza orçamentária a pagar:** Informe qual natureza orçamentária a pagar irá constar nos lançamentos do RM Fluxus, o sistema apresentará na lista de opções todos as Natureza orçamentária a pagar já cadastrados;  
   
**Natureza orçamentária a receber:** Informe qual natureza orçamentária a receber irá constar nos lançamentos do RM Fluxus, o sistema apresentará na lista de opções todos as Natureza orçamentária a receber já cadastrados;

**Local de Estoque\*:** Informe o local de estoque para a geração de movimentos (comissões, despesas, etc.) para este empreendimento. O sistema apresenta para a seleção apenas os locais de estoque associados à filial do empreendimento. Esta informação não é obrigatória.

Importante!

\*Para que a informação do campo **Local de Estoque** seja persistida em banco, no cadastro do Empreendimento, é necessário executar o RM Atualizador com o Patch a partir  de 09/08/2024:

**Atividade Econômica:** Este campo estará disponível a partir da versão 12.1.25 para atender a legislação fiscal CPRB - CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA;  
   
**Item Contábil:**   
Informe o Item Contábil do Empreendimento;  
   
**Classe Valor:**   
Informe o Classe Valor do Empreendimento;  
   
**Rateio por Departamento:**   
É possível realizar o rateio por Departamento do Empreendimento.   
   
**Rateio por Centro de Custo:**   
É possível realizar o rateio por Centro de Custo do Empreendimento.

**Parâmetro : Calcular Valores Contábeis com Base na Diferença dos Valores de Repasse  :**Criado este parâmetro no cadastro de empreendimento para definir as contabilizações relacionadas aos contratos daquele empreendimento (venda, aditivo, distrato, reajuste, seguro e entrega de chaves) serão realizadas a partir do percentual não repassado (100% - percentual total dos repasses do empreendimento).  
**OBS**: Esse parâmetro terá efeito apenas quando o evento contábil **utilizado for por percentual.**

Repasse é feito na seguinte ordem:

**1º )** Buscando repasse no cadastro do Apto;

**2º )** Não achando , busca o Repasse no cadastro do Bloco; e

por **Último** , Buscando o repasse no cadastro do Empreendimento.

   
**Carteira:** Usado apenas para cobrança eletrônica. Consulte o manual de cobrança do Banco para certificar-se sobre o código correspondente à carteira a ser utilizada;   
   
**Comando:** Usado apenas para cobrança eletrônica. Consulte o manual de cobrança do Banco para certificar-se sobre o código correspondente ao comando. O comando varia de acordo com a operação a ser efetuada, como por exemplo , registro de títulos, solicitação de baixa, etc;  
**Banco:** Informe o código do banco que irá realizar a cobrança eletrônica;  
**Conta Contábil:** Informe a conta contábil do empreendimento para efetuar a contabilização;  
**Tipo de Documento a receber:** O sistema apresentará na lista de opções todos os tipos de documento já cadastradas no RM Fluxus. Esta informação é obrigatória, pois os lançamentos a receber no RM Fluxus serão classificados com o tipo de documento do empreendimento da venda;  
**Tipo de Documento a pagar:** O sistema apresentará na lista de opções todos os tipos de documento já cadastradas no RM Fluxus. Neste campo, deverá ser informado o tipo de documento da parcela gerada no RM Fluxus ocasionada por um distrato com devolução. O campo não é obrigatório e caso não seja preenchido será utilizado o tipo de documento definido no campo "Tipo de Documento".

**Conta Caixa:** Informe em qual conta caixa os lançamento no RM Fluxus serão gravados.

**Tipo de Documento de Adiantamento:** Informe um tipo de documento financeiro que tenha a classificação de *adiantamento*, que esteja ativo e que seja da mesma coligada que o empreendimento. Este tipo de documento será utilizado no Portal de Imóveis, para que seja possível criar o lançamento de adiantamento do sinal.

**Default de Juros e Multa**

**Valor Juros:**Informe o valor de Juros.  
**Fórmula Juros:**Informe a fórmula para o calculo dos Juros.  
**Valor Multa:** Informe o valor da Multa.  
**Fórmula Multa:** Informe a fórmula para calculo da Multa.  
**Tipo Juros ao dia:** Selecione o tipo de juros ao dia e informe o seu valor/percentual.  
**Carência de Juros:** Informe os dias de carência para os Juros.

É possível utilizar apenas uma opção para Juros/Multa, por exemplo, caso seja informado o valor de Juros os demais campos referente a juros serão desabilitados.

Voltar
