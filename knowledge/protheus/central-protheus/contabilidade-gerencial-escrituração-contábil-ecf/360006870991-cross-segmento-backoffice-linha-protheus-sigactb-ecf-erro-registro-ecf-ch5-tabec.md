---
article_id: 360006870991
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 626f4e0d464510498ef7a2bd77a2040ff12bc4b72135b5021eb151e4e5342420
fetched_at: '2026-06-28T22:40:47.306905+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF -  ERRO: Registro
  _ECF( CH5_TABECF) Conta Referencial _ (CH5_CTAREF)'
type: support-article
updated_at: '2023-07-19T19:25:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006870991-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-ERRO-Registro-ECF-CH5-TABECF-Conta-Referencial-CH5-CTAREF
---

**Ocorrência**

Erro 1 - Linha: 2 - O valor '01' informado na coluna 3 para o campo Tabela Registro ECF ( CH5\_TABECF ) somado ao valor '1.01.01.01.00' informado na coluna 4 para o campo Conta Referencial ( CH5\_CTAREF ) não existe na base de dados.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409634090775)

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – **A partir da versão 12**  
  
**Solução**

Para a correção deste problema, deve-se realizar o seguinte processo: <http://tdn.totvs.com/pages/releaseview.action?pageId=284470956>

Compartilhamento das tabelas [ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-TABELAS-ECD-E-ECF-COMPARTILHAMENTO?source=search)

Compartilhamento das tabelas do TAF :

<https://tdn.totvs.com/display/public/TAF/TAF0181+Tabelas+para+compartilhamento+-+ECF>

<https://tdn.totvs.com/pages/releaseview.action?pageId=464949275#Reinf--56521921>

Erro 1 - Linha: 2 - O valor '01' informado na coluna 3 para o campo Tabela Registro ECF ( CH5\_TABECF ) somado ao valor '1.01.01.01.00' informado na coluna 4 para o campo Conta Referencial ( CH5\_CTAREF ) não existe na base de dados.  
[MP - SIGACTB - ECF - ERRO: Registro \_ECF( CH5\_TABECF) Conta Referencial \_ (CH5\_CTAREF)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006870991-MP-SIGACTB-ECF-ERRO-Registro-ECF-CH5-TABECF-Conta-Referencial-CH5-CTAREF-?source=search)  
  
|T010|20110211|01|1|5|1110105|CAIXA - FUNDO FIXO RG - P-63|||11101|20110211|1|  
|T010AA||01|1.01.01.01.00|2020|  
  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/4IwKIwN4Bcxfdk5koe4CKTxi1/?name=inline-1150271686.png)

* [Layout Único](https://tdn.totvs.com/pages/viewpage.action?pageId=498722271) do TAF

![](https://tdn.totvs.com/download/attachments/284470956/image2017-7-7%2012%3A13%3A15.png?version=1&modificationDate=1499441129000&api=v2)

**Registro J050 - Plano de Contas do Contribuinte**  
Tabelas - C1O (Plano de Contas Contábeis) / C2R (Natureza Contra Grupo Contábil)  
Registro do Layout TOTVS - **T010**  
Rotina - **TAFA060**(Cadastro de Plano de Contas)  
**Registro J051 - Plano de Contas Referencial**  
Tabela - C1P (Centro de Custo) **CH5** (Plano de Contas Referencial)  
Registro do Layout TOTVS - **T010AA**  
Rotina - **TAFA060** (Cadastro de Plano de Contas)  
[http://tdn.totvs.com/pages/releaseview.action?pageId=192089512](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)  
  
Através da rotina TAFA060 verificar a validação do campo CH5\_TABECF , veja que o sistema busca da tabela CHA  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/5HnyLKLVFevzf7Q7IMxZikGxa/?name=inline-1572048525.png)  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/0CTn4uc6SQAWPjftRo98dmsbO/?name=inline334103293.png)​  
  
Veja na CHA que a conta em questão não existe     
Obs : CHA é atualizada pela autocontida do TAF a contabilidade não alimenta está tabela.  
  
![](https://totvssuporte.zendesk.com/attachments/token/5Y3OCwXj0lu5oSvPgrqsUC3Uv/?name=inline-622576335.png)​  
  
Veja que a conta não existe na CHA   
  
![](https://totvssuporte.zendesk.com/attachments/token/l94S07pXtVtl7I2ZTMibHMViz/?name=inline966125416.png)  
  
A tabela CHA é atualizada pelo desenvolvimento do TAF via Autocontida com base na tabelas dinâmicas da receita   
  
Tabela dinâmica da receita :<http://sped.rfb.gov.br/arquivo/show/5718>   
  
Veja que na tabela dinâmica da receita a conta 1.01.01.01.00 não existe para L100A  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/ANdBoDSCRfkHOjOPTPu0iDh6h/?name=inline1720393085.png)  
  
Diante disso necessário que a contadora avalie o plano referencial que esta seno utilizado  
  
OBS  :  
  
  
A receita é responsavel por liberar o plano referencial para entregas das obrigações, a totvs disponibiliza modelo que não devem ser utilizado para entrega das obrigações. Diante disso solicito que verifique junto a receita o plano referencial atualizado .Segue abaixo o procedimento para converter e importar o arquivo  
  
Como converter e importar o plano referencial da Receita Federal  
  
[MP - SIGACTB - Como importar Plano referencial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007547712-MP-SIGACTB-Como-importar-Plano-referencial-?source=search)  
  
  
Arquivos Modelos - Plano Referencial  
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=189314312>

Para maiores informações, acessar o link: <http://tdn.totvs.com/display/public/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF>

Página Centralizadora: <http://tdn.totvs.com/display/PROT/ECF>

Veja também : [MP - SIGACTB - CTBS001 - Atualização das Tabelas Autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006985071-MP-SIGACTB-CTBS001-Atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-)
