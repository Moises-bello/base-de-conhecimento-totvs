---
article_id: 1500003255781
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: cf7c79cd2665b8d0febda39f4d7453b0922267a8de7672db67973c27242cff2d
fetched_at: '2026-06-28T22:39:08.107607+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como bloquear um produto
  no Protheus?
type: support-article
updated_at: '2026-06-17T15:24:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003255781-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-bloquear-um-produto-no-Protheus
---

Para bloquear um produto no Protheus via MATA010, acesse Estoque/Custos, abra o cadastro do produto, edite e marque o campo "Blq. de Tela" como "Sim". O produto ficará bloqueado, exibindo uma tarja cinza e impedindo movimentações, com aviso HELP REGBLOQ. É possível filtrar produtos bloqueados na rotina de cadastro, mas não ocultá-los em dados históricos. Para obsolescência, avalie a limpeza de saldos vinculados ao produto.

**Dúvida**  
Como efetuar o bloqueio de um produto via MATA010 - Cadastro de Produtos no Protheus?  
  
**Ambiente**  
Microsiga Protheus - Estoque/Custos - A partir da versão 11.80

**Solução**  
Caso seja necessário o bloqueio de um produto para toda e qualquer movimentação, basta seguir os passos abaixo:

**1° -** Acessar ao modulo de Estoque/Custos e localizar a rotina de Cadastro de Produtos - MATA010 (ou pelo caminho: Atualizações - > Cadastros -> Produto -> Produtos);

![Screenshot_20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31985281791767)

**2° -** Localizar o produto e clicar em "Editar"

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31985281793047)

**3° -** Localizar o campo "Blq. de Tela" (B1\_MSBLQL) e deixar com conteúdo = Sim

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31985287343127)

**4° -** Dessa forma o produto sera bloqueado, e ficara com a tarja cinza no cadastro:

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31985287343767)

**5° -** Também é possivel realizar um filtro avançado, para que não seja exibido produtos bloqueados, **apenas na rotina de cadastro de produtos**, para os produtos com bloqueio, nas demais rotinas em que o produto já foi utilizado, não é possível ocultá-lo, uma vez que se trata de um dado histórico do item.

![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31985281794711)![Screenshot_6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31985287345303)

![Screenshot_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31985287345431)

**6° -** Após confirmar, todo e qualquer movimento que algum usuário fizer utilizando este produto apresentará o HELP REGBLOQ, conforme a imagem abaixo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003489421)

Observação: Caso queira bloquear o produto para deixar o mesmo obsoleto, avaliar internamente a possibilidade de limpeza dos saldos de empenhos, reservas e afins para o produto. Para mais detalhes de como saber onde localizar estes saldos para um produto, [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-MP-SIGAEST-Consulta-F4-cadastro-de-produtos)

**Saiba mais:**

[*MP - SIGAEST - MATA010 - Erro ao excluir produto no Protheus*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003401642)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003255781)
