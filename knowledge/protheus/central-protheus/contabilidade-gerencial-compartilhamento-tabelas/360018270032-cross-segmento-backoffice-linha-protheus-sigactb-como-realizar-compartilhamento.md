---
article_id: 360018270032
category: Contabilidade Gerencial - Compartilhamento Tabelas
content_hash: 195adbc91af3e0d694debbf8c70bb75c073b2b6037e22bc6efc0334848e2fe4c
fetched_at: '2026-06-28T22:40:57.813737+00:00'
product: protheus
section_id: 1500001537461
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Como realizar compartilhamento
  de tabelas no Contabilidade Gerencial (SIGACTB)?'
type: support-article
updated_at: '2022-03-29T20:04:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB
---

**Dúvida**Como realizar compartilhamento de tabelas no Contabilidade Gerencial (SIGACTB)?

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

De acordo com a necessidades é possível modificar a situação de compartilhamento padrão das tabelas utilizadas no **Contabilidade Gerencial (SIGACTB)** de forma a melhor atender cada estrutura.

É considerada divisão das tabelas em dois grupos: **Cadastros** e **Movimentos/Saldos**, sendo assim as configurações possíveis são:

| CADASTROS | MOVIMENTO/SALDOS |
| --- | --- |
| Exclusivos | Exclusivos |
| Compartilhados | Exclusivos |
| Compartilhados | Compartilhados |

Considerando as seguintes tabelas:  
  
Cadastros

* CT1, CT5, CT8, CT9, CTA, CTB, CTD, CTE, CTG CQD, CTH, CTJ, CTL, CTN, CTO, CTP, CTR, CTS, CTT, CV5, CV9, CVA, CVB, CVC, CVD,CVE,CVF e demais cadastros.

**Atenção:**Em caso de alteração do compartilhamento da tabela CT1, a mesma deve ser efetuada para a tabela CVD, CVN e vice-versa, pois uma depende da outra no momento da gravação e geração de informação. **É obrigatório a utilização do mesmo compartilhamento para essas tabelas.**

Movimentos/Saldos

* CT2, CT3, CT4, ,CT7, CTI, CTU, CTV, CTW, CTX, CTY, CT6, CTC, CTF, CTK, CTZ, CV1, CV2, CV3, CV4, CV6, CV7, CV8 e CVO.
* A partir da versão **12** do **Microsiga Protheus**, as seguintes tabelas também devem ser consideradas: CQ0, CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ07 CQ8, CQ9 e CQA

Caso ocorra o compartilhamento das tabelas que estejam divergente entre as demais tabelas do seu grupo, o sistema poderá eventualmente trazer informações incorretas ou até gerar erro. Não é recomendado esta prática.

**Aviso:**Não é recomendável a alteração de compartilhamento das tabelas do ambiente de **Contabilidade Gerencial**, pois em alguns casos pode parar de funcionar e/ou gerar erros sistêmicos.

**Saiba mais:**  
[MP - SIGACTB: Como alterar o compartilhamento de tabelas após bloqueio realizado a partir da LIB versão 20181015](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026077191-MP-SIGACTB-Como-alterar-o-compartilhamento-de-tabelas-ap%C3%B3s-bloqueio-realizado-a-partir-da-LIB-vers%C3%A3o-20181015?source=search)

<http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB>
