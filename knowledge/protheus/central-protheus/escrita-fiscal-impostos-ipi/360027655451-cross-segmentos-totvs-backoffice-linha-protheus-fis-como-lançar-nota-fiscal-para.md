---
article_id: 360027655451
category: Escrita Fiscal - Impostos - IPI
content_hash: 86c57e17cb19c5472adfa752a9c854b10f0ea452761f3d76ee4c1f6ffc61068c
fetched_at: '2026-06-28T22:39:29.005697+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como lançar nota
  fiscal para Comerciante Não Atacadista - IPI?
type: support-article
updated_at: '2022-10-05T19:02:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027655451-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-lan%C3%A7ar-nota-fiscal-para-Comerciante-N%C3%A3o-Atacadista-IPI
---

**Dúvida**MP - FIS - Como lançar nota fiscal para Não Atacadista - IPI  - 50% de Crédito - Comerciante Não Atacadista?

**Ambiente**Protheus -  A partir da versão 11.80  
  
**Solução**

 Por ser um benefício fiscal os valores de IPI desta operação devem ser tratados como outros créditos na página de Demonstrativo de Apuração do Imposto.  
  
Quando é efetuado o lançamento de uma nota onde o fornecedor trata-se de comerciante atacadista não contribuinte de IPI, o valor do IPI não poderá ser considerado como uma operação tributada e por esse motivo a tes deverá ser configurada da seguinte forma:  
  
Calc.IPI (F4\_IPI) = R (Comerciante não atacadista)  
L.Fiscal IPI (F4\_LFIPI) = Outros  
  
Efetuando o lançamento da nota com essa configuração, o sistema irá gravar o valor do IPI corretamente na apuração, gerando o crédito de 50%, porém esse valor não será destacado nos livros fiscais pois não trata-se de um valor tributado em nota fiscal.   
  
  
Obs.: atentar-se no trecho da documentação:  
  
Conclui-se que com a entrada e orientação da EFD ICMS/IPI a nota fiscal de aquisição de insumos, fornecidos por comerciante atacadista não-contribuinte, sem destaque do IPI, com destino a industrialização ou comercialização, deverá ser escriturada sem direito ao crédito no Registro C100, pai e filhos, e o crédito de 50% previsto no artigo 227 do (Decreto 7212/2010) deve ser apropriado por meio de ajuste no Registro E530 e E531.

Para gerar o Registro E531, precisa configurar na TES o código de relfexo

Código Reflexo:  
Base = Base IPI  
Alíquota = Aliq IPI  
Valor = Valor IPI

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9356014135831)

Lançamento da nota fiscal de entradas

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9356117218455)

Parametro

MV\_IPIATAC = .T.

Apuração do IPI

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9356157038743)

Desta forma, o valor correspondente ao crédito de 50% do IPI, não irá compor o valor total da nota fiscal, sendo este crédito, apropriado por intermédio dos ajustes na Apuração do IPI.  
Lembrando que os livros registros de entrada, saida e apuração de ICMS e IPI foram substituídos pela EFD ICMS/IPI, versão eletrônica dos livros, sendo utilizando por alguns contribuintes como relatório auxiliar.
