---
content_hash: 685b6bc15dab3a9d2eac780653907bf72aa9d36048f30eec3f4b474383f80f5a
fetched_at: '2026-06-29T00:09:26.034237+00:00'
page_id: '423938228'
product: rm
source: tdn-rm
title: Unidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Unidade
version: 4
---

Nesta opção, cadastram-se a Unidade de Medida que serão utilizadas pelo sistema. As unidades aqui cadastradas poderão ser utilizadas nos produtos, nas cotações e movimentos.

***Observações***: O Fator de Conversão, é o valor, em relação a unidade base, pelo qual deverá ser multiplicada a quantidade do produto nesta unidade. Será respeitada uma consistência que verificará se o fator de conversão, após ser truncado, será diferente de zero. Caso o fator de conversão seja diferente de zero, será gravado normalmente, caso contrário, uma mensagem será exibida para o usuário informando que o fator de conversão está errado e deverá ser alterado. As quantidades serão apresentadas, de acordo com o número de casas decimais informada na unidade, no campo Nº Casas Decimais.   
O tamanho do Código Reduzido está limitado a 2 caracteres e será utilizado para a integração com parceiros de automação comercial, devido à restrição existente nas impressoras fiscais, que limitam o tamanho do código da unidade de medida.

**Migração**  
   
Para o Cadastro de Unidades do TOTVS Gestão de Estoque, Compras e Faturamento serão desenvolvidas telas web utilizando o TOTVS HTML Framework. Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig e/ou Portal RM para que o usuário possa ter um acesso mais ágil e prático do cadastro.  
   
**Campos e Regras**  
   
O Cadastro de Unidade de Medida possui os seguintes campos e suas respectivas regras.  
   
**Código:** Código da unidade de medida. Campo obrigatório.

**Descrição:** Descrição da unidade de medida. Campo obrigatório.

**Cód. Unidade Base:** Utilizado para a conversão. Não poderá ser alterado caso esteja vinculado a um produto com saldo. Valor padrão: UN.

**Fator de Conversão:** Utilizado, juntamente com o cód. de unidade base para realizar a conversão. Não poderá ser alterado caso esteja vinculado a um produto com saldo. Deve ser positivo. Valor padrão: 1.

**Código Reduzido:** Sigla que identifica, de forma resumida, o código da unidade. Tamanho máximo de 2 caracteres.

**Nº Casas Decimais:** Utilizado ao exibir/imprimir as quantidades. Necessário ter um valor maior que zero e não pode conter mais que 4 caracteres. Valor padrão: 0.
