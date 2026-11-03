---
article_id: 360034164074
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 09230cac3c4ecd59c9c213fec7aebddd8ca820b8a16e306c9533fc43212975ec
fetched_at: '2026-06-28T22:40:48.735778+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - X320 COMO GERAR '
type: support-article
updated_at: '2022-06-03T22:25:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034164074-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-X320-COMO-GERAR
---

**Dúvida**Como gerar o registro **X320 - Operações com o Exterior – Importações (Saída de Divisas) ?**  
  
**Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão 11.80  
  
**Solução**

Para gerar bloco **X320 - Operações com o Exterior – Importações (Saída de Divisas) ,**deve haver um **documento de entrada/Nota de importação** com os cadastros de produto e fornecedor com as seguintes configurações:

**Através da rotina MATA010 Produto:** 

* Origem (B1\_ORIGEM) preenchido com:

1- Estr.(Importacao Direta),   
6 - Estr-Import dir,sem similar nac,consta na lista CAMEX ou   
7 - Estr-Adq intern,sem similar nac,consta na lista CAMEX 

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044234234/mceclip2.png)  
 

* Pos.IPI/NCM (B1\_POSIPI) diferente de vazio.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045095833/mceclip3.png)

**Através da rotina MATA020** **Fornecedor:**

* Tipo ( A2\_TIPO ) preenchido com: 'X'

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044233494/mceclip0.png)

* P. Vinculo ( A2\_VINCULO ) diferente de vazio.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045095013/mceclip1.png)

**Através da rotina central de escrituração CTBS001** ao gerar a ECF deve seleciona "Sim" para DIPJ

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045096293/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044234954/mceclip5.png)

Através da APSDU acesse as tabelas TAFST1 e TAFST2  e veja se o bloco T098 foi gerado  
  
  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração  
     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada  
  
   Ex: |T098|20181231|000000001|02|IMPORTAÇÃO X320|0,00||0,00||2|0,00|0,00|0,00|0,0000|0,0000|0,0000|||

* Verifique o TAFSTATUS = 3

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044235474/mceclip6.png)

**Através da rotina TAFTICKET** também é possível visualizar o bloco T098

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044235714/mceclip8.png)

**Através do layout do TAF**  verifique se foi gerado corretamente  
  
[Último Layout Disponível](http://tdn.totvs.com/pages/releaseview.action?pageId=498722271)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045096853/mceclip7.png)

**A rotina TAFA335** do TAF e veja se o bloco X foi gerado 

[Registro X320 - Operações com o Exterior – Importações (Saída de Divisas)](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoK-SaldosdasContasCont%C3%A1beiseReferenciais)

* Tabelas - CFV (Oper.Exterior - Exportações) / C0A (Nomenclatura Comum Mercosul) / CHJ (Unidade de Medida ECF ) / CZT (Codigo CNC) / CZU (Tipo de Moeda)
* Registro do Layout TOTVS - T098
* Rotina - TAFA335 (Operacoes com o Exterior - Importações)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045097313/mceclip9.png)

Através da rotina TAFOBRIG gere o arquivo TXT 

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045097553/mceclip10.png)

Veja se o arquivo gerou o dados corretamente  
  
![](https://totvssuporte.zendesk.com/attachments/token/qghe8GD4hX0Z2tdOvRHDtFgdo/?name=inline91502461.png)

|X320|: Identificação do tipo do registro.  
|000000001|: Número de ordem para identificar a operação.  
|02|: Tipo de importação (02-Serviços).  
|IMPORTACAO X320|: Descrição do bem.  
|0,00|: Total da operação (R$ 0,00).  
||: Código NCM do bem.  
||: Quantidade.  
||: Unidade de medida .  
|PRL20|: Método do preço de revenda menos lucro (PRL 20%).  
|0,00|: Valor do preço médio ponderado de aquisição nas importações apurado no ano-calendário (R$ 0,00).  
|0,00|: Valor do preço médio ponderado de aquisição nas importações praticado no ano-calendário (R$ 0,00).  
|0,00|: Valor do ajuste (R$ 0,00).  
|0,00|: Juros   
|0,00|: Taxa de Juros Mínima.  
|0,00|: Taxa de Juros Máxima..  
||: Código CNC  
||: Moeda

Saiba mais :

[Relatório MATR933](https://tdn.totvs.com/pages/releaseview.action?pageId=6076191)

[MP - SIGACTB - ECF - X320 - UNIDADE DE MEDIDA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020084511-MP-SIGACTB-ECF-X320-UNIDADE-DE-MEDIDA-?source=search)

[MP - SIGACTB - ECF -Como realizar a geração dos blocos X e Y?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006827952-MP-SIGACTB-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-dos-blocos-X-e-Y-?source=search)

[Relatório Transfer Pricing - Preço de Transferência](http://tdn.totvs.com/pages/releaseview.action?pageId=6076191)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)
