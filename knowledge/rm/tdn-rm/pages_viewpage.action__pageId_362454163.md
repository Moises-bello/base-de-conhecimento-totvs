---
content_hash: b3d60204fc0ec0099a00a31fd74369537303a57986101297df32261b4d8608fc
fetched_at: '2026-06-29T00:08:59.453814+00:00'
page_id: '362454163'
product: rm
source: tdn-rm
title: 2924473 DEDUINTEGRACOES-2285 DT Impedimento para trocar de módulo ou contexto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362454163
version: 2
---

# IMPEDIMENTO PARA TROCAR DE MÓDULO OU CONTEXTO - EDUCACIONAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Acesso ao módulo do Educacional ou troca de contexto |
| **Situação/Requisito:** | Sistema emite aviso abaixo e impede qualquer usuário de fazer alteração de contexto ou voltar para o módulo Totvs Educacional. Mensagem: Erro ao criar: EduActionModuleController Para utilizar descontos por antecipação nesta versão é necessário a execução do script 'CN.2018.04\_02,CN.2018.04\_03,CN.2018.05\_01'. Favor executar o script fornecido junto com a versão e repetir a operação. Em caso de dúvidas, favor procurar o nosso suporte técnico. |
| **Solução/Implementação:** | Foi excluído o código defensivo ao entrar no módulo Educacional e incluído o código defensivo para "Habilitar" ou "Desabilitar" as opções de desconto por antecipação no menu Financeiro/Contábil -> Financeiro. As opções tratadas foram: cadastro de desconto por antecipação, visão de descontos por antecipação das parcelas / lançamentos e alteração de vencimento de desconto por antecipação do lançamento.  Foram tratados também:   * Processo de geração de lançamentos: O sistema emitirá uma mensagem de erro para o usuário que está faltando os scripts caso já tenha desconto por antecipação cadastrado e não a base não possua todos os scripts de desconto por antecipação executados. * Anexo de detalhamento de bolsas por vencimento. A mesma mensagem de erro citada nos processos acima será emitida caso o usuário tente acessar esse anexo de alguma forma. * Sistema não mostrará o anexo de "Descontos por antecipação da parcela" e não mostrará o processo "Alterar vencimento do desconto por antecipação do lançamento" caso todos os scripts de desconto por antecipação não tenham sido rodados. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
