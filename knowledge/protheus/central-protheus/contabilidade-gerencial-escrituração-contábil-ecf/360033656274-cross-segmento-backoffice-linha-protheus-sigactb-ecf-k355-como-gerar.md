---
article_id: 360033656274
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 3bfc67f9edf3233152488a54873c143ec88fcbe23e703acdf7707f76666620fe
fetched_at: '2026-06-28T22:40:48.786793+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF : K355 COMO GERAR'
type: support-article
updated_at: '2022-06-03T22:34:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033656274-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-K355-COMO-GERAR
---

**Dúvida**

Quais procedimento para gerar o K355 ?  
  
**Ambiente**

Microsiga Protheus  – Contabilidade Gerencial  – A partir da versão 11.80  
  
**Solução**

Para que o bloco seja gerado com centro de custo

* necessário que o centro de custo tenha sido apurado, com isso na apuração de resulto deve ser informado o centro de custo
* caso a apuração já tenha sido executada será necessário estonar a apuração e apurar novamente informando centro de custo
* antes de executar a apuração de resultado emita relatórios de centro de custo para verificar se os saldos (Anterior, Saldo Final) e Movimento estão corretos
* Orientação abaixo para realizar apuração de resultado com centro de Custo  

  <http://tdn.totvs.com/pages/releaseview.action?pageId=226526594>
* Após realizar apuração de resultado emita relatórios de centro de custo para verificar se o centro de custo (001 e 002) foi realmente zerado e o se o saldo gerado no centro de custo de apuração(003) está correto
* caso exista diferença de saldo dos relatórios de centro de custo será necessário revisar os movimentos existente para os centros de custo
* Caso o centro de custo possua saldo anterior , será gerado no arquivo
* o  caso possua centro de custo cadastrado e movimentado em sua a base o sistema irá considerar o movimento e saldos existe nele.

  **Obs:**  Caso não for gerar o Bloco com centro de custo desconsidere os pontos acima

Verifique a amarrada e cadastro da conta (CTBA020)

**Importante** : Ao amarrar mais de uma vez o a conta referencial  , necessário que seja informado centro de custo , caso contrario será apresentado erro de duplicidade na integração com o TAF

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043280094/mceclip0.png)

**Importante** : caso tenha amarrado mais de um centro de custo a conta referencial , será  necessário gerar a ECF informando o parâmetro abaixo , caso contrario será apresentado erro de duplicidade na integração com o TAF

Caso deseja gerar o Bloco com [Centro de custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search) informe "sim" no parâmetro 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043280214/mceclip1.png)

Através da rotina de Escrituração CTBS001 veja se a tabelas formam alimentadas   
  
Registro            Tabela                 
Reg J050           CS3                     
Reg J051           CS4                     
Reg J100           CS5                     
Reg K355          CSC                  

Através da tabela CSC verifique se foi gerado 

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043280314/mceclip2.png)

Através da tabela CS4  verifique se foi gerado 

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044119633/mceclip3.png)

CS5

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043284474/mceclip0.png)

Blocos/Registros – geração no TAF ou na integração  
  
[Registro K355 - Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)

* Tabela - CAF (Saldos Cont. antes Encerram. per)
* Registro do Layout TOTVS - T087AC
* Rotina - [TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL)

Registro            Tabela              TAFST1/TAFST2  
Reg K355          CSC                  T087AC

Na tabela TAFST1 e TAFST2  
- no registro da conta verifique T087AC  
  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração  
     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada  
  
   Ex: |T087AC|31301001|30011010|18000|1|  
  
- Verifique o TAFSTATUS = 3

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044122693/mceclip1.png)

* [Conheça o Layout de Integração](http://tdn.totvs.com/pages/releaseview.action?pageId=187534666)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044249933/mceclip1.png)

Através da rotina TAFA311 e verifique se o bloco foi gerado

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044122773/mceclip2.png)

Exemplo de Preenchimento:  
  
|K355|31301001|30011010|18.000,00|D|  
  
|K355|: Identificação do tipo do registro.  
|31301001|: Código da conta analítica de resultado.  
|30011010|: Código do centro de custos (30011010).  
|18.000,00|: Valor do saldo final da conta de resultado antes do encerramento (R$ 18.000,00).  
|D|: Indicador de situação do saldo final (D = Devedor).

Veja mais : [MP - SIGACTB - ECF : K156 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search)

[MP - SIGACTB - ECF - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search)

[MP - SIGACTB - ECF - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search)
