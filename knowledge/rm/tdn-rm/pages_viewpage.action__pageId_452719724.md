---
content_hash: 1012c11b807a5be7007afad7a2c38d6fc18c83219e879953a0701a775ebb3483
fetched_at: '2026-06-29T00:10:09.898818+00:00'
page_id: '452719724'
product: rm
source: tdn-rm
title: Cálculo de Beneficíos de Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719724
version: 3
---

O cálculo dos benefícios lançados no RM Vitae será feito no RM Labore através da interface Cálculo de Benefícios dos Funcionários disponível no Menu Rotinas - Cálculo de Benefícios dos Funcionários.  
Nesta tela o usuário poderá selecionar os benefícios a serem calculados e utilizar a seleção de funcionários caso deseje calcular somente para alguns funcionários. A data limite deverá ser informada e corresponde a data de referência para realizar o cálculo conforme o período do lançamento no Assistente de Lançamento do RM Vitae. A data Limite sempre deverá estar dentro da competência atual do sistema.

**Lançando os benefícios para o envelope do funcionário**

Para lançar os benefícios para o envelope do funcionário, o usuário deverá acessar a tela de Grupo de Eventos disponível no Menu Movimento – Folha de Pagamento – Lançamentos Automáticos – Grupo de Eventos e selecionar:  
A opção "Lançar eventos da Integração com Outros Aplicativos"   
O comportamento: A (Adicionar), I (Ignorar) ou S (Substituir)  
Na Aba "Integração com os Outros Aplicativos" marcar o Tipo de lançamento correspondente aos benefícios a serem calculados. No cadastro de Benefícios do RM Vitae o Tipo de Lançamento é informado pasta "Parâmetros de Cálculo".  
Observação: Se o benefício a ser calculado for obrigatório e não existir lançamento para o mesmo no RM Vitae, o sistema exibirá uma mensagem informando que não é possível realizar o cálculo.

**Observações:**

1. Em versões anteriores , o sistema gerava os dois eventos (funcionário  e empresa) independente da fórmula de percentual ser informada.  Atualmente só é lançado evento para a empresa e funcionário quando os eventos estão vinculados a um benefícios e este possui fórmula de percentual  que determina o valor que será lançado para cada evento sendo que o valor do percentual é aplicado para o evento empresa e a diferença lançada para o funcionário.
2. Ao selecionar um funcionário no filtro e realizar o cálculo do mesmo somente os benefícios dos funcionários selecionados no filtros serão removidos e recalculados.
3. Ao marcar o parâmetro '**Atualizar Benefício Selecionado**', disponível em**RH | Gestão de Pessoas | Configurações |  Parametrizador | Configurações | Benefícios**, o sistema irá incluir ou substituir  somente o benefício selecionado sem impactar nos benefícios que já haviam sido calculados.
