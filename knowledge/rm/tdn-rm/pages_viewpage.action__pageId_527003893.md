---
content_hash: e8e1261027d6dd38f5fd64eee5aa177cf3e14c8bb4f9ad275bacd360cde5606a
fetched_at: '2026-06-29T00:10:32.529795+00:00'
page_id: '527003893'
product: rm
source: tdn-rm
title: DT - Anonimização de candidatos (Exclusão do Banco de talentos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527003893
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Gestão de Pessoas |
| Função: | Candidatos |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [RHU01-9232](https://jiraproducao.totvs.com.br/browse/RHU01-9232) |

## **02. SITUAÇÃO/REQUISITO**

Necessidade de criar uma rotina em que os usuários podem pedir que seus dados de candidato sejam apagadas dos sistemas da empresa, tanto pelo Banco de talentos quanto pela MDI.

## **03. SOLUÇÃO**

Foram criadas duas rotinas em que é possível solicitar a exclusão dos dados  uma pelo Banco de talentos no qual o próprio usuário escolhe que quer seus dados apagados e outra rotina em que a pessoas responsáveis do RH podem selecionar os candidatos e apaga-los partir de um processo.

### Banco de talentos

No banco de taletos foi criada uma nova aba chamada **Excluir Cadastro:**

Ao clicar na aba é aberto uma página mostrando qual a finalidade do processo.

Ao clicar em **Excluir** é executado o processo de exclusão. Com a conclusão do processo com sucesso será enviado um e-mail para o usuário confirmado a exclusão e ele será desconectado do Banco de Talentos.

**Observação:**Caso o usuário possua algum outro vinculo no sistema que não esteja relacionado com o candidato, não será possível concluir a exclusão e será necessário que o usuario entre em contado com Recursos Humanos da empresa para que seja feita uma analise  dos dados.

### MDI

Na MDI foi modificado o processo na visão de candiados chamado **Exclusão Coletiva de Funcionários**para que seja possível excluir os dados de candidatos selecionados na visão.

No processo foi criado um parâmetro **Apagar candidato com base na LGPD** , que ao marca-lo serão excluídos todos os dados do candidato mesmo que este esteja participando de um processo seletivo, mas não serão excluídos aqueles que possuem referencias em outras partes do sistema. Ao final do processo será mostrado um log detalhando quais candidatos selecionados foram excluídos e quais não foram. Para os candidatos que não foram excluídos é possível ver os motivos pelos quais não foi possível concluir o processo.
