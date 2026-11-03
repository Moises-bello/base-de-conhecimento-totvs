---
content_hash: c7a955e15f19081ea8ee02995458f803eb232b3dd72f55e90ed09c08e82b6d30
fetched_at: '2026-06-29T00:09:26.132115+00:00'
page_id: '423938274'
product: rm
source: tdn-rm
title: Fechamento de Período - Gestão Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938274
version: 4
---

O fechamento de período tem como objetivo realizar todo o fechamento dos valores calculados, atualizando o saldo dos patrimônios e liberando os recursos para novos cálculos. Ou seja o Fechamento do Período é o real responsável pelo cálculo dos saldos dos patrimônios, gravação dos históricos e por fim, a liberação das tabelas de cálculos para receber novos cálculos.  
   
**Para sua segurança, faça um BACKUP da base de dados.** **Se por algum motivo a liberação não se completar, restaure o Backup e inicie o processo novamente.**

**Parametrização**

Durante o processo de Fechamento de Período será verificado se os parâmetros "Guardar o histórico dos cálculos do patrimônio após o Fechamento de Período" e "Guardar o histórico de ocorrências após o fechamento de período" estão marcados. Caso esta condição seja verdadeira todos os históricos relacionados às ocorrências e aos cálculos serão armazenados por patrimônio. Como forma de aviso sobre esta situação o sistema emitirá uma mensagem informando caso estes parâmetros estejam desmarcados. Esta situação não impedirá a execução do processo.

Outro procedimento realizado pelo Fechamento de Período é a atualização do saldo dos patrimônios. O Saldo dos patrimônios será atualizado de acordo com os valores pertencentes ao cálculo razão do último mês do período em aberto.

Exemplo: Caso o mês/ano de cálculo estejam em Dezembro/2011, ao executar o processo de Fechamento o período de cálculo será atualizado para Janeiro/2012 e os valores pertencentes ao último dia de Dezembro de 2011 serão transferidos para o saldo anterior do(s) patrimônio(s) cadastrado(s). Os valores referentes ao(s) patrimônio(s) em Janeiro/2012 estarão vazios tendo assim a necessidade de executar o processo de cálculo de depreciação.

Veja Também
