---
content_hash: 154ede8e6a912b5c86295e3236c44cd6f6b279aac2de64c1f555a6b9b039912d
fetched_at: '2026-06-29T00:09:28.756175+00:00'
page_id: '423938786'
product: rm
source: tdn-rm
title: Tipos de Produtos para Faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipos+de+Produtos+para+Faturamento
version: 3
---

Por esta opção serão cadastrados os tipos de produto para faturamento. Esse cadastro pode ser definido para cada produto cadastrado no sistema como um default, na pasta "Integração | Tipo para Faturamento" . Essas informações são utilizadas em conjunto com o Tipo de produto por Filial para o calculo de tributos no movimento.   
    
 **Exemplos de Tipos de produtos para faturamento**

Produto (venda), serviço de manutenção, serviço de instalação.  
Os campos disponíveis para preenchimento no cadastro são:  
**Código**: Informe o código do tipo.  
**Descrição**: Informe a descrição para o tipo de produto para faturamento.  
**Sigla Série**: Informe a sigla para o tipo, exemplo:

* SM (para o tipo "serviço de manutenção"),
* SI (para "serviço de instalação),
* PV (para "produto de venda"), etc.

**Campo Livre**: Este campo é destinado para qualquer informação adicional que desejar registrar para o tipo incluído.  
**Comissão**: Informe, se desejar, o percentual de comissão para o tipo de produto.  
**Cont. Nº Série**: Informe o número inicial para ser o contador do número de série para os produtos do contrato.  
**Inc. Nº Série**: Marque esta opção se deseja que o número de série do item do contrato seja incrementado, ou seja, para cada item incluído no contrato, o número de série será acrescido de 1, de acordo com o número inicial indicado no campo anterior, sendo que nos parâmetros do contrato, que são determinados através do menu Opções/Parâmetros/Contratos, precisa ser indicado que o número de série será sequencial.  
**Inc. Nº Coligada**: Informe se deseja que o sistema também incremente o número da coligada no número de série do item do contrato.  
***Observações***: Os campos "Inc. Nº Série" e "Inc. Nº Coligada" só poderão ser acessados se nos parâmetros do contrato, você optou por utilizar número de série sequencial. Só será permitida a exclusão de tipos que não estão sendo utilizados por algum contrato.

---
