---
content_hash: 327902ef2cc60773946881a6f9e871c2feecf873184782761983971404927f78
fetched_at: '2026-06-28T21:35:30.916957+00:00'
page_id: '862608345'
product: fluig
source: tdn-fluig
title: ARQ - Como executar jobs em apenas uma instância do Fluig?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862608345
version: 11
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.8.1 ou superior

# Ocorrência

Duplicação dos *jobs* de tarefas intermediárias no  devido a uma inconsistência de concorrência específica de fluxos similares ao exemplificado abaixo:

**Sobre o fluxo:**

1 - A intermediária adiciona um agendamento.

2 - O agendamento é executado e envia para o *gateway*. Depois disso, o agendamento é removido.

3 - A condição do *gateway* volta para a intermediária.

# Causa

Ocorre uma inconsistência de concorrência ao tentar adicionar e remover um mesmo agendamento quando feito em múltiplas *threads* e com múltiplas instâncias do Fluig quando existem solicitações sendo executadas paralelamente.

# Solução

Existem duas possibilidades de solução para esse caso.

**→ Alterar o processo.**

* Em vez de adicionar uma condição no *gateway* para retornar para a atividade intermediária, adicione a mesma condição na intermediária e utilize o "*return false;*" para reagendar o agendamento sem que o sistema precise removê-lo.

**→ Limitar o agendamento para executar em apenas uma *thread* e uma instância.**

* Para isso, acesse o diretório **[diretório\_instalação]\repository\wcmdir\config** e verifique se existe o arquivo **configuration.properties**.

* Se existir, abra-o com um editor de texto e adicione os parâmetros abaixo com seus respectivos valores. Se os parâmetros já existirem, verifique se os valores são os indicados abaixo. Se não forem, é necessário alterá-los.

  javaconfiguration.properties
* Se o arquivo de configurações não existir, é necessário criá-lo manualmente com o nome **configuration** e a extensão **.properties**. Adicione os parâmetros acima e seus respectivos valores.

* Em seguida, reinicie os serviços do Fluig.

  Nota:

  Não se preocupe se o arquivo for excluído, pois a plataforma faz a leitura dele, atualiza a tabela "fdn\_paramgeral" e, em seguida, remove o arquivo automaticamente.

Dica!

Se desejar voltar o valor dos parâmetros para o padrão:

* Basta alterá-los para os indicados abaixo no arquivo **configuration.properties**.

  javaconfiguration.properties
* Reinicie os serviços do Fluig.
