---
content_hash: 9ea0e2891b4e36698e072e9198ad96a3566739f31c6c55a9338ea1824d3b3dde
fetched_at: '2026-06-29T00:09:28.141387+00:00'
page_id: '423938671'
product: rm
source: tdn-rm
title: Controle Plano de Contas Anterior (Registro I157)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938671
version: 10
---

**Foram mapeados dados pessoais ou sensíveis que estão de acordo com a Lei Geral de Proteção de Dados Pessoais. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei n° 13.709/2018.**

Neste cadastro deve ser selecionada a Forma de Escrituração criada anteriormente para a geração do SPED. Com esta informação, será possível verificar quais contas tiveram seus códigos alterados, informando qual o novo código a conta passou a receber.  
Através do menu : Processos | Identificar Contas do Plano de Contas Anteriores Automaticamente, será possível recuperar de forma automática as contas que não estão cadastradas no Plano de Contas Contábil atual.

O Tipo de Recuperação deste arquivo pode ser feito de duas formas:

**1. Recupera do arquivo do SPED Contábil do ano anterior**  
Nesta opção o sistema solicitará a importação do arquivo de Sped Contábil do ano anterior ao que está sendo gerado, através deste arquivo o sistema:

Identifica as contas contábeis do arquivo que não existem no plano de contas atual. - Identifica no último mês do registro I150 através do registro I155 o saldo final de todas as contas que não existem mais no plano de contas atual.  
Após a recuperação das informações o usuário deverá editar o cadastro e informar o campo Conta Atual, para que seja possível fazer um "de para" na geração do SPED Contábil.

**2. Recuperar do Histórico de Alteração do Código da Conta**  
Este processo identificará no Histórico de Alteração do Código da Conta todas as contas que tiveram o seu código alterado, sendo de responsabilidade do usuário as devidas conferências.  
Com a opção 'Limpar as contas cadastradas e recuperar tudo novamente' marcada, as contas já selecionadas na aba 'Contas Plano de Contas Anterior (Registro 157)' serão excluídas e inseridas novamente.

Campo Centro de Custo Anterior e Atual:

-Estes campos só são exibidos se o parâmetro "Considerar para o Centro de Custo" (parâmetros do Gestão Contábil) for igual a "Próprio Centro de Custo".

O campo centro de custo anterior e descrição são campos de texto livre para preenchimento.

O campo centro de custo atual pode ser selecionado.

Campo Conta Gerencial Anterior e Atual:

-Estes campos só são exibidos se o parâmetro "Considerar para o Centro de Custo" (parâmetros do Gestão Contábil) for igual a "Conta Gerencial".

O campo conta gerencial anterior e descrição são campos de texto livre para preenchimento.

O campo conta gerencial atual pode ser selecionado.

Campo Filial:

O campo Filial deve ser preenchido apenas quando a Filial é do tipo SCP. As Filiais SCP entregam a ECD separada da Filial Matriz e por isso devem ter o saldo identificado no registro I157 caso tenham sido feitas as transferências de saldo através do mesmo.

Para as demais Filias incluindo a Matriz este campo ficará em branco, pois o saldo da conta não é dividido entre as mesmas e fica a Filial Matriz responsável pela entrega da ECD.

Veja Também

* Alteração do Código da Conta Contábil
