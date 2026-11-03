---
content_hash: ee96ce259107c0cdda09c71685e11637878339d182841cf4a0e7aac96f9f273f
fetched_at: '2026-06-29T00:10:04.784048+00:00'
page_id: '452719251'
product: rm
source: tdn-rm
title: Lançamento de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719251
version: 3
---

Este processo tem o objetivo em lançar os eventos do Recibo de Férias para o envelope de pagamento do funcionário e alterar a situação do funcionário de 'A-Ativo ' para 'F-Férias '.  
Para isso, é imprescindível o cadastramento do 'Evento para Pagamento de Licença Remunerada' e do ' Motivo de Afastamento por Licença Remunerada' existente em Configurações | Parametrizador | Férias | Férias Coletivas.  
    
É possível lançar as férias para a próxima competência, para isso deve marcar o parâmetro e informar o período desejado.   
    
É permitido o lançamento de mais de umas férias no mesmo envelope de pagamento (período), quando o caixa de pagamento das férias é igual.   
O sistema soma os valores dos eventos e assume a data de pagamento do último lançamento.  
   
Quando o caixa é diferente é apresentada a mensagem: 'Funcionário XXXX possui férias lançadas neste período, com mês caixa diferente. As novas férias deverão ser lançadas em outro período do envelope. '   
   
**Observação:**  
Esta implementação se fez necessária para que o IRRF, DIRF e Informe de Rendimentos fiquem corretos.  
   
É gravado o histórico de situação de férias, para isso é necessário informar o motivo de início e retorno   
Configurações | Parametrizador | Férias | Mudança da Situação  
   
 Abono  
Somente a média do abono é lançada discriminada, isso porque não existe a possibilidade do abono ser partido, já as férias existe, e devido existir código de cálculo específico para a média de abono.   
   
Quando o funcionário tem somente abono pecuniário calculado, é utilizada a data de pagamento para verificar o período informado na tela. Os eventos são lançados para o envelope de pagamento, porém a situação do funcionário continua 'A-Ativo'.  
   
Pensão Alimentícia de Férias  
A pensão alimentícia de férias, código de cálculo 113, não tem seu valor recalculado no lançamento.  
   
**Atenção I:**  
Os eventos de férias do envelope devem ter as mesmas incidências dos eventos do recibo, ou seja, incidindo em pensão de férias e IRRF de férias.  
Para que, caso o funcionário seja demitido no mês do gozo das férias, os eventos do gozo de férias sejam somados aos eventos de férias na rescisão e abata a pensão já descontada no gozo das férias.   
   
**Atenção II:**  
O código de cálculo '113-PENSÃO ALIMENTÍCIA SOBRE FÉRIAS' é utilizado apenas no cálculo do recibo de férias.   
Para calcular a pensão sobre as férias da rescisão é utilizado o código de cálculo '319- PENSÃO ALIMENTÍCIA FÉRIAS NA RESCISÃO'.   
   
**Atenção III:**  
Para o cálculo da pensão alimentícia no recibo de férias, a base de cálculo é composta pelos eventos do recibo de férias mais os eventos que estão na PFFINANC (eventos que incidem em Pensão de Férias).  
Porém para deduzir o valor da pensão já pago (quando o funcionário tem mais de um recibo de férias no mesmo mês) o valor da pensão do outro recibo de férias somente é verificado quando a situação de férias é 'P-Pagas', 'F-Finalizadas' ou 'X-Finalizadas Próximo Mês'.  
   
**Atenção IV:**  
Sempre que a data de pagamento do recibo de férias atual é alterada, ao salvar, o campo 'Data Pagto Férias' do movimento da pensão é atualizado.  
   
**Atenção V:**  
O campo 'Período' do movimento da pensão é atualizado com o período do lançamento das férias.

O campo 'Situação das Férias' é preenchido conforme abaixo:  
G – Aguardando Aprovação do Gestor (quando o subordinado cadastra a sugestão de férias);  
D – Aguardando Aprovação do DP (quando o gestor aprova a sugestão e não tem permissão de marcar férias);  
M – Marcadas (quando o DP aprova ou quando o gestor tem permissão para marcar);  
P – Pagas (quando calcula as férias e as mesmas são lançadas na movimentação);  
F – Finalizadas (quando fecha o período aquisitivo e abre outro período aquisitivo, independente de ser um novo ou o mesmo);  
X - Finalizadas para o próximo mês (quando é processada a finalização de férias para a próxima competência. Na liberação de competência este campo é alterado para F – Finalizadas).

**Observação:**

Caso o parâmetro '**Não calcula Recibo de Férias**', disponível em **RH | Administração de Pessoal | Funcionários | Informações para o Cálculo | Parâmetros**, esteja 'marcado', o sistema não irá calcular o recibo de férias para o funcionário e também não serão exibidos no cadastro de férias o campo 'Data Pagamento' e os botões de 'Calcular' e 'Visualizar Recibo' de férias.

A mudança da situação do funcionário para 'Férias', continuará sendo feito pelo processo 'Lançar' férias'.

O processo 'Finalizar' férias vai mudar a situação do funcionário de 'Férias' para 'Ativo' e atualizar os dados cadastrais do período aquisitivo de férias.

O sistema não irá consistir na Liberação de Competência se constam no envelope do funcionário os códigos de cálculo específicos de férias para funcionários com o parâmetro marcado.

Local de Chamada

Processo Férias | Lançamento

Funcionário | Movimento | Férias | Processo Lançar
