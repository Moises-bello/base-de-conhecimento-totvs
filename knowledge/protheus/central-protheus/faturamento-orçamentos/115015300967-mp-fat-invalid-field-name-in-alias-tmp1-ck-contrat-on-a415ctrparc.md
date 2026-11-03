---
article_id: 115015300967
category: Faturamento - Orçamentos
content_hash: e745148f05951600a76feb85b5016ed940d4c450595d1c124ed34e8d70b674ad
fetched_at: '2026-06-28T22:38:25.004215+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: MP-FAT-Invalid field name in Alias TMP1->CK_CONTRAT on A415CTRPARC
type: support-article
updated_at: '2021-04-28T15:15:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015300967-MP-FAT-Invalid-field-name-in-Alias-TMP1-CK-CONTRAT-on-A415CTRPARC
---

**Ocorrência**   
  
Ao alterar o orçamento gera o erro :invalid field name in Alias TMP1->CK\_CONTRAT on A415CTRPARC(MATA415.PRX)   
  
**Causa**  
  
A tabela temporária que esta gerando o incidente é montada com base nos campos da SCK e por algum motivo o campo não ficou disponível para query, geralmente essa situação, que pode acontecer em três situações, veja abaixo:  
  
1-O campo não está como 'Usado'  
2- O campo não está disponível para utilização de todos os módulos  
3- Nível do Campo  
  
**Ambiente**  
  
Microsiga Protheus - versão 11 e versão 12  
  
**Solução**  
  
Para solucionar :  
  
  
1- Se campo não está marcado como usado, vá no Configurador, e valide se  o campo  CK\_CONTRAT está marcado como usado, caso não esteja, marque-o como usado, salve a tabela e depois atualize o dicionário de dados.

2 - Se o problema estiver relacionado a marcação do uso do campo por todos os módulos, vá no Configurador, acesse a tabela SCk, localize o campo CK\_CONTRAT, edite-o e vá até a aba módulos, e selecione a opção utilizado por todos os módulos. Salve a de se  o campo  tabela e depois atualize o dicionário de dados.  
  
3 - Se o problema estiver relacionado ao nível do campo,é preciso avaliar se o nível de campo é  superior ao nível do usuário/menu,pode ocasionar o problema e neste caso altere o nível de campo e mantenha para o nível padrão do campo que é 1. Salve a tabela e depois atualize o dicionário de dados.  
  
Obs: Nesta rotina também existe o ponto de entrada 'M415NCPO' que pode inibir campos da tabela SCK, verifique se não esta utilizando este P.E.<http://tdn.totvs.com/pages/viewpage.action?pageId=102924503>  
Caso não saiba efetuar o processo no configurador, solicite apoio a equipe de framework.
