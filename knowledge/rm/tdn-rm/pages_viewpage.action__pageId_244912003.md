---
content_hash: d16f462abae99f613d079cc2d04b8dbaa5bd4b0a915aa64ff9f2a7a0d8805ff1
fetched_at: '2026-06-29T00:08:15.585703+00:00'
page_id: '244912003'
product: rm
source: tdn-rm
title: RMPAT00001_Fechamento_de_Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244912003
version: 9
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.16 ou superior |
| **Ocorrência:** | Fechamento de Período |
| **Ambiente:** |  |
| **Passo a passo:** | O Fechamento de Período tem como objetivo realizar todo o fechamento dos valores calculados, atualizando o saldo dos patrimônios e liberando os recursos para novos cálculos. Ou seja, o Fechamento do Período é o real responsável pelo cálculo dos saldos dos patrimônios, gravação dos históricos e por fim, a liberação das tabelas de cálculos para receber novos cálculos.  É extremamente importante que se faça um BACKUP da base de dados antes da execução do processo de Fechamento de Período. Se por algum motivo o fechamento de período não se completar deve-se verificar o log gerado ao final do processo, e se necessário restaurar imediatamente o BACKUP e iniciá-lo novamente.  **Observação:** aconselhamos a realizar o processo de fechamento de período, em base de teste primeiramente, realizar a conferencia dos relatório (saldo anterior antes do processo e posteriormente ao processo). Este processo deve ser realizado anualmente, após o sistema completar 72 meses de cálculo na linha de calculo razão.      **Procedimento (Procedimentos anteriores ao Fechamento de Período)** 1º Conferir se todas as aquisições pendentes de contabilização foram contabilizadas; 2º Emitir o Relatório de Contabilização; 3º Conferir se todas as NF's do Nucleus foram integradas e se todas as Contabilizações do Saldus foram integradas; 4º Emitir os Relatórios Agrupamento por Contas, Ficha de Imobilizado e demais relatórios patrimoniais; 5º Conferir os cálculos; **6º Fazer um backup.**    **Procedimento (Fechamento de Período)** **Acessar o processo pelo Menu Utilitários | Liberações | Fechamento de Período.** Neste processo, o sistema continuará a trabalhar com o Mês vigente, mas apagará das respectivas tabelas e enviará todos os trabalhos de ocorrências e cálculos de depreciação do período informado para o encerramento realizados anteriormente, para as tabelas de histórico e ficarão disponíveis para acesso ao mesmo apenas como HISTÓRICO DE OCORRÊNCIAS e HISTÓRICO DE CÁLCULOS no cadastro do patrimônio. O processo deve ser feito em  horário apropriado, ou seja, no fim de semana e fora do horário de expediente.        Após o Fechamento de Período deve-se conferir se os Cálculos foram gerados e emitir os relatórios Ficha de Imobilizado e Agrupamento por Contas imediatamente e realizar as conferências de Saldos de todas as contas.     **ATENÇÃO:** **Observação 1:** Se houver algum travamento, queda de energia, o backup deverá ser restaurado imediatamente. **Observação 2:** Quando realizar o procedimento de conferência de Saldo dos Relatórios, se algum cálculo estiver incorreto deve-se restaurar um backup imediatamente, e notificar o Suporte Técnico.    **LEMBRETE:** Após o Fechamento de Período não é possível realizar a Reabertura de Competência para o Mês anterior e a emissão dos relatórios para o período fechado. Por este motivo, orientamos que este processo seja feito de forma ANUAL.    **Este é um processo irreversível.** |
| **Observações:** |  |
