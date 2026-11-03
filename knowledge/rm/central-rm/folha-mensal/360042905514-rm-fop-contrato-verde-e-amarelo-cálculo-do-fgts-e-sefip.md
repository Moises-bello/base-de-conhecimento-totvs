---
article_id: 360042905514
category: Folha Mensal
content_hash: 0b028a6625c41ed3478f30bfd85204638b877ac16ee658fec3856fbd173fa291
fetched_at: '2026-06-28T22:46:59.509436+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RM - FOP - Contrato Verde e Amarelo: Cálculo do FGTS e SEFIP'
type: support-article
updated_at: '2021-06-21T13:22:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042905514-RM-FOP-Contrato-Verde-e-Amarelo-C%C3%A1lculo-do-FGTS-e-SEFIP
---

**Dúvida**Como realizar o cálculo do FGTS 2% para funcionários na modalidade Contrato Verde e Amarelo e como gerar a SEFIP?  
   
 **Ambiente**RM – Folha de pagamento – A partir dos Patches 12.1.27.121 | 12.1.26.178  |  12.1.25.230  |  12.1.24.281  
  
**Solução**No caso do FGTS, as empresas contratantes ganharão desconto na hora de recolher o dinheiro para o fundo. Ao invés de realizarem o pagamento de 8% da alíquota em cima do salário do trabalhador, a taxa cairá para 2% com esse tipo de contrato.  
 **Alteração no Produto Folha de Pagamento**Para atender as normas estabelecidas acima, foram necessárias adequações em algumas rotinas. Orientamos ao usuário a proceder conforme documentado abaixo:  
 ***SEFIP***Foi publicada a Circular Caixa nº 888 em 07 de Janeiro de 2020, com orientações para o trabalhador Contrato Verde e Amarelo, sendo estabelecido que:

* A categoria do trabalhador que deve ser informada é a 07, sendo que a mesma teve seu nome alterado para Aprendiz - Lei n°10.097/2000 - Contrato Verde/Amarelo MP905.
* Incluída a movimentação do trabalhador X1 - Trabalhador com contrato Verde e Amarelo, que deve ser utilizado exclusivamente para empregados com contrato Verde Amarelo com admissão a partir de 01/01/2019, devendo ser informado pelo empregador em todos os recolhimentos indicando, como data de movimentação a data da admissão do trabalhador.

O processo da Geração da SEFIP foi adequado para atender a regra estabelecida pela Circular nº 888. Para que seja enviado o Código de Categoria e a movimentação do trabalhador é necessário que o vínculo de Contrato Verde e Amarelo tenha as informações do Código de Categoria e Tipo de Funcionário conforme orientado no link [Cadastro de Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=528465156).   
  
 *Exemplo*

Funcionário com contrato verde Amarelo admitido em 06/01, com salário mensal de 1200,00, teve as seguintes verbas incidentes em FGTS:

![](https://tdn.totvs.com/download/attachments/533740337/image2020-2-5_14-7-53.png?version=1&modificationDate=1580922473453&api=v2)

No programa SEFIP 8.4 é possível verificar a base de Cálculo e o código de movimentação do trabalhador:

![](https://tdn.totvs.com/download/attachments/533740337/image2020-2-5_14-29-53.png?version=1&modificationDate=1580923793730&api=v2)  ![](https://tdn.totvs.com/download/attachments/533740337/image2020-2-5_14-36-11.png?version=1&modificationDate=1580924171867&api=v2)

E será calculado o recolhimento do FGTS considerando a alíquota de 2% sobre a base informada:

![](https://tdn.totvs.com/download/attachments/533740337/image2020-2-5_14-49-25.png?version=1&modificationDate=1580924965747&api=v2&effects=drop-shadow)  
  
Informações sobre Cadastro de Funcionários no Contrato Verde e Amarelo, [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=528465156)Informações sobre lançamento de Folha no Contrato Verde e Amarelo, [clique aqui.](https://tdn.totvs.com/display/public/LRM/Movimento+Mensal)  
  
Informações sobre Rescisões no Contrato Verde e Amarelo, [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=531010306)  
  
Informações sobre Guia de INSS, Encargos, SEFIP/FGTS no Contrato Verde e Amarelo, [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=533740337)
