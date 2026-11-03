---
article_id: 360006878192
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: f9d46976f2d646cc878dc1617d963ebafc695c4331682f1ce552907d4174f940
fetched_at: '2026-06-28T22:40:47.432524+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - TAFOBRIG não aparece
  a Versão "108"
type: support-article
updated_at: '2022-06-20T20:04:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006878192-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-TAFOBRIG-n%C3%A3o-aparece-a-Vers%C3%A3o-108
---

**Ocorrência**

No módulo TAF ao acessar a rotina Central de Obrigações (TAFOBRIG) para gerar o arquivo do ECF, não aparece o Versão "108" referente ao layout 8.00 do ECF.

**Ambiente**Protheus - ECF - A partir da versão 11.80  
  
**Causa**

Esse incidente ocorre devido a atualização das Autocontidas do TAF de todas empresas.

**Solução**

**OBSERVAÇÃO [Importante]**O procedimento indicado abaixo deve ser realizado após o sistema está devidamente atualizado, conforme artigo:

[MP - SIGACTB - ECF - Como realizar a atualização do ECF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-MP-SIGACTB-ECF-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ECF-)

1. Limpe o conteúdo do parâmetro **MV\_VAUTCON**

2. Acesse o módulo **TAF (TOTVS Automação Fiscal)**

3. Acesse a rotina **Wizard de Configuração TAF (TAFLOAD)**

4. Execute o **Processamento** das Autocontidas para todas as empresas.

5. Após este procedimento aparecerá a opção "106" referente ao Layout 6.00 do ECF

![tafobrig.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067179334/tafobrig.png)

Verifique também se os parâmetros abaixo estão corretamente configurados:

MV\_TAFTALI = "Deve ser informado no nome do TOPALIAS do seu ambiente dentro do appserver.ini" 

MV\_TAFTDB = "Deve ser informado nome do banco do seu ambiente Exemplo MSSQL ou MSSQL7 informado no seu TOPBASE dentro do appserver.ini" 

MV\_TAFPORT = Indica o numero da porta do serviço do TopConnect 

MV\_TAFVER = Release corrente do TAF 

MV\_TAFWIZ =.T. (Em MAIÚSCULO)

MV\_TAFINT = .T. (Em MAIÚSCULO)
