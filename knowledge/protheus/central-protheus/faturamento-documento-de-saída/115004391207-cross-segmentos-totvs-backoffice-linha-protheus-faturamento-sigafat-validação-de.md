---
article_id: 115004391207
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 813b06e199858450b09659cb1fe92ae48cab450a8966526b691efe5f7eb3b5d2
fetched_at: '2026-06-28T22:38:44.200847+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Validação de exclusão do Documento de Saída com uso do JOB FATJOBNFE
type: support-article
updated_at: '2025-09-12T15:07:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004391207-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Valida%C3%A7%C3%A3o-de-exclus%C3%A3o-do-Documento-de-Sa%C3%ADda-com-uso-do-JOB-FATJOBNFE
---

**Ocorrência**

Exclusão do Documento de Saída - MATA521 com uso do JOB FATJOBNFE

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões

**Solução**

O JOB "**FATJOBNFE**" trata-se de uma funcionalidade que envia o cancelamento das NF's exigindo a consulta do Status de transmissão da Nota **(NFe - Modelo 55 / NFSe**), para então, permitir ou não a exclusão do Doc. de saída pela rotina **MATA521**. O uso do JOB evita que sejam excluídos do ERP documentos de saída que não estão aptos para o cancelamento junto ao SEFAZ.

**O suporte não orienta em implementação. Este material é unicamente objeto de apoio, e orientamos firmemente que seja solicitado analista inloco para implementar a ferramenta e homologar o uso em produção.**

A implementação deve ser realizada primeiramente em ambiente de homologação padrão atualizado e, posteriormente em Produção respeitando os devidos backups preventivos.

Para ativar o Job, caso possua apenas uma empresa e uma filial;

**1°** Configure o parâmetro MV\_CANCNFE ou MV\_CANNFSE ( para notas de serviços) = .T.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404650745879)

**2°** Configure o Job no appeserver.ini do Protheus para a execução do processo de cancelamento que foram emitidos por NFe ou NFSe.

[ONSTART]  
JOBS=FatJobNFe\_<empresa><filial>  
[FatJobNFe\_<empresa><filial>]   
MAIN=FatJobNFe  
ENVIRONMENT=<ambiente de trabalho>  
nParms=2  
parm1=<Empresa>  
parm2=<Filial>  
START\_TIME=00:00:01  
FINISH\_TIME=23:59:59  
INTERVAL=5  
ACTIVATE=ON

Caso tenha **mais de uma filial** ou **Gestão de empresas**, além do parâmetro ativado,  veja como deve ser configurado o JOB no appserver.ini. Siga as orientações do tópico ao lado:  **Configurações para mais de uma filial/ Gestão de empresas**

**OBSERVAÇÃO 1:** São as mesmas tags para nota de serviço, o que diferencia é o parâmetro **MV\_CANNFSE** que deve estar habilitado. Verifique se a prefeitura dispõe de serviço de cancelamento.

Caso contrario, indiferente do configurado no parâmetro de sistema MV\_CANNFSE não irá existir a transmissão para o cancelamento.

O fonte **UpdFATNFE.PRX** somente era necessário para o uso da **versão 11**, a partir da versão 12, não é mais necessário bastando apenas efetuar a configuração do ambiente.

**Saiba mais:**

**[FAT0191\_FATJOBNFE\_para\_Exclusão\_documento\_de\_Saída\_MATA521](https://tdn.totvs.com/pages/releaseview.action?pageId=272154294#FATJOB-FATJOB)**

**[MP - NFE - Como cancelar uma nota fiscal eletrônica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018751111-MP-NFE-Como-cancelar-uma-nota-fiscal-eletr%C3%B4nica-)**

**[MP - NFE - AUTONFE Transmissão, Monitoramento e Cancelamento Automáticos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029358971-MP-NFE-AUTONFE-Transmiss%C3%A3o-Monitoramento-e-Cancelamento-Autom%C3%A1ticos)**
