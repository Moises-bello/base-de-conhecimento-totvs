---
content_hash: 3e1fe88399aa4926671137e5a854fb4bbca7f6cbdc53c3afc256977a440266f9
fetched_at: '2026-06-29T00:10:52.331900+00:00'
page_id: '572011740'
product: rm
source: tdn-rm
title: Preferências do usuário na parametrização da rotina EFD ICMS IPI "SPED Fiscal"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572011740
version: 12
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

No formulário do SPED Fiscal foi adicionado a opção "Gravar Preferências do Usuário", com esta opção habilitada serão salvos todos os parâmetros definidos na execução do processo, e na próxima vez em que for executado os parâmetros serão carregados novamente automaticamente.

Disponível a partir da biblioteca 12.1.29 e 12.1.31.

## **02. EXEMPLO DE UTILIZAÇÃO**

Marcar a flag "Gravar Preferências do Usuário":

Imagem

Preencher e salvar as parametrizações, e executar a rotina.

Imagem

  

Após abrir a rotina de SPED Fiscal novamente as preferências estarão salvas de acordo com a última execução salva [[1]](https://tdn.totvs.com/pages/viewpage.action?pageId=572011740#_ftn1).

Nota

###### [[1]](https://tdn.totvs.com/pages/viewpage.action?pageId=572011740#_ftnref1) As parametrizações serão gravadas e carregadas por coligada e usuário.

###### Exemplo por coligada:

###### Usuário [X] ao executar a rotina na coligada 1 teve as parametrizações salvas apenas para esta coligada e ao abrir o processo novamente as parametrizações serão carregadas apenas para esta coligada.

###### Se ele trocar para a coligada 2 as parametrizações feitas serão salvas e carregadas apenas para esta coligada, ou seja, o que foi salvo na coligada 1 não influencia a coligada 2.

###### Exemplo por usuário:

###### Usuário [X] executou a rotina na coligada 1 e as parametrização foram salvas. Quando o usuário [Y] logar no sistema na coligada 1 as preferências salvas para o usuário [X] não serão carregadas para o usuário [Y].
