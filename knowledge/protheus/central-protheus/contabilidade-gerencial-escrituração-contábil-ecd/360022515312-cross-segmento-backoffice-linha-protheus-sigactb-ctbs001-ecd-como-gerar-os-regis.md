---
article_id: 360022515312
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 5880df8f7c84a288aba0b28086025420e16b5ea67c32cf7f28999150b00bc7fd
fetched_at: '2026-06-28T22:40:44.830202+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001  : ECD COMO
  GERAR  OS REGISTROS I050 E I051: PLANO DE CONTAS E PLANO DE CONTAS REFERENCIAL'
type: support-article
updated_at: '2024-09-26T13:56:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022515312-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-COMO-GERAR-OS-REGISTROS-I050-E-I051-PLANO-DE-CONTAS-E-PLANO-DE-CONTAS-REFERENCIAL
---

**Dúvida**  
Como gerar os registro I050 Plano de contas e I051 Plano de contas referencial  o arquivo da ECD

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – **A partir da versão 12**

**Requisitos**

* Aplique [**Pacotes de Atualização - Contabilidade**](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777) seguindo as instruções [Aqui descritas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-MP-SIGACTB-Como-atualizar-o-ECD-?source=search)
* **Aplique o Pacote Acumulado Contábil + [Instalação de Procedure nele existente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8388802894615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-instalar-a-nova-gest%C3%A3o-de-procedures-e-as-procedures?source=search):**

**Solução**

Necessário revisar:

* o compartilhamento das tabelas esteja correta
* Dados estejam cadastrados
* Veja se ordem dos campos das tabelas foram alteradas

CTS    Entidade Gerencial  
CVE    Visão gerencial  
CVF    Itens da Visão Gerencial  
CTN    Configuração de Livros Contábeis  
  
CT1 - PLANO DE CONTA  
CVD - Plano referencial  
CVN - Plano de contas X plano referencial.

CS3 Plano de contas   
CS4 Plano de conta referencial

Obs: necessário que as tabelas  mencionada esteja com o compartilhamento correto :[compartilhamento de tabelas no Contabilidade Gerencial (SIGACTB)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search)e o compartilhamento das [TABELAS ECD E ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF?source=search)

* Configure [MV\_CTBSPRC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-MP-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD?source=search)
* vverifique se os campos [X2\_AUTREC, X2\_TAMFIL, X2\_TAMUN, X2\_TAMEMP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018497311-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA190-Campo-Filial-das-tabelas-CQ-n%C3%A3o-est%C3%A3o-sendo-alimentadas?source=search) , das tabelas CT1,CVD,CVN,CS3 e CS4 estão corretos em relação ao SIGAMAT
* Caso esteja gerando o arquivo com  [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)
* Através da rotina de plano de contas referencial(CTBA025) Importe o plano de contas referencial
* [Arquivos Modelos - Plano Referencial](http://tdn.totvs.com/pages/releaseview.action?pageId=189314312)
* Veja [Como importar Plano referencial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007547712-MP-SIGACTB-Como-importar-Plano-referencial-?source=search)
* Através da rotina Cadastro Plano de Contas (CTBA020), é necessário que nas contas sintéticas e analíticas os campos sinalizados abaixo estejam preenchidos.
* Classe da conta (CTI\_CLASSE), Cta superior (CT1\_CTASUP), Nat.Conta (CT1\_SPEDST), NatCta Sped (CT1\_NATCTA).
* Nivel das contas estejam corretos : [I050 : 5 - NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010)
* Verifique cadastro e amarração da conta contábil

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068233333)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067160994)

Caso esteja sendo gerado com centro de custo necessário:

* verifique a amarração da conta contábil ao centro de custo
* Veja detalhes para gerar com o [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)
* Caso possua mais de um centro de custo amarrado a conta contábil deve ser a amarrada a mesma conta referencial , conforme exemplo abaixo

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068234013)

Através da tabela CVD é possível verificar se a  amarração das contas estão corretas  
  
Veja que para o mesmo "Plano ref = CVD\_CODPLA"  foi amarrado vários centro de custo , porem a conta referencial "CVD\_CTAREF" permanece a mesma

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067161174)

Ao gerar o arquivo da ECD Informe:

* as contas que para gerar o I050
* informe as contas referencial  para gerar o I051
* Ao Informar o Codigo do plano referencial o sistema irá gatilhar a versão. esse campo não deve ser informado manualmente , o sistema deve gatilhar

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067161294)

* Informar o parâmetro abaixo para gerar o I051

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070100634)

* Veja se a tabela CS3  foi alimentada com todas as conta contábeis  e de forma de forma correta

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067161394)

* Veja se a CS4 foi alimentada de forma correta

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068234353)

Posteriormente gere o arquivo e veja se foi gerado o I050 e o I051

Veja mais :

* [NATUREZA CONTA CONTABIL - ECD/ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006887272-MP-SIGACTB-CTBA020-NATUREZA-CONTA-CONTABIL-ECD-ECF?source=search)
* [ECD LIMPEZA TABELA CS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026508851-MP-SIGACTB-ECD-LIMPEZA-TABELA-CSB?source=search)
* [Como atualizar o ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-MP-SIGACTB-Como-atualizar-o-ECD-?source=search)
* [ECD PRÉ-REQUISITOS PARA GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834291-MP-SIGACTB-ECD-PR%C3%89-REQUISITOS-PARA-GERAR-?source=search)
* [I050 E I051: GERAR CONTA BLOQUEADA , SEM SALDO ANTERIOR E OU SEM MOVIMENTO NO PERIODO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047812633-MP-SIGACTB-ECD-I050-E-I051-GERAR-CONTA-BLOQUEADA-SEM-SALDO-ANTERIOR-E-OU-SEM-MOVIMENTO-NO-PERIODO?source=search)
* [COD\_CTA\_REF ; Conta não existe no plano de contas referencial informado no registro 0000 (COD\_PLAN\_REF).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048292614-MP-SIGACTB-ECD-I051-COD-CTA-REF-Conta-n%C3%A3o-existe-no-plano-de-contas-referencial-informado-no-registro-0000-COD-PLAN-REF-?source=search)
* [COD\_PLAN\_REF O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048293454-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-I051-COD-PLAN-REF-O-registro-I051-%C3%A9-obrigat%C3%B3rio-quando-existe-c%C3%B3digo-do-plano-de-contas-referencial-informado-no-registro)
* [ECD I050 COD\_CTA\_SUP Conta de nível superior deverá ter a mesma natureza da subconta.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049037713-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-I050-COD-CTA-SUP-Conta-de-n%C3%ADvel-superior-dever%C3%A1-ter-a-mesma-natureza-da-subconta)
* [ECD/ECF GERAR CONTA BLOQUEADA , SEM SALDO ANTERIOR E OU SEM MOVIMENTO NO PERIODO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047812633-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-ECF-GERAR-CONTA-BLOQUEADA-SEM-SALDO-ANTERIOR-E-OU-SEM-MOVIMENTO-NO-PERIODO)
