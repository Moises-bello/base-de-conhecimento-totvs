---
content_hash: 195ecde209e9e211be1aa048fb0d366f102752956365fb4ee64b97656909c874
fetched_at: '2026-06-29T00:10:43.196825+00:00'
page_id: '550308333'
product: rm
source: tdn-rm
title: DT - Cópia de Eventos Contábeis entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550308333
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Contábil |
| Função: | Cópia eventos contábeis entre coligadas |
| Requisito/Story/Issue (informe o requisito relacionado) : | [CONTROLADORIA01-4566](https://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-4566) |

## **02. SITUAÇÃO/REQUISITO**

Foi solicitado pelo PO da equipe a evolução do processo já existente de Cópia de Eventos Contábeis entre Coligadas para atender a demanda do projeto de Aceleradores de Implantação.

## **03. SOLUÇÃO**

Implementação de um novo processo para atender a cópia pois, no cenário de implantação de nova coligada que surgiu sera necessário copiar toda a estrutura para garantir que os registro de classes de parâmetros de outros produtos não percam as referências com o  campo TEVENTOSCONT.CODEVENTO que é gerenciado pela tabela GAUTOINC.

Os eventos contábeis tem dependência com outros registros de outras bases. Segue a relação de dependência:

CCONTA, CGERENCIA, GFILIAL, GDEPTO, GCCUSTO, CCLASSIFICACC, CHISTP, DTRIBUTO, GFORMULA.

Além das tabelas citadas existe a dependência com a mascará do plano de contas Contábeis e Gerencias. Essas dependências caso não estejam presentes na coligada de destino impedem que o processo seja executado, sendo necessário a cópia destas informações antes da utlização do processo em questão.

Ao final da execução deverá ser exibido um log informando os dados que foram copiados. Caso o usuário marque a opção “Substitui registros no destino se eles já existirem” o log deverá ser gerado como dito anteriormente.

É importante destacar que esse processo só estará disponível no template que se encontra em Serviços Globais -> Administração -> Cópia de Coligada.

## **04. DEMAIS INFORMAÇÕES**

Para executar o template é necessário configurar o ambiente para 3 camadas, permitindo que o agendamento seja realizado. Em seguida iniciar o servidor de job no cockpit e dar permissão de acesso aos jobs em Segurança -> Segurança de Jobs Fracionáveis. Por fim é necessário dar permissão ao usuário logado em Serviços Globais -> Perfis, para que ele possa acessar o cadastro de cópia coligada template e executar o processo de cópia de coligadas.
