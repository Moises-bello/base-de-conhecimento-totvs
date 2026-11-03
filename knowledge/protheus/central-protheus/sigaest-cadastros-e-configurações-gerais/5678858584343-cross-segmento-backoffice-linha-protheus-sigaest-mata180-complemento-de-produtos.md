---
article_id: 5678858584343
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: cb6abe49fa4b664a1f0327534007967370a6b0267b47875e21ab14effd138f06
fetched_at: '2026-06-28T22:39:09.616590+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA180 - Complemento
  de Produtos
type: support-article
updated_at: '2022-04-25T20:42:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5678858584343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA180-Complemento-de-Produtos
---

**Dúvida**O que é e para que serve a rotina MATA180 - Complemento de Produtos?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Esta rotina permite manter dados adicionais sobre um produto sem alterar seu cadastro. Também são armazenadas tabelas de preços, medidas, nome científico, certificado de qualidade, etc.

Para que ocorra o cadastro de complemento, o produto deve constar no castrado de Produtos

### Procedimentos

Para cadastrar um complemento de produto:

1. Ao acessar **Complemento de Produto**, clique em **Incluir**.

São exibidas as pastas que devem ter seus dados preenchidos, conforme orientações do *help* de campo:

* **Cadastrais:** devem ser informados os dados referentes ao complemento do produto. Exemplo: comprimento, espessura, largura, entre outros.
* **Gestão de Varejo:** são apresentados os campos referentes às informações adicionais dos produtos, como: Bas Calorica, Peso, Gordura, Gor Saturada, Gor Trans, Cor, Altura, Modelo, Espécie Prod. e Qualidade.
* **Logística:**devem ser informados os dados referentes a armazenagem do produto. Exemplo: descrição da embalagem, quantidade de itens que cabem nas embalagens, comprimento e largura (para cálculo da capacidade de armazenagem), etc.
* **Outros:** apresenta informações adicionais que são específicas para alguns ambientes.

|  |
| --- |
| Importante:  Nessa pasta, é possível configurar o campo **Envia MKT**para que o documento de solicitação de compra seja enviado automaticamente para o **Portal Marketplace**.  Se este campo for configurado como **Sim**, assim que a solicitação de compra for gerada e aprovada pelo controle de alçadas (caso exista), ela será enviada automaticamente, alterando o status do documento para **Solicitação Pendente (MarketPlace)**.  Não faz o envio automático da solicitação de compra, se o campo for configurado como **Não**.  Se o campo for configurado como Talvez, a solicitação de compra é enviada ao MarketPlace e ficará disponível para o Comprador. |

* **TMS:**devem ser informados os dados referentes ao transporte do produto, como: limite de valor de embarque, limite de peso de embarque, percentual de cubagem, periculosidade, idade máxima, etc. Dessa forma, é possível bloquear a viagem, caso o transporte não esteja de acordo com o produto.

|  |
| --- |
| Nessa pasta, é possível indicar o produto considerado como transporte de carga perigosa. Para isso, é necessário vincular esse tipo de carga ao código da ONU, de acordo com as leis estabelecidas. As informações devem ser enviadas para SEFAZ após o [cálculo do frete](http://tdn.totvs.com/x/jsD1H) desse produto. |

* **Vendas:** devem ser informados os dados referentes aos preços de venda e sua data de referência.
* **Wms**
* **Acd**
* **Agro**
* **Gestão de Serviços:**informe o campo **Tipo de Insumos**selecionando as opções pela seta indicativa.O campo **Mat.Consumo?**selecione entre **Sim** ou **Não.**Campo **Loc.Equip?**utilizando a seta indicativa

2. Confira e confirme.

|  |
| --- |
| Sempre que ativado o controle de revisão de produto através do parâmetro MV\_REVPROD e do campo**B5\_REVPROD=SIM**, a cada nova inclusão ou alteração de revisão, o Sistema deverá apresentar o status da revisão do produto como **bloqueado**, impedindo assim qualquer tipo de movimentação da nova revisão, até que algum usuário com privilégios faça a inspeção da nova revisão e libere-a. |

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
