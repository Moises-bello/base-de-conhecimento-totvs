---
content_hash: 99dd9969ab25ff334a57f946f5a60b4ea076f73ec5cf6b71ede5b5bbfb8b0abd
fetched_at: '2026-06-29T00:08:09.112487+00:00'
page_id: '239024761'
product: rm
source: tdn-rm
title: TUUXNC_DT_Rastreabilidade_Lancamento_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUUXNC_DT_Rastreabilidade_Lancamento_Financeiro
version: 115
---

# Rastreabilidade lançamento financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Rastreabilidade do lançamento financeiro* |
| **Situação/Requisito:** | Para alguns usuários, ao acessar o menu de lançamentos financeiros (RM Labore) não está sendo apresentada a opção Rastreabilidade do Lançamento nos anexos do lançamento. Verifiquei que o sistema valida se o usuário tem permissão total para os menus relacionados ao item [06.05] Financeiro. Se qualquer permissão do perfil que inicie com 06.05 estiver bloqueada, por exemplo, [06.05.01.01] Parâmetros, o anexo não é apresentado.  Nesse caso seria necessário criar um menu de permissão específico para este anexo. |
| **Solução/Implementação:** | Script criado com a finalidade de incluir um parâmetro que irá direcionar a funcionalidade da rastreabilidade do lançamento financeiro do Labore para  outra action que conterá a sub tag de segurança específica para este processo. Este script deve ser executado apenas na versão 11.80  e apenas para os clientes que desejam utilizar a permissão específica da rastreabilidade,  pois atualmente o sistema vincula a rastreabilidade à outra tag de segurança (Parametros do lançamento financeiro).  Após a execução do script, o cliente deve habilitar a permissão para a rastreabilidade, que estará disponível como sub item da permissão  " [06.05.01.01] Parâmetros " |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUUXNC |
| **Requisito (ISSUE):** |  |

divs
