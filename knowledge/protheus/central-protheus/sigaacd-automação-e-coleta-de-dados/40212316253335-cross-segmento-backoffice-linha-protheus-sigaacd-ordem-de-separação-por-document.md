---
article_id: 40212316253335
category: SIGAACD - Automação e Coleta de Dados
content_hash: fc445e3b7bfa4c31d1b0e6597cd1ccb29e3fdea7d5f89b7bcc22f06cf8db2592
fetched_at: '2026-06-28T22:39:12.909141+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Ordem de Separação
  por documento de saída
type: support-article
updated_at: '2026-05-04T16:58:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40212316253335-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Ordem-de-Separa%C3%A7%C3%A3o-por-documento-de-sa%C3%ADda
---

O artigo explica como gerar Ordem de Separação por Documento de Saída no TOTVS Protheus, detalhando a configuração do parâmetro MV\_CBPE007, cadastro de operador, preparação do documento via módulo Faturamento e geração da ordem. A separação é realizada no Meu Coletor de Dados, finalizando com a validação do status de embarque no sistema.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40212316210583) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como gerar Ordem de Separação por Documento de Saída?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
**Configuração do processo**

Atenção

**Recursos Disponibilizado(s):**

Separação dos itens para posterior geração de Documento de saída via módulo de Faturamento

**Recursos não disponibilizado(s):**

Embalagem Simultânea

Embalagem

Gera Nota Via Coletor

Imprimir Nota

Imprimir Etiq. Volume

Embarque.

O processo consiste em configurar o parâmetro de sistema para o ACD, cadastrar um operador, preparar o documento de saída via módulo Faturamento e gerar a Ordem de Separação. Após isso, a separação é realizada pelo Meu Coletor de Dados.

**Passos**

1. Acesse o módulo Configurador, no menu Ambiente > Cadastros > Parâmetros, e edite o parâmetro MV\_CBPE007. Configure-o como ".T." (Lógico) para permitir a gravação das tabelas de Ordens de Separação do ACD com os dados da Nota Fiscal gerada pelo Protheus.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212316216471)
2. Acesse o módulo Estoque/Custos, vá em Atualizações > ACD > Operadores, clique em Incluir e preencha os campos obrigatórios para configurar o Operador.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212300090007)
3. Cadastre as movimentações básicas, como Cliente, Condição de Pagamento, Locais de Estoque, Produto, Saldo e uma TES informando os campos Tipo do TES igual a S-Saída, Atu. Estoque igual a S-Sim e Poder Terc. igual a N-Não.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212316219799)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212300091671)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212316220823)
4. No módulo Faturamento, acesse Atualizações > Pedidos > Pedido de Venda, inclua um pedido preenchendo os campos obrigatórios e fature o item.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212300093975)
5. Realize a preparação do documento de saída no assistente e confirme a série da nota.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212316223639)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212300098839)
6. No módulo Faturamento, acesse Atualizações > ACD > Ordem de Separação e clique em Gerar. 

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212300099735)

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212316232215)

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212300102295)
7. Na tela de parâmetros, selecione a opção Nota Fiscal e defina os filtros desejados, como Nota, Série, Cliente e Data emissão.
8. Confirme também os parâmetros do Meu Coletor de dados, informando opções como Embalagem simultânea e Embarque. Selecione a ordem de separação e clique em Gerar. 

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212300104087)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40212300107287)

   9. Acesse o Meu Coletor de Dados informando o login do operador, selecione a ordem de separação e realize a separação do item para finalizar a tarefa.

   10. Para validar, no Microsiga Protheus acesse a Ordem de Separação e clique em Visualizar para conferir o status da separação, que deve indicar o embarque finalizado.

**Saiba Mais**

[Ordem de Separação por documento de saída - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=464946966)

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
