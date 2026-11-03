---
article_id: 360029247774
category: Configurador
content_hash: 251cea42f450a3183e3edb3735e44a28c27b2d7cc835ddfdaad41221ca78e1ff
fetched_at: '2026-06-28T22:42:18.973278+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Configurar dias de troca da Data Base do Sistema
type: support-article
updated_at: '2024-05-08T11:38:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029247774-Framework-Linha-Protheus-Configurar-dias-de-troca-da-Data-Base-do-Sistema
---

**Dúvida**A Data Base do Sistema pode ser alterada em mais de um lugar. Qual é a regra de prevalência?  
   
 **Ambiente**Protheus - Configurador - A partir da versão 11  
   
**Solução**O conceito da configuração de dias de troca da data base é a seguinte:  
  
1. O usuário deve ter o **acesso 36** (Alterar Database do Sist.) habilitado, senão ele não poderá alterar a database do sistema  
  
![DTB_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042801473)  
  
A configuração de quantos dias pode-se avançar e retroceder a data base do sistema pode ser feita:  
- No **Cadastro do Usuário** (aba Parametrização)  
- No **Cadastro do Grupo** (aba Grupo > Parametrização)  
- Na **Política** (aba Outros > Parâmetros)  
  
2. Se no usuário, na aba ***Parametrização***, a opção **Configurar dias de troca da data base** estiver como **NÃO**, o sistema irá checar o que está configurado na **Política** (aba ***Outros***). Se na **Política** este campo também estiver como **NÃO**, é permitido alterar a data base sem limitação. Se na **Política** estiver como **SIM**, terá que configurar a quantidade de dias nos campos **Retroceder** e **Avançar**. Se deixar como 0, irá exibir uma mensagem que o usuário não pode retroceder ou avançar mais do que 0 dias.  
  
![DTB_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041960434)  
  
![DTB_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041960414)  
  
3. Se no usuário a opção **Configurar dias de troca da data base** estiver como **SIM**, a configuração que será respeitada é a do usuário, não a da **Política**. Neste caso, deve-se inserir o número de dias que ele pode avançar/retroceder, pois se deixar como 0, irá exibir uma mensagem de que o usuário não pode retroceder ou avançar mais do que 0 dias.  
  
![DTB_04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041960454)  
  
4. Se o usuário fizer parte de algum **Grupo**, essa configuração deve ser feita no **Grupo**  
  
![DTB_05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041960494)

|  |
| --- |
| **Informação:**  * Se um usuário faz parte de um grupo, a configuração de "Dias de Troca de Data Base" será considerada do **Grupo**, e não do **Usuário**. * Se a configuração no **Grupo** está como "Não", ainda assim não é considerada a configuração do **Usuário**, mas sim, a da **Política**. * Se o usuário fizer parte de algum **Grupo**, e a "Regra de acesso por grupo" estiver como "Priorizar" ou como "Somar", será considerada a configuração do **Grupo**. Se a "Regra de acesso por grupo" estiver como "Desconsiderar", será considerada a configuração do **Usuário**. * Quando o **Usuário** tiver mais de um grupo, a configuração de "Dias de Troca de Data Base" será considerada do grupo que estiver com a coluna Prioriza = **Sim**. Se nenhum grupo estiver com Prioriza = **Sim**, a configuração será considerada do **primeiro grupo** da listagem de grupos do usuário. |

Tabela de possibilidades:

| Regra de acesso por grupo | Grupo | Usuário | Política | Respeita configuração de: |
| --- | --- | --- | --- | --- |
| Sem grupo | Sem grupo | Configurar dias = Sim | Configurar dias = Sim | **Usuário** |
| Sem grupo | Sem grupo | Configurar dias = Não | Configurar dias = Sim | **Política** |
| Sem grupo | Sem grupo | Configurar dias = Sim | Configurar dias = Não | **Usuário** |
| Sem grupo | Sem grupo | Configurar dias = Não | Configurar dias = Não | **Alteração de data sem limite** |
| Priorizar/Somar | Configurar dias = Sim | Configurar dias = Sim | Configurar dias = Sim | **Grupo** |
| Desconsiderar | Configurar dias = Sim | Configurar dias = Sim | Configurar dias = Sim | **Usuário** |
| Priorizar/Somar | Configurar dias = Sim | Configurar dias = Sim | Configurar dias = Não | **Grupo** |
| Desconsiderar | Configurar dias = Sim | Configurar dias = Sim | Configurar dias = Não | **Usuário** |
| Priorizar/Somar | Configurar dias = Sim | Configurar dias = Não | Configurar dias = Sim | **Grupo** |
| Desconsiderar | Configurar dias = Sim | Configurar dias = Não | Configurar dias = Sim | **Política** |
| Priorizar/Somar | Configurar dias = Sim | Configurar dias = Não | Configurar dias = Não | **Grupo** |
| Desconsiderar | Configurar dias = Sim | Configurar dias = Não | Configurar dias = Não | **Alteração de data sem limite** |
| Priorizar/Somar | Configurar dias = Não | Configurar dias = Sim | Configurar dias = Sim | **Política** |
| Desconsiderar | Configurar dias = Não | Configurar dias = Sim | Configurar dias = Sim | **Usuário** |
| Priorizar/Somar | Configurar dias = Não | Configurar dias = Sim | Configurar dias = Não | **Alteração de data sem limite** |
| Desconsiderar | Configurar dias = Não | Configurar dias = Sim | Configurar dias = Não | **Usuário** |
| Priorizar/Somar | Configurar dias = Não | Configurar dias = Não | Configurar dias = Sim | **Política** |
| Desconsiderar | Configurar dias = Não | Configurar dias = Não | Configurar dias = Sim | **Política** |
| Priorizar/Somar | Configurar dias = Não | Configurar dias = Não | Configurar dias = Não | **Alteração de data sem limite** |
| Desconsiderar | Configurar dias = Não | Configurar dias = Não | Configurar dias = Não | **Alteração de data sem limite** |

Baseando-se na tabela acima, seguem abaixo alguns exemplos de cenários, e a configuração que deve ser feita:  
  
**Cenário 1:** Necessito configurar a data base do sistema para todos os usuários e grupos de uma única vez, Avançar e Retroceder configurados como 90 dias.  
>>> No menu **Política**, aba **Outros**, em **Configurar dias de troca da data base** selecione **Sim**, e nos campos **Retroceder** e **Avançar** digite **90**. Nos Usuários e Grupos deixe a opção **Configurar dias de troca da data base** selecionado como **Não**.  
  
**Cenário 2:** Necessito configurar a data base do sistema para um usuário especifico que pertence a um grupo, para Avançar e Retroceder até 90 dias. Os outros usuários desse Grupo podem Avançar e Retroceder até 30 dias, e o restante dos usuários do sistema não devem ter limitação de alteração da data base.  
>>> Crie um novo **Grupo**, sem nenhuma configuração (Filiais, Acessos, Ambientes, etc). Nesse grupo, defina a opção **Configurar dias de troca da data base** como **Sim**, e digite **90** nos campos **Retroceder** e **Avançar**.   
No cadastro deste usuário específico, utilize a **Regra de acesso por grupo** como **Somar**. Associe este novo grupo à listagem de grupos do usuário, e na coluna **Prioriza**selecione **Sim**. Desta forma este usuário irá seguir as regras de data base deste novo grupo, mas as definições de acessos dos demais grupos que faz parte.  
No grupo principal, que os usuários fazem parte, em **Configurar dias de troca da data base** deve estar selecionado **Sim**, com o valor **30** nos campos **Retroceder** e **Avançar**.  
Os demais usuários do sistema, que não fazem parte deste grupo, e que não tem configuração de **Configurar dias de troca da data base** no usuário ou no grupo ao qual pertençam, irão assumir a configuração da **Política**, que deve estar com a opção de **Configurar dias de troca da data base** como **Não**, para que a alteração seja ilimitada.  
  
**Cenário 3:** Necessito configurar a data base para todos os usuários de um grupo especifico para avançar e retroceder até 90 dias, os demais grupos serão ilimitados para alterar a data base  
>>> Neste grupo, em **Configurar dias de troca da data base** deve estar selecionado **Sim**, com o valor **90** nos campos **Retroceder** e **Avançar**. Nos demais grupos, em **Configurar dias de troca da data base** deve estar selecionado **Não**, e na **Política**, em **Configurar dias de troca da data base** também deve estar selecionado **Não**.  
  
**Cenário 4:** Necessito que um usuário que possui dois grupos tenha a seguinte configuração de data base nos grupos:  
Grupo 1: Avançar e Retroceder 90 dias  
Grupo 2: Avançar e Retroceder 30 dias  
>>> **Não** é possível configurar uma limitação diferente de **Avançar/Retroceder** data base do sistema dependendo do Grupo que é acessado. A configuração será considerada pelo **Grupo** que estiver priorizado.
