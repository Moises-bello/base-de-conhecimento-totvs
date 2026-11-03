---
content_hash: 30178994ab48b33658b762e37df0c03998be41f8fce542fa2dd921e995ad8b3b
fetched_at: '2026-06-29T00:05:56.568521+00:00'
page_id: '152801235'
product: rm
source: tdn-rm
title: COMO FAZER - Cópia de Registros Entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152801235
version: 2
---

**Produto: RM Labore**

Processo: Cópia de Registros Entre Coligadas

Versão: 11.5X ou superior

**Atenção:**

Alguns módulos do sistema obrigatoriamente necessitam de seguir uma ordem na cópia de registro entre suas coligadas. O roteiro abaixo deverá ser seguido, quando o usuário utilizar a opção "Copiar todos os Registros".

Será necessário criar um filtro que busque todos os registros, exceto aqueles que estão cadastrados na coligada 0, isto porque a coligada 0 é global, portanto um registro que está cadastrado para a mesma, está cadastrado para todas as demais. Veja exemplo de filtro abaixo:

1 - Copie as tabelas de cálculos para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastros -> Cálculos -> Tabelas de cálculo

Menu .Net: Administração de Pessoal -> Cálculos -> Tabelas de cálculo

2 - Copie as tabelas dinâmicas para a coligada destino através do ícone "Copiar Registro entre Coligadas"

Menu Delphi: Cadastros -> Tabelas dinâmicas

Menu .Net: Administração de Pessoal -> Cadastros globais -> Tabelas dinâmicas

3 - Copie as fórmulas para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastros -> Fórmulas

Menu .Net: Administração de Pessoal -> Fórmulas

4 - Copie o plano de contas para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastros -> Contabilização -> Plano de contas contábeis (RM Labore)

Menu Delphi: Cadastros -> Contabilização -> Plano de contas gerenciais (RM Labore)

Menu Delphi: Cadastros -> Contabilização -> Plano de contas contábeis (RM Saldus)

Menu Delphi: Cadastros -> Contabilização -> Plano de contas gerenciais (RM Saldus)

5 - Copie o Historico padrão para a coligada destino através do ícone "Copiar Registro entre Coligadas"

Menu Delphi: Cadastro -> Contabilização -> Historico padrão

Menu .Net: Encargos -> Cadastros -> Historico padrão

Obs. O passo 5A só deverá ser realizado, caso o usuário utilize o parâmetro "Cálculo por centro de custo" e os eventos seguem algum rateio. (campo "segue rateio por evento" preenchido da tabela eventos)

5A - Copie o rateio de eventos para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastro -> Rateio de Eventos

Menu .Net: Administração de pessoal -> Eventos -> Rateio de Eventos

6 - Copie os eventos para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastros -> Eventos

Menu .Net: Administração de pessoal -> Eventos -> Eventos

Obs. O passo 7 só deverá ser realizado caso o passo anterior tenha sido executado, ou o campo "Evento pra diferença" (no módulo de eventos) estiver selecionado.

7 - Copie os eventos novamente marcando agora na a opção "Sobrepõe o registro do destino".

Menu Delphi: Cadastros -> Eventos

Menu .Net: Administração de pessoal -> Eventos -> Eventos

**Atenção:**

Se o usuário fizer a cópia de registro em ordem inversa poderá ocorrer erros de chave estrangeira violada.

**Exemplo:**  
Na tabela Eventos existe o campo "Fórmula Valor" e se caso o usuário copiar primeiro os eventos e as fórmulas ainda não foram copiadas ocorrerá o erro de chave estrangeira violada. Portanto a ordem acima deverá ser respeitada para que assim não ocorra este tipo de erro. Na cópia de EVENTOS utilizando os passos 5 , 6 e 7 poderá ocorrer o erro de chave estrangeira violada. Esta mensagem de erro será normal, pois o usuário deverá seguir os passos 6 e 7 para que obter sucesso na cópia de registro de uma coligada para outra.

8 - Copie os sindicatos para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastros -> Sindicatos

Menu .Net: Administração de pessoal -> Sindicatos

9 - Copie os Valores Fixos para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastros -> Cálculos -> Valores fixos

Menu .Net: Administração de pessoal -> Cálculos -> Valores fixos

10 - Copie os Encargos Contábeis para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastros -> Contabilização -> Encargos contábeis

Menu .Net: Encargos -> Cadastros -> Encargos

11 - Copie as Tarifas de Transportes para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastros -> Tabelas auxiliares -> Tarifas de transporte

Menu .Net: Administração de pessoal -> Tarifas de transporte

12 - Copie as Linhas de Transportes para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Menu Delphi: Cadastros -> Tabelas auxiliares -> Linhas de transporte

Menu .Net: Administração de pessoal -> Linhas de transporte

13 - Copie os códigos de Acordo Coletivo / Reajuste por Lei para a coligada destino através do ícone "Copiar Registro entre Coligadas".

eSocial  - > Acordo Coletivo / Reajuste por Lei

**Atenção:**  
Certifique-se que as Tarifas de Transportes tenham sido copiadas corretamente ou que na coligada destino existam as mesmas tarifas cadastradas nas linhas de transporte para a cópia correta, caso contrário a coligada destino ficará inconsistente.

Roteiro para cópia de registros entre coligadas  
Alguns módulos do sistema obrigatoriamente necessitam de seguir uma ordem na cópia de registro entre suas coligadas.  
O roteiro abaixo deverá ser seguido, quando o usuário utilizar a opção "Copiar todos os Registros":  
Passo 1:  
Copie as tabelas de cálculos para a coligada destino através do ícone "Copiar Registro entre Coligadas".  
Passo 2:  
Copie as tabelas dinâmicas para a coligada destino através do ícone "Copiar Registro entre Coligadas".  
Passo 3:  
Copie as fórmulas para a coligada destino através do ícone "Copiar Registro entre Coligadas".

Passo 4:

Copie Acordo Coletivo / Reajuste por Lei para a coligada destino através do ícone "Copiar Registro entre Coligadas".  
Passo 5:  
Copie o plano de contas para a coligada destino através do ícone  
"Copiar Registro entre Coligadas".  
Passo 6:  
Copie o Historico padrão Localizado em  
Cadastro\Contabilização\Historico padrão para a coligada destino  
através do ícone "Copiar Registro entre Coligadas".  
O passo 6A só deverá ser realizado, caso o usuário utilize o  
parâmetro "Cálculo por centro de custo" e os eventos seguem  
algum rateio. (campo "segue rateio por evento" preenchido da  
tabela eventos)  
Passo 6A:  
Copie o rateio de eventos para a coligada destino através do  
ícone "Copiar Registro entre Coligadas".  
Passo 7:  
Copie os eventos para a coligada destino através do ícone "Copiar Registro entre Coligadas".  
O passo 7 só deverá ser realizado caso o passo anterior tenha sido executado, ou o campo "Evento pra diferença" (no módulo de eventos) estiver selecionado.  
Passo 8:  
Copie os eventos novamente marcando agora na a opção "Sobrepõe o registro do destino".  
Observação:  
Se caso o usuário fizer a cópia de registro em ordem inversa poderá ocorrer erros de chave estrangeira violada.  
Exemplo:  
Na tabela Eventos existe o campo "Fórmula Valor" e se caso o usuário copiar primeiro os eventos e as fórmulas ainda não foram copiadas ocorrerá o erro de chave estrangeira violada. Portanto a ordem acima deverá ser respeitada para que assim não ocorra este tipo de erro. Na cópia de EVENTOS utilizando os passos 5 , 6 e 7 poderá ocorrer o erro de chave estrangeira violada. Esta mensagem de erro será normal, pois o usuário deverá seguir os passos 6 e 7 para que obter sucesso na cópia de registro de uma coligada para outra.  
Passo 9:  
Copie os sindicatos para a coligada destino através do ícone "Copiar Registro entre Coligadas".  
Passo 10:  
Copie os Valores Fixos para a coligada destino através do ícone "Copiar Registro entre Coligadas".  
Passo 11:  
Copie os Encargos Contábeis para a coligada destino através do ícone "Copiar Registro entre Coligadas".  
Passo 12:  
Copie as Tarifas de Transportes para a coligada destino através do ícone "Copiar Registro entre Coligadas".  
Passo 13:  
Copie as Linhas de Transportes para a coligada destino através do ícone "Copiar Registro entre Coligadas".  
Atenção:  
Certifique-se que as Tarifas de Transportes tenham sido copiadas corretamente ou que na coligada destino existam as mesmas tarifas cadastradas nas linhas de transporte para a cópia correta, caso contrário a coligada destino ficará inconsistente.
