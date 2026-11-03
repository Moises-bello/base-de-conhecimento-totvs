---
content_hash: a521dcdec9955f65fae633d9d50b90cff827fd218f8f70c138f2a23206922648
fetched_at: '2026-06-29T00:10:43.133771+00:00'
page_id: '550111895'
product: rm
source: tdn-rm
title: DT - Cópia de Parâmetros entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550111895
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Contábil |
| Função: | Cópia de parâmetros entre coligadas |
| Requisito/Story/Issue (informe o requisito relacionado) : | CONTROLADORIA01-4567  CONTROLADORIA01-5464 |

## **02. SITUAÇÃO/REQUISITO**

Foi solicitado pelo PO da equipe a criação de um processo de cópia de parâmetros contábeis entre coligadas.

## **03. SOLUÇÃO**

Implementação do processo de cópia de parâmetros entre coligadas do módulo contábil. Ele é responsável por copiar toda a parametrização da coligada de origem para a coligada de destino. As tabelas envolvidas nessa cópia são CPARAM, GCCUPAR, GPARSTATUS e CMULTIMOEDA.

Durante a execução do processo não iremos copiar os dados das tabelas CCONTAMOEDAFUNCIONAL e CBLOQUEIOCONT, que representam as contas de moeda funcional e os bloqueios da contabilização respectivamente.

Ao final da execução deverá ser exibido um log informando os dados que foram copiados. Esse log também deverá conter um texto informando que as contas de moeda funcional e os bloqueios de contabilização não serão enviados para a coligada de destino. Caso o usuário marque a opção “Substitui registros no destino se eles já existirem” o log deverá ser gerado como dito anteriormente, porém para os registros que representam máscaras deverá ser informado que esse tipo de informação já existe na coligada de destino.

É importante destacar que esse processo só estará disponível no template que se encontra em Serviços Globais -> Administração -> Cópia de Coligada.

## **04. DEMAIS INFORMAÇÕES**

Para executar o template é necessário configurar o ambiente para 3 camadas, permitindo que o agendamento seja realizado. Em seguida iniciar o servidor de job no cockpit e dar permissão de acesso aos jobs em Segurança -> Segurança de Jobs Fracionáveis. Por fim é necessário dar permissão ao usuário logado em Serviços Globais -> Perfis, para que ele possa acessar o cadastro de cópia coligada template e executar o processo de cópia de coligadas.
