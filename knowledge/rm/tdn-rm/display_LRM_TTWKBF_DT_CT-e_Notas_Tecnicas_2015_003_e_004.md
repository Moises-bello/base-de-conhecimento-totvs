---
content_hash: 6c5f63658942bc6bff372bcdb64704c7ada43fc791c30ea84227a27660064220
fetched_at: '2026-06-29T00:06:21.190672+00:00'
page_id: '223163720'
product: rm
source: tdn-rm
title: TTWKBF_DT_CT-e_Notas_Tecnicas_2015_003_e_004
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWKBF_DT_CT-e_Notas_Tecnicas_2015_003_e_004
version: 9
---

# CT-e - NOTAS TÉCNICAS 2015/003 E 2015/004

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Envio CT-e | RM.Mov.CTe.Intf | |
| **Chamados Relacionados** | TTWKBF |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | DCFOP - Naturezas Fiscais  DREGRAICMS - Regras de ICMS  TITMMOV - Itens de Movimento  TITMTMV - Parâmetros do Tipo de Movimento  TMOV - Movimentos  TMOVFISCAL - Dados Fiscais do Movimento  TTRBMOV - Tributos do Movimento |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 11.82.42 e 11.83.55 |

## Descrição

Esta melhoria tem como objetivo gerar o arquivo XML do CT-e no novo leiaute, atendendo à Nota Técnica 2015/003 que determinou a inclusão da informação do ICMS devido para a UF de término do serviço de transporte, nas operações interestaduais para consumidor final, conforme as definições da Emenda Constitucional 87/15 e à Nota Técnica 2015/004 que determinou a inclusão das informações relativas ao Fundo Estadual de Combate à Pobreza.

A Emenda Constitucional nº 87/15, publicada no DOU de 17/04/2015, alterou o § 2º do art. 155 da Constituição Federal e incluiu o art. 99 no Ato das Disposições Constitucionais Transitórias, para tratar da sistemática de cobrança do ICMS incidente sobre as operações e prestações que destinem bens e serviços a consumidor final, contribuinte ou não do imposto, localizado em outro Estado.

Essa Emenda altera a forma de repartição do ICMS entre os Estados de Origem e Destino da mercadoria, introduzindo o Diferencial de Alíquotas nas operações interestaduais de venda a consumidor final, visando beneficiar com isto o Estado que recebe a mercadoria (destinatário), visto que antes o imposto ficava todo para o Estado remetente. Desta forma traz um equilíbrio maior e equipara as operações de vendas interestaduais com não contribuintes às operações de vendas interestaduais com contribuintes, já que nestas últimas o Diferencial já é cobrado.

Apesar de estar prevendo já para 2015 a repartição entre os Estados e o cálculo do diferencial de alíquotas, a EC 87/15 só estará vigente a partir de 2016.

Por essa nova redação, não teremos diferenciação entre as operações destinadas a consumidores finais, ou seja, tanto faz se forem contribuintes ou não. Em ambos os casos, será devido o diferencial de alíquota para o Estado destinatário. Podemos ilustrar da seguinte forma:

Para não impactar de forma repentina na arrecadação dos Estados remetentes, a EC 87/15 estabelece que essa mudança será gradual, conforme art. 99 do ADCT e nas vendas de bens e serviços destinadas a consumidor final, não contribuinte do ICMS, localizado em outra unidade da federação, o ICMS correspondente à diferença entre a alíquota interna e a interestadual será partilhado entre os Estados de origem e de destino, na seguinte proporção:

Até o ano de 2019, o valor do diferencial de alíquota relativo às operações destinadas a não-contribuintes do imposto será repartido entre os Estados envolvidos. Essa mudança gradual é bem fácil de lembrar, pois de um ano para outro a mudança será sempre de 20%.

A NT 2015/003 instituiu o novo leiaute do CT-e quanto ao diferencial de alíquota, enquanto que a NT 2015/004 divulga novas regras de validação e insere tags para informar o Fundo de Combate à Pobreza no arquivo XML do CT-e.

## Procedimento para Utilização

Para que o Totvs Gestão de Estoque, Compras e Faturamento efetue os cálculos relativos ao diferencial de alíquota do ICMS do CT-e e gere corretamente o seu XML já no novo leiaute definido pela Nota Técnica 2015/003, é necessária a prévia parametrização das Regras de ICMS vinculadas às naturezas de operação (CFOP) utilizadas nos movimentos de CT-e quando das prestações de serviços interestaduais para consumidor final.

Para isso vá em*"Cadastros > Fiscais > Naturezas Fiscais"* e selecione a natureza (CFOP) utilizada nos movimentos de CT-e nas prestações de serviços interestaduais para consumidor final.

Acesse a pasta "Tributação ICMS/IPI" e verifique qual é a Regra de ICMS que está vinculada à Natureza Fiscal:

Vá em*"Cadastros > Fiscais > Mais... > Regras de ICMS"* e edite a Regra que está vinculada à Natureza Fiscal utilizada no movimento de CT-e quando das prestações de serviços interestaduais para consumidor final.

Na pasta*"Identificação"*, o campo 'Operação Tributária' deve estar configurado como "Diferencial de Alíquota'.

Na pasta*"Dados ICMS"*, no campo 'Alíquota ICMS (%)' informe o percentual da alíquota de ICMS nas operações de saída interna.

Na pasta*"Dados ICMS S.T."* informe no campo 'Alíquota S.T. / Interna D.A. (%)' o percentual da alíquota de ICMS nas operações de saída dentro da sua UF.

Em atendimento à NT 2015/003 nesta pasta foram criados os campos:

* % ICMS UF Destinatário: onde deverá ser informado o percentual do ICMS Diferencial de Alíquota destinado à UF de término do serviço de transporte. O sistema utilizará a informação deste campo para calcular o valor da Partilha do ICMS entre os Estados, lembrando que o conteúdo do mesmo deve ser alterado ao início de cada ano conforme percentuais estabelecidos na EC 87/15.
* % FCP (Fundo de Combate à Pobreza): onde deverá ser informado o percentual a ser aplicado sobre o valor do serviço de transporte para cálculo do valor relativo ao Fundo de Combate à Pobreza na operação. É importante lembrar que o Fundo de Combate à Pobreza ainda não foi instituído em todas as UF, ou seja, ao fornecer esta informação deverá ser levado em conta a UF de término do serviço de transporte.

Vale lembrar que a aba *"Dados ICMS S.T."* somente será apresentada nas regras de ICMS cuja 'Operação Tributária' esteja definida como Diferencial de Alíquota ou Substituição Tributária.

Através dessas informações e  dos demais dados do movimento de CT-e o sistema efetuará o cálculo do ICMS Diferencial de Alíquota através da seguinte fórmula:

Após a parametrização das Regras de ICMS o sistema estará apto a efetuar o cálculo do ICMS Diferencial Alíquota e gravá-lo no XML.

Como a partilha do ICMS Diferencial de Alíquota se aplica somente nas operações destinadas aos consumidores finais,  o seu cálculo será ativado sempre que essa informação for fornecida, ou seja, o sistema somente efetuará esse cálculo caso no movimento de CT-e seja utilizada uma natureza fiscal devidamente parametrizada e caso seja informado que o movimento é destinado a Consumidor Final.

Para fornecer essa informação, quando da inclusão de um CT-e, acesse a tela de Integração Fiscal do movimento e marque o campo 'Consumidor Final'.

Com o resultado do valor do diferencial de alíquota já calculado o sistema irá aplicar o percentual informado na Regra de ICMS da Natureza de Operação utilizada e irá obter o valor da partilha do ICMS do destinatário. Já o valor da partilha do ICMS do remetente será correspondente ao valor resultante da diferença entre o valor do ICMS diferencial de alíquota e o valor da partilha do ICMS do destinatário.

Foram criados novos grupos no leiaute do CT-e e os mesmos serão preenchidos no momento do envio do XML, ou seja, é no momento do envio que o sistema irá calcular o valor do ICMS diferencial de alíquota para o CT-e bem como a partilha deste valor.

Não haverá alteração no leiaute do DACTE, mas as empresas emitentes devem informar, no campo de Informações Adicionais, os valores recolhidos através de GNRE, visando à conferência nas unidades de fiscalização de mercadorias em trânsito das UFs de término da prestação do serviço de transporte. 

Vale salientar que esta melhoria visa apenas a geração do XML no novo leiaute para atendimento à legislação, ou seja, não haverá nenhum reflexo nas telas dos movimentos de CT-e no Totvs Gestão de Estoque e Faturamento.

Detalhes técnicos acerca deste novo procedimento encontram-se na Especificação de Requisitos relativa a essa melhoria. Veja em: [TTWKBF\_ER\_CT-e\_Notas\_Tecnicas\_2015\_003\_e\_004](http://tdn.totvs.com/display/LRM/TTMGKP_ER_CT-e_Notas_Tecnicas_2015_003_e_004)

divs
