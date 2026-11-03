---
content_hash: 08977bd2d7b30771717b8232404d6db7e0f6dbf21ba618112004fef350593638
fetched_at: '2026-06-29T00:06:02.190598+00:00'
page_id: '198944190'
product: rm
source: tdn-rm
title: Controle de Deduções Contratuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198944190
version: 7
---

## Visão Geral

As deduções tratadas neste processo são aquelas que envolvem despesas ou débitos não fiscais como: alimentação, transporte, combustível, dentre outras.   
Estas não são abatidas do valor do serviço, mas sim descontadas no momento do pagamento.   
Para realizar o controle de deduções contratuais, deve ser incluído um contrato no TOTVS Construção e Projetos, em seguida, gerar e medir os períodos do contrato.  
Devem ser informados os valores referentes à dedução através do processo de Liberação de período | Detalhamento de Retenção.  
Em seguida, deve ser executado o processo “Gerar integração com Suprimentos | Faturamento”.   
O movimento será enviado ao BackOffice Materiais, conforme parametrização.   
O valor do contrato será enviado integralmente e o valor referente á dedução será enviado para o campo “Despesa” no movimento |aba Valores.

**Principais Campos e Parâmetros**

O movimento utilizado para tratar as deduções de um contrato no TOTVS Gestão de Estoque, Compras e Faturamento deve ser do tipo 1.1.XX e deve estar parametrizado na etapa “Mov – Valores Financeiros 1/4”, parâmetro “Desconto” para ser registrado em Valor ou Ambos.  
***Observação***: Os movimentos gerados pelo TOP enviam somente o Valor da dedução.   
Quando o tipo de movimento for parametrizado para trabalhar com Percentual(%) o valor da dedução será calculado como zero, pois ao recalcular ele considera o percentual como zero.   
Sendo assim o tipo de movimento utilizado pelo TOP deverá ser parametrizado para usar Desconto em Valor ou Ambos.

No TOTVS Construção e Projetos, parâmetros de Projetos | Contratos, deve ser selecionada a opção “Discriminar valores de retenção e dedução” para que os valores informados para dedução sejam carregados no movimento.   
Na inclusão do Contrato, aba Fórmula deve ser utilizada a fórmula “C – valor com reajuste” para que seja enviado ao módulo de materiais o valor bruto do contrato.   
Na aba Defaults, deve ser informado o tipo de movimento que será gerado no BackOffice.

|  |  |
| --- | --- |
| **Tabela** | **Descrição** |
| TMOV | Movimentos |
| TTMV | Tipos de Movimentos |

Conteúdos Relacionados

* [Controle de Retenções Contratuais](http://tdn.totvs.com/pages/viewpage.action?pageId=198944573)
* [Como Fazer: Processo Medição de Contrato / Liberar Retenção](http://tdn.totvs.com.br/pages/viewpage.action?pageId=173082042)
