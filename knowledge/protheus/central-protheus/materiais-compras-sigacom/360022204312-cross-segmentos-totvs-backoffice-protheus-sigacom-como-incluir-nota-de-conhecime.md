---
article_id: 360022204312
category: Materiais - Compras (SIGACOM)
content_hash: d895a2da86b9b9abe5af2d90d68c461e6c3d834a7da668052952caf0a9ff31ef
fetched_at: '2026-06-28T22:41:07.698550+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir Nota de
  Conhecimento de Frete (MATA116)?
type: support-article
updated_at: '2026-02-20T18:01:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022204312-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-incluir-Nota-de-Conhecimento-de-Frete-MATA116
---

**Dúvida**  
Nota de Conhecimento de frete (MATA116) para um Documento de entrada (MATA103) ?

**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução :**

A nota de conhecimento de frete é emitida quando o transporte é feito por uma transportadora e é do tipo FOB. São efetuadas diversas entregas e, ao final de um período definido pela empresa, é emitida uma nota para que sejam pagos os serviços da transportadora.  
Assim, para que a geração da nota seja possível, é necessário que a transportadora seja cadastrada como um fornecedor, para que um título a pagar seja gerado no financeiro (quando a empresa possuir o Financeiro integrado).

**Para saber mais sobre o conceito de conhecimento de frete, acesse nossa pagina no YouTube:**

[**How To | MP - SIGACOM - Conhecimento de Frete - MATA116**](https://www.youtube.com/watch?v=GGThTqWrwzU)

**CONFIGURAÇÃO :**

1. Vá em : Atualizações> Movimentos > Conhecimento de Frete;

É apresentada uma tela de parâmetros, dividida em dois quadros:  
*-> Quando a Nota :* Devem ser informados os dados da(s) Nota(s) fiscal(is) de Entrada para o sistema carregar. Dentre elas serão selecionadas e associadas ao conhecimento de frete;  
*-> Dados da Nf. de Frete :* Devem ser informados os dados do Conhecimento de Frete a ser gerado;

![frete.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4526921274519)

2. Informe o código do fornecedor, TES, Valor, de frete a ser gerado.

3. Unidade da federação UF que será utilizada no documento de conhecimento de frete;

4. Informe se deseja que os produtos sejam aglutinados;

5. ( Caso calcule Impostos : Informe base de calculo do ICMS retido e Informe o valor do ICMS retido;

6. Informe a Espécie da Nota Fiscal;

7. Selecione a opção Gera Conhec., o programa estrutura com os valores adequados à tela de digitação da nota. Os valores são calculados segundo a proporção da compra de cada produto.

8. Ao confirmar os parâmetros, será apresentada uma relação de notas fiscais de entrada para que seja(m) selecionada(s).

![20220228_104109.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4527093763607)

9. Quando o processo é concluído o sistema carrega a informação na tabela SF8;

![query.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4527086813847)

**OBSERVAÇÕES:**

**1-)** Caso a nota fiscal de entrada que esteja referenciado no CTE (MATA116) seja uma nota fiscal de retorno de beneficiamento ou devolução de vendas, ao selecionar a entrada será carregado automaticamente as informação de documento origem referente ao retorno. Pois a tela é um espelho do documento de entrada.

Exemplo:

Nota fiscal de Entrada referenciando uma saída para Beneficiamento:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6070273516951)

Pois o documento de entrada gerado pelo MATA116 é somente um **espelho** da nota referenciada.

Para saber a qual frete se refere a nota fiscal de fato deve ser verificado na tabela SF8 ou através do relatório NF Original x NF de Conhecimento de Frete **(MATR015 - descontinuado) Substituido pelo Relatório Smartview COMSV018.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36233584775063)

**2-)** A espécie CTR é a espécie padrão para o conhecimento de frete, ou seja, se não informar a Espécie por default vai trazer a CTR;  
Caso desejar que o conhecimento de frete seja incluso com outra espécie, é necessário digitar a espécie no local.

![especie.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8920888997271)

**3-)** Por padrão o sistema não permite realizar vinculo de Pedido de compras nas notas do tipo C (Complemento, Frete e Complemento de Preço) pois só é permitido nas notas do tipo normal.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11281722695703)

Irá ser gerado o Help: A103TIPON.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11281736924311)

OBS. : Se executar a rotina direto pela rotina MATA116 o vinculo do pedido não é exibido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11281384257431)

**4-)** No módulo do compras só conseguimos vincular CTE´s referentes às notas de origem de entrada.

CTE´s cuja origem, seja uma nota de saída, o sistema padrão não localiza para vínculo.

Favor verificar módulo do GFE - Gestão de Frete Embarcador.

5-) Cenários que o sistema padrão verifica para a exibição do help **A116CHVNFE**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38531327336343)

Veja mais detalhes no link:[**PCOM14008 - MATA116 - A116CHVNFE - Validação da chave NF-e - MV\_VCHVNFE**](https://tdn.totvs.com/pages/releaseview.action?pageId=1045010138)

***Saiba Mais***

* [Registro na tabela SF8 não é deletado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021565311-MP-SIGACOM-Ao-excluir-um-Conhecimento-de-Frete-pela-rotina-MATA116-o-registro-na-tabela-SF8-n%C3%A3o-%C3%A9-deletado)
* [Nota de conhecimento de frete (MATA116 - SIGACOM)](Nota%20de%20conhecimento%20de%20frete%20(MATA116%20-%20SIGACOM)%20Skip%20to%20end%20of%20banner)
* [Help A103CAGREG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021564091-MP-SIGACOM-Help-A103CAGREG)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
