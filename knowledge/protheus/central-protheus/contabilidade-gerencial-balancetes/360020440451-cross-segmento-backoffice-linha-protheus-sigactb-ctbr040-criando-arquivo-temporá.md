---
article_id: 360020440451
category: Contabilidade Gerencial - Balancetes
content_hash: a48fb6e27a81febd5ccff8ddec37e60fdfebfca6c202d561d53547b6e881c75f
fetched_at: '2026-06-28T22:41:04.134981+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR040 - Criando Arquivo
  Temporário
type: support-article
updated_at: '2022-04-18T19:14:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020440451-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR040-Criando-Arquivo-Tempor%C3%A1rio
---

**Ocorrência**No módulo da Contabilidade Gerencial ao emitir o relatório CTBR040, fica apenas na tela "Criando Arquivo Temporário", e não emite o relatório.

![CAT_-_arquivo_temp.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016241752/CAT_-_arquivo_temp.png)  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Causa**Esse incidente ocorre devido a estrutura do Plano de Contas Contábil estar incorreto.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes procedimento:  
1 - Acesse a rotina CTBA170 - Valida Plano de Contas.  
2 - Preencha os parâmetros.  
  
O sistema emite o relatório com as inconsistências do Plano de Contas, sendo necessário efetuar o ajuste. Após isso validar novamente a emissão do relatório CTBR040 - Balancete Modelo 1.

Saiba mais:

* <http://tdn.totvs.com/display/public/PROT/CTB0066_Balancete_em_looping>
* [MP - SIGACTB - CTBA102 Lentidão envolvendo processos de contabilização ou atualização de saldos contábeis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006878452-MP-SIGACTB-CTBA102-Lentid%C3%A3o-envolvendo-processos-de-contabiliza%C3%A7%C3%A3o-ou-atualiza%C3%A7%C3%A3o-de-saldos-cont%C3%A1beis?source=search)
* [MP - SIGACTB - CTBR400: Lentidão na impressão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006983291-MP-SIGACTB-CTBR400-Lentid%C3%A3o-na-impress%C3%A3o?source=search)
* [MP - SIGACTB - Erro no arquivo temporário ao gerar relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016501852-MP-SIGACTB-Erro-no-arquivo-tempor%C3%A1rio-ao-gerar-relat%C3%B3rios-?source=search)
