---
article_id: 360019381552
category: Encargos
content_hash: 2e6033d69873ed307c1ceac2f771f6b43a91fc45aed3d2c2c4194ab440fd8799
fetched_at: '2026-06-28T22:46:53.374300+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Pensão: [Erro] Não existem lançamentos a serem efetuados'
type: support-article
updated_at: '2025-03-05T18:46:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019381552-RH-RM-FOP-Pens%C3%A3o-Erro-N%C3%A3o-existem-lan%C3%A7amentos-a-serem-efetuados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**:00:03:00min  
  
Ocorrência**Ao gerar o lançamento financeiro de Pensão Alimentícia o sistema está apresentando a mensagem: **[Erro] Não existem lançamentos a serem efetuados.**  
![lanc_financeiro_pens_o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360015241312/lanc_financeiro_pens_o.jpg)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro pode ocorrer devido as informações da pensão estarem informadas apenas no envelope de pagamento **neste caso a movimentação não consta parametrizada no movimento da pensão de dependentes**, ou o tipo de lançamento não está sendo gerado conforme os lançamentos ativos selecionado no momento da geração do lançamento financeiro.

**Solução**Para solucionar esta ocorrência, realize os seguintes passos:  
  
**1.** Veja se o evento de pensão está lançado no envelope de pagamento;  
  
**2.** Acesse o cadastro do dependente e vá em **Anexos | Movimento da pensão de dependentes** e verifique se a movimentação está corretamente cadastrada.

No meu exemplo, o movimento é de férias.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10978315249047)  
  
As informações devem constar de acordo com o tipo da pensão gerada, por exemplo: Se for pensão nas férias, o tipo de movimentação deverá constar como férias, tais como as informações de ano/mês competência, ano/mês caixa e valores devem estar corretos conforme o envelope de pagamento.  
  
**3.** Para conferir o tipo de lançamento que está sendo gerado, acesse o menu: **Encargos | Cadastros financeiros | Parâmetros.** Nesta tela serão apresentados os tipos de lançamentos financeiros. Acesse o cadastro do lançamento financeiro de pensão e veja se na aba **Identificação** o tipo de lançamento financeiro está cadastrado como um dos cadastros relativos a pensão **14 Total da Pensão / 16 Pensão Folha / 17 Pensão Férias / 18 Pensão 13º.**  
  
Acesse também a aba **Lançamentos Ativos** e escolha um dos lançamentos que desejar atrelar o cadastro do lançamento financeiro, que será selecionado na geração dos lançamentos financeiros.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10978375735319)  
  
**4.** No momento da geração do lançamento financeiro deverá validar as parametrizações iniciais se estão corretas Ano, Competência, Período, Seleção de funcionários, etc e marcar o lançamento ativo referenciado no cadastro do lançamento financeiro de pensão.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10978420630295)

**Importante**Caso queira criar um lançamento ativo especifico para pensão, você poderá cadastrar através das tabela dinâmica. Acesse o menu **Administração de pessoal | Cadastros globais | Tabelas dinâmicas** e selecione o sistema **Folha de Pagamento**. O Cadastro dos lançamentos ativos é encontrado na tabela **CODLANATIV**.
