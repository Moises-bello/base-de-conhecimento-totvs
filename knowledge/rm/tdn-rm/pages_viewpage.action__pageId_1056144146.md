---
content_hash: 1e35b89e53a1f475fc4619763333474e3cb09623a590e6caa7b4df045afbd144
fetched_at: '2026-06-29T00:05:52.020614+00:00'
page_id: '1056144146'
product: rm
source: tdn-rm
title: Lista de serviços prestados (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056144146
version: 10
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

1true1Regras gerais

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **servicos** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | **G** | **1-1** | **Tag raiz que agrupara os serviços prestados declarados no documento.** |  |  |
| servico | servicos | G | 1-N | Tag raiz para as informações sobre o serviço prestado. |  | Todos os dados serão agrupados em um único serviço caso não seja marcada a opção de "Não Agrupar Itens" nos |
| codigo | servico | E | 1-1 | Código do serviço na lista. | DTRBMUNICIPIOPRD.CODIGOSERVICOFEDERAL OU TPRD.CODIGOSERVICOFEDERAL |  |
| aliquota | servico | E | 1-1 | Alíquota do serviço. | TTRBMOV.ALIQUOTA | Alíquota do ISS |
| cnae | servico | E | 1-1 | Código CNAE do serviço. | Se algum dos serviços possuir o campo código CNAE preenchido no anexo: tributos do produto por município preenchido para o município da filial.  Então: primeiro código encontrado: DTRBMUNICIPIOPRD.CNAE  Senão Se campo Código de Serviço preenchido no movimento (Integrações | Fiscal)  Então: TMOV.CODIGOSERVICO  Senão Se Filial é SCP (sócio ostensiva) e  código atividade federal socio ostensivo preenchido  Então: FILIALSOCIOOSTENSIVO.CODATIVFED  Senão Se o CNAE da filial estiver preenchido  Então: GFILIAL.CODATIVFED | \* Campo Gerado apenas para os municípios que exigem a informação |
| codtrib | servico | E | 1-1 | Código de tributação do serviço. | DTRBMUNICIPIOPRD.CODIGOSERVICO | Será levado o Código referente ao Tributo cadastrado no produto e utilizado no movimento |
| discr | servico | E | 1-1 | Discriminação do serviço. |  |  |
| quant | servico | E | 1-1 | Quantidade do serviço tomado. | TITMMOV.QUANTIDADE |  |
| valunit | servico | E | 1-1 | Valor unitário do serviço. | TITMMOV.PRECOUNITARIO | Se Layout Município = ABRASF ou SIGISS Então TITMMOV.PRECOUNITARIO Senão TITMMOV.PRECOUNITARIO - TITMMOV.VALORDESC + TITMMOV.VALORDESP |
| valtotal | servico | E | 1-1 | Valor total do serviço. |  | Se Parâmetro "Edita Preço Total do Item" habilitado Entao TITMMOV.VALORTOTALITEM Senao TITMMOV.QUANTIDADE \* valunit |
| basecalc | servico | E | 1-1 | Base de cálculo do serviço. | TTRBMOV.BASEDECALCULO | Base de Calculo do ISS Se Município da Filial = Salvador E ( Regime tributação = Estimativa ou Sociedade Profissional ou Natureza tributação = Isenção ou imunidade)uberlandia Entao 0 Senao TTRBMOV.BASEDECALCULO |
| issretido | servico | E | 1-1 | Retenção de ISS do serviço. Os conteúdos possíveis são:  •  1 – Sim; •  2 – Não; •  3 – Substituição Tributária; |  | Se Tipo de recolhimento do ISS = Retido na Fonte ou Retido Deduzido  Então 1 - Sim Senão 2 - Não |
| valdedu | servico | E | 1-1 | Valor das deduções sobre o serviço. |  | (TMOVFISCAL.VLRDEDUCAOMATERIAL + MOVFISCAL.VLRDEDCAOSUBEMPREITADA +TMOVFISCAL.VLRDEDUCAOOUTRO) \* (valtotal / SOMA(valtotal de todos os itens)) |
| valpis | servico | E | 1-1 | Valor do PIS sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo PISRF do item + o PISRF do movimento  Esta tag é gerada se o parâmetro indicativo de não aderência à NT007 estiver cadastrado. |
| valcof | servico | E | 1-1 | Valor do COFINS sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo COFINSRF do item + o COFINSRF do movimento  Esta tag é gerada se o parâmetro indicativo de não aderência à NT007 estiver cadastrado. |
| valinss | servico | E | 1-1 | Valor do INSS sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo INSS do item + o INSS do movimento |
| valir | servico | E | 1-1 | Valor do IR sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo IRRF e IRRFPJ do item + o IRRF e IRRFPJ do movimento |
| valcsll | servico | E | 1-1 | Valor do CSLL sobre o serviço. | TTRBMOV.VALOR | Será considerado o valor do tributo CSLLRF do item + o CSLLRF do movimento |
| valiss | servico | E | 1-1 | Valor do ISS sobre o serviço. |  | Será considerado o valor do tributo ISS cujo o tipo de recolhimento seja "Retido na Fonte" ou "Retido Deduzido", ( ISS do item + o ISS do movimento) |
| valissret | servico | E | 1-1 | Valor do ISS retido sobre o serviço. | TTRBMOV.VALOR | Se Município da Filial = Aracaju E valissret > 0 Então 0 Senão Será considerado o valor do tributo ISS do item + o ISS do movimento |
| valliq | servico | E | 1-1 | Valor líquido da NFS-e. |  | valtotal - valpis - valcof - valinss - valir - valcsll - outrasret - valissret - descinc - desccond |
| desccond | servico | E | 1-1 | Valor do desconto condicionado do serviço. | TITMMOV.VALORDESCCONDICONALITM |  |
| descinc | servico | E | 1-1 | Valor do desconto incondicionado do serviço. | TITMMOV.VALORDESC |  |
| unidmed | servico | E | 0-1 | Unidade de medida do serviço. | TITMMOV.CODUND | Se a sigla for maior que dois caracteres serão considerados os dois primeiros caracteres |
| aliqIssRetido | servico | E | 0-1 | Aliquota do ISS retido do documento | TTRBMOV.ALIQUOTA | ISS do item do Movimento que esteja com o tipo de recolhimento retido |
| codigoTribNacional | servico | E | 0-1 | Código tributação Nacional | Cadastro do Produto, Anexo "Tributo do Produto Por Município", Campo "Código de Serviço Federal"  DTRBMUNICIPIOPRD.CODIGOSERVICOFEDERAL | Atualmente o padrão Nacional não recebe estrutura de itens. Campo previsto para uso futuro.  Uso específico para NFS-e Modelo Nacional |
| baseCalculoInss | servico | E | 0-1 | Base de cálculo do INSS | TTRBMOV.BASEDECALCULO |  |
| baseCalculoIrrf | servico | E | 0-1 | Base de cálculo do Imposto de Renda Retido na Fonte | TTRBMOV.BASEDECALCULO |  |
| baseCalculoCofins | servico | E | 0-1 | Base de cálculo do COFINS | TTRBMOV.BASEDECALCULO |  |
| baseCalculoCsll | servico | E | 0-1 | Base de cálculo da CSLL | TTRBMOV.BASEDECALCULO |  |
| baseCalculoPis | servico | E | 0-1 | Base de cálculo do PIS | TTRBMOV.BASEDECALCULO |  |
| reducaoBaseCalculo | servico | E | 0-1 | Valor da redução da base de cálculo do ISS do item |  | Não gerado |
| reducaoBaseCalculoRetido | servico | E | 0-1 | Valor da redução da base de cálculo do ISS retido do item |  | Não gerado |
| baseCalculoRetido | servico | E | 0-1 | Valor da base de cálculo do ISS retido do item |  | Não gerado |
| codigonbs | servico | E | 0-1 | Código NBS (Nomenclatura Brasileira de Serviços) | DCLASSIFBENSSERVICO.NBS (A partir da versão 2502)  TPRODUTO.NUMERONBS (versões anteriores) | Código NBS do Serviço informado no cadastrado no produto. |
| ibscbs | servico | G | 0-1 |  |  |  |

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
