---
content_hash: 15dc8878ccae298b7e8b711181f662ece9e904c53b815bcbe02e99ddfd4541a5
fetched_at: '2026-06-29T00:10:08.103593+00:00'
page_id: '452719511'
product: rm
source: tdn-rm
title: Rateio Tomadores
type: documentation
url: https://tdn.totvs.com/display/LRM/Rateio+Tomadores
version: 4
---

No anexo de rateio de tomadores de serviços serão cadastradas as informações das empresas Tomadoras de Serviço. As informações dos Tomadores de Serviço serão prestadas nos arquivos com Códigos de Recolhimento que exigirem informações de tomadores de serviços (Exemplo: 130, 150, 155, 327 e 608). Para os funcionários que trabalharam em Tomadores de serviço a movimentação do funcionário deverá ser informada proporcionalmente aos dias trabalhados em cada Tomador de Serviço.   
   
**Exemplo**:  
O Funcionário trabalhou 14 dias na Empresa, 10 dias no Tomador 1 e 06 dias no tomador 2.  
Os dados deverão ser informados da seguinte forma:   
Cód.Tomador   Nome do Tomador                  Valor  
0001                   Tomador 1                              10  
0002                   Tomador 2                               6  
   
Considerando o mês comercial (30 dias). Os demais dias serão considerados como trabalhados na Empresa. Estas informações serão utilizadas no momento da distribuição dos valores dos eventos por Tomador de Serviço.  
   
**Atenção:**  
Se o funcionário sempre trabalha 30 dias no mesmo tomador de serviço não será necessário dar manutenção no cadastro de funcionário, pois este cadastro é mantido mesmo após a geração do SEFIP e liberação de competência. A distribuição é necessária para a movimentação do mês em que o funcionário trabalhou para vários tomadores de serviço em dias diferentes.  
   
Quando é inserido um tomador no Rateio tomadores somente será atualizado o calculo interno de Saldo a ratear após salvar, na visão (Pasta Identificação), todas as inserções de tomadores de serviços.

No campo competência final cadastre a data fim da validade do rateio para este funcionário, este campo poderá ser deixado em branco.  
   
No Campo Tomador só apresentará Clientes/Fornecedores ativos e tomador de serviços folha. Para isto, os campos "Ativo" e "Tomador de serviços folha" em Cadastros de Clientes/Fornecedores deverão estar marcados.   
   
Em caso de a coligada possuir licença de uso do Sistema de Controle Financeiro Gestão Financeira e nos parâmetros do Gestão Financeira, item "Parâmetros Lançamentos", estiver desmarcado o parâmetro "Permite Globais", não será possível associar em campos de cadastros do Folha de Pagamento, Cliente/Fornecedor que foram cadastrados como "Global".  
   
É possível escolher o tomador de serviço pelo nome ou nome fantasia, além de outros de acordo com o filtro ao lado o campo Nome.  
   
Marcar o tipo de tomador de serviço, ou seja, se o tomador de serviço é um prestador de serviços ou uma construção civil. Para as empresas que cedem somente mão-de-obra específica como prestação de serviço ou apenas para construção civil deve marcar o parâmetro somente em Parâm.de Cálculo do sistema. Este parâmetro serve para o relatório do SEFIP ser gerado de acordo com o recolhimento.  
   
**Exemplo:**  
Se um funcionário trabalhou na Empresa "Construtora X" em alguma obra civil "Tomador 1" por 10 dias e este mesmo funcionário trabalhou na limpeza "Tomador 2" por 15 dias.  
O usuário deve marcar:

* Em Parâm.de Cálculo do sistema "Construção civil" para gerar os administrativos;
* Em Clientes/Fornecedores "Tomador 1" como "Construção civil" ou não marcar nada que será considerado o parâmetro marcado em Parâm.de Cálculo do sistema;
* E em "Tomador 2" como "Cessão de mão-de-obra".
* Distribuir e gerar o SEFIP.

Para o código de recolhimento 150 será gerado os 15 dias trabalhados para o "Tomador 2" marcando "Não" para "gera administrativos" e o código de recolhimento 155 será gerado com os 10 dias do "Tomador 1" e os 05 dias da parte do administrativo da "Empresa cedente" marcando "Sim" para "gera administrativos".  
   
O sistema funcionará da seguinte forma na verificação do Tipo de tomador de serviços:  
   
1.    Marcando somente o parâmetro "Tipo de tomador default" em Parâm.de Cálculo do sistema será gerado normalmente o arquivo SEFIP.RE considerando todos os tomadores de serviço de acordo com a opção marcada.  
2.    Marcando o parâmetro "Tipo de tomador default" em Parâm.de Cálculo do sistema e o parâmetro "Tipo de tomador" em Cadastros de Clientes/Fornecedores será considerado para empresa cedente o parâmetro em Parâm.de Cálculo do sistema e para os tomadores de serviços o parâmetro marcado em Cadastros de Clientes/Fornecedores.  
3.    Marcando o parâmetro "Tipo de tomador default" em Parâm.de Cálculo do sistema, o parâmetro "Tipo de tomador" em Cadastros de Clientes/Fornecedores e o parâmetro "Tipo de Tomador" em Cadastros de Funcionários no Anexo Rateio Tomadores será considerado para empresa cedente o parâmetro em Parâm.de Cálculo do sistema e para os tomadores de serviços o parâmetro marcado em Cadastros de Funcionários no Anexo Rateio Tomadores.  
   
**Atenção:**  
Esta parametrização somente será validada para as empresas que estão caracterizadas como FPAS 507, pois o validador da CEF não valida o código de recolhimento 155 com FPAS 515.  
   
**Observação:**  
Para ativar o flag "Enviar Informações Para o PPP", é necessário habilitar a integração do Labore com o Vitae. Para isso vá em Ambiente | Parâmetros | Integrações de Sistemas, localize onde o Sistema 1 é Labore e o Sistema 2 é Vitae, edite e marque o flag de Integrado. Após isso será necessário reiniciar o Host do Sistema e então o Flag será habilitado.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
