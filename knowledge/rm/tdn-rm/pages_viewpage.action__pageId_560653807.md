---
content_hash: ab4aa9f76e7916a84b766bb265f9784c797a779d93bd533638dd222244c0e69c
fetched_at: '2026-06-29T00:10:47.761625+00:00'
page_id: '560653807'
product: rm
source: tdn-rm
title: Lista de serviços prestados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653807
version: 24
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

1true1Regras gerais

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **servicos** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **G** | **1-1** | **Tag raiz que agrupara os serviços prestados declarados no documento.** |  |  |
| servico | servicos | G | 1-N | Tag raiz para as informações sobre o serviço prestado. |  | Todos os dados serão agrupados em um único serviço caso não seja marcada a opção de "Não Agrupar Itens" nos |
| codigo | servico | E | 1-1 | Código do serviço na lista. | DTRBMUNICIPIOPRD.CODIGOSERVICOFEDERAL OU TPRD.CODIGOSERVICOFEDERAL |  |
| aliquota | servico | E | 1-1 | Alíquota do serviço. | TTRBMOV.ALIQUOTA | Alíquota do ISS |
| idcnae | servico | E | 0-1 | ID do CNAE | TPRDCOMPL.IDCNAE |  |
| cnae | servico | E | 1-1 | Código CNAE do serviço. | Se algum dos serviços possuir o campo código CNAE preenchido no anexo: tributos do produto por município preenchido para o município da filial.  Então: primeiro código encontrado: DTRBMUNICIPIOPRD.CNAE  Senão Se campo Código de Serviço preenchido no movimento (Integrações | Fiscal)  Então: TMOV.CODIGOSERVICO  Senão Se Filial é SCP (sócio ostensiva) e  código atividade federal socio ostensivo preenchido  Então: FILIALSOCIOOSTENSIVO.CODATIVFED  Senão Se o CNAE da filial estiver preenchido  Então: GFILIAL.CODATIVFED | \* Campo Gerado apenas para os municípios que exigem a informação |
| codtrib | servico | E | 1-1 | Código de tributação do serviço. | DTRBMUNICIPIOPRD.CODIGOSERVICO | Será levado o Código referente ao Tributo cadastrado no produto e utilizado no movimento |
| cTribNac | servico | E | 0-1 | Código Tributação Nacional. |  | Cadastro do Produto, Anexo "Tributo do Produto Por Município", Campo "Código de Serviço Federal", vinculado ao município de incidência  DTRBMUNICIPIOPRD.CODIGOSERVICOFEDERAL |
| discr | servico | E | 1-1 | Discriminação do serviço. |  |  |
| quant | servico | E | 1-1 | Quantidade do serviço tomado. | TITMMOV.QUANTIDADE |  |
| valunit | servico | E | 1-1 | Valor unitário do serviço. | TITMMOV.PRECOUNITARIO | Se Layout Município = ABRASF ou SIGISS Então TITMMOV.PRECOUNITARIO Senão TITMMOV.PRECOUNITARIO - TITMMOV.VALORDESC + TITMMOV.VALORDESP |
| valtotal | servico | E | 1-1 | Valor total do serviço. |  | **Se** Parâmetro "Edita Preço Total do Item" habilitado **&** VALORTOTALITEM > 0 **Entao** TITMMOV.VALORTOTALITEM **Senao** TITMMOV.QUANTIDADE \* valunit |
| basecalc | servico | E | 1-1 | Base de cálculo do serviço. | TTRBMOV.BASEDECALCULO | Base de Cálculo do ISS Se Município da Filial = Salvador E ( Regime tributação = Estimativa ou Sociedade Profissional ou Natureza tributação = Isenção ou imunidade)uberlandia Entao 0 Senao TTRBMOV.BASEDECALCULO |
| issretido | servico | E | 1-1 | Retenção de ISS do serviço. Os conteúdos possíveis são:  •  1 – Sim; •  2 – Não; •  3 – Substituição Tributária; |  | Se Tipo de recolhimento do ISS = Retido na Fonte ou Retido Deduzido  Então 1 - Sim Senão 2 - Não |
| valdedu | servico | E | 1-1 | Valor das deduções sobre o serviço. |  | (TMOVFISCAL.VLRDEDUCAOMATERIAL + MOVFISCAL.VLRDEDCAOSUBEMPREITADA +TMOVFISCAL.VLRDEDUCAOOUTRO) \* (valtotal / SOMA(valtotal de todos os itens)) |
| valreceb | servico | E | 1-1 | Valor de recebimento da nota | TMOV.VALORLIQUIDO | Condições de geração:   * Tributo ISS está presente no item do movimento, E * Campo de geração está marcado em Produto | Anexos | Tributos do Produto por Município | NFSe | Valor Total Recebido   Gerado com o valor líquido da nota, TMOV.VALORLIQUIDO |
| discrdedu | servico | E | 0-1 | Discriminação da dedução sobre o serviço | TMOVCOMPL.DISCRDEDUCOES | Se TMOVCOMPL.INCENTIVCULTURAL Preenchido Então Preencher tag <DiscrDed> Senão Não preencher tag <DiscrDed>  Gerado apenas para TSS |
| valpis | servico | E | 1-1 | Valor do PIS sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo PISRF do item + o PISRF do movimento |
| valcof | servico | E | 1-1 | Valor do COFINS sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo COFINSRF do item + o COFINSRF do movimento |
| valinss | servico | E | 1-1 | Valor do INSS sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo INSS do item + o INSS do movimento |
| valir | servico | E | 1-1 | Valor do IR sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo IRRF e IRRFPJ do item + o IRRF e IRRFPJ do movimento |
| valcsll | servico | E | 1-1 | Valor do CSLL sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo CSLLRF do item + o CSLLRF do movimento |
| valiss | servico | E | 1-1 | Valor do ISS sobre o serviço. |  | Será considerado o valor do tributo ISS cujo tipo de recolhimento seja "Retido na Fonte" ou "Retido Deduzido", ( ISS do item + o ISS do movimento) |
| valissret | servico | E | 1-1 | Valor do ISS retido sobre o serviço. | TTRBMOV.VALOR | Se Município da Filial = Aracaju E valissret > 0 Então 0 Senão Será considerado o valor do tributo ISS do item + o ISS do movimento |
| outrasret | servico | E | 1-1 | Valor referente a outras retenções sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo CONTRIBSOCIALRF do item + o CONTRIBSOCIALRF do movimento |
| valliq | servico | E | 1-1 | Valor líquido da NFS-e. |  | valtotal - valpis - valcof - valinss - valir - valcsll - outrasret - valissret - descinc - desccond |
| valtrib | servico | E | 0-1 | Valor Aprox. Tributos (Item). | TITMMOVFISCAL.VLRTOTTRIB | Preenchido a partir dos valores da lei da transparência no Movimento |
| desccond | servico | E | 1-1 | Valor do desconto condicionado do serviço. | TITMMOV.VALORDESCCONDICONALITM |  |
| descinc | servico | E | 1-1 | Valor do desconto incondicionado do serviço. | TITMMOV.VALORDESC |  |
| unidmed | servico | E | 0-1 | Unidade de medida do serviço. | TITMMOV.CODUND | Se a sigla for maior que dois caracteres serão considerados os dois primeiros caracteres |
| tributavel | servico | E | 0-1 | Tributável (S/N). |  | Se houver ISS no movimento com base de cálculo > 0 a tag é gerada com "S" senão com "N" |
| cfps | servico | E | 0-1 | CFPS | DCFOP.CFPS |  |
| cst | servico | E | 0-1 | Código da situação tributária. | TTRBMOV.SITTRIBUTARIA | Será gerado o valor preenchido na linha do tributo ISS. |
| valrepasse | servico | E | 0-1 | Valor Repasse. |  | Não será gerado |
| valcartri | servico | E | 0-1 | Valor da carga tributária | TITMMOVFISCAL.VLRTOTTRIB |  |
| valpercartri | servico | E | 0-1 | Percentual da carga tributária |  | Soma dos campos do serviço utilizado:  TPRDCODFISCAL.ALIQIBPTFEDERAL,   TPRDCODFISCAL.ALIQIBPTESTADUAL,                                          TPRDCODFISCAL.ALIQIBPTMUNICIPAL |
| valfoncartri | servico | E | 0-1 | Fonte da carga tributária |  | Informação Fixa: IBPT |
| outrasdespesas | servico | E | 0-1 | Outras Despesas. |  | Não será gerado |
| vlbascsll | servico | E | 0-1 | Base CSLL Item. |  | Base de cálculo do tributo CSLL ou CSLLRF |
| vlbaspis | servico | E | 0-1 | Base PIS Item. Retido |  | Base de cálculo do tributo PIS ou PISRF |
| vlbascfins | servico | E | 0-1 | Base COFINS Item. Retido |  | Base de cálculo do tributo COFINS ou COFINSRF |
| vlbasir | servico | E | 0-1 | Base IR Item. |  | Base de cálculo do tributo IRRF ou IRRFPJ |
| vlbasinss | servico | E | 0-1 | Base INSS Item. |  | Base de cálculo do tributo INSS |
| codnbs | servico | E | 0-1 | Código NBS (Nomenclatura Brasileira de Serviços) | DCLASSIFBENSSERVICO.NBS (A partir da versão 2502)  TPRODUTO.NUMERONBS (versões anteriores) | Será levado o Código NBS do Serviço informado no cadastrado no produto. |
| **piscofins** | **servico** | **G** | **0-1** |  |  |  |
| dtinicioevento | servico | E | 0-1 | Data de início do evento. | DATIVIDADEEVENTO.DTINICIO | Data de início da atividade de evento. Ano, Mês e Dia (AAAA-MM-DD) |
| dtfimevento | servico | E | 0-1 | Data de fim do evento. | DATIVIDADEEVENTO.DTFIM | Data de fim da atividade de evento. Ano, Mês e Dia (AAAA-MM-DD) |
| ncm | servico | E | 0-1 | Código NCM (Nomenclatura Comum do Mercosul). | DCLASSIFBENSSERVICO.NUMERO |  |
| descMovel | servico | E | 0-1 | Descrição do bem móvel. |  | Não será gerado |
| QtdMovel | servico | E | 0-1 | Quantidade do bem móvel. |  | Não será gerado |
| cIntContrib | servico | E | 0-1 | Código interno do contribuinte. |  | Não será gerado |
| **comExt** | **servico** | **G** | **0-1** |  |  |  |
| inscImobFisc | servico | E | 0-1 | Inscrição Imobiliária Fiscal. | MPRJCOMPL.INSCMUNOBRA | Criar o campo complementar no projeto com o nome INSCMUNOBRA, o tamanho e tipo do campo deve ser verificado no manual da NFS-e Nacional |
| **atvEvento** | **servico** | **G** | **0-1** |  |  |  |

Ao usar o  os tributos devem ser associados somente nos itens do movimento.

2Regras específicas por município1lefttrue1Campinas

O layout da NFS-e foi alterado para que os campos **InscricaoMunicipalObra** e **ServicoObra** sejam gerados no [Layout único de integração da NFS-e - Construção](https://tdn.totvs.com/pages/viewpage.action?pageId=560653923).

O campo **InscricaoMunicipalObra** será gerado com base em campo complementar do cadastro do projeto.

**Regras:**

* A tag deverá ser gerada somente quando o campo complementar estiver preenchido.
* Sempre que o município do projeto for diferente do município de prestação, devemos ignorar o valor preenchido no campo complementar e gerar a tag com 000000000 (9 zeros). Caso seja o mesmo município devemos gerar com o valor preenchido no campo complementar.

O campo **ServicoObra** deverá ser gerado a partir de um campo complementar do item do Movimento.

**Regra:** Gerar a tag somente quando o campo complementar estiver preenchido.

**Exemplo:**

*<construcao>*

*<inscmunobra>000000000</inscmunobra>*

*<codservobra>27</codservobra>*

*</construcao>*

falseCadastro dos campos complementares

Segue exemplo de onde e como os campos complementares devem ser cadastrados.

2true1Passo 1

Os campos devem ser criados na solução de Obras e Projetos.

Para isso acesse:

*Construção | Obras e Projetos*

*Cadastros Gerais | Básicos | Campos Complementares | Projeto*

2Passo 2

Inclua os novos campos (conforme dados indicados no layout da NFS-e):

CODSERVOBRAINSCMUNOBRA3Passo 3

Agora vamos Criar/Editar um Projeto, para isso acesse:

*Construção | Obras e Projetos*

*Projeto | Básico | Selecionar Projeto*

Ao abrir nosso projeto, na aba *Campos Complementares*, os campos criados podem ser editados neste caminho

Campos ComplementaresNota

Disponível a partir da biblioteca 12.1.33

2Criciúma/SC

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| issretido | servico | E | 1-1 | Retenção de ISS do serviço. Os conteúdos possíveis são:  •  1 – Sim; •  2 – Não; •  3 – Substituição Tributária; |  | Se Tipo de recolhimento do ISS = Retido na Fonte ou Retido Deduzido  Então 1 - Sim Senão 2 - Não  Para o município de Criciúma/SC caso no cadastro do cliente, aba Tributos, o campo "Retenção de ISS" esteja selecionado a opção Substituição Tributária a tag é gerada com o valor 3.  Veja o [How To](https://tdn.totvs.com/pages/viewpage.action?pageId=676036822) sobre o ISS retido substituição tributária |

2Campo Grande/MS

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| tributavel  tributavel | servico | E | 0-1 | Indica se o serviço é tributável ou não. Os valores possíveis são:  •  1 – Tributável;  •  2 – Não tributável. |  | Será gerado quando o valor da base de calculo do ISS do item do movimento for maior que zero  Campo especifico para os municípios:   * **Uberlândia/MG** * **Campo Grande/MS** |

3Uberlândia/MG

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| tributavel | servico | E | 0-1 | Indica se o serviço é tributável ou não. Os valores possíveis são:  •  1 – Tributável;  •  2 – Não tributável. |  | Será gerado quando o valor da base de calculo do ISS do item do movimento for maior que zero  Campo especifico para os municípios:   * **Uberlândia/MG** * **Campo Grande/MS** |

4Florianópolis/SC

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| cfps | servico | E | 0-1 | Código fiscal de prestação de serviço. | DCFOP.CFPS | Será gerado apenas para o município de Florianópolis/SC. |

4Batatais/SP

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| serierps | identificacao | E | 1-1 | Série do RPS. |  | Série gerada a partir do campo complementar do movimento - criar e preencher campo BLOCO na TMOVCOMPL. |
