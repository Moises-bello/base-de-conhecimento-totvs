---
content_hash: 42b064354cbf211f26b31a89d6d741bca12cb02d5ce4bf2b7b6c990495c1fceb
fetched_at: '2026-06-29T00:11:17.474203+00:00'
page_id: '680967167'
product: rm
source: tdn-rm
title: Reajuste - Regras de configuração e comportamentos (Juros E CM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680967167
version: 26
---

Este documento tem por objetivo demonstrar as regras para a busca do valor base do cálculo de reajuste e a aplicação destes para os componentes que compõe as parcelas.

Importante!

O TCGI trabalha com dois momentos essencias para o entendimento da dinâmica do reajuste.

- primeiro momento é o cálculo do componente e a utilização do mesmo em todos os pontos que forem necessários.  
- segundo momento é a aplicação do valor encontrado no componente para a data determinada pelo campo "Data próximo reajuste" .

### Cenário 1:

Juros calculado sobre o valor principal somado ao CM acumulado até o mês anterior ao reajuste. Juros calculado mensalmente e correção monetária calculada anualmente.

**Configuração Juros**

Taxa de juros %: 1 (informe o valor do juros inteiro, utilizado para encontrar o valor do juros, que será calculado pelo sistema)  
Tipo de periodicidade: Mensal  
Tipo de juros: Simples  
Data base de referência para calculo do reajuste: Data da venda  
Data base: 01/01/2002  
Periodicidade: 1  
Dia vencimento resíduo: 0 (somente será utilizado para quando se utiliza calculo anual com resíduo)  
Data próximo reajuste: 01/02/2002 (valor preenchido pelo sistema)

- A data do próximo reajuste será preenchida pelo sistema seguindo a regra de data base informada no campo "Data base de referência para calculo do reajuste" mais o valor do campo "Periodicidade" e "Tipo de periodicidade"  
- O valor será atualizado para o próximo reajuste sempre que for atingido a data deste reajuste, para a próxima data de reajuste que o componente deverá ser calculado e o valor for aplicado.

Referência de entrega para o componente: Data entrega do empreendimento  
Aplicar reajuste em: Ambas(vincendas e vencidas)  
Calcular valor do juros sobre: Principal + [Periodo CM]

- Período CM: CM Acumulado até o mês anterior ao reajuste (campo habilitado em decorrência de o valor do campo "Calcular valor do juros sobre" selecionado ter referência ao [Período CM])

**Configuração Correção Monetária**

Moeda/Índice: INCC (Moeda cadastrada e abastecida mensalmente pelo usuário do sistema)  
Defasagem: 0  
Tipo: Índice acumulado  
Coeficiente: 0   
Aplicar coeficiente mensalmente: desmarcado  
Ignorar deflação: desmarcado  
Data base de referência para calculo do reajuste: Data da venda  
Data base: 01/01/2002  
Periodicidade: 1  
Dia vencimento resíduo: 0 (somente será utilizado para quando se utiliza calculo anual com resíduo)  
Data próximo reajuste: 01/02/2002 (valor preenchido pelo sistema)aplicacaoreajuste

- A data do próximo reajuste será preenchida pelo sistema seguindo a regra de data base informada no campo "Data base de referência para calculo do reajuste" mais o valor do campo "Periodicidade" e "Tipo de periodicidade"  
- O valor será atualizado para o próximo reajuste sempre que for atingido a data deste reajuste, para a próxima data de reajuste que o componente deverá ser calculado e o valor for aplicado.

Referência de entrega para o componente: Data entrega do empreendimento  
Aplicar reajuste em: Ambas(vincendas e vencidas)  
Calcular valor do juros sobre: Principal + [Periodo Juros]

- Período juros: Juros acumulado até o mês anterior ao reajuste (campo habilitado em decorrência de o valor do campo "Calcular valor do CM sobre" selecionado ter referência ao [Período Juros])

Pro rata dia: desmarcado  
Correção monetária capitalizada (correção sobre correção): marcado

CENÁRIO 1 - COMPORTAMENTO

Juros calculado sobre o valor principal (componente gerador de parcela) + período CM → período CM selecionado como "CM acumulado até o mês anterior ao reajuste"

### Juros Contratuais (JUROS)

* O valor do CM será apresentado e considerado para o cálculo do juros como parametrizado.   
  Isso ocorre porque foi selecionado que o CM é base do juros, então o valor do CM irá ser calculado para compor a base do juros.   
  No entanto, o valor do CM não será aplicado no componente de CM da parcela para o mês reajustado.   
  Ao visualizar o log da memória de cálculo, poderá ser visto o valor de CM que fez parte da base de calculo separadamente.

  Importante!

  Os reajuste deverão ocorrer todos os meses, caso seja efetuado o reajuste para uma data futura, como a data de aplicação do CM sem que se faça o reajuste de todos os meses do juros, o valor do juros a ser aplicado na parcela ficará com o do ultimo mês que ocorreu o reajuste do juros aplicado.

  Memória calculotrue

### Correção Monetária (CM)

* A correção monetária será calculada quando a data informada pelo usuário na tela de filtro do reajuste no campo "Data do Reajuste" no passo "Ações do Reajuste" do wizard for igual o valor do campo "Data próximo reajuste" do componente de CM.  
  O valor do Juros será calculado até o mês anterior e acumulado para compor a base junto com o componente principal, em seguida será calculado o valor do CM e aplicado para as parcelas nos próximos 12 meses. 

  Memória calculotrue

---

Para visualizar a memória de cálculo do reajuste deverá selecionar a parcela que se deseja verificar a memória de cálculo e clicar no ícone de lupa como demonstrado nas três visões de parcela abaixo:

Importante!

Caso o log esteja vazio, sem demonstrar a memória de cálculo, verifique a parametrização de armazenamento do histórico de alterações do financeiro, marque a opção e clique em executar:
