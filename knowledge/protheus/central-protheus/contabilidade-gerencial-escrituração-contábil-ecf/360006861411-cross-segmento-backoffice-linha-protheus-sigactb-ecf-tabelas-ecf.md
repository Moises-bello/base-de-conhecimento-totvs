---
article_id: 360006861411
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 374dde4bf72900742497ae0f71a5b64f73d575fe8e5ae30d639b786e7c962acb
fetched_at: '2026-06-28T22:40:47.428326+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Tabelas ECF
type: support-article
updated_at: '2022-05-10T13:23:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Tabelas-ECF
---

**Dúvida**

Quais tabelas são populadas na geração da ECF

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

* Através do Modulo Contábil  são populadas as Tabela Cs
* [Compartilhamento das TABELAS ECD E ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF?source=search)
* Através da rotina CTBS001 é possível visualizar se as tabelas foram populadas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007120491/mceclip0.png)

* Através modulo TAF os Blocos T são populadas nas tabelas  TAFST1 e TAFST2
* [Tipos de Registros Gerados (rotina do TAF ,para cada bloco)](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512)
* [Como devo utilizar o compartilhamento de tabelas do TAF? (Tabelas autocontidas não devem ter seucompartilhamento alterado)](http://tdn.totvs.com/pages/releaseview.action?pageId=342301375)
* Através da rotina TAFA099 e tabelas  T2U (Cadastro de Tabelas Dinâmicas) são apresentadas todas as autocontidas.
* [Conheça o Layout de Integração](http://tdn.totvs.com/pages/releaseview.action?pageId=187534666)
* [Blocos/Registros](http://tdn.totvs.com/pages/releaseview.action?pageId=192094180)
* Através da APSDU é possível verificar se os blocos foram gerado dentro do  TAFMSG   
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007120891/mceclip2.png)

* Registro            Tabela              [TAFST1/TAFST2](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)  
  Reg 0010          CSZ                  T127  
  Reg 0020          CSZ                  T127  
  Reg 0030          Cadastro de Empresas - SIGAMAT  
  Reg 0035          CSR                  T01AM  
  Reg 0930          CS8                  T002  
  Reg J050           CS3                  T010  
  Reg J051           CS4                  T010AA  
  Reg J053           CST                  T010AB  
  Reg J100           CS5                  T0111  
  Reg K155          CSC                  T087AA  
  Reg K156          CSK                  T087AB  
  Reg K355          CSC                  T087AC  
  Reg K356          CSK                  T087AD  
  Reg L100          CSC / CSK         T088AA quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial ([CVD, CVN, CT1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search))  
  Reg L100          CSD / CSE         T088AA quando utilizado Visão Gerencial. ([CTS, CVE, CVF, CTN)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)  
  Reg L200          CSD / CSE         T088AB  
  Reg L210          CSD / CSE         T088AC  
  Reg L300          CSC / CSK         T088AD quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial ([CVD, CVN, CT1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search))  
  Reg L300          CSD / CSE         T088AD quando utilizado Visão Gerencial. ([CTS, CVE, CVF, CTN)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)  
  Reg P100          CSC / CSK         T092AA quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial ([CVD, CVN, CT1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search))  
  Reg P100          CSD / CSE         T092AA quando utilizado Visão Gerencial. ([CTS, CVE, CVF, CTN)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)  
  Reg P130          CSD / CSE         T092AB   
  Reg P150          CSC / CSK         T092AC quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial ([CVD, CVN, CT1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search))  
  Reg P150          CSD / CSE         T092AC quando utilizado Visão Gerencial. ([CTS, CVE, CVF, CTN)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)  
  Reg P200          CSD / CSE         T092AB  
  Reg P230          CSD / CSE         T092AB  
  Reg P300          CSD / CSE         T092AB  
  Reg P400          CSD / CSE         T092AB  
  Reg P500          CSD / CSE         T092AB  
  Reg T120          CSD / CSE         T093AA  
  Reg T150          CSD / CSE         T093AA  
  Reg T170          CSD / CSE         T093AA  
  Reg T181          CSD / CSE         T093AA  
  Reg U100          CSC / CSK         T094AA quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial ([CVD, CVN, CT1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search))  
  Reg U100          CSD / CSE         T094AA quando utilizado Visão Gerencial. ([CTS, CVE, CVF, CTN)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)  
  Reg U150          CSC / CSK         T094AC quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial ([CVD, CVN, CT1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search))  
  Reg U150          CSD / CSE         T094AC quando utilizado Visão Gerencial. ([CTS, CVE, CVF, CTN)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)  
  Reg U180          CSD / CSE         T094AB  
  Reg U182          CSD / CSE         T094AB  
  Bloco X             CSD / CSE         T096 para os registros exportados pelo SIGACTB   
  Bloco Y             CSD / CSE         T096 para os registros exportados pelo SIGACTB

Veja mais

[MP-SIGACTB - ECF Tabelas Relacionadas a Apuração IRPJ CSLL no TAF (Lalur)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034815894-MP-SIGACTB-ECF-Tabelas-Relacionadas-a-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-Lalur-?source=search)
