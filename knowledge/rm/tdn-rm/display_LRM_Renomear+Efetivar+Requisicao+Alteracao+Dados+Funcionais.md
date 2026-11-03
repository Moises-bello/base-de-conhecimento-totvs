---
content_hash: 05ab315e8e2f8d63851d0cbd7a3e2f1fbece69b1a1beb582dc6125dfb434cba6
fetched_at: '2026-06-29T00:10:07.947195+00:00'
page_id: '452719480'
product: rm
source: tdn-rm
title: Renomear Efetivar Requisicao Alteracao Dados Funcionais
type: documentation
url: https://tdn.totvs.com/display/LRM/Renomear+Efetivar+Requisicao+Alteracao+Dados+Funcionais
version: 3
---

**Efetivar Alteração de Dados Funcionais**

A Efetivação da Alteração de Dados Funcionais tem por objetivo possibilitar a conclusão deste tipo de requisição pelo processo "Concluir Requisição".

Ao executar o processo "Concluir Requisição", a requisição terá seu status alterado para "Concluída" e os dados do funcionário selecionado serão atualizados de acordo com os dados propostos na requisição. Caso a requisição esteja vinculada a uma requisição "pai" essa também será concluída, sendo a requisição "pai" de aumento de quadro, essa será concluída se todas as vagas aprovadas tiverem sido utilizadas.

Ao executar o processo "Concluir Requisição", e a requisição possuir progressões relacionadas, o sistema terá o seguinte comportamento:

* - Possuindo apenas uma progressão, o processo irá efetivar a progressão e também irá concluir a requisição.
* - Possuindo mais de uma progressão, o processo irá efetivar apenas a próxima progressão e não irá concluir a requisição, pois a requisição só pode ser concluída depois de todas as progressões efetivadas. No caso de ser a última progressão, o processo irá efetivar a progressão e também irá concluir requisição.

Como forma de acompanhamento dos processos relacionados à requisição serão enviados e-mail´s com mensagens padronizadas, podendo ainda optar-se pela notificação ao gestor de RH e ao gestor do departamento pessoal.

Todo o processo de notificação poderá ser parametrizado no aplicativo, para isto verifique em Opções | Parâmetros | RM Vitae | Geral | Pasta "Requisições".

**Observações**

* - Somente podem ser concluídas as requisições aprovadas de alteração de dados funcionais.
* - Este processo somente poderá ser realizado no RM Vitae.

**Atenção**

Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros | Segurança | Perfis | Pasta Acesso a Menus.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Identificação Alteração de dados funcionais progressivo

|  |  |
| --- | --- |
|  | Como Fazer |

---

Concluir Requisição
