---
article_id: 360022410352
category: RH - CAGED
content_hash: 4f5de16993f6a2e7d4fa17e66e51a32bf6e340b3a38f9bad80f9900b767f5a56
fetched_at: '2026-06-28T22:43:33.039147+00:00'
product: protheus
section_id: 360010781674
source: central-protheus
title: RH - Linha Protheus - GPE - Não gera exame toxicológico no arquivo CAGED
type: support-article
updated_at: '2025-08-27T17:31:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022410352-RH-Linha-Protheus-GPE-N%C3%A3o-gera-exame-toxicol%C3%B3gico-no-arquivo-CAGED
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29401075930391)** **Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Não gera exame toxicológico no arquivo CAGED.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**Ocorre normalmente quando não preenche a data do Resultado ou a data informada é anterior a admissão e/ou posterior a demissão.  
  
**Solução**O toxicológico só será gerado se na **função** atrelada ao funcionário, o código do **CBO** for algum destes;

782310 - Motorista de furgão ou veículo similar;   
782320 - Condutor de ambulância;  
782405 - Motorista de ônibus rodoviário;   
782410 - Motorista de ônibus urbano;   
782415 - Motorista de trólebus;  
782510 - Motorista de caminhão (Rotas regionais e internacionais);  
782515 - Motorista operacional de guincho.

Será gerado para acertos de competência igual ou superior a **03/2016** ou inclusão igual ou superior a **09/2017;**

No **SIGAMDT**, faça as seguintes verificações:

1 - Em **Atualizações \ Cadastros Gerais \ Fornecedores** - Verifique se o Fornecedor possui CNPJ informado;

**2** - Em **Atualizações \ Atendimento Médico \ Ficha Médica**, verifique se a ficha está atrelada a Função e ao CBO correspondente, e se a data de implantação da ficha, está dentro da admissão do funcionário;

**3** - Em **Atualizações \ Atendimento Médico \ Médico Emit. Atestado** - verifique se o médico está com a função 1-Médico Trabalho, número de Emitente e UF preenchidos;

**4** - Em **Atualizações \ PCMSO \ Exames** - Verifique se existe o exame Toxicológico cadastrado, cujo os campos "Admissional", "Demissional" e "Ret. Trab" devem estar com **SIM**.

**5** - Em **Atualizações \ PCMSO \ Fornecedores Exames -** Verifique se existe o relacionamento do exame Toxicológico com o fornecedor;

**6** - Em **Atualizações \ PCMSO \ Exames do Func. -** Verifique se para a ficha Médica do funcionário, existe o exame amarrado, e os campos abaixo preenchidos:  
**Fornecedor****Origem - Assistencial****Função****CBO**  
**Cod. Denatran**  
**Médico**

Além desses campos, existem os campo **Data Exame** e **Data Resultado,** que devem estar preenchidos​, sendo que para os casos de Admissão, não pode ter conteúdo inferior a data de admissão do funcionário.

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)

Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento:

<https://www.youtube.com/watch?v=T7b4zMlphTI>
