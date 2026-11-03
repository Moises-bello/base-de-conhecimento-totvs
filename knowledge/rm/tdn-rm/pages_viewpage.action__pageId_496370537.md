---
content_hash: e6adc376f165dbe26976a8a045a5a36a5d0218b5b7f49ab4fa89b64a2c3acc19
fetched_at: '2026-06-29T00:10:22.051742+00:00'
page_id: '496370537'
product: rm
source: tdn-rm
title: Manual Revitalização Atualizador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496370537
version: 6
---

Versão 12.1.19

Antes de executar o atualizador e transformar a base padrão para revitalização é necessário que se atualize a base de dados até a ultima versão de mercado liberada, faça o backup desta base e execute a ferramenta "Conversor Revitalização"

Acesse “Executar”, localize “Conversor Revitalização”

A cada execução o sistema apresenta o resultado com o "Check" (verde), caso haja erro não será possível continuar até a devida correção.

Algumas verificações podem solicitar que o usuário faça alguma correção como nos sub processos 8, 9 e 10. Nestes casos os registros que apresentarem lançamentos financeiros não integrados devem ser Efetivados ou cancelados ou ter o plano de financiamento gerado, de acordo com cada caso.

Depois de executar todas as opções sem erros, a base estará apta para ser revitalizada. Se houver erro entre em contato com seu canal de atendimento.

Obs.: Sugerimos para melhorar a performance da conversão, a reinicialização da instância do banco de dados após a execução do "Conversor da Revitalização".

Ao final de todos os passos é preciso executar o Atualizador novamnete para a versão revitalizada.

Em caso de dúvida, abaixo identificaremos os ajustes que foram executados pelo "Conversor Revitalização" em cada um dos processos.

São principalmente duas alterações:

1- Na versão 12.1.22 (apenas), não valida mais no Atualizador as condições de cliente Piloto, novos, ... etc;

2- Nas versões 12.1.18 em diante, não impede mais o Conversor da Revitalização (ImbConversorRevitalizacaoAction);

Pesquisar por Revitalização

1 . Rastreamento de lançamentos filhos

Executar

2 - Conversor de Baixa Parcial com Cheque emitido na baixa antiga

3 -  Utilitários de Lançamentos Imobiliários

4 – Conversão dos Lançamentos Filhos para Nova Baixa

Sim

5 – Executar novamente o Utilitário de lançamentos imobiliários

6 – Habilitar o histórico dos lançamentos financeiros

7 – Conversão dos Aditivos com XML para tabelas

8 – Validar se existem vendas sem integração com lançamentos financeiros

Ao Marcar o Parâmetro; Não Gerar Lançamentos das Parcelas de Vendas Quitadas Sem Integração com TOTVS Gestão Financeira

Não serão gerados os lançamentos financeiros para o TOTVS Gestão Financeira, o que poderá ocasionar perda de informação.

Atenção - Objetos Gerenciais, Relatórios de parcelas e consultas anexas não funcionarão.

Sendo assim, o TIN na versão revitalizada somente terá a visualização dos lançamentos financeiros.”

É relacionado as vendas quitadas que o usuário decidiu não corrigir

Tal processo deverá ser executado a primeira vez **sem marcar** o Parâmetro para que o Conversor corrija as vendas quitadas que estejam com sem lançamentos e sem lançamentos.

Observação :“**Processo irreversível**

**SELECT** XVENDA.CODCOLIGADA, XVENDA.NUM\_VENDA **AS** NUMEROVENDA

**FROM** XVENDA

**WHERE** EXISTS

          (**SELECT** 1

**FROM** XPARCELAPAGAMENTO

**WHERE** XPARCELAPAGAMENTO.CODCOLIGADA = XVENDA.CODCOLIGADA

                  AND XPARCELAPAGAMENTO.NUM\_VENDA = XVENDA.NUM\_VENDA

                  AND COALESCE(XPARCELAPAGAMENTO.IDLAN,0) = 0)

         AND NOT EXISTS (**SELECT** 1 **FROM** XDISTRATO **WHERE** XDISTRATO.NUMVENDA = XVENDA.NUM\_VENDA)

**ORDER** **BY** XVENDA.CODCOLIGADA, XVENDA.NUM\_VENDA

Através da visão apresentada, o usuário deverá selecionar cada venda e executar o processo que mais se adeque: "Gerar Lançamentos Financeiros” ou “Excluir o Plano de financiamento”. A visão apresentada é da venda permitindo os ajustes manuais dentro da ferramenta de conversão.

Depois de ajustar venda a venda, o usuário deve fechar a tela.

9 -  Validar se existem vendas com aditivos em preparação , que impactam valores de parcela

Efetivar ou cancelar  os Adivitos que estao em Amarelo

11-  Migrar Gráficos , Relatórios e Sentença SQL dos cadastros antigos para os Novos Cadastros

Feita a Revitalização

Agora é processar o Atualizador

Avançar

Avançar

Avançar

Marcar parametros e em seguida - Homologação

Marcar os temos para prosseguir e em seguida : Avançar

Avançar

Avançar

Avançar

Avançar

Concluir

Atualização do banco de dados executado.
