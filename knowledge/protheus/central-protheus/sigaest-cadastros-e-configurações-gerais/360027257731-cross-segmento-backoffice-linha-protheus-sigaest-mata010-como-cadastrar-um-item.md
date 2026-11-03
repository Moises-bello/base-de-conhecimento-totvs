---
article_id: 360027257731
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: f9c428c7dd9c6c8672b71bad9736fe049a0eedccaf4264180671dc16e1ef2cde
fetched_at: '2026-06-28T22:39:09.446190+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como cadastrar
  um item em forma de Kit de Produtos?
type: support-article
updated_at: '2026-02-24T12:12:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027257731-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-cadastrar-um-item-em-forma-de-Kit-de-Produtos
---

O artigo explica como cadastrar um Kit de Produtos no Protheus, detalhando o cadastro dos componentes, montagem da estrutura, criação de Ordem de Produção e apontamento, além do controle de estoque e custos. Também orienta sobre desmontagem do kit e destaca que kit e componentes possuem estoques separados.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38590009017879)**  Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Como cadastrar um item em formato de Kit de Produtos no *Protheus*?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Para formar um KIT via modulo Estoque, temos a alternativa à seguir:

O produto pode ser cadastrado como uma estrutura de produtos. Para isso siga os passos:

**1. Cadastre cada um dos componentes no Cadastro de Produtos (MATA010) sendo:**

1040 - KIT PAIS (O código do KIT)

1041 - CAMISETA (Produto componente do Kit)

1042 - CANECA (Produto componente do Kit)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411536548503)

**2. No Cadastro de Estruturas (MATA200), monte as estruturas, conforme exemplo abaixo:**

**![mceclip1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411529467031)**

**Nota:** o produto-pai (estrutura) pode ser caixa (cx), Kit, Conjunto, etc.

O Processo para alimentar estoque no código do KIT e consumir os componentes é o seguinte:

- Inclua uma Ordem de Produção (MATA650) para esse kit de produtos. Após isso o sistema fará o empenho dos materiais que compõem do kit;

![mceclip2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411529923735)

**Importante:** Ajustar o parâmetro (MV\_REQAUT = A), esse parâmetro é responsável pelas requisições dos componentes dos KITs.

- Ao efetuar o apontamento da produção (MATA250) do item , o saldo dos produtos que compõem o kit serão consumidos e o saldo do produto kit (pai da estrutura) será alimentado, conforme a quantidade que foi apontada na produção.

![mceclip3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411537397783)

Desta forma, o usuário terá o controle da quantidade de kits montados bem como a quantidade de matérias primas (ou componentes) disponíveis para montá-lo, com tratamento adequado para o custo do Kit produzido.

**Para desmontar o Kit**

Via Desmontagem de Produto (MATA242), é possível buscar o produto principal e desmontar em vários produtos, realizando o rateio do custo do produto principal também. Controlando lote e validade.

**Observação:** Tanto no processo de venda, quanto no processo de entrada de notas, os componentes (1041 e 1042), e o código do KIT (1040) são produtos diferentes, com estoque separado.

Exemplo:

- Para que seja possível compor o saldo do KIT, é necessário gerar a O.P. que vai consumir os componentes (Dando baixa no estoque dos códigos 1041 e 1042 e alimentando o código 1040).

- Para transformar um KIT e alimentar seus componentes novamente, é necessário realizar a desmontagem ( Esse processo vai desmembrar o KIT 1040 conforme quantidade informada e voltar a quantidade para os componentes 1041 e 1042).

- Outro Ponto importante é que em um pedido de venda, que informe o KIT 1040, o sistema não vai dar baixa nos componentes 1041 e 1042, esse processo já foi feito na Ordem de Produção e no Apontamento de Produção.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
