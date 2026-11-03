---
article_id: 360026040933
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: de2343b64b0a7a551d03eb522f8fd441f32ee8248042578d9a363bfccc58a9db
fetched_at: '2026-06-28T22:39:48.658431+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus  SIGAEIC - Solicitação de
  Numerário '
type: support-article
updated_at: '2024-01-30T13:21:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026040933-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Solicita%C3%A7%C3%A3o-de-Numer%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Solicitação de numerário, incluir no importação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Procedimento para o lançamento das despesas através da Solicitação de númerario. Esta rotina controlará os lançamentos de despesas previstas, disponibilizando-as como despesas efetivas para o processo apenas após a aprovação da realização do adiantamento ao despachante.  
  
COMO REALIZAR A MANUTENÇÃO DE NUMERÁRIO:  
1. Selecione o menu Atualizações\Embarque\Solicit. Numerário.  
2. Localize o embarque “EMB-XXX”.   
3. Clique na opção Manutenção selecione a opção Incluir.  
4. Selecione Ações Relacionadas e informe os dados.   
5. Clique sobre o botão Confirmar para efetivar a gravação.

COMO REALIZAR A LIBERAÇÃO DO ADIANTAMENTO DO NUMERÁRIO:  
1. Para liberar o Adiantamento (após a fase de manutenção) acesse a opção Liberar Adiantamento disponível em Ações Relacionadas. Esta opção só é ativada quando existe saldo no campo “Valor Não Aprovado” no cabeçalho da tela de manutenção.  
  
GERAÇÃO DE TÍTULOS DE PAGAMENTO ANTECIPADO  
Quando integrado ao módulo Financeiro (SigaFin), após a liberação de adiantamento é necessário realizar a “Geração de PA” para gerar o título de adiantamento no contas a pagar. Para isso verifique os parâmetro “MV\_EASYFIN” e acesse a rotina “Geração de PA” através do menu “Atualizações / Financeiro”. Esta rotina exibirá, por empresa, todos os processos que estão aguardando a geração do título, sendo possível gerar um único título consolidando todas as despesas aprovadas.  
  
EXEMPLO – COMO REALIZAR A GERAÇÃO DO PA:  
1. Acesse o menu Atualizações\ Financeiro\ Geração de PA.   
2. Localize o cadastro do Despachante e acesse a opção Gera PA.  
3. Na tela de “Despesas de Adiantamento”, marque o processo para os qual será gerado o título de pagamento antecipado. Caso haja mais de um processo, é possível marca-los e gerar um único título.  
4. Após a seleção dos itens, acesse a opção Gera PA disponível em Ações Relacionadas. O sistema exibirá a tela do Título a Pagar; preencha os dados faltantes e confirme a geração.

EXEMPLO – COMO REALIZAR A EXCLUSÃO DO PA:  
1. Acesse o menu Atualizações\ Financeiro\ Geração de PA.   
2. Localize o cadastro do Despachante, selecione Outras Ações \ Cancela PA.  
3. Marque o PA a ser excluído e selecione Salvar  
4. Sera apresentado o título, selecione Confirmar.
