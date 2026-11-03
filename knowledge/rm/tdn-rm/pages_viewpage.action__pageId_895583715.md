---
content_hash: 6f060fff85a469003ab7560b8ac900ffc7ef79202185914d7a87e71614375450
fetched_at: '2026-06-29T00:12:01.396604+00:00'
page_id: '895583715'
product: rm
source: tdn-rm
title: SPED Fiscal Alterações do Layout 2025 - Versão 3.1.8
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=895583715
version: 12
---

Com essa atualização, você terá à disposição todas as ferramentas necessárias para gerar e enviar a declaração de forma precisa e eficiente, de acordo com as alterações estabelecidas no mais recente manual fornecido pelo governo.  
  
Lembrando que é necessário atualizar para um dos patches abaixo ou superior, a fim de garantir o pleno funcionamento do sistema

* 12.1.2410.128
* 12.1.2406.197
* 12.1.2402.252
1lefttrue1Bloco 0

* Registro 0000:

Na tela de geração da rotina, alterado a versão para “**019**”. Essa versão só é válida a partir de 01/01/2025.

2Bloco D

As alterações dos Registros D100 e D130 são voltadas para o CTe Simplificado e serão atendidas sob demanda, ou seja, neste primeiro momento não foram desenvolvidas no produto padrão.

* Registro D100:

Alterações de preenchimento dos campos :  
**Campo 18** - Se CT-e simplificado (COD\_MOD 57 e TP\_CTe 4 ou 5), o valor deve ser igual à soma do campo VL\_FRT do(s) registro(s) D130 existentes

**Campo 24** - COD\_MUN\_ORIG: Código do município de origem do serviço, conforme a tabela IBGE (Preencher com 9999999, se Exterior) - Preencher com “9999998” quando se tratar de CT-e simplificado ou substituição de CT-e simplificado.

**Campo 25** - COD\_MUN\_DEST: Código do município de destino, conforme a tabela IBGE (Preencher com 9999999, se Exterior) - Preencher com “9999998” quando se tratar de CT-e simplificado ou substituição de CT-e simplificado.

* Registro D130:

Alterações de preenchimento dos campos :

**Campo 02** - COD\_PART\_CONSG Código do participante (campo 02 do Registro 0150) - consignatário, se houver

**Campo 03** - COD\_PART\_RED Código do participante (campo 02 do Registro 0150) - redespachado, se houver

**Campo 05** - COD\_MUN\_ORIG Código do município de origem do serviço, conforme a tabela IBGE(Preencher com 9999999, se Exterior)

**Campo 06** - COD\_MUN\_DEST Código do município de destino, conforme a tabela IBGE(Preencher com 9999999, se Exterior)

falseRoda Pé Sped Fiscalfalseblankhiddenfalse14411
