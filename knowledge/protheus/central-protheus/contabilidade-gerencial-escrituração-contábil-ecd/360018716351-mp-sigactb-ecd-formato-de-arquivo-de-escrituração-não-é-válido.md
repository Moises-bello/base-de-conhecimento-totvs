---
article_id: 360018716351
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 9312e1419e8462401b9bfd3e1706a99c1384e3c77182ef645d349dc49aa993bf
fetched_at: '2026-06-28T22:40:45.762710+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'MP - SIGACTB ECD: FORMATO_DE_ARQUIVO_DE_ESCRITURAÇÃO_NÃO_É_VÁLIDO.'
type: support-article
updated_at: '2021-04-28T22:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018716351-MP-SIGACTB-ECD-FORMATO-DE-ARQUIVO-DE-ESCRITURA%C3%87%C3%83O-N%C3%83O-%C3%89-V%C3%81LIDO
---

**Dúvida**FORMATO\_DE\_ARQUIVO\_DE\_ESCRITURAÇÃO\_NÃO\_É\_VÁLIDO.

![](http://tdn.totvs.com/download/attachments/342299686/erro_ecd.png?version=1&modificationDate=1519992064000&api=v2)

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução**

Para gerar a escrituração, é necessário que utilize o xml para este leiaute, e também, siga as instruções abaixo:

-No registro "0000" é necessário incluir 3 novos campos - Indicador de Situação Especial, Finalidade da Escrituração e o Código Hash. Com a inclusão destes 3 campos, o registro possuirá a seguinte estrutura:  
**|Código do Registro|Tipo de Leiaute|Data Inicial|Data Final|Nome/Razão Social|CNPJ|UF/Estado|Inscrição Estadual|Cód.Município|Inscrição Municipal|Indicador de Situação Especial|Finalidade da Escrituração|Código Hash|**-Para o registro "J930" será necessário incluir um único campo - Responsável pela Assinatura. Após esta inclusão, o registro ficará com a seguinte estrutura:   
**|Código do Registro|Nome do Signatário|CPF/CNPJ|Qualificação|Código de Qualificação do Assinante|CRC|Responsável pela Assinatura|**-Após importar o arquivo para o PVA, será necessário incluir manualmente o registro J801. Para sua inclusão, siga as orientações abaixo:  
  
1- Criar o termo de substituição em Word, salvando-o com a extensão .rtf;  
2- Importe o arquivo ECD gerado para o PVA;  
3- Após importá-lo, crie manualmente o registro J801 no PVA, e informe o arquivo .rtf no campo "Arquivo .RTF" - "Termo de Verificação".
