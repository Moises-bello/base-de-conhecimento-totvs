---
content_hash: 4cce1924d71887ba71b14475de5053b937d0ff320de6aec9df4e3fa9755dcaba
fetched_at: '2026-06-29T00:06:16.351111+00:00'
page_id: '212896471'
product: rm
source: tdn-rm
title: TTMGKP ER CT-e Notas Técnicas 2015 003 e 004
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212896471
version: 149
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Totvs Gestão de Estoque, Compras e Faturamento | **Módulo** | Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Chamado** | TTMGKP | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Sim |
| **País** | (X ) Brasil | | |

## Objetivo

Esta melhoria tem como objetivo gerar o XML do CT-e no novo leiaute, atendendo à Nota Técnica 2015/003 que determinou a inclusão da informação do ICMS devido para a UF de término do serviço de transporte, nas operações interestaduais para consumidor final, conforme as definições da Emenda Constitucional 87/15 e à Nota Técnica 2015/004 que determinou a inclusão das informações relativas ao Fundo Estadual de Combate à Pobreza.

## 

## Definição da Regra de Negócio

A Emenda Constitucional nº 87/15, publicada no DOU de 17/04/2015, alterou o § 2º do art. 155 da Constituição Federal e incluiu o art. 99 no Ato das Disposições Constitucionais Transitórias, para tratar da sistemática de cobrança do ICMS incidente sobre as operações e prestações que destinem bens e serviços a consumidor final, contribuinte ou não do imposto, localizado em outro Estado.

Essa Emenda altera a forma de repartição do ICMS entre os Estados de Origem e Destino da mercadoria, introduzindo o Diferencial de Alíquotas nas operações interestaduais de venda a consumidor final, visando beneficiar com isto o Estado que recebe a mercadoria (destinatário), visto que antes o imposto ficava todo para o Estado remetente. Desta forma traz um equilíbrio maior e equipara as operações de vendas interestaduais com não contribuintes às operações de vendas interestaduais com contribuintes, já que nestas últimas o Diferencial já é cobrado.

Apesar de estar prevendo já para 2015 a repartição entre os Estados e o cálculo do diferencial de alíquotas, a EC 87/15 só estará vigente a partir de 2016.

Por essa nova redação, não teremos diferenciação entre as operações destinadas a consumidores finais, ou seja, tanto faz se forem contribuintes ou não. Em ambos os casos, será devido o diferencial de alíquota para o Estado destinatário. Podemos ilustrar da seguinte forma:

Para não impactar de forma repentina na arrecadação dos Estados remetentes, a EC 87/15 estabelece que essa mudança será gradual, conforme art. 99 do ADCT e nas vendas de bens e serviços destinadas a consumidor final, não contribuinte do ICMS, localizado em outra unidade da federação, o ICMS correspondente à diferença entre a alíquota interna e a interestadual será partilhado entre os Estados de origem e de destino, na seguinte proporção:

Até o ano de 2019, o valor do diferencial de alíquota relativo às operações destinadas a não-contribuintes do imposto será repartido entre os Estados envolvidos. Essa mudança gradual é bem fácil de lembrar, pois de um ano para outro a mudança será sempre de 20%.

Já a NT 2015/004 divulga novas regras de validação e insere tags para informar o Fundo de Combate à Pobreza no arquivo XML do CT-e.

Assim, conforme as NT 2015/003 e 2015/004 no leiaute do CT-e foi criado um novo grupo de informações para  identificar a partilha do ICMS para a UF de término da prestação do serviço de transporte nas operações interestaduais para consumidor final, bem como para informar o Fundo de Combate à Pobreza, atendendo ao disposto na Emenda Constitucional 87 de 2015.

Para que o Totvs Gestão de Estoque, Compras e Faturamento efetue os cálculos relativos ao Fundo de Combate à Pobreza e ao diferencial de alíquota do ICMS do CT-e e gere corretamente o seu XML já no novo leiaute definido pelas Notas Técnicas 2015/003 e 2015/004, é necessária a prévia parametrização das Regras de ICMS vinculadas às naturezas de operação (CFOP) utilizadas nos movimentos de CT-e quando das prestações de serviços interestaduais para consumidor final.

Inicialmente deverá ser analisado se o movimento do CT-e está destinado a consumidor final e para isso será verificado se o campo 'Consumidor Final' do movimento (TMOVFISCAL.OPERACAOCONSUMIDORFINAL) está marcado. Caso o campo não esteja marcado os valores relativos a este grupo do leiaute não serão preenchidos. Caso o campo esteja marcado o sistema irá verificar nos parâmetros do tipo de movimento de CT-e qual o tipo de Seleção Automática da Natureza (TITMTMV.EDITANATIT) e conforme o tipo de seleção informada ira verificar no movimento ou no item de movimento do CT-e qual foi a natureza fiscal utilizada (TMOV.IDNAT ou TITMMOV.IDNAT).

Caso o 'Tipo' da natureza fiscal (DCFOP.TIPOMOVIMENTO) seja saída e a sua 'Origem/Destino' (DCFOP.ORIGEMDESTINO) seja Interestadual o sistema automaticamente entenderá que se configura o diferencial de alíquota de ICMS e irá verificar a Regra de ICMS (DCFOP.IDREGRAICMS) vinculada à natureza fiscal utilizada no CT-e para efetuar o cálculo do valor do ICMS Diferencial de Alíquota através da seguinte fórmula:

onde:

* Base de Cálculo do ICMS: Conforme constante da tabela de tributos do movimento (TTRBMOV.BASEDECALCULO) para o tributo ICMS (TTRBMOV.CODTRB = ICMS) do movimento (TTRBMOV. NSEQITMMOV = 0) ou do item de movimento (TTRBMOV,NSEQITMMOV > 0);
* Alíquota ICMS Interna: Conforme constante do campo "Alíquota S.T. / Interna D.A. (%)" da tabela de Regras de ICMS (DREGRAICMS.ALIQSUBST);
* Alíquota ICMS Interestadual: Conforme constante do campo "Alíquota ICMS (%)" da tabela de Regras de ICMS (DREGRAICMS.ALIQICMS).

Com o resultado do valor do diferencial de alíquota já calculado o sistema irá aplicar o percentual (DREGRAICMS.PERICMSESTDESTINO) informado na Regra de ICMS da Natureza de Operação utilizada e irá obter o valor da partilha do ICMS do destinatário. Já o valor da partilha do ICMS do remetente será correspondente ao valor resultante da diferença entre o valor do ICMS diferencial de alíquota e o valor da partilha do ICMS do destinatário.

Além disso o sistema irá verificar na Regra de ICMS vinculada à natureza fiscal utilizada no CT-e qual o percentual informado no campo "% FCP (Fundo de Combate à Pobreza)" (DREGRAICMS.PERICMSFCP) e fará o cálculo do valor do Fundo através da seguinte fórmula:

                                          

Estes valores, bem como os demais campos do novo leiaute, serão calculados no momento do envio do CT-e. São eles:

* vBCUFFim : Será preenchido com o valor da Base de ICMS do Movimento ou do Item do Movimento do CT-e, conforme parametrização do tipo de movimento quanto aos seus tributos;
* pFCPUFFim: Será preenchido com o percentual do Fundo de Combate à Pobreza da UF de término da prestação de serviço, conforme preenchido no campo '% FCP (Fundo de Combate à Pobreza)' (DREGRAICMS.PERICMSFCP) da Regra de ICMS vinculada à natureza fiscal utilizada;
* pICMSUFFim: Será preenchido com a alíquota interna da UF de término da prestação de serviço, conforme preenchido no campo 'Alíquota S.T./Interna D.A. (%)' (DREGRAICMS.ALIQSUBST) da Regra de ICMS vinculada à natureza fiscal utilizada;
* pICMSInter: Será preenchido com a alíquota interestadual das UF envolvidas na prestação de serviço, conforme preenchido no campo 'Alíquota ICMS (%)' (DREGRAICMS.ALIQICMS) da Regra de ICMS vinculada à natureza fiscal utilizada;
* pICMSInterPart: Será preenchido com o percentual de partilha para a UF de término da prestação de serviço, conforme preenchido no campo '% ICMS UF Destinatário' (DREGRAICMS.PERICMSESTDESTINO) da Regra de ICMS vinculada à natureza fiscal utilizada;
* vFCPUFFim: Será preenchido com o valor calculado para o Fundo de Combate à Pobreza relativo à prestação do serviço;
* vICMSUFFim e vICMSUFIni: Serão preenchidos com os valores calculados para o ICMS de partilha para as UF de término e de início da prestação do serviço respectivamente.

Não haverá alteração no leiaute do DACTE, mas as empresas emitentes devem informar, no campo de Informações Adicionais, os valores recolhidos através de GNRE, visando à conferência nas unidades de fiscalização de mercadorias em trânsito das UFs de término da prestação do serviço de transporte. 

Vale salientar que esta melhoria visa apenas a geração do XML no novo leiaute para atendimento à legislação, ou seja, não haverá nenhum reflexo nas telas dos movimentos de CT-e no Totvs Gestão de Estoque e Faturamento.

O roteiro para utilização do novo procedimento encontra-se no Documento Técnico relativo a essa melhoria.Veja em: 

## Rotinas Envolvidas:

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Envio do CT-e | Alteração | Vendas > Faturamento > Conhecimento de Transporte Eletrônico (CT-e) | Conforme especificado nas Regras de Negócio |

## Tabelas Utilizadas:

* DCFOP - Naturezas Fiscais;
* DREGRAICMS - Regras de ICMS;
* TITMMOV - Itens de Movimento;
* TITMTMV - Parâmetros do Tipo de Movimento;
* TMOV - Movimentos;
* TMOVFISCAL - Dados Fiscais do Movimento
* TTRBMOV - Tributos do Movimento.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
