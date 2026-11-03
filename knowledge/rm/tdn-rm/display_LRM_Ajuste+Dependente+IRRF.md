---
content_hash: fcf0b0e8c37183994894cc4d1d0a20ceae1c5d32f85a5e25a2430b0f8b1cf60b
fetched_at: '2026-06-29T00:10:42.884206+00:00'
page_id: '547865828'
product: rm
source: tdn-rm
title: Ajuste Dependente IRRF
type: documentation
url: https://tdn.totvs.com/display/LRM/Ajuste+Dependente+IRRF
version: 42
---

## **ÍNDICE**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01.****VERSÕES**

* 12.1.25.276
* 12.1.26.223
* 12.1.27.178

## **02.****VISÃO GERAL**

Esse processo irá ajustar a incidência de IRRF dos dependentes afetados pela inconsistência da Liberação de Competência existente nos patches:  
  
•   12.1.25.269 a 12.1.25.273  
•   12.1.26.214 a 12.1.26.220  
•   12.1.27.169 a 12.1.27.175  
  
Caso a competência tenha sido liberada em patches posteriores aos mencionados, não é necessária a execução desse processo.

IMPORTANTE

* As versões que apresentaram a inconsistência já foram removidas da Central de Downloads.
* Caso exista algum backup anterior a liberação de competência, aconselhamos atualizar a versão para uma que não exista a inconsistência para conferência dos registros após execução do processo liberado.

Nas versões citadas acima, existe inconsistência na atualização de dependente de IRRF através do processo de liberação de competência, ocorrendo somente quando o dependente tem o grau de parentesco "1-Filho Valido" ou "3-Menor Pobre". Para estes casos, o sistema desmarcou a incidência de IRRF no Cadastro do Dependente, mesmo quando a idade do dependente era inferior a 22 anos ou inferior a 25 anos e era universitário.

Para realizar os ajustes nesses dependentes, foi criado o processo de **Ajuste de Dependentes IRRF**.  Este processo irá fazer a comparação entre:

* o valor do campo "Nro. Dependente IRRF" da competência anterior (Funcionários | Anexo | Históricos de Dependentes)
* a quantidade de dependentes que possuem o grau de parentesco igual "1-Filho Valido" e "M-Menor Pobre". (Funcionários | Anexo | Dependentes)
* a quantidade de dependentes que NÃO incide IRRF, que possuem o grau de parentesco igual "1-Filho Valido" e "M-Menor Pobre" e a idade do dependente é inferior a 22 anos ou inferior a 25 anos e é universitário.

Caso as três quantidades obtidas acima sejam iguais, o sistema irá realizar de forma automática a atualização (marcar a incidência de IRRF em todos os dependentes que deveriam estar incidindo).

Para os casos que existirem diferenças, será exibido um grid no processo para que o usuário possa tomar a decisão de quais os dependentes devem ter ou não a incidência marcada.

**OBSERVAÇÃO:**

* O processo irá realizar a alteração no cadastro de funcionário sendo: Dependentes (campo PFDEPEND: INCIRRF), Históricos de Dependentes (PFHSTNDP: NRODEPENDIRRF) e no campo "Nro. Dep. IRRF" (campo PFUNC: NRODEPIRRF).

FIQUE ATENTO!

Esse processo ficará disponível somente nas versões 12.1.27, 12.1.26 e 12.1.25, isso porque a partir da versão 12.1.28 não há essa inconsistência.

## **03. EXEMPLO DE UTILIZAÇÃO**

1true2ParametrizaçãoParametrização

Acesse o menu Serviços Globais | Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 11.09 Ajustes

3Ajustes de Dependentes IRRFRetificação do 13° Salário23-1ProcessoCalculo

Acesse o menu RH | Folha de Pagamento | Configurações | Ajustes

Selecione as Coligadas que deseja realizar as alterações; Clique em avançar.

Ao clicar em Avançar, é realizado a validação internamente e retornado os funcionários que deveriam ter a incidência de IRRF, porém o Usuário terá quer realizar a conferencia e tomar a decisão. Por padrão todos já estão marcados, caso o usuário identifique algum funcionário que não deve ter incidência em IRRF basta desmarcar o mesmo da listagem e clicar em avançar.

Ao finalizar o processo é apresentado o Log com todas as chapas alteradas Manualmente e Automaticamente

## **04. TABELAS UTILIZADAS**

* PFUNC, PFDEPEND, PFHSTNDP.

]]>
