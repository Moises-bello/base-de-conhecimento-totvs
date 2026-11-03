---
content_hash: fa7779a74875b48c796ff60ad43dc396ab83928065a227f0e40061c9c08eb8b2
fetched_at: '2026-06-29T00:10:01.444946+00:00'
page_id: '452718736'
product: rm
source: tdn-rm
title: Efetivar Transferência com Alteração de Dados Funcionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718736
version: 2
---

**Efetivar Transferência com Alteração de Dados Funcionais**

A Efetivação da Transferência com Alteração de Dados Funcionais tem por objetivo possibilitar a conclusão deste tipo de requisição através do processo "Concluir Requisição". Ao executar o processo "Concluir Requisição", a requisição terá seu status alterado para "Concluída" e os dados do funcionário selecionado serão atualizados de acordo com os dados propostos na requisição. Caso a requisição esteja vinculada a uma requisição "pai" essa também será concluída, sendo a requisição "pai" de aumento de quadro, essa será concluída se todas as vagas aprovadas tiverem sido utilizadas.  
   
Ao executar o processo "Concluir Requisição", e a requisição possuir progressões relacionadas, o sistema terá o seguinte comportamento:

- Possuindo apenas uma progressão, o processo irá efetivar a progressão e também irá concluir a requisição.

- Possuindo mais de uma progressão, o processo irá efetivar apenas a próxima progressão e não irá concluir a requisição, pois a requisição só pode ser concluída depois de todas as progressões efetivadas. No caso de ser a última progressão, o processo irá efetivar a progressão e também irá concluir requisição.

Como forma de acompanhamento dos processos relacionados à requisição serão enviados e-mail´s com mensagens padronizadas, podendo ainda optar-se pela notificação ao gestor de RH e ao gestor do departamento pessoal.

Todo o processo de notificação poderá ser parametrizado no aplicativo, para isto verifique em Opções | Parâmetros | RM Vitae | Geral | Pasta "Requisições".

**Atenção**

Requisições de transferência com alteração de dados funcionais que dependam de alteração de CNPJ somente podem ser efetivadas através do processo de rescisão do funcionário.

* Caso a parametrização do sistema esteja por Gestão de Hierarquia por Posição ao concluir a rescisão de um funcionário que ocupe posição de liderança, a vigência do líder será encerrada e a data final da vigência será atualizada de acordo com a data da rescisão.

**Observação**

- Somente podem ser concluídas pelo processo "Concluir Requisição" as requisições aprovadas de transferência com alteração de dados funcionais. As requisições que solicitem a transferência da vaga podem incrementar o limite de vagas da lotação de destino, conforme as configurações do controle de lotação.

- Este processo somente poderá ser realizado no RM Vitae.  
   
**Atenção** Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros | Segurança | Perfis | Pasta Acesso a Menus.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Identificação Transferência com alteração de dados funcionais progressivo

|  |  |
| --- | --- |
|  | Como Fazer |

---

Concluir Requisição
