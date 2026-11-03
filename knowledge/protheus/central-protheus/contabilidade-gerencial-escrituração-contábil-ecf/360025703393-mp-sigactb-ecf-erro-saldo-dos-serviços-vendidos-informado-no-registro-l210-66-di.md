---
article_id: 360025703393
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 0eb6f2a11b71c257c61d25a97ba0bcaea49261cf6d2dbc2b6f0e73abf59f1192
fetched_at: '2026-06-28T22:40:48.987093+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: MP_SIGACTB ECF ERRO "SALDO DOS SERVIÇOS VENDIDOS INFORMADO NO REGISTRO L210
  (66) DIFERENTE DO CUSTO DOS SERVIÇOS VENDIDOS NO REGISTRO L300 .."
type: support-article
updated_at: '2021-04-28T22:10:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025703393-MP-SIGACTB-ECF-ERRO-SALDO-DOS-SERVI%C3%87OS-VENDIDOS-INFORMADO-NO-REGISTRO-L210-66-DIFERENTE-DO-CUSTO-DOS-SERVI%C3%87OS-VENDIDOS-NO-REGISTRO-L300
---

**Ocorrência**

4- VALOR - Saldo do custo dos servições vendidos informado no registro L210(66) Diferente do custo dos seerviços vendidos no registro L300 (3.01.01.03.01.03)  
  
Não gero o registro L200 nem o L210, porém o PGE acusa diferença de saldos entre o L210 e L300.![](https://totvssuporte.zendesk.com/attachments/token/j7mxOiNUjmJFMgXEBw4Y6vdUr/?name=inline1887666867.png)  
   
 **Ambiente**Protheus – Contabilidade Gerencial– A partir da versão 11.80  
   
 **Causa**Essa inconsistência na ECF ocorre porque o sistema leva o valor da conta do CMV para o registro L300 (DRE) na linha da conta do referencial configurado, geralmente no grupo 3.01.01.03 – Custo dos Bens e Serviços e esse valor é confrontado com a linha 66 do registro L210.

![](https://totvssuporte.zendesk.com/attachments/token/q8bSu8Ta3T9G9RXZt8bDeXyQv/?name=inline-1570936043.png)  
   
 **Solução**Se não há controle de Custo, registro L210, filho do registro L200, a conta contábil (CT1) não foi mapeada com a conta referencial correta (CVD).  O contador deverá rever a amarração das contas referenciais conforme características da conta. 

* Acessar a rotina Cadastro de plano de contas (CTBA020)  e verificar se a conta referencial amarrada esta de acordo com o seguimento da empresa (Serviços) .

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040561633/mceclip1.png)

* Acessar a rotina Visão gerencial (CTBA0161)  e verificar se a conta referencial amarrada esta de acordo com o seguimento da empresa (Serviços) .

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039731074/mceclip2.png)

* Utilize a visão gerencial de acordo com o seguimento da empresa

[Arquivos Modelos - Plano Referencial / Visões Gerenciais](http://tdn.totvs.com/pages/releaseview.action?pageId=189314312)

[MP - SIGACTB - CTBA161 /CTBA130 - Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)

[MP - SIGACTB - ECF - É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)

[MP\_SIGACTB\_ECF REGISTRO L210 É GERADO NO TXT POREM NÃO É EXPORTADO PARA O PGE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033735033-MP-SIGACTB-ECF-REGISTRO-L210-%C3%89-GERADO-NO-TXT-POREM-N%C3%83O-%C3%89-EXPORTADO-PARA-O-PGE?source=search)
