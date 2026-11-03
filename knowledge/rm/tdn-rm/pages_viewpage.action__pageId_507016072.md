---
content_hash: dcdbc80fb8142775c2d20a445237340e12e062dc83bf7b064ffc3c4d3c8eae80
fetched_at: '2026-06-29T00:10:25.962202+00:00'
page_id: '507016072'
product: rm
source: tdn-rm
title: 14 - Executar relatórios sempre via Job Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=507016072
version: 3
---

O Portal do Processo Seletivo é utilizado por usuários que não necessariamente estão registrados no sistema como um usuário, ou seja, realizam algumas atividades e executam funcionalidades sem estarem autenticados no sistema por um usuário e senha gerado previamente, como por exemplo, a própria inscrição do usuário no processo seletivo. Neste cenário, não é requerido que o usuário faça qualquer tipo de autenticação prévia no Portal do Processo Seletivo com um usuário próprio.

Nestas situações o Portal do Processo Seletivo associa todas as execuções e atividades a um usuário padrão chamado **RMProcessoSeletivo** para registrar em campos de log ou tabelas de auditorias todas as atividades realizadas pelos usuários anônimos.

Porém, quando o RM está parametrizado para sempre executar relatórios através de Job Server, um usuário cadastrado no RM passa a ser requerido para permitir que estes novos usuários do processo seletivo sejam capazes de durante o processo de inscrição, sejam capazes de gerar um boleto ou gerar um comprovante de inscrição. Ou seja, sempre quando for criado um novo Job a ser executado para a geração de relatório esta solicitação deverá ser feita através de um usuário existente no RM.

Portanto ao parametrizar o sistema conforme a documentação "", passa a ser **requerido** que seja cadastrado um novo usuário no produto "Processo Seletivo" chamado "RMProcessoSeletivo", independente da senha de acesso ou nível de permissão.

Este cadastro é necessário para manter a integridade do banco de dados ao referenciar usuários válidos em todas as execuções de Job.
