---
article_id: 27326579199895
category: Originação de Grãos (OG)
content_hash: ce8ee35df800db4e96408a2e1c8ac24c2d165fc3417330b9a94efc5ed9333412
fetched_at: '2026-06-28T22:45:37.743496+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Configuração Impressão de Contratos Word
type: support-article
updated_at: '2025-07-12T10:52:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27326579199895-Agro-Linha-Protheus-AGR-Configura%C3%A7%C3%A3o-Impress%C3%A3o-de-Contratos-Word
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326550652183) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Configuração Impressão de **Contratos de Venda OGA290** via *Word*.  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para configurar o **Contrato de Venda OGA290** via *Word*, realize os passos:

**1.** Acesse **Gestão de Agronegócio > Atualização >> Originação >>> Controle de Vendas >>>> Contrato de Venda OGA290**. Ir em **Outras Ações > Mais ações... >> Imprimir Word**. Será apresentada a janela de impressão do *word*.

![CICW.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326550653719)

Na janela de impressão *word*, possui as opções: **Parâmetros, Impr. Variáveis e Impr**. Documento.

1. **Parâmetros:** informar o local do arquivo *word*, informar o local para salvar a impressão e se caso a opção permite execução de macros, informar qual a macro ser executada.
2. **Impr. Variáveis:** imprime em lista as variáveis disponíveis para configuração do documento *word* para a impressão. Lista de variáveis baseada na tabela **NJR - Contratos (Modelo Clássico)**.
3. **Impr. Documento:** realiza a impressão do documento *word* conforme sua configuração.

![CICW1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326550655895)

![CICW2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326579153815)

**2.** Crie o documento *word* para a impressão. Para que seja possível a impressão do documento é necessário informar as variáveis para cada informação desejada. Criar um campo do tipo **DocVariable**: no *word* ir em I**nserir > Partes Rápidas > Campo**;

![CICW3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326550659607)

**3.** Inclua as variáveis conforme o modelo do documento *word* a ser criado;

![CICW4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326579156631)

Para visualizar as variáveis no documento *word*, é necessário selecionar o documento por completo, clicar com o botão direito do mouse na opção **Alternar códigos de campo**.

![CICW5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326550662807)

![CICW6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326550666263)

**4.** **Crie Macros no documento.** No inicio do documento é de extrema importância criar as variáveis **cParam01 e cParam02**;

**Exemplo:**

Essas variáveis controlam as macros no word, identificando conteúdo e quantidade de linhas para a criação de tabela.

* A variável **cParam01** controla conteúdo para a tabela.
* A variável **cParam02** controla quantidade de linhas para a tabela.

As variáveis de controle devem ser criadas no inicio do documento *word*, como padrão, possui tamanho igual a 1 **um** e com cor da folha utilizada.

![CICW7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326579162647)

Após a criação das variáveis de controle, devemos criar as macros que serão utilizadas.

![CICW8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326579168279)

**Saiba mais:**

[Agro - Linha Protheus - AGR - Configuração Impressão de Contratos Word - Macros Word](https://totvssuporte.zendesk.com/knowledge/editor/01JB2099BBQ7SWH5ZXKXBP2GX4/pt-br?brand_id=1509248)
