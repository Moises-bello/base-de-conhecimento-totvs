---
content_hash: 77c661830e42fd61e6983ad681b6c1d9300476456607d55301048631e7268093
fetched_at: '2026-06-29T00:10:44.017812+00:00'
page_id: '552079491'
product: rm
source: tdn-rm
title: DT - Cópia de Planos de Contas Paralelos entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552079491
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Contábil |
| Função: | Cópia de Planos de Contas Paralelos entre Coligadas |
| Requisito/Story/Issue (informe o requisito relacionado) : | CONTROLADORIA01-4565 |

## **02. SITUAÇÃO/REQUISITO**

Foi solicitado pelo PO da equipe a criação de um processo de cópia de planos de contas paralelos entre coligadas.

## **03. SOLUÇÃO**

Implementação do processo de cópia de planos de contas paralelos entre coligadas do módulo contábil. Ele é responsável por copiar a capa do plano paralelo, as contas paralelas, as contas contábeis associadas as contas paralelas e as contas gerencias/centros de custo associados as contas contábeis. As tabelas envolvidas nessa cópia são CPARALELO, CCONTA2, CCTACTA2 e CCTACTA2ITEM. Vale ressaltar que os planos de contas consolidados não serão copiados.

Ao executar o processo será verificado se a coligada de destino possui todas as contas contábeis, contas gerenciais e centros de custo necessários para realizar a cópia. Havendo uma ou mais pendências o processo será cancelado e o log gerado deverá informar quais estruturas devem existir na coligada antes da cópia ser executada. Se a execução do processo for realizada com sucesso será exibido um log informando os planos paralelos que foram copiados.

É importante destacar que esse processo só estará disponível no template que se encontra em Serviços Globais -> Administração -> Cópia de Coligada.

## **04. DEMAIS INFORMAÇÕES**

Para executar o template é necessário configurar o ambiente para 3 camadas, permitindo que o agendamento seja realizado. Em seguida iniciar o servidor de job no cockpit e dar permissão de acesso aos jobs em Segurança -> Segurança de Jobs Fracionáveis. Por fim é necessário dar permissão ao usuário logado em Serviços Globais -> Perfis, para que ele possa acessar o cadastro de cópia coligada template e executar o processo Cópia de Planos de Contas Paralelos entre Coligadas .
