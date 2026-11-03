---
article_id: 1500001884321
category: SIGAEST - CUSTOS
content_hash: e0b8feafe37b783abe45054b3f88d84426cdc680c53eeefa867186c5d39e1717
fetched_at: '2026-06-28T22:39:00.911431+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro de aplicação
  na thread de Contabilização
type: support-article
updated_at: '2025-07-07T11:25:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001884321-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-de-aplica%C3%A7%C3%A3o-na-thread-de-Contabiliza%C3%A7%C3%A3o
---

**Dúvida**Ao executar o Recálculo do Custo Médio ocorre "Erro: MATA330 - Erro de aplicação na thread de contabilização". Como resolver?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405088180631)  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Este erro ocorre quando há inconsistência em algum Lançamento Padronizado cadastrado.

Para investigação do problema, caso tenha gerado log, tente localizar o LP pela variável **CPADRAO**ou pelo campo **CT5\_LANPAD,** cujo conteúdo provavelmente seja o LP com problemas. Corrija a sintaxe.

Caso não tenha gerado log, uma opção é desinstalar as Storeds Procedures 19 e 20 e executar novamente para que gere errorlog o qual deve indicar o LP que está gerando esse erro de sintaxe, caso você esteja usandoa  rotina MATA038, efetue o mesmo procedimento na rotina MATA330 diretamente, com as mesmas parametrizações, pois a rotina em PO-UI é limitada a erros, e mostra apenas o CABEÇALHO do erro, sendo inviavel uma analise efetiva de TODO O ERRO que pode ter sido gerado, portanto, efetuar o teste na rotina MATA330.

**Importante**:  O Suporte Técnico não valida/configura **L****ançamentos Padronizados**, por envolver informações sobre o negócio/processos em que o usuário deseja contabilizar, e desenvolvimento da regra em ADVPL. Informamos que as configurações de **LPs** são de responsabilidade do **cliente/analista de implantação**, já que o mesmo é liberado para configurações e customizações específicas. Caso não tenha conhecimento na utilização do cadastro de LP, recomendamos que seja solicitado ao Executivo de Soluções de Negocio (ESN) a visita de um analista in loco para avaliar o ambiente e adequar as fórmulas de LP.

**Obs: Algumas outras ponderações que podem auxiliar, em segunda instância, nesta ocorrência são:**

- Realizar teste com configurações de LP com sintaxe simples. Exemplo: SD1->D1\_CUSTO ou SD2->D2\_CUSTO1 ou SD3->D3\_CUSTO1

Lembrando que o Suporte padrão não avalia o conteúdo do campo CT5\_VLR01, por se tratar de regra de negócio.

- Avaliar quantas threads utiliza para o processamento da contabilização. Realizar um teste com o parâmetro **MV\_M330THR** = 1 e **MV\_M330JCM** em branco, para que não seja utilizado a chamada de threads, para verificar o impacto no comportamento pontual desse processamento.

Detalhes aqui: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047857193-MP-SIGAEST-Dicas-de-Performance-para-Rotina-de-Custo-M%C3%A9dio>

- Certificar-se de realizar um teste em ambiente de Testes atualizado. [Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)/ [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) -[Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) / [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947528)  | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1031460) / Smartclient - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1031469) / [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

Para demais ocorrências no processo de Acompanha Custos, consulte:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - "Ocorrências" X "Soluções" no Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12093061866135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Ocorr%C3%AAncias-X-Solu%C3%A7%C3%B5es-no-Acompanha-Custos?source=search)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
