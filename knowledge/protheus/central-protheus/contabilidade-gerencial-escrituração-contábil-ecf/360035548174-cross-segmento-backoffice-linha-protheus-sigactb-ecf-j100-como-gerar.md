---
article_id: 360035548174
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 7568b59e436a9caaee28716f63bb1be9d97dab6325a1d325b928e3b4c33b482d
fetched_at: '2026-06-28T22:40:48.767581+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF : J100 COMO GERAR'
type: support-article
updated_at: '2025-05-15T17:46:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035548174-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-J100-COMO-GERAR
---

**Dúvida**

Como gerar o registro J100 de centro de custo para ECF?  
  
**Ambiente**  
Microsiga Protheus  – Contabilidade Gerencial  – A partir da versão 11.80  
  
**Solução**

Para que o bloco seja gerado com centro de custo, é importante revisar os itens abaixo:

* Necessário que as tabela CT1,CVD,CVN, CTT [tenham o mesmo compartilhamento](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)
* Necessário que as [Tabelas CS estejam com o Compartilhamento corrreto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-TABELAS-ECD-E-ECF-COMPARTILHAMENTO)
* Necessário que o centro de custo tenha sido apurado, com isso na apuração de resultado deve ser informado o centro de custo;
* Caso o centro de custo possua saldo anterior,movimento no período ou saldo final, sistema irá considerar o movimento e saldos existes nele e será gerado no arquivo;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067003774) Veja com atenção como realizar a [APURAÇÃO DO CENTRO DE CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)

* através da rotina de plano de contas referencial (CTBA025)importe o plano de contas referencial
* [Plano de contas referencial modelo (Clique aqui)](http://tdn.totvs.com/pages/releaseview.action?pageId=189314312)
* Para gerar com centro de custo, solicito que verifique a amarração da conta contábil ao centro de custo através da rotina de Cadastro de plano de conta CTBA020  
    
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046316774)

Caso possua mais de um centro de custo amarrado a uma conta contábil, deve ser a amarrada a mesma conta referencial , conforme exemplo abaixo   
  
Ao amarrar a conta referencial os campos "Tp.Utiliz, Classe Conta, Nat Conta, Entid Superior" deve ser populada automaticamente.  
Obs: Todas as conta Contábeis, precisam estar amarradas ao centro de custo

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047183993)

Através da tabela CVD, é possível verificar se a  amarração das contas estão corretas.

Veja, que para o mesmo "Plano ref = CVD\_CODPLA"  foi amarrado vários centro de custos, porém a conta referencial "CVD\_CTAREF" permanece a mesma.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047184933)

Ao gerar uma revisão informar o parâmetro ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19666008731031)

Com base na documentação abaixo acompanhe a geração da conta em questão , podendo assim identificar o momento que ela esta se perdendo, sendo nas CS, na TAFST1 ,na TAFST2, ou nas rotina do TAF  
  
Registro      Tabela        TASFST1  
Reg J100      CS5           T011  
  
-Verifique se a Tabela CS5  foi alinhada corretamente

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047184993)

-Verifique se a tabela TAFST1 foi alimentada :  
**SEGUE O BLOCO**  
  
Registro      Tabela        TASFST1  
Reg J100      CS5           T011  
  
Blocos/Registros – geração no TAF ou na integração  
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=192094180>

Na tabela TAFST1 e TAFST2  
- no registro da conta verifique T011  
  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração

     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada

   Ex: |T011|19800101|1006|ARMAZENAGEM |19800101|

-veja que é o centro de custo 1006  
- Verifique o TAFSTATUS = 3

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047185913)

Com base na no link abaixo verifique a estrutura do Layout do Bloco T011 –Verifique se esta correto  
  
[07. Conheça o Layout de Integração](http://tdn.totvs.com/pages/viewpage.action?pageId=187534666)  
<http://tdn.totvs.com/pages/releaseview.action?pageId=187534666>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047186053)

**Registro J100 - Centro de Custos**  
· Tabela - **C1P**(Centro de Custo)  
· Registro do Layout TOTVS - T011  
· Rotina - TAFA061 (Cadastro de Centro de Custo)  
<http://tdn.totvs.com/pages/releaseview.action?pageId=192089512>  
Através da rotina TAFA061 verificar se o registro foi criado com o centro de custo em questão  
O exemplo que estamos apresentando é o centro de custo 1006

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046320214)

Veja se o centro de custo foi integrado com todos os dados necessários

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046320414)

Exemplo de Preenchimento:

|J100|01011980|1006|ARMAZENAGEM|

|J100|: Identificação do tipo do registro.  
|01011980|: Data da alteração (01/01/1980).  
|1006|: Código do centro de custos.  
|ARMAZENAGEM|: Nome do centro de custos.

Saiba Mais:

[MP - SIGACTB - ECF : K355 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033656274-MP-SIGACTB-ECF-K355-COMO-GERAR?source=search)

[MP - SIGACTB - Como realizar Apuração de resultados dentro do Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search)

[MP - SIGACTB - ECF : K355 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033656274-MP-SIGACTB-ECF-K355-COMO-GERAR?source=search)

Não gera Registro L210: [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006856251-MP-SIGACTB-ECF-N%C3%A3o-gera-registro-L210)

Tabelas ECF: [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)

Parâmetro de Integração CTB/TAF: [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)
