---
content_hash: 4eb56d6fe4844e36d484b999958151cb4aa503497363cdc6266ca41b48d8423d
fetched_at: '2026-06-29T00:10:01.483054+00:00'
page_id: '452718752'
product: rm
source: tdn-rm
title: Recálculo do Saldo de FGTS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718752
version: 9
---

Efetua o recálculo do saldo de FGTS para um determinado filtro de funcionários. Ao final do processamento será gerado um LOG informativo com os funcionários recalculados.

Dentro do filtro de funcionários, é possível localizar um determinado funcionário pela chapa ou pelo nome. Também é possível selecionar a "Situação", "Tipo de Funcionário" e "Recebimento" ou usar filtro ou fórmula de seleção.

Na tela de LOG, além das informações de conclusão do processo de "Recálculo do Saldo de FGTS", é possível salvar o LOG de informações através do botão Notepad (bloco de notas).

**Exemplo do cálculo realizado pelo sistema para atualização do saldo de FGTS**

Para realizar o recálculo do saldo de FGTS o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Recálculo do Saldo de FGTS

Legenda:

**S** - Saldo de FGTS do Mês Anterior;

**D** - Depósito de FGTS da Última Competência;

**DM** - Depósito Mensal

**F** - Fator de Atualização saldo FGTS;

**R** - Debito/Resgaste/Saque

**Formula aplicada FGTS na CEF =** S + (DM x F referente ao mês correspondente) + D - R

**Formula aplicada FGTS Fins Rescisório =** S + (DM x F referente ao mês correspondente) + D

**Exemplo :**

Última atualização de saldo FGTS do funcionário: 10/03/2023

Valor do último saldo atualizado: R$492,00

Saldo FGTS na CEF 03/2023: R$492,00

**Formula aplicada FGTS na CEF=** S + (DM x F referente ao mês correspondente) + D - R

**Formula aplicada FGTS na CEF=** 240 + (240 X 0,05) + 240 - 0

**Formula aplicada FGTS na CEF=** 240 + (12,00) + 240 - 0

**Formula aplicada FGTS na CEF=** 492,00

**Formula aplicada FGTS Fins Rescisório=** S + (DM x F referente ao mês correspondente) + D

**Formula aplicada FGTS Fins Rescisório=** 240 + (240 X 0,05) + 240

**Formula aplicada FGTS Fins Rescisório=** 240 + (12,00) + 240

**Formula aplicada FGTS Fins Rescisório=** 492,00

Cadastro de manutenção do extrato:

Tabela de cotações:

Alterada a cotação referente ao mês de fevereiro **De 0,0500 Para 0,0300**

**Vamos fazer o recalculo na competência 03/2023 após a alteração da cotação acima**

Última atualização de saldo FGTS do funcionário: 10/03/2023

Valor do último saldo atualizado: R$487,20

Saldo FGTS na CEF 03/2023: R$487,20

**Formula aplicada FGTS na CEF=** S + (DM x F referente ao mês correspondente) + D - R

**Formula aplicada FGTS na CEF=** 240 + (240 X 0,03) + 240 - 0

**Formula aplicada FGTS na CEF=** 240 + (7,20) + 240 - 0

**Formula aplicada FGTS na CEF=** 487,20

**Formula aplicada FGTS Fins Rescisório=** S + (DM x F referente ao mês correspondente) + D

**Formula aplicada FGTS Fins Rescisório=** 240 + (240 X 0,03) + 240

**Formula aplicada FGTS Fins Rescisório=** 240 + (7,20) + 240

**Formula aplicada FGTS Fins Rescisório=** 487,20

Cadastro de manutenção do extrato:

**Importante:**

As bases para o recálculo são referentes a competência anterior. Para o cálculo é utilizados os valores de cotação da tabela GCOTACAO com os valores salvos no cadastro manutenção de FGTS para cada mês, conforme formula aplicada.
