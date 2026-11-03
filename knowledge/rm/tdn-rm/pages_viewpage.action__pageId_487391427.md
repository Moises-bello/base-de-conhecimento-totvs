---
content_hash: 2829ac9b17e2119a1e1ab420249c0c4917aa23025ef2f366f94f8f575cb38389
fetched_at: '2026-06-29T00:10:20.169710+00:00'
page_id: '487391427'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-4893 DT Provisão de contratos de forma isolada na contabilização
  por competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=487391427
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Gestão Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Contabilização por competência |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUINTEGRACOES-4893 DEDUINTEGRACOES-33 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a contabilização por competência do TOTVS Educacional, necessita-se que seja possível realizar apenas a provisão do contrato de forma que seja possível que esta provisão tenha data de contabilização anterior ao período de competência parametrizado no sistema.

## **03. SOLUÇÃO**

Foi desenvolvida nova funcionalidade no processo de contabilização por competência, de forma a permitir que seja feita a provisão do contrato de forma separada ou inclusive, parametrizar o sistema para que somente seja feita a provisão.

## **DESCRIÇÃO**

Com o objetivo de permitir a provisão do contrato de forma separada, foi desenvolvida funcionalidade que permite que seja feita a provisão de contrato de forma separada do diferimento mensal. Para tanto, passa a existir uma opção, ao executar o processo, para que o sistema faça apenas a provisão do contrato, conforme abaixo.

Com a opção acima habilitada, o sistema não fará a contabilização da competência mensal e por isso, o campo para digitação da competência fica desabilitado para preenchimento. Dessa forma, apenas a provisão do contrato será feita.

Como regra, a data de contabilização informada no processo será a data de contabilização da provisão do contrato. Porém, caso a data de contabilização não seja informada, a data do contrato será a data de contabilização da provisão, pois entende-se a data do contrato como a data do fato gerador. Caso o contrato não possua data, será utilizada a data atual do sistema.

Um doas objetivos de permitir a provisão do contrato de forma isolada é realizar a provisão na data do fato gerador, mesmo que o período de prestação de serviços ainda não tenha sido iniciado. Para tanto, utiliza-se a data do contrato conforme explicado acima. Porém, caso a provisão esteja sendo feita junto com o diferimento mensal, passa a existir opção para que mesmo assim, a data do contrato possa ser utilizada para a provisão do contrato. Para habilitar essa opção, é necessário parametrizar o sistema, conforme abaixo.

Outra opção que passou a estar disponível para o processo de contabilização por competência foi a parametrização que impede o sistema de realizar o diferimento mensal. Assim, uma vez parametrizado, o sistema somente fará a provisão dos contratos. Assim, o parâmetro para considerar a data de contrato, caso seja feita a contabilização junto com o diferimento mensal passa  estar indisponível por não fazer sentido, já que não será feito mais o diferimento mensal, conforme pode ser observado na imagem abaixo.

Caso o parâmetro para não diferir mensalmente esteja habilitado, o sistema exibirá uma imagem em cor amarela, alertando, caso se passe o mouse em cima dela, que o sistema não fará o diferimento mensal, exceto se o contrato já tiver sido diferido. Situação esta que pode ocorrer para os contratos já contabilizados antes do parâmetro ser habilitado. Ou seja, a data de competência para contabilização não é obrigatória e o que for digitado será ignorado para novos contratos.
