---
content_hash: 5a98537b19d5458717d8581fa96ae3a7843eef4c58571c0bd0aaa1c4fbe4214d
fetched_at: '2026-06-29T00:09:19.911175+00:00'
page_id: '422545625'
product: rm
source: tdn-rm
title: SPED Fiscal - Bloco G
type: documentation
url: https://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+G
version: 21
---

Este bloco é composto pelos registros: 

BLOCOGleftG110G110

**ICMS - Ativo Permanente - CIAP**

G125G125

**Movimentação de Bem ou Componente do Ativo Imobilizado**

Selecionados registros onde a Data de Aquisição seja Menor que a Data Final do Período.  
Situações Tributárias com data de Aquisição dentro ou menor do Período de Geração serão incluídos no Arquivo.

Composição de Patrimônio 

Ao utilizar o processo [Composição de Patrimônio](https://tdn.totvs.com.br/pages/viewpage.action?pageId=423938345) o Registro G125 poderá ocasionar erro, uma vez que este processo irá replicar o mesmo código de patrimônio em vários itens e estes comportamento não é aceito pela EFD ICMS IPI. Portanto não deve ser utilizado para as empresas que pretendem gerar o bloco G.

G126G126

**Outros créditos CIAP**

G130G130

**Identificação do documento fiscal**

G140G140

**Identificação do item do documento fiscal**

**Observações Sobre o Preenchimento**

* **Campo 01 (REG): Valor Válido:**[G140].
* ****Campo 02 (NUM\_ITEM):**** Número sequencial do item no documento fiscal
* ****Campo 03 (COD\_ITEM):****Código correspondente do bem no documento fiscal (TPRD.CODIGOPRD).
* **Campo 04 (QTDE):** Gerado a partir de 2020 - Se o Bem tiver sido incluído pela tela de Ativo Imobilizado será gerado com a informação correspondente da DATIVO.  
  Nas operações de saída, é a quantidade utilizada, informada no Patrimônio (DITEMBEM.VALORUTILIZ).
* **Campo 05 (UNID):** Gerado a partir de 2020 - Se o Bem tiver sido incluído pela tela de Ativo Imobilizado será gerado com a Unidade de Compra do Produto (TPRD.CODUNDCOMPRA).
* **Campo 06 (VL\_ICMS\_OP\_APLICADO ):** Gerado a partir de 2020 - Se o Bem tiver sido incluído pela tela de Ativo Imobilizado será gerado com a informação correspondente da DATIVO.
* **Campo 07 (VL\_ICMS\_ST\_APLICADO):** Gerado a partir de 2020 - Se o Bem tiver sido incluído pela tela de Ativo Imobilizado será gerado com a informação correspondente da DATIVO.
* **Campo 08 (VL\_ICMS\_FRT\_APLICADO):** Gerado a partir de 2020 - Se o Bem tiver sido incluído pela tela de Ativo Imobilizado será gerado com a informação correspondente da DATIVO.
* **Campo 09 (VL\_ICMS\_DIF\_APLICADO):** Gerado a partir de 2020 - Se o Bem tiver sido incluído pela tela de Ativo Imobilizado será gerado com a informação correspondente da DATIVO.
Demais Informações.Demais Informações

* **Criação de Campos complementares**

Para geração do bloco G do SPED é necessário a criação dos seguintes campos complementares:

|  |  |  |
| --- | --- | --- |
| Nome da Coluna Vinculada | Descrição | Tabela de Campo Complementar |
| FUNC | Descrição da Função do bem | Bens |
| TPMOVCIAP | Tipo de Movimentação do Bem ou componente | Item |

Deve ser criada uma tabela dinâmica com os seguintes valores para movimentação do bem ou componente:

| Código | Descrição |
| --- | --- |
| MC | Imobilização oriunda do Ativo Circulante |
| AT | Alienação ou Transferência |
| PE | Parecimento, Extrativo ou Deterioração |
| OT | Outras Saídas do Imobilizado |
| CI | Conclusão de Imobilização em Andamento - Bem Resultante |

 A tabela dinâmica criada com os valores acima deve ser vinculada ao campo complementar TPMOVCIAP.

* **Configuração do processo**

Para cada lançamento fiscal que controla crédito de ativo permanente, deve ser informado o tipo de movimentação do bem ou componente, conforme os tipos listados na tabela dinâmica acima.  
O tipo de movimentação dos demais lançamentos será gerado automaticamente pelo sistema da seguinte forma, seguindo a legislação do [Guia Prático EFD ICMS IPI](http://sped.rfb.gov.br/pasta/show/1573):

| Código | Descrição |
| --- | --- |
| IM | Imobilização de bem individual (Entradas de bens no período de apuração que não possuem Bem Principal - Cadastro de bem campo "agregado" não preenchido) |
| IA | Imobilização em Andamento - Componente (Entrada de bens no período de apuração que possuem Bem Principal - Cadastro de bem campo "agregado" preenchido) |
| SI | Saldo inicial de bens imobilizados |
| BA | Baixa do Saldo de ICMS - Fim do período de apropriação |

***Observação***: O Saldo Inicial é gerado para os bens que foram adquiridos em período de apuração anterior ao período em que a rotina está sendo gerada e que ainda não foram baixados.  
  
A Baixa do Saldo – BA, é gerado com bens baixados pelo fim do período de apropriação no ICMS no período apuração. Para esses bens, além do tipo de movimentação "BA" será gerado, também, um registro com o tipo de movimentação "SI". No registro gerado pelo BA, os campos "NUM\_PARC", "VL\_PARC\_PASS" e "VL\_PARC\_APROP" não serão apresentados.  
  
Existem dois métodos adotados pelas SEFAZ para o reconhecimento/aproveitamento de crédito de ICMS sobre Ativo Imobilizado para os casos de Bens em Construção: o Crédito pelo Componente e o Crédito pelo Bem Resultante / Final. As Filiais deverão adotar somente um método, que são:

**Apuração por Crédito componente**

* Os registros do bloco G só serão gerados para lançamentos fiscais que tenham o CFOP na faixa X.551 a X.555 e seu tipo de ICMS de compra de Ativo Imobilizado.
* Não Gera CI;
* IA gerado automático (se possuir "agregado" no cadastro de bem);
* Será gerado IA caso bem entrou no período de apuração do SPED Fiscal e SI nos períodos posteriores até que termine o crédito de 48 meses;

* Lançamentos anteriores a implantação do sistema deverão ser lançados via manutenção CIAP, e demais períodos via lançamentos fiscais de entrada com regra de CFOP´s acima;

**Apuração por Crédito Bem resultante**

* Os registros do bloco G só serão gerados para lançamentos fiscais que tenham o CFOP na faixa X.551 a X.555 e seu tipo de ICMS seja diferente de compra de Ativo Imobilizado.
* CI deverá ser gerado manualmente no PVA;
* IA gerado automático (se possuir "agregado" no cadastro de bem);
* IA gerado caso o bem entrou no período de apuração do SPED. NÃO gera SI nos períodos posteriores, pois o crédito será controlado pelo CI. Este CI deverá ser informado manualmente no PVA no período de conclusão do bem e SI para os períodos posteriores;
* Clientes que implantaram o TOTVS Gestão Fiscal e irão apurar o CIAP pela primeira vez, como IA´s serão somente via lançamentos fiscais de entrada conforme regra de CFOP´s acima, e entraram no período de apuração do arquivo, o CI deverá ser informado manualmente no PVA, e os IA´s deste também manualmente caso for o primeiro arquivo. (vide regra abaixo);
* No primeiro arquivo, caso o usuário informe manualmente um SI originado de um CI ou um CI no período de apuração, deverá conter no registro G130 e filhos as informações de todos componentes deste SI originado de CI ou componentes do CI que deverão ser também informados manualmente no arquivo.  
    
  ***Nota!***As informações de código de conta analítica (registro 0300), código do centro de custo (registro 0305) e Código da natureza da conta/grupo de contas (registro 0500) só serão enviadas para o arquivo magnético se os aplicativos TOTVS Gestão Patrimonial e TOTVS Gestão Contábil estiverem instalados e configurados. Caso contrário essas informações devem ser informadas diretos no sistema PVA.
